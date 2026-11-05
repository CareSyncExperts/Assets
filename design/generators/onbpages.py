# Onboarding boards for Grace (onboarding lead): queue, gates, form checks, questions,
# address check and handover. Run from SP/gen:  python3 onbpages.py ../hub-canvas/project
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from staffboard import build
OUT = sys.argv[1] if len(sys.argv) > 1 else '../hub-canvas/project'

CSS = '''.ob-in{min-height:36px;padding:0 10px;border-radius:8px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:13px;box-sizing:border-box;width:100%}
.ob-ta{width:100%;box-sizing:border-box;min-height:60px;padding:8px 10px;border-radius:8px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:13px;line-height:18px;resize:vertical}
.ob-pick{min-height:36px;padding:0 12px;border-radius:999px;font:inherit;font-size:13px;cursor:pointer}
.p-on{border:2px solid var(--cs-action-primary);background:var(--cs-selection-bg);color:var(--cs-text-primary);font-weight:500}
.p-off{border:1px solid var(--cs-border-default);background:var(--cs-surface-raised);color:var(--cs-text-primary)}
.ob-pick:focus-visible,.ob-in:focus-visible,.ob-ta:focus-visible,.ob-link:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:2px}
.g-row{padding:12px 20px;border-top:1px solid var(--cs-border-subtle);display:flex;flex-direction:column;gap:8px;font-size:14px;line-height:20px}
.g-fail{box-shadow:inset 4px 0 0 var(--cs-status-error-border)}
.g-wait{box-shadow:inset 4px 0 0 var(--cs-status-warning-border)}
.g-pass{box-shadow:none}
.g-num{width:26px;height:26px;flex-shrink:0;border-radius:8px;background:var(--cs-surface-brand);color:var(--cs-text-brand);display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:600}
.g-panel{margin-left:40px;padding:12px;border-radius:10px;background:var(--cs-surface-page);border:1px solid var(--cs-border-subtle);display:flex;flex-direction:column;gap:8px}
.ob-box{padding:12px 14px;border-radius:10px;background:var(--cs-surface-page);border:1px solid var(--cs-border-subtle);display:flex;flex-direction:column;gap:6px}
.ob-ok{padding:10px 12px;border-radius:10px;background:var(--cs-status-success-bg);color:var(--cs-status-success-text);font-size:13px;line-height:18px}
.ob-warn{padding:10px 12px;border-radius:10px;background:var(--cs-status-warning-bg);color:var(--cs-status-warning-text);font-size:13px;line-height:18px}
.ob-lock{padding:10px 12px;border-radius:10px;background:var(--cs-surface-subtle);color:var(--cs-text-primary);font-size:13px;line-height:18px;display:flex;gap:8px;align-items:flex-start}
.ob-flex{display:flex;gap:8px;align-items:flex-start}
.ob-k{font-size:12px;line-height:16px;color:var(--cs-text-muted)}
.ob-v{font-size:14px;line-height:20px}
.ob-step{display:flex;flex-direction:column;gap:2px;padding:8px 10px;border-radius:8px;flex:1 1 0;min-width:0}
.s-done{background:var(--cs-status-success-bg);color:var(--cs-status-success-text)}
.s-todo{background:var(--cs-surface-subtle);color:var(--cs-text-secondary)}
.ob-log{display:flex;gap:10px;padding:8px 0;border-top:1px solid var(--cs-border-subtle);font-size:13px;line-height:18px}
.ob-link{color:var(--cs-text-brand);font-weight:500;text-decoration:none;font-size:13px}
.ob-sheetk{font-size:12px;line-height:16px;color:var(--cs-text-muted)}
.ob-grp{width:100%;min-height:40px;padding:8px 0;border:0;border-top:1px solid var(--cs-border-subtle);background:transparent;color:var(--cs-text-primary);font:inherit;font-size:14px;font-weight:500;text-align:left;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:8px}
.ob-grp:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:-2px}
'''

def H1(title, sub_binding):
    return '''        <div style="display: flex; flex-direction: column; gap: 4px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">''' + title + '''</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">''' + sub_binding + '''</span>
        </div>
'''

def PICKS(lst, var):
    return '<sc-for list="{{' + lst + '}}" as="' + var + '" hint-placeholder-count="4"><button class="{{' + var + '.cls}}" aria-pressed="{{' + var + '.pressed}}" onClick="{{' + var + '.pick}}">{{' + var + '.label}}</button></sc-for>'

# Gate rows, shared by Onboarding (wide) and FormStaff (stacked).
def GATE_ROWS(wide):
    btns = '''<span style="display: flex; gap: 6px; flex-wrap: wrap; flex-shrink: 0;">
                <button class="sb-btn b-gh" onClick="{{g.accept}}">Accept</button>
                <button class="sb-btn b-gh" onClick="{{g.failOpen}}" aria-expanded="{{g.failExp}}">Fail with a reason</button>
                <button class="sb-btn b-gh" onClick="{{g.assignOpen}}" aria-expanded="{{g.assignExp}}">Assign</button>
              </span>'''
    head = '''<span style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><span style="font-weight: 500;">{{g.name}}</span><span class="{{g.chipCls}}">{{g.chip}}</span><sc-if value="{{g.hasAssign}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-info">{{g.assignText}}</span></sc-if></span>
                <span class="sb-sub">{{g.text}}</span>
                <span class="sb-muted">{{g.decided}}</span>'''
    if wide:
        top = '''<div style="display: flex; gap: 14px; align-items: flex-start;">
              <span class="g-num">{{g.n}}</span>
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px;">
                ''' + head + '''
              </span>
              ''' + btns + '''
            </div>'''
    else:
        top = '''<div style="display: flex; gap: 12px; align-items: flex-start;">
              <span class="g-num">{{g.n}}</span>
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px;">
                ''' + head + '''
                <span style="padding-top: 4px;">''' + btns + '''</span>
              </span>
            </div>'''
    return '''          <sc-for list="{{gates}}" as="g" hint-placeholder-count="8">
          <div class="{{g.rowCls}}">
            ''' + top + '''
            <sc-if value="{{g.failing}}" hint-placeholder-val="{{ false }}">
              <div class="g-panel">
                <label class="ob-k" for="{{g.fid}}">Reason (the client sees this wording on the fix list)</label>
                <textarea class="ob-ta" id="{{g.fid}}" value="{{g.reasonVal}}" onChange="{{g.onReason}}"></textarea>
                <span class="sb-muted">{{g.failNote}}</span>
                <span style="display: flex; gap: 6px;"><button class="sb-btn b-pri" onClick="{{g.failSave}}">Save as Fail</button><button class="sb-btn b-gh" onClick="{{g.cancel}}">Cancel</button></span>
              </div>
            </sc-if>
            <sc-if value="{{g.assigning}}" hint-placeholder-val="{{ false }}">
              <div class="g-panel">
                <span class="ob-k">Who checks it</span>
                <span style="display: flex; gap: 6px; flex-wrap: wrap;">''' + PICKS('g.people', 'p') + '''</span>
                <span class="ob-k">By when</span>
                <span style="display: flex; gap: 6px; flex-wrap: wrap;">''' + PICKS('g.dates', 'd') + '''</span>
                <span style="display: flex; gap: 6px;"><button class="sb-btn b-pri" onClick="{{g.assignSave}}">{{g.assignLabel}}</button><button class="sb-btn b-gh" onClick="{{g.cancel}}">Cancel</button></span>
              </div>
            </sc-if>
          </div>
          </sc-for>
'''

# JS: turns gate data plus state into rows. Expects st.g, st.tick, this.now(), this.logSet(patch, text).
GATE_JS = r'''
  gateRows(G, key, fixes, client) {
    const st = this.state;
    const RES = { pass: ['Pass', 'sb-chip c-ok', ' g-pass'], fail: ['Fail', 'sb-chip c-bad', ' g-fail'], wait: ['Waiting', 'sb-chip c-warn', ' g-wait'] };
    const PEOPLE = ['Grace', 'Daniel', 'Divine', 'Collins'];
    const DATES = this.dates();
    const upd = (n, patch) => Object.assign({}, st.g, { [key + n]: Object.assign({}, st.g[key + n] || {}, patch) });
    return G.map(b => {
      const o = Object.assign({}, b, st.g[key + b.n] || {});
      const who = o.who || 'Daniel', when = o.when || DATES[1];
      const draft = o.draft !== undefined ? o.draft : (o.reason || o.fixText || '');
      const decided = o.res === 'wait' ? 'Waiting on ' + o.waitOn + ' since ' + o.at + '. Recheck ' + o.recheck + '. Logged' : (o.res === 'pass' ? 'Accepted by ' : 'Failed by ') + o.by + ', ' + o.at + '. Logged';
      return {
        n: String(o.n), name: o.name, text: o.text, chip: RES[o.res][0], chipCls: RES[o.res][1], rowCls: 'g-row' + RES[o.res][2],
        decided: o.rec ? o.rec + ' ' + decided : decided,
        hasAssign: !!o.assigned, assignText: o.assigned || '', fid: 'gr-' + key + o.n,
        failing: o.mode === 'fail', assigning: o.mode === 'assign', failExp: String(o.mode === 'fail'), assignExp: String(o.mode === 'assign'),
        reasonVal: draft, onReason: e => this.setState({ g: upd(o.n, { draft: e.target.value }) }),
        failNote: o.noFix ? o.noFix : 'Saving adds this to the fix list for ' + client + '. You can still edit the wording there before sending.',
        accept: () => this.logSet({ g: upd(o.n, { res: 'pass', by: 'Grace', at: this.now(), mode: null, rec: '' }), fixes: (st.fixes || []).filter(f => f.id !== key + o.n) }, 'accepted gate ' + o.n + ', ' + o.name),
        failOpen: () => this.setState({ g: upd(o.n, { mode: o.mode === 'fail' ? null : 'fail' }) }),
        assignOpen: () => this.setState({ g: upd(o.n, { mode: o.mode === 'assign' ? null : 'assign' }) }),
        cancel: () => this.setState({ g: upd(o.n, { mode: null }) }),
        failSave: () => {
          const r = draft.trim() || 'Reason to be added';
          const list = st.fixes || [];
          const has = list.some(f => f.id === key + o.n);
          const nf = o.noFix ? list : (has ? list.map(f => f.id === key + o.n ? Object.assign({}, f, { text: r }) : f) : list.concat([{ id: key + o.n, gate: 'Gate ' + o.n + ', ' + o.name, text: r }]));
          this.logSet({ g: upd(o.n, { res: 'fail', by: 'Grace', at: this.now(), reason: r, mode: null, rec: '' }), fixes: nf }, 'failed gate ' + o.n + ', ' + o.name + ': ' + r);
        },
        people: PEOPLE.map(p => ({ label: p, cls: 'ob-pick ' + (who === p ? 'p-on' : 'p-off'), pressed: String(who === p), pick: () => this.setState({ g: upd(o.n, { who: p }) }) })),
        dates: DATES.map(d => ({ label: d, cls: 'ob-pick ' + (when === d ? 'p-on' : 'p-off'), pressed: String(when === d), pick: () => this.setState({ g: upd(o.n, { when: d }) }) })),
        assignLabel: 'Assign to ' + who + ', by ' + when,
        assignSave: () => this.logSet({ g: upd(o.n, { assigned: who + ' checks it by ' + when, mode: null }) }, 'assigned gate ' + o.n + ' to ' + who + ', due ' + when)
      };
    });
  }
  logSet(patch, text) {
    const st = this.state;
    this.setState(Object.assign({ tick: st.tick + 1, log: [{ who: 'Grace', text, at: this.now() }].concat(st.log || []) }, patch));
  }
'''

