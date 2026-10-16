---
name: smallest-change
description: Apply when sizing a diff, refactoring, replacing an API, or tempted to add an abstraction, layer, option, or guard. Remove before adding, make the smallest change that solves the problem, and keep the code easy for the next reader to trace.
---

# Smallest change

Aim for less code, and code that is easier to read.

- **Subtract first.** Delete dead code, unused options, redundant validation, and stale references before building anything new. Build on the simpler base.
- **Make the smallest diff that solves the problem.** Three similar lines beat a premature abstraction. Don't add validators, options, or guards that the requirement doesn't ask for.
- **Remove layers that don't earn their place.** Inline a wrapper with one caller, an adapter with one implementation, or a layer that passes the same arguments straight through.
- **Keep state small.** Prefer return values to mutation, local variables to fields, and fields to module or global state. Derive a value instead of keeping two copies in sync.
- **Replace, don't run two versions.** When a new internal API replaces an old one, move every caller and delete the old API in the same change. Don't leave compatibility shims or parallel old and new paths unless external users depend on the old API.
- **Decide once.** If the same choice is made in several places, put it in one place and pass the result along.

**Check:** can a new reader answer "where does this value come from?" and "what can change it?" in under 30 seconds? If not, cut layers or cut state.
