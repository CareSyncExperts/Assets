# Care Sync Hub design (screens, generators and super admin notes)

The written design lives in `docs/superpowers/specs/` (the spec, the client emails and the demo world). This folder holds the screens that go with it, so nothing depends on one session or one canvas.

These are clickable design mock-ups, not working software: no database, sign-in or live connections. They show exactly how each screen looks and behaves, for the build.

## What is here
- `boards/`: all 86 screens (`*.dc.html`), `canvas.json` (board numbers, titles and positions on the canvas), `registry.js` (the one settings registry every screen reads: weekly update day, reply promises, prices, timings), and `ds/` (the Care Sync design system tokens and components).
- `generators/`: the Python scripts that build most screens (for example `sahome.py` builds the super admin Home, Go-live and System health; `bizpages.py` builds the price book, forms, team and cover, manager dashboard and money; `staffboard.py` and `phoneboard.py` are the shared staff and client shells). `generators/tenders/` builds the Tender Radar and the tender record. Some screens are hand-made and have no generator: Staff, Weekly, PortalWatch, ResubmitStaff, IntroCall, ClientPage, AddClient, Account and most client boards. The scripts were written in a working folder, so their output paths point there: run them with an output folder argument where they take one.
- `super-admin/`: the super admin research and decisions: `decisions.md` (how every conflicting rule was settled), `ia.md` (the plan and shared demo facts), `inventory.json` and `registry.json` (every rule, its value, owner, approval and where it is used), `security-review.md`, `persona-month.md`, `followups.md`.
- `demo-world.md`: the one demo day (Monday 2 November 2026) every staff screen follows.
- `tools/`: the checks used on every board (`audit.js` light and dark, `leftovers.js`, `clickall.js`, `board.js` screenshots, `register.py` canvas placement) and `agent-brief.md` (the board format rules).

## Viewing a screen
The screens use the design canvas runtime, which comes with the Artifact type and is not copied here (`support.js` in each board). The live canvas is the Care Sync Hub design artifact on claude.ai. To view locally, serve `boards/` with a copy of that runtime saved as `boards/support.js`, then open `http://localhost:8765/<Board>.dc.html`.

## Rules for any change
British English; never em or en dashes; plain words; synthetic people only; every rule value read from `registry.js`, never typed into a screen; check light and dark, leftovers and clicks before publishing.
