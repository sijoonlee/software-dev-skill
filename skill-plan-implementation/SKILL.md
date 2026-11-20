---
name: plan-implementation
description: >-
  Turn an egm-draft design and its supporting documents into a dependency-ordered
  implementation plan. Use after design drafting to map features, code entry
  points, shared foundations, buildable tasks, and acceptance checks through
  one-question-at-a-time discussion and independent plan review. Produces planning
  documents; does not implement application code.
---

# Plan Implementation

Use the resulting files from `egm-draft` as the design baseline. This is a
standalone follow-on skill: EGM does not need to be installed to run it. It follows
EGM's document construction and author approval approach, adding explicit rules
for ordering implementation questions and tasks.

The finished plan must answer: **What can I implement next, where do I start,
what must already exist, and how will I know it is done?**

## Applicability and boundaries

- Use for an existing design that needs an executable implementation plan,
  including a design whose implementation section is still too broad.
- Use for one feature or a coordinated collection of features. Scale the plan to
  the change; do not invent services, phases, migrations, or deployment systems.
- If the requested problem or architecture is still undecided, identify the
  specific missing design decision. Resolve that decision with the author or
  return to design drafting; do not silently create a different design.
- Inspect source and project guidance read-only. Write only requested planning
  artifacts. Do not edit production files, install dependencies, reset databases,
  commit, publish, or start implementation under this workflow.
- Source inspection and planning approval do not establish that checks passed.
  Distinguish a proposed command from a command actually executed.

## Working rules

1. **Design is the baseline.** Carry forward approved requirements, non-goals,
   interfaces and exceptions with source references. Do not re-ask settled choices.
   If code or a new request contradicts the baseline, explain the conflict and
   obtain the author's resolution before writing a conflicting plan.
2. **One question per interaction.** Read
   [question protocol](references/question-protocol.md) before the first question.
   Ask only the next unresolved impactful decision. Do not hide several decisions
   in one sentence, options list, or approval question.
3. **Author owns consequential choices.** Explain up to three defensible options
   with their mechanisms, trade-offs and failure conditions. Do not silently pick
   an architectural option or preselect a default. Honor explicit delegation from
   the author and record any delegated choice. Resolve routine mechanical details
   without a gate.
4. **Write artifacts as decisions settle.** Keep the full plan in files; chat
   contains a short explanation, a link, and at most one question. Save agreed
   changes before presenting the next question. Never interpret silence as approval.
5. **Review substance.** Challenge concrete gaps and failure cases, without forced
   disagreement, flattery or speculative complexity. Explain mechanisms in plain
   English. Do not require choices that are irrelevant to the approved scope.
6. **Maintain resumable state.** Record current stage/feature, approved sections,
   decisions, pending questions, blocked tasks and the next decision in the plan.
   On resume, read those records before asking anything new.

## Inputs and artifacts

Accept explicit paths to the final design or `design_draft.md`, related contracts,
decision records, and any existing implementation plan. Do not require a fixed
filename from EGM.

When paths are omitted, inspect the current project and its design/documentation
index. Prefer the design identified by the current conversation. If several are
plausible, ask which one; do not choose by filename date alone. If no design is
available, ask for its path rather than substituting a concepts brief as an
approved design. Supporting briefs can clarify intent but do not override design.

Use the user's output path. Otherwise place `implementation-plan.md` beside the
selected design. Resume an existing plan in that location rather than overwriting
it. Create a separate file or folder only if the existing artifact has another
purpose, the author requests it, or scale justifies it. Link details instead of
copying contracts into multiple competing documents.

Read [plan template](references/plan-template.md) before writing. It defines the
required information, not a demand for a separate document per section. Maintain
one navigation entry point if details span several files. Add
`implementation-review.md` beside the plan when independent review runs.

## Workflow

Follow these stages in order. Existing approved material can satisfy a stage:
reference it and assess gaps instead of restarting. Ask for approval when a new
stage's concrete artifact is ready, before moving to the next stage. Apply inline
comments before advancing. An explicit instruction to cover several stages
already authorizes that scope; do not repeatedly request the same permission.

### 1. Establish baseline and planning scope

