MECH ARENA TACTICAL HUB — MAINTENANCE + PROMO CODE MONITOR

Upload the CONTENTS of this folder to the root of your GitHub repository, preserving .github/workflows/ and scripts/ directories. Do not upload this folder as a nested directory.

Existing pages included: hangar-showdown.html, equipment-database.html, best-mech-builds.html, weapon-guide.html, and their JS/CSS/JSON dependencies. If you have edited these live files since the previous packages, back them up and compare before overwriting. Do not replace newer JSON data with older copies.

New pages:
- /maintenance.html: local-only JSON editor for mechs.json, weapons.json, promo-codes.json. Validate and download; manually commit updates in GitHub. NOT password protected. Does not accept credentials.
- /promo-codes.html: public promo code listing sourced from promo-codes.json. All codes are labeled as reported/unverified, with account eligibility.

Automatic check:
- .github/workflows/promo-code-check.yml runs daily and can be run manually from GitHub Actions.
- scripts/check_promo_codes.py checks a public Plarium forum moderator thread for candidate codes.
- New candidate codes are put into promo-candidates.json via a pull request for human review. They are NOT automatically published as active because no reliable public redemption-validation API exists. This workflow cannot monitor in-game news, Discord, social networks or videos automatically.
- In GitHub Settings > Actions > General, set Workflow permissions to Read and write permissions and allow GitHub Actions to create and approve pull requests if your repo permits it. Some repositories disallow this; review GitHub Actions errors.
- Scheduled Actions can be delayed/disabled for inactivity. No guarantee of daily delivery.
- Review candidates in GitHub PR and add confirmed codes manually to promo-codes.json. Commit to main to publish.

Sources:
https://mecharena-support.plarium.com/hc/en-us/articles/15047121074460-How-to-get-a-Promo-Code
https://forum.plarium.com/mech-arena/702_game-discussion/1759149_active-promo-codes---10th-june--2026/
https://portal.plarium.com/en/redeem/mech-arena/

Do not advertise unverified codes as active or guaranteed. Avoid putting GitHub tokens, Plarium credentials, or private data in the public repository.
