# Board 80: Rules and promises (the registry). Run: python3 rules.py ../hub-canvas/project
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from staffboard import build_sa
from sa_common import SP, EMAILS
OUT = sys.argv[1]
REG = json.load(open(SP + '/superadmin/registry.json'))['rules']
AREAS = ['Promises and timings', 'Journey and gates', 'Sessions and coaching', 'Regulators', 'Tenders', 'Money', 'People and access', 'Security',
         'Data and privacy', 'Messages and notifications', 'Forms and templates', 'Branding and wording', 'Integrations', 'Aftercare and growth', 'Reviews and feedback']
KINDS = ['client', 'staff', 'email', 'automation', 'report']
# compact encoding with string tables
tabs = {k: [] for k in ['owner', 'source', 'approval', 'effective', 'unit', 'cl', 'by', 'vef']}
def T(k, s):
    t = tabs[k]
    if s not in t: t.append(s)
    return t.index(s)
rows = []
for e in REG:
    used = [[KINDS.index(u['kind']), u['ref'], u['says']] for u in e['used_in']]
    vers = [[v['v'], v['date'], v['value'], T('by', v['by']), v['status'], T('vef', v['effective'])] for v in e['versions']]
    w = e['waiting']
    rows.append([e['id'], AREAS.index(e['area']), e['name'], e['rule'], e['value'], T('unit', e['unit']), 1 if e['legal'] else 0, T('source', e['source']),
                 1 if e['locked'] else 0, T('owner', e['owner']), T('approval', e['approval']), T('effective', e['effective']), used, vers,
                 e['clients_now'], T('cl', e['clients_label']), 1 if e['changed_this_month'] else 0,
                 [w['value'], w['by'], w['on'], w['waiting'], w['where'], w['file']] if w else 0, e['registry_key'], e['note']])
DATA = json.dumps({'areas': AREAS, 'tabs': tabs, 'rows': rows}, separators=(',', ':'), ensure_ascii=False)

def E(n):
    return n + ' ' + EMAILS.get(n, '')
F7, F3, F2 = 'CQC form v7', 'CIW form v3', 'RQIA form v2'
G = ['Gate 1 Company and directors', 'Gate 2 Identity', 'Gate 3 Office address evidence', 'Gate 4 Registered manager', 'Gate 5 Employment history', 'Gate 6 References', 'Gate 7 DBS', 'Gate 8 Professional registers']
ALL3 = ['CQC', 'CIW', 'RQIA']
# Regulator requirements: what depends on each (forms, gates and checks, Pack Doctor rules, emails, screens)
REQ = {
 'nop-representation-deadline': ('Legal deadlines', ALL3, [], ['Legal deadline calculator', 'Deadlines (board 75)'], ['Cover note shows the legal deadline'], ['5.2', '10.8', '11.6'], ['board 76 Answer the regulator', 'board 5 CQC centre']),
 'appeal-deadline': ('Legal deadlines', ALL3, [], ['Legal deadline calculator', 'Deadlines (board 75)'], [], ['5.3a', '10.9', '11.7'], ['board 65 Refused: we resubmit', 'board 66 Resubmission project']),
 'withdraw-before-notice': ('Legal deadlines', ['CQC'], [], ['Withdraw option closes when a notice is served'], [], ['5.2'], ['board 76 Answer the regulator']),
 'legal-alerts-always-on': ('Legal deadlines', ALL3, [], ['Legal deadline alerts, cannot be switched off'], [], ['5.2', '5.3a'], ['board 7 My day', 'board 75 Deadlines']),
 'nop-internal-targets': ('Our targets around regulator dates', ALL3, [], ['Senior review on day 20'], ['Representations reviewed by a second person'], ['5.2'], ['board 75 Deadlines', 'board 76 Answer the regulator']),
 'nop-alert-schedule': ('Our targets around regulator dates', ALL3, [], ['Alerts on day 7, 14, 21 and 25, then daily'], [], [], ['board 7 My day', 'board 43 Manager dashboard']),
 'rfi-reply-targets': ('Our targets around regulator dates', ALL3, [], ['Target date 4 working days before the regulator\'s date'], ['Answer checked against the request'], ['4.2', '10.5', '11.3'], ['board 75 Deadlines', 'board 76 Answer the regulator']),
 'resubmission-promise': ('Our targets around regulator dates', ALL3, [], ['No charge to the client on the resubmission project'], [], ['5.3a', '5.3b', '10.9', '11.7'], ['board 65 Refused: we resubmit', 'board 60 Plan and costs']),
 'resubmission-gate': ('Our targets around regulator dates', ALL3, [], ['Resubmission gate, 7 items (board 66)'], ['Whole pack checked again, not only the reasons'], ['5.3b'], ['board 66 Resubmission project']),
 'resubmission-refresh-ages': ('Our targets around regulator dates', ALL3, [F7 + ': DBS issue date'], ['Refresh check (board 66)'], ['DBS under 12 months, references under 6 months'], ['5.3b', '11.8'], ['board 66 Resubmission project']),
 'refusal-same-day-actions': ('Our targets around regulator dates', ALL3, [], ['Same-day tasks after a refusal'], [], ['5.3a', '10.9', '11.7'], ['board 66 Resubmission project']),
 'refusal-kind-check-in': ('Our targets around regulator dates', ALL3, [], ['Check-in task a week later'], [], [], ['board 70 Client care']),
 'resubmission-target': ('Our targets around regulator dates', ALL3, [], ['Target set by the manager'], [], ['5.3b'], ['board 66 Resubmission project']),
 'dbs-age-rules': ('Evidence the regulator asks for', ['CQC', 'CIW'], [F7 + ': manager DBS details', F3 + ': DBS', F2 + ': AccessNI'], [G[6], 'DBS age at submission (board 13)'], ['DBS dated within 12 months of submission'], ['2.4'], ['board 8 Onboarding gates']),
 'identity-documents': ('Evidence the regulator asks for', ALL3, [F7 + ': identity', F3 + ': identity', F2 + ': identity for AccessNI'], [G[1], 'Address and identity check (board 14)'], [], ['2.4', '11.1'], ['board 34 Snap and send']),
 'brp-expiry-allowance': ('Evidence the regulator asks for', ALL3, [F7 + ': identity'], [G[1], 'Address and identity check (board 14)'], [], ['2.4'], []),
 'proof-of-address-age': ('Evidence the regulator asks for', ALL3, [F7 + ': proof of address'], [G[1], G[2], 'Address and identity check (board 14)'], [], ['2.4'], ['board 15 One quick question']),
 'address-history-length': ('Evidence the regulator asks for', ALL3, [F7 + ': address history', F3 + ': address history', F2 + ': address history'], [G[1], 'Address gap warning (board 61)'], ['5 years of addresses for each person'], ['2.4'], ['board 61 Address history']),
 'cv-gap-rules': ('Evidence the regulator asks for', ALL3, [F7 + ': registered manager details', F3 + ': employment history', F2 + ': employment history'], [G[4], 'CV gap check (board 13)'], ['Every gap explained in the CV'], ['2.4'], ['board 52 After the form (fix list)']),
 'referee-rules': ('Evidence the regulator asks for', ALL3, [F7 + ': reference details', F3 + ': references', F2 + ': references'], [G[5], 'Referee link (board 37)'], ['References match the regulator\'s rule'], ['10.2'], ['board 37 One-task links']),
 'psc-threshold': ('Checks and formats', ALL3, [F7 + ': directors and owners'], [G[0], 'Companies House match (board 13)'], ['Owners over 25% listed'], ['2.4'], ['board 36 Directors and owners']),
 'format-checks': ('Checks and formats', ALL3, [F7, F3, F2], [G[0], G[6], 'Format checks on every form'], [], [], ['board 13 Form received and checks']),
 'regulator-fixed-facts': ('Checks and formats', ['CIW', 'RQIA'], [F3 + ': areas and hours bands', F2 + ': HSC Trust'], ['Lists inside the forms'], ['Statement of Purpose uses the right areas'], ['11.1'], ['board 63 Your regulator']),
 'ciw-start-date': ('Checks and formats', ['CIW'], [F3 + ': planned start date'], ['Start date at least 14 weeks ahead'], ['Statement of Purpose start date'], ['10.3'], ['board 63 Your regulator']),
 'ciw-post-registration-duties': ('After registration duties', ['CIW'], [], ['Aftercare schedule (board 71)'], [], ['10.7', '6.1'], ['board 30 Aftercare and growing', 'board 71 Aftercare (staff)']),
 'rqia-post-registration-duties': ('After registration duties', ['RQIA'], [], ['Aftercare schedule (board 71)'], [], ['11.5'], ['board 30 Aftercare and growing', 'board 71 Aftercare (staff)']),
}
reg_ids = [e['id'] for e in REG if e['area'] == 'Regulators']
assert set(reg_ids) == set(REQ), set(reg_ids) ^ set(REQ)
REQD = json.dumps([[i, g, regs, forms, gates, pack, [E(n) for n in emails], screens] for i, (g, regs, forms, gates, pack, emails, screens) in REQ.items()], separators=(',', ':'), ensure_ascii=False)

