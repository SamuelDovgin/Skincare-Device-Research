#!/usr/bin/env python3
"""Apply the two citation features to this research archive. Idempotent — safe to
re-run after the viewer HTML is regenerated externally (which wipes the popover).

  1. linkify_md   : turn numbered inline markers [n] into [[n]](source-url) in every
                    .md file that has a "Sources/References" list with URLs.
  2. inject_pop   : add the hover (desktop) / tap-sheet (mobile) evidence popover to
                    every folder index.html. On hover/tap of [n] it shows the source
                    name + the supporting quote pulled from that doc's Sources list,
                    with an "Open full source" link.
  3. sync_embeds  : re-sync each index.html's embedded DOCS[].md from disk so the
                    rendered viewer reflects the linkified markdown.

Usage:  python3 tools/apply_citation_features.py            (apply, in-place)
        python3 tools/apply_citation_features.py --check     (report only, exit 1 if work pending)
"""
import re, sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECK = "--check" in sys.argv

HEAD_RE  = re.compile(r'^#{1,6}\s+.*\b(sources|references|bibliography)\b', re.I | re.M)
ENTRY_RE = re.compile(r'^\s*(\d+)\.\s+(.*)$')
URL_RE   = re.compile(r'https?://[^\s)>\]]+')
# a bare [n] marker: not already inside [[n]](..) (lookbehind) and not a link [n](..) (lookahead)
CITE_RE  = re.compile(r'(?<!\[)\[(\d+)\](?!\()(?!\])')

pending = 0

def linkify_md():
    global pending
    for f in sorted(ROOT.glob("**/*.md")):
        if "/.git/" in str(f):
            continue
        text = f.read_text()
        heads = list(HEAD_RE.finditer(text))
        if not heads:
            continue
        sec = heads[-1].start()
        body, refs = text[:sec], text[sec:]
        urlmap = {}
        for line in refs.splitlines():
            m = ENTRY_RE.match(line)
            if not m:
                continue
            um = URL_RE.search(m.group(2))
            if um:
                urlmap[m.group(1)] = um.group(0).rstrip('.,;:')
        if not CITE_RE.search(body):
            continue
        new_body = CITE_RE.sub(lambda m: f'[[{m.group(1)}]]({urlmap[m.group(1)]})'
                               if m.group(1) in urlmap else m.group(0), body)
        if new_body != body:
            pending += 1
            print(f"  linkify: {f.relative_to(ROOT)}")
            if not CHECK:
                f.write_text(new_body + refs)


CSS = r"""
/* cite-enhance */
.cite{display:inline-block;font:inherit;border:0;background:transparent;padding:0;margin:0 .5px;cursor:pointer;color:var(--accent);font-weight:600;border-bottom:1px dotted currentColor;line-height:inherit}
.cite::before{content:"["}.cite::after{content:"]"}
.cite:hover,.cite:focus,.cite.on{color:var(--accent2);outline:none;background:rgba(0,0,0,.04);border-radius:3px}
#citebackdrop{position:fixed;inset:0;background:rgba(15,18,24,.45);z-index:9998;opacity:0;transition:opacity .15s}
#citebackdrop[hidden]{display:none}#citebackdrop.show{opacity:1}
#citepop{position:fixed;z-index:9999;max-width:390px;width:max-content}
#citepop[hidden]{display:none}
#citepop .cp-card{position:relative;background:var(--card,#fff);color:var(--ink,#1f2430);border:1px solid var(--line,#e5e7eb);border-radius:12px;box-shadow:0 12px 38px rgba(0,0,0,.20);padding:13px 15px;font-size:13px;line-height:1.5;max-height:60vh;overflow:auto}
#citepop .cp-src{font-weight:700;font-size:11.5px;letter-spacing:.02em;color:var(--accent);margin:0 28px 6px 0;text-transform:uppercase}
#citepop .cp-quote{color:var(--ink,#1f2430)}
#citepop .cp-quote.cp-empty{color:var(--muted,#6b7280);font-style:italic}
#citepop .cp-link{display:inline-block;margin-top:11px;font-size:12px;font-weight:600;color:var(--accent);text-decoration:none}
#citepop .cp-link:hover{text-decoration:underline}
#citepop .cp-close{position:absolute;top:6px;right:8px;border:0;background:transparent;color:var(--muted,#6b7280);font-size:20px;line-height:1;cursor:pointer;padding:2px 6px;display:none}
#citepop.sheet{left:0;right:0;bottom:0;top:auto!important;max-width:none;width:auto}
#citepop.sheet .cp-card{border-radius:16px 16px 0 0;border-left:0;border-right:0;border-bottom:0;padding:18px 20px calc(26px + env(safe-area-inset-bottom));font-size:15px;max-height:72vh}
#citepop.sheet .cp-src{font-size:12px}
#citepop.sheet .cp-close{display:block;font-size:26px;top:10px;right:12px}
#citepop.sheet .cp-link{font-size:14px}
"""