# The single truth for Harbour Lane (demo-world.md). at: Onboarding uses "30 Oct", FormStaff "30/10".
def HL_GATES(d):
    def t(day, hm):
        return (day + ' Oct ' + hm) if d == 'long' else ('%s/10 %s' % (day, hm))
    s = r'''[
      { n: 1, name: 'Company and directors', res: 'fail', by: 'Grace', at: '__A1__', text: 'Companies House shows 2 directors, Amara Okafor and Kwame Okafor. The form lists 1. Name, number and registered office match.', fixText: "Please add Kwame Okafor's details as your second director. Companies House lists him, so CQC needs him on the form too." },
      { n: 2, name: 'Identity', res: 'pass', by: 'Grace', at: '__A2__', text: "Amara's 3 identity documents checked: passport, driving licence photocard and council tax bill." },
      { n: 3, name: 'Office address evidence', res: 'wait', by: 'Grace', at: '__A3__', waitOn: 'the landlord, Tom Reid,', recheck: 'Thu 5 Nov', text: 'Office: Flat 2, 14 Harbour Road (rented). Tenancy received and matches. Landlord letter link sent to Tom Reid on Fri 30 Oct.', noFix: 'Already requested from Tom Reid on Fri 30 Oct, so it is never added to the client fix list again. Saving records the result only.' },
      { n: 4, name: 'Registered manager', res: 'pass', by: 'Grace', at: '__A4__', text: 'Ruth Bennett, a different person from Amara (nominated individual). CV received.' },
      { n: 5, name: 'Employment history', res: 'fail', by: 'Grace', at: '__A5__', text: "Ruth's CV has an unexplained gap, March to November 2019. Any gap longer than 4 weeks needs a line of explanation.", fixText: "Please add one line to Ruth's CV explaining the gap from March to November 2019." },
      { n: 6, name: 'References', res: 'pass', by: 'Grace', at: '__A6__', text: "The referee is Ruth's last employer, with permission for CQC to contact them." },
      { n: 7, name: 'DBS', res: 'pass', by: 'Grace', at: '__A7__', text: 'Ruth: Enhanced DBS with adult barred list, issued 14 Feb 2026, photo uploaded 30 Oct. Amara (nominated individual) has no DBS yet: we start her application, ID done.' },
      { n: 8, name: 'Professional registers', res: 'pass', by: 'Grace', at: '__A8__', rec: 'Register check recorded: Ruth is not on a register that applies.', text: 'Checked against the registers that could apply to Ruth. Result, date and checker are kept with the record.' }
    ]'''
    if d != 'long':
        for a, b in [('Fri 30 Oct', 'Fri 30/10'), ('30 Oct', '30/10'), ('14 Feb 2026', '14/02/2026'), ('Thu 5 Nov', 'Thu 05/11')]:
            s = s.replace(a, b)
    return s.replace('__A1__', t('30', '11:05')).replace('__A2__', t('30', '10:20')).replace('__A3__', t('30', '15:12')).replace('__A4__', t('30', '11:40')).replace('__A5__', t('30', '11:45')).replace('__A6__', t('30', '12:00')).replace('__A7__', t('30', '14:10')).replace('__A8__', t('30', '14:20'))

NOW_JS = r'''
  now() { const t = 40 + (this.state.tick || 0); return '__DAY__' + (t < 60 ? '09:' + t : '10:' + String(t - 60).padStart(2, '0')); }
  dates() { return ['Tue 3 Nov', 'Wed 4 Nov', 'Thu 5 Nov', 'Fri 6 Nov']; }
'''

LOG = '''<sc-for list="{{log}}" as="l" hint-placeholder-count="6"><div class="ob-log"><span class="sb-muted" style="width: 110px; flex-shrink: 0;">{{l.at}}</span><span style="flex: 1; min-width: 0;"><span style="font-weight: 500; margin-right: 5px;">{{l.who}}</span><span>{{l.text}}</span></span></div></sc-for>'''

# ---------------------------------------------------------------- Onboarding (Harbour Lane gates)
B_ONB = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <a class="ob-link" href="OnboardingQueue.dc.html">Onboarding queue</a>
          <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
            <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Harbour Lane Care Ltd</h1>
            <span class="{{badgeCls}}">{{badge}}</span>
          </div>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Stage 1 of 11: Welcome, onboarding checks. CQC, domiciliary care, Full start-up package. Paid and introduction call Mon 19 Oct. Form sent 19 Oct, arrived Thu 29 Oct. Grace owns it until a manager approves the handover.</span>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <a class="ob-link" href="FormStaff.dc.html" style="min-height: 36px; display: inline-flex; align-items: center;">Open the form answers</a>
          <a class="ob-link" href="AddressCheck.dc.html" style="min-height: 36px; display: inline-flex; align-items: center;">Address and identity check</a>
        </div>
      </div>
      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="4"><div class="sb-card sb-kpi"><span class="sb-kv">{{k.v}}</span><span class="sb-sub">{{k.k}}</span></div></sc-for>
      </div>
      <div class="ob-lock" role="note"><span style="font-weight: 600;">Locked until a manager approves the handover:</span><span>application work (stages 2 to 6) and the 3 included sessions. Nothing starts while a gate is open.</span></div>
      <section class="sb-card" aria-labelledby="gt-h">
        <div class="sb-head"><h2 id="gt-h" class="sb-h2">Onboarding gates</h2><span class="sb-sub">The same 8 checks and results as the form check and the client's fix list. Every decision is logged with who and when.</span></div>
''' + GATE_ROWS(True) + '''        <div class="sb-row" style="align-items: flex-start;"><x-import component-from-global-scope="CareSync.Icon" name="info" size="{{n18}}"></x-import><span class="sb-sub" style="flex: 1; min-width: 0;">{{rulesNote}}</span></div>
      </section>
      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <section class="sb-card" style="flex: 1 1 520px; min-width: 0; padding: 18px 20px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="fx-h">
          <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px; flex-wrap: wrap;"><h2 id="fx-h" class="sb-h2">Fix list for Amara</h2><span class="sb-sub">Made from the failed gates. Edit the wording before you send.</span></div>
          <sc-for list="{{fixes}}" as="f" hint-placeholder-count="2">
            <div class="ob-box">
              <span style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="ob-k">{{f.no}}. {{f.gate}}</span><sc-if value="{{f.manual}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" onClick="{{f.remove}}">Remove</button></sc-if></span>
              <textarea class="ob-ta" aria-label="{{f.aria}}" value="{{f.text}}" onChange="{{f.edit}}"></textarea>
            </div>
          </sc-for>
          <div style="display: flex; gap: 8px; align-items: center;">
            <input class="ob-in" aria-label="Add a manual item" placeholder="Add a manual item, for example: a clearer photo of page 2" value="{{newText}}" onChange="{{onNew}}">
            <button class="sb-btn b-sec" onClick="{{addNew}}">Add item</button>
          </div>
          <div style="display: flex; flex-direction: column; gap: 6px;">
            <span class="ob-k">Due date for the client</span>
            <span style="display: flex; gap: 6px; flex-wrap: wrap;">''' + PICKS('dues', 'd') + '''</span>
          </div>
          <div class="ob-box">
            <span style="font-weight: 500; font-size: 14px;">Already requested</span>
            <span class="sb-sub">Landlord letter for Flat 2, 14 Harbour Road. Sent to Tom Reid on Fri 30 Oct. Not on Amara's list, so she is not asked twice.</span>
            <div style="display: flex; gap: 6px;">
              <sc-for list="{{track}}" as="t" hint-placeholder-count="4"><span class="{{t.cls}}"><span style="font-size: 12px; font-weight: 500;">{{t.k}}</span><span style="font-size: 12px;">{{t.v}}</span></span></sc-for>
            </div>
            <span style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><button class="sb-btn b-gh" onClick="{{nudge}}">{{nudgeLabel}}</button><span class="sb-muted">Landlord reminders go after 3 working days, then weekly: Tom's goes automatically on Wed 4 Nov. Recheck Thu 5 Nov.</span></span>
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
            <button class="sb-btn b-pri" onClick="{{send}}">{{sendLabel}}</button>
            <button class="sb-btn b-gh" onClick="{{togglePreview}}" aria-expanded="{{previewExp}}">{{previewLabel}}</button>
          </div>
          <sc-if value="{{sent}}" hint-placeholder-val="{{ false }}"><div class="ob-ok" role="status">{{sentText}}</div></sc-if>
          <sc-if value="{{preview}}" hint-placeholder-val="{{ false }}">
            <div style="align-self: center; width: 340px; max-width: 100%; border-radius: 20px; border: 1px solid var(--cs-border-default); background: var(--cs-surface-page); padding: 16px; display: flex; flex-direction: column; gap: 10px;">
              <span class="ob-k">Preview: what Amara sees on her phone</span>
              <span style="font-size: 13px; color: var(--cs-status-warning-text); font-weight: 500;">Nearly there</span>
              <span style="font-size: 20px; line-height: 28px; font-weight: 600;">{{pvTitle}}</span>
              <sc-for list="{{fixes}}" as="f" hint-placeholder-count="2"><div style="padding: 10px 12px; border-radius: 10px; background: var(--cs-surface-raised); box-shadow: var(--cs-elevation-1); font-size: 14px; line-height: 20px;">{{f.text}}</div></sc-for>
              <span style="font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">Still being checked: your landlord's letter. We asked Tom Reid on Fri 30 Oct. Nothing for you to do.</span>
              <span style="font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">{{pvDue}}</span>
            </div>
          </sc-if>
        </section>
        <section class="sb-card" style="flex: 1 1 460px; min-width: 0; padding: 18px 20px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="ho-h">
          <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px; flex-wrap: wrap;"><h2 id="ho-h" class="sb-h2">Handover to the case owner</h2><span class="{{hoCls}}">{{hoChip}}</span></div>
          <span class="ob-k">Proposed case owner (the manager confirms)</span>
          <span style="display: flex; gap: 6px; flex-wrap: wrap;">''' + PICKS('owners', 'o') + '''</span>
          <span class="sb-sub">{{ownerLoad}}</span>
          <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px;">
            <span style="display: flex; flex-direction: column;"><span class="ob-k">Weekly update owner</span><span class="ob-v">{{weekly}}</span></span>
            <span style="display: flex; flex-direction: column;"><span class="ob-k">Approves</span><span class="ob-v">Collins, director</span></span>
          </div>
          <div class="ob-box">
            <span style="font-weight: 500; font-size: 14px;">Handover summary for the consultant</span>
            <span class="ob-k">Key answers</span>
            <span class="sb-sub">Amara Okafor: director and nominated individual. Kwame Okafor: second director (details to add). Ruth Bennett: proposed registered manager. Personal care, domiciliary care for adults 65+, dementia and physical disability. Office: Flat 2, 14 Harbour Road, rented.</span>
            <span class="ob-k">Introduction call notes (Divine, Mon 19 Oct)</span>
            <span class="sb-sub">Wants to start supporting people in the spring. A little nervous about the CQC interview. Asked about WhatsApp: it comes later, so email and the Hub for now. Landlord is friendly.</span>
            <span class="ob-k">Open risks</span>
            <span class="sb-sub">{{risks}}</span>
          </div>
          <button class="sb-btn b-pri" style="align-self: flex-start;" onClick="{{request}}">{{requestLabel}}</button>
          <sc-if value="{{requested}}" hint-placeholder-val="{{ false }}"><div class="ob-warn" role="status">{{requestText}}</div></sc-if>
          <span class="sb-muted">When Collins approves: the case owner and weekly update owner are set, Amara is told who her consultant is, stage 2 opens and the kick-off session can be booked. Not before.</span>
        </section>
      </div>
      <section class="sb-card" style="padding: 18px 20px 10px;" aria-labelledby="hi-h">
        <h2 id="hi-h" class="sb-h2" style="margin-bottom: 8px;">History</h2>
        ''' + LOG + '''
      </section>
