---
name: technical-writing
description: Apply when writing or reviewing a document for other engineers, such as a README, design doc, ERD, RFC, runbook, how-to, PR description, or commit message. Pick one document type, structure it for a reader who skims, and leave no sentence open to two readings.
---

# Technical writing

Write so a tired engineer understands on the first read. Sentence-level rules and AI tells are in the **write-plainly** skill. Apply it too. This skill covers the document.

## Pick one document type first

Every document does one job. Ask what the reader came to do.

| Type | Reader wants to | Write it as |
|---|---|---|
| **Tutorial** | learn by doing | Steps that each produce a visible result. Say what they'll see. Keep explanation to a clause and a link. |
| **How-to** | finish a task they already understand | Commands only, in order. Assume competence. Allow forks: "If you need X, do Y." Title it by the task: "How to rotate the WorkOS key". |
| **Reference** | look up a fact | Dry, complete, and sure. Mirror the structure of the thing described (one section per route, flag, or table). No opinions or instructions. |
| **Explanation** | understand why | One bounded topic. The context, constraints, alternatives, and decision. This is the only type where opinion belongs. |

Don't mix types in one document. If a how-to needs background, link to an explanation. If a design doc needs a config table, put it in a reference section or a separate page.

## Structure for skimming

- **Put the point first.** The first screen says what this is, the decision or result, and what the reader should do.
- **Headings carry the point**, not just the topic: "Blocking is per user, not per org", not "Blocking". Use sentence case. Don't skip heading levels.
- **Numbered lists for sequences, bullets for everything else.** Introduce a list with a full sentence. Keep items parallel in form.
- **Use a table** when items share the same attributes. Use a diagram when the reader must hold more than three moving parts.
- **Put the common case first** and exceptions after. Put a condition or warning before the step it applies to: "To delete the org, first revoke its approvals."
- **Code font** for symbols, files, flags, and commands. **Bold** for UI labels.

## Use the codebase's words

- Write the real symbol, file, flag, or command, not a description of it. `isEmailBlocked`, not "the block check".
- Call each thing by one name everywhere. A doc that says "the gate", "the check", and "the guard" for one thing teaches three things.
- Don't invent jargon. If a named pattern is needed, define it the first time it appears.

## Leave no sentence open to two readings

- Keep "only" and "not" next to the word they change. "Fails only on growth" and "only fails on growth" differ.
- Make every "it", "this", and "they" point at one obvious noun. Repeat the noun when in doubt.
- Break long noun strings: "the proto import budget check script" becomes "the script that checks the proto-import budget".
- Don't drop a verb in the second half of a sentence. "Phase 1 moves the converters and Phase 2 the runtime" needs "moves" twice.
- Use periods, not semicolons. No slashes: write "a, b, or both", not "a/b".
- No idioms, Latin abbreviations, or "etc.". Say up front when a list is partial.
- Give instructions as commands in the present tense: "Run `launch.sh`." Never "should be run" or "simply run".

## Vary the rhythm

Following every rule can still read as machine-written. Mix sentence lengths on purpose: a short one lands a point, a longer one carries a fact with its condition. In an explanation, say what you make of the trade-offs instead of listing pros and cons. Prefer a specific example to a general claim: "a column rename fails the build", not "schema changes can cause issues".

## PR descriptions and commit messages

- A PR description is a briefing a reviewer reads in under a minute: what changed for the user, why, how it was verified, and what's still open.
- Link logs, benchmark tables, and long output. Don't paste them.
- A commit message subject says what the commit does, in the imperative: "Block users by email, not by user id".
- Make every count, path, or tree in the text true at the commit that lands it.

## Example

Before:

> Configuration of the proto import ratchet budget script parameters is performed via budget.json. Note that it's important to remember that running with --write, which updates the committed budget to reflect the current count, should only be done when lowering it. If exceeded, CI fails.

After:

> `budget.mjs` reads the committed budget from `budget.json` and counts the files that import protos. If the count exceeds the budget, CI fails. Run `budget.mjs --write` only to lower the budget.
