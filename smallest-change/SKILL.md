---
name: smallest-change
description: Apply when deciding what the finished code should look like, especially when tempted to add code, an abstraction, a layer, an option, or a guard, or when replacing an API. Remove before adding, keep the diff as small as the problem allows, and leave code the next reader can trace. For the order of work and commits, use small-verified-steps.
---

# Smallest change

This skill is about the result: how much code there is and how easy it is to read. The order you do the work in is **small-verified-steps**.

- **Subtract first.** Delete dead code, unused options, redundant validation, and stale references before building anything new. Build on the simpler base.
- **Make the smallest diff that solves the problem.** Three similar lines beat a premature abstraction. Don't add validators, options, or guards that the requirement doesn't ask for.
- **Remove layers that don't earn their place.** Inline a wrapper with one caller, an adapter with one implementation, or a layer that passes the same arguments straight through.
- **Keep state small.** Prefer return values to mutation, local variables to fields, and fields to module or global state. Derive a value instead of keeping two copies in sync.
- **Replace, don't run two versions.** When a new internal API replaces an old one, move every caller and delete the old API. The finished code has no compatibility shims and no parallel old and new paths, unless external users depend on the old API.
- **Decide once.** If the same choice is made in several places, put it in one place and pass the result along.

**Check:** can a new reader answer "where does this value come from?" and "what can change it?" in under 30 seconds? If not, cut layers or cut state.
