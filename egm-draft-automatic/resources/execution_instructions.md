<!-- Modified from EGM 0.1.1 on 2026-11-21: replaced human consensus gates
and blanket contradiction pauses with bounded three-voter decisions. Apache-2.0. -->

# Execution instructions

- **Design only:** Write drafts, decision records, and local documentation.
  Do not modify production implementation files or build the proposed feature.
  Illustrative code belongs in Markdown. If investigation needs temporary code,
  use a private scratch directory outside the project source tree.
- **Three independent voters:** Route routine clarification, architecture
  choices, and section checks through the bundled voting protocol. Do not add
  the upstream human approval gates or its seven-reviewer swarm.
- **One question per packet:** All three voters receive the same question,
  choices, criteria, constraints, evidence, and earlier relevant decisions.
  Do not supply one voter's response to another before its vote.
- **Authority:** Votes provide provisional design decisions. They cannot invent
  user preferences, override explicit user requirements, grant external action
  permission, or claim human approval.
- **Contradictions:** Record contradictions and stop dependent drafting while
  resolving them. Continue independent work. Use evidence and the voting
  protocol for provisional design disagreements; defer an essential unknown
  user preference to the user. Do not silently overwrite earlier commitments.
- **Bounded work:** At most three rounds per original question by default.
  Preserve unresolved questions instead of looping until agreement appears.
- **Artifacts:** Put large drafts and findings in files. Give concise chat
  updates and links. Never present a partial design as implementation-ready.
