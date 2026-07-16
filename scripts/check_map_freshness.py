#!/usr/bin/env python3
"""
check_map_freshness.py — deterministic capability-map freshness gate.

Fails (exit 1) when a change touches code owned by a capability but leaves that
capability's map entry stale: the capability's `lastVerifiedSha` predates the
change AND neither its map directory nor its watermark was updated in the same
change. In other words: you moved a capability's code without reconciling its map.

This is the ENFORCEMENT half of map freshness — it detects and blocks drift; it
does NOT fix it. The fix is the `map-reconcile` skill. Enforcement is a script
(the answer is computable) so it can't be forgotten and runs on every push.

Reads the freshness substrate the bootstrapper/steward maintain:
  project-context/coverage-ledger.json   (surface item -> capability)
  project-context/capabilities.json      (per-capability lastVerifiedSha)

Usage (typically in CI on a PR):
  check_map_freshness.py --base origin/main --head HEAD [--project-context project-context]

Exit codes: 0 = fresh (or nothing relevant changed); 1 = stale capability found;
2 = misconfig (missing artifacts / git error). Reference implementation — adapt the
path-matching to your repo layout.
"""
import argparse, json, subprocess, sys, os


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def changed_files(base, head):
    out = git("diff", "--name-only", f"{base}...{head}")
    return [line.strip() for line in out.splitlines() if line.strip()]


def is_ancestor(maybe_ancestor, ref):
    # True if `maybe_ancestor` is an ancestor of `ref` (i.e. the watermark is at or
    # behind ref — the capability was NOT re-verified at/after this change).
    r = subprocess.run(["git", "merge-base", "--is-ancestor", maybe_ancestor, ref])
    return r.returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--head", default="HEAD")
    ap.add_argument("--project-context", default="project-context")
    args = ap.parse_args()

    pc = args.project_context
    ledger_path = os.path.join(pc, "coverage-ledger.json")
    caps_path = os.path.join(pc, "capabilities.json")
    if not (os.path.exists(ledger_path) and os.path.exists(caps_path)):
        print(f"::error:: missing {ledger_path} or {caps_path} — run the bootstrapper first", file=sys.stderr)
        return 2

    ledger = json.load(open(ledger_path))
    caps = json.load(open(caps_path))
    # capabilities.json may be a list or {"capabilities":[...]}; normalize.
    cap_list = caps["capabilities"] if isinstance(caps, dict) else caps
    watermark = {c["id"]: c.get("lastVerifiedSha") for c in cap_list}

    try:
        changed = changed_files(args.base, args.head)
    except subprocess.CalledProcessError as e:
        print(f"::error:: git diff failed: {e}", file=sys.stderr)
        return 2

    # Resolve changed code files to capabilities via the ledger (longest-prefix match).
    entries = sorted(ledger.get("entries", []), key=lambda e: len(e["item"]), reverse=True)
    affected, unmapped = {}, []
    for f in changed:
        if f.startswith(pc + os.sep):          # map edits themselves aren't "code"
            continue
        if not f.startswith("src"):            # adapt: which trees are "capability code"
            continue
        hit = next((e for e in entries if f == e["item"] or f.startswith(e["item"].rstrip("/") + "/")), None)
        if hit is None:
            unmapped.append(f)
        elif hit.get("capability"):
            affected.setdefault(hit["capability"], []).append(f)

    stale = []
    for cap, files in affected.items():
        wm = watermark.get(cap)
        map_dir_touched = any(f.startswith(os.path.join(pc, "capabilities")) and cap in f for f in changed)
        caps_json_touched = caps_path in changed  # watermark could have advanced here
        # Stale if the code moved past the watermark and the map wasn't updated for it.
        moved_past = (wm is None) or is_ancestor(wm, args.base)
        if moved_past and not (map_dir_touched or caps_json_touched):
            stale.append((cap, files))

    ok = True
    for cap, files in stale:
        ok = False
        print(f"::error:: {cap} code changed but its map entry is stale "
              f"(lastVerifiedSha behind this change, map not updated). "
              f"Run map-reconcile. Files: {', '.join(files[:5])}"
              + (" …" if len(files) > 5 else ""))
    if unmapped:
        # Not a hard failure by default — a changed file under no capability is a
        # possible discovery gap. Surface it; flip to a failure if your policy is strict.
        print(f"::warning:: {len(unmapped)} changed file(s) map to no capability "
              f"(possible new/expanded capability): {', '.join(unmapped[:5])}"
              + (" …" if len(unmapped) > 5 else ""))

    if ok:
        print("map freshness: OK")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
