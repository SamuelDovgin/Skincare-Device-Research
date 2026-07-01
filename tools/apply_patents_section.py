#!/usr/bin/env python3
"""Aggregate '## Patents'-style blocks from every folder's markdown docs into that
folder's viewable Patents page (a `#patents` section + sidebar link/chip in its
index.html). Idempotent — safe to re-run after the viewer HTML is regenerated
externally (see the site-viewer-regenerator memory).

Authoring convention (in any *.md file, anywhere a patent is worth citing):

    ## 9. Patents referenced in this analysis

    ### US 9,308,390 B2 — Devices and methods for radiation-based dermatological treatments
    - **Assignee:** Tria Beauty, Inc.
    - **Discloses:** one or two sentences on what it actually claims/discloses.
    - **Link:** https://patents.google.com/patent/US9308390B2/en
    - **Mirrored PDF:** quantified_gap_source_docs/us-patent-9308390-tria-laser.pdf

`Mirrored PDF` is optional (omit if not locally mirrored). The section heading only
needs to contain the word "patent" (any ## heading text works, any doc, any folder).
The same patent cited in multiple docs within one folder is de-duplicated into a
single card that lists every doc it's used in.

Usage:  python3 tools/apply_patents_section.py            (apply, in-place)
        python3 tools/apply_patents_section.py --check     (report only, exit 1 if work pending)
"""
import re, sys, pathlib
from collections import OrderedDict

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECK = "--check" in sys.argv

SECTION_RE = re.compile(r'^##\s+.*\bpatents?\b.*$', re.I | re.M)
NEXT_H2_RE = re.compile(r'^##\s+(?!#)', re.M)
DIVIDER_RE = re.compile(r'^---\s*$', re.M)
BLOCK_RE = re.compile(r'^###\s+(.+?)\s*$', re.M)
FIELD_RE = re.compile(r'^-\s+\*\*(Assignee|Discloses|Link|Mirrored PDF):\*\*\s*(.+?)\s*$', re.M)
H1_RE = re.compile(r'^#\s+(.+?)\s*$', re.M)
NUMBER_PREFIX_RE = re.compile(r'^(US|USD|EP|CN|WO)\s*[\d,]+')

CSS_BLOCK = """
/* patents-section */
.patents{display:flex;flex-direction:column;gap:10px;margin-top:10px}
.patent{border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:var(--card)}
.patent .pt-num{font-weight:700;color:var(--ink);text-decoration:none}
.patent .pt-num:hover{color:var(--accent)}
.patent .pt-meta{font-size:12px;color:var(--muted);margin:2px 0 6px;font-weight:600}
.patent .pt-desc{font-size:13.5px;color:var(--ink);line-height:1.5}
.patent .pt-used{font-size:12px;color:var(--muted);margin-top:8px}
.patent .pt-used a{color:var(--muted);text-decoration:underline}
.patent .pt-links{margin-top:6px}
.patent .pt-links a{font-size:12px;font-weight:600;color:var(--accent);text-decoration:none;margin-right:14px}
"""

pending = 0


def extract_patents(md_path):
    """Return a list of patent dicts found in this doc's '## ...Patents...' section(s)."""
    text = md_path.read_text()
    h1m = H1_RE.search(text)
    doc_title = h1m.group(1) if h1m else md_path.name
    out = []
    for sec in SECTION_RE.finditer(text):
        start = sec.end()
        end = len(text)
        nh2 = NEXT_H2_RE.search(text, start)
        if nh2:
            end = min(end, nh2.start())
        div = DIVIDER_RE.search(text, start)
        if div:
            end = min(end, div.start())
        body = text[start:end]
        blocks = list(BLOCK_RE.finditer(body))
        for i, b in enumerate(blocks):
            title = b.group(1).strip()
            if not NUMBER_PREFIX_RE.match(title):
                continue
            bstart = b.end()
            bend = blocks[i + 1].start() if i + 1 < len(blocks) else len(body)
            chunk = body[bstart:bend]
            fields = {k: v.strip() for k, v in FIELD_RE.findall(chunk)}
            if "Link" not in fields:
                continue
            out.append({
                "title": title,
                "assignee": fields.get("Assignee", ""),
                "discloses": fields.get("Discloses", ""),
                "link": fields["Link"],
                "mirrored": fields.get("Mirrored PDF", ""),
                "doc_file": md_path.name,
                "doc_title": doc_title,
            })
    return out


def dedupe_key(title):
    head = title.split("—")[0].strip()
    return re.sub(r'\s+', ' ', head).upper()


