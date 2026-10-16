# sijoon-ai-skill

Engineering principles for coding agents, one skill per folder. They are a condensed version of [pstack](https://github.com/cursor/plugins/tree/main/pstack). The 24 pstack principles were merged into 8, and its multi-model and orchestration machinery was dropped.

| Skill | Merged from pstack |
|---|---|
| `understand-before-changing` | foundational-thinking, redesign-from-first-principles, the `how` and `why` skills |
| `model-the-domain` | model-the-domain, type-system-discipline, boundary-discipline |
| `smallest-change` | laziness-protocol, subtract-before-you-add, minimize-reader-load, migrate-callers-then-delete-legacy-apis |
| `fix-root-causes` | fix-root-causes, attack-the-premise, the bug-fix playbook |
| `prove-it-works` | prove-it-works, test-behavior-not-implementation, explain-the-number, the `tdd` skill |
| `small-verified-steps` | sequence-verifiable-units, build-the-lever, outcome-oriented-execution |
| `act-dont-ask` | never-block-on-the-human, the Autonomy section of poteto-mode |
| `write-plainly` | the `unslop` and `no-comments` skills, the reply rules of poteto-mode |
| `few-comments` | the code-comment rules from `no-comments`, tightened to comments about behaviour outside the repo |
| `technical-writing` | the `technical-writing` skill (Diátaxis, Google style, STE, and Global English layers), with sentence rules left to `write-plainly` |
| `typescript-best-practices` | the `typescript-best-practices` skill and its `references/patterns.md`, merged into one file |
| `create-feature-map` | the feature-map part of create-verification-skill, plus a new "Where it lives in code" section |
| `update-feature-map` | the source-reading half of maintain-verification-skill, plus a diff mode that updates only what a change touched |

## App layout these skills produce

```
<app>/                                # repo root for a single-app repo
  .skill-ground/
    feature-map/README.md, <feature>.md
  CLAUDE.md                           # one line pointing at the feature map
```

Dropped principles. Exhaust-the-design-space, experience-first, make-operations-idempotent, separate-before-serializing-shared-state, guard-the-context-window, and encode-lessons-in-structure. They are either narrow or already default agent behavior.

## Install

Copy or symlink each folder into `~/.claude/skills/` for every project, or into `.claude/skills/` for one project.
