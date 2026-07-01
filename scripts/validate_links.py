#!/usr/bin/env python3
"""Validate relative markdown links and heading anchors across the repo's docs.

Checks every [text](target) link in *.md files (README, docs/, adrs/):
- relative file links point to a file that exists
- '#fragment' parts point to a heading that exists in the target file
  (or the current file, for same-file links)

External (http/https) and mailto links are skipped.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD_DIRS = [ROOT, ROOT / "docs", ROOT / "adrs"]

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")


def slugify(heading: str) -> str:
    """Approximate GitHub's heading-to-anchor algorithm."""
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug


def collect_markdown_files() -> list[Path]:
    files: list[Path] = []
    for d in MD_DIRS:
        if not d.exists():
            continue
        files.extend(sorted(p for p in d.glob("**/*.md") if p.is_file()))
    # de-duplicate while preserving order (ROOT glob won't recurse into subdirs)
    seen = set()
    unique_files = []
    for f in files:
        if f not in seen:
            seen.add(f)
            unique_files.append(f)
    return unique_files


def headings_for(path: Path) -> set[str]:
    slugs: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING_RE.match(line)
        if match:
            slugs.add(slugify(match.group(2)))
    return slugs


def main() -> int:
    files = collect_markdown_files()
    heading_cache: dict[Path, set[str]] = {}
    errors: list[str] = []

    for file in files:
        text = file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(2).strip()

            if target.startswith(("http://", "https://", "mailto:")):
                continue

            path_part, _, fragment = target.partition("#")

            if path_part == "":
                resolved = file
            else:
                resolved = (file.parent / path_part).resolve()

            if not resolved.exists():
                errors.append(f"{file}: broken link target '{target}' -> {resolved}")
                continue

            if fragment:
                if resolved not in heading_cache:
                    heading_cache[resolved] = headings_for(resolved)
                if fragment not in heading_cache[resolved]:
                    errors.append(
                        f"{file}: broken anchor '#{fragment}' in link '{target}' "
                        f"(no matching heading in {resolved.relative_to(ROOT)})"
                    )

    if errors:
        print(f"Found {len(errors)} broken link(s):\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Checked {len(files)} markdown file(s). All links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
