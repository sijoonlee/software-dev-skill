---
name: auto-run
description: Run one task or a queue of tasks unattended, for example overnight, and leave verified local branches for the user to review. Use when the user says "auto-run", "run this overnight", "I'm going to bed", "work on these while I'm away", or hands over a list of tasks to finish without them.
---

# Auto-run

Work without the user, then hand back branches they can review in minutes. Nothing leaves the machine: no push, no PR, no merge.

## 1. Agree the contract before starting

Don't start until each task has these. Ask once, up front, for anything missing. After that, don't ask again.

- **Goal.** What changes, in one or two sentences.
- **Done check.** A check that passes or fails, such as "`npx jest __tests__/lib/overview.spec.ts` passes and `rg oldParser src` finds nothing". A duration ("work for 4 hours") is not a done check.
- **Base.** The branch to start from, usually `main`.
- **Way out.** When to stop and write up why instead of pushing on, such as "the same check failed after three different approaches".

Write the contract as the first rows of the log (step 4).

## 2. Hard limits

- Never push, open a PR, merge, rebase a shared branch, or deploy.
- Never write to shared systems: shared dev databases, Slack, email, ticket trackers, other people's services. If a task needs one, park that task (step 6).
- Each task works only on its own branch, `auto/<task-slug>`, in its own worktree. Never touch the user's checkout or another task's branch.
- Never loosen a done check, skip a test, or delete a failing assertion to get to green.

## 3. The loop, for each task

1. Make the smallest change the evidence supports (**smallest-change**).
2. Run the done check and any tests the change can affect (**prove-it-works**).
3. If it moved forward, commit with a clear message. If not, discard the change. Don't leave "might help" code behind.
4. Log one row (step 4).
5. Repeat until the done check passes or the way out triggers. A plateau means try a different approach (**fix-root-causes**: after two failed attempts, test the assumption they share). It does not mean stop.

Fix small problems you hit along the way, such as a flaky test or a broken script, in their own commit. Don't stop to ask about anything reversible (**act-dont-ask**).

## 4. Decision log

Keep one TSV per run at `<repo>/.skill-ground/auto-run/<run-slug>/decisions.tsv`, in the user's main checkout, so every agent can append to it. Add `.skill-ground/auto-run/` to `.git/info/exclude` so it's never committed, even in a repo that commits the rest of `.skill-ground/`.

```
ts	task	decision	why	evidence	result
2026-10-16T23:10:00Z	overview-range	switched the floor to the affiliate's createdAt	test showed ranges before onboarding	auto/overview-range@3f2a1c9	jest green
```

- One row per decision, iteration, revert, or blocker. Plain words. Evidence is a commit, a path, or a command, never a paragraph.
- Append only. Correct a wrong row with a new row.

## 5. A queue of tasks

- **One owner agent per task.** Spawn each with `isolation: "worktree"`, in the background, with the task's contract, the branch name, the log path, and this skill's path. Run independent tasks in parallel. When a task depends on another, start it from that task's branch after it's verified.
- **A different agent verifies.** When an owner reports done, spawn a fresh read-only agent that didn't write the code. Give it the branch, the contract, and the done check. It runs the check itself, reads the diff for the problems this skill forbids, and reports `PASS`, `ISSUES` (each with evidence), or `BLOCKED`.
- **Fix rounds go to a fresh agent.** On `ISSUES`, spawn a new owner with the original contract, the verifier's findings, and the branch. Allow two fix rounds. After that, mark the task `NOT VERIFIED` and move on.
- **You only coordinate.** You read results, spawn agents, and keep the log. You don't write the code yourself, so the verifier is checking someone else's work.

## 6. Park instead of guessing

Park a task, log why, and move to the next one when it needs any of these: a product decision no test can settle, access to a shared system, an irreversible action, or more than the way out allows. A parked task with a clear reason is a good result.

## 7. Pause and resume

- **Pause** when the user says to, or before the session must end. Finish or back out of the current step, commit work in progress as `wip: <what>`, and write `.skill-ground/auto-run/<run-slug>/resume.md` with what's done, what's verified, and the next step.
- **Resume** from `resume.md` and the log's last rows. Don't redo finished work. Re-run the done check on each branch to confirm where it stands.

## 8. Morning report

End with one table, then the details:

| Task | Branch | Done check | Verifier | Notes |
|---|---|---|---|---|
| overview-range | `auto/overview-range` | passes | PASS | |
| lead-price-ui | `auto/lead-price-ui` | fails | NOT VERIFIED | two fix rounds, see log rows 14 to 19 |
| slack-copy | none | parked | | needs a product call on the wording |

- For each branch, give the command to review it: `git log --oneline main..auto/<slug>` and `git diff main...auto/<slug>`.
- List what to look at first: anything the verifier flagged, anything you weren't sure about, and every parked task with its reason.
- Give the log path.
- Leave every branch and worktree in place. The user decides what to keep.
