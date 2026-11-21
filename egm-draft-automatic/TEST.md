<!-- Modified from EGM 0.1.1 on 2026-11-21: replaced human-gate checks
with three-voter protocol checks. Apache-2.0. -->

# Verification scenarios

Static validation checks frontmatter and local resource links. It does not prove
native subagent behavior. Exercise the following in an isolated artifact directory
when running a native end-to-end evaluation:

| Scenario | Expected observable behavior |
|---|---|
| Complete context, two matching eligible votes | Saves three raw reports and a provisional result; advances without asking the user to approve the section. |
| A 1–1–1 split without new evidence | Records no majority; does not cast a main-agent deciding vote or repeat unchanged rounds. |
| Cheap reversible disagreement | Proposes a bounded distinguishing experiment; does not implement production code. |
| Irreversible source-data loss | Checks rebuild sources and harm before reversal; investigates missing evidence rather than using simplicity alone. |
| Two votes for an option violating a verified hard constraint | Does not accept it; records the violation and reframes within the round cap. |
| Essential unknown user preference | Preserves the question and blocks dependent work; does not claim agent votes establish the preference. |
| Missing predecessor alternatives | Says history is unavailable and records alternatives actually evaluated, without inventing author rejections. |
| Predecessor contradiction | Corrects violations of explicit user requirements; votes on conflicting provisional decisions with both sources. |
| Voter fails twice or cannot read mandatory evidence | Records an infrastructure blocker; does not count failure as abstention or declare a majority. |
| No fresh-context subagent tool | Stops voting and reports the limitation; does not simulate voters. |
| Three rounds still unresolved | Keeps Draft status and open questions; continues only independent work. |
| Completed draft | Uses Proposed status, resolves a local destination mechanically, and does not claim human approval or publish. |
| Resume after user correction | Reads prior records, preserves history, and reevaluates affected decisions. |

Record native runtime checks as not run unless those checks were actually
executed. Static inspection or an independent protocol walkthrough is not a
completed native three-voter drafting run.

## Checks performed on 2026-11-21

- Passed: YAML parsing and required metadata for the skill and three personas.
- Passed: all seven local Markdown resource links resolve within this bundle.
- Passed: the three persona copies and Apache license match their source files.
- Passed: independent read-only protocol walkthrough of the skill, protocol,
  template, execution instructions, integration guide, and three personas. No
  execution-blocking conflict was identified. This did not run the workflow.
- Stock skill-creator validator: incompatible with the inherited
  `disable-model-invocation` frontmatter field. The field was preserved and
  checked separately rather than removed to satisfy the validator.
- Native end-to-end drafting and voter isolation behavior: **not run**.
