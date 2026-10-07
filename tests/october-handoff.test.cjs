const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'advisor_edge_october_2026.html'), 'utf8');
const hubspot = fs.readFileSync(path.join(root, 'advisor-edge-october-hubspot.html'), 'utf8');
const base = 'https://theshawncraig-a11y.github.io/Advisor-Edge-September-2026/';
assert.equal(hubspot.split(base).join(''), source, 'HubSpot must match the standalone page');
assert.doesNotMatch(hubspot, /(?:src|href)=["']assets\//);
assert.doesNotMatch(hubspot, /url\(\s*["']?assets\//);
const refs = [...new Set([...source.matchAll(/assets\/[^"')\s]+/g)].map(m => m[0]))];
for (const ref of refs) assert.ok(fs.existsSync(path.join(root, decodeURIComponent(ref))), ref);
const ids = [...source.matchAll(/\bid=["']([^"']+)["']/g)].map(m => m[1]);
assert.equal(new Set(ids).size, ids.length, 'IDs must be unique');
for (const ref of source.matchAll(/(?:href|aria-controls)=["']#?([^"']+)["']/g)) {
  if (ref[0].startsWith('href="#')) assert.ok(ids.includes(ref[1]), `Missing anchor: ${ref[1]}`);
}
for (const tag of ['div', 'section', 'article', 'style', 'script', 'button', 'details']) {
  assert.equal((source.match(new RegExp(`<${tag}\\b`, 'gi')) || []).length,
    (source.match(new RegExp(`</${tag}>`, 'gi')) || []).length, `${tag} tags must balance`);
}
assert.equal((source.match(/class="mt-pc-cta" data-modal-target=/g) || []).length, 3);
console.log(`October handoff verified: matching exports, ${refs.length} assets, unique IDs, valid anchors, balanced markup.`);
