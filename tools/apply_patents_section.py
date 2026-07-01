#!/usr/bin/env python3
"""Aggregate '## Patents'-style blocks from every folder's markdown docs into that
folder's viewable Patents page (a `#patents` section + sidebar link/chip in its
index.html). Idempotent — safe to re-run after the viewer HTML is regenerated
externally (see the site-viewer-regenerator memory).

Authoring convention (in any *.md file, anywhere a patent OR trademark is worth
citing):

    ## 9. Patents referenced in this analysis

    ### US 9,308,390 B2 — Devices and methods for radiation-based dermatological treatments
    - **Company:** Tria Beauty
    - **Type:** Utility Patent
    - **Filed:** 2012-04-10
    - **Granted:** 2016-04-12
    - **Assignee:** Tria Beauty, Inc. (now Aesthete Holding Corporation, 2025 reassignment)
    - **Discloses:** one or two sentences on what it actually claims/discloses.
    - **Link:** https://patents.google.com/patent/US9308390B2/en
    - **Mirrored PDF:** quantified_gap_source_docs/us-patent-9308390-tria-laser.pdf

`Company` is the SHORT canonical grouping key used to build the company-filter
menu — use the SAME string for every filing from one company's lineage (e.g.
always "Tria Beauty", never "SpectraGenics" for one block and "Tria Beauty" for
another) even if `Assignee` spells out a longer reassignment history in prose.
`Type` is free text but should be one of "Utility Patent" / "Design Patent" /
"Trademark" so the timeline can badge it consistently. `Filed`/`Granted` are
YYYY-MM-DD (a bare YYYY is fine if that's all that's known); use "Pending" for
`Granted` if not yet granted/registered. `Assignee` and `Mirrored PDF` are
optional; `Company`, `Type`, `Filed`, `Discloses`, and `Link` are expected on
every block (missing ones degrade gracefully — the page just shows less).

The section heading only needs to contain the word "patent" (any ## heading text
works, any doc, any folder). The same patent cited in multiple docs within one
folder is de-duplicated into a single card that lists every doc it's used in.

A second, separate convention: a `## Future tech signals` heading (must contain
that exact phrase, case-insensitive) marks a free-form markdown section — prose,
tables, whatever — that gets carried onto the same Patents page verbatim, rendered
client-side by the page's own marked.js (see FUTURE_HEAD_RE below). Unlike patent
blocks this is NOT parsed into structured fields; it's just forwarded as raw
markdown inside a <script type="text/markdown"> tag and rendered on load.

Usage:  python3 tools/apply_patents_section.py            (apply, in-place)
        python3 tools/apply_patents_section.py --check     (report only, exit 1 if work pending)
"""
import re, sys, pathlib
from collections import OrderedDict

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECK = "--check" in sys.argv