def collect_folder_patents(folder):
    agg = OrderedDict()
    for md in sorted(folder.glob("*.md")):
        for p in extract_patents(md):
            key = dedupe_key(p["title"])
            if key not in agg:
                agg[key] = {**p, "used_in": []}
            agg[key]["used_in"].append((p["doc_file"], p["doc_title"]))
    return list(agg.values())


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_section(patents):
    cards = []
    for p in patents:
        used = " · ".join(f'<a href="{esc(f)}">{esc(t)}</a>' for f, t in p["used_in"])
        links = f'<a href="{esc(p["link"])}" target="_blank" rel="noopener">🔗 View patent</a>'
        if p["mirrored"]:
            links = f'<a href="{esc(p["mirrored"])}" target="_blank">📄 Mirrored PDF</a>' + links
        cards.append(
            f'<div class="patent"><a class="pt-num" href="{esc(p["link"])}" target="_blank" rel="noopener">{esc(p["title"])}</a>'
            f'<div class="pt-meta">{esc(p["assignee"])}</div>'
            f'<div class="pt-desc">{esc(p["discloses"])}</div>'
            f'<div class="pt-used">Used in: {used}</div>'
            f'<div class="pt-links">{links}</div></div>'
        )
    note = "Patents behind the science and the specific devices covered in this folder — assignee, what each discloses, and which doc relies on it."
    return (
        '<section class="doc" id="patents"><h1>Patents</h1>'
        f'<p class="note">{note}</p>'
        f'<div class="patents">{"".join(cards)}</div></section>'
    )


def inject_css(html):
    m = re.search(r'\n/\* patents-section \*/.*?(?=\n</style>|\Z)', html, re.S)
    if m:
        if m.group(0) == CSS_BLOCK.rstrip("\n"):
            return html, False
        return html[: m.start()] + CSS_BLOCK.rstrip("\n") + html[m.end() :], True
    idx = html.find("</style>")
    if idx == -1:
        return html, False
    return html[:idx] + CSS_BLOCK + html[idx:], True


def inject_section(html, section_html):
    m = re.search(r'<section class="doc" id="patents">.*?</section>', html, re.S)
    if m:
        if m.group(0) == section_html:
            return html, None
        return html[:m.start()] + section_html + html[m.end():], "updated"
    for anchor_id in ("source-docs", "pdfs", "data", "gallery"):
        m = re.search(r'<section class="doc[^"]*" id="' + anchor_id + r'">.*?</section>', html, re.S)
        if m:
            return html[:m.end()] + "\n    " + section_html + html[m.end():], f"inserted-after-{anchor_id}"
    m = re.search(r'<section class="doc" id="doc0">', html)
    if m:
        return html[: m.start()] + section_html + "\n    " + html[m.start() :], "inserted-before-doc0"
    return html, None


def find_sibling_chip(html, marker):
    """Find one complete <div class="st-chip" ...>...</div> containing `marker`.
    Chips don't nest divs inside themselves, so a non-greedy match from THIS
    specific chip's own opening tag to the next </div> is safe — unlike trying
    to span the whole (nested-div) .st-grid container in one regex."""
    for m in re.finditer(r'<div class="st-chip"[^>]*>.*?</div>', html, re.S):
        if marker in m.group(0):
            return m
    return None


def inject_nav_trigger(html, count):
    if 'data-go="patents"' in html or 'href="#patents"' in html:
        return html, False
    chip_sibling = find_sibling_chip(html, 'data-go="pdfs"') or find_sibling_chip(html, 'data-go="data"')
    if chip_sibling:
        chip = '<div class="st-chip" data-go="patents" role="button" tabindex="0">📜 Patents<span>Primary patents behind the devices in this folder</span></div>'
        insert_at = chip_sibling.end()
        return html[:insert_at] + chip + html[insert_at:], True
    idx = html.rfind("</nav>")
    if idx == -1:
        return html, False
    link = f'<a class="navbtn" href="#patents">📜 Patents ({count})</a>\n  '
    return html[:idx] + link + html[idx:], True


def process_folder(folder):
    global pending
    patents = collect_folder_patents(folder)
    if not patents:
        return
    index = folder / "index.html"
    if not index.exists():
        return
    html = index.read_text()
    section_html = render_section(patents)
    html, css_changed = inject_css(html)
    html, sec_action = inject_section(html, section_html)
    html, nav_changed = inject_nav_trigger(html, len(patents))
    changed = css_changed or bool(sec_action) or nav_changed
    if changed:
        pending += 1
        print(f"  {folder.name}: {len(patents)} patent(s) — {sec_action or 'section unchanged'}"
              f"{', +css' if css_changed else ''}{', +nav' if nav_changed else ''}")
        if not CHECK:
            index.write_text(html)
    else:
        print(f"  {folder.name}: {len(patents)} patent(s), already up to date")


if __name__ == "__main__":
    print(("CHECK" if CHECK else "APPLY") + " patents section:")
    for folder in sorted(ROOT.glob("0*_*")):
        if folder.is_dir():
            process_folder(folder)
    if pending == 0:
        print("  up to date — nothing to do.")
    print(f"done ({pending} folder(s) {'pending' if CHECK else 'applied'}).")
    sys.exit(1 if (CHECK and pending) else 0)
