---
name: prove-it-works
description: Apply before declaring a task done, when writing or keeping a test, or before reporting a measured number such as a speedup or regression. Verify against the real running thing, write tests that assert observable behavior, and explain what limits any number you report.
---

# Prove it works

Check the real thing directly. "It compiles", "the tests pass", and a subagent's report are not proof that the change works.

**Verify on the real artifact**
- Run the feature where the user would see it: the page, the endpoint, the CLI. Verify a bug fix the same way you reproduced the bug.
- Read the actual value, not a cached or derived copy of it.
- When a check passes too easily, or fails strangely, suspect the check before the system.
- "Inconclusive" is not a pass. Say so.
- Prefer a script anyone can rerun over a one-time look. Keep its output for the reviewer.

**Test behavior, not implementation**
- Assert what callers can observe: return values, errors, saved state, requests sent, messages emitted.
- Don't assert private helpers, internal call order, or which internal function did the work.
- Judge each test with two imagined edits. If you break the behavior and the test still passes, the test proves nothing. If you restructure the internals and the test fails, it is tied to the implementation. Keep tests that pass both checks.
- Derive the expected value from the requirement, not by running the code.
- For a bug with a cheap test path, write the failing test first, watch it fail for the right reason, then fix it. If a good test would be expensive or flaky, use a targeted repro script instead. No test is better than a bad test.

**Explain the number**
- Before you report a measured number, name what limits it, such as CPU, a lock, I/O, the network, or the benchmark tool itself.
- Rule out the usual false results: errors, cached or skipped work, code that never ran, an untuned baseline, and noise.
- Report the number of runs and the spread together with the number.