'''

S_ONB = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { tick: 0, g: {}, log: [], fixes: [
      { id: 'hl1', gate: 'Gate 1, Company and directors', text: "Please add Kwame Okafor's details as your second director. Companies House lists him, so CQC needs him on the form too." },
      { id: 'hl5', gate: 'Gate 5, Employment history', text: "Please add one line to Ruth's CV explaining the gap from March to November 2019." }
    ], due: 'Thu 5 Nov', newText: '', preview: false, sent: false, sentText: '', nudged: '', owner: 'daniel', requested: false, reqAt: '' };
  }
''' + NOW_JS.replace('__DAY__', 'Mon 2 Nov ') + GATE_JS + r'''
  renderVals() {
    const st = this.state;
    const G = ''' + HL_GATES('long') + r''';
    const gates = this.gateRows(G, 'hl', st.fixes, 'Amara');
    const res = G.map(b => (st.g['hl' + b.n] || {}).res || b.res);
    const nPass = res.filter(r => r === 'pass').length, nWait = res.filter(r => r === 'wait').length, nFail = res.filter(r => r === 'fail').length;
    const open = 8 - nPass;
    const n = st.fixes.length;
    const fixes = st.fixes.map((f, i) => ({ no: String(i + 1), gate: f.gate, text: f.text, manual: !!f.manual, aria: 'Fix list item ' + (i + 1),
      edit: e => { const a = st.fixes.slice(); a[i] = Object.assign({}, f, { text: e.target.value }); this.setState({ fixes: a }); },
      remove: () => this.logSet({ fixes: st.fixes.filter((x, j) => j !== i) }, 'removed a manual item from the fix list') }));
    const O = [['daniel', 'Daniel', 'Daniel: 6 active, covering 4 this week for Olu. Harbour Lane would be his 7th own client.'], ['olu', 'Olu', 'Olu: on leave Mon 2 to Fri 6 November. 4 active clients, covered by Daniel this week.'], ['sam', 'Sam Patel', 'Sam Patel: leaving Friday 6 November, so not taking new clients.']];
    const ow = O.find(x => x[0] === st.owner);
    const risks = [nWait ? 'Landlord letter still with Tom Reid (gate 3).' : '', nFail ? nFail + (nFail === 1 ? ' fix' : ' fixes') + ' open with the client.' : '', 'Amara has no DBS yet: we start her application, ID done.'].filter(Boolean).join(' ');
    const GR = (id, fb) => (window.CSR ? window.CSR.get(id, fb) : fb);
    const rulesNote = 'Rules from Rules and promises (board 80): any gap longer than ' + GR('cv-gap-weeks', 4) + ' weeks on a CV needs a line of explanation. Documents that expire (DBS, insurance, right to work) get a warning ' + GR('expiry-warning-weeks', 6) + ' weeks before. Form reminders ' + GR('form-reminders', 'after 2 days and 4 days; Grace calls on day 6; then weekly') + '. Landlord and referee reminders ' + GR('third-party-reminders', 'after 3 working days, then weekly') + '. Documents: reminders ' + GR('document-reminders', 'after 3 days, then weekly') + '.';
    return {
      theme: this.props.theme ?? 'light', three: 3, n18: 18, user: { name: 'Grace Whitfield', initials: 'GW' }, nav: __NAV__, rulesNote,
      gates, badge: nPass + ' of 8 passed', badgeCls: 'sb-chip ' + (open ? 'c-warn' : 'c-ok'),
      kpis: [[nPass + ' of 8', 'gates passed'], [String(nWait), 'waiting on the landlord'], [String(nFail), 'to fix by the client'], ['14', 'days in onboarding, since Mon 19 Oct']].map(([v, k]) => ({ v, k })),
      fixes, newText: st.newText, onNew: e => this.setState({ newText: e.target.value }),
      addNew: () => { const t = st.newText.trim(); if (!t) return; this.logSet({ fixes: st.fixes.concat([{ id: 'm' + st.tick, gate: 'Added by Grace', text: t, manual: true }]), newText: '' }, 'added a manual item to the fix list'); },
      dues: ['Thu 5 Nov', 'Fri 6 Nov', 'Mon 9 Nov'].map(d => ({ label: d, cls: 'ob-pick ' + (st.due === d ? 'p-on' : 'p-off'), pressed: String(st.due === d), pick: () => this.setState({ due: d }) })),
      track: [['Sent', 'Fri 30 Oct 15:12', true], ['Opened', 'Sat 31 Oct 09:14', true], ['Uploaded', 'Not yet', false], ['Accepted', 'Not yet', false]].map(([k, v, d]) => ({ k, v, cls: 'ob-step ' + (d ? 's-done' : 's-todo') })),
      nudge: () => { if (st.nudged) return; this.logSet({ nudged: this.now() }, 'nudged Tom Reid about the landlord letter'); },
      nudgeLabel: st.nudged ? 'Nudge sent to Tom, ' + st.nudged : 'Nudge Tom',
      sendLabel: (st.sent ? 'Send again (' : 'Send fix list (') + n + ')',
      send: () => { if (!n) return; this.logSet({ sent: true, sentText: 'Sent to Amara, ' + this.now() + '. ' + n + (n === 1 ? ' item' : ' items') + ', due ' + st.due + '. She sees it on her Today page and by email.' }, 'sent the fix list (' + n + ') to Amara, due ' + st.due); },
      sent: st.sent, sentText: st.sentText,
      preview: st.preview, previewExp: String(st.preview), previewLabel: st.preview ? 'Hide the preview' : 'Preview as the client',
      togglePreview: () => this.setState({ preview: !st.preview }),
      pvTitle: n + (n === 1 ? ' small thing to fix' : ' small things to fix'), pvDue: 'Please reply by ' + st.due + '. Not sure? Tap Ask and Grace will help.',
      owners: O.map(([k, label]) => ({ label, cls: 'ob-pick ' + (st.owner === k ? 'p-on' : 'p-off'), pressed: String(st.owner === k), pick: () => this.setState({ owner: k }) })),
      ownerLoad: ow[2], weekly: 'Grace until handover, then ' + ow[1],
      hoChip: st.requested ? 'Waiting for Collins' : 'Not requested yet', hoCls: 'sb-chip ' + (st.requested ? 'c-warn' : 'c-neutral'),
      risks, requested: st.requested,
      requestLabel: st.requested ? 'Approval requested' : 'Request manager approval',
      request: () => { if (st.requested) return; this.logSet({ requested: true, reqAt: this.now() }, 'asked Collins to approve the handover to ' + ow[1]); },
      requestText: 'Sent to Collins, ' + st.reqAt + ', proposing ' + ow[1] + '. ' + (open ? 'Collins can approve only when all 8 gates pass: ' + open + ' still open. ' + ow[1] + ' can read this summary now, but does not start.' : 'All 8 gates have passed, so Collins can approve now.'),
      log: st.log.concat([
        { who: 'Tom Reid', text: 'opened the landlord letter link', at: 'Sat 31 Oct 09:14' },
        { who: 'Grace', text: 'sent the landlord letter link to Tom Reid for Flat 2, 14 Harbour Road', at: 'Fri 30 Oct 15:12' },
        { who: 'Grace', text: "recorded the register check for Ruth: not on a register that applies", at: 'Fri 30 Oct 14:20' },
        { who: 'Grace', text: "accepted Ruth's DBS: Enhanced with adult barred list, issued 14 Feb 2026", at: 'Fri 30 Oct 14:10' },
        { who: 'Grace', text: "failed gate 5: gap on Ruth's CV, March to November 2019", at: 'Fri 30 Oct 11:45' },
        { who: 'Grace', text: 'failed gate 1: Companies House shows 2 directors, the form lists 1', at: 'Fri 30 Oct 11:05' },
        { who: 'Grace', text: "accepted Amara's 3 identity documents", at: 'Fri 30 Oct 10:20' },
        { who: 'Amara', text: 'sent the onboarding form, signed electronically', at: 'Thu 29 Oct 21:46' },
        { who: 'Divine', text: 'made the introduction call. The onboarding form was sent straight after', at: 'Mon 19 Oct' }
      ])
    };
  }
}'''

build(OUT + '/Onboarding.dc.html', 'Onboarding gates', 'Onboarding', 2460, B_ONB, S_ONB, 'onboarding', CSS)

# ---------------------------------------------------------------- FormStaff (form received, CQC / CIW / RQIA)
TABS = '''      <div role="tablist" aria-label="Which form" style="display: flex; gap: 6px; flex-wrap: wrap;">
        <sc-for list="{{tabs}}" as="tb" hint-placeholder-count="3">
          <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
          <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
        </sc-for>
      </div>
'''
B_FORM = TABS + '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <span style="font-size: 14px; line-height: 20px; color: var(--cs-text-brand); font-weight: 500;">{{kicker}}</span>
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">{{client}}</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">{{sub}}</span>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
          <a class="ob-link" href="{{gatesHref}}" style="min-height: 36px; display: inline-flex; align-items: center;">{{gatesLink}}</a>
          <button class="{{fixCls}}" onClick="{{sendFix}}">{{fixLabel}}</button>
        </div>
      </div>
      <sc-if value="{{fixSent}}" hint-placeholder-val="{{ false }}"><div class="ob-ok" role="status">{{fixSentText}}</div></sc-if>
      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <div style="flex: 3 1 600px; min-width: 0; display: flex; flex-direction: column; gap: 16px;">
          <section class="sb-card" aria-labelledby="chk-h">
            <div class="sb-head">
              <span style="display: flex; flex-direction: column; gap: 2px;"><h2 id="chk-h" class="sb-h2">Checks, grouped into the 8 onboarding gates</h2><span class="sb-sub">{{chkSub}}</span></span>
              <span style="display: flex; gap: 6px; flex-wrap: wrap;"><span class="sb-chip c-ok">{{nPass}}</span><span class="sb-chip c-warn">{{nWait}}</span><span class="sb-chip c-bad">{{nFail}}</span></span>
            </div>
''' + GATE_ROWS(False) + '''          </section>
          <section class="sb-card" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="chg-h">
            <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px; flex-wrap: wrap;"><h2 id="chg-h" class="sb-h2">Changed since submission</h2><span class="sb-sub">{{chgWhen}}</span></div>
            <sc-for list="{{changes}}" as="c" hint-placeholder-count="2">
              <div style="display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr); gap: 10px; font-size: 14px; line-height: 20px; padding-top: 8px; border-top: 1px solid var(--cs-border-subtle);"><span style="font-weight: 500;">{{c.k}}</span><span style="color: var(--cs-status-error-text); text-decoration: line-through;">{{c.old}}</span><span style="color: var(--cs-status-success-text);">{{c.now}}</span></div>
            </sc-for>
            <span class="sb-sub">{{chgNote}}</span>
          </section>
        </div>
        <div style="flex: 2 1 400px; min-width: 0; display: flex; flex-direction: column; gap: 16px;">
          <section class="sb-card" aria-labelledby="dl-h">
            <div class="sb-head"><h2 id="dl-h" class="sb-h2">Download</h2><span class="sb-muted">Every download is logged</span></div>
            <sc-for list="{{downloads}}" as="d" hint-placeholder-count="4">
              <div class="sb-row"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column;"><span style="font-weight: 500;">{{d.k}}</span><span class="sb-muted">{{d.v}}</span></span><button class="sb-btn b-gh" onClick="{{d.get}}">{{d.label}}</button></div>
            </sc-for>
          </section>
          <section class="sb-card" style="padding: 18px 20px 10px; display: flex; flex-direction: column; gap: 4px;" aria-labelledby="sh-h">
            <h2 id="sh-h" class="sb-h2">{{sheetName}}</h2>
            <span class="sb-sub" style="margin-bottom: 6px;">In the same order as {{portal}}. Open a group, then copy each field. No re-typing.</span>
            <sc-for list="{{groups}}" as="gr" hint-placeholder-count="6">
              <div>
                <button class="ob-grp" aria-expanded="{{gr.exp}}" onClick="{{gr.toggle}}"><span>{{gr.name}}</span><span class="sb-muted">{{gr.count}}</span></button>
                <sc-if value="{{gr.open}}" hint-placeholder-val="{{ false }}">
                  <div style="display: flex; flex-direction: column; padding-bottom: 6px;">
                    <sc-for list="{{gr.fields}}" as="f" hint-placeholder-count="3">
                      <div style="display: flex; align-items: center; gap: 8px; padding: 4px 0 4px 10px;"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column;"><span class="ob-sheetk">{{f.k}}</span><span style="font-size: 13px; line-height: 18px;">{{f.v}}</span></span><button class="sb-btn b-gh" style="min-height: 36px; padding: 0 10px;" onClick="{{f.copy}}">{{f.label}}</button></div>
                    </sc-for>
                  </div>
                </sc-if>
              </div>
            </sc-for>
          </section>
        </div>
      </div>
