## Intent

<!-- What problem does this solve? Link the task or issue when available. -->

## What changed

<!-- Summarize the change for a reviewer. Keep this focused on behavior, not a list of files. -->

## Verification

<!-- Include exact commands and their outcomes. Attach a screenshot or recording for UI changes. -->

- [ ] Tests:
- [ ] Lint / format:
- [ ] Typecheck:
- [ ] Build:
- [ ] Manual verification:
- [ ] UI artifact (if applicable):

## Fresh-context review

<!-- State the result of the independent agent review. Link or paste unresolved findings and their resolution. -->

- [ ] Reviewed against the task, diff, project guidance, and verification evidence.
- Findings / resolution:

## Risk level

<!-- Select one. The level reflects the change and its blast radius, not who authored it. -->

- [ ] **Low** — Small, reversible, isolated change. Examples: copy/docs, internal tooling, styling, a well-tested bug fix, or an additive feature behind a flag. A failure is easy to detect and revert.
- [ ] **Medium** — Normal product behavior or a change that touches shared code, caching, external integrations, user-facing workflows, or an area with meaningful regression risk. It needs a focused human review.
- [ ] **High** — A mistake could cause security, privacy, financial, data-integrity, availability, deployment, or broad compatibility harm. Examples: auth/permissions, secrets, payments, destructive actions, migrations, CI/CD, infrastructure, dependency upgrades, public APIs, and architectural patterns. It needs deliberate human review and a clear release plan.

## Failure mode and rollback

<!-- What is most likely to go wrong, and how can this change be undone quickly? -->

Potential failure:

Rollback:

## Reviewer notes

<!-- For medium/high risk: what should the human pay special attention to? -->
