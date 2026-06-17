Use the Engineering Lead role to create the implementation team and assignments.

The initiative is located at:

initiatives/2026-001-pre-shift-assignment-display/

Read:

- execution-plan.md

Based on the execution plan, generate:

- assignments.md

Your job is to determine the appropriate implementation team composition and assign execution tasks accordingly.

Instructions:

- Infer the needed agent roles from the execution plan.
- Create the smallest effective agent team.
- Assign every execution task to exactly one agent.
- Respect all task dependencies.
- Maximize safe parallel execution.
- Keep tightly related tasks together.
- Avoid unnecessary coordination overhead.
- Do not modify the execution plan.
- Do not decompose tasks further.
- Do not redesign the solution.

For each agent, include:

- Agent name
- Role / specialty
- Assigned task IDs
- Dependencies to wait for
- Implementation focus
- Expected output

Use this format:

# assignments.md

## Agent 1 — Backend / Sync

Assigned Tasks:
- Task 1
- Task 2

Waits For:
- None

Focus:
- Hydrate cloud-filled shift assignments into local POS data.

Expected Output:
- Code changes
- Tests
- Implementation summary

---

## Agent 2 — POS UI

Assigned Tasks:
- Task 3

Waits For:
- Task 1

Focus:
- Display assigned employee on the Pre-shift Planning screen.

Expected Output:
- Code changes
- Tests
- Implementation summary

---

## Agent 3 — Integration / Verification

Assigned Tasks:
- Task 4

Waits For:
- Task 1
- Task 2
- Task 3

Focus:
- Validate sync-to-UI behavior and regression coverage.

Expected Output:
- Tests
- Verification notes
- Implementation summary