SECTION_RE = re.compile(r'^##\s+.*\bpatents?\b.*$', re.I | re.M)
FUTURE_HEAD_RE = re.compile(r'^##\s+.*\bfuture tech\b.*$', re.I | re.M)
NEXT_H2_RE = re.compile(r'^##\s+(?!#)', re.M)
DIVIDER_RE = re.compile(r'^---\s*$', re.M)
BLOCK_RE = re.compile(r'^###\s+(.+?)\s*$', re.M)
FIELD_RE = re.compile(r'^-\s+\*\*(Company|Type|Filed|Granted|Assignee|Discloses|Link|Mirrored PDF):\*\*\s*(.+?)\s*$', re.M)
H1_RE = re.compile(r'^#\s+(.+?)\s*$', re.M)
NUMBER_PREFIX_RE = re.compile(r'^(US|USD|EP|CN|WO)\s*[\d,]+')
YEAR_RE = re.compile(r'(\d{4})')

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
.patent .pt-dates{font-size:11.5px;color:var(--muted);margin:2px 0}
.pt-type{display:inline-block;font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.03em;padding:2px 7px;border-radius:20px;margin-bottom:6px}
.pt-t-util{background:#e8f0fe;color:#1a56c4}
.pt-t-design{background:#fdeee3;color:#b45309}
.pt-t-tm{background:#e9f7ef;color:#0f7b45}
.pt-tabs{display:flex;gap:8px;margin:14px 0 10px}
.pt-tab{border:1px solid var(--line);background:var(--card);border-radius:8px;padding:6px 14px;font-size:13px;font-weight:600;color:var(--muted);cursor:pointer}
.pt-tab.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.pt-menu{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}
.pt-mchip{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:4px 12px;font-size:12px;font-weight:600;color:var(--ink);cursor:pointer}
.pt-mchip.active{background:var(--ink);color:#fff;border-color:var(--ink)}
.patent[hidden],.pt-tl-row[hidden]{display:none}
.patents[hidden],.pt-timeline[hidden]{display:none}
.pt-timeline{display:flex;flex-direction:column;gap:2px}
.pt-tl-year{font-size:16px;font-weight:800;color:var(--accent);margin:18px 0 4px;padding-top:6px;border-top:1px solid var(--line)}
.pt-tl-year:first-child{margin-top:0;border-top:0}
.pt-tl-row{display:flex;align-items:center;gap:10px;padding:6px 4px;border-bottom:1px solid var(--line);font-size:13px;flex-wrap:wrap}
.pt-tl-date{font-size:11.5px;color:var(--muted);min-width:92px}
.pt-tl-row a{color:var(--ink);font-weight:600;text-decoration:none;flex:1;min-width:200px}
.pt-tl-row a:hover{color:var(--accent)}
.pt-tl-company{font-size:11.5px;color:var(--muted);font-style:italic}
.future-tech-wrap{margin-top:32px;padding-top:20px;border-top:2px dashed var(--line)}
.future-tech-wrap>p.note:first-of-type{margin-top:0}
"""

pending = 0


def section_body(text, heading_match):
    """Slice from just after a ## heading to the next ##(not###)/---/EOF."""
    start = heading_match.end()
    end = len(text)
    nh2 = NEXT_H2_RE.search(text, start)
    if nh2:
        end = min(end, nh2.start())
    div = DIVIDER_RE.search(text, start)
    if div:
        end = min(end, div.start())
    return text[start:end]


def extract_future_tech(md_path):
    """Return raw markdown body text for each '## Future tech...' section in this doc."""
    text = md_path.read_text()
    h1m = H1_RE.search(text)
    doc_title = h1m.group(1) if h1m else md_path.name
    out = []
    for sec in FUTURE_HEAD_RE.finditer(text):
        body = section_body(text, sec).strip()
        if body:
            out.append({"body": body, "doc_file": md_path.name, "doc_title": doc_title})
    return out


def collect_folder_future_tech(folder):
    items = []
    for md in sorted(folder.glob("*.md")):
        items.extend(extract_future_tech(md))
    return items


def extract_patents(md_path):
    """Return a list of patent dicts found in this doc's '## ...Patents...' section(s)."""
    text = md_path.read_text()
    h1m = H1_RE.search(text)
    doc_title = h1m.group(1) if h1m else md_path.name
    out = []
    for sec in SECTION_RE.finditer(text):
        body = section_body(text, sec)
        blocks = list(BLOCK_RE.finditer(body))
        for i, b in enumerate(blocks):
            title = b.group(1).strip()
            bstart = b.end()
            bend = blocks[i + 1].start() if i + 1 < len(blocks) else len(body)
            chunk = body[bstart:bend]
            fields = {k: v.strip() for k, v in FIELD_RE.findall(chunk)}
            # Validity: either a real patent-number-style title (catches old-schema
            # blocks with no Type field), OR an explicit Company/Type pair (catches
            # trademarks and non-US patent numbers like TWI/JP/KR that don't start
            # with a familiar prefix). Either way Link is mandatory.
            looks_like_patent_number = bool(NUMBER_PREFIX_RE.match(title))
            has_explicit_fields = "Company" in fields and "Type" in fields
            if not (looks_like_patent_number or has_explicit_fields):
                continue
            if "Link" not in fields:
                continue
            company = fields.get("Company", "").strip()
            if not company:
                company = fields.get("Assignee", "Unknown").split("(")[0].split("—")[0].split("→")[-1].strip() or "Unknown"
            out.append({
                "title": title,
                "company": company,
                "type": fields.get("Type", "Utility Patent"),
                "filed": fields.get("Filed", ""),
                "granted": fields.get("Granted", ""),
                "assignee": fields.get("Assignee", ""),
                "discloses": fields.get("Discloses", ""),
                "link": fields["Link"],
                "mirrored": fields.get("Mirrored PDF", ""),
                "doc_file": md_path.name,
                "doc_title": doc_title,
            })
    return out


def sort_key(item):
    """Chronological sort key: prefer Filed, fall back to Granted, undated last."""
    for field in ("filed", "granted"):
        m = YEAR_RE.search(item.get(field, ""))
        if m:
            val = item[field]
            year = m.group(1)
            rest = val[m.end():].lstrip("-/. ") or "01-01"
            if re.match(r'^\d{2}-\d{2}', rest):
                return f"{year}-{rest[:5]}"
            return f"{year}-01-01"
    return "9999-99-99"


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


def render_future_tech(items):
    if not items:
        return ""
    blocks = []
    for it in items:
        md = it["body"].replace("</script", "<\\/script")
        blocks.append(
            f'<p class="note" style="margin-top:22px">From <a href="{esc(it["doc_file"])}">{esc(it["doc_title"])}</a>:</p>'
            f'<script type="text/markdown" class="future-md">{md}</script>'
        )
    return (
        '<div class="future-tech-wrap"><h2>Where this is headed</h2>'
        + "".join(blocks)
        + "</div>"
    )


TYPE_CLASS = {"utility patent": "pt-t-util", "design patent": "pt-t-design", "trademark": "pt-t-tm"}


def type_class(t):
    return TYPE_CLASS.get(t.strip().lower(), "pt-t-util")


def render_section(patents, future_tech=None):
    by_company = OrderedDict()
    for p in sorted(patents, key=lambda x: x["company"]):
        by_company.setdefault(p["company"], []).append(p)

    cards = []
    for p in patents:
        used = " · ".join(f'<a href="{esc(f)}">{esc(t)}</a>' for f, t in p["used_in"])
        links = f'<a href="{esc(p["link"])}" target="_blank" rel="noopener">🔗 View</a>'
        if p["mirrored"]:
            links = f'<a href="{esc(p["mirrored"])}" target="_blank">📄 Mirrored PDF</a>' + links
        dates = " · ".join(filter(None, [
            f"Filed {esc(p['filed'])}" if p["filed"] else "",
            f"Granted {esc(p['granted'])}" if p["granted"] else "",
        ]))
        cards.append(
            f'<div class="patent" data-company="{esc(p["company"])}" data-type="{esc(p["type"])}">'
            f'<span class="pt-type {type_class(p["type"])}">{esc(p["type"])}</span>'
            f'<a class="pt-num" href="{esc(p["link"])}" target="_blank" rel="noopener">{esc(p["title"])}</a>'
            f'<div class="pt-meta">{esc(p["company"])}{" — " + esc(p["assignee"]) if p["assignee"] and p["assignee"] != p["company"] else ""}</div>'
            + (f'<div class="pt-dates">{dates}</div>' if dates else "")
            + f'<div class="pt-desc">{esc(p["discloses"])}</div>'
            f'<div class="pt-used">Used in: {used}</div>'
            f'<div class="pt-links">{links}</div></div>'
        )

    menu = ['<button class="pt-mchip active" data-company="__all__">All (' + str(len(patents)) + ")</button>"]
    for company, items in by_company.items():
        menu.append(f'<button class="pt-mchip" data-company="{esc(company)}">{esc(company)} ({len(items)})</button>')

    timeline_items = sorted(patents, key=sort_key)
    tl_rows = []
    last_year = None
    for p in timeline_items:
        key = sort_key(p)
        year = key[:4] if key != "9999-99-99" else "Undated"
        if year != last_year:
            tl_rows.append(f'<div class="pt-tl-year">{esc(year)}</div>')
            last_year = year
        date_label = p["filed"] or p["granted"] or "date unknown"
        tl_rows.append(
            f'<div class="pt-tl-row" data-company="{esc(p["company"])}" data-type="{esc(p["type"])}">'
            f'<span class="pt-tl-date">{esc(date_label)}</span>'
            f'<span class="pt-type {type_class(p["type"])}">{esc(p["type"])}</span>'
            f'<a href="{esc(p["link"])}" target="_blank" rel="noopener">{esc(p["title"])}</a>'
            f'<span class="pt-tl-company">{esc(p["company"])}</span></div>'
        )

    note = "Patents and trademarks behind the science and the specific devices covered in this folder — filter by company or view chronologically."
    return (
        '<section class="doc" id="patents"><h1>Patents</h1>'
        f'<p class="note">{note}</p>'
        '<div class="pt-tabs">'
        '<button class="pt-tab active" data-view="cards">By company</button>'
        '<button class="pt-tab" data-view="timeline">Timeline</button>'
        "</div>"
        f'<div class="pt-menu">{"".join(menu)}</div>'
        f'<div class="patents" data-view-panel="cards">{"".join(cards)}</div>'
        f'<div class="pt-timeline" data-view-panel="timeline" hidden>{"".join(tl_rows)}</div>'
        + render_future_tech(future_tech or [])
        + "</section>"
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


FUTURE_MD_JS = """<script>/*future-md-render*/
(function(){
  function run(){
    document.querySelectorAll('script.future-md').forEach(function(s){
      if(typeof marked==='undefined') return;
      var d=document.createElement('div'); d.className='future-tech';
      d.innerHTML=marked.parse(s.textContent); s.replaceWith(d);
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',run); else run();
})();
</script>
"""


def inject_future_md_renderer(html):
    if "/*future-md-render*/" in html:
        return html, False
    idx = html.rfind("</body>")
    if idx == -1:
        return html, False
    return html[:idx] + FUTURE_MD_JS + html[idx:], True


PATENTS_UI_JS = """<script>/*patents-ui*/
(function(){
  function run(){
    document.querySelectorAll('#patents').forEach(function(sec){
      var tabs=sec.querySelectorAll('.pt-tab');
      var panels=sec.querySelectorAll('[data-view-panel]');
      var chips=sec.querySelectorAll('.pt-mchip');
      var company='__all__';
      function applyFilter(){
        sec.querySelectorAll('.patent,[data-view-panel="timeline"] .pt-tl-row').forEach(function(el){
          el.hidden = company!=='__all__' && el.dataset.company!==company;
        });
        sec.querySelectorAll('.pt-tl-year').forEach(function(y){
          var next=y.nextElementSibling, anyVisible=false;
          while(next && !next.classList.contains('pt-tl-year')){
            if(!next.hidden) anyVisible=true;
            next=next.nextElementSibling;
          }
          y.hidden=!anyVisible;
        });
      }
      tabs.forEach(function(t){
        t.addEventListener('click',function(){
          tabs.forEach(function(x){x.classList.remove('active');});
          t.classList.add('active');
          var view=t.dataset.view;
          panels.forEach(function(p){ p.hidden = p.dataset.viewPanel!==view; });
        });
      });
      chips.forEach(function(c){
        c.addEventListener('click',function(){
          chips.forEach(function(x){x.classList.remove('active');});
          c.classList.add('active');
          company=c.dataset.company;
          applyFilter();
        });
      });
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',run); else run();
})();
</script>
"""


def inject_patents_ui_js(html):
    if "/*patents-ui*/" in html:
        return html, False
    idx = html.rfind("</body>")
    if idx == -1:
        return html, False
    return html[:idx] + PATENTS_UI_JS + html[idx:], True


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
    """Two independent triggers, added separately so both can coexist:
    (1) a chip inside the 'Start here' panel's own content (only visible while
        viewing that panel — folders 01/02's richer nav has this pattern), and
    (2) a plain link in the ALWAYS-VISIBLE <nav class="side"> sidebar (folders
        03/04's only mechanism, and — this matters — 01/02 need it too, since
        their sidebar's existing "Source PDFs"/"Data files" links are visible
        from every doc, not just from 'Start here', and Patents should be
        equally reachable, not one extra click behind a specific panel)."""
    changed = False
    if 'data-go="patents"' not in html:
        chip_sibling = find_sibling_chip(html, 'data-go="pdfs"') or find_sibling_chip(html, 'data-go="data"')
        if chip_sibling:
            chip = '<div class="st-chip" data-go="patents" role="button" tabindex="0">📜 Patents<span>Primary patents behind the devices in this folder</span></div>'
            insert_at = chip_sibling.end()
            html = html[:insert_at] + chip + html[insert_at:]
            changed = True
    if 'href="#patents"' not in html:
        nav_m = re.search(r'<nav class="side">.*?</nav>', html, re.S)
        if nav_m and ('href="#pdfs"' in nav_m.group(0) or 'href="#data"' in nav_m.group(0) or 'href="#gallery"' in nav_m.group(0) or 'href="#source-docs"' in nav_m.group(0)):
            idx = nav_m.end() - len("</nav>")
            link = f'<a class="navbtn" href="#patents">📜 Patents ({count})</a>\n  '
            html = html[:idx] + link + html[idx:]
            changed = True
        elif html.rfind("</nav>") != -1:
            idx = html.rfind("</nav>")
            link = f'<a class="navbtn" href="#patents">📜 Patents ({count})</a>\n  '
            html = html[:idx] + link + html[idx:]
            changed = True
    return html, changed


def process_folder(folder):
    global pending
    patents = collect_folder_patents(folder)
    future_tech = collect_folder_future_tech(folder)
    if not patents and not future_tech:
        return
    index = folder / "index.html"
    if not index.exists():
        return
    html = index.read_text()
    section_html = render_section(patents, future_tech)
    html, css_changed = inject_css(html)
    html, js_changed = inject_future_md_renderer(html)
    html, js2_changed = inject_patents_ui_js(html)
    html, sec_action = inject_section(html, section_html)
    html, nav_changed = inject_nav_trigger(html, len(patents))
    changed = css_changed or js_changed or js2_changed or bool(sec_action) or nav_changed
    label = f"{len(patents)} patent(s)" + (f", {len(future_tech)} future-tech block(s)" if future_tech else "")
    if changed:
        pending += 1
        print(f"  {folder.name}: {label} — {sec_action or 'section unchanged'}"
              f"{', +css' if css_changed else ''}{', +js' if js_changed else ''}{', +nav' if nav_changed else ''}")
        if not CHECK:
            index.write_text(html)
    else:
        print(f"  {folder.name}: {label}, already up to date")


if __name__ == "__main__":
    print(("CHECK" if CHECK else "APPLY") + " patents section:")
    for folder in sorted(ROOT.glob("0*_*")):
        if folder.is_dir():
            process_folder(folder)
    if pending == 0:
        print("  up to date — nothing to do.")
    print(f"done ({pending} folder(s) {'pending' if CHECK else 'applied'}).")
    sys.exit(1 if (CHECK and pending) else 0)
