# Board 89: How it fits together. Run: python3 fitmap.py ../hub-canvas/project [height]
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from staffboard import build_sa
from sa_common import SP
OUT = sys.argv[1]
REG = json.load(open(SP + '/superadmin/registry.json'))['rules']
NRULES = len(REG)
NLOCK = sum(e['locked'] for e in REG)

# setting, board, approval line 1, line 2, consumers [(label, sub, outside?)]
ROWS = [
 ('Price book', 'board 77', 'Other super admin', 'New clients only', [('Add a client', 'board 51', 0), ('Plan and costs', 'board 60', 0), ('Your account', 'board 29', 0), ('Stripe instalments', 'payments', 1), ('Xero invoices', 'board 87', 1)]),
 ('Packages and journeys', 'board 81', 'Other super admin', 'New clients only', [('Add a client', 'board 51', 0), ('Your journey', 'board 2', 0), ('Onboarding gates', 'board 8', 0), ('Sessions', 'board 69', 0), ('Aftercare', 'board 71', 0)]),
 ('Forms', 'board 44', 'Other super admin', 'Halfway clients stay', [('Onboarding forms', 'boards 47, 55, 56', 0), ('Gates', 'board 8', 0), ('Checks', 'board 13', 0), ('Application sheet', 'board 13', 0), ('Questions inbox', 'board 67', 0)]),
 ('Rules and promises', 'board 80', 'Super admin or the other', 'Everyone from a date', [('My day', 'board 7', 0), ('Today (client)', 'board 1', 0), ('Weekly update', 'board 9', 0), ('Deadlines', 'board 75', 0), ('Reports', 'board 72', 0)]),
 ('Messages and automations', 'board 82', 'Other super admin', 'For legal wording', [('64 client emails', 'email library', 0), ('46 automations', 'board 82', 0), ('The bell', 'board 41', 0), ('Texts', 'urgent only', 1), ('Quiet hours', '8pm to 8am', 0)]),
 ('People and access', 'board 83', 'Other super admin', 'From a date', [('Every menu', 'by role', 0), ('Client scope', 'assigned, covered', 0), ('Vault reveal', 'board 84', 0), ('Consultant lists', 'board 51', 0), ('Google Workspace', 'and 6 more', 1)]),
 ('Data and privacy', 'board 85', 'Other super admin', 'Retention schedule', [('Deletion runs', '7 days\' notice', 0), ('Privacy page', 'board 29', 0), ('Security page', 'board 62', 0), ('Rights requests', 'board 85', 0), ('Outside systems', 'cleared by hand', 1)]),
]
W, X1, X1W, XG, XGW, XC, CW, CG = 1100, 0, 200, 248, 186, 500, 110, 9
RH, RG, TOP = 62, 16, 64
svg = []
H = TOP + len(ROWS) * (RH + RG) + 74
a = svg.append
a('<svg viewBox="0 0 %d %d" role="img" aria-label="Each super admin setting goes through one approval step, becomes a dated version, and is then read by the screens, emails and outside systems listed on its row." style="width: 100%%; height: auto; display: block;">' % (W, H))
a('<defs><marker id="fm-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="fm-arh" d="M0 0 L10 5 L0 10 z"></path></marker></defs>')
# column headings
a('<text class="fm-h" x="%d" y="20">Super admin setting</text>' % X1)
a('<text class="fm-h" x="%d" y="20">Approval and version</text>' % XG)
a('<text class="fm-h" x="%d" y="20">Reads the live version</text>' % XC)
a('<text class="fm-s" x="%d" y="38">Where it is defined, once</text>' % X1)
a('<text class="fm-s" x="%d" y="38">Who approves, and who it applies to</text>' % XG)
a('<text class="fm-s" x="%d" y="38">Client screens, staff screens, emails and outside systems</text>' % XC)
for i, (name, board, ap1, ap2, cons) in enumerate(ROWS):
    y = TOP + i * (RH + RG)
    cy = y + RH / 2
    a('<rect class="fm-set" x="%d" y="%d" width="%d" height="%d" rx="10"></rect>' % (X1, y, X1W, RH))
    a('<text class="fm-t" x="%d" y="%d">%s</text>' % (X1 + 14, cy - 3, name))
    a('<text class="fm-s" x="%d" y="%d">%s</text>' % (X1 + 14, cy + 15, board))
    a('<line class="fm-ln" x1="%d" y1="%d" x2="%d" y2="%d" marker-end="url(#fm-ar)"></line>' % (X1 + X1W, cy, XG - 2, cy))
    a('<rect class="fm-gate" x="%d" y="%d" width="%d" height="%d" rx="31"></rect>' % (XG, y, XGW, RH))
    a('<text class="fm-gt" x="%d" y="%d" text-anchor="middle">%s</text>' % (XG + XGW / 2, cy - 3, ap1))
    a('<text class="fm-gs" x="%d" y="%d" text-anchor="middle">%s</text>' % (XG + XGW / 2, cy + 15, ap2))
    a('<line class="fm-ln" x1="%d" y1="%d" x2="%d" y2="%d" marker-end="url(#fm-ar)"></line>' % (XG + XGW, cy, XC - 6, cy))
    for j, (lab, sub, outside) in enumerate(cons):
        x = XC + j * (CW + CG)
        a('<rect class="%s" x="%d" y="%d" width="%d" height="%d" rx="8"></rect>' % ('fm-out' if outside else 'fm-con', x, y + 4, CW, RH - 8))
        a('<text class="fm-c" x="%d" y="%d" text-anchor="middle">%s</text>' % (x + CW / 2, cy - 2, lab))
        a('<text class="fm-s" x="%d" y="%d" text-anchor="middle">%s</text>' % (x + CW / 2, cy + 14, sub))
    if i == 0:
        a('<text class="fm-al" x="%d" y="%d" text-anchor="middle">drafts</text>' % ((X1 + X1W + XG) / 2, cy - 8))
        a('<text class="fm-al" x="%d" y="%d" text-anchor="middle">publishes</text>' % ((XG + XGW + XC) / 2, cy - 8))
