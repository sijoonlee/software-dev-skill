---
name: create-feature-map
description: Create an app's feature map, a set of short markdown files that list what the app does, how a user reaches each feature, where it lives in code, and what usually misleads. Use when asked to "map the features", "make a feature map" or when an app has no map and an agent keeps rediscovering the same features.
---

# Create a feature map

A feature map is compact, shared memory for agents and people. An agent opens the one file for the feature it's changing instead of searching the codebase or reading a wiki.

It lives in the app's directory, which is the repo root for a single-app repo:

```
<app>/.skill-ground/feature-map/
  README.md        # index, grouped by area, plus a sweep order
  <feature>.md     # one file per feature area
```

If `README.md` already exists, use the **update-skill-ground** skill instead.

## 1. Inventory features from the user's side

List what a user can do, not how the code is organized. Find features in:

- routes and pages, navigation menus, and modals
- public API endpoints, if the API is the product
- CLI commands, if the app is a CLI
- docs, READMEs, and existing end-to-end tests

Group them into feature areas that a user would name, such as "Sign-in", "Rate comparison", or "Mortgage calculator". One file per area. Split a file when one of its sections needs its own setup or preconditions. Merge tiny areas into an `odds-and-ends.md`.

## 2. Write each feature file

Read the source for the area before writing. Every claim should be something you saw in code or in the running app.

```markdown
# <Feature name>

One sentence on what it does for the user.

## Sub-features
- <name>: what it does, in user terms.

## How to get to it (user POV)
Where the user starts and what they click, type, or call. Include every entry point: menu, URL, shortcut, deep link.

## Where it lives in code
- `path/to/route-or-page`: entry point.
- `path/to/component-or-handler`: main logic.
- `path/to/api-or-service`: backend it calls.

## Tests
Existing specs that cover it: unit, component, or end-to-end. Write "none" when there are none.

## Gotchas
What misleads an agent: feature flags, account or plan state it needs, async loading, A/B variants, parts that can't be automated.
```

Keep each file short enough to read in under a minute. List entry points and invariants, not implementation details that change with every refactor.

## 3. Write the index

`README.md` lists every feature file grouped by area, with one line each. Then add a **sweep order**, the order to walk the files for a broad "did we break anything?" check, with the core user journey first. Then state the file contract: the section names above, so that later edits keep the same shape.

## 4. Point agents at it

Add one line to the app's `CLAUDE.md` (and `AGENTS.md` if the repo has one):

```
Feature map: `.skill-ground/feature-map/README.md`. Open the file for the feature you're changing. Update it in the same PR when user-facing behavior changes.
```

## 5. Check the map

Open three files at random. Confirm every path under "Where it lives in code" exists, and that every route or entry point under "How to get to it" exists in the source. Fix what's wrong.

To keep the map current later, use the **update-skill-ground** skill.
