#!/usr/bin/env python3
"""Generate the October HubSpot web page and a portable IT handoff ZIP."""
from pathlib import Path
from urllib.parse import unquote
import re
import zipfile

root = Path(__file__).resolve().parent.parent
source = root / 'advisor_edge_october_2026.html'
hosted_base = 'https://theshawncraig-a11y.github.io/Advisor-Edge-September-2026/'
html = source.read_text()
refs = sorted(set(re.findall(r'assets/[^\"\')\s]+', html)))
for ref in refs:
    assert (root / unquote(ref)).is_file(), f'Missing asset: {ref}'
hubspot = root / 'advisor-edge-october-hubspot.html'
hubspot.write_text(html.replace('assets/', hosted_base + 'assets/'))
archive = root / 'handoff/Advisor-Edge-October-2026-IT-Handoff.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
    for path in [source, hubspot, root / 'handoff/IT-README.md']:
        bundle.write(path, path.name)
    for ref in refs:
        path = root / unquote(ref)
        bundle.write(path, unquote(ref))
print(f'Generated {hubspot.name} and {archive.name} with {len(refs)} assets.')