CSS = '''.bz-in{min-height:40px;padding:0 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;box-sizing:border-box}
.bz-ta{width:100%;min-height:64px;padding:8px 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;line-height:20px;box-sizing:border-box;resize:vertical}
.bz-in:focus-visible,.bz-ta:focus-visible,.rl-area:focus-visible,.bz-link:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:1px}
.bz-err{font-size:13px;line-height:18px;color:var(--cs-status-error-text);font-weight:500}
.bz-box{padding:12px 14px;border-radius:10px;background:var(--cs-surface-subtle);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-amb{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-warning-border);background:var(--cs-status-warning-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-ok{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-success-border);background:var(--cs-status-success-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-info{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-info-border);background:var(--cs-status-info-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-lbl{font-size:12px;line-height:16px;color:var(--cs-text-muted);font-weight:500}
.bz-b{font-weight:500}
.bz-link{color:var(--cs-text-link);text-decoration:underline;text-underline-offset:2px;font-weight:500}
.rl-cols{display:grid;grid-template-columns:232px minmax(0,1fr);gap:18px;align-items:start}
.rl-areas{display:flex;flex-direction:column;padding:8px}
.rl-area{display:flex;justify-content:space-between;align-items:center;gap:8px;min-height:38px;padding:0 12px;border-radius:8px;border:0;background:transparent;color:var(--cs-text-secondary);font:inherit;font-size:14px;text-align:left;cursor:pointer}
.rl-area.on{background:var(--cs-surface-brand);color:var(--cs-text-brand);font-weight:500}
.rl-area .n{font-size:12px;color:var(--cs-text-muted)}
.rl-rule{padding:14px 20px;border-top:1px solid var(--cs-border-subtle);display:flex;flex-direction:column;gap:8px}
.rl-top{display:grid;grid-template-columns:minmax(0,1fr) 210px 168px;gap:16px;align-items:start}
.rl-name{font-size:15px;line-height:22px;font-weight:500}
.rl-val{font-size:14px;line-height:20px;color:var(--cs-text-primary)}
.rl-meta{font-size:12px;line-height:17px;color:var(--cs-text-muted)}
.rl-chips{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.rl-det{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:16px;padding:12px 14px;border-radius:10px;background:var(--cs-surface-subtle)}
.rl-k{font-size:12px;line-height:16px;color:var(--cs-text-muted);font-weight:600}
.rl-li{display:grid;grid-template-columns:106px minmax(0,1fr);gap:8px;font-size:13px;line-height:18px;padding:3px 0}
.rl-q{color:var(--cs-text-secondary)}
.rl-ver{display:grid;grid-template-columns:30px 112px minmax(0,1fr);gap:8px;font-size:13px;line-height:18px;padding:4px 0;border-top:1px solid var(--cs-border-subtle)}
.rl-edit{border:2px solid var(--cs-action-primary);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:12px;background:var(--cs-surface-raised)}
.rl-steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.rl-step{display:flex;flex-direction:column;gap:6px}
.rl-imp{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px}
.rl-imp div{padding:10px 12px;border-radius:10px;background:var(--cs-surface-subtle);display:flex;flex-direction:column;gap:2px}
.rl-imp b{font-size:20px;line-height:26px;font-weight:600}
.rl-pick{min-height:36px;padding:0 12px;border-radius:10px;font:inherit;font-size:13px;cursor:pointer}
.p-on{border:2px solid var(--cs-action-primary);background:var(--cs-surface-brand);color:var(--cs-text-brand);font-weight:500}
.p-off{border:1px solid var(--cs-border-default);background:var(--cs-surface-raised);color:var(--cs-text-primary)}
.rl-lock{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border-radius:10px;border:1px solid var(--cs-border-default);background:var(--cs-surface-raised);font-size:13px;line-height:18px}
.rl-try{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:18px;align-items:start}
.rl-sel{min-height:40px;padding:0 10px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px}
.rq-row{padding:14px 20px;border-top:1px solid var(--cs-border-subtle);display:flex;flex-direction:column;gap:10px}
.rq-deps{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
.rq-dep{display:flex;flex-direction:column;gap:4px;font-size:13px;line-height:18px}
.rq-dep span.i{padding:4px 8px;border-radius:8px;background:var(--cs-surface-subtle)}
.rq-plan{display:grid;grid-template-columns:150px minmax(0,1fr) 190px;gap:10px;font-size:13px;line-height:18px;padding:8px 0;border-top:1px solid var(--cs-border-subtle)}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
'''

TABS = '''<div role="tablist" aria-label="__LABEL__" style="display: flex; gap: 6px; flex-wrap: wrap;">
          <sc-for list="{{__LIST__}}" as="tb" hint-placeholder-count="4">
            <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
            <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
          </sc-for>
        </div>'''
def tabs_(lst, label):
    return TABS.replace('__LIST__', lst).replace('__LABEL__', label)

