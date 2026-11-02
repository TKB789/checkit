"""Add a module's content to index.html and slides.html.

Usage (from the repo root):
  python3 tools/add_module.py tools/m15/manifest.json

The manifest (JSON) lists what to add; every key is optional:
{
  "n": 15, "name": "Optimization", "short": "M15 Optimization",
  "slides": "m15_slides.json",          # one module object for slides.html
  "exam": {"id": "mid2", "file": "m15_exam.json", "sub": "Modules 11–15 so far"},
  "slidetest": "m15_slidetest.js",       # S(...) calls
  "explain": "m15_explain.js",           # R(...) calls
  "guide": "m15_guide.json",             # {id,title,desc,html,toc}; inserted after the previous module's guide
  "inserts": [ {"guide": "models", "anchor": "...exact text...", "where": "before|after", "html": "..."},
               {"guide": "models", "toc": {"id": "...", "title": "...", "kicker": "MODEL"}},
               {"guide": "rscript", "pre_append": "plain R code (will be escaped)"} ],
  "replace": [ {"guide": "sheet2", "old": "...", "new": "..."} ]
}
Re-running is safe: existing items for the module are replaced, never duplicated, and nothing
already published is reordered (progress is keyed by question ID).
"""
import json, re, sys, os, html

def load(p, base): return json.load(open(os.path.join(base, p)))

def block(s, sid):
    m = re.search(r'(<script type="application/json" id="%s">)(.*?)(</script>)' % sid, s, re.S)
    return m, json.loads(m.group(2))

def put(s, m, obj, ascii=True):
    js = json.dumps(obj, ensure_ascii=ascii).replace('</', '<\\/')
    return s[:m.start(2)] + js + s[m.end(2):]

def once(h, a):
    n = h.count(a)
    if n != 1: sys.exit(f'anchor found {n} times (need exactly 1): {a[:80]!r}')

def main(manifest, index='index.html', slides='slides.html'):
    base = os.path.dirname(os.path.abspath(manifest)); M = json.load(open(manifest))
    n = M['n']; m, Mx = f'm{n}', f'M{n}'
    # ---- slides.html
    if 'slides' in M:
        s = open(slides).read()
        mm = re.search(r'(<script id="data"[^>]*>)(.*?)(</script>)', s, re.S); D = json.loads(mm.group(2))
        D['modules'] = [x for x in D['modules'] if x['module'] != m] + [load(M['slides'], base)]
        open(slides, 'w').write(s[:mm.start(2)] + json.dumps(D).replace('</', '<\\/') + s[mm.end(2):])
    s = open(index).read()
    # ---- register the module (idempotent)
    prev = f"'m{n-1}'"
    name = M.get('name', ''); short = M.get('short', f'{Mx} {name}')
    if f"MODS.{m}=" not in s:
        a = re.search(r"MODS\.m%d='[^']*'; SHORT\.m%d='[^']*';\n" % (n-1, n-1), s).group(0)
        s = s.replace(a, a + f"MODS.{m}='Module {n} · {name}'; SHORT.{m}='{short}';\n", 1)
    s = s.replace(f"{prev}]", f"{prev},'{m}']") if f"'{m}']" not in s else s
    s = re.sub(r"(m%d:'m%d')\};" % (n-1, n-1), r"\1,%s:'%s'};" % (m, m), s) if f"{m}:'{m}'" not in s else s
    s = re.sub(r"('M%d','MIX'\])" % (n-1), f"'M{n-1}','{Mx}','MIX']", s) if f"'{Mx}','MIX'" not in s else s
    if f"{Mx}:'Module {n}" not in s:
        s = re.sub(r"(M%d:'[^']*',)(MIX:)" % (n-1), r"\1%s:'Module %d · %s',\2" % (Mx, n, name), s, count=1)
    # ---- midterm scenarios
    if 'exam' in M:
        mm, d = block(s, 'px-data'); e = [x for x in d['exams'] if x['id'] == M['exam']['id']][0]
        new = load(M['exam']['file'], base); ids = {x['id'] for x in new}
        e['exam'] = [x for x in e['exam'] if x['id'] not in ids] + new
        for x in new:
            for p in x['parts']:
                assert p['type'] in ('multi', 'single', 'match'), p['q']
                if p['type'] == 'match': assert len(p['answer']) == len(p['items']) == len(p['why'])
                else: assert all(0 <= a < len(p['options']) for a in p['answer']) and p['answer']
        if 'sub' in M['exam']:
            e['sub'] = f"{M['exam']['sub']} · {sum(len(x['parts']) for x in e['exam'])} questions"
        s = put(s, mm, d)
    # ---- slide test + explain-it prompts
    if 'slidetest' in M:
        s = re.sub(r"^S\('%s',.*?\n\]\);\n" % m, '', s, flags=re.S | re.M)
        a = "// ---- explain-it prompts\n"; once(s, a)
        s = s.replace(a, open(os.path.join(base, M['slidetest'])).read() + a)
    if 'explain' in M:
        s = re.sub(r"^ ?R\('%s',.*?\n\]\);\n" % m, '', s, flags=re.S | re.M)
        b = "/*M11_13:END*/"; once(s, b); i = s.index(b)
        s = s[:i] + open(os.path.join(base, M['explain'])).read() + " " + s[i:]
    # ---- guides
    mm, G = block(s, 'guides-data'); g = {x['id']: x for x in G}
    if 'guide' in M:
        new = load(M['guide'], base); G = [x for x in G if x['id'] != new['id']]
        k = [x['id'] for x in G].index(f'm{n-1}'); G.insert(k + 1, new); g = {x['id']: x for x in G}
    for ins in M.get('inserts', []):
        x = g[ins['guide']]
        if 'toc' in ins:
            if all(t['id'] != ins['toc']['id'] for t in x['toc']): x['toc'].append(ins['toc'])
        elif 'pre_append' in ins:
            if ins['pre_append'].strip().splitlines()[1] not in html.unescape(x['html']):
                k = x['html'].rindex('</pre>'); x['html'] = x['html'][:k] + html.escape(ins['pre_append']) + x['html'][k:]
        else:
            if ins['html'] in x['html']: continue
            once(x['html'], ins['anchor'])
            rep = ins['html'] + ins['anchor'] if ins.get('where', 'before') == 'before' else ins['anchor'] + ins['html']
            x['html'] = x['html'].replace(ins['anchor'], rep)
    for r in M.get('replace', []):
        x = g[r['guide']]; fld = r.get('field', 'html')
        if r['new'] in x[fld]: continue
        once(x[fld], r['old']); x[fld] = x[fld].replace(r['old'], r['new'])
    s = put(s, mm, G, ascii=False)
    open(index, 'w').write(s)
    print('done:', Mx)

if __name__ == '__main__':
    main(*sys.argv[1:])
