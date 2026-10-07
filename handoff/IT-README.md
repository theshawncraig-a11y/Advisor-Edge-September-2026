# Advisor Edge — October 2026 IT Handoff

## Files

- `advisor_edge_october_2026.html`: standalone web page; keep the included `assets/` directory next to it.
- `advisor-edge-october-hubspot.html`: the same complete web page with absolute image and PDF URLs on the existing GitHub Pages asset host.
- `assets/`: all 37 images, logos, and PDFs referenced by this edition.

This is a browser-based newsletter landing page, not an HTML email template. It contains JavaScript for product tabs, release detail dialogs, navigation, and the edition dropdown. An email editor will not preserve these interactions.

## HubSpot setup

1. Use `advisor-edge-october-hubspot.html` for the October web page, following the same hosting workflow as September. If using HubSpot Design Manager, add the standard HubSpot header/footer includes required by your template type and paste the page into a custom coded page template, not a rich-text or email module.
2. The prepared file uses this asset base:
   `https://theshawncraig-a11y.github.io/Advisor-Edge-September-2026/assets/`
   The repository name is the existing host name; the page and new asset names are for October.
3. If assets should be hosted in HubSpot Files instead, upload the included assets and replace each corresponding GitHub Pages URL with its HubSpot URL. Preserve the paths or use an explicit URL mapping; do not flatten files without updating references.
4. Preview before publishing. Check the hero, all nine section links, the Past Editions dropdown, both Product Update tabs, all three release dialogs, the social-media PDF, and the Agent Launchpad PDF. Check desktop and mobile layouts.
5. Publish the page at the intended October URL only after preview review. GitHub commit/push does not publish the HubSpot page.

## Past Editions

- August: https://www.cincpro.com/hubfs/Advisor%20and%20Agent%20Edge/advisor-edge-august-27.html
- September: https://www.cincpro.com/hubfs/Advisor%20and%20Agent%20Edge/advisor-edge-september-2026.html

## Maintenance

Edit the standalone October HTML, then run `python3 scripts/prepare-october-handoff.py` from the repository to regenerate the HubSpot file and ZIP. The ZIP is a generated delivery artifact; HTML, required assets, generator, and these instructions are kept in Git.

The separate `advisor_tips_social_preview.html` is a working preview and is not the deployment source.