BODY = '''      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 4px; max-width: 820px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Rules and promises</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Every rule the Hub follows is defined once, here. Client screens, staff screens, emails, automations and reports read it, so a change shows everywhere at once. Rules fixed by law, a regulator or a protected promise are locked.</span>
        </div>
        <a class="sb-btn b-gh" style="display: inline-flex; align-items: center; text-decoration: none;" href="FitsTogether.dc.html">How it fits together (board 89)</a>
      </div>
      ''' + tabs_('mainTabs', 'Rules or regulator requirements') + '''

      <sc-if value="{{isRules}}" hint-placeholder-val="{{ true }}">
      <div style="display: flex; flex-direction: column; gap: 18px;">
        <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
          <sc-for list="{{kpis}}" as="k" hint-placeholder-count="4">
            <div class="sb-card sb-kpi"><span class="sb-muted">{{k.k}}</span><span class="sb-kv">{{k.v}}</span><span class="sb-sub">{{k.note}}</span></div>
          </sc-for>
        </div>

        <section class="sb-card" aria-labelledby="wt-h">
          <div class="sb-head"><h2 id="wt-h" class="sb-h2">Waiting for approval</h2><span class="sb-sub">These are part of the 7 decisions on Home. Each is decided on its own board, with a reason.</span></div>
          <sc-for list="{{waitList}}" as="w" hint-placeholder-count="4">
            <div class="sb-row" style="align-items: flex-start;">
              <span class="sb-chip c-warn" style="flex-shrink: 0;">Waiting</span>
              <span style="flex: 1 1 auto; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{w.name}}</span><span class="sb-sub">{{w.text}}</span></span>
              <a class="bz-link" style="font-size: 13px; white-space: nowrap;" href="{{w.file}}">{{w.where}}</a>
            </div>
          </sc-for>
        </section>

        <section class="sb-card" aria-labelledby="try-h" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 12px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 12px; flex-wrap: wrap;"><h2 id="try-h" class="sb-h2">Try it in this browser</h2><span class="{{trialChipCls}}">{{trialChip}}</span></div>
          <div class="rl-try">
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <span class="sb-sub">See a change on the other boards before anyone approves it. This writes a trial value in this browser only: no client is told and nothing is published. Then open Welcome (board 25), Your account (board 29), Notifications (board 41) or Plan and costs (board 60) for the day, and the Questions inbox (board 67) or Reports (board 72) for the reply promise.</span>
              <div style="display: flex; gap: 12px; flex-wrap: wrap; align-items: flex-end;">
                <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">Weekly update day</span><select class="rl-sel" value="{{tryDay}}" onChange="{{onTryDay}}"><option>Wednesday</option><option>Thursday</option><option>Friday</option></select></label>
                <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">Reply promise for client questions</span><select class="rl-sel" value="{{tryReply}}" onChange="{{onTryReply}}"><option>4 working hours</option><option>1 working day</option><option>2 working days</option></select></label>
                <button class="sb-btn b-pri" onClick="{{applyTrial}}">Try it</button>
                <button class="sb-btn b-gh" onClick="{{clearTrial}}">Clear trial</button>
              </div>
            </div>
            <div class="bz-box" role="status">
              <span class="bz-b">{{trialTitle}}</span>
              <sc-for list="{{trialLines}}" as="t" hint-placeholder-count="3"><span class="sb-sub">{{t.t}}</span></sc-for>
            </div>
          </div>
        </section>

        <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
          <label style="flex: 1 1 320px; display: flex;"><span class="sr-only">Search rules</span><input class="bz-in" style="width: 100%;" value="{{q}}" onChange="{{onQ}}" placeholder="Search a rule, a value, a board or an email number"></label>
          ''' + tabs_('filters', 'Filter rules') + '''
        </div>

        <div class="rl-cols">
          <nav class="sb-card rl-areas" aria-label="Areas">
            <sc-for list="{{areaList}}" as="a" hint-placeholder-count="16">
              <button class="{{a.cls}}" aria-pressed="{{a.pressed}}" onClick="{{a.pick}}"><span>{{a.label}}</span><span class="n">{{a.n}}</span></button>
            </sc-for>
          </nav>
          <section class="sb-card" aria-labelledby="list-h">
            <div class="sb-head"><h2 id="list-h" class="sb-h2">{{listTitle}}</h2><span class="sb-sub">{{listSub}}</span></div>
            <sc-if value="{{noRows}}" hint-placeholder-val="{{ false }}"><div class="sb-row"><span class="sb-sub">No rule matches. Try another word, or choose All.</span></div></sc-if>
            <sc-for list="{{rows}}" as="r" hint-placeholder-count="6">
              <div class="rl-rule">
                <div class="rl-top">
                  <div style="display: flex; flex-direction: column; gap: 4px; min-width: 0;">
                    <div class="rl-chips"><span class="rl-name">{{r.name}}</span><sc-for list="{{r.chips}}" as="c" hint-placeholder-count="1"><span class="{{c.cls}}">{{c.t}}</span></sc-for></div>
                    <span class="rl-val">{{r.value}}</span>
                    <span class="rl-meta">{{r.meta}}</span>
                  </div>
                  <div style="display: flex; flex-direction: column; gap: 2px;">
                    <span class="rl-k">Used in</span><span style="font-size: 13px; line-height: 18px;">{{r.usedSum}}</span>
                    <span class="rl-k" style="margin-top: 4px;">Clients affected now</span><span style="font-size: 13px; line-height: 18px;">{{r.clients}}</span>
                  </div>
                  <div style="display: flex; flex-direction: column; gap: 6px; align-items: stretch;">
                    <button class="sb-btn b-gh" aria-expanded="{{r.expanded}}" onClick="{{r.toggle}}">{{r.toggleLabel}}</button>
                    <sc-if value="{{r.canEdit}}" hint-placeholder-val="{{ true }}"><button class="sb-btn b-sec" onClick="{{r.edit}}">Change this rule</button></sc-if>
                    <sc-if value="{{r.isLocked}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-neutral" style="justify-content: center; min-height: 36px; border-radius: 10px; gap: 6px;"><x-import component-from-global-scope="CareSync.Icon" name="lock" size="{{n16}}"></x-import>{{r.lockLabel}}</span></sc-if>
                    <sc-if value="{{r.isBusy}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-warn" style="justify-content: center; min-height: 36px; border-radius: 10px;">{{r.busyLabel}}</span></sc-if>
                  </div>
                </div>
                <sc-if value="{{r.isLocked}}" hint-placeholder-val="{{ false }}"><div class="rl-lock"><x-import component-from-global-scope="CareSync.Icon" name="lock" size="{{n16}}"></x-import><span><span class="bz-b">{{r.lockTitle}}</span> {{r.source}}</span></div></sc-if>

                <sc-if value="{{r.isEditing}}" hint-placeholder-val="{{ false }}">
                  <div class="rl-edit" role="group" aria-label="Change this rule">
                    <div style="display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap;"><span class="bz-b">Change: {{r.name}}</span><span class="sb-sub">{{r.routeNote}}</span></div>
                    <div class="rl-steps">
                      <div class="rl-step"><span class="rl-k">1. The change</span>
                        <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">New value (now: {{r.value}})</span><input class="bz-in" value="{{ev}}" onChange="{{onEv}}"></label>
                        <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">Why (the approver reads this)</span><textarea class="bz-ta" value="{{er}}" onChange="{{onEr}}" placeholder="For example: clients asked for updates before the weekend"></textarea></label>
                      </div>
                      <div class="rl-step"><span class="rl-k">2. Who it applies to</span>
                        <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="{{effNewCls}}" aria-pressed="{{effNewP}}" onClick="{{pickNew}}">New clients only</button><button class="{{effDateCls}}" aria-pressed="{{effDateP}}" onClick="{{pickDate}}">Everyone from a date</button></div>
                        <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">{{dateLabel}}</span><input class="bz-in" value="{{edate}}" onChange="{{onDate}}"></label>
                        <span class="sb-sub">{{effNote}}</span>
                      </div>
                      <div class="rl-step"><span class="rl-k">3. Approval</span>
                        <span class="sb-sub">{{r.approvalText}}</span>
                        <sc-if value="{{eErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">{{eErrText}}</span></sc-if>
                        <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{sendEdit}}">{{r.sendLabel}}</button><button class="sb-btn b-gh" onClick="{{cancelEdit}}">Cancel</button></div>
                      </div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                      <span class="rl-k">Impact preview: what changes when this is published</span>
                      <div class="rl-imp">
                        <sc-for list="{{r.impact}}" as="m" hint-placeholder-count="5"><div><b>{{m.n}}</b><span class="sb-muted">{{m.k}}</span></div></sc-for>
                      </div>
                      <sc-for list="{{r.impactLines}}" as="l" hint-placeholder-count="3"><span style="font-size: 13px; line-height: 18px;">{{l.t}}</span></sc-for>
                    </div>
                  </div>
                </sc-if>

                <sc-if value="{{r.hasDecision}}" hint-placeholder-val="{{ false }}">
                  <div class="{{r.decCls}}" role="status">
                    <span class="bz-b">{{r.decTitle}}</span>
                    <span class="sb-sub">{{r.decText}}</span>
                    <sc-if value="{{r.canDecide}}" hint-placeholder-val="{{ false }}">
                      <div style="display: flex; flex-direction: column; gap: 8px;">
                        <span class="sb-sub">Demo: act as {{r.approver}}. Collins cannot approve his own change.</span>
                        <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">{{r.approver}}'s note (needed to approve or decline)</span><textarea class="bz-ta" value="{{decNote}}" onChange="{{onDecNote}}" placeholder="For example: agreed, the team rhythm moves a day earlier too"></textarea></label>
                        <sc-if value="{{decErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Write a note first. Every decision is recorded with its reason.</span></sc-if>
                        <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{r.approve}}">{{r.approveLabel}}</button><button class="sb-btn b-gh" onClick="{{r.decline}}">Decline</button></div>
                      </div>
                    </sc-if>
                  </div>
                </sc-if>

                <sc-if value="{{r.expanded}}" hint-placeholder-val="{{ false }}">
                  <div class="rl-det">
                    <div style="display: flex; flex-direction: column; gap: 10px; min-width: 0;">
                      <div style="display: flex; flex-direction: column; gap: 2px;"><span class="rl-k">Why this rule exists</span><span style="font-size: 13px; line-height: 18px;">{{r.why}}</span><span class="sb-muted">{{r.note}}</span></div>
                      <div style="display: flex; flex-direction: column;"><span class="rl-k">Used in: {{r.usedSum}}</span>
                        <sc-for list="{{r.used}}" as="u" hint-placeholder-count="4"><div class="rl-li"><span class="{{u.cls}}">{{u.kind}}</span><span><span>{{u.ref}}</span> <span class="rl-q">{{u.says}}</span></span></div></sc-for>
                        <sc-if value="{{r.noUsed}}" hint-placeholder-val="{{ false }}"><span class="sb-sub">Not shown on a screen or in an email. Followed by the team and by the Hub in the background.</span></sc-if>
                      </div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 10px; min-width: 0;">
                      <div style="display: flex; flex-direction: column;"><span class="rl-k">Version history</span>
                        <sc-for list="{{r.vers}}" as="v" hint-placeholder-count="2"><div class="rl-ver"><span class="bz-b">v{{v.v}}</span><span class="sb-sub">{{v.date}}</span><span><span>{{v.value}}</span><br><span class="rl-meta">{{v.by}}. {{v.ef}}. {{v.st}}</span></span></div></sc-for>
                      </div>
                      <div style="display: flex; flex-direction: column; gap: 2px;"><span class="rl-k">Unit and setting</span><span class="sb-sub">{{r.unitText}}</span></div>
                    </div>
                  </div>
                </sc-if>
              </div>
            </sc-for>
          </section>
        </div>
      </div>
      </sc-if>

      <sc-if value="{{isReq}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; flex-direction: column; gap: 18px;">
        <div style="display: flex; justify-content: space-between; align-items: center; gap: 14px; flex-wrap: wrap;">
          <span class="sb-sub" style="max-width: 760px; font-size: 14px; line-height: 20px;">Each regulator requirement the Hub uses, with every form, gate, check, Pack Doctor rule and email that depends on it. When a regulator changes something, start here: the change plan covers all of them, so nothing is left saying the old thing.</span>
          <button class="sb-btn b-pri" onClick="{{openChange}}">A regulator changed something</button>
        </div>

        <sc-if value="{{chOpen}}" hint-placeholder-val="{{ false }}">
          <section class="sb-card rl-edit" aria-labelledby="ch-h">
            <div style="display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap;"><h2 id="ch-h" class="sb-h2">A regulator changed something</h2><button class="sb-btn b-gh" onClick="{{closeChange}}">Close</button></div>
            <div class="rl-steps">
              <div class="rl-step"><span class="rl-k">1. Which requirement</span>
                <select class="rl-sel" value="{{chReq}}" onChange="{{onChReq}}"><sc-for list="{{reqOptions}}" as="o" hint-placeholder-count="26"><option value="{{o.id}}">{{o.name}}</option></sc-for></select>
                <span class="sb-sub">Now: {{chNow}}</span>
              </div>
              <div class="rl-step"><span class="rl-k">2. What changed</span>
                <textarea class="bz-ta" value="{{chWhat}}" onChange="{{onChWhat}}" placeholder="Describe the change in plain words"></textarea>
                <button class="sb-btn b-gh" style="align-self: flex-start;" onClick="{{useExample}}">Use the example</button>
              </div>
              <div class="rl-step"><span class="rl-k">3. Where you saw it</span>
                <input class="bz-in" value="{{chSrc}}" onChange="{{onChSrc}}" placeholder="Link, letter or bulletin, with its date">
                <span class="sb-sub">Needed: the new version of the requirement keeps this as its source.</span>
                <sc-if value="{{chErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Say what changed and where you saw it first.</span></sc-if>
                <button class="sb-btn b-pri" style="align-self: flex-start;" onClick="{{buildPlan}}">Build the change plan</button>
              </div>
            </div>
            <sc-if value="{{hasPlan}}" hint-placeholder-val="{{ false }}">
              <div style="display: flex; flex-direction: column;">
                <div style="display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; padding-bottom: 8px;"><span class="bz-b">{{planTitle}}</span><span class="sb-sub">{{planSub}}</span></div>
                <div class="rq-plan" style="border-top: 0;"><span class="sb-th">Where</span><span class="sb-th">What changes</span><span class="sb-th">Who, and approval</span></div>
                <sc-for list="{{plan}}" as="p" hint-placeholder-count="6"><div class="rq-plan"><span class="bz-b">{{p.where}}</span><span>{{p.what}}</span><span class="sb-sub">{{p.who}}</span></div></sc-for>
                <div class="{{planBoxCls}}" style="margin-top: 10px;" role="status"><span class="bz-b">{{planBoxTitle}}</span><span class="sb-sub">{{planBoxText}}</span>
                  <sc-if value="{{canSendPlan}}" hint-placeholder-val="{{ true }}"><button class="sb-btn b-pri" style="align-self: flex-start;" onClick="{{sendPlan}}">Send the plan to the owners</button></sc-if>
                </div>
              </div>
            </sc-if>
          </section>
        </sc-if>

        <sc-for list="{{reqGroups}}" as="g" hint-placeholder-count="5">
          <section class="sb-card">
            <div class="sb-head"><h2 class="sb-h2">{{g.label}}</h2><span class="sb-sub">{{g.n}}</span></div>
            <sc-for list="{{g.items}}" as="q" hint-placeholder-count="4">
              <div class="rq-row">
                <div style="display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; align-items: baseline;">
                  <div class="rl-chips"><span class="rl-name">{{q.name}}</span><sc-for list="{{q.regs}}" as="x" hint-placeholder-count="3"><span class="sb-chip c-info">{{x.t}}</span></sc-for><span class="{{q.lockCls}}">{{q.lockT}}</span><sc-if value="{{q.inPlan}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-warn">Change plan sent</span></sc-if></div>
                  <span class="sb-sub">{{q.clients}}</span>
                </div>
                <span class="rl-val">{{q.value}}</span>
                <span class="rl-meta">{{q.source}}</span>
                <div class="rq-deps">
                  <sc-for list="{{q.deps}}" as="d" hint-placeholder-count="5"><div class="rq-dep"><span class="rl-k">{{d.k}}</span><sc-for list="{{d.items}}" as="i" hint-placeholder-count="2"><span class="i">{{i.t}}</span></sc-for></div></sc-for>
                </div>
              </div>
            </sc-for>
          </section>
        </sc-for>
      </div>
      </sc-if>
'''

