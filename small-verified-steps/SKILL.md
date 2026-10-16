---
name: small-verified-steps
description: Apply to multi-step work such as migrations, sweeps, runs of similar edits, or a refactor, and when organizing commits and PRs. Work in small units that each end in a check, and order commits so they tell the story of the change.
---

# Small verified steps

Break the work into small units. Each unit ends in a state you can check. Don't start the next unit until the current one passes.

**While working**
- Each unit goes like this: a known-good state, one change, run the check, then move on. A failure caught at the unit that caused it is cheap to find. A failure found after ten changes is not.
- For a refactor, pin the current behavior first, using an existing test, a characterization test, or an output snapshot. Keep it green after every step. A type check and lint do not count as a pin.
- When a change repeats across many places, write a script or codemod after doing the first one by hand. Check the script against your hand-made version, then run it on the rest. A reviewer can rerun the script instead of rechecking every edit.
- Run the check for each unit even when it seems obvious.

**When delivering**
- Order commits so the history explains the change. Typical orders are a failing test then the fix, a removal then the reshape, or setup then the feature.
- Each commit should build and pass on its own.
- Keep each commit to one purpose. Split unrelated cleanups into their own commits.

**Planned breakage.** In a planned migration you may break intermediate states on purpose, instead of writing throwaway compatibility code. Say where things are broken, and fully verify everything at the end.