'''

S_FORM = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { reg: 'cqc', tick: 0, g: {}, log: [], fixes: null, open: { cqc0: true, cqc1: true, ciw0: true, rqia0: true }, copied: '', got: '', sent: {} }; }
''' + NOW_JS.replace('__DAY__', '02/11 ') + GATE_JS + r'''
  renderVals() {
    const st = this.state, reg = st.reg;
    const CQC = ''' + HL_GATES('short') + r''';
    const CIW = [
      { n: 1, name: 'Company and officers', res: 'pass', by: 'Grace', at: '13/10 10:05', text: 'Name, number, registered office and both officers match Companies House.' },
      { n: 2, name: 'Identity', res: 'pass', by: 'Grace', at: '13/10 10:20', text: "Rhian's DBS is on the Update Service with consent to view, so no ID documents were needed." },
      { n: 3, name: 'Office address evidence', res: 'pass', by: 'Grace', at: '13/10 10:30', text: 'Office in Wales. Lease in the company name, uploaded.' },
      { n: 4, name: 'Responsible Individual', res: 'pass', by: 'Grace', at: '13/10 11:00', text: 'Rhian Example is the RI. "Why you are the right RI" answer read and passed to Daniel for the narrative.' },
      { n: 5, name: 'Manager and Social Care Wales', res: 'pass', by: 'Grace', at: '13/10 11:20', text: 'Manager registration with Social Care Wales applied for, reference given.' },
      { n: 6, name: 'References', res: 'pass', by: 'Grace', at: '13/10 11:40', text: 'Two referees for the RI. Contact details complete. CIW asks the referees itself.' },
      { n: 7, name: 'DBS', res: 'pass', by: 'Grace', at: '13/10 12:00', text: 'Full 12 digit number, on the Update Service, consent to view given.' },
      { n: 8, name: 'Areas and service details', res: 'pass', by: 'Grace', at: '13/10 12:15', text: '2 regional partnership areas, so 2 service entries. Confirmed with Daniel.' }
    ];
    const RQIA = [
      { n: 1, name: 'Company and directors', res: 'pass', by: 'Grace', at: '26/09 10:00', text: 'Name, number (Northern Ireland) and officers match Companies House.' },
      { n: 2, name: 'Identity for AccessNI', res: 'pass', by: 'Grace', at: '26/09 10:15', text: "Three ID documents each for the RI and the manager, including photo ID and proof of address, ready for RQIA's own AccessNI check." },
      { n: 3, name: 'Office address evidence', res: 'pass', by: 'Grace', at: '26/09 10:30', text: 'Office lease in the company name, uploaded.' },
      { n: 4, name: 'Responsible Individual', res: 'pass', by: 'Grace', at: '26/09 11:00', text: 'Niamh Example is the RI. Qualifications and experience given.' },
      { n: 5, name: 'Manager and NISCC', res: 'pass', by: 'Grace', at: '29/09 09:30', text: 'Manager is a different person. NISCC registration underway, reference given.' },
      { n: 6, name: 'Employment history', res: 'pass', by: 'Grace', at: '29/09 09:45', text: "7 month gap in 2021 on the manager's CV, explained by the client on 28/09." },
      { n: 7, name: 'References', res: 'pass', by: 'Grace', at: '26/09 11:30', text: 'Referee 1 is the most recent employer. Dates match the CV.' },
      { n: 8, name: 'Staffing plan', res: 'pass', by: 'Grace', at: '26/09 12:00', text: '8 staff for 20 service users. Matches the hours in the business plan.' }
    ];
    const F = (k, v) => [k, v];
    const D = {
      cqc: { label: 'CQC', G: CQC, kicker: 'CQC Registration Information Form received', client: 'Harbour Lane Care Ltd', who: 'Amara', portal: 'the CQC provider application', sheetName: 'CQC application sheet', gatesHref: 'Onboarding.dc.html', gatesLink: 'Open the onboarding gates',
        sub: 'Form arrived Thu 29/10, 21:46, from Amara Okafor, director. Saved and finished over 3 sittings. Signed electronically. Stage 1 of 11: onboarding checks.',
        chkSub: 'Ran the moment the form arrived. Grace confirms each one. The same results show on the gates board and on the client fix list.',
        chgWhen: 'Edited by the client 31/10, 08:12', changes: [['Manager mobile', '07700 900111', '07700 900222'], ['Trading name', 'None', 'Harbour Lane Home Care']], chgNote: 'Affected checks were rerun: no change to any gate. The trading name is added to the consistency check across the pack.',
        groups: [
          ['Provider details', [F('Provider name', 'Harbour Lane Care Ltd'), F('Company number', '99000101'), F('Registered office', 'Flat 2, 14 Harbour Road, Stevenage SG1 2AB'), F('Telephone', '07700 900456'), F('Email', 'amara@harbourlanecare.co.uk'), F('Directors', 'Amara Okafor; Kwame Okafor (details on the fix list)')]],
          ['Nominated individual', [F('Name', 'Amara Okafor'), F('Date of birth', '14/03/1986'), F('Role', 'Director'), F('DBS', 'Application to be started by Care Sync. ID checked 30/10')]],
          ['Registered manager', [F('Name', 'Ruth Anne Bennett'), F('Date of birth', '09/07/1979'), F('Email', 'ruth@harbourlanecare.co.uk'), F('DBS', 'Enhanced with adult barred list, issued 14/02/2026'), F('Professional register', 'None that applies (checked 30/10)')]],
          ['Locations', [F('Location name', 'Harbour Lane Care Ltd, office'), F('Address', 'Flat 2, 14 Harbour Road, Stevenage SG1 2AB'), F('Service type', 'Domiciliary care service')]],
          ['Regulated activities', [F('Activity', 'Personal care')]],
          ['Service users', [F('Bands', 'Older people (65 and over); younger adults; dementia; physical disability')]],
          ['Declarations', [F('Form declaration', 'Signed by Amara Okafor, director, 29/10/2026'), F('CQC declaration', 'Signed by the client at final pack sign-off (stage 6)')]]
        ] },
      ciw: { label: 'CIW', G: CIW, kicker: 'CIW Registration Information Form', client: 'Afon Care Ltd', who: 'Rhian', portal: 'CIW Online', sheetName: 'CIW Online sheet', gatesHref: 'Handover.dc.html', gatesLink: 'How CIW gates differ',
        sub: 'Form arrived 12/10 from Rhian Example, director. All gates passed 13/10. Submitted on CIW Online 14/10. Stage 8 of 11: with CIW.',
        chkSub: 'All 8 passed before submission. Kept for the record; a gate can still be reopened with a reason.',
        chgWhen: 'Edited by the client 28/10, 19:30', changes: [['Manager mobile', '07700 900310', '07700 900311'], ['Office telephone', '029 2018 0000', '029 2018 0001']], chgNote: 'These changed after we submitted to CIW Online on 14/10. Daniel tells CIW about the change through CIW Online. Task added for Daniel.',
        groups: [
          ['Organisation', [F('Organisation name', 'Afon Care Ltd'), F('Legal entity', 'Private limited company'), F('Preferred language', 'English')]],
          ['Responsible Individual', [F('Name', 'Rhian Example'), F('DBS', 'On the Update Service, consent to view given')]],
          ['Service', [F('Service type', 'Domiciliary Support Service'), F('Range of needs', 'Care and support for adults'), F('Areas (one service entry each)', 'Cardiff and Vale; West Glamorgan'), F('Average support hours per week', '251 to 500')]],
          ['Manager', [F('Social Care Wales', 'Registration applied for, reference given')]],
          ['Declarations', [F('Form declaration', 'Signed by Rhian Example, 12/10/2026')]]
        ] },
      rqia: { label: 'RQIA', G: RQIA, kicker: 'RQIA Registration Information Form', client: 'Lagan View Care Ltd', who: 'Niamh', portal: 'the RQIA Web Portal', sheetName: 'RQIA Web Portal sheet', gatesHref: 'Handover.dc.html', gatesLink: 'How RQIA gates differ',
        sub: 'Form arrived 25/09 from Niamh Example, director. All gates passed 29/09. Submitted on the RQIA Web Portal 30/09. Stage 8 of 11: with RQIA.',
        chkSub: 'All 8 passed before submission. Kept for the record; a gate can still be reopened with a reason.',
        chgWhen: 'No edits since submission', changes: [], chgNote: 'Nothing has changed since we submitted on 30/09. If the client edits an answer, it shows here and Daniel is told.',
        groups: [
          ['Provider', [F('Provider name', 'Lagan View Care Ltd'), F('Legal entity', 'Private limited company (Northern Ireland)')]],
          ['Responsible Individual', [F('Name', 'Niamh Example'), F('AccessNI', 'Three ID documents ready for RQIA\'s check')]],
          ['Registered manager', [F('NISCC', 'Registration underway, reference given')]],
          ['Service', [F('Service type', 'Domiciliary Care Agency (conventional)'), F('HSC Trust areas', 'Belfast; South Eastern')]],
          ['Service users', [F('Groups', 'Older people, dementia, physical disability'), F('Expected number', '20')]],
          ['Declarations', [F('Form declaration', 'Signed by Niamh Example, 25/09/2026')]]
        ] }
    };
    const d = D[reg];
    const fixes = st.fixes || [{ id: 'cqc1' }, { id: 'cqc5' }];
    const gates = this.gateRows(d.G, reg, fixes, d.who);
    const res = d.G.map(b => (st.g[reg + b.n] || {}).res || b.res);
    const nP = res.filter(r => r === 'pass').length, nW = res.filter(r => r === 'wait').length, nF = res.filter(r => r === 'fail').length;
    const nFix = d.G.filter((b, i) => res[i] === 'fail' && !b.noFix).length;
    const sent = st.sent[reg];
    const fixLabel = nFix ? (sent ? 'Sent (' + nFix + ')' : 'Send fix list (' + nFix + ')') : 'No fixes to send';
    const groups = d.groups.map(([name, fields], i) => { const key = reg + i, open = !!st.open[key]; return {
      name, count: fields.length + (fields.length === 1 ? ' field' : ' fields'), open, exp: String(open),
      toggle: () => this.setState({ open: Object.assign({}, st.open, { [key]: !open }) }),
      fields: fields.map(([k, v], j) => ({ k, v, label: st.copied === key + '-' + j ? 'Copied' : 'Copy', copy: () => this.setState({ copied: key + '-' + j }) })) }; });
    const DL = [['Client Information Pack', 'Branded PDF with signature record'], [d.sheetName, 'Every field with a copy button'], ['Everything pack', 'ZIP: PDF plus every upload, named consistently'], ['Redacted PDF', 'Dates of birth and ID numbers hidden']];
    return {
      theme: this.props.theme ?? 'light', three: 3, user: { name: 'Grace Whitfield', initials: 'GW' }, nav: __NAV__,
      tabs: Object.keys(D).map(k => ({ label: D[k].label + ': ' + D[k].client, on: k === reg, off: k !== reg, pick: () => this.setState({ reg: k }) })),
      kicker: d.kicker, client: d.client, sub: d.sub, chkSub: d.chkSub + ' Rules: any CV gap longer than ' + (window.CSR ? window.CSR.get('cv-gap-weeks', 4) : 4) + ' weeks needs a line of explanation; documents that expire get a warning ' + (window.CSR ? window.CSR.get('expiry-warning-weeks', 6) : 6) + ' weeks before.', portal: d.portal, sheetName: d.sheetName, gatesHref: d.gatesHref, gatesLink: d.gatesLink,
      gates, nPass: nP + ' pass', nWait: nW + ' waiting', nFail: nF + ' fail',
      fixLabel, fixCls: 'sb-btn ' + (nFix ? 'b-pri' : 'b-gh'),
      sendFix: () => { if (!nFix || sent) return; this.logSet({ sent: Object.assign({}, st.sent, { [reg]: this.now() }) }, 'sent the fix list'); },
      fixSent: !!sent && nFix > 0, fixSentText: 'Fix list (' + nFix + ') sent to ' + d.who + ', ' + (sent || '') + '. The landlord letter is not on it: it was already requested from Tom Reid on 30/10.',
      chgWhen: d.chgWhen, changes: d.changes.map(([k, old, now]) => ({ k, old, now })), chgNote: d.chgNote,
      downloads: DL.map(([k, v]) => ({ k, v, label: st.got === reg + k ? 'Downloaded' : 'Download', get: () => this.setState({ got: reg + k }) })),
      groups
    };
  }
}'''
build(OUT + '/FormStaff.dc.html', 'Form received', 'Onboarding', 1820, B_FORM, S_FORM, 'onboarding', CSS)