# locked rules band
yb = TOP + len(ROWS) * (RH + RG) + 6
a('<rect class="fm-lock" x="0" y="%d" width="%d" height="44" rx="10"></rect>' % (yb, W))
a('<text class="fm-t" x="16" y="%d">%d locked rules skip the approval step: they are fixed by law, a regulator or a protected promise, and every screen shows them with their source.</text>' % (yb + 27, NLOCK))
a('</svg>')
SVG = '\n'.join(svg)

AREAS = [
 ('Price book (board 77)', 'PriceBook.dc.html', 'Every price, VAT and instalment split. Anyone may suggest a price; a super admin enters it; the other super admin approves it, for new clients only.', ['Add a client (board 51): package prices and the total', 'Plan and costs (board 60) and Your account (board 29)', 'Stripe instalments, taken after the client signs', 'Xero invoices and the accountant export (board 87)']),
 ('Packages and journeys (board 81)', 'Packages.dc.html', 'What each package includes. A package is offered only when its form, price, journey and emails are ready.', ['Add a client (board 51): which packages can be sold', 'Your journey (board 2) and the 11 stages', 'Onboarding gates (board 8) and handover (board 74)', 'Sessions (board 69) and aftercare (board 71)']),
 ('Forms (board 44)', 'FormBuilder.dc.html', 'Every onboarding form, versioned. Grace drafts; the other super admin approves. Clients halfway through stay on their version unless moved.', ['The client forms (boards 47, 55, 56, 38)', 'Gates (board 8) and checks (board 13)', 'The application sheet for each regulator (board 13)', 'Suggested replies in the Questions inbox (board 67)']),
 ('Rules and promises (board 80)', 'Rules.dc.html', 'Every timing, threshold and promise, %d rules in all. Boards read them from one registry, so a change shows everywhere at once.' % NRULES, ['My day (board 7) and the weekly update (board 9)', 'Today (board 1), Ask (board 6) and every client screen with a promise', 'Deadlines (board 75): our targets and the legal dates', 'Reports (board 72): each promise measured against the one in force']),
 ('Messages and automations (board 82)', 'Messages.dc.html', 'The 64 client emails and 46 automations. Legal wording needs the other super admin; quiet hours come from Rules and promises.', ['Every client email, with merge fields filled', 'The bell (board 41) and urgent texts', 'Automation failures on System health (board 86)']),
 ('People and access (board 83)', 'PeopleAccess.dc.html', 'Roles and permissions. Super admin is a flag on a role. Changes need the other super admin.', ['Every menu and which clients each person sees', 'Vault reveal and cover delegation (boards 84 and 78)', 'Consultant lists in Add a client (board 51)', 'Accounts in Google Workspace and the other systems']),
 ('Data and privacy (board 85)', 'DataPrivacy.dc.html', 'The retention schedule, legal holds and rights requests. Collins is the data protection lead.', ['Scheduled deletion runs, with 7 days\' notice', 'The client\'s privacy page (board 29)', 'How we keep your information safe (board 62)']),
]

