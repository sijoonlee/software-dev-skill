---
name: update-skill-ground
description: Keep an app's feature map in `.skill-ground/feature-map/` in line with the code. Diff mode updates only what a branch or PR changed. Audit mode checks the whole map. Use after changing user-facing behavior, before opening a PR, or when asked to "update the feature map" or "audit the feature map".
---

# Update skill-ground

This skill keeps `<app>/.skill-ground/feature-map/` current. The **create-feature-map** skill creates it. If the map doesn't exist, stop and run that skill instead.

## Rules for both modes

- **Edit only `.skill-ground/`.** Never edit product code here. When the map and the code disagree, decide which is wrong:
  - **Doc drift.** The map describes the app wrong. Fix the map.
  - **Product regression.** The code no longer does what it should. Report it to the user and leave the map describing the intended behavior.
- **Check claims against the source.** Every entry point, code path, and gotcha you write must be something you saw in the code or the running app.
- **Keep the file shape.** Feature files keep their sections: Sub-features, How to get to it, Where it lives in code, Tests, Gotchas.

## Diff mode (default)

Use it for a branch, a PR, or the working tree. The default is the current branch against `main`.

1. **Read the diff.** `git diff main...HEAD` plus uncommitted changes.
2. **Map the changed files to features.** Use the "Where it lives in code" sections. A changed file that appears in no feature file is a candidate for a new or missing feature. Decide whether it's user-facing.
3. **Update.**
   - Changed feature: update its sub-features, entry points, code paths, tests, and gotchas.
   - New feature: add a file and an entry in the README index.
   - Removed feature: delete its file and its index entry.
   - Added or removed specs: update the Tests section.
4. **Check** that every path you added or changed exists.
5. **Report** the files updated, added, and removed, and any regressions. If nothing user-facing changed, say so and change nothing.

## Audit mode

Use it periodically or when the map feels stale. Run it only when asked for an audit.

1. **Index.** Every feature file is in the README, and every README entry has a file.
2. **Code pointers.** Every path in "Where it lives in code" and "Tests" still exists. Use `git log --follow` to find files that moved.
3. **Entry points.** Every route, menu item, endpoint, or command in "How to get to it" still exists in the source.
4. **Missing features.** Compare the current routes, menus, endpoints, and commands with the map. Add a file for each missing user-facing feature, and cite the source path that proves it exists.
5. **Outcome.** Report exactly one:
   - **clean.** Every feature was checked and nothing needed fixing.
   - **changed.** List the fixes. Put them all in one commit or PR that touches only `.skill-ground/`.
   - **blocked.** Say what stopped the audit and how far it got.

For a large app, spawn one read-only subagent per feature area to check code pointers and find drift from source. Then write the fixes yourself.
