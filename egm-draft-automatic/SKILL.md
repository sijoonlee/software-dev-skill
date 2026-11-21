---
name: egm-draft-automatic
license: Apache-2.0
disable-model-invocation: true
description: >-
  Draft a technical design from a concepts brief or supplied notes using three
  independent agent voters instead of routine user choice and section approval
  gates. Records provisional decisions, dissent, and unresolved user preferences.
---

<!-- Modified from EGM 0.1.1 on 2026-11-21: replaced human decision and section
approval gates with Practicality, Consequences, and Fitness voters. This local
variant does not represent upstream EGM behavior. Licensed under Apache-2.0. -->

# Design drafting with three independent voters

Read [execution instructions](resources/execution_instructions.md),
[host integration](docs/integration.md), and the
[voting protocol](references/voting.md) before drafting. Resolve bundle paths
against this copy of `egm-draft-automatic`, not an installed EGM plugin. This is a local
skill bundle, not a registered or installed plugin.

The main agent frames questions, gathers evidence, writes artifacts, and counts
votes. Three fresh-context agents independently evaluate every choice:

| Voter | Persona | Main concern |
|---|---|---|
| Practicality | [practicality.md](agents/practicality.md) | Simplest sufficient approach, delivery, reuse, and maintenance |
| Consequences | [consequences.md](agents/consequences.md) | Detection, recovery, persistent effects, and information loss |
| Fitness | [fitness.md](agents/fitness.md) | Actual problem, domain behavior, constraints, and justified capacity needs |

Their roles direct attention, not fixed priorities. All three vote against the
same goal, constraints, and criteria. Do not launch EGM's seven reviewers or its
synthesizer in this workflow.

## Boundaries and artifacts

- Produce design documents only. Do not implement or deploy the proposed design.
- Keep substantive drafts and reports in files, with concise progress messages
  and absolute-path links in chat.
- Use plain English and concrete mechanisms. Challenge assumptions and explain
  trade-offs without promotional language or reflexive agreement.
- Routine design questions, architecture choices, intake checks, section checks,
  and predecessor contradictions go through the voting protocol, not user gates.
- Mechanical choices with one defensible answer may be made directly. Record
  consequential architecture choices through a vote.
- Votes are provisional agent decisions, never user approval. They cannot change
  an explicit user requirement or grant permission for external actions.
- Unknown user preferences remain unresolved. Ask one concise user question only
  when the answer is essential to further progress; keep independent work moving.
  If the user requests no questions, record the blocker instead.
- Honor new user corrections and inline comments. Reevaluate affected decisions
  rather than silently retaining an earlier agent majority.

Write the following under the user's selected artifact directory, or the working
directory by default:

- `design_draft.md`: the evolving design, including open questions and decisions.
- `draft-decisions/`: versioned decision packets, raw voter reports, and results.

Use unique decision IDs and round numbers to preserve earlier evidence. On
resume, read existing artifacts before writing; preserve unrelated work and reuse
valid decisions unless their inputs changed. A completed draft has status
`Proposed`; an incomplete draft has status `Draft`. Never mark it `Approved`
without actual user approval.

## Inputs

Optional inputs are a context file, feature name, output path, author, established
principles and criteria, and a maximum voting-round count. The default is at most
three rounds per original question, including reframing and evidence updates.
All retries and stopping rules are defined in the voting protocol.

## Section check, used after Steps 2–5

Write the section, then create one question: “Does this section meet the stated
requirements well enough to continue drafting?” Choices are:

- `continue`: accept the section provisionally and proceed.
- `revise`: identify concrete corrections before proceeding.
- `blocked`: essential information or a user decision is missing.

Provide the exact section version, source requirements, applicable earlier
decisions, and evidence to all three voters. Check fidelity to the requirements,
internal consistency, consequential omissions, and whether architectural choices
have decision records. Do not ask agents to infer user satisfaction.

A `continue` majority advances only after the main agent resolves any verified
hard-constraint violation. A `revise` majority requires corrections and a new
round on the revised section. A `blocked` result is recorded with the missing
information. Any result without two matching votes uses the protocol's no-majority
path. Abstention and rejection remain available for every question.

Carry ordinary dissent forward; do not demand unanimity. Do not conceal a
material evidence gap behind a section-check majority. Bound revision rounds;
when the limit is reached, record the section as unresolved and continue only
work that does not depend on its acceptance.

After a completed check, link the draft and briefly report the result and any
material dissent. Continue automatically when the decision permits it; do not
wait for routine human approval.

## Step 1: Ingest and establish the drafting basis

1. Read an explicitly supplied context file first. If none is supplied, check
   `concepts_brief.md`, then `discussion_summary.md`, under the artifact directory,
   working directory, or `scratch/`, in that order within each file type.
2. If neither exists, use the user's supplied notes and explicitly identified
   project sources. Do not invent the problem, goals, or requirements. If there
   is no usable problem statement, record what is missing and ask only for the
   essential context; voting cannot manufacture it.