CSS = '''.fm-h{fill:var(--cs-text-primary);font:600 14px Kanit, sans-serif}
.fm-s{fill:var(--cs-text-secondary);font:400 11.5px Kanit, sans-serif}
.fm-t{fill:var(--cs-text-primary);font:500 13.5px Kanit, sans-serif}
.fm-c{fill:var(--cs-text-primary);font:500 12.5px Kanit, sans-serif}
.fm-al{fill:var(--cs-text-muted);font:500 11.5px Kanit, sans-serif}
.fm-gt{fill:var(--cs-text-brand);font:600 12.5px Kanit, sans-serif}
.fm-gs{fill:var(--cs-text-brand);font:400 11.5px Kanit, sans-serif}
.fm-set{fill:var(--cs-surface-raised);stroke:var(--cs-text-primary);stroke-width:1.5}
.fm-gate{fill:var(--cs-surface-brand);stroke:var(--cs-action-primary);stroke-width:1.5}
.fm-con{fill:var(--cs-surface-subtle);stroke:var(--cs-border-default);stroke-width:1}
.fm-out{fill:var(--cs-surface-raised);stroke:var(--cs-border-default);stroke-width:1.2;stroke-dasharray:4 3}
.fm-lock{fill:var(--cs-surface-subtle);stroke:none}
.fm-ln{stroke:var(--cs-text-muted);stroke-width:1.5;fill:none}
.fm-arh{fill:var(--cs-text-muted)}
.fm-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.fm-card{padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.fm-li{font-size:13px;line-height:18px;display:flex;gap:8px}
.fm-dot{width:6px;height:6px;border-radius:999px;background:var(--cs-action-primary);margin-top:6px;flex-shrink:0}
.bz-link{color:var(--cs-text-link);text-decoration:underline;text-underline-offset:2px;font-weight:500;font-size:13px}
.fm-key{display:inline-flex;align-items:center;gap:8px;font-size:13px;line-height:18px;color:var(--cs-text-secondary)}
.fm-sw{width:26px;height:16px;border-radius:5px;box-sizing:border-box;display:inline-block}
'''

BODY = '''      <div style="display: flex; flex-direction: column; gap: 4px; max-width: 860px;">
        <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">How it fits together</h1>
        <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Each setting is defined once, in super admin. A change goes through one approval step, becomes a dated version, and every screen, email and outside system on its row reads that version. Nothing holds its own copy.</span>
      </div>

      <section class="sb-card" style="padding: 20px 24px; display: flex; flex-direction: column; gap: 14px;" aria-labelledby="fm-h">
        <h2 id="fm-h" class="sb-h2">From a setting to every place that uses it</h2>
        <figure style="margin: 0; display: flex; flex-direction: column; gap: 12px;">
''' + SVG + '''
          <figcaption style="display: flex; gap: 20px; flex-wrap: wrap; align-items: center;">
            <span class="fm-key"><span class="fm-sw" style="border: 1.5px solid var(--cs-text-primary); background: var(--cs-surface-raised);"></span>Where the setting lives</span>
            <span class="fm-key"><span class="fm-sw" style="border: 1.5px solid var(--cs-action-primary); background: var(--cs-surface-brand); border-radius: 999px;"></span>Approval, then a dated version</span>
            <span class="fm-key"><span class="fm-sw" style="border: 1px solid var(--cs-border-default); background: var(--cs-surface-subtle);"></span>A Hub screen or message</span>
            <span class="fm-key"><span class="fm-sw" style="border: 1.2px dashed var(--cs-border-default); background: var(--cs-surface-raised);"></span>An outside system or a manual step</span>
          </figcaption>
        </figure>
      </section>

      <div class="fm-grid">
        <sc-for list="{{areas}}" as="ar" hint-placeholder-count="7">
          <section class="sb-card fm-card">
            <a class="bz-link" style="font-size: 16px; line-height: 22px;" href="{{ar.file}}">{{ar.name}}</a>
            <span class="sb-sub">{{ar.what}}</span>
            <span class="sb-th" style="margin-top: 2px;">Read by</span>
            <sc-for list="{{ar.uses}}" as="u" hint-placeholder-count="4"><span class="fm-li"><span class="fm-dot"></span><span>{{u.t}}</span></span></sc-for>
          </section>
        </sc-for>
        <section class="sb-card fm-card">
          <span class="sb-h2" style="font-size: 16px; line-height: 22px;">When something fails</span>
          <span class="sb-sub">Nothing fails silently. A failed sync, automation, delivery or watch shows on System health (board 86) with what it affects and who is told.</span>
          <a class="bz-link" href="Health.dc.html">System health (board 86)</a>
        </section>
      </div>
'''
SCRIPT = r'''class Component extends DCLogic {
  renderVals() {
    const A = __AREAS__;
    return {
      theme: this.props.theme ?? 'light', three: 7, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      areas: A.map(([name, file, what, uses]) => ({ name, file, what, uses: uses.map(t => ({ t })) }))
    };
  }
}'''.replace('__AREAS__', json.dumps(AREAS, ensure_ascii=False))
HH = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
build_sa(OUT + '/FitsTogether.dc.html', 'How it fits together', 'How it fits together', HH, BODY, SCRIPT, 'map', CSS)
print('ok', H)
