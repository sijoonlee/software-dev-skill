---
name: code-and-review
description: Implement and review a local code change with evidence, risk-based delegation, and a PR description. Use when a task should be completed through an implementation-and-review workflow before a human merge decision.
---

# Code and review

Use this workflow to produce a small, verified change and a reviewer-ready PR description. The goal is to move routine checking before human review while preserving human ownership of risk and merge decisions.

Read `AGENTS.md` when it exists. Use the repository's `PR_TEMPLATE.md` to draft the PR description.

## 1. Define the task contract

Before editing, state:

- the goal and acceptance criteria;
- scope boundaries and files/areas likely affected;
- relevant verification commands and required UI evidence;
- a provisional risk level: low, medium, or high.

Risk is determined by the change and its blast radius, not by its author:

- **Low:** small, isolated, reversible work with easy-to-detect failure—for example docs, copy, styling, internal tooling, or a well-tested bug fix.
- **Medium:** normal product work or changes to shared code, user workflows, caching, or integrations.
- **High:** changes affecting security, privacy, permissions, money, data integrity, migrations, CI/CD, infrastructure, dependencies, public APIs, or broadly copied architecture.

If risk is unclear, choose the higher tier until a human changes it.

## 2. Choose the review path

- For a low-risk task, the main agent may implement and verify it directly. Still run relevant checks and create the PR description.
- For medium- or high-risk work, the main agent delegates implementation and review to separate sub-agents.
- Always require a human merge decision for high-risk work. Do not treat an agent's review as human approval.

## 3. Implementation and evidence

For delegated work, instruct the implementation sub-agent to:

1. Inspect the relevant code and follow the task contract.
2. Make a focused change without unrelated cleanup.
3. Run the required checks, plus focused tests appropriate to the change.
4. For UI work, exercise the changed flow and capture a screenshot or recording.
5. Return the diff summary, exact commands, outcomes, artifacts, known limitations, and suggested rollback.

Do not accept “done” without concrete verification evidence. Failed or unavailable checks must be reported plainly.

## 4. Fresh-context review

For medium- and high-risk tasks, give the review sub-agent:

- the task contract;
- the current diff;
- relevant repository guidance;
- implementation evidence and UI artifacts.

Do not provide the implementation sub-agent's private reasoning. Ask the reviewer to independently check the diff against the task and evidence.

The reviewer reports only introduced, actionable findings. Each finding must include file-and-line evidence and severity. It should say plainly when there is nothing to fix. Ignore style preferences, speculative issues, and unrelated pre-existing problems unless they block safe completion.

## 5. Resolve and re-review

The main agent decides whether a finding is valid. Valid findings are fixed and the affected verification reruns. Record a short reason for rejected findings.

After the first review round, re-review only the follow-up diff unless the task changed materially. Cap the process at three review rounds. If it does not converge, stop and ask a human to reconsider the approach rather than letting agents churn.

## 6. Draft the PR description

Fill every applicable section of `PR_TEMPLATE.md` from the task contract and actual evidence:

- intent and reviewer-oriented summary;
- commands run, outcomes, and UI artifacts;
- fresh-context review result and finding resolutions;
- one selected risk level with a short rationale;
- likely failure mode and a concrete rollback path;
- reviewer notes for medium/high-risk changes.

Draft the description locally. Do not create, submit, or merge a remote PR unless the user explicitly requests that external action.

## 7. Human handoff

Present the final diff, PR description, unresolved limitations, and recommended human review depth. The person directing the change owns the outcome, regardless of whether an agent wrote the code.
