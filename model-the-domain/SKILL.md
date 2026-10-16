---
name: model-the-domain
description: Apply when writing stateful logic, designing types or function signatures, wiring validation, or when code branches a lot or repeats the same shape assumption across files. Encode the domain in data structures and types, and validate only at system boundaries.
---

# Model the domain

Put the rules of the domain into data structures and types instead of spreading them across conditionals.

**Pick the structure**
- Use a state machine instead of several booleans that must stay in sync.
- Use a lookup table, registry, or discriminated union instead of an if/else chain that grows by one branch per feature.
- Use a typed model instead of loose parameters or the same shape assumption repeated in several files.
- Organize modules around a body of domain knowledge, not around steps like load, validate, and save.

**Make illegal states unrepresentable**
- `{ done: boolean; doneAt?: Date }` allows `done: true` with no date. Write `{ kind: 'open' } | { kind: 'done'; at: Date }` instead.
- Give IDs that mean different things different types, even if both are strings underneath.
- Handle every variant exhaustively, so that adding a variant makes the compiler point at each place that needs a new case.
- Every `as`, `any`, or non-null assertion marks a place where the type is too weak. Fix the type, or validate the value where it enters.

**Validate at the boundary, trust inside**
- Parse external input (HTTP, JSON, env, config, database rows, CLI args) into typed values where it enters the system.
- Inside the system, trust the types. Don't repeat null checks deep in the call chain.
- Keep business logic in pure functions with no framework dependencies, so it can be tested without the framework.

**Don't force it.** If the code is already clear, local, and unlikely to grow, leave it as plain code. An abstraction must delete branches, invalid states, or duplicated rules. Indirection alone is not a gain.

**Sign you skipped this:** a new feature added one more branch to an existing if/else chain, or added a second boolean that must stay in sync with the first.
