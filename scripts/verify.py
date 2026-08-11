#!/usr/bin/env python3
"""Verification pass for democraticsocialism101.com.

Run from the repository root:

    python3 scripts/verify.py              # structure, links, freshness report
    python3 scripts/verify.py --max-age 90 # tighter freshness threshold
    python3 scripts/verify.py --strict     # stale dates fail too, for CI

Three checks, in the order they matter.

1. Structure. Every HTML file parses with balanced tags. Catches the
   broken-markup class of error before it reaches a reader.

2. Internal links. Every href to a local path resolves to a file that
   exists, and every "#fragment" resolves to an id that exists on the
   target page. Catches the dangling cross-reference class, which this
   site is unusually exposed to because pages deliberately link to each
   other instead of redefining terms.

3. Freshness. This one exists because of a specific failure. An audit on
   2026-08-11 found seven factual errors on figures.html, and five of
   them were not mistakes of research but of time: a head of state listed
   as sitting who had left office five months earlier, officials listed
   as serving who had lost their seats years before. Every one sat behind
   a "verified" date that had been refreshed without the claim behind it
   being re-checked. A date that is not enforced is a decoration, so this
   check reads every dated claim on the site and reports its age.

Structural and link failures exit nonzero. Stale dates are reported but
do not fail unless --strict is passed, because staleness is a prompt to
go and look rather than proof that anything is wrong.

No third-party dependencies, by design: this repository has no build
step and should not acquire one for a checker.
"""

import argparse
import datetime as dt
import glob
import os
import re
import sys
from html.parser import HTMLParser

VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "source", "track", "wbr",
}

DATE_PATTERN = re.compile(
    r"(Last reviewed|Last verified|Status verified)\s*:?\s*</strong>\s*(\d{4}-\d{2}-\d{2})"
)


class Balance(HTMLParser):
    """Tag-balance checker. Reports the first unbalanced close it sees."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"stray </{tag}> at line {self.getpos()[0]}")
            return
        top, pos = self.stack[-1]
        if top != tag:
            self.errors.append(
                f"expected </{top}> (opened line {pos[0]}) but found </{tag}> at line {self.getpos()[0]}"
            )
        else:
            self.stack.pop()


def html_files():
    return sorted(glob.glob("*.html") + glob.glob("*/*.html"))


def check_structure(files):
    problems = []
    for path in files:
        parser = Balance()
        parser.feed(open(path, encoding="utf-8").read())
        for err in parser.errors:
            problems.append(f"{path}: {err}")
        for tag, pos in parser.stack:
            problems.append(f"{path}: <{tag}> opened at line {pos[0]} is never closed")
    return problems


def check_links(files):
    ids = {}
    for path in files:
        ids[path] = set(re.findall(r'id="([^"]+)"', open(path, encoding="utf-8").read()))

    problems = []
    for path in files:
        text = open(path, encoding="utf-8").read()

        for href in re.findall(r'href="(/[^"]*)"', text):
            target, _, fragment = href.partition("#")
            resolved = target.lstrip("/") or "index.html"
            if resolved.endswith("/"):
                resolved += "index.html"
            if not os.path.exists(resolved):
                problems.append(f"{path}: link to {href} but {resolved} does not exist")
            elif fragment and fragment not in ids.get(resolved, set()):
                problems.append(f"{path}: link to {href} but #{fragment} is not an id on {resolved}")

        for fragment in re.findall(r'href="#([^"]+)"', text):
            if fragment not in ids[path]:
                problems.append(f"{path}: local link to #{fragment} but no such id on this page")

    return problems


def check_freshness(files, max_age_days, today):
    entries = []
    for path in files:
        for label, stamp in DATE_PATTERN.findall(open(path, encoding="utf-8").read()):
            try:
                when = dt.date.fromisoformat(stamp)
            except ValueError:
                entries.append((path, label, stamp, None))
                continue
            entries.append((path, label, stamp, (today - when).days))
    stale = [e for e in entries if e[3] is not None and e[3] > max_age_days]
    unparseable = [e for e in entries if e[3] is None]
    return entries, stale, unparseable


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-age", type=int, default=180,
                    help="days after which a dated claim is reported stale (default 180)")
    ap.add_argument("--strict", action="store_true",
                    help="treat stale dates as failures, not warnings")
    args = ap.parse_args()

    if not os.path.exists("index.html"):
        print("Run this from the repository root (no index.html here).", file=sys.stderr)
        return 2

    files = html_files()
    today = dt.date.today()
    failures = []

    structure = check_structure(files)
    links = check_links(files)
    entries, stale, unparseable = check_freshness(files, args.max_age, today)

    print(f"Checked {len(files)} HTML file(s) and {len(entries)} dated claim(s).\n")

    print(f"Structure:      {'ok' if not structure else str(len(structure)) + ' problem(s)'}")
    for problem in structure:
        print(f"  - {problem}")

    print(f"Internal links: {'ok' if not links else str(len(links)) + ' problem(s)'}")
    for problem in links:
        print(f"  - {problem}")

    if entries:
        oldest = max(e[3] for e in entries if e[3] is not None)
        print(f"Freshness:      oldest dated claim is {oldest} day(s) old (threshold {args.max_age})")
    else:
        print("Freshness:      no dated claims found")

    for path, label, stamp, age in sorted(stale, key=lambda e: -e[3]):
        print(f"  - {path}: \"{label}\" is {age} day(s) old ({stamp})")
    for path, label, stamp, _ in unparseable:
        print(f"  - {path}: \"{label}\" has an unparseable date ({stamp})")

    failures += structure + links
    failures += [f"{p}: unparseable date {s}" for p, _, s, _ in unparseable]
    if args.strict:
        failures += [f"{p}: stale {label} ({s})" for p, label, s, _ in stale]

    if failures:
        print(f"\nFAIL: {len(failures)} problem(s) must be fixed.")
        return 1

    if stale:
        print(f"\nPASS, with {len(stale)} dated claim(s) worth re-checking. "
              "Re-verify the claim itself before touching the date.")
    else:
        print("\nPASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
