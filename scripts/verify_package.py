#!/usr/bin/env python3
"""Verify the draft package's local integrity and internal references.

This detects accidental mismatch against MANIFEST.sha256. It does not establish
authorship, trusted time, adoption, authenticity, or runtime loading.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.sha256"
CORE = ROOT / "docs" / "HUMAN_RIGHTS_FLOOR.md"
CHARTER = ROOT / "templates" / "USER_AI_USE_CHARTER.md"
LEGACY_FILES = {
    "templates/AI_REVIEW_TEMPLATE.md",
    "templates/IMPLEMENTATION_PROFILE_TEMPLATE.md",
    "templates/USER_AI_COVENANT_TEMPLATE.md",
}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def parse_manifest() -> dict[str, str]:
    records: dict[str, str] = {}
    if not MANIFEST.is_file():
        raise ValueError("MANIFEST.sha256 is missing")
    for number, raw in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        match = re.fullmatch(r"([0-9a-f]{64})  \./(.+)", raw)
        if not match:
            raise ValueError(f"invalid manifest line {number}: {raw!r}")
        checksum, name = match.groups()
        if name in records:
            raise ValueError(f"duplicate manifest path: {name}")
        records[name] = checksum
    return records


def local_markdown_links() -> list[str]:
    errors: list[str] = []
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for source in ROOT.rglob("*.md"):
        if source == MANIFEST:
            continue
        text = source.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target_path = target.split("#", 1)[0]
            if target_path and not (source.parent / target_path).resolve().exists():
                errors.append(f"broken link in {source.relative_to(ROOT)}: {target}")
    return errors


def main() -> int:
    errors: list[str] = []
    try:
        recorded = parse_manifest()
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    actual = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and path != MANIFEST
    }

    for missing in sorted(actual - recorded.keys()):
        errors.append(f"missing from manifest: {missing}")
    for stale in sorted(recorded.keys() - actual):
        errors.append(f"manifest references absent file: {stale}")
    for name in sorted(actual & recorded.keys()):
        observed = digest(ROOT / name)
        if observed != recorded[name]:
            errors.append(f"checksum mismatch: {name}")

    for name in sorted(LEGACY_FILES & actual):
        errors.append(f"legacy template still present: {name}")

    core_hash = digest(CORE)
    charter_text = CHARTER.read_text(encoding="utf-8")
    core_reference = re.search(r"Core SHA-256: `([0-9a-f]{64})`", charter_text)
    if not core_reference:
        errors.append("charter has no exact Core SHA-256 reference")
    elif core_reference.group(1) != core_hash:
        errors.append("charter Core SHA-256 does not match HUMAN_RIGHTS_FLOOR.md")

    errors.extend(local_markdown_links())

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {len(actual)} files match the manifest; Core reference and local links are valid.")
    print("Note: this check does not prove authorship, trusted time, adoption, or enforcement.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
