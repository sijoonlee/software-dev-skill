#!/usr/bin/env python3
"""Behavioral checks for provenance, isolation, stale maps and safe embedding."""

import json
import re
import tempfile
import unittest
from pathlib import Path

from build_guide import (GuideError, build_payload, main, read_document,
                         validate_map, write_output)


class GuideTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="decision-guide-test-")
        self.root = Path(self.directory.name)
        self.source = self.root / "draft.md"
        self.source.write_text("# Notification delivery\n\n- **Status:** Proposed\n"
                               "- **Date:** 2026-11-21\n\n## Delivery\n"
                               "Send one email per recipient.\n\n### Retries\n"
                               "Retry temporary failures once.\n", encoding="utf-8")
        self.document = read_document(self.source)
        self.mapping = {"sourceSha256": self.document["sourceSha256"], "groups": [{
            "id": "delivery", "label": "Delivery", "title": "Deliver email once.",
            "answer": "Send an email.", "why": "The source selects email.",
            "tradeoff": "Other channels are outside scope.", "details": [{
                "id": "retry", "title": "Which failures are retried?",
                "answer": "Temporary failures, once.", "why": "Not stated.",
                "tradeoff": "Permanent errors need intervention.", "sources": ["retries"]
            }]}]}

    def tearDown(self):
        self.directory.cleanup()

    def test_fences_do_not_create_decisions_or_fake_approval(self):
        self.source.write_text("# Example\n```md\n**Status:** Approved\n## Fake\n```\n"
                               "~~~text\n### Also fake\n~~~\n## Real\nBody\n")
        data = read_document(self.source)
        self.assertEqual([s["title"] for s in data["sections"]], ["Example", "Real"])
        self.assertEqual(data["sourceStatus"], "Status not specified")

    def test_duplicate_headings_have_unique_ids_and_correct_parent(self):
        self.source.write_text("# Draft\n## Policy\nOne\n### Detail\nA\n## Policy\nTwo\n")
        data = read_document(self.source)
        self.assertEqual([s["id"] for s in data["sections"]], ["draft", "policy", "detail", "policy-2"])
        self.assertEqual(data["sections"][2]["parent"], "policy")
        self.assertEqual(data["sections"][3]["line"], 6)

    def test_opaque_local_links_are_not_followed(self):
        self.source.write_text("# Draft\n## Decision\n[Unavailable](plan/never-open.md)\n")
        data = read_document(self.source)
        self.assertIn("plan/never-open.md", data["sections"][1]["text"])
        self.assertFalse((self.root / "plan").exists())

    def test_changed_source_invalidates_old_editorial_map(self):
        self.source.write_text(self.source.read_text() + "New decision.\n")
        with self.assertRaisesRegex(GuideError, "sourceSha256"):
            validate_map(self.mapping, read_document(self.source))

    def test_missing_source_reference_rejected(self):
        self.mapping["groups"][0]["details"][0]["sources"] = ["not-a-section"]
        with self.assertRaisesRegex(GuideError, "missing source"):
            validate_map(self.mapping, self.document)

    def test_invalid_connections_and_duplicate_detail_ids_rejected(self):
        group = self.mapping["groups"][0]
        group["connections"] = ["delivery"]
        with self.assertRaisesRegex(GuideError, "connection"):
            validate_map(self.mapping, self.document)
        group["connections"] = []
        group["details"].append(dict(group["details"][0]))
        with self.assertRaisesRegex(GuideError, "Duplicate detail"):
            validate_map(self.mapping, self.document)

    def test_map_cannot_promote_status_or_replace_embedded_source(self):
        self.mapping["sourceStatus"] = "Approved"
        self.mapping["sourceRaw"] = "replacement"
        payload = build_payload(self.mapping, self.document)
        self.assertEqual(payload["sourceStatus"], "Proposed")
        self.assertEqual(payload["sourceRaw"], self.source.read_text())

    def test_source_and_existing_output_are_protected(self):
        original = self.source.read_bytes()
        with self.assertRaisesRegex(GuideError, "input"):
            write_output(self.source, "changed", {self.source.resolve()}, force=True)
        self.assertEqual(original, self.source.read_bytes())
        output = self.root / "guide.html"
        output.write_text("unrelated")
        with self.assertRaisesRegex(GuideError, "already exists"):
            write_output(output, "new", {self.source.resolve()})
        self.assertEqual(output.read_text(), "unrelated")

    def test_build_is_self_contained_and_escapes_script_terminator(self):
        self.source.write_text(self.source.read_text() + '\n</script><script>throw new Error("injected")</script>\n')
        self.document = read_document(self.source)
        self.mapping["sourceSha256"] = self.document["sourceSha256"]
        mapping = self.root / "guide.map.json"
        mapping.write_text(json.dumps(self.mapping))
        output = self.root / "guide.html"
        original = self.source.read_bytes()
        self.assertEqual(main(["build", "--source", str(self.source), "--map", str(mapping),
                               "--output", str(output)]), 0)
        rendered = output.read_text()
        block = re.search(r'<script id="guide-data" type="application/json">(.*?)</script>',
                          rendered, flags=re.S).group(1)
        payload = json.loads(block)
        self.assertEqual(payload["sourceRaw"], self.source.read_text())
        self.assertNotIn("</script>", block)
        self.assertNotRegex(rendered, r'<(?:script|link|img|iframe)\b[^>]*(?:src|href)=["\']https?://')
        self.assertEqual(original, self.source.read_bytes())

    def test_empty_source_is_not_a_fake_design(self):
        self.source.write_text(" \n")
        with self.assertRaisesRegex(GuideError, "empty"):
            read_document(self.source)

    def test_unheaded_document_still_preserves_every_byte_of_text(self):
        self.source.write_bytes(b"Plain decision.\r\nSecond line.\r\n")
        data = read_document(self.source)
        self.assertEqual(data["sourceRaw"], "Plain decision.\r\nSecond line.\r\n")
        self.assertEqual(data["sections"][0]["text"], data["sourceRaw"])

    def test_bom_source_still_parses_and_download_text_preserves_bytes(self):
        original = b"\xef\xbb\xbf# Draft\r\n\r\n## Choice\r\nUse email.\r\n"
        self.source.write_bytes(original)
        data = read_document(self.source)
        self.assertEqual(data["title"], "Draft")
        self.assertEqual(data["sourceRaw"].encode("utf-8"), original)
        self.assertEqual(data["sections"][1]["line"], 3)


if __name__ == "__main__":
    unittest.main()
