---
name: small-verified-steps
description: Apply when work takes more than one step, such as a migration, a sweep of similar edits, or a multi-file refactor, and when organizing commits. Do one change at a time, check it before the next, and order commits so they explain the change. For what the finished code should look like, use smallest-change.
---

# Small verified steps

This skill is about the order of work. What the finished code should look like is **smallest-change**.

Break the work into small units. Each unit ends in a state you can check. Don't start the next unit until the current one passes.

**While working**
- Each unit goes like this: a known-good state, one change, run the check, then move on. A failure caught at the unit that caused it is cheap to find. A failure found after ten changes is not.
- For a refactor, pin the current behavior first, using an existing test, a characterization test, or an output snapshot. Keep it green after every step. A type check and lint do not count as a pin.
- When a change repeats across many places, write a script or codemod after doing the first one by hand. Check the script against your hand-made version, then run it on the rest. A reviewer can rerun the script instead of rechecking every edit.
- Run the check for each unit even when it seems obvious.

**Breaking things on the way**
In a migration you may leave intermediate states broken on purpose, rather than writing temporary code to keep every step working. Say which steps are broken and why, keep the checks for the code you're touching, and run every check at the end.

**When delivering**
- Order commits so the history explains the change: a failing test, then the fix, or the removals smallest-change asks for, then the new code, or setup, then the feature.
- Each commit should build and pass on its own, unless it's part of a planned broken stretch.
- Keep each commit to one purpose. Split unrelated cleanups into their own commits.