JS = r"""<script>/*cite-enhance*/
(function(){
  if(window.__citeEnhanced) return; window.__citeEnhanced=true;
  var back=document.createElement('div'); back.id='citebackdrop'; back.hidden=true;
  var pop=document.createElement('div'); pop.id='citepop'; pop.hidden=true;
  pop.setAttribute('role','dialog'); pop.setAttribute('aria-modal','false'); pop.setAttribute('aria-live','polite');
  pop.innerHTML='<div class="cp-card"><button type="button" class="cp-close" aria-label="Close">×</button><div class="cp-src"></div><div class="cp-quote"></div><a class="cp-link" target="_blank" rel="noopener">Open full source ↗</a></div>';
  document.body.appendChild(back); document.body.appendChild(pop);
  var srcEl=pop.querySelector('.cp-src'), qEl=pop.querySelector('.cp-quote'),
      linkEl=pop.querySelector('.cp-link'), closeEl=pop.querySelector('.cp-close');
  var canHover=window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  var hideT=null, current=null;
  function fill(el){
    srcEl.textContent=el.dataset.title||('Source '+el.dataset.n);
    var ev=el.dataset.evidence||'';
    if(ev){qEl.textContent=ev; qEl.classList.remove('cp-empty');}
    else{qEl.textContent='No quote was extracted for this source — open it to read the original.'; qEl.classList.add('cp-empty');}
    if(el.dataset.url){linkEl.href=el.dataset.url; linkEl.style.display='';} else linkEl.style.display='none';
  }
  function setCur(el){ if(current)current.classList.remove('on'); current=el; if(el)el.classList.add('on'); }
  function positionFloat(el){
    var r=el.getBoundingClientRect(), pr=pop.getBoundingClientRect();
    var top=r.top-pr.height-8; if(top<8) top=r.bottom+8;
    top=Math.max(8,Math.min(top,window.innerHeight-pr.height-8));
    var left=r.left+r.width/2-pr.width/2;
    left=Math.max(8,Math.min(left,window.innerWidth-pr.width-8));
    pop.style.top=top+'px'; pop.style.left=left+'px';
  }
  function openFloat(el){
    clearTimeout(hideT); setCur(el); fill(el);
    pop.classList.remove('sheet'); back.hidden=true;
    pop.style.visibility='hidden'; pop.hidden=false;
    requestAnimationFrame(function(){ positionFloat(el); pop.style.visibility=''; });
  }
  function openSheet(el){
    clearTimeout(hideT); setCur(el); fill(el);
    pop.classList.add('sheet'); pop.style.top=''; pop.style.left='';
    back.hidden=false; pop.hidden=false;
    requestAnimationFrame(function(){ back.classList.add('show'); });
  }
  function close(){ pop.hidden=true; back.hidden=true; back.classList.remove('show'); pop.classList.remove('sheet'); setCur(null); }
  function scheduleHide(){ hideT=setTimeout(close,160); }
  pop.addEventListener('mouseenter',function(){ if(canHover) clearTimeout(hideT); });
  pop.addEventListener('mouseleave',function(){ if(canHover) scheduleHide(); });
  closeEl.addEventListener('click',close);
  back.addEventListener('click',close);
  document.addEventListener('keydown',function(e){ if(e.key==='Escape') close(); });
  window.addEventListener('scroll',function(){ if(current && !pop.classList.contains('sheet')) close(); },true);
  window.addEventListener('resize',close);
  function bind(el){
    if(canHover){
      el.addEventListener('mouseenter',function(){ clearTimeout(hideT); openFloat(el); });
      el.addEventListener('mouseleave',scheduleHide);
      el.addEventListener('focus',function(){ openFloat(el); });
      el.addEventListener('blur',scheduleHide);
      el.addEventListener('click',function(e){ e.preventDefault(); openFloat(el); });
    }else{
      el.addEventListener('click',function(e){ e.preventDefault(); (pop.hidden||current!==el)?openSheet(el):close(); });
    }
  }
  function citeData(md){
    var map={}, lines=md.split('\n');
    var headRe=/^#{1,6}\s+.*\b(sources|references|bibliography)\b/i;
    var last=-1; for(var i=0;i<lines.length;i++) if(headRe.test(lines[i])) last=i;
    if(last<0) return map;
    var entryRe=/^\s*(\d+)\.\s+(.*)$/, urlRe=/https?:\/\/[^\s)>\]]+/;
    for(var j=last+1;j<lines.length;j++){
      var ln=lines[j]; if(/^#{1,6}\s/.test(ln)) break;
      var m=entryRe.exec(ln); if(!m) continue;
      var n=m[1], rest=m[2], um=rest.match(urlRe), url='', title=rest, ev='';
      if(um){ url=um[0].replace(/[.,;]+$/,''); title=rest.slice(0,um.index); ev=rest.slice(um.index+um[0].length); }
      title=title.replace(/[*_`]/g,'').replace(/\s*[—–-]\s*$/,'').trim();
      ev=ev.replace(/^\s*[—–-]\s*/,'').replace(/[*_`]/g,'').trim();
      map[n]={title:title,url:url,evidence:ev};
    }
    return map;
  }
  function enhance(container,map){
    if(!container||!Object.keys(map).length) return;
    container.querySelectorAll('a').forEach(function(a){
      var t=(a.textContent||'').trim(); var m=/^\[(\d+)\]$/.exec(t); if(!m) return;
      var num=m[1], d=map[num]; if(!d) return;
      var b=document.createElement('button');
      b.className='cite'; b.type='button'; b.textContent=num;
      b.dataset.n=num; b.dataset.title=d.title; b.dataset.evidence=d.evidence;
      b.dataset.url=d.url||a.getAttribute('href')||'';
      b.setAttribute('aria-label','Citation '+num+'. '+(d.title||'')+'. '+(d.evidence||''));
      a.replaceWith(b); bind(b);
    });
  }
  function run(){ try{ if(typeof DOCS==='undefined') return;
    DOCS.forEach(function(d){ enhance(document.getElementById(d.id+'_r'), citeData(d.md)); }); }catch(e){} }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',run); else run();
})();
</script>
"""

