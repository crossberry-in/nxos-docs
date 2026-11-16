#!/usr/bin/env python3
"""Check relative markdown links in the docs tree point at real files
and anchors (nxos-docs QA)."""
import os
import re
import sys
from urllib.parse import unquote

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

def md_files():
    out = []
    for root, _dirs, names in os.walk(DOCS):
        for n in names:
            if n.endswith(".md"):
                out.append(os.path.join(root, n))
    return out

def anchor_exists(path, anchor):
    if not anchor:
        return True
    wanted = collapse(anchor.lower())
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^#{1,6}\s+(.*)$", line)
            if m:
                head = re.sub(r"`", "", m.group(1))
                t = collapse(re.sub(r"[^a-z0-9 \-]", "", head.lower()).strip())
                if t == wanted:
                    return True
    return False

def collapse(s):
    return re.sub(r"-+", "-", s.replace(" ", "-"))

problems = 0
for f in md_files():
    base = os.path.dirname(f)
    text = open(f, encoding="utf-8").read()
    for m in LINK_RE.finditer(text):
        target = m.group(1)
        if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        anchor = target.split("#")[1] if "#" in target else ""
        target = unquote(target.split("#")[0])
        if not target:
            continue  # pure-anchor link within the same page
        p = os.path.normpath(os.path.join(base, target))
        if os.path.isdir(p):
            continue
        if not os.path.exists(p):
            print(f"BROKEN  {os.path.relpath(f, DOCS)} -> {m.group(1)}")
            problems += 1
        elif p.endswith(".md") and not anchor_exists(p, anchor):
            print(f"ANCHOR  {os.path.relpath(f, DOCS)} -> {m.group(1)}")
            problems += 1

print("link problems:", problems)
