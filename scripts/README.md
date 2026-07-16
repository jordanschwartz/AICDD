# AICDD scripts

## check_map_freshness.py — the freshness enforcement gate

Deterministic CI check that blocks a change from merging if it moves a capability's
code without reconciling that capability's map entry. It's the enforcement half of
map freshness: it **detects and blocks** drift; the **fix** is the `map-reconcile`
skill.

Why a script (not a skill): the answer is computable — "did a capability's code
change past its watermark without its map being updated?" — so it's computed, not
reasoned about, and it runs on every push so nobody has to remember.

It reads the substrate the `bootstrapper`/`steward` maintain:
`project-context/coverage-ledger.json` and the per-capability `lastVerifiedSha` in
`project-context/capabilities.json`.

### Wire it into CI (GitHub Actions example)

```yaml
- name: Capability map freshness
  run: |
    python3 path/to/aicdd/scripts/check_map_freshness.py \
      --base "origin/${{ github.base_ref || 'main' }}" --head HEAD
```

Exit 0 = fresh, 1 = a stale capability was found (fix with `map-reconcile`), 2 =
misconfig (run the bootstrapper first). It's a **reference** — adapt the path
matching (`src`, `project-context`) to your repo layout, and decide whether an
unmapped changed file (a possible new capability) should warn or hard-fail per your
policy.