# ---------------------------------------------------------------- Questions inbox
QCSS = CSS + '''.qi-item{width:100%;padding:14px 20px;border:0;border-top:1px solid var(--cs-border-subtle);font:inherit;text-align:left;cursor:pointer;display:flex;gap:12px;align-items:flex-start;color:var(--cs-text-primary)}
.qi-sel{background:var(--cs-selection-bg)}
.qi-uns{background:transparent}
.qi-item:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:-2px}
.qi-ta{width:100%;box-sizing:border-box;min-height:120px;padding:10px 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;line-height:20px;resize:vertical}
'''
B_Q = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
''' + H1('Questions from clients', '{{headSub}}') + '''        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <span class="sb-chip c-warn">{{openText}}</span>
          <span class="sb-chip c-ok">{{answeredText}}</span>
          <span class="sb-chip c-neutral">0 overdue</span>
        </div>
      </div>
      <div style="display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; align-items: center;">
        <div role="tablist" aria-label="Show" style="display: flex; gap: 6px; flex-wrap: wrap;">
          <sc-for list="{{filters}}" as="f" hint-placeholder-count="3">
            <sc-if value="{{f.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{f.pick}}">{{f.label}}</button></sc-if>
            <sc-if value="{{f.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{f.pick}}">{{f.label}}</button></sc-if>
          </sc-for>
        </div>
        <div style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;"><span class="sb-muted">Demo: viewing as</span>''' + PICKS('viewers', 'v') + '''</div>
      </div>
      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <div style="flex: 2 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 16px;">
          <section class="sb-card" aria-label="Questions">
            <sc-if value="{{empty}}" hint-placeholder-val="{{ false }}"><div class="sb-row" style="border-top: 0;"><span class="sb-sub">Nothing here. Every question in this view is answered.</span></div></sc-if>
            <sc-for list="{{items}}" as="q" hint-placeholder-count="5">
              <button class="{{q.cls}}" onClick="{{q.pick}}" aria-pressed="{{q.pressed}}">
                <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px;">
                  <span style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><span style="font-weight: 500;">{{q.client}}</span><span class="sb-muted">{{q.where}}</span></span>
                  <span style="font-size: 14px; line-height: 20px;">{{q.text}}</span>
                  <span class="sb-muted">{{q.who}}</span>
                </span>
                <span style="display: flex; flex-direction: column; gap: 4px; align-items: flex-end;"><span class="{{q.slaCls}}">{{q.sla}}</span><sc-if value="{{q.senior}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-brand">With Collins</span></sc-if></span>
              </button>
            </sc-for>
          </section>
          <section class="sb-card" style="padding: 16px 20px; display: flex; flex-direction: column; gap: 8px;" aria-labelledby="sn-h">
            <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px;"><h2 id="sn-h" class="sb-h2">Waiting on a senior</h2><span class="sb-muted">{{seniorTarget}}</span></div>
            <sc-if value="{{noSenior}}" hint-placeholder-val="{{ false }}"><span class="sb-sub">Nothing waiting on a senior.</span></sc-if>
            <sc-for list="{{seniorList}}" as="s" hint-placeholder-count="1">
              <div class="ob-box"><span style="display: flex; justify-content: space-between; gap: 8px;"><span style="font-weight: 500; font-size: 14px;">{{s.client}}</span><span class="sb-muted">{{s.at}}</span></span><span class="sb-sub">{{s.note}}</span><span class="sb-muted">{{s.by}}</span></div>
            </sc-for>
          </section>
          <section class="sb-card" style="padding: 16px 20px 8px;" aria-labelledby="an-h">
            <h2 id="an-h" class="sb-h2" style="margin-bottom: 6px;">Answered earlier today</h2>
            <sc-for list="{{answered}}" as="a" hint-placeholder-count="2"><div class="ob-log" style="flex-direction: column; gap: 2px;"><span><span style="font-weight: 500;">{{a.client}}</span></span><span class="sb-sub">{{a.text}}</span><span class="sb-muted">{{a.by}}</span></div></sc-for>
          </section>
        </div>
        <section class="sb-card" style="flex: 3 1 480px; min-width: 0; padding: 20px; display: flex; flex-direction: column; gap: 14px;" aria-labelledby="qd-h">
          <div style="display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap;">
            <div style="display: flex; flex-direction: column; gap: 2px;"><span class="sb-muted">{{sel.where}}</span><h2 id="qd-h" class="sb-h2">{{sel.client}}</h2></div>
            <span class="{{sel.slaCls}}">{{sel.sla}}</span>
          </div>
          <div class="ob-box"><span class="ob-k">Routed</span><span class="sb-sub">{{sel.route}}</span></div>
          <div style="padding: 12px 14px; border-radius: 10px; background: var(--cs-surface-page); display: flex; flex-direction: column; gap: 6px;">
            <span class="sb-muted">The question</span><span style="font-size: 15px; line-height: 22px;">{{sel.text}}</span>
            <span class="sb-muted">{{sel.context}}</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 6px;">
            <span style="font-weight: 500; font-size: 14px;">Drafted reply</span>
            <span class="sb-muted">{{sel.basis}}</span>
            <textarea class="qi-ta" aria-label="Reply" value="{{sel.reply}}" onChange="{{editReply}}"></textarea>
          </div>
          <sc-if value="{{sel.open}}" hint-placeholder-val="{{ true }}">
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <button class="sb-btn b-pri" onClick="{{send}}">Send reply</button>
              <button class="sb-btn b-sec" onClick="{{askOpen}}" aria-expanded="{{askExp}}">{{askLabel}}</button>
              <button class="sb-btn b-gh" onClick="{{book}}">{{bookLabel}}</button>
            </div>
          </sc-if>
          <sc-if value="{{asking}}" hint-placeholder-val="{{ false }}">
            <div class="g-panel" style="margin-left: 0;">
              <span class="ob-k">Send to a senior: Collins, director</span>
              <label class="ob-k" for="qs-note">Your note for Collins</label>
              <textarea class="ob-ta" id="qs-note" value="{{noteVal}}" onChange="{{onNote}}"></textarea>
              <span class="sb-muted">The client is not told. The question stays in your list, marked "With Collins", and comes back to you with the answer.</span>
              <span style="display: flex; gap: 6px;"><button class="sb-btn b-pri" onClick="{{askSend}}">Send to Collins</button><button class="sb-btn b-gh" onClick="{{askOpen}}">Cancel</button></span>
            </div>
          </sc-if>
          <sc-if value="{{sel.isSenior}}" hint-placeholder-val="{{ false }}"><div class="ob-warn" role="status">{{sel.seniorText}}</div></sc-if>
          <sc-if value="{{sel.done}}" hint-placeholder-val="{{ false }}"><div class="ob-ok" role="status">Sent. The reply appears under the question in the client's Hub, and by email.</div></sc-if>
          <div style="display: flex; gap: 10px; align-items: flex-start; padding-top: 10px; border-top: 1px solid var(--cs-border-subtle);">
            <span style="flex: 1; min-width: 0;" class="sb-sub">{{sel.learn}}</span>
            <button class="sb-btn b-gh" onClick="{{improve}}">{{improveLabel}}</button>
          </div>
        </section>
      </div>
      <span class="sb-muted">How questions are routed: questions from onboarding forms (CQC, CIW, RQIA and tender) go to Grace. Questions from clients past handover go to their case owner, or to the person covering. A question not answered within 6 working hours alerts the team lead.</span>
'''

S_Q = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { f: 'mine', me: 'Grace', sel: 0, sent: {}, senior: { 2: { note: 'Kingfisher\'s insurance renews in January, after the bid date. Can they bid with the current certificate and a renewal letter, or do we need the new one first?', at: '09:20', by: 'Grace' } }, asking: false, note: '', replies: {}, booked: {}, improved: {} }; }
  renderVals() {
    const st = this.state, f = st.f;
    const Q = [
      { to: 'Grace', client: 'Harbour Lane Care Ltd', where: 'CQC onboarding form: DBS for the nominated individual', text: 'I had a DBS for a care job in March 2025. Does that count, or do I need a new one?', who: 'Amara Okafor', sla: 'Reply by 10:00 tomorrow', slaK: 'ok', route: 'To Grace: asked on the CQC onboarding form, before handover.', context: "Her answer so far: not answered yet. Ruth's DBS is done (Enhanced with adult barred list, issued 14 Feb 2026). Amara's 3 ID documents were checked 30 Oct.", basis: "Based on the form's own DBS tip: Enhanced, adult barred list, countersigned, and dated within the last 12 months. 14 similar questions answered before.", reply: "Hi Amara, thank you for asking. For CQC, a DBS counts only if it is an Enhanced check with the adult barred list, countersigned, and issued within the last 12 months. A DBS from March 2025 is more than 12 months old, so it needs to be redone. The good news: your ID is already checked, so we can start the new application for you this week. Choose No on this page and we do the rest. Grace", learn: 'Asked 14 times on this question. Adding "a DBS from another care job counts only if it is Enhanced, with the adult barred list, countersigned and less than 12 months old" to the help text would answer it for most clients.' },
      { to: 'Grace', client: 'Ty Seren Care Ltd', where: 'CIW onboarding form, page 11: references', text: 'My best referee is my current manager, but I have not told them about my company yet. What should I do?', who: 'Ffion Pryce', sla: 'Reply by 12:00 today', slaK: 'warn', route: 'To Grace: asked on the CIW onboarding form, before handover.', context: 'Referee 1 not filled in yet. Referee 2: a former manager.', basis: "Based on the CIW referee questions in the form and Care Sync's reference guidance", reply: 'Hi Ffion, that is a very common worry. CIW contacts referees itself once the application is in CIW Online, so nothing goes to your manager before then. We can talk through the timing, and who else could give a reference, on a short call. Would tomorrow morning suit you? Grace', learn: 'This question comes up for most new providers. The reassurance box on the CQC form could be added to the CIW and RQIA forms too.' },
      { to: 'Grace', client: 'Kingfisher Support Ltd', where: 'Tender onboarding form: finance and insurance', text: 'Our insurance renews in January. Can we still use the current certificate for the bid?', who: 'Marcus Hale', sla: 'Reply by 15:00 today', slaK: 'warn', route: 'To Grace: asked on the tender onboarding form, before handover.', context: 'Employer\'s liability and public liability certificates uploaded Sat 31 Oct. Both end on 14 January.', basis: 'Drafted from the tender form. Waiting for Collins before sending.', reply: 'Hi Marcus, thank you for checking early. Please keep the current certificate on your profile for now. We are checking what this tender asks for when cover renews during the bid, and we will tell you today if you need anything from your broker. Grace', learn: 'Insurance end dates could be read from the upload, with a reminder 6 weeks before they end.' },
      { to: 'Daniel', client: 'Bright Path Care Ltd', where: 'Ask screen', text: 'Is a council flat OK for a home office?', who: 'Joy Adeyemi', sla: 'Reply by 16:00 tomorrow', slaK: 'ok', route: 'To Daniel: Bright Path is past handover and Daniel is the case owner.', context: 'Stage 4 of 11: drafting. Session 2 of 3 with Millicent today at 10:00, Daniel joins.', basis: 'Based on how we handle landlord permission for home offices', reply: 'Hi Joy, it can be. Council tenancies usually need the council\'s written permission before a flat is used for any business, even office work only. We can send the council a short request for you, the same way we do with private landlords. No care happens at the flat, which helps. Let us talk it through in today\'s session at 10:00. Daniel', learn: 'Home office questions come up often. A short "Your office" help note on the Ask screen would answer most of them.' },
      { to: 'Daniel', client: 'Afon Care Ltd', where: 'Ask screen', text: 'CIW has not heard back from my referee Sarah yet. Should I chase her myself?', who: 'Rhian Example', sla: 'Reply by 11:00 tomorrow', slaK: 'ok', route: 'To Daniel: Afon is past handover and Daniel is the case owner.', context: 'Stage 8 of 11: with CIW. CIW asked referee Sarah Jones 3 days ago. Daniel nudges today. Suitability interview Thu 26 Nov.', basis: 'Based on the CIW stage on the client record', reply: 'Hi Rhian, a short friendly message to Sarah is fine: just ask her to look out for CIW\'s email and reply when she can. We are following up today too, and we will tell you as soon as CIW confirms it has her reference. It does not affect your interview on Thu 26 Nov. Daniel', learn: 'Clients at the "with the regulator" stage often ask about referees. The stage page could say who CIW is waiting on.' }
    ];
    const F = [['mine', 'Assigned to me'], ['all', 'All'], ['senior', 'Waiting on a senior']];
    const by2 = t => { const m = /^(\d{2}):(\d{2})$/.exec(t || ''); return m ? String(Number(m[1]) + 2).padStart(2, '0') + ':' + m[2] : 'within 2 working hours'; };
    const senior = st.senior;
    const shown = Q.map((q, i) => Object.assign({ i }, q)).filter(q => !st.sent[q.i] || f === 'all').filter(q => f === 'all' || (f === 'mine' ? q.to === st.me : !!senior[q.i]));
    const selIdx = shown.some(q => q.i === st.sel) ? st.sel : (shown[0] ? shown[0].i : st.sel);
    const cur = Q[selIdx];
    const done = !!st.sent[selIdx];
    const isSen = !!senior[selIdx] && !done;
    const open = Q.filter((q, i) => !st.sent[i]).length;
    const g = Q.filter((q, i) => !st.sent[i] && q.to === 'Grace').length, d = Q.filter((q, i) => !st.sent[i] && q.to === 'Daniel').length;
    const items = shown.map(q => ({ client: q.client, where: q.where, text: q.text, who: q.who + '. Assigned to ' + q.to, senior: !!senior[q.i] && !st.sent[q.i],
      sla: st.sent[q.i] ? 'Answered' : q.sla, slaCls: 'sb-chip ' + (st.sent[q.i] ? 'c-ok' : (q.slaK === 'warn' ? 'c-warn' : 'c-info')),
      cls: 'qi-item ' + (q.i === selIdx ? 'qi-sel' : 'qi-uns'), pressed: String(q.i === selIdx), pick: () => this.setState({ sel: q.i, asking: false }) }));
    const seniorList = Object.keys(senior).filter(k => !st.sent[k]).map(k => ({ client: Q[k].client, note: senior[k].note, at: 'Asked ' + senior[k].at, by: 'From ' + senior[k].by + ' to Collins. Answer by ' + by2(senior[k].at) + '. Question: "' + Q[k].text + '"' }));
    const nowT = '09:' + (45 + Object.keys(senior).length);
    const GQ = (id, fb) => (window.CSR ? window.CSR.get(id, fb) : fb);
    const seniorTarget = 'Target: ' + GQ('reply-senior', '2 working hours');
    const headSub = 'From "Not sure? Ask us" on every form question and from the Ask screen. We reply within ' + GQ('reply-client', '1 working day') + '. Questions sent to a senior are answered within ' + GQ('reply-senior', '2 working hours') + '.';
    return { headSub, seniorTarget,
      theme: this.props.theme ?? 'light', three: 3, user: st.me === 'Grace' ? { name: 'Grace Whitfield', initials: 'GW' } : { name: 'Daniel Mensah', initials: 'DM' }, nav: __NAV__,
      filters: F.map(([k, label]) => ({ label: k === 'senior' ? label + ' (' + seniorList.length + ')' : label, on: f === k, off: f !== k, pick: () => this.setState({ f: k }) })),
      viewers: ['Grace', 'Daniel'].map(n => ({ label: n, cls: 'ob-pick ' + (st.me === n ? 'p-on' : 'p-off'), pressed: String(st.me === n), pick: () => this.setState({ me: n }) })),
      items, empty: items.length === 0,
      openText: open + ' open: Grace ' + g + ', Daniel ' + d, answeredText: (6 + Object.keys(st.sent).length) + ' answered today',
      sel: { client: cur.client, where: cur.where, text: cur.text, context: cur.context, basis: cur.basis, route: cur.route, reply: st.replies[selIdx] !== undefined ? st.replies[selIdx] : cur.reply, learn: cur.learn,
        sla: done ? 'Answered' : cur.sla, slaCls: 'sb-chip ' + (done ? 'c-ok' : (cur.slaK === 'warn' ? 'c-warn' : 'c-info')), open: !done, done,
        isSenior: isSen, seniorText: isSen ? 'With Collins since ' + senior[selIdx].at + '. Your note: ' + senior[selIdx].note : '' },
      editReply: e => this.setState({ replies: Object.assign({}, st.replies, { [selIdx]: e.target.value }) }),
      send: () => this.setState({ sent: Object.assign({}, st.sent, { [selIdx]: true }), asking: false }),
      asking: st.asking && !done, askExp: String(st.asking), askLabel: isSen ? 'Add to the note for Collins' : 'Ask a senior',
      askOpen: () => this.setState({ asking: !st.asking, note: '' }),
      noteVal: st.note, onNote: e => this.setState({ note: e.target.value }),
      askSend: () => this.setState({ asking: false, senior: Object.assign({}, senior, { [selIdx]: { note: st.note.trim() || 'Please check my drafted reply before I send it.', at: nowT, by: cur.to } }) }),
      seniorList, noSenior: seniorList.length === 0,
      book: () => this.setState({ booked: Object.assign({}, st.booked, { [selIdx]: true }) }), bookLabel: st.booked[selIdx] ? 'Call link sent to the client' : 'Book a 10 minute call',
      improve: () => this.setState({ improved: Object.assign({}, st.improved, { [selIdx]: true }) }), improveLabel: st.improved[selIdx] ? 'Sent to the form builder' : 'Improve the help text',
      answered: [
        ['Oakleaf Living Ltd', 'Kemi asked if her HR lead can fill in the staff numbers for the Northshire bid. Yes: the task can be passed to someone in her team.', 'Answered by Daniel at 09:12'],
        ['Willow Bank Supported Living Ltd', 'David asked when they can start bidding for contracts. Most need registration first; the tender profile is built alongside.', 'Answered by Daniel, covering for Olu, at 09:40']
      ].map(([client, text, by]) => ({ client, text, by }))
    };
  }
}'''
build(OUT + '/Questions.dc.html', 'Questions inbox', 'Questions', 1260, B_Q, S_Q, 'questions', QCSS)

