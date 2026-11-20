# Implementation plan information model

Use this structure as an information checklist. Keep small plans in one file.
For a large plan, keep a linked navigation index and give each detailed contract
one authoritative home. Do not produce empty sections for inapplicable concerns.
Templates below describe fields to fill; they are not literal draft content.

## Baseline and state

- Design and governing contract links, relevant revision/status and scope.
- Current source revision when available, plus material uncommitted source changes
  observed during inspection. Do not claim a clean checkout without checking.
- Planning status: drafting, blocked, ready-for-approval, approved, or partial.
- Current stage and feature, approved sections, next decision and next executable
  task/checkpoint. Preserve this state across compaction and handoff.
- Non-goals and existing author exceptions affecting implementation.

## Feature map

| Feature ID | Actor/trigger and outcome | Entry point | Governing source | Owning modules | Prerequisites | Acceptance checks | Task IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |

Describe each feature's main flow and relevant alternate/error states below the
table. Identify inputs, outputs, permission boundaries, and where it delegates.
Entry points can be routes, commands, event handlers or exported module functions.
Mark newly proposed entry points explicitly. Foundation rows must name consumers.

## Shared foundations and dependency order

| ID | Shared responsibility/contract | Consumers | Prerequisites and reasons | Owning modules/files |
| --- | --- | --- | --- | --- |

Provide an ordered feature/foundation list or graph. Every dependency must have a
concrete reason. Explain coordinated integration groups and activation rules.
Record remaining cycles as blockers instead of publishing an impossible order.

## Decisions and questions

Decision record fields: ID, decision, rationale, design/source or author approval,
affected features/tasks, and superseded decision if any. Keep current decisions
distinct from historical alternatives.

Include the queue defined in [question protocol](question-protocol.md). The queue
is an index; do not duplicate long contracts in it. Link design departures and
their explicit resolution.

## Tasks by feature, in dependency order

Use stable task IDs. For each task include:

- **Feature and outcome:** which capability this task delivers or enables.
- **Start here:** the actual or proposed code entry point and what to read first.
- **Prerequisites:** task/foundation IDs and the specific contracts or artifacts
  they provide. Explain any external dependency.
- **Concrete changes:** implementation behavior, inputs/outputs, state transitions
  and cross-module interaction sufficient to avoid new consequential choices.
  Reference exact approved schemas/contracts rather than paraphrasing them.
- **File ownership:** every known file to create/modify/delete and why. Include
  related tests/docs/config when affected. For generated files specify generator,
  output location, and review expectations; do not guess generated names.
- **Completion criteria:** observable assertions that establish this task is done.
- **Verification:** exact known commands/checks, fixtures, environment and expected
  outcomes. Label proposed commands/scripts that a preceding task must implement.
- **Integration/activation:** checkpoint membership and anything that must remain
  inactive until consumers are changed. Cite the governing design constraints.
- **Readiness:** ready when prerequisites land, blocked with question/dependency
  IDs, or complete only if implementation evidence actually exists.

For a very small task, combine related fields in prose. Do not replace concrete
behavior with “wire up,” “handle errors,” or “add tests.” Ordinary local coding
choices need not be dictated; impactful unanswered decisions must be explicit.

## Buildable checkpoints

| Checkpoint | Tasks | Prerequisites | What builds/runs | Integration acceptance | Activation boundary |
| --- | --- | --- | --- | --- | --- |

Tasks grouped by feature are the navigation view. Checkpoints are the execution
view and may coordinate multiple features. Reference task IDs in both without
duplicating task bodies. Keep foundation work and consumers in one checkpoint
when neither is valid independently under the approved design.

If parallel implementation is useful, name disjoint ownership or the explicit
integration owner for overlapping files. Independence of product behavior alone
does not imply safe parallel writes to the same file.

## Acceptance and integration

| Design requirement/journey | Feature | Tasks/checkpoint | Observable acceptance and verification |
| --- | --- | --- | --- |

Cover every in-scope requirement and material invariant, including failure modes
that cross feature boundaries. Record setup/fixtures and test isolation needed
to reproduce checks. For UI work identify the interaction and screenshot/recording
evidence required, without claiming that evidence already exists.

Document migration, reset, removal, activation and rollback only where applicable.
If reset is the approved recovery policy, give its task/command ownership rather
than inventing a data-preserving rollback. If a command needs an unavailable
service, identify that limitation and whether it blocks readiness or execution.

## Review and handoff

Link the consolidated review report and unresolved issues. Name the next task or
combined checkpoint and its entry point. Mark the whole plan approved only when
scope, dependencies, concrete tasks and checks are accepted and blocking decisions
are resolved. If only a subset is ready, explicitly bound that subset.

Check that each in-scope requirement is covered, each non-foundational task has a
valid prerequisite chain, every listed file has an owner, and all claimed checks
are distinguishable from planned checks. Do not begin implementation from the
handoff unless the author separately requests it.
