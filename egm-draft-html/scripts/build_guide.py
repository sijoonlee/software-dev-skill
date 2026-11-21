#!/usr/bin/env python3
"""Inspect a Markdown source, validate an editorial decision map, build offline HTML.

Python 3.9+, standard library only. Does not fetch links or inspect repository files.
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


VERSION = "egm-draft-html/v1"
ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")
MARKER = "__GUIDE_DATA__"


class GuideError(ValueError):
    pass


def read_document(path):
    path = Path(path).resolve(strict=True)
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise GuideError("Source must be UTF-8 Markdown") from exc
    lines = text.splitlines(keepends=True)
    headings = []
    fence = None
    header = True
    header_lines = []
    for index, line in enumerate(lines):
        parse_line = line.lstrip("\ufeff") if index == 0 else line
        fence_match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", parse_line.rstrip("\r\n"))
        if fence_match:
            run, tail = fence_match.groups()
            if fence is None:
                fence = (run[0], len(run))
            elif run[0] == fence[0] and len(run) >= fence[1] and not tail.strip():
                fence = None
            continue
        if fence is not None:
            continue
        match = re.match(r"^ {0,3}(#{1,6})[ \t]+(.+?)\s*$", parse_line)
        if match:
            title = re.sub(r"\s+#+\s*$", "", match.group(2)).strip()
            headings.append((index, len(match.group(1)), title))
            if len(match.group(1)) >= 2:
                header = False
        if header:
            header_lines.append(line)
    if not text.strip():
        raise GuideError("Source is empty; there are no decisions to summarize")
    sections = []
    used = set()
    parents = []
    if not headings or headings[0][0] > 0:
        end = headings[0][0] if headings else len(lines)
        preamble = "".join(lines[:end])
        if preamble.strip():
            sections.append({"id": "document-preamble", "title": "Document preamble",
                             "line": 1, "level": 0, "parent": None, "text": preamble})
            used.add("document-preamble")
    for number, (index, level, title) in enumerate(headings):
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "section"
        candidate, suffix = slug, 2
        while candidate in used:
            candidate = "{}-{}".format(slug, suffix)
            suffix += 1
        used.add(candidate)
        while parents and parents[-1][0] >= level:
            parents.pop()
        end = headings[number + 1][0] if number + 1 < len(headings) else len(lines)
        sections.append({"id": candidate, "title": title, "line": index + 1,
                         "level": level, "parent": parents[-1][1] if parents else None,
                         "text": "".join(lines[index + 1:end])})
        parents.append((level, candidate))
    title = next((title for _, level, title in headings if level == 1), path.stem)

    def metadata(field, default):
        match = re.search(r"^\s*[-*]?\s*\*\*" + re.escape(field)
                          + r":\*\*\s*(.+)$", "".join(header_lines), flags=re.M | re.I)
        return match.group(1).strip() if match else default

    return {"schema": VERSION, "title": title, "sourceName": path.name,
            "sourceSha256": hashlib.sha256(raw).hexdigest(), "sourceRaw": text,
            "sourceStatus": metadata("Status", "Status not specified"),
            "sourceDate": metadata("Finalized", metadata("Date", "Date not specified")),
            "sections": sections}


def nonempty(value, location):
    if not isinstance(value, str) or not value.strip():
        raise GuideError("{} must be a nonempty string".format(location))
    return value


def identifier(value, location):
    if not isinstance(value, str) or not ID.fullmatch(value):
        raise GuideError("{} must contain lowercase letters, digits and hyphens".format(location))
    return value


def validate_map(mapping, document):
    if not isinstance(mapping, dict):
        raise GuideError("Decision map must be a JSON object")
    if mapping.get("sourceSha256") != document["sourceSha256"]:
        raise GuideError("Map sourceSha256 does not match the source. Reinspect and reconcile the map; do not reuse stale source IDs.")
    groups = mapping.get("groups")
    if not isinstance(groups, list) or not groups:
        raise GuideError("groups must be a nonempty array")
    source_ids = {section["id"] for section in document["sections"]}
    group_ids = set()
    detail_ids = set()
    referenced = set()
    for gi, group in enumerate(groups):
        where = "groups[{}]".format(gi)
        if not isinstance(group, dict):
            raise GuideError("{} must be an object".format(where))
        gid = identifier(group.get("id"), where + ".id")
        if gid in group_ids:
            raise GuideError("Duplicate group id: " + gid)
        group_ids.add(gid)
        for field in ("label", "title", "answer", "why", "tradeoff"):
            nonempty(group.get(field), where + "." + field)
        children = group.get("details")
        if not isinstance(children, list) or not children:
            raise GuideError(where + ".details must be a nonempty array")
        for di, detail in enumerate(children):
            location = "{}.details[{}]".format(where, di)
            if not isinstance(detail, dict):
                raise GuideError(location + " must be an object")
            did = identifier(detail.get("id"), location + ".id")
            if did in detail_ids:
                raise GuideError("Duplicate detail id: " + did)
            detail_ids.add(did)
            for field in ("title", "answer", "why", "tradeoff"):
                nonempty(detail.get(field), location + "." + field)
            refs = detail.get("sources")
            if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) for ref in refs):
                raise GuideError(location + ".sources must be a nonempty array of section IDs")
            missing = set(refs) - source_ids
            if missing:
                raise GuideError(location + " references missing source sections: " + ", ".join(sorted(missing)))
            referenced.update(refs)
    for group in groups:
        connections = group.get("connections", [])
        if not isinstance(connections, list) or any(not isinstance(ref, str) for ref in connections):
            raise GuideError("connections must be an array of group IDs")
        if set(connections) - group_ids or group["id"] in connections:
            raise GuideError("Invalid or self-referencing connection in " + group["id"])
    warnings = []
    if len(groups) > 9:
        warnings.append("More than nine major decisions: consider grouping for the overview")
    for group in groups:
        if len(group["details"]) > 10:
            warnings.append("{} has more than ten children; check reading load".format(group["id"]))
    return {"groups": len(groups), "details": len(detail_ids),
            "referencedSourceSections": len(referenced), "warnings": warnings}


def build_payload(mapping, document):
    validate_map(mapping, document)
    payload = dict(document)
    payload["title"] = nonempty(mapping.get("title", document["title"]), "title")
    payload["groups"] = []
    # Only documented fields reach the template. Source status/date cannot be
    # overwritten by an editorial map or turned from Proposed into Approved.
    for group in mapping["groups"]:
        item = {key: group[key] for key in ("id", "label", "title", "answer", "why", "tradeoff")}
        item["connections"] = group.get("connections", [])
        item["details"] = [{key: detail[key] for key in
                            ("id", "title", "answer", "why", "tradeoff", "sources")}
                           for detail in group["details"]]
        payload["groups"].append(item)
    return payload


def write_output(path, content, protected, force=False):
    path = Path(path).resolve()
    if path in protected:
        raise GuideError("Output must not overwrite the input source or decision map")
    if path.exists() and not force:
        raise GuideError("Output already exists; choose another name or use --force for an authorized regeneration")
    path.parent.mkdir(parents=True, exist_ok=True)
    # A failed validation cannot leave a partially overwritten artifact.
    import os
    import tempfile
    fd, temporary = tempfile.mkstemp(prefix=".decision-guide-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as stream:
            stream.write(content)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inspect", help="Extract exact source sections and metadata without following links")
    inspect.add_argument("--source", type=Path, required=True)
    inspect.add_argument("--output", type=Path, required=True)
    inspect.add_argument("--force", action="store_true")
    for command in ("validate", "build"):
        sub = commands.add_parser(command)
        sub.add_argument("--source", type=Path, required=True)
        sub.add_argument("--map", type=Path, required=True)
        if command == "build":
            sub.add_argument("--output", type=Path, required=True)
            sub.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    try:
        document = read_document(args.source)
        protected = {args.source.resolve()}
        if args.command == "inspect":
            write_output(args.output, json.dumps(document, ensure_ascii=False, indent=2) + "\n", protected, args.force)
            print(json.dumps({"sourceSha256": document["sourceSha256"], "sections": len(document["sections"]),
                              "output": str(args.output)}))
            return 0
        protected.add(args.map.resolve())
        mapping = json.loads(args.map.read_text(encoding="utf-8"))
        summary = validate_map(mapping, document)
        if args.command == "build":
            if args.output.suffix.lower() != ".html":
                raise GuideError("Build output must have an .html extension")
            template_path = Path(__file__).resolve().parent.parent / "assets" / "guide.html"
            template = template_path.read_text(encoding="utf-8")
            if template.count(MARKER) != 1:
                raise GuideError("Renderer template must have exactly one data marker")
            payload = json.dumps(build_payload(mapping, document), ensure_ascii=False)
            # Embedded Markdown may contain </script> or arbitrary HTML. It is
            # data, never executable markup; text views also escape it.
            payload = payload.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
            write_output(args.output, template.replace(MARKER, payload), protected, args.force)
            summary["output"] = str(args.output)
        print(json.dumps(summary, ensure_ascii=False))
        return 0
    except (GuideError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print("Error: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
