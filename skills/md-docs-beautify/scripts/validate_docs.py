#!/usr/bin/env python3
"""validate_docs.py — sanity-check a docs visual upgrade.

Usage:  python3 validate_docs.py <doc1.md> [doc2.md ...] --assets <assets_dir>

Checks:
  1. Every .svg in assets/ parses as well-formed XML.
  2. No svg contains script/handler elements or attributes (GitHub strips
     them anyway; their presence means the figure may render blank).
  3. Every asset is referenced by at least one doc (orphan = forgot to embed).
  4. Every doc image reference points at an existing file (typo catcher).
  5. Estimate hygiene: any chart file named *estimate* must contain the
     string 'estimate' at least twice (title/subtitle + per-bar label).
Exit code 0 iff all checks pass. Prints a per-file report.
"""
import argparse
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET

BANNED = re.compile(r"<script|onload=|onclick=|javascript:", re.I)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("docs", nargs="+")
    ap.add_argument("--assets", default="docs/assets")
    args = ap.parse_args()

    problems: list[str] = []
    svgs = sorted(glob.glob(os.path.join(args.assets, "*.svg")))
    if not svgs:
        print(f"no SVGs found in {args.assets}")
        return 1

    referenced: set[str] = set()
    for path in svgs:
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        try:
            ET.fromstring(text)
            print(f"  OK   xml   {name}")
        except ET.ParseError as e:
            problems.append(f"{name}: XML parse error: {e}")
            continue
        if BANNED.search(text):
            problems.append(f"{name}: contains script/handler markup")
        if "estimate" in name and len(re.findall(r"estimate", text, re.I)) < 2:
            problems.append(
                f"{name}: estimate chart must label estimates "
                "(subtitle + per-bar) — never pass projections as data"
            )

    for doc in args.docs:
        body = open(doc, encoding="utf-8").read()
        refs = re.findall(r'(?:\(([^)\s]+\.svg)\)|<img[^>]*src="([^"\s]+\.svg)")', body)
        refs = [a or b for a, b in refs]
        local = 0
        for ref in refs:
            if ref.startswith(("http://", "https://")):
                continue  # external badges are fine
            resolved = os.path.normpath(os.path.join(os.path.dirname(doc), ref))
            if not os.path.exists(resolved):
                problems.append(f"{doc}: broken reference {ref}")
            else:
                referenced.add(os.path.basename(resolved))
                local += 1
        print(f"  OK   embed {os.path.basename(doc)}: {len(refs)} svg refs ({local} local)")

    for path in svgs:
        name = os.path.basename(path)
        if name not in referenced:
            problems.append(f"{name}: orphaned asset — not embedded in any doc")

    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print(f"  ✗ {p}")
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
