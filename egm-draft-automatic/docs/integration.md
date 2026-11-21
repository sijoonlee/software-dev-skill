# Host integration for the revised draft skill

This local bundle adapts EGM 0.1.1 and includes only the revised draft skill,
its design template, voting instructions, and three standalone personas.
It is not a plugin installation or a claim of cross-host certification.

## Resource paths

The bundle root is the directory containing the selected `SKILL.md`. Resolve
`references/`, `agents/`, `resources/`, and `docs/` against that directory. Use this bundle's resources and personas, not similarly
named files in a global plugin or the workspace's separate `agents/` directory.
Pass absolute persona, packet, and selected evidence paths to voters.

Resolve user input paths against the working directory. Write deliverables to
an explicitly selected artifact directory or the working directory by default.
Honor an `EGM artifact directory: <path>` supplied by the user or applicable
project instructions within the host's permissions. If an instruction-file path
resolves outside the workspace and has not been explicitly authorized by the
user, use the working directory and explain the fallback. Do not infer a
user-specific destination through agent voting.

## Fresh-context dispatch

The main agent directly launches exactly three voter jobs per round, one for
each persona. No synthesizer or nested reviewers are needed. Run them concurrently
when three child slots are available. If the host has fewer slots, use batches
without exposing earlier results to later voters; report the scheduling limit.

Inspect the native subagent schema. With Codex `spawn_agent`, use
`fork_turns: "none"`; if the host exposes `fork_context`, set it to false.
Use the inherited/default model unless the user explicitly specifies otherwise.
Do not pass conversation history, hidden reasoning, or memory lookups. Give all
voters the identical saved decision packet plus only their own persona path.

Fresh context does not prove instruction-file or filesystem isolation. Report
this distinction accurately. Voters are instructed to be read-only; those
instructions are not a tool sandbox. Restrict tools to read/search where the
host supports it and do not claim enforced restrictions when unavailable.

Require every voter to read its persona, the packet, and all mandatory evidence
before returning. Wait for actual completion. Preserve returned reports and
record unread sources or failed reads. A started job is not a completed vote.

If the host cannot establish fresh-context subagents, record the capability
blocker and stop the voting workflow. Do not imitate three personas in the main
context, reuse old voter sessions, or silently substitute a global EGM reviewer.

## Running the local variant

Select this bundle’s `SKILL.md` or invoke `egm-draft-automatic`. Its distinct
name separates this automatic workflow from the upstream `egm-draft` skill.
The copied files do not register themselves with a host. No other EGM skills,
plugin manifests, adapters, or review swarm are included.