SCRIPT = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    const D = __DATA__;
    const K = ['Client screen', 'Staff screen', 'Email', 'Automation', 'Report'];
    this.AREAS = D.areas;
    this.R = D.rows.map(x => ({ id: x[0], area: D.areas[x[1]], name: x[2], why: x[3], value: x[4], unit: D.tabs.unit[x[5]], legal: !!x[6], source: D.tabs.source[x[7]], locked: !!x[8],
      owner: D.tabs.owner[x[9]], approval: D.tabs.approval[x[10]], effective: D.tabs.effective[x[11]], used: x[12].map(u => ({ k: u[0], kind: K[u[0]], ref: u[1], says: u[2] })),
      vers: x[13].map(v => ({ v: v[0], date: v[1], value: v[2], by: D.tabs.by[v[3]], status: v[4], ef: D.tabs.vef[v[5]] })), clientsNow: x[14], clientsLabel: D.tabs.cl[x[15]],
      changed: !!x[16], waiting: x[17] ? { value: x[17][0], by: x[17][1], on: x[17][2], who: x[17][3], where: x[17][4], file: x[17][5] } : null, key: x[18], note: x[19] }));
    this.REQ = __REQ__;
    let trial = {};
    try { trial = (window.CSR && window.CSR.trial) || {}; } catch (e) { trial = {}; }
    const day = trial['weekly-update-day'] || 'Friday', reply = trial['reply-client'] || '1 working day';
    this.state = { tab: 'rules', area: 'Promises and timings', q: '', f: 'all', open: {}, edit: '', ev: '', er: '', eff: 'date', edate: 'Mon 16 Nov 2026', eErr: '', changes: {}, decNote: '', decErr: false,
      tryDay: day, tryReply: reply, trialOn: !!(trial['weekly-update-day'] || trial['reply-client']),
      chOpen: false, chReq: 'address-history-length', chWhat: '', chSrc: '', chErr: false, plan: false, planSent: {} };
  }
  csrGet(id, fb) { try { return window.CSR ? window.CSR.get(id, fb) : fb; } catch (e) { return fb; } }
  rhythm(day) {
    if (day === 'Wednesday') return 'Monday review and chase, Tuesday second-person check, Wednesday send';
    if (day === 'Thursday') return 'Monday review, Tuesday chase, Wednesday second-person check, Thursday send';
    return 'Monday review, Wednesday chase, Thursday second-person check, Friday send';
  }
  renderVals() {
    const s = this.state, R = this.R, A = this.AREAS;
    const ch = s.changes;
    const isWaiting = r => (r.waiting && !ch[r.id]) || (ch[r.id] && ch[r.id].status === 'waiting');
    const isChanged = r => r.changed || (ch[r.id] && ch[r.id].status === 'live');
    const q = s.q.trim().toLowerCase();
    const match = r => {
      if (s.f === 'locked' && !r.locked) return false;
      if (s.f === 'changed' && !isChanged(r)) return false;
      if (s.f === 'waiting' && !isWaiting(r)) return false;
      if (!q) return true;
      return (r.name + ' ' + r.value + ' ' + r.why + ' ' + r.id + ' ' + r.used.map(u => u.ref).join(' ')).toLowerCase().indexOf(q) >= 0;
    };
    const M = R.filter(match);
    let area = s.area;
    if (area !== 'all' && (q || s.f !== 'all') && !M.some(r => r.area === area)) area = 'all';
    const shown = M.filter(r => area === 'all' || r.area === area);
    const cnt = (list, k) => list.filter(u => u.k === k).length;
    const plural = (n, a, b) => n + ' ' + (n === 1 ? a : b);
    const usedSum = r => {
      const c = cnt(r.used, 0), st = cnt(r.used, 1) + cnt(r.used, 4), e = cnt(r.used, 2), a = cnt(r.used, 3);
      const parts = [];
      if (c) parts.push(plural(c, 'client screen', 'client screens'));
      if (st) parts.push(plural(st, 'staff screen', 'staff screens'));
      if (e) parts.push(plural(e, 'email', 'emails'));
      if (a) parts.push(plural(a, 'automation', 'automations'));
      return parts.length ? parts.join(', ') : 'Followed in the background';
    };
    const approverOf = r => r.approval === 'manager' ? 'Rachel Turner (manager)' : 'Rachel Turner';
    const KC = ['sb-chip c-brand', 'sb-chip c-info', 'sb-chip c-ok', 'sb-chip c-neutral', 'sb-chip c-warn'];
    const rows = shown.map(r => {
      const c = ch[r.id];
      const chips = [];
      if (r.locked) chips.push({ t: r.legal ? 'Locked by law or a regulator' : 'Locked by us', cls: 'sb-chip c-neutral' });
      if (isWaiting(r)) chips.push({ t: 'Waiting for approval', cls: 'sb-chip c-warn' });
      if (c && c.status === 'live') chips.push({ t: 'v' + c.v + ' from ' + c.date, cls: 'sb-chip c-ok' });
      else if (r.changed) { const lv = r.vers[r.vers.length - 1]; chips.push({ t: 'v' + lv.v + ', changed ' + lv.date.replace(' 2026', ''), cls: 'sb-chip c-info' }); }
      if (area === 'all') chips.push({ t: r.area, cls: 'sb-chip c-neutral' });
      const val = c && c.status === 'live' ? c.value : r.value;
      const vers = r.vers.map(v => ({ v: String(v.v), date: v.date, value: v.value, by: v.by, ef: 'Applies to ' + v.ef, st: v.status === 'live' ? 'Live' : (v.status === 'waiting' ? 'Waiting for approval' : 'Replaced') }));
      if (c) vers.push({ v: String(c.v), date: 'Just now', value: c.value, by: 'Requested by Collins' + (c.status === 'live' ? (c.approvedBy ? ', approved by ' + c.approvedBy : ', published by Collins') : (c.status === 'declined' ? ', declined by ' + c.approvedBy : ', waiting for ' + approverOf(r))), ef: 'Applies to ' + (c.eff === 'new' ? 'new clients from ' : 'everyone from ') + c.date, st: c.status === 'live' ? 'Live from ' + c.date : (c.status === 'declined' ? 'Declined' : 'Waiting for approval') });
      const editing = s.edit === r.id;
      const busy = !!(isWaiting(r));
      const nC = cnt(r.used, 0), nS = cnt(r.used, 1) + cnt(r.used, 4), nE = cnt(r.used, 2), nA = cnt(r.used, 3);
      const emails = r.used.filter(u => u.k === 2).map(u => u.ref.replace('email ', ''));
      const autos = r.used.filter(u => u.k === 3).map(u => u.ref.replace('automation: ', ''));
      const screens = r.used.filter(u => u.k === 0 || u.k === 1 || u.k === 4).map(u => u.ref.replace('board ', ''));
      const list = (xs, n) => xs.slice(0, n).join('; ') + (xs.length > n ? '; and ' + (xs.length - n) + ' more' : '');
      const impactLines = [];
      if (screens.length) impactLines.push({ t: 'Screens: ' + list(screens, 8) + '.' });
      if (emails.length) impactLines.push({ t: 'Emails get a new version (Messages and automations, board 82): ' + list(emails, 6) + '. Emails already sent are not changed.' });
      if (autos.length) impactLines.push({ t: 'Automations: ' + list(autos, 6) + '.' });
      impactLines.push({ t: s.eff === 'new' ? 'Clients already signed keep v' + r.vers[r.vers.length - 1].v + '. New clients from ' + s.edate + ' get the new value.' : 'From ' + s.edate + ', every screen, email and automation above reads the new value. Today that is ' + r.clientsNow + ' ' + (r.clientsNow === 1 ? 'client' : 'clients') + ' (' + r.clientsLabel + ').' });
      if (r.key) impactLines.push({ t: 'Boards read it from one registry key ("' + r.key + '"), so they all change together.' });
      if (r.id === 'client-question-reply-time') impactLines.push({ t: 'The complaint acknowledgement (1 working day) is a separate locked rule and does not change. Reports measure each reply against the promise in force at the time.' });
      if (r.id === 'weekly-update-day') impactLines.push({ t: 'The team rhythm moves with it (a manager setting): review, chase and second-person check stay the same number of days before the send.' });
      const sendLabel = r.approval === 'other super admin' ? 'Send to Rachel Turner for approval' : (r.approval === 'manager' ? 'Send to a manager for approval' : 'Publish the change');
      const approvalText = r.approval === 'other super admin' ? 'This rule needs the other super admin. Rachel Turner approves or declines, with a note. You cannot approve your own change.' :
        (r.approval === 'manager' ? 'A manager setting: Rachel Turner, as a manager, approves it.' : 'A super admin can publish this alone. Rachel Turner is told, and the decision is recorded in the audit log.');
      let decTitle = '', decText = '', decCls = 'bz-amb', canDecide = false;
      if (c) {
        if (c.status === 'waiting') { decTitle = 'Waiting for ' + approverOf(r) + ': ' + c.value; decText = 'Requested by Collins just now. Applies to ' + (c.eff === 'new' ? 'new clients from ' : 'everyone from ') + c.date + '. Reason: "' + c.reason + '". Nothing changes until it is approved.'; canDecide = true; }
        else if (c.status === 'live') { decCls = 'bz-ok'; decTitle = 'Decision recorded: v' + c.v + ' approved'; decText = (c.approvedBy ? 'Approved by ' + c.approvedBy + ': "' + c.note + '". ' : 'Published by Collins. Rachel Turner was told. ') + 'Applies to ' + (c.eff === 'new' ? 'new clients from ' : 'everyone from ') + c.date + '. Requested by Collins: "' + c.reason + '". Written to the audit log.'; }
        else { decCls = 'bz-info'; decTitle = 'Declined by ' + c.approvedBy; decText = 'Note: "' + c.note + '". The rule stays as it is. Written to the audit log.'; }
      }
      const decide = ok => () => {
        if (!s.decNote.trim()) { this.setState({ decErr: true }); return; }
        this.setState({ decErr: false, decNote: '', changes: Object.assign({}, ch, { [r.id]: Object.assign({}, c, { status: ok ? 'live' : 'declined', approvedBy: approverOf(r), note: s.decNote.trim() }) }) });
      };
      return {
        name: r.name, value: val, chips,
        meta: (r.locked ? 'Owner: ' + r.owner : 'Owner: ' + r.owner + '. Approval: ' + (r.approval === 'super admin' ? 'a super admin' : (r.approval === 'manager' ? 'a manager' : 'the other super admin')) + '. Applies to ' + r.effective + '.'),
        usedSum: usedSum(r), clients: r.clientsNow + ': ' + r.clientsLabel,
        expanded: !!s.open[r.id], toggleLabel: s.open[r.id] ? 'Hide details' : 'Used in and history', toggle: () => this.setState({ open: Object.assign({}, s.open, { [r.id]: !s.open[r.id] }) }),
        canEdit: !r.locked && !busy && !editing, isLocked: r.locked, lockLabel: r.legal ? 'Locked by law' : 'Locked by us', isBusy: busy && !r.locked, busyLabel: 'Waiting for approval',
        lockTitle: r.legal ? 'Fixed by law or a regulator. Shown, not edited.' : 'Locked by Care Sync. It cannot be switched off.', source: 'Source: ' + r.source,
        edit: () => this.setState({ edit: r.id, ev: val, er: '', eff: r.effective === 'new clients only' ? 'new' : 'date', edate: 'Mon 16 Nov 2026', eErr: '' }),
        isEditing: editing, routeNote: 'Draft. Nothing changes until it is ' + (r.approval === 'super admin' ? 'published' : 'approved') + '.',
        approvalText, sendLabel,
        impact: [[nC, 'client screens'], [nS, 'staff screens and reports'], [nE, 'emails'], [nA, 'automations'], [r.clientsNow, 'clients affected now']].map(([n, k]) => ({ n: String(n), k })),
        impactLines,
        hasDecision: !!c, decTitle, decText, decCls, canDecide, approver: approverOf(r), approveLabel: 'Approve as ' + approverOf(r), approve: decide(true), decline: decide(false),
        why: r.why, note: r.note, used: r.used.map(u => ({ kind: u.kind, cls: KC[u.k], ref: u.ref, says: u.says ? '"' + u.says + '"' : '' })), noUsed: !r.used.length, vers,
        unitText: 'Unit: ' + r.unit + '.' + (r.key ? ' Registry key: ' + r.key + ' (read by boards with CSR.get).' : '') + ' Rule id: ' + r.id + '.'
      };
    });
    const sendEdit = () => {
      const r = R.find(x => x.id === s.edit);
      if (!r) return;
      const cur = ch[r.id] && ch[r.id].status === 'live' ? ch[r.id].value : r.value;
      if (!s.ev.trim() || s.ev.trim() === cur) { this.setState({ eErr: 'Write the new value first. It must differ from the current one.' }); return; }
      if (!s.er.trim()) { this.setState({ eErr: 'Write why first. The approver and the audit log need the reason.' }); return; }
      if (!s.edate.trim()) { this.setState({ eErr: 'Choose the date it applies from.' }); return; }
      const v = r.vers[r.vers.length - 1].v + 1;
      const live = r.approval === 'super admin';
      this.setState({ edit: '', eErr: '', decNote: '', decErr: false, changes: Object.assign({}, ch, { [r.id]: { v, value: s.ev.trim(), reason: s.er.trim(), eff: s.eff, date: s.edate.trim(), status: live ? 'live' : 'waiting' } }) });
    };
    const nLocked = R.filter(r => r.locked).length, nLegal = R.filter(r => r.locked && r.legal).length;
    const nChanged = R.filter(isChanged).length, nWait = R.filter(isWaiting).length;
    const F = [['all', 'All'], ['locked', 'Locked by law or by us'], ['changed', 'Changed this month'], ['waiting', 'Waiting for approval']];
    const areaList = [{ k: 'all', label: 'All areas', n: M.length }].concat(A.map(a => ({ k: a, label: a, n: M.filter(r => r.area === a).length }))).map(a => ({
      label: a.label, n: String(a.n), cls: 'rl-area' + (area === a.k ? ' on' : ''), pressed: String(area === a.k), pick: () => this.setState({ area: a.k, edit: '' }) }));
    const waitList = R.filter(r => r.waiting).map(r => ({ name: r.name, text: r.waiting.value + '. Entered by ' + r.waiting.by + ', ' + r.waiting.on + '. Waiting for ' + r.waiting.who + '.', where: 'Decide on ' + r.waiting.where, file: r.waiting.file }));
    // Try it
    const wk = R.find(r => r.id === 'weekly-update-day'), rp = R.find(r => r.id === 'client-question-reply-time');
    const trialDay = this.csrGet('weekly-update-day', 'Friday'), trialReply = this.csrGet('reply-client', '1 working day');
    const trialLines = s.trialOn ? [
      { t: 'Weekly update day: ' + trialDay + '. Team rhythm: ' + this.csrGet('weekly-rhythm', this.rhythm(trialDay)) + '.' },
      { t: 'Reply promise: ' + trialReply + '. The complaint acknowledgement stays 1 working day.' },
      { t: 'If published, this would reach ' + usedSum(wk) + ' (weekly update) and ' + usedSum(rp) + ' (reply promise).' }
    ] : [
      { t: 'Live values: weekly update on ' + wk.value.replace(', for every client', '') + ' by ' + this.csrGet('weekly-update-time', '16:00') + ', and replies within ' + rp.value + '.' },
      { t: 'The weekly update day is used in ' + usedSum(wk) + '. The reply promise is used in ' + usedSum(rp) + '.' }
    ];
    // Regulator requirements
    const RQ = this.REQ.map(([id, g, regs, forms, gates, pack, emails, screens]) => ({ id, g, regs, forms, gates, pack, emails, screens, r: R.find(x => x.id === id) }));
    const GROUPS = ['Legal deadlines', 'Evidence the regulator asks for', 'Checks and formats', 'After registration duties', 'Our targets around regulator dates'];
    const none = [{ t: 'None' }];
    const items = xs => xs.length ? xs.map(t => ({ t })) : none;
    const reqGroups = GROUPS.map(label => {
      const its = RQ.filter(x => x.g === label);
      return { label, n: plural(its.length, 'requirement', 'requirements'), items: its.map(x => ({
        name: x.r.name, value: x.r.value, regs: x.regs.map(t => ({ t })), source: x.r.locked ? 'Source: ' + x.r.source : 'Our rule, built around the regulator\'s date. Owner: ' + x.r.owner + '.',
        lockCls: x.r.locked ? 'sb-chip c-neutral' : 'sb-chip c-brand', lockT: x.r.locked ? (x.r.legal ? 'Locked by law or a regulator' : 'Locked by us') : 'Our target',
        clients: plural(x.r.clientsNow, 'client', 'clients') + ' now: ' + x.r.clientsLabel, inPlan: !!s.planSent[x.id],
        deps: [['Forms', x.forms], ['Gates and checks', x.gates], ['Pack Doctor rules', x.pack], ['Emails', x.emails], ['Screens', x.screens]].map(([k, xs]) => ({ k, items: items(xs) })) })) };
    });
    const cur = RQ.find(x => x.id === s.chReq) || RQ[0];
    const EX = { 'address-history-length': ['Example: CIW now asks for 10 years of address history for every person named in the application.', 'Example: CIW provider bulletin, with its date'] };
    const ex = EX[s.chReq] || ['Example: ' + cur.r.name + ' changes from "' + cur.r.value + '" to a new value.', 'Example: regulator guidance page, with its date'];
    let plan = [];
    if (s.plan) {
      cur.forms.forEach(f => plan.push({ where: 'Form', what: 'Draft a new version of the ' + f.split(':')[0] + (f.indexOf(':') > 0 ? ', page "' + f.split(': ')[1] + '"' : '') + '. Clients halfway stay on their version; Grace checks each one.', who: 'Grace drafts. The other super admin approves (Forms, board 44)' }));
      cur.gates.forEach(g => plan.push({ where: /^Gate/.test(g) ? 'Onboarding gate' : 'Check', what: 'Update "' + g + '" to the new requirement.', who: 'Rachel Turner. Gates on board 8, checks on board 13' }));
      cur.pack.forEach(p => plan.push({ where: 'Pack Doctor rule', what: 'Update the rule "' + p + '" so packs are checked against the new requirement.', who: 'Daniel Mensah, checked by a second person' }));
      cur.emails.forEach(e => plan.push({ where: 'Email', what: 'New version of email ' + e + ' if its wording mentions the requirement.', who: 'Daniel drafts. Legal wording needs the other super admin (board 82)' }));
      cur.screens.forEach(sc => plan.push({ where: 'Screen', what: 'Check the wording on ' + sc + '. It reads the registry, so most text updates itself.', who: 'Rachel Turner' }));
      plan.push({ where: 'Rules and promises', what: 'New version of "' + cur.r.name + '" with the source: ' + (s.chSrc.trim() || 'as entered') + '.', who: cur.r.locked ? 'Collins enters it, Rachel Turner approves' : 'A super admin' });
      plan.push({ where: 'Clients', what: cur.r.clientsNow + ' ' + (cur.r.clientsNow === 1 ? 'client' : 'clients') + ' affected now (' + cur.r.clientsLabel + '). Their case owners are told which clients need anything new, and the client hears it in their weekly update.', who: 'Case owners' });
    }
    const sent = !!s.planSent[s.chReq];
    return {
      theme: this.props.theme ?? 'light', three: 7, n16: 16, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      mainTabs: [['rules', 'Rules (' + R.length + ')'], ['req', 'Regulator requirements (' + RQ.length + ')']].map(([k, label]) => ({ label, on: s.tab === k, off: s.tab !== k, pick: () => this.setState({ tab: k }) })),
      isRules: s.tab === 'rules', isReq: s.tab === 'req',
      kpis: [['Rules', String(R.length), 'In ' + A.length + ' areas, each defined once'], ['Locked', String(nLocked), nLegal + ' by law or a regulator, ' + (nLocked - nLegal) + ' by us'], ['Changed this month', String(nChanged), 'Mostly the 4 November decisions'], ['Waiting for approval', String(nWait), 'Linked to decisions on Home']].map(([k, v, note]) => ({ k, v, note })),
      waitList,
      tryDay: s.tryDay, tryReply: s.tryReply, onTryDay: e => this.setState({ tryDay: e.target.value }), onTryReply: e => this.setState({ tryReply: e.target.value }),
      applyTrial: () => { if (window.CSR) { window.CSR.setTrial('weekly-update-day', s.tryDay); window.CSR.setTrial('weekly-rhythm', this.rhythm(s.tryDay)); window.CSR.setTrial('reply-client', s.tryReply); } this.setState({ trialOn: true }); },
      clearTrial: () => { if (window.CSR) window.CSR.clearTrial(); this.setState({ trialOn: false, tryDay: 'Friday', tryReply: '1 working day' }); },
      trialChip: s.trialOn ? 'Trial on in this browser' : 'No trial running', trialChipCls: 'sb-chip ' + (s.trialOn ? 'c-warn' : 'c-neutral'),
      trialTitle: s.trialOn ? 'Trying: updates on ' + trialDay + ', replies within ' + trialReply : 'What the boards show now', trialLines,
      q: s.q, onQ: e => this.setState({ q: e.target.value, edit: '' }),
      filters: F.map(([k, label]) => ({ label, on: s.f === k, off: s.f !== k, pick: () => this.setState({ f: k, edit: '' }) })),
      areaList, rows, noRows: !rows.length,
      listTitle: area === 'all' ? (q ? 'Rules matching "' + s.q.trim() + '"' : 'All areas') : area, listSub: plural(rows.length, 'rule', 'rules') + (s.f !== 'all' ? ', filtered: ' + F.find(x => x[0] === s.f)[1].toLowerCase() : ''),
      ev: s.ev, er: s.er, edate: s.edate, onEv: e => this.setState({ ev: e.target.value, eErr: '' }), onEr: e => this.setState({ er: e.target.value, eErr: '' }), onDate: e => this.setState({ edate: e.target.value, eErr: '' }),
      effNewCls: 'rl-pick ' + (s.eff === 'new' ? 'p-on' : 'p-off'), effDateCls: 'rl-pick ' + (s.eff === 'date' ? 'p-on' : 'p-off'), effNewP: String(s.eff === 'new'), effDateP: String(s.eff === 'date'),
      pickNew: () => this.setState({ eff: 'new' }), pickDate: () => this.setState({ eff: 'date' }),
      dateLabel: s.eff === 'new' ? 'For clients who sign from' : 'For everyone from',
      effNote: s.eff === 'new' ? 'Clients already signed keep what they agreed.' : 'Every client moves on the date. Messages already sent stay as they were.',
      eErr: !!s.eErr, eErrText: s.eErr, sendEdit, cancelEdit: () => this.setState({ edit: '', eErr: '' }),
      decNote: s.decNote, decErr: s.decErr, onDecNote: e => this.setState({ decNote: e.target.value, decErr: false }),
      reqGroups, chOpen: s.chOpen, openChange: () => this.setState({ chOpen: true }), closeChange: () => this.setState({ chOpen: false }),
      reqOptions: RQ.map(x => ({ id: x.id, name: x.r.name })), chReq: s.chReq, onChReq: e => this.setState({ chReq: e.target.value, plan: false, chErr: false }),
      chNow: cur.r.value, chWhat: s.chWhat, chSrc: s.chSrc, onChWhat: e => this.setState({ chWhat: e.target.value, chErr: false }), onChSrc: e => this.setState({ chSrc: e.target.value, chErr: false }),
      useExample: () => this.setState({ chWhat: ex[0], chSrc: ex[1], chErr: false }), chErr: s.chErr,
      buildPlan: () => { if (!s.chWhat.trim() || !s.chSrc.trim()) { this.setState({ chErr: true }); return; } this.setState({ plan: true, chErr: false }); },
      hasPlan: s.plan, plan, planTitle: 'Change plan: ' + cur.r.name, planSub: plural(plan.length, 'step', 'steps') + ' across forms, gates, checks, Pack Doctor, emails and screens',
      planBoxCls: sent ? 'bz-ok' : 'bz-amb', planBoxTitle: sent ? 'Plan sent to the owners' : 'Nothing changes until each owner acts',
      planBoxText: sent ? 'Each owner has a task with this plan. The requirement shows "Change plan sent" until every step is done, and forms and emails still go through their own approval. Written to the audit log.' : 'What changed: ' + (s.chWhat.trim() || 'not written yet') + '. Sending creates a task for each owner, with the source attached.',
      canSendPlan: !sent, sendPlan: () => this.setState({ planSent: Object.assign({}, s.planSent, { [s.chReq]: true }) })
    };
  }
}'''
SCRIPT = SCRIPT.replace('__DATA__', DATA).replace('__REQ__', REQD)
H = int(sys.argv[2]) if len(sys.argv) > 2 else 2900
build_sa(OUT + '/Rules.dc.html', 'Rules and promises', 'Rules and promises', H, BODY, SCRIPT, 'rules', CSS)
print('written', len(SCRIPT))
