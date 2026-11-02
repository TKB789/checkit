"""Shared HTML helpers for study-guide builders (Maya stories, boxes, tables)."""
import html as H
P = lambda t: f'<p>{t}</p>'
def box(cls, label, body): return f'<div class="g-box {cls}"><p class="g-label"><b>{label}</b></p>{body}</div>'
plain = lambda t: box('g-plain', 'In plain English', P(t))
trap = lambda t: box('g-trap', 'Common trap', P(t))
ex = lambda t: box('g-ex', 'Worked example', t)
formula = lambda t: f'<div class="g-box g-formula"><div class="g-formula">{t}</div></div>'
def ul(items): return '<ul class="g-list">' + ''.join(f'<li><p>{i}</p></li>' for i in items) + '</ul>'
def tbl(head, rows, c='c3'):
    th = ''.join(f'<th><p>{h}</p></th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td><p>{x}</p></td>' for x in r) + '</tr>' for r in rows)
    return f'<div class="g-tbl"><table class="{c}"><tr>{th}</tr>{tr}</table></div>'
def who(calc, you, how):
    return ('<div class="g-box g-who"><div class="g-wrow"><p><b>Math or you? Who picks the numbers</b></p></div>'
            '<div class="g-wgrid"><div><p><b>Software / math calculates</b></p></div><div><p><b>You (the analyst) choose</b></p></div></div>'
            f'<div class="g-wgrid"><div><p>{calc}</p></div><div><p>{you}</p></div></div><div class="g-wrow"><p><b>How to choose:</b> {how}</p></div></div>')
def code(title, src, auto=None, decide=None):
    t = f'<div class="g-box g-code"><p class="g-label"><b>In R: {title}</b></p><pre class="g-pre">{H.escape(src)}</pre>'
    if auto: t += P(f'<b>R automates:</b> {auto}') + P(f'<b>Maya still decides:</b> {decide}')
    return t + '</div>'
def sec(kicker, sid, title, sub): return f'<p class="g-kicker">{kicker}</p><h2 class="g-h1" id="{sid}">{title}</h2><p class="g-sub">{sub}</p>'
def ch(n, title, intro): return f'<h3 class="g-h2">Chapter {n}. {title}</h3>' + P(intro)
nearly = lambda t: box('g-trap', 'Where she almost went wrong', P(t))
remembered = lambda t: box('g-ok', 'What she remembered', P(t))

