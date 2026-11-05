# How to work on the Care Sync Hub design boards

SP = /tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad

## Where things are
- Boards: SP/hub-canvas/project/*.dc.html (the design canvas source). Staff boards are 1440 wide; client boards are 390 wide phone boards.
- The one demo world every staff board must follow: SP/demo-world.md. Read it first, fully. It wins over anything a board currently says.
- Shared staff shell generator: SP/gen/staffboard.py (`build(path, title, top, h, body, script, current, css='')`; put `nav: __NAV__` in renderVals and pass the nav key as `current`). Do not edit staffboard.py. Example generator using it: SP/gen/staffpages.py (read it to learn the pattern: CSS classes sb-card, sb-head, sb-h2, sb-row, sb-chip c-ok/c-warn/c-bad/c-info/c-neutral/c-brand, sb-tab t-on/t-off, sb-btn b-pri/b-sec/b-gh, sb-kpi, bar + w0..w100).
- Do NOT edit SP/hub-canvas/project/canvas.json, SP/demo-world.md or staffboard.py. The lead registers new boards on the canvas.
- Design spec (read only, for intent): /home/user/Assets/docs/superpowers/specs/2026-11-02-care-sync-hub-design.md

## Board format rules (break these and the board breaks)
- `.dc.html` files: `<x-dc>` with `<helmet>` (styles), markup with `<sc-for list="{{items}}" as="x">` and `<sc-if value="{{flag}}">`, and a `<script type="text/x-dc" data-dc-script>` holding `class Component extends DCLogic { renderVals() { return {...} } }`. State: `this.state`, `this.setState`. Event handlers are functions returned from renderVals, bound as `onclick="{{fn}}"` or `{{x.pick}}` inside sc-for.
- `{{binding}}` must be a whole attribute value or text content only. Never inside a style attribute or mixed with other text in an attribute (class="sb-chip {{x}}" is WRONG: compute the whole class string in JS).
- No ternaries or expressions in bindings; compute in renderVals.
- Textareas: `<textarea value="{{x}}"></textarea>`, never `<textarea>{{x}}</textarea>`.
- Components: `<x-import component-from-global-scope="CareSync.SideNav" ...>`, CareSync.TopBar, CareSync.Button, CareSync.StatusBadge, CareSync.Icon, CareSync.Alert, CareSync.IconButton. Look at existing boards for attributes.
- Colours only from tokens (var(--cs-...)); both light and dark must work. Body text 13 to 15px, Kanit. Touch targets at least 36px on staff boards.
- The `$preview` height in data-props and the outer min-height should fit the content (set both to the same number; report it).
- Every staff board uses the one staff navigation in demo-world.md (replace whatever nav literal a hand-made board has).

## Writing rules
British English. Never use em dashes or en dashes anywhere (UI text, comments). Plain, kind, short sentences. Synthetic people only. Use they/them for people whose pronouns are not stated, or use names. Never claim a legal fact you are not sure of; say "we check" or keep it general.

## Testing (do this for every board you change or create)
A static server is already running: http://localhost:8765/ serving SP/render. After editing, copy the board: `cp SP/hub-canvas/project/X.dc.html SP/render/project/`.
- Screenshot: `cd SP && node board.js X.dc.html light shots/X.png 1440 1200` (also `dark`), then look at the PNG with the Read tool. It prints any page errors. Check nothing is clipped, nothing overlaps, every tab works.
- Leftovers: grep your rendered text for "[object Object]", "undefined", "NaN", "{{". Quick way: `cd SP && node -e "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});await p.goto('http://localhost:8765/project/X.dc.html');await p.waitForTimeout(1500);const t=await p.evaluate(()=>document.body.innerText);console.log(/\[object Object\]|undefined|NaN|\{\{/.test(t)?'LEFTOVER':'clean');await b.close()})()"`
- Click every tab and button that changes state and check it updates (SP/clickall.js X.dc.html does a quick pass).
- Grep your boards for "—" and "–" (must be none) and for American spellings (-ize, color, center, organization, program).

## Report back (short)
For each board: name, what changed (one line each), final height, test results (errors, leftovers, dark mode). List any fact you needed that demo-world.md did not settle, and what you chose.
