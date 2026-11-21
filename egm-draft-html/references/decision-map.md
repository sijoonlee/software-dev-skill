# Decision map format

The agent authors the hierarchy. The Python builder does not infer importance,
resolve conflicting policies, or summarize the source automatically.

Run `inspect` first. Copy its `sourceSha256` and use its exact section IDs.
The map contains editorial fields only; source status, date and original content
are taken directly from the supplied Markdown, not from this map.

```json
{
  "sourceSha256": "copy the actual 64-character hash from the inspector",
  "title": "Design document title",
  "groups": [
    {
      "id": "responsibility",
      "label": "Responsibility",
      "title": "Keep authorization with the application.",
      "answer": "The application authorizes requests; the worker performs the allowed operation.",
      "why": "The source assigns identity and permission checks to the application.",
      "tradeoff": "The worker still needs to validate its own execution inputs.",
      "connections": [],
      "details": [
        {
          "id": "identity-owner",
          "title": "Who establishes the request identity?",
          "answer": "The application uses the authenticated session.",
          "why": "Rationale not stated separately in the source.",
          "tradeoff": "Inferred consequence: the worker cannot substitute a caller-supplied identity.",
          "sources": ["use-an-authenticated-identity"]
        }
      ]
    }
  ]
}
```

This is a schema example, not content to copy into unrelated designs. Replace
all example text and source IDs with statements supported by the selected draft.

## Fields

| Field | Requirement |
|---|---|
| `sourceSha256` | Required; exact inspector hash. A mismatch blocks rendering. |
| `title` | Optional nonempty page title; defaults to the source's first H1 or filename. |
| `groups` | Nonempty list in editorial reading order. |
| Group `id` | Unique lowercase letters/digits/hyphens. Used in `#group/<id>`. |
| Group `label` | Short navigation label, usually one to three words. |
| Group `title` | The major decision in a short declarative sentence. |
| `answer`, `why`, `tradeoff` | Nonempty plain text. No HTML or Markdown formatting needed. Preserve uncertainty and label inference. |
| `connections` | Optional list of other major group IDs; no self-reference. |
| `details` | Nonempty list of supporting decisions; IDs must be unique across every group. |
| Detail `title` | A short question explaining what this supporting choice settles. |
| Detail `sources` | Nonempty array of exact inspector section IDs. Multiple sections can support one decision. |

Group fields are grounded in the union of their supporting source sections.
Unmapped source sections remain available in the source browser; do not promote
every implementation paragraph into a major decision merely to map everything.
Conversely, do not omit a material architectural choice because it complicates
the preferred narrative. Inspect headings and source bodies for decisions that
appear outside the formal Technical Plan.

## Revision handling

Preserve explicit supersession. A section labeled “superseded” is historical
evidence, not an additional active implementation option. Source ordering alone
does not settle contradictions without an explicit revision or maintained rule.
When there is no defensible resolution, summarize the choice as unresolved and
link both statements. Do not invent an approval date or claim a review ran.

The page's source browser includes all inspected heading levels and exact raw
Markdown, including unmapped history. Local links in rendered source appear as
unbundled references; the renderer never opens those files. HTTPS citations are
user-initiated links only. The HTML loads no external assets.
