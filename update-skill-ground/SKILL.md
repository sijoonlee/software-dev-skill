---
name: update-skill-ground
description: Keep an app's `.skill-ground/` (feature map and verify skill) in line with the code. Diff mode updates only what a branch or PR changed. Audit mode checks the whole map and drives every feature live. Use after changing user-facing behavior, before opening a PR, or when asked to "update the feature map", "update the verify skill", or "audit skill-ground".
---

# Update skill-ground

This skill keeps two things current in `<app>/.skill-ground/`:

- `feature-map/`, one file per feature (from the **create-feature-map** skill)
- `verify/SKILL.md`, how to launch, check, drive, and clean up the app (from the **create-verification-skill** skill)

If either is missing, stop and run the matching create skill instead.

## Rules for both modes

- **Edit only `.skill-ground/`.** Never edit product code here. When the map and the code disagree, decide which is wrong:
  - **Doc drift.** The map or the verify skill describes the app wrong. Fix it.
  - **Harness gap.** The app works but the verify steps can't drive it. Fix the verify skill.
  - **Product regression.** The app is broken. Report it to the user and leave the map describing the intended behavior.
- **Prove by driving.** A change to "How to get to it", "Driving it", or the verify skill's Launch, Doctor, or Drive sections counts only after you've run it against the app. Follow the verify skill's own Launch, Doctor, and Cleanup steps.
- **Keep the file shape.** Feature files keep their sections: Sub-features, How to get to it, Where it lives in code, Driving it, Gotchas.

## Diff mode (default)

Use it for a branch, a PR, or the working tree. The default is the current branch against `main`.

1. **Read the diff.** `git diff main...HEAD` plus uncommitted changes.
2. **Map the changed files to features.** Use the "Where it lives in code" sections. A changed file that appears in no feature file is a candidate for a new or missing feature. Decide whether it's user-facing.
3. **Check whether the verify skill is affected.** Changes to dev scripts, ports, env vars, seed data, auth, or the test setup can break Launch, Doctor, or Drive.
4. **Update.**
   - Changed feature: update its sub-features, entry points, code paths, and gotchas.
   - New feature: add a file and an entry in the README index.
   - Removed feature: delete its file and its index entry.
   - Changed launch or login: update the verify skill.
5. **Drive each affected feature once** with the updated steps, and capture evidence. If a step fails, classify it using the rules above.
6. **Report** the files updated, added, and removed, what you drove and the evidence, and any regressions. If nothing user-facing changed, say so and change nothing.

## Audit mode

Use it periodically or when the map feels stale. Run it only when asked for an audit.

1. **Index.** Every feature file is in the README, and every README entry has a file.
2. **Code pointers.** Every path in "Where it lives in code" still exists. Use `git log --follow` to find files that moved.
3. **Missing features.** Compare the current routes, menus, endpoints, and commands with the map. Add a file for each missing user-facing feature, and cite the source path that proves it exists.
4. **Live pass.** Launch the app and run Doctor. Drive every feature at least once, following the README's sweep order. Run Doctor again after any failed drive before you continue. A feature you can't reach is "unreachable" only when you name the concrete precondition (account, flag, external service) and what you tried. If the map doesn't mention that precondition, add it to Gotchas.
5. **Clean up** with the verify skill's own steps. Confirm the evidence survived.
6. **Outcome.** Report exactly one:
   - **clean.** Every feature was checked and nothing needed fixing.
   - **changed.** List the fixes. Put them all in one commit or PR that touches only `.skill-ground/`.
   - **blocked.** Say what stopped the audit and how far it got.

For a large app, spawn one read-only subagent per feature area to check code pointers and find drift from source. Do all the live driving yourself, in one session, so instances don't collide.