Read the selected design, its governing references, project instructions and
relevant feature maps. Inspect the existing implementation section. Record the
source paths, status/version where available, approved scope and exclusions.
Distinguish current code from planned additions; use real entry points and label
proposed paths as proposed. Unknown generated filenames may be identified by
their generator and output directory rather than invented exact names.

Give a brief baseline confirmation with the files and scope identified. Ask one
question to confirm this baseline if the user's request did not already identify
it unambiguously. Then begin the artifact. Intake is not permission to implement.

### 2. Map features and end-to-end user flows

List observable capabilities and assign stable feature IDs. For each, connect:

**User action or system trigger → code entry point → governing contract → owning
modules/files → observable result and acceptance checks.**

Include actor, permission boundary, relevant failure states, what the feature
delegates, and where the neighboring feature takes over. Shared technical work
belongs in foundations, linked to the features it enables; do not present every
table or helper as a user feature.

Map design requirements/journeys to features so omitted scope is visible. Ask only
for missing feature boundaries that affect subsequent work. Persist the feature
map and obtain approval for its coverage before building the dependency sequence.

### 3. Resolve shared foundations and dependencies

Extract shared contracts, ownership, data changes, execution boundaries and other
prerequisites required by the approved design. Inspect code where it can answer a
question. Optional bounded sub-agent research follows
[delegation and review](references/delegation-and-review.md).

Build a directed dependency graph using feature/foundation IDs and reasons for
each edge. Order prerequisites before consumers. Resolve cycles by identifying a
missing shared prerequisite or an explicitly coordinated integration group. Never
pretend mutually dependent schema/runtime changes can activate independently.

Maintain a visible question queue using the question protocol. Resolve shared
decisions before asking consumers to choose details that depend on them. Independent
features may proceed while one feature remains blocked; keep that boundary visible.
Obtain approval for the foundations and dependency map.

### 4. Detail features into buildable tasks

Take the next dependency-ready feature and work through its flow end to end.
Reuse approved shared contracts. Resolve its remaining decisions before moving to
dependent features. Do not alternate unrelated database/API/UI trivia across the
project without explaining which feature and task it unblocks.

For each task, record the template's entry point, prerequisites, concrete change,
owned files and rationale, inputs/outputs, observable completion criteria and
focused verification. Include documentation, schemas, configuration and tests
when affected. Carry constraints through the whole request/data/rendering flow;
a file inventory alone is not an implementation plan.

Group tasks into checkpoints that can build and be verified. Separate mergeability
from activation if the design requires it. Each checkpoint must say what can run,
what remains inactive, and how integration is checked. For inseparable changes,
state the required combined checkpoint instead of adding compatibility machinery
that the author did not approve. Record file overlap before labeling tasks parallel.

Obtain approval for each completed feature's tasks, or a small explicitly grouped
set sharing one integration boundary. This approval replaces an additional
duplicative stage-4 gate. Do not ask for approval of every mechanical task.

### 5. Complete verification and integration

Trace every in-scope requirement to feature IDs, task IDs and an observable
acceptance check. Specify local commands, necessary fixtures/environment and
expected outcomes. Cover failure/concurrency/privacy states when the design makes
them material. Include UI evidence for changed user flows. Use existing test
mechanisms when suitable; do not require new frameworks or arbitrary coverage
percentages.

Document setup, activation, migration/reset/removal and rollback boundaries only
as applicable to the design. Preserve approved hard-reset/no-compatibility scope;
do not invent backup/recovery features. Identify external work and unavailable
checks as dependencies. Ask approval for this integrated verification plan.

### 6. Review, reconcile and hand off

Run an independent plan review under
[delegation and review](references/delegation-and-review.md). For a narrow plan,
one reviewer is enough; split coverage and execution-readiness only when each has
substantial independent scope. Reconcile findings into one report.

Fix mechanical omissions directly. Put unresolved consequential choices into the
existing question queue and ask the author one at a time. Never call a blocked
task ready. Recheck the final plan against the baseline and decision log; report
any design departure for author resolution instead of changing the design.

After review, show a short linked description of what is ready, what is blocked,
and the next implementable task/checkpoint. Ask one final approval question if
final approval has not already been given. Mark ready only after the author
approves and no blocking decisions/review findings remain. A scoped subset can be
ready while the larger plan remains explicitly partial. Handoff does not start
implementation or create a PR.
