SINGLE MECH SHOWDOWN OPTIMIZER

Upload BOTH files to your GitHub repository root, replacing existing files:
  hangar-showdown.html
  hangar-optimizer.js

Keep your existing mechs.json and weapons.json unchanged.

Commit to main and wait for Cloudflare Pages deployment.
Open https://mech-arena-tactical-hub.pages.dev/hangar-showdown.html
Refresh with Ctrl+Shift+R.

Features: one mech selection, playstyle, mech capacity, combined total weapon energy, capacity check, top five heuristic weapon-family recommendations.

The old five-slot localStorage state is not deleted; the new optimizer uses its own key.
