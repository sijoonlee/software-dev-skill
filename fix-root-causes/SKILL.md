---
name: fix-root-causes
description: Apply when debugging a defect, or when a fix did not work. Reproduce first, trace the symptom back to the first wrong decision in the code, and fix it there. After two failed fixes, test the assumption they shared before trying a third.
---

# Fix root causes

The symptom is where a wrong state became visible. The root cause is the first place the code did something it should not, or failed to handle a state it should handle. Fix the root cause.

- **Reproduce first.** If it won't reproduce, narrow the conditions or add logging until it does. Don't fix a bug you haven't seen.
- **Use evidence, not guesses.** Read the actual error and the actual values. When the state is unclear, add logging and run the code. List the possible causes and rule them out one at a time, choosing each check to eliminate as many as possible.
- **Ask why until you reach a decision in the code**, not just a consequence of an earlier step.
- **Decide whether the bad state is legitimate.** If the system can validly be in that state, the code that broke on it is wrong, and handling the state there is the fix. If the state should never exist, a guard where it surfaced hides the bug. Find what produced it. Guards, retries, swallowed errors, and clamped values are the usual ways to hide a bug.
- **Ship only what the evidence supports.** A change that "might help" is a hypothesis, not a fix. If the evidence rules a hypothesis out, revert the code it motivated.
- **Fix the pattern, not just this instance.** Search for the same fault elsewhere.
- **After two failed fixes, question the assumption.** Write down the one sentence both fixes assumed. Find an observation that would come out differently if that sentence were false, and make it before writing a third fix.
- **If it fails only after a restart**, suspect persisted state first: caches, config files, lock files, saved data.

**Sign you skipped this:** the fix needs a long comment explaining why the workaround is necessary.
