# Question selection and interaction

Read before asking the first planning question. The purpose is to resolve the
next consequential unknown without turning planning into an unbounded interview.

## The queue

Maintain one queue in the plan with:

| ID | Feature/task | Decision needed | Source or gap | Depends on | Blocks | State / answer reference |
| --- | --- | --- | --- | --- | --- | --- |

Use states `open`, `waiting-on-dependency`, `resolved`, or `deferred`. A deferred
impactful choice blocks its affected task; writing “decide during implementation”
does not make the task ready. Preserve resolved rows or link their decision-log
entries so future sessions do not repeat them. Do not dump the queue into chat as
a questionnaire.

Before adding a question:

1. Check the design, existing decisions and code. Cite the answer if one exists.
2. Determine whether different answers change behavior, ownership, compatibility,
   interfaces, dependencies, verification or the ability to deliver the task.
3. If not, handle the mechanical detail yourself or leave ordinary coding latitude.
4. If so, record the specific decision and what it blocks.

## Choosing the next question

Apply this order, skipping settled or inapplicable items:

1. Resolve a direct contradiction or scope/baseline ambiguity affecting the current
   work. A contradiction is not a reason to reopen every approved decision.
2. Resolve a shared prerequisite blocking multiple features before its consumers.
3. Choose a feature whose prerequisites are settled, following dependency order.
   For equally ready features, prefer the one unblocking more downstream work;
   otherwise retain the documented feature order.
4. Within that feature, follow the user/system flow: missing actor/outcome rules,
   entry-point contract, state/ownership, cross-component interactions, then
   failure cases and acceptance checks. Move a prerequisite earlier whenever a
   later answer would invalidate an earlier question.
5. Finish that feature's consequential decisions and task approval before moving
   to a dependent feature. Independent work may continue if a blocker is deferred.

This is dependency ordering, not a universal “database before API before UI” rule.
For example, whether draft edits are visible to learners must be settled before
choosing an API response that would expose them. A known design decision about
draft visibility should be cited, not asked again.

When the author steers to another topic, answer it and preserve the queue. Explain
any unresolved prerequisite before asking its dependent question. Update prior
decisions only when the author explicitly changes them; record affected tasks.

## Presenting the question

Briefly name the current feature/stage and say what the decision unblocks. Ask
exactly one decision. Offer up to three substantive options when alternatives
exist. Explain each option's mechanism, trade-off, and relevant failure condition.
Avoid multiple alternatives differing only in wording. Do not rank or preselect
an architecture option unless the author has asked you to recommend or choose.

Use a supported single-select question tool when its schema and current mode
permit the interaction. Otherwise ask in plain chat. Follow higher-priority host
requirements for option formatting; never invent a tool or treat a preselected
choice as a submitted answer. If a tool requires a default that would misrepresent
an undecided author choice, use plain chat instead.

The gate is the final action of the turn: perform relevant reads and save settled
decisions before asking; do not run more tools or start dependent work afterward.
This allows the artifact-first update and a question in the same turn. There is
one interactive gate, not a rule banning the file write preceding that gate.

If asked to explain, explain the current question without advancing the queue.
If an answer is ambiguous, ask one clarification. If the author explicitly asks
you to choose, make and explain the delegated choice rather than repeating the
same gate indefinitely. A requested recommendation is not approval of it.

## Approval gates

Approve concrete, linked artifacts. Name the section/feature, mention the few
material additions, and ask one approval question with choices to approve and
continue or request changes. Do not combine approval with an unresolved design
choice. Resolve that choice first.

Apply supplied comments before advancing. If the author requests revisions but
provides neither text nor accessible comments, ask what should change and wait.
Do not loop empty approval prompts. Existing explicit approval remains valid
until a material change affects the approved scope; seek reapproval only for that
changed portion.

If approval gates are required by this skill and the author questions a pause,
link the relevant SKILL.md stage, explain that requirement, and distinguish it
from your own interpretation. Honor explicit user changes to the workflow.