# ---------------------------------------------------------------- Address and identity check (Harbour Lane)
B_ADDR = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <a class="ob-link" href="Onboarding.dc.html">Harbour Lane Care Ltd: onboarding gates</a>
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Address and identity check</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Every fact from the onboarding form compared with Companies House and the uploads. Each line belongs to one of the 8 onboarding gates. Last run Mon 2 Nov, 08:15.</span>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;"><span class="sb-chip c-ok">{{nMatch}}</span><span class="sb-chip c-bad">{{nDiff}}</span><span class="sb-chip c-warn">{{nWait}}</span></div>
      </div>
      <section class="sb-card" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="ch-h">
        <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 12px; flex-wrap: wrap;"><h2 id="ch-h" class="sb-h2">Companies House (gate 1, Company and directors)</h2><span class="sb-sub">Watching for changes</span></div>
        <div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 10px;">
          <sc-for list="{{ch}}" as="c" hint-placeholder-count="6"><div class="ob-box" style="gap: 2px;"><span class="ob-k">{{c.k}}</span><span style="font-size: 14px; line-height: 20px; font-weight: 500;">{{c.v}}</span></div></sc-for>
        </div>
        <span class="sb-muted">Personal codes are the Companies House identity verification codes for each director. They belong to gate 1, not gate 2: Kwame's code comes with his director details, which are already on the fix list. Gate 2 (Identity) covers Amara's own identity documents.</span>
      </section>
''' + TABS + '''      <section class="sb-card" aria-labelledby="mx-h">
        <div class="sb-head"><h2 id="mx-h" class="sb-h2">Every fact, by gate</h2><span class="sb-sub">The Statement of Purpose, policies and insurance are not written yet. They are checked against these facts at stage 4.</span></div>
        <div class="sb-row" style="border-top: 0;"><span class="sb-th" style="flex: 0 0 70px;">Gate</span><span class="sb-th" style="flex: 2 1 200px;">Fact</span><span class="sb-th" style="flex: 2 1 190px;">Onboarding form</span><span class="sb-th" style="flex: 2 1 190px;">Companies House</span><span class="sb-th" style="flex: 2 1 210px;">Evidence uploaded</span><span class="sb-th" style="flex: 0 0 150px;">Result</span></div>
        <sc-for list="{{rows}}" as="r" hint-placeholder-count="10">
          <div class="sb-row" style="align-items: flex-start;">
            <span style="flex: 0 0 70px;"><span class="sb-chip c-brand">{{r.gate}}</span></span>
            <span style="flex: 2 1 200px; min-width: 0; font-weight: 500;">{{r.fact}}</span>
            <span style="flex: 2 1 190px; min-width: 0;" class="sb-sub">{{r.form}}</span>
            <span style="flex: 2 1 190px; min-width: 0;" class="sb-sub">{{r.ch}}</span>
            <span style="flex: 2 1 210px; min-width: 0;" class="sb-sub">{{r.ev}}</span>
            <span style="flex: 0 0 150px;"><span class="{{r.cls}}">{{r.res}}</span></span>
          </div>
        </sc-for>
      </section>
      <section class="sb-card" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="of-h">
        <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 12px; flex-wrap: wrap;"><h2 id="of-h" class="sb-h2">Office address (gate 3): form, tenancy and landlord letter</h2><span class="sb-chip c-warn">Waiting on Tom Reid</span></div>
        <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px;">
          <div class="ob-box"><span class="ob-k">Onboarding form, chosen by postcode lookup</span><span style="font-size: 15px; line-height: 22px;">Flat 2, 14 Harbour Road, Stevenage SG1 2AB</span><span class="sb-chip c-ok" style="align-self: flex-start;">Source</span></div>
          <div class="ob-box"><span class="ob-k">Tenancy agreement, page 1, read automatically</span><span style="font-size: 15px; line-height: 22px;">Flat 2, 14 Harbour Road, Stevenage SG1 2AB</span><span class="sb-chip c-ok" style="align-self: flex-start;">Matches</span></div>
          <div class="ob-box"><span class="ob-k">Landlord letter from Tom Reid</span><span style="font-size: 15px; line-height: 22px;">Link sent Fri 30 Oct 15:12. Opened Sat 31 Oct 09:14. Not uploaded yet.</span><span class="sb-chip c-warn" style="align-self: flex-start;">Recheck Thu 5 Nov</span></div>
        </div>
        <span class="sb-sub">Found in the tenancy: it is in Amara's personal name, so Tom's letter must allow the flat to be used as the office of Harbour Lane Care Ltd. The letter we sent him already says this.</span>
        <span class="sb-muted">{{remindNote}}</span>
        <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
          <button class="sb-btn b-sec" onClick="{{nudge}}">{{nudgeLabel}}</button>
          <a class="ob-link" href="ThirdParty.dc.html">See what Tom sees</a>
        </div>
      </section>
'''
S_ADDR = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { t: 'all', nudged: false }; }
  renderVals() {
    const st = this.state;
    const R = [
      ['Gate 1', 'Company name and number', 'Harbour Lane Care Ltd, 99000101', 'Same', 'Not needed', 'Match', 'ok'],
      ['Gate 1', 'Registered office', 'Flat 2, 14 Harbour Road', 'Same', 'Not needed', 'Match', 'ok'],
      ['Gate 1', 'Directors', '1 listed: Amara Okafor', '2: Amara Okafor and Kwame Okafor', 'Not needed', 'Differs: on fix list', 'bad'],
      ['Gate 1', "Directors' personal codes", "Amara's code given", 'Amara verified. Kwame not yet', 'Not needed', "Comes with Kwame's details", 'warn'],
      ['Gate 2', 'Amara: name, date of birth, address', 'Amara Okafor, 14/03/1986, Flat 2, 14 Harbour Road', 'Name and month of birth match', 'Passport, driving licence photocard, council tax bill', 'Match, checked 30 Oct', 'ok'],
      ['Gate 3', 'Office address', 'Flat 2, 14 Harbour Road (rented)', 'Not applicable', 'Tenancy matches. Landlord letter not yet', 'Waiting on Tom Reid', 'warn'],
      ['Gate 4', 'Ruth Bennett: name and date of birth', 'Ruth Anne Bennett, 09/07/1979', 'Not applicable', 'CV and DBS certificate match', 'Match', 'ok'],
      ['Gate 5', "Ruth's employment dates", 'CV received', 'Not applicable', 'Gap March to November 2019', 'Differs: on fix list', 'bad'],
      ['Gate 6', 'Referee 1 is the last employer', 'Referee details given', 'Not applicable', "Matches the last role on Ruth's CV", 'Match', 'ok'],
      ['Gate 7', "Ruth's DBS", 'Number and issue date given', 'Not applicable', 'Photo: Enhanced, adult barred list, 14/02/2026', 'Match', 'ok'],
      ['Gate 8', "Ruth's professional registers", 'Not on a register', 'Not applicable', 'Register check recorded 30 Oct', 'Match', 'ok']
    ];
    const rows = R.filter(r => st.t === 'all' || r[6] !== 'ok').map(r => ({ gate: r[0], fact: r[1], form: r[2], ch: r[3], ev: r[4], res: r[5], cls: 'sb-chip c-' + r[6] }));
    const c = k => R.filter(r => r[6] === k).length;
    return {
      theme: this.props.theme ?? 'light', three: 3, user: { name: 'Grace Whitfield', initials: 'GW' }, nav: __NAV__,
      tabs: [['all', 'All facts (' + R.length + ')'], ['act', 'Needs action (' + (R.length - c('ok')) + ')']].map(([k, label]) => ({ label, on: st.t === k, off: st.t !== k, pick: () => this.setState({ t: k }) })),
      rows, nMatch: c('ok') + ' match', nDiff: c('bad') + ' differ, on the fix list', nWait: c('warn') + ' waiting',
      ch: [['Status', 'Active'], ['Incorporated', '12/03/2025'], ['Nature of business', '88100, fits home care'], ['Filings', 'None overdue'], ['Disqualified directors', 'None found'], ['Directors', '2: Amara and Kwame Okafor'], ['Personal codes', '1 of 2 verified']].map(([k, v]) => ({ k, v })),
      nudge: () => this.setState({ nudged: true }), nudgeLabel: st.nudged ? 'Nudge sent to Tom Reid, 09:40' : 'Nudge Tom Reid',
      remindNote: 'Landlord and referee reminders go ' + (window.CSR ? window.CSR.get('third-party-reminders', 'after 3 working days, then weekly') : 'after 3 working days, then weekly') + '. Tom\'s first reminder goes automatically on Wed 4 Nov, 3 working days after the link. The client is never asked for it.'
    };
  }
}'''
build(OUT + '/AddressCheck.dc.html', 'Address and identity check', 'Onboarding', 1580, B_ADDR, S_ADDR, 'onboarding', CSS)

