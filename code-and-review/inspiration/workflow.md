# Local daily task workflow

This is a lightweight, local version of the Claude Code team's review model:

> implementation agent verifies its work -> fresh-context reviewer checks it -> human owns the decision.

The purpose is not to remove human responsibility. It is to make sure a human spends time on product intent, risk, and trade-offs instead of discovering routine failures that tools can catch.

## One-time project setup

Keep two short files at the repository root.

### `AGENTS.md`

Document only what an agent needs to work safely:

- how to install dependencies and run the app;
- required format, lint, typecheck, test, and build commands;
- architectural conventions and important boundaries;
- paths that are risky or must not be changed casually;
- how to test UI changes and where screenshots belong.

### `REVIEW.md`

Record the team's most useful review rules:

- what failures look like in this repository;
- security, data-loss, and backwards-compatibility concerns;
- areas that always need a human review, such as authentication, billing, migrations, CI, deployment, permissions, and secrets;
- a rule to report only actionable, introduced issues with file-and-line evidence.

Keep both files brief. Add a rule only after it has repeatedly mattered in a real review or incident.

## The daily task

### 1. Start with a small, testable task

Write the task in terms of outcome and constraints, not just an implementation idea.

```md
Goal: Let a signed-in user rename a saved project from its settings page.

Acceptance criteria:
- The name can be changed and persists after a refresh.
- Blank or whitespace-only names are rejected.
- A user cannot rename another user's project.
- Existing project URLs continue to work.

Scope: Do not redesign the settings page or change project permissions.
```

Small changes are easier to verify, review, revert, and own. Split unrelated cleanup into another task.

### 2. Ask the implementation agent to plan, implement, and prove the change

Give the agent the task plus the repository guidance. Ask for a plan before edits if the change is non-trivial.

Use an instruction like this:

```md
Implement this task. First inspect the relevant code and state a short plan.
After implementing, verify the work using the commands in AGENTS.md.
For UI work, exercise the changed flow and capture a screenshot.
Do not claim completion without showing the exact commands run, their results,
and any artifacts. State clearly what you could not verify and why.
Keep the diff limited to the requested scope.
```

The agent should leave behind a change that is already checked, not a change that merely looks plausible.

### 3. Require concrete verification before review

Run the smallest useful set of checks locally. For example:

```sh
npm run format:check
npm run lint
npm run typecheck
npm test -- --runInBand
npm run build
```

Adapt these commands to the project. Run focused tests during development and the broader required suite before merging. For a UI task, also verify the actual flow in a browser and attach a screenshot or recording.

Record results in a handoff note:

```md
## Verification
- `npm run lint` — passed
- `npm run typecheck` — passed
- `npm test -- project-settings` — passed (6 tests)
- `npm run build` — passed
- Manual: renamed a project, refreshed, and confirmed the new name remained.
- Artifact: `artifacts/project-rename.png`
```

If a check fails, do not hide it. Fix it, narrow the task, or explicitly hand it to a human with the failure noted.

### 4. Run a fresh-context review

Use a second agent/session that did not implement the task. Give it:

- the original task and acceptance criteria;
- the diff;
- `AGENTS.md` and `REVIEW.md`;
- the verification note and any screenshot.

Use this review prompt:

```md
Review this change with fresh context. Check it against the task, acceptance
criteria, repository guidance, and verification evidence. Look for introduced,
actionable bugs, security issues, missing tests, broken edge cases, or scope
violations. Cite file and line evidence for each finding. Do not report style
preferences or speculative concerns. Start with the number of findings and say
plainly if there is nothing to fix.
```

The implementation agent has context but also a natural bias toward its own solution. The separate reviewer is a low-cost way to challenge assumptions before the task reaches a person.

### 5. Resolve findings, with a review-round cap

- Fix confirmed findings and rerun the affected checks.
- If a finding is incorrect or intentional, record a short reason rather than silently ignoring it.
- After the first review round, review only the new diff unless the task changed materially.
- Cap the loop at three rounds. If it still does not converge, stop and have a human reconsider the approach rather than letting agents churn indefinitely.

### 6. Describe risk and rollback in the PR

Complete the repository's [PR template](PR_TEMPLATE.md). It puts the task, verification evidence, review results, risk level, and rollback plan in one place for the human deciding whether to merge.

### 7. Merge small and keep rollback easy

For medium- or high-risk behavior, prefer a feature flag, staged release, or a separate migration plan. The person who requested or directs the work owns the outcome, even when an agent wrote the code.

After merging, perform a quick smoke test for the user-facing path.

## Daily checklist

```md
- [ ] Task has a clear outcome, acceptance criteria, and scope.
- [ ] Implementation agent read `AGENTS.md` and made a focused change.
- [ ] Relevant tests, lint, typecheck, and build were run.
- [ ] UI work has manual evidence (screenshot or recording).
- [ ] A fresh-context agent reviewed the diff and evidence.
- [ ] Findings are fixed or explicitly resolved.
- [ ] Risk level and rollback path are recorded.
- [ ] A human reviewed the appropriate level of risk and owns the merge.
```

## Improve the workflow from real mistakes

When a bug, revert, or noisy review comment happens, ask which layer should have caught it. Then make one small improvement:

- add a focused test;
- add or adjust a lint/type rule;
- clarify `AGENTS.md` or `REVIEW.md`;
- improve the implementation or review prompt;
- reclassify the area as higher risk.

This keeps the workflow grounded in failures the project actually has, instead of growing a large set of theoretical rules.
