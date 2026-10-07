#!/usr/bin/env python3
"""Generate the October HubSpot HTML using GitHub-hosted assets."""
from pathlib import Path
from urllib.parse import unquote
import re

root = Path(__file__).resolve().parent.parent
source = root / 'advisor_edge_october_2026.html'
hosted_base = 'https://theshawncraig-a11y.github.io/Advisor-Edge-September-2026/'
html = source.read_text()
refs = sorted(set(re.findall(r'assets/[^\"\')\s]+', html)))
for ref in refs:
    assert (root / unquote(ref)).is_file(), f'Missing asset: {ref}'
hubspot = root / 'advisor-edge-october-hubspot.html'
hubspot.write_text(html.replace('assets/', hosted_base + 'assets/'))
print(f'Generated {hubspot.name} with {len(refs)} GitHub-hosted asset references.')
