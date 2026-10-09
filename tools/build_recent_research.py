#!/usr/bin/env python3
"""Generate the homepage's five latest article links from content changes.

Persist hashes/dates so checkout timestamps and later bundle regenerations do
not make unchanged articles look new. Only numbered topic articles qualify;
navigation, README files, datasets and source captures are not articles.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
from zoneinfo import ZoneInfo
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'recent-research.json'
START = '<!-- recent-research:start -->'
END = '<!-- recent-research:end -->'
ZONE = ZoneInfo('America/Chicago')


def git(*args: str) -> str:
    return subprocess.run(['git', *args], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


def history() -> dict[str, tuple[int, str]]:
    result = {}
    timestamp = 0
    # One history read for the whole archive. First occurrence is newest.
    for line in git('log', '--format=COMMIT:%ct', '--name-status',
                    '--diff-filter=AM', '--', '*.md').splitlines():
        if line.startswith('COMMIT:'):
            timestamp = int(line.partition(':')[2])
        elif '\t' in line:
            status, path = line.split('\t', 1)
            result.setdefault(path, (timestamp, status))
    return result


def routes() -> dict:
    text = (ROOT / 'site-router.js').read_text()
    match = re.search(r'\bconst ROUTES=(\{.*?\});', text, re.S)
    if not match:
        raise RuntimeError('Generate site-router.js before recent research.')
    return json.loads(match.group(1))


def plain_title(text: str, fallback: str) -> str:
    match = re.search(r'^#\s+(.+)$', text, re.M)
    title = match.group(1) if match else fallback
    title = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', title)
    return html.unescape(re.sub(r'[*`]', '', title)).strip()


def build() -> tuple[dict, str]:
    old = json.loads(MANIFEST.read_text())['articles'] if MANIFEST.exists() else {}
    past = history()
    changed = {p for p in git('diff', 'HEAD', '--name-only', '--', '*.md').splitlines()}
    untracked = set(git('ls-files', '--others', '--exclude-standard', '--', '*.md').splitlines())
    items = {}
    for path, route in routes().items():
        if not re.fullmatch(r'\d{2}_[^/]+/\d{2}_[^/]+\.md', path):
            continue
        source = ROOT / path
        text = source.read_text()
        digest = hashlib.sha256(text.encode()).hexdigest()
        previous = old.get(path)
        if previous and previous['sha256'] == digest:
            timestamp, status = previous['timestamp'], previous['status']
        elif path in changed or path in untracked:
            timestamp = int(source.stat().st_mtime)
            status = 'Added' if path in untracked else 'Updated'
        elif path in past:
            timestamp, change_type = past[path]
            status = 'Added' if change_type == 'A' else 'Updated'
        else:
            timestamp, status = int(source.stat().st_mtime), 'Added'
        topic = source.parent / 'README.md'
        topic_title = plain_title(topic.read_text(), source.parent.name) if topic.exists() else source.parent.name
        href = route['index'] + ('#' + route['id'] if route.get('id') else '')
        viewer_path = urlsplit(route['index']).path
        if viewer_path.endswith('.md') or not (ROOT / viewer_path).is_file():
            raise RuntimeError(f'Article has no rendered route: {path}')
        items[path] = dict(title=plain_title(text, source.stem), topic=topic_title,
                           href=href, timestamp=timestamp, status=status,
                           date=datetime.fromtimestamp(timestamp, ZONE).date().isoformat(), sha256=digest)
    latest = sorted(items, key=lambda p: (-items[p]['timestamp'], p))[:5]
    if len(latest) != 5:
        raise RuntimeError('Expected five research articles.')
    lines = [START, '<section class="recent-research" aria-labelledby="recent-research-title">',
             '<div class="recent-heading"><h2 id="recent-research-title">Recent research</h2><span>Latest 5 additions &amp; updates</span></div>',
             '<ol class="recent-list">']
    for path in latest:
        item = items[path]
        date = datetime.fromtimestamp(item['timestamp'], ZONE).strftime('%b %-d, %Y')
        lines.append(f'<li><div class="recent-meta"><time datetime="{item["date"]}">{date}</time>'
                     f'<span class="recent-status">{item["status"]}</span></div>'
                     f'<div class="recent-article"><a href="{html.escape(item["href"], quote=True)}">'
                     f'{html.escape(item["title"])}</a><span>{html.escape(item["topic"])}</span></div></li>')
    lines += ['</ol>', '</section>', END]
    return dict(timezone='America/Chicago', articles=items, latest=latest), '\n'.join(lines)


def main(check: bool = False) -> int:
    manifest, section = build()
    index = ROOT / 'index.html'
    text = index.read_text()
    if START in text:
        new = re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda _: section, text, flags=re.S)
    else:
        marker = '</header><section class="start-panel">'
        if marker not in text:
            raise RuntimeError('Homepage insertion marker missing.')
        new = text.replace(marker, '</header>\n' + section + '\n<section class="start-panel">', 1)
    payload = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
    if check:
        okay = text == new and MANIFEST.exists() and MANIFEST.read_text() == payload
        print('RECENT RESEARCH ' + ('OK' if okay else 'needs regeneration'))
        return 0 if okay else 1
    index.write_text(new)
    MANIFEST.write_text(payload)
    print('WROTE homepage recent research (5 rendered article links)')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    raise SystemExit(main(args.check))
