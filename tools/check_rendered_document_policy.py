#!/usr/bin/env python3
"""Fail when an authored page can expose Markdown as a reader-facing option."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
RAW_GUARD = '.openmd,[data-raw-download],[data-mode="m"],.raw{display:none!important}'
SKIP_PARTS = {"node_modules", "source_docs", "patents_source_docs"}


def authored_html() -> list[Path]:
    pages: list[Path] = []
    for page in ROOT.rglob("*.html"):
        rel = page.relative_to(ROOT)
        if any(part in SKIP_PARTS for part in rel.parts):
            continue
        pages.append(page)
    return sorted(pages)


def main() -> int:
    errors: list[str] = []
    if not (ROOT / "site-documents.js").is_file():
        errors.append("site-documents.js: embedded document bundle is missing")

    for page in authored_html():
        rel = page.relative_to(ROOT)
        source = page.read_text(encoding="utf-8", errors="replace")

        if "The research file itself is available directly" in source:
            errors.append(f"{rel}: raw-file fallback language is forbidden")

        has_legacy_raw_ui = bool(
            re.search(r'class="[^"]*\bopenmd\b', source)
            or 'data-raw-download' in source
            or re.search(r'data-mode="m"', source)
        )
        if has_legacy_raw_ui and RAW_GUARD not in source:
            errors.append(f"{rel}: raw Markdown control is not suppressed")

        if rel.as_posix() == "markdown-viewer.html" and (
            'data-raw-download' in source or re.search(r'class="[^"]*\bopenmd\b', source)
        ):
            errors.append(f"{rel}: the generic viewer must not offer a raw-file link")

        if rel.as_posix() == "markdown-viewer.html" and 'src="site-documents.js"' not in source:
            errors.append(f"{rel}: embedded document source is not loaded")

        if len(rel.parts) == 2 and rel.name == "index.html" and "fetch(" in source:
            if 'src="../site-documents.js"' not in source:
                errors.append(f"{rel}: Markdown viewer is not available when opened from disk")

    if errors:
        print("RENDERED-DOCUMENT POLICY FAILED")
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"RENDERED-DOCUMENT POLICY OK ({len(authored_html())} authored HTML pages checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
