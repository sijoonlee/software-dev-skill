---
name: few-comments
description: Apply whenever writing or editing code, tests, stories, or config. Add a comment only when it explains behaviour outside the repo, such as a library quirk, a browser rule, or an external service's contract. Leave business rules and in-repo design reasons out of comments.
---

# Few comments

Most code needs no comment. Before you write one, ask: **does it explain something outside this repo?** If not, don't write it.

**Write a comment for**
- A library or framework quirk. "Recharts centres every tick on its point, so the first and last labels overhang." "A `'use server'` module may only export async functions."
- A browser or platform rule. "iOS Safari zooms into inputs with a font size under 16px." "A nested `<label>` is invalid HTML."
- An external service's contract. "WorkOS can't disable a user, and a partner who registers again gets a new user id." "cities-search rejects a query with only a province."
- A tool directive the build needs: `eslint-disable`, `@ts-expect-error`, `/// <reference>`, `@jest-environment`, Dockerfile `# syntax=`.

Keep it to the outside fact, in one or two lines. Don't add our own reasoning on top. If a workaround needs a long comment to justify it, fix the code instead.

**Don't write a comment for**
- What the code does, or what a name, type, or prop already says. No JSDoc that restates the function name.
- Business or product rules, copy decisions, and our own design choices. Leave out notes like "deliberately", "on purpose", or "we chose X so that Y".
- Invariants between files in this repo, or why one module mirrors another.
- Test narration, arrange/act/assert labels, the test title restated, or why a fixture has a certain value.
- File-header overviews, section dividers, history ("previously", "changed in PR"), or TODO narration.
- References to ERDs, PRDs, SDDs, `§` sections, or tickets.

**When an in-repo comment seems critical**
If deleting the reason would plausibly cause a security hole, data loss, or a production bug for the next developer, don't decide alone. Ask the user before keeping it. Examples that earned a keep: "the blocklist check must run before anything is written", "seed with `$setOnInsert` so a redeploy keeps admin changes", "this id is published in partners' snippets and must never change". Something that is merely helpful doesn't qualify.

**When editing existing code**
Hold new comments to this bar. Don't rewrite comments you didn't touch, unless the user asked for a cleanup. If a comment you touch states something no longer true, fix it or delete it.

**Check:** read each comment you added and name the outside system it explains: a library, a browser, or a service. If you can't, delete it.
