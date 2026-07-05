#!/usr/bin/env python3
"""Render the project review markdown to a well-formatted PDF.
markdown -> HTML (tables, footnotes, fenced code) -> PDF (xhtml2pdf/reportlab).
Images referenced relatively are resolved from the markdown's own directory."""
import os, re, sys
import markdown
from xhtml2pdf import pisa

SRC = sys.argv[1]
OUT = sys.argv[2]
BASE = os.path.dirname(os.path.abspath(SRC))

md = open(SRC).read()

# xhtml2pdf has no GitHub-style emoji; keep the one ⚠ etc. out of the way is unnecessary here.
html_body = markdown.markdown(
    md,
    extensions=["tables", "footnotes", "fenced_code", "sane_lists", "attr_list"],
    extension_configs={"footnotes": {"BACKLINK_TEXT": "&#8617;"}},
)

CSS = """
@page { size: A4; margin: 1.8cm 1.9cm 2.0cm 1.9cm;
        @frame footer { -pdf-frame-content: footerContent; bottom: 1cm; height: 1cm; }}
body { font-family: Helvetica; font-size: 9.4pt; line-height: 1.42; color: #1a1a1a; }
h1 { font-size: 19pt; color: #3a5a40; border-bottom: 2px solid #3a5a40;
     padding-bottom: 4px; margin: 0 0 6px 0; }
h2 { font-size: 13pt; color: #344e41; margin: 15px 0 5px 0;
     border-bottom: 1px solid #ccc; padding-bottom: 2px; }
h3 { font-size: 10.5pt; color: #3a5a40; margin: 11px 0 3px 0; }
p { margin: 0 0 6px 0; text-align: justify; }
em { color: #333; }
strong { color: #111; }
a { color: #2a6f4a; text-decoration: none; }
code { font-family: Courier; font-size: 8.4pt; background: #f2f2f0; }
table { -pdf-keep-in-frame-mode: shrink; margin: 6px 0 10px 0; width: 100%; }
th { background: #3a5a40; color: #fff; font-size: 8.2pt; padding: 4px 5px; text-align: left; }
td { font-size: 8.2pt; padding: 3px 5px; border-bottom: 0.5px solid #ddd; }
hr { border: none; border-top: 0.5px solid #bbb; margin: 10px 0; }
blockquote { color: #444; border-left: 2px solid #3a5a40; margin: 6px 0; padding-left: 8px; }
img { -pdf-keep-in-frame-mode: shrink; }
.footnote { font-size: 7.8pt; color: #444; }
.footnote ol { padding-left: 14px; }
ul, ol { margin: 0 0 6px 0; }
li { margin-bottom: 2px; }
"""

# Nudge image widths so full-width charts fit the frame.
html_body = re.sub(r"<img ", '<img style="width:16cm;" ', html_body)

html = f"""<html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>
<div id="footerContent" style="font-size:7pt;color:#888;text-align:center;">
The Thales Project — Interim Review · paper trading only · <pdf:pagenumber> of <pdf:pagecount>
</div>
{html_body}
</body></html>"""

with open(OUT, "wb") as f:
    result = pisa.CreatePDF(html, dest=f, path=BASE + "/")
print("OK" if not result.err else f"ERRORS: {result.err}", "->", OUT)