# ---------------------------------------------------------------- Onboarding queue (new)
B_QUEUE = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
''' + H1('Onboarding', "Grace's queue: every client between payment and handover. Monday 2 November, 10:30.") + '''      </div>
      <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="5"><div class="sb-card sb-kpi"><span class="sb-kv">{{k.v}}</span><span class="sb-sub">{{k.k}}</span></div></sc-for>
      </div>
''' + TABS + '''      <section class="sb-card" aria-label="Clients in onboarding">
        <div class="sb-row" style="border-top: 0;"><span class="sb-th" style="flex: 2 1 190px;">Client</span><span class="sb-th" style="flex: 1 1 130px;">Package and regulator</span><span class="sb-th" style="flex: 1 1 150px;">Form progress</span><span class="sb-th" style="flex: 1 1 150px;">Last activity</span><span class="sb-th" style="flex: 2 1 190px;">Waiting on</span><span class="sb-th" style="flex: 0 0 84px;">Recheck</span><span class="sb-th" style="flex: 0 0 56px;">Days</span><span class="sb-th" style="flex: 0 0 116px;">Nudge</span></div>
        <sc-for list="{{rows}}" as="r" hint-placeholder-count="6">
          <div class="sb-row" style="align-items: flex-start;">
            <span style="flex: 2 1 190px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{r.name}}</span><span class="sb-muted">{{r.contact}}</span><sc-if value="{{r.hasLink}}" hint-placeholder-val="{{ false }}"><a class="ob-link" href="{{r.href}}">{{r.linkText}}</a></sc-if></span>
            <span style="flex: 1 1 130px; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span class="{{r.regCls}}" style="align-self: flex-start;">{{r.reg}}</span><span class="sb-muted">{{r.pkg}}</span></span>
            <span style="flex: 1 1 150px; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span class="sb-sub">{{r.prog}}</span><span class="bar" aria-hidden="true"><span class="{{r.bar}}"></span></span></span>
            <span style="flex: 1 1 150px; min-width: 0;" class="sb-sub">{{r.last}}</span>
            <span style="flex: 2 1 190px; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span class="{{r.waitCls}}" style="align-self: flex-start;">{{r.wait}}</span><span class="sb-muted">{{r.waitWhy}}</span></span>
            <span style="flex: 0 0 84px;" class="sb-sub">{{r.recheck}}</span>
            <span style="flex: 0 0 56px; font-weight: 500;">{{r.days}}</span>
            <span style="flex: 0 0 116px; display: flex; flex-direction: column; gap: 2px;"><button class="{{r.nudgeCls}}" onClick="{{r.nudge}}" aria-label="{{r.nudgeAria}}">{{r.nudgeLabel}}</button><span class="sb-muted">{{r.nudgeTo}}</span></span>
          </div>
        </sc-for>
      </section>
      <span class="sb-muted">{{queueNote}}</span>
'''
S_QUEUE = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { t: 'all', nudged: {} }; }
  renderVals() {
    const st = this.state;
    // [key, name, contact, reg, pkg, prog, bar, last, waitGroup, wait, waitWhy, recheck, days, nudgeTo, link]
    const R = [
      ['hl', 'Harbour Lane Care Ltd', 'Amara Okafor', 'CQC', 'Full start-up, domiciliary care', 'Form arrived 29 Oct. Checks 5 of 8', 'w60', 'Tom Reid opened the landlord letter link, Sat 31 Oct', 'us', 'Us: send fix list (2)', 'Also waiting on the landlord, Tom Reid, for the office letter', 'Thu 5 Nov', 14, 'Tom Reid', ['Onboarding.dc.html', 'Open the gates']],
      ['mv', 'Meadow View Care Ltd', 'Ade Ola', 'CQC', 'Full start-up, domiciliary care', 'Form not sent yet. Sent after the call', 'w0', 'Paid today 10:02', 'us', 'Us: introduction call', 'Divine calls by 12:02. Then the form goes out', 'Today 12:02', 0, 'Divine', ['IntroCall.dc.html', 'Open the call']],
      ['ts', 'Ty Seren Care Ltd', 'Ffion Pryce', 'CIW', 'CIW registration, domiciliary support', 'Form arrived 28 Oct. Checks 6 of 8', 'w75', 'Asked about referees, today 08:50', 'client', 'Client: 2 fixes', 'A second RI referee, and the manager\'s Social Care Wales reference. Sent Fri 30 Oct', 'Wed 4 Nov', 12, 'Ffion Pryce', null],
      ['kf', 'Kingfisher Support Ltd', 'Marcus Hale', 'Tender', 'Tender writing, supported living', 'Tender form 9 of 15 sections', 'w60', 'Uploaded insurance certificates, Sat 31 Oct', 'client', 'Client: rest of the form', 'Policies list, workforce and case studies still to fill in', 'Thu 5 Nov', 7, 'Marcus Hale', null],
      ['oh', 'Oak Hollow Care Ltd', 'Lena Brooks', 'CQC', 'CQC registration, supported living', 'Stopped at section 8 of 13', 'w60', 'Last answer Tue 27 Oct, 6 days ago', 'client', 'Client: stopped mid-form', 'Reminders sent Thu 29 Oct and Sat 31 Oct, not opened. Day 6: Grace calls today', 'Today', 13, 'Lena Brooks', null],
      ['bn', 'Binnian Care Ltd', 'Ciara Doherty', 'RQIA', 'RQIA registration, domiciliary care agency', 'Form arrived 22 Oct. Checks 8 of 8', 'w100', 'Grace asked Collins to approve the handover, Fri 30 Oct', 'ready', 'Ready for handover', 'Waiting for Collins to approve. Proposed case owner: Olu', 'Today', 18, 'Collins', ['Handover.dc.html', 'Open the handover']]
    ];
    const T = [['all', 'All'], ['client', 'Waiting on the client'], ['us', 'Waiting on us'], ['ready', 'Ready for handover']];
    const cnt = k => R.filter(r => r[8] === k).length;
    const WC = { us: 'c-info', client: 'c-warn', ready: 'c-ok' };
    const rows = R.filter(r => st.t === 'all' || r[8] === st.t).map(r => {
      const sent = st.nudged[r[0]];
      return { name: r[1], contact: r[2], reg: r[3], regCls: 'sb-chip ' + (r[3] === 'Tender' ? 'c-info' : 'c-brand'), pkg: r[4], prog: r[5], bar: r[6], last: r[7],
        wait: r[9], waitCls: 'sb-chip ' + WC[r[8]], waitWhy: r[10], recheck: r[11], days: String(r[12]),
        hasLink: !!r[14], href: r[14] ? r[14][0] : '#', linkText: r[14] ? r[14][1] : '',
        nudgeLabel: sent ? 'Sent ' + sent : 'Nudge', nudgeCls: 'sb-btn ' + (sent ? 'b-gh' : 'b-sec'), nudgeTo: (sent ? 'Nudged: ' : 'To ') + r[13], nudgeAria: 'Nudge ' + r[13] + ' about ' + r[1],
        nudge: () => { if (sent) return; this.setState({ nudged: Object.assign({}, st.nudged, { [r[0]]: '10:' + String(30 + Object.keys(st.nudged).length) }) }); } };
    });
    const avg = Math.round(R.reduce((a, r) => a + r[12], 0) / R.length);
    const GN = (id, fb) => (window.CSR ? window.CSR.get(id, fb) : fb);
    const queueNote = 'Days in onboarding count from payment. Form reminders: ' + GN('form-reminders', 'after 2 days and 4 days; Grace calls on day 6; then weekly') + '. Landlord and referee reminders ' + GN('third-party-reminders', 'after 3 working days, then weekly') + '. Documents: ' + GN('document-reminders', 'after 3 days, then weekly') + '. No reminder goes in quiet hours (' + GN('quiet-hours', '8pm to 8am') + '). Nudges are logged on the client record. A worried client gets a call from a person instead of automatic nudges.';
    return { queueNote,
      theme: this.props.theme ?? 'light', three: 3, user: { name: 'Grace Whitfield', initials: 'GW' }, nav: __NAV__,
      tabs: T.map(([k, label]) => ({ label: label + ' (' + (k === 'all' ? R.length : cnt(k)) + ')', on: st.t === k, off: st.t !== k, pick: () => this.setState({ t: k }) })),
      rows,
      kpis: [[String(R.length), 'clients in onboarding'], [String(cnt('client')), 'waiting on the client'], [String(cnt('us')), 'waiting on us'], [String(cnt('ready')), 'ready for handover'], [avg + ' days', 'average time in onboarding']].map(([v, k]) => ({ v, k }))
    };
  }
}'''
build(OUT + '/OnboardingQueue.dc.html', 'Onboarding queue', 'Onboarding', 1030, B_QUEUE, S_QUEUE, 'onboarding', CSS)

