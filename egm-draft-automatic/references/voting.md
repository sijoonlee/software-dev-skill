# Three-voter decision protocol

## Prepare one decision packet

The main agent gathers evidence and writes a versioned packet under
`draft-decisions/<decision-id>/round-<n>-packet.md`. Every voter receives that
same saved version. Do not edit it while the round is running.

Include:

- Decision ID, round, question, and affected section/version.
- Goal, applicable user requirements, and non-goals.
- Shared decision criteria and established company principles. Do not invent
  priorities or weights on behalf of the user. If trade-offs depend on an
  unknown preference, state that gap.
- Normally two or three named choices with stable IDs. Explain each mechanism,
  benefits, costs, and failure conditions neutrally; do not mark a preferred
  answer. Abstention and rejection are always available in addition to choices.
- Observed facts, estimates, and unknowns, separated explicitly.
- Mandatory evidence paths and relevant excerpts with provenance. Identify
  optional sources separately. For a section check, save the exact section
  snapshot or full draft version being evaluated, not a moving target.
- Earlier applicable decisions, their authority (explicit user requirement or
  provisional agent decision), and status. Supply established outcomes and
  evidence, not the main agent's private reasoning or earlier individual votes.
- The four consequence questions: impact area, ending event, rebuild sources
  and retention, discovery point. Include harm before reversal.

Voters may inspect the same selected sources and point out a missing option.
The main agent's framing is itself challengeable. Do not manufacture choices
about facts that should instead be verified by reading code or evidence.

## Dispatch and collect

Launch the bundled Practicality, Consequences, and Fitness personas in fresh
contexts using the host integration instructions. Each evaluates every choice
and returns the output required by its persona, including one vote, a strongest
objection, consequences, and missing evidence. No voter sees another voter's
response before submitting its own.

Save each native returned report verbatim under the decision directory as
`round-<n>-<role>.md`, together with its completion/read status. If a voter fails,
times out, or cannot read mandatory input, mark its vote unavailable. Retry that
role once in a new context against the identical packet. A failure is not an
abstention and does not count as support for any option. After a second failure,
record the infrastructure blocker; do not declare a majority from an incomplete
panel. Do not silently substitute a role. If the packet changes, invalidate the
whole round and rerun all three voters within the original question's round cap.

## Determine the result

Require three completed, input-complete reports before tallying. An explicit
abstention caused by insufficient evidence is a valid completed report; failing
to read a mandatory source is not.

| Reports | Result |
|---|---|
| At least two select the same eligible choice | Provisional majority for that choice, subject to the checks below |
| Two or three reject all choices | Reframe options; no selected design |
| Two or three abstain | Identify missing evidence or preference; no selected design |
| Three different choices, or no choice has two votes | No majority; follow the bounded resolution path |
| A report is unavailable after its retry | Infrastructure blocker; no majority declared |

Before applying a majority:

1. Check material claims against cited evidence, including minority findings.
2. Exclude a choice that verifiably violates an explicit hard constraint. A
   majority cannot waive that constraint. If eligibility changes, issue a new
   packet and rerun rather than transfer votes to another choice.
3. Investigate a credible but unverified hard-constraint concern or a material
   evidence gap that could invalidate the result. Do not treat every speculative
   risk as a veto, and do not treat a missing user preference as majority consent.
4. Preserve ordinary trade-off dissent without requiring unanimity. Explain why
   it does or does not change the next step.

Record results in `round-<n>-result.md`: packet and report paths, per-role votes,
counts, result status, evidence checks, dissent, conditions, affected sections,
and next action. Explicitly label the outcome `provisional agent decision`.
A later reversal gets a new record linking the superseded decision.

## Resolve disagreement without unlimited revoting

Use at most three evaluation rounds per original question unless the user
supplies another limit. Intake, section checks, and architecture choices all
use this bound. Renaming or splitting the same unresolved question does not
reset its limit. A failed-voter retry is allowed once per role per round; it is
not a new evaluation round.

After no majority, rejection, abstention, or a majority blocked by evidence:

1. Diagnose whether the disagreement concerns facts, conflicting priorities,
   omitted choices, or consequences of being wrong. Do not assume consensus
   improves simply by asking the same question again.
2. Verify missing facts with targeted read-only investigation. Reframe an
   omitted alternative when warranted. Version the packet and rerun all three
   voters only if the evidence or choices materially changed.
3. If failure would be cheap, contained, and reversible, propose the smallest
   experiment that could distinguish the choices, with a success criterion and
   stop condition. The agents may vote on that next step. This design-only
   workflow records experiments requiring implementation or external actions;
   it does not carry them out. Authorized read-only probes may gather evidence.
4. If failure would be costly, persistent, or hard to detect, prioritize evidence
   addressing that consequence. A best practice is useful evidence only when
   its assumptions fit; it is not an automatic tie-breaker.
5. If choices are materially equivalent, offer a stated tie-breaker such as
   simpler implementation or easier reversal in a revised packet. Do not let
   the main agent silently cast a deciding fourth vote.
6. Unknown user preferences stay unresolved. Ask one concise question only when
   necessary, or record the blocker if no questions were requested.
7. At the round limit, preserve the unresolved result, stop dependent work, and
   continue independent drafting. Do not select an arbitrary winner or claim
   the affected section passed.

## Reconcile previous decisions

Explicit user requirements remain binding. A fresh vote may reconsider a
provisional agent decision when evidence or requirements change, but cannot
retroactively turn it into a user decision. Give voters both relevant source
versions and new evidence without revealing earlier individual votes. Record
what changed, which decision was superseded, and which sections need rechecking.
