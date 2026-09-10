#!/usr/bin/env python3
"""Assembles the three self-contained pitch pages from parts/."""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
CSS  = (ROOT / "parts/_shared.css").read_text()

PAGES = [
    ("index.html",      "overview", "Ogier — website roadmap concepts | ClerksWell"),
    ("idea-one.html",   "one",      "Idea One: Routes into our expertise | Ogier roadmap concepts"),
    ("idea-two.html",   "two",      "Idea Two: A digital concierge | Ogier roadmap concepts"),
    ("idea-three.html", "three",    "Idea Three: News and insights | Ogier roadmap concepts"),
    ("idea-four.html",  "four",     "Idea Four: Enquiry routing | Ogier roadmap concepts"),
]
NAV = [("index.html","Overview","","overview"),
       ("idea-one.html","One"," · Routes in","one"),
       ("idea-two.html","Two"," · Concierge","two"),
       ("idea-three.html","Three"," · Insights","three"),
       ("idea-four.html","Four"," · Enquiries","four")]

SHELL = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Concept designs for the Ogier website roadmap, prepared by ClerksWell.">
<style>
{css}
</style>
{headextra}</head>
<body class="present">
<header class="deckbar">
  <div class="deckbar__in">
    <a class="deckbar__brand" href="index.html">Ogier <span>Roadmap concepts</span></a>
    <nav class="deckbar__nav">
{nav}      <button class="annotoggle" id="annotoggle" data-on="false" type="button">Show notes</button>
    </nav>
  </div>
</header>
{body}
<footer class="wrap" style="padding-top:52px;padding-bottom:64px;border-top:1px solid var(--line);margin-top:40px">
  <p class="small muted" style="margin:0;max-width:74ch">
    Concept designs prepared by <strong style="color:var(--ink)">ClerksWell</strong> for discussion with Ogier.
    Interface copy, service names, jurisdictions and article titles are taken from ogier.com and used
    illustratively; individual names and job titles shown in the demos are placeholders. These are
    interactive concepts, not production code, and nothing here constitutes legal advice.
  </p>
</footer>
<script>
(function(){{
  var t=document.getElementById('annotoggle');
  t.addEventListener('click',function(){{
    var on=t.dataset.on==='true';
    document.body.classList.toggle('present',on);
    t.dataset.on=on?'false':'true';
    t.textContent=on?'Show notes':'Hide notes';
  }});
}})();
</script>
{jsextra}</body>
</html>
"""

for filename, key, title in PAGES:
    src = (ROOT / f"parts/{key}.html").read_text()
    for inc in re.findall(r"<!--INCLUDE-CSS:\s*([\w.\-]+)\s*-->", src):
        src = src.replace(f"<!--INCLUDE-CSS: {inc}-->",
                          (ROOT / f"parts/css/{inc}").read_text().rstrip())
    headextra, jsextra = "", ""
    m = re.search(r"<!--HEAD-->(.*?)<!--/HEAD-->", src, re.S)
    if m:
        headextra = m.group(1).strip() + "\n"
        src = src.replace(m.group(0), "")
    m = re.search(r"<!--JS-->(.*?)<!--/JS-->", src, re.S)
    if m:
        jsextra = m.group(1).strip() + "\n"
        src = src.replace(m.group(0), "")
    nav = ""
    for href, label, tail, k in NAV:
        cur = ' aria-current="page"' if k == key else ""
        tailhtml = f'<span class="navtail">{tail}</span>' if tail else ""
        nav += f'      <a href="{href}"{cur}>{label}{tailhtml}</a>\n'
    (ROOT / filename).write_text(
        SHELL.format(title=title, css=CSS, nav=nav, body=src.strip(),
                     headextra=headextra, jsextra=jsextra)
    )
    print(f"built {filename}  ({len((ROOT/filename).read_text()):,} bytes)")