# ---------------------------------------------------------------- Handover (new): Binnian Care Ltd, RQIA, all gates passed
B_HO = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <a class="ob-link" href="OnboardingQueue.dc.html">Onboarding queue</a>
          <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
            <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Handover: Binnian Care Ltd</h1>
            <span class="sb-chip c-ok">All 8 gates passed</span><span class="{{stateCls}}">{{stateChip}}</span>
          </div>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">RQIA, domiciliary care agency. RQIA registration package. Paid Thu 15 Oct, form arrived Thu 22 Oct, last gate passed Fri 30 Oct. Grace hands over; Collins approves. Viewing as Collins.</span>
        </div>
      </div>
      <div class="{{lockCls}}" role="status"><span style="font-weight: 600;">{{lockTitle}}</span><span>{{lockText}}</span></div>
      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <div style="flex: 3 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 16px;">
          <section class="sb-card" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="sa-h">
            <h2 id="sa-h" class="sb-h2">Summary of answers</h2>
            <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px 20px;">
              <sc-for list="{{answers}}" as="a" hint-placeholder-count="8"><span style="display: flex; flex-direction: column;"><span class="ob-k">{{a.k}}</span><span class="ob-v">{{a.v}}</span></span></sc-for>
            </div>
          </section>
          <section class="sb-card" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 8px;" aria-labelledby="ic-h">
            <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px;"><h2 id="ic-h" class="sb-h2">Introduction call notes</h2><span class="sb-muted">Divine, Thu 15 Oct</span></div>
            <sc-for list="{{call}}" as="c" hint-placeholder-count="4"><span class="sb-sub" style="display: flex; gap: 8px;"><span aria-hidden="true">&#8226;</span><span>{{c.t}}</span></span></sc-for>
          </section>
          <section class="sb-card" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 8px;" aria-labelledby="rk-h">
            <h2 id="rk-h" class="sb-h2">Open risks for the case owner</h2>
            <sc-for list="{{risks}}" as="r" hint-placeholder-count="3"><div class="ob-box" style="flex-direction: row; gap: 10px; align-items: flex-start;"><span class="{{r.cls}}">{{r.level}}</span><span class="sb-sub" style="flex: 1; min-width: 0;">{{r.t}}</span></div></sc-for>
          </section>
          <section class="sb-card" aria-labelledby="dr-h">
            <div class="sb-head"><h2 id="dr-h" class="sb-h2">Documents received</h2><span class="sb-sub">{{docCount}}</span></div>
            <sc-for list="{{docs}}" as="d" hint-placeholder-count="7"><div class="sb-row"><span style="flex: 1; min-width: 0;">{{d.k}}</span><span class="sb-muted">{{d.v}}</span><span class="sb-chip c-ok">Accepted</span></div></sc-for>
          </section>
        </div>
        <div style="flex: 2 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 16px;">
          <section class="sb-card" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="ap-h">
            <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px;"><h2 id="ap-h" class="sb-h2">Manager approval</h2><span class="{{stateCls}}">{{stateChip}}</span></div>
            <span class="ob-k">Proposed case owner</span>
            <span style="display: flex; gap: 6px; flex-wrap: wrap;">''' + PICKS('owners', 'o') + '''</span>
            <span class="sb-sub">{{ownerLoad}}</span>
            <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px;">
              <span style="display: flex; flex-direction: column;"><span class="ob-k">Weekly update owner</span><span class="ob-v">{{weekly}}</span></span>
              <span style="display: flex; flex-direction: column;"><span class="ob-k">Coach</span><span class="ob-v">Millicent</span></span>
            </div>
            <sc-if value="{{waiting}}" hint-placeholder-val="{{ true }}">
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <label class="ob-k" for="ho-note">Note for Grace and the case owner (optional)</label>
                <textarea class="ob-ta" id="ho-note" value="{{note}}" onChange="{{onNote}}"></textarea>
                <span style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{approve}}">{{approveLabel}}</button><button class="sb-btn b-gh" onClick="{{sendBack}}">Send back to Grace</button></span>
              </div>
            </sc-if>
            <sc-if value="{{approved}}" hint-placeholder-val="{{ false }}"><div class="ob-ok" role="status">{{approvedText}}</div></sc-if>
            <sc-if value="{{back}}" hint-placeholder-val="{{ false }}"><div class="ob-warn" role="status">{{backText}}</div></sc-if>
            <sc-if value="{{notWaiting}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" style="align-self: flex-start;" onClick="{{reset}}">Undo (demo)</button></sc-if>
            <div class="ob-box"><span class="ob-k">What Ciara sees in her Hub now</span><span class="sb-sub">{{clientSees}}</span></div>
          </section>
          <section class="sb-card" aria-labelledby="gs-h">
            <div class="sb-head"><h2 id="gs-h" class="sb-h2">RQIA gates</h2><span class="sb-sub">8 of 8 passed</span></div>
            <sc-for list="{{gates}}" as="g" hint-placeholder-count="8"><div class="sb-row" style="padding: 8px 20px;"><span class="g-num">{{g.n}}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column;"><span style="font-weight: 500;">{{g.k}}</span><span class="sb-muted">{{g.v}}</span></span><span class="sb-chip c-ok">Pass</span></div></sc-for>
          </section>
          <section class="sb-card" style="padding: 18px 20px 10px;" aria-labelledby="lg-h">
            <h2 id="lg-h" class="sb-h2" style="margin-bottom: 6px;">Log</h2>
            ''' + LOG + '''
          </section>
        </div>
      </div>
      <section class="sb-card" style="padding: 18px 20px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="df-h">
        <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px; flex-wrap: wrap;"><h2 id="df-h" class="sb-h2">How the gates differ by regulator</h2><span class="sb-sub">Every client has 8 gates before handover. What each gate checks depends on the regulator or the tender.</span></div>
        <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
          <sc-for list="{{regs}}" as="r" hint-placeholder-count="4">
            <div class="ob-box" style="gap: 6px;">
              <span style="display: flex; gap: 8px; align-items: center;"><span class="sb-chip c-brand">{{r.name}}</span><span class="sb-muted">{{r.who}}</span></span>
              <sc-for list="{{r.items}}" as="i" hint-placeholder-count="5"><span class="sb-sub" style="display: flex; gap: 6px;"><span aria-hidden="true">&#8226;</span><span>{{i.t}}</span></span></sc-for>
            </div>
          </sc-for>
        </div>
        <span class="sb-muted">Kept general on purpose. Grace checks the regulator's current guidance for each client, and the form builder holds the exact questions.</span>
      </section>
'''
S_HO = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { st: 'waiting', owner: 'olu', note: '', at: '' }; }
  renderVals() {
    const s = this.state;
    const O = [['olu', 'Olu', 'Olu: does RQIA work and has Lagan View. 4 active clients. On leave Mon 2 to Fri 6 November, so starts Mon 9 Nov. Nothing waits on Daniel.'], ['daniel', 'Daniel', 'Daniel: 6 active, covering 4 this week for Olu, and Harbour Lane coming after approval. Does CQC, CIW and tenders.']];
    const ow = O.find(x => x[0] === s.owner);
    const approved = s.st === 'approved', back = s.st === 'back';
    const baseLog = [
      { who: 'Grace', text: 'asked Collins to approve the handover, proposing Olu', at: 'Fri 30 Oct 16:05' },
      { who: 'Grace', text: 'accepted gate 5: NISCC registration underway, reference given', at: 'Fri 30 Oct 15:40' },
      { who: 'Grace', text: 'accepted the office lease and landlord letter (gate 3)', at: 'Wed 28 Oct 11:10' },
      { who: 'Ciara', text: 'sent the RQIA onboarding form, signed electronically', at: 'Thu 22 Oct 19:20' },
      { who: 'Divine', text: 'made the introduction call. The form was sent straight after', at: 'Thu 15 Oct' }
    ];
    const extra = approved ? [
      { who: 'Hub', text: 'unlocked the 3 included sessions. Ciara can book her kick-off with Millicent', at: 'Mon 2 Nov ' + s.at },
      { who: 'Hub', text: 'told Ciara: "' + ow[1] + ' is your consultant"', at: 'Mon 2 Nov ' + s.at },
      { who: 'Hub', text: 'opened Stage 2 of 11: CV review, and set ' + ow[1] + ' as case owner and weekly update owner', at: 'Mon 2 Nov ' + s.at },
      { who: 'Collins', text: 'approved the handover to ' + ow[1] + (s.note.trim() ? '. Note: ' + s.note.trim() : ''), at: 'Mon 2 Nov ' + s.at }
    ] : (back ? [{ who: 'Collins', text: 'sent the handover back to Grace. Note: ' + (s.note.trim() || 'please add more detail on the staffing plan'), at: 'Mon 2 Nov ' + s.at }] : []);
    return {
      theme: this.props.theme ?? 'light', three: 3, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      stateChip: approved ? 'Approved by Collins' : (back ? 'Sent back to Grace' : 'Waiting for Collins'), stateCls: 'sb-chip ' + (approved ? 'c-ok' : 'c-warn'),
      lockCls: approved ? 'ob-ok ob-flex' : 'ob-lock', lockTitle: approved ? 'Unlocked:' : 'Locked until Collins approves:',
      lockText: approved ? 'application work (stages 2 to 6) and the 3 included sessions are open. Ciara has been told who her consultant is.' : 'application work (stages 2 to 6) and the 3 included sessions. The client has not been told who her consultant is yet.',
      answers: [['Provider', 'Binnian Care Ltd, a Northern Ireland company'], ['Responsible Individual', 'Ciara Doherty, director'], ['Registered manager', 'Aoife Kelly, a different person'], ['Service', 'Domiciliary care agency (conventional)'], ['HSC Trust area', 'Southern HSC Trust'], ['Service users', 'Older people, dementia, physical disability. About 15 at the start'], ['Office', 'Unit 4, Example Business Park, Newry. Leased, landlord letter accepted'], ['Planned start', 'Spring 2027']].map(([k, v]) => ({ k, v })),
      call: ['Ciara ran a care team for 9 years and knows the Minimum Standards well.', 'Worried about the time RQIA takes. We explained RQIA sets its own pace and we update her every Friday.', 'Prefers email, and calls after 16:00.', 'Happy with the call. No concerns raised.'].map(t => ({ t })),
      risks: [['Check', 'c-warn', "Aoife's NISCC registration is underway, not confirmed. Check it is in place before the application goes in."], ['Note', 'c-info', "RQIA runs its own AccessNI check with its PIN after the application is in. Both sets of 3 ID documents are ready."], ['Note', 'c-info', 'Referee 2 for Aoife is due from Ciara by Fri 13 Nov. It is not a gate.']].map(([level, k, t]) => ({ level, cls: 'sb-chip ' + k, t })),
      docs: [['CVs for Ciara and Aoife', '22 Oct'], ['3 ID documents each, for AccessNI', '22 Oct'], ['Office lease and landlord letter', '28 Oct'], ["Referee 1 for Aoife, most recent employer", '26 Oct'], ['GP details for both', '22 Oct'], ["Aoife's NISCC application reference", '30 Oct'], ['Company certificate', 'From Companies House']].map(([k, v]) => ({ k, v })),
      docCount: '7 documents, all accepted by Grace',
      owners: O.map(([k, label]) => ({ label, cls: 'ob-pick ' + (s.owner === k ? 'p-on' : 'p-off'), pressed: String(s.owner === k), pick: () => { if (s.st === 'waiting') this.setState({ owner: k }); } })),
      ownerLoad: ow[2], weekly: ow[1] + ', from approval',
      waiting: s.st === 'waiting', notWaiting: s.st !== 'waiting', approved, back,
      note: s.note, onNote: e => this.setState({ note: e.target.value }),
      approveLabel: 'Approve handover to ' + ow[1],
      approve: () => this.setState({ st: 'approved', at: '10:45' }), sendBack: () => this.setState({ st: 'back', at: '10:45' }), reset: () => this.setState({ st: 'waiting', at: '' }),
      approvedText: 'Approved by Collins, Mon 2 Nov 10:45, and logged. ' + ow[1] + ' is case owner and weekly update owner. Ciara has been told, stage 2 is open and sessions are unlocked.',
      backText: 'Sent back to Grace, Mon 2 Nov 10:45, and logged. Nothing is unlocked and the client is not told.',
      clientSees: approved ? '"Your checks are done. ' + ow[1] + ' is your consultant and starts on your RQIA application' + (s.owner === 'olu' ? ' on Mon 9 Nov' : '') + '. Book your kick-off session with Millicent."' : '"Your checks are done, thank you. We are choosing your consultant and will tell you very soon."',
      gates: [['Company and directors', 'Companies House (Northern Ireland) matches'], ['Identity for AccessNI', '3 ID documents each for Ciara and Aoife'], ['Office address evidence', 'Lease and landlord letter accepted 28 Oct'], ['Responsible Individual', 'Ciara: qualifications and experience given'], ['Manager and NISCC', 'NISCC registration underway, reference given'], ['Employment history', 'Both CVs complete, no gaps'], ['References', 'Referee 1 is the most recent employer'], ['Professional registers', 'Checked for Ciara and Aoife 30 Oct, recorded']].map(([k, v], i) => ({ n: String(i + 1), k, v })),
      log: extra.concat(baseLog),
      regs: [
        ['CQC', 'England', ['Company and directors (Companies House)', 'Identity, or DBS details', 'Office address evidence', 'Registered manager and nominated individual', 'Enhanced DBS with adult barred list', 'Employment history, references, professional registers']],
        ['CIW', 'Wales', ['Company and officers', 'Responsible Individual named for the company', 'DBS for the RI and the manager', 'Manager registered with Social Care Wales, or applied', 'References and GP details for each person', 'Office in Wales and the areas served']],
        ['RQIA', 'Northern Ireland', ['Company and directors', 'Responsible Individual', 'ID documents for AccessNI, which RQIA checks itself', 'Manager registered with NISCC, or underway', 'A reference from the current or most recent employer', 'Office address and staffing plan']],
        ['Tender', 'Any council', ['Tender profile complete', 'Policies in date', 'Insurance in place and in date', 'Registration in place where the tender needs it', 'Case studies and references ready', 'Bid or no bid approved by Collins']]
      ].map(([name, who, items]) => ({ name, who, items: items.map(t => ({ t })) }))
    };
  }
}'''
build(OUT + '/Handover.dc.html', 'Handover', 'Onboarding', 2020, B_HO, S_HO, 'onboarding', CSS)
