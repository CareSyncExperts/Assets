# Register new staff boards on the canvas and sync heights of existing boards from their $preview.
import json, re, sys, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hub-canvas/project')
c = json.load(open(P + '/canvas.json'))
B = c['boards']

def preview_h(name):
    s = open(P + '/' + name).read()
    m = re.search(r'"\$preview":\{"width":(\d+),"height":(\d+)\}', s)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)

NEW = [
    # row, name, title
    (0, 'ClientsList.dc.html', '68. Clients: every client, with filters for mine, covering, needs attention and each regulator (staff, try the tabs)'),
    (0, 'Deadlines.dc.html', '75. Deadlines: legal and internal dates across every client, list and month (staff, try it)'),
    (0, 'RegReply.dc.html', '76. Answer the regulator: Notice of Proposal representations and a request for more information (staff, try the tabs)'),
    (1, 'OnboardingQueue.dc.html', '73. Onboarding queue: every client in onboarding, waiting on whom, nudge (Grace, try it)'),
    (1, 'Handover.dc.html', '74. Handover from onboarding to the case owner, with manager approval (try approving)'),
    (1, 'CoachSessions.dc.html', '69. Sessions and interview practice (Millicent)'),
    (2, 'ClientCare.dc.html', '70. Client care: introduction calls, concerns, gone quiet (Divine)'),
    (2, 'AftercareStaff.dc.html', '71. Aftercare: the 12 months after registration, by regulator (staff, try the tabs)'),
    (2, 'Reports.dc.html', '72. Reports: promises kept, days per stage, outcomes by regulator, tenders (directors)'),
    (3, 'PriceBook.dc.html', '77. Price book: every price, VAT and instalments, changes need the second super admin (try editing)'),
    (3, 'TeamCover.dc.html', '78. Team and cover: workload, leave and cover delegation, leavers (try booking leave)'),
    (4, 'GoLive.dc.html', '79. Super admin: go-live readiness and setup mode (try entering the ICO number)'),
    (4, 'Rules.dc.html', '80. Super admin: Rules and promises, every rule defined once, where it is used, change and approve (try it)'),
    (4, 'Packages.dc.html', '81. Super admin: Packages and journeys, each package end to end (try adding a package)'),
    (5, 'Messages.dc.html', '82. Super admin: Messages and automations, preview any email as a real client (try approving 5.2 v3)'),
    (5, 'PeopleAccess.dc.html', '83. Super admin: People and access, roles grid, joiners, leavers, access review'),
    (5, 'SecurityCentre.dc.html', '84. Super admin: Security, incidents and the 72-hour clock, audit log, vault, elevated access, sign-in'),
    (6, 'DataPrivacy.dc.html', '85. Super admin: Data and privacy, retention, deletions, rights requests, records, suppliers'),
    (6, 'Health.dc.html', '86. Super admin: System health, every connection, failures and retries, email delivery, backups'),
    (6, 'MoneyExports.dc.html', '87. Super admin: Money and exports, month close, accountant export, Stripe and Xero'),
    (7, 'ViewAs.dc.html', '88. Super admin: View as, communication history and the complaints register (try viewing as Amara)'),
    (7, 'FitsTogether.dc.html', '89. Super admin: how it fits together, every setting and what reads it'),
]
names = [n for _, n, _ in NEW]
# sync heights of every board from $preview; when a board grows, push down everything below its old bottom
grow = []
for name, b in B.items():
    if name in names: continue
    w, h = preview_h(name)
    if h and h != b['h']:
        print('resize', name, b['h'], '->', h)
        grow.append((b['y'] + b['h'], h - b['h'], name)); b['h'] = h
# shift by the largest growth per old row bottom, cumulatively
shift_at = {}
for bottom, d, name in grow:
    if d > 0: shift_at[bottom] = max(shift_at.get(bottom, 0), d)
for bottom in sorted(shift_at, reverse=True):
    d = shift_at[bottom]
    for name, b in B.items():
        if name in names: continue
        if b['y'] >= bottom: b['y'] += d
top = max(b['y'] + b['h'] for k, b in B.items() if k not in names) + 300
rows = {}
for row, name, title in NEW:
    if not os.path.exists(P + '/' + name):
        print('missing', name); continue
    rows.setdefault(row, []).append((name, title))
y = top
for row in sorted(rows):
    x = 0; hmax = 0
    for name, title in rows[row]:
        w, h = preview_h(name)
        if name in B:
            b = B[name]; b.update({'title': title, 'w': w, 'h': h, 'x': x, 'y': y})
        else:
            B[name] = {'title': title, 'w': w, 'h': h, 'x': x, 'y': y, 'expand': 'fill', 'is_interactive': True}
        x += w + 80; hmax = max(hmax, h)
    y += hmax + 300
# report overlaps
items = list(B.items())
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        (n1, a), (n2, b) = items[i], items[j]
        if a['x'] < b['x'] + b['w'] and b['x'] < a['x'] + a['w'] and a['y'] < b['y'] + b['h'] and b['y'] < a['y'] + a['h']:
            print('OVERLAP', n1, n2)
if '--write' in sys.argv:
    json.dump(c, open(P + '/canvas.json', 'w'), indent=1)
    print('written', len(B), 'boards')