def folder_index_htmls():
    out = []
    for p in sorted(ROOT.glob("*/index.html")):
        if "const DOCS=" in p.read_text():
            out.append(p)
    return out

def inject_pop():
    global pending
    for p in folder_index_htmls():
        t = p.read_text()
        if "/*cite-enhance*/" in t:
            continue
        pending += 1
        print(f"  inject popover: {p.relative_to(ROOT)}")
        if CHECK:
            continue
        t = t.replace("</style>", CSS + "</style>", 1)
        i = t.rfind("</body>")
        p.write_text(t[:i] + JS + "\n" + t[i:])

def sync_embeds():
    global pending
    for p in folder_index_htmls():
        t = p.read_text()
        i = t.find("const DOCS="); j = t.find("\n", i)
        arr = json.loads(t[i+len("const DOCS="):j].rstrip(";"))
        changed = False
        for e in arr:
            disk = (p.parent / e["file"]).read_text()
            if disk != e["md"]:
                e["md"] = disk; changed = True
        if changed:
            pending += 1
            print(f"  sync embeds: {p.relative_to(ROOT)}")
            if not CHECK:
                p.write_text(t[:i] + "const DOCS=" + json.dumps(arr, ensure_ascii=False) + ";" + t[j:])

if __name__ == "__main__":
    print(("CHECK" if CHECK else "APPLY") + " citation features:")
    linkify_md()
    sync_embeds()      # md links -> embedded copies
    inject_pop()
    if pending == 0:
        print("  up to date — nothing to do.")
    print(f"done ({pending} item(s) {'pending' if CHECK else 'applied'}).")
    sys.exit(1 if (CHECK and pending) else 0)
