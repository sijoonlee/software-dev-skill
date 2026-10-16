---
name: create-verification-skill
description: Generate an app-local skill that launches this app, drives it the way a user does, and captures proof. Use when asked to "make a verification skill", "make the agent able to test the app", or when an app has no scripted way to prove that UI, CLI, or API behavior works.
---

# Create a verification skill

Write a verify skill for the app. It tells any later agent how to launch the app, check that it's healthy, drive a feature, capture evidence, and clean up. Assume the reader is an agent mid-task that has never seen the app.

It lives in the app's directory, which is the repo root for a single-app repo, next to the feature map:

```
<app>/
  .skill-ground/
    feature-map/                  # from the create-feature-map skill
    verify/SKILL.md               # this skill writes it
  .claude/skills/verify-<app> -> ../../.skill-ground/verify   # symlink so Claude Code finds it
```

## 0. Make sure a feature map exists

If `<app>/.skill-ground/feature-map/README.md` doesn't exist, run the **create-feature-map** skill first. The verify skill holds what is the same for every feature. The map holds what is specific to each feature.

## 1. Learn how the app runs

Answer these from the code, docs, and scripts. Ask the user only what you can't find out.

- **Surface.** What does a user touch: web UI, API, CLI, or something else? If there are several, pick the main one and note the rest.
- **Run.** The app's own dev command, ports, env vars, seed data, and how login works locally.
- **Drive.** Reuse what exists first: Playwright or Cypress specs, API clients, test fixtures. Otherwise use Playwright (or the Playwright MCP) for web, `curl` for APIs, and tmux for CLIs.
- **Observe.** What can serve as evidence: screenshots, response bodies, logs, database rows, exit codes.

If the app doesn't start as-is, fix that or report exactly what fails before writing anything. A skill written against a broken setup teaches wrong steps.

## 2. Write `.skill-ground/verify/SKILL.md`

Use frontmatter with `name: verify-<app>` and a `description` that names the app, the surface, and when to use it. Fill these sections with real commands and selectors from this app, with no placeholders:

- **Launch.** The exact start command, and how to tell it's ready to use, not just that a process answers on the port. It must work from a clean state, including migrations and seed data.
- **Doctor.** One read-only check that answers "is this instance worth driving?": the process is up, it's the current build, the port belongs to this app, and login works. Run it first, and again after anything surprising.
- **Drive.** How to log in and move around in general. Prefer stable handles such as ARIA roles and labels, `data-testid`, routes, and API paths over CSS classes and coordinates. Wait for an observable state, never a fixed sleep. Point to the feature map for anything specific to one feature.
- **Proof bar.** A proof uses the real user path, not internal setters or test-only endpoints. It shows the action and the resulting state. It checks side effects such as a network call, a saved row, or a reload that keeps the change, not only pixels. "It opens" is not proof. Before proving a change, open the feature map file for that feature and exercise every entry point it lists that the change can affect.
- **Cleanup.** Stop only what this run started. Never kill processes by name. Keep the evidence, and name where it's saved.

Any helper script lives in `.skill-ground/verify/`, must be executable, and the skill body must show how to call it. Don't write a custom CLI up front. Add one when the same command sequence keeps repeating.

Then register it with a relative symlink, run from the app directory:

```bash
mkdir -p .claude/skills && ln -s ../../.skill-ground/verify .claude/skills/verify-<app>
```

## 3. Fill in "Driving it" in the feature map

For the 3 to 5 most important features, write the "Driving it" section of each feature file. Include commands, selectors, and the observable end state that proves the feature works. If the seed data can't reach a feature, write the missing precondition in Gotchas. Never weaken the steps so that they pass.

## 4. Run it once before handing it over

Follow the generated skill end to end once: launch, doctor, drive one feature from the map, capture evidence, clean up. Confirm the evidence still exists after cleanup. Fix whatever failed and run the cleanup after each failed attempt. A skill that was never run is a draft, not a deliverable.

## 5. Keep it current

Tell the user about the **update-skill-ground** skill. Its diff mode runs after a change, and its audit mode is a periodic full check.
