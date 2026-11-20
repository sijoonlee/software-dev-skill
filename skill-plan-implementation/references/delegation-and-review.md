# Bounded research and independent review

Read before delegating or reviewing. The main agent owns the plan, decision
queue, author interaction and reconciliation. Sub-agents do not approve the plan
or independently change architecture.

## Code research

Use sub-agents when independently inspecting several substantial code areas
would reduce uncertainty. Skip delegation for facts a small local read resolves.
Each research assignment has a bounded question, explicit paths and a read-only
scope. Ask for entry points, current contracts, file ownership and evidence with
paths/lines, separating facts from proposals. Inspect every result before using
it. Never delegate the author's decision or ask the user parallel questions.

Researchers return findings to the main agent; they do not write competing plans
or modify source. Parallelize disjoint reads, not dependent choices or edits.
Planning sub-agents do not run migrations, install packages or exercise services
with side effects. If a fact needs such verification, record the future check or
seek authorization through the normal task boundaries.

## Fresh-context review

Use native sub-agent tools with conversation inheritance disabled (`fork_turns:
"none"` or the host's equivalent). Pass absolute paths to this reference, the
plan, governing design/decision documents, and relevant project guidance/source.
Include only the minimum reading list needed for the review; do not include the
parent's conversation, private reasoning or an explanation supplying answers
missing from the plan. Decision records needed by an implementer must be linked
from the plan and available to the reviewer.

Require reviewers to read the listed inputs. A missing read, tool failure or
timeout is an incomplete review, not a clean result. Wait for actual completion.
If native delegation is unavailable or cannot establish separate conversation
context, state the limitation. A self-check may be recorded as a self-check, never
as independent review. Do not make the plan's scope impossible merely because
independent tooling is absent; report the review limitation in the handoff and
let the author decide whether to accept it.

One reviewer normally covers both lenses below. For a large plan, two reviewers
may work independently, one per lens; do not launch a fixed EGM five-stage panel.

### Design coverage and alignment

- Trace in-scope behavior, permission boundaries and material invariants from the
  design to feature/task/acceptance IDs. Identify missing or expanded scope.
- Check that tasks preserve approved exceptions and distinguish current decisions
  from historical alternatives. Do not reopen explicit author choices merely
  because another architecture could work.
- Check cross-feature behavior, including ownership of handoffs and shared state.

### Execution readiness

- Try to choose the first implementation task, locate its entry point, follow its
  prerequisites and determine what observable check completes it.
- Repeat for downstream checkpoints. Find missing prerequisites, cycles, undefined
  interfaces, duplicate file ownership, and changes that cannot build/activate in
  the stated order. Check schema/runtime cutovers as combined units when required.
- Identify only consequential decisions left to an implementer, rather than
  asking the plan to prescribe every helper or local variable.
- Check realistic command/environment/fixture ownership and failure paths. Planned
  checks must not be presented as executed evidence.

## Findings and one report

Reviewers return findings to the main agent without writing files. Each finding
contains severity (`blocker` or `major`; omit style nits), feature/task or file/line
evidence, the concrete missing/contradictory contract, why execution is affected,
and the decision or correction needed. A clean result must identify what was read
and checked. Do not count absent optional sections as defects.

The main agent writes one `implementation-review.md` with reviewed inputs,
completed/incomplete reviewer status, deduplicated findings, dispositions and
remaining blockers. Rejected findings need a reason tied to the design or code.
Mechanical corrections can be applied directly. Author choices return to the
single question queue before the plan changes.

Re-review affected changes rather than restarting unrelated reviews. After at
most three review rounds, report remaining issues and stop cycling. Never label
unresolved blockers clean. A report can document partial readiness; independent
review alone never supplies the author's final approval.