3. Extract goals, non-goals, constraints, known decisions, rejected alternatives,
   and unknowns. Keep explicit user commitments distinct from agent hypotheses.
4. Run an intake vote: use the available context to start, reconcile identified
   inconsistencies, or mark intake blocked. The voters assess sufficiency and
   consistency, not whether this is what an absent user secretly intended.
5. Resolve the author from an explicit input, then the brief, then
   `git config user.name`, then `GIT_AUTHOR_NAME`. If none exists, write
   `Author: Unspecified`; voters must not invent an identity.
6. Start the draft with the feature name, date, author, and `Draft` status using
   the [design template](references/design_doc.md). Derive a neutral feature name
   from the supplied problem if none was given.

## Step 2: Draft overview, problem, and scope

Write Overview, The Problem, Goals, Non-Goals, Open Questions, and Critical User
Journeys when applicable. Describe the user need and intended behavior before
technical mechanisms. Cite the source of requirements and label assumptions.

Use design-choice votes when a consequential scope question has multiple
acceptable answers. Do not put explicit user requirements up for majority
replacement. Run the section check for Overview & Goals.

## Step 3: Draft the technical plan

Inspect relevant code and supplied evidence. Describe components, interfaces,
data models, data flow, dependencies, and critical non-functional requirements.
Use ASCII or Mermaid diagrams when they clarify relationships.

For each unresolved consequential architecture choice, prepare up to three
materially different options with mechanisms, trade-offs, and failure conditions.
Run a choice vote before incorporating a selected option as the provisional
plan. Voters may challenge the framing or suggest an omitted alternative.

Use the four consequence questions to scale investigation: impact area, ending
event, rebuild sources and retention, and discovery point. Include harm before
reversal. Cheap, contained decisions need less evidence than irreversible ones;
low reversal cost does not excuse violating a hard requirement.

Reference decision records in the Technical Plan and run its section check.

## Step 4: Draft alternatives

Read `Alternatives Weighed` from the predecessor if available. Preserve the
attributed reasons for earlier decisions; do not rely on conversational memory.
If that history is absent, say it was not supplied. Use options actually examined
in this drafting session and their recorded vote results instead of inventing
historical rejections or asking the user for routine alternative selection.

Distinguish “Rejected by author” when explicitly supported by the source from
“Not selected by agent vote,” and preserve dissent. Attribute an upstream
maintainer rejection only with its supporting issue, discussion, or PR URL.

Write Alternatives Considered and run its section check.

## Step 5: Draft the detailed implementation plan

Write one unified plan covering every known file to create, modify, or delete,
including documentation, configuration, schemas, and meaningful verification.
For each file, explain what changes and why. Use precise paths where supported
by inspection; label proposed new paths. Include rollout, recovery, and failure
checks when relevant. Do not write production implementation code. Interface
sketches, schemas, and pseudocode are allowed in the document.

Use votes to resolve new impactful design choices rather than leaving them to
an implementer. Retain genuine unknowns in Open Questions and mark dependent
implementation steps blocked; do not manufacture detail to claim readiness.
Run the Detailed Implementation section check.

## Step 6: Reconcile and finalize locally

1. Reread the predecessor file, or the supplied notes used as the drafting basis
   when no predecessor file exists, and compare it to the draft. List contradictions first,
   then additions affecting architecture, external interfaces, or dependencies.
   Quote or cite both sources in the relevant decision packets.
2. An explicit user requirement is binding unless the user changes it. Correct a
   draft that violates it; if it cannot be satisfied, record the blocker. For
   discrepancies between provisional design decisions, run a vote with both
   sources and new code evidence. Keep dependent work blocked while unresolved.
   The voters may read the brief here; this is decision reconciliation, not an
   upstream EGM blind document review.
3. Recheck affected sections after material reconciliation changes. Record each
   resolution and preserve the original decision history.
4. Use an explicitly supplied output file or directory. Otherwise select the
   context file's containing design directory when suitable, then an existing
   `docs/designs/`, then default to `docs/designs/`. This mechanical fallback
   does not require a vote or user gate. Artifact-directory selection is
   separate from the final design destination. Respect filesystem permissions.
   Do not overwrite unrelated existing content; use an unused filename when
   needed and report the chosen path.
5. If all sections passed and no consequential question remains unresolved, set
   status to `Proposed` and save `<FEATURE>.md` in the destination. Otherwise
   keep status `Draft`, preserve the partial artifact, and report blockers;
   do not claim drafting is complete. When saving into a different directory,
   rebase relative links to evidence and decision records against the final
   document location and verify they resolve. Keep the original record files
   in their artifact directory unless the user requests a move.
6. For a completed design, register it in an existing destination `SITEMAP.md`
   using that file's format. Do not create a sitemap solely for this workflow.
7. Check Markdown structure, links, decision references, and that every plan
   follows the latest recorded decisions. Link the design and decision records,
   state its provisional status, and name unresolved matters if any. Human or
   broader EGM review is an optional next step, not part of this bundle or a
   requirement to finish this drafting task. Do not publish, open a PR, or
   implement the design automatically.
