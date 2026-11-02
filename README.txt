MECH ARENA SMART OPTIMIZER V4 — NOV 2026

Upload these files to the SAME GitHub repository folder as index.html:
- hangar-showdown.html (replaces previous version)
- hangar-optimizer.js (NEW, REQUIRED)
- mechs.json (existing 48-mech catalog)
- weapons.json (existing 58 weapon-family catalog)
- equipment-database.html, app.js, style.css (included for convenience; unchanged)

This upgrade includes:
1. Energy-capacity calculator for two weapons per mech, five slots.
2. Named weapon variants and auto-fill ONLY when the JSON contains verifiedEnergy: true and a numeric energy value.
3. Tactical weapon-family recommendations by role and playstyle.
4. Five-mech hangar coverage report, duplicate checks, role/range diversity, and transparent heuristic planning score.
5. Browser-local save and migration from previous planner state.

IMPORTANT DATA LIMITATIONS:
The inherited database has no VERIFIED mech energy capacities and no VERIFIED weapon energy variants.
Therefore the calculator is operational but requires the player to input exact in-game energy figures.
No official live-game stats or complete individual weapon variant roster are claimed. The 48 mechs and 58 families are an unverified partial catalog. Recommendation scores are heuristics, not measured performance.

Test: open /hangar-showdown.html, choose Voidghost, enter in-game capacity, select two weapon families, enter their variant names and energy, and verify over-capacity warnings. Use Recommend weapon families to see tactical suggestions.
