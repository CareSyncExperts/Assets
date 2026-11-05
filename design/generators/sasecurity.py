# Super admin boards owned by agent D: Security (84), Data and privacy (85), People and access (83).
# Run from SP/gen:  python3 sasecurity.py
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from staffboard import build_sa
OUT = os.path.join(HERE, '..', 'hub-canvas', 'project')
H_SEC, H_PRIV, H_PPL = 2720, 2240, 1520
if len(sys.argv) > 1:
    OUT = sys.argv[1]

CSS = '''.sx-in{min-height:40px;padding:0 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;box-sizing:border-box}
.sx-ta{width:100%;min-height:64px;padding:8px 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;line-height:20px;box-sizing:border-box;resize:vertical}
.sx-in:focus-visible,.sx-ta:focus-visible,.sx-sw:focus-visible,.sx-tile:focus-visible,.sx-cell:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:2px}
.sx-err{font-size:13px;line-height:18px;color:var(--cs-status-error-text);font-weight:500}
.sx-box{padding:12px 14px;border-radius:10px;background:var(--cs-surface-subtle);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.sx-red{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-error-border);background:var(--cs-status-error-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.sx-amb{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-warning-border);background:var(--cs-status-warning-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.sx-ok{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-success-border);background:var(--cs-status-success-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.sx-inf{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-info-border);background:var(--cs-status-info-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.sx-lbl{font-size:12px;line-height:16px;color:var(--cs-text-muted);font-weight:500}
.sx-b{font-weight:500}
.sx-big{font-size:30px;line-height:38px;font-weight:600}
.sx-cols{display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start}
.sx-pad{padding:0 20px 18px;display:flex;flex-direction:column;gap:12px}
.sx-kv{display:grid;grid-template-columns:170px minmax(0,1fr);gap:8px 16px;font-size:14px;line-height:20px}
.sx-kv>span:nth-child(odd){color:var(--cs-text-muted);font-size:13px}
.sx-tile{background:var(--cs-surface-raised);border-radius:12px;box-shadow:var(--cs-elevation-1);border:0;padding:14px 16px;display:flex;flex-direction:column;gap:2px;text-align:left;font:inherit;color:var(--cs-text-primary);cursor:pointer;min-height:96px}
.sx-tv{font-size:24px;line-height:32px;font-weight:600}
.sx-sw{width:52px;height:32px;border-radius:999px;border:0;padding:3px;display:inline-flex;align-items:center;cursor:pointer;flex-shrink:0}
.sx-sw span{width:26px;height:26px;border-radius:999px;background:var(--cs-surface-raised);display:block}
.sw-on{background:var(--cs-action-primary);justify-content:flex-end}
.sw-off{background:var(--cs-border-default);justify-content:flex-start}
.sw-lock{background:var(--cs-action-primary);justify-content:flex-end;opacity:.55;cursor:not-allowed}
.sx-step{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.st-done{display:inline-flex;align-items:center;min-height:28px;padding:0 10px;border-radius:999px;font-size:12px;font-weight:500;background:var(--cs-status-success-bg);color:var(--cs-status-success-text)}
.st-now{display:inline-flex;align-items:center;min-height:28px;padding:0 10px;border-radius:999px;font-size:12px;font-weight:600;border:2px solid var(--cs-action-primary);color:var(--cs-text-primary);background:var(--cs-surface-raised)}
.st-next{display:inline-flex;align-items:center;min-height:28px;padding:0 10px;border-radius:999px;font-size:12px;border:1px dashed var(--cs-border-default);color:var(--cs-text-muted)}
.sx-chk{display:flex;gap:10px;align-items:flex-start;min-height:36px;cursor:pointer;font-size:14px;line-height:20px}
.sx-chk input{width:20px;height:20px;margin:0;flex-shrink:0;accent-color:var(--cs-action-primary)}
.sx-cell{min-height:36px;width:100%;padding:4px 8px;border-radius:8px;font:inherit;font-size:12px;line-height:16px;text-align:left;cursor:pointer;border:1px solid var(--cs-border-subtle);background:var(--cs-surface-raised);color:var(--cs-text-primary)}
.cell-ch{border:2px solid var(--cs-action-primary);background:var(--cs-surface-brand);color:var(--cs-text-brand);font-weight:500}
.cell-no{color:var(--cs-text-muted);background:transparent}
.sx-link{color:var(--cs-text-brand);font-weight:500;text-decoration:underline;text-underline-offset:2px}
.sx-col3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.sx-col2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.sx-ol{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
'''

def tabs(label):
    return '''      <div role="tablist" aria-label="''' + label + '''" style="display: flex; gap: 6px; flex-wrap: wrap;">
        <sc-for list="{{tabs}}" as="tb" hint-placeholder-count="6">
          <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
          <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
        </sc-for>
      </div>
'''

def subtabs(listname, label, count=4):
    return '''<div role="tablist" aria-label="''' + label + '''" style="display: flex; gap: 6px; flex-wrap: wrap;">
          <sc-for list="{{''' + listname + '''}}" as="tb" hint-placeholder-count="''' + str(count) + '''">
            <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
            <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
          </sc-for>
        </div>'''

def header(title, sub, right=''):
    return '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px; max-width: 820px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">''' + title + '''</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">''' + sub + '''</span>
        </div>
''' + right + '''      </div>
'''

TILES = '''      <div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{tiles}}" as="k" hint-placeholder-count="6">
          <button class="sx-tile" onClick="{{k.go}}" aria-label="{{k.aria}}"><span class="sb-sub">{{k.k}}</span><span class="sx-tv">{{k.v}}</span><span class="{{k.cls}}" style="white-space: normal; align-self: flex-start;">{{k.note}}</span></button>
        </sc-for>
      </div>
'''

JSHELP = r'''    const G = (k, f) => { try { return (window.CSR && window.CSR.get) ? window.CSR.get(k, f) : f; } catch (e) { return f; } };
    const ch = k => 'sb-chip c-' + k;
    const up = (o, k, v) => Object.assign({}, o, { [k]: v });
'''

# ---------------------------------------------------------------------------------------------
# 84. Security
# ---------------------------------------------------------------------------------------------
SEC_RIGHT = '''        <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
          <button class="sb-btn b-gh" onClick="{{toggleRep}}">{{repLabel}}</button>
        </div>
'''
SEC_B = header('Security', 'Incidents, the audit log, the vault, elevated access, sign-in and resilience, in one place. Shown at Monday 2 November, 09:20. Collins, the data protection lead, owns this screen with Rachel Turner, the other super admin.', SEC_RIGHT) + '''      <sc-if value="{{repOpen}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card sx-pad" style="padding-top: 16px;" aria-labelledby="rep-h">
          <h2 id="rep-h" class="sb-h2">Report a concern or incident</h2>
          <span class="sb-sub">Anyone at Care Sync can report from any staff screen: a lost phone, an email to the wrong person, something that looks wrong. It goes straight to Collins, the data protection lead, and Rachel Turner, and the time you report is written down.</span>
          <label class="sx-lbl" for="rep-ta">What happened, as far as you know</label>
          <textarea id="rep-ta" class="sx-ta" value="{{repText}}" onChange="{{onRep}}" placeholder="For example: I left my work phone on the train at 08:15. It has a screen lock."></textarea>
          <sc-if value="{{repErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Write a few words about what happened first.</span></sc-if>
          <div style="display: flex; gap: 8px;"><button class="sb-btn b-pri" onClick="{{sendRep}}">Send the report</button></div>
          <sc-if value="{{repSent}}" hint-placeholder-val="{{ false }}"><div class="sx-ok"><span class="sx-b">Sent to Collins and Rachel Turner at 09:20.</span><span class="sb-sub">It is in the audit log as an incident step, and Collins, the data protection lead, decides whether it needs a breach assessment.</span></div></sc-if>
        </section>
      </sc-if>
''' + TILES + tabs('Security areas') + '''
      <sc-if value="{{isInc}}" hint-placeholder-val="{{ true }}">
        <div class="sx-cols">
          <section class="sb-card" style="flex: 3 1 600px; min-width: 0;" aria-labelledby="inc-h">
            <div class="sb-head"><h2 id="inc-h" class="sb-h2">Incident 2026-01: a leaver downloaded 38 client documents</h2><span class="{{incCls}}">{{incState}}</span></div>
            <div class="sx-pad">
              <div class="sx-step" aria-label="Where this incident is">
                <sc-for list="{{steps}}" as="st" hint-placeholder-count="5"><span class="{{st.cls}}">{{st.label}}</span></sc-for>
              </div>
              <div class="sx-kv">
                <sc-for list="{{facts}}" as="f" hint-placeholder-count="10"><span>{{f.k}}</span><span>{{f.v}}</span></sc-for>
              </div>
              <div class="sx-ok">
                <span class="sx-b">Contained</span>
                <sc-for list="{{contain}}" as="c" hint-placeholder-count="5"><span style="display: flex; gap: 10px;"><span class="sb-chip c-ok" style="flex: 0 0 auto;">{{c.t}}</span><span>{{c.x}}</span></span></sc-for>
              </div>
              <div class="sx-box" style="gap: 10px;">
                <span class="sx-b">Risk to the people in the files</span>
                <div style="display: flex; gap: 24px; flex-wrap: wrap;">
                  <div style="display: flex; flex-direction: column; gap: 6px;"><span class="sx-lbl">How likely is harm</span>''' + subtabs('likeTabs', 'Likelihood', 3) + '''</div>
                  <div style="display: flex; flex-direction: column; gap: 6px;"><span class="sx-lbl">How bad it would be</span>''' + subtabs('sevTabs', 'Severity', 3) + '''</div>
                </div>
                <span class="sb-sub">{{riskText}}</span>
              </div>
              <div class="sx-box" style="gap: 10px;">
                <div style="display: flex; justify-content: space-between; gap: 8px; flex-wrap: wrap;"><span class="sx-b">Report to the ICO: yes or no, with reasons</span><span class="sb-muted">UK GDPR Art 33(1) and 33(5)</span></div>
                <span class="sb-sub">Report unless the breach is unlikely to result in a risk to people. The record is kept either way, with the facts, the effects and what we did.</span>
                <span class="sb-sub">The data protection lead (Collins) decides. Because Collins is also a super admin, Rachel Turner reviews the decision as a second pair of eyes.</span>
                <sc-if value="{{icoOpen}}" hint-placeholder-val="{{ true }}">
                  <div style="display: flex; flex-direction: column; gap: 8px;">
                    ''' + subtabs('icoTabs', 'Report to the ICO', 2) + '''
                    <label class="sx-lbl" for="ico-ta">Reasons (kept in the breach record)</label>
                    <textarea id="ico-ta" class="sx-ta" value="{{icoR}}" onChange="{{onIcoR}}" placeholder="{{icoPh}}"></textarea>
                    <sc-if value="{{icoErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">{{icoErrText}}</span></sc-if>
                    <div><button class="sb-btn b-pri" onClick="{{saveIco}}">Record the decision</button></div>
                  </div>
                </sc-if>
                <sc-if value="{{icoDone}}" hint-placeholder-val="{{ false }}">
                  <div class="{{icoBox}}"><span class="sx-b">{{icoHead}}</span><span class="sb-sub">{{icoNote}}</span><span class="sb-sub">Reasons: "{{icoR}}"</span><div><button class="sb-btn b-gh" onClick="{{undoIco}}">Change the decision</button></div></div>
                </sc-if>
              </div>
              <div class="sx-box" style="gap: 10px;">
                <div style="display: flex; justify-content: space-between; gap: 8px; flex-wrap: wrap;"><span class="sx-b">Tell the people affected: yes or no</span><span class="sb-muted">UK GDPR Art 34(1) and 34(3)</span></div>
                <span class="sb-sub">Tell them without undue delay where the breach is likely to be high risk to them. The 6 clients are told either way by their new consultant, as a courtesy, once the decision is made.</span>
                <span class="sb-sub">If yes, the people affected get email 9.4 "We need to tell you about a data incident", filled from this record and signed by the data protection lead (Collins), who also makes this decision. It is never sent automatically: Rachel Turner reviews the decision and approves the email first. <a class="sx-link" href="Messages.dc.html">Open email 9.4 (Messages and automations, board 82)</a></span>
                <sc-if value="{{tellOpen}}" hint-placeholder-val="{{ true }}">
                  <div style="display: flex; flex-direction: column; gap: 8px;">
                    ''' + subtabs('tellTabs', 'Tell the people affected', 2) + '''
                    <label class="sx-lbl" for="tell-ta">Reasons (kept in the breach record)</label>
                    <textarea id="tell-ta" class="sx-ta" value="{{tellR}}" onChange="{{onTellR}}" placeholder="For example: no sign the files left the managed laptop; low likelihood of harm, so not high risk."></textarea>
                    <sc-if value="{{tellErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">{{tellErrText}}</span></sc-if>
                    <div><button class="sb-btn b-pri" onClick="{{saveTell}}">Record the decision</button></div>
                  </div>
                </sc-if>
                <sc-if value="{{tellDone}}" hint-placeholder-val="{{ false }}">
                  <div class="{{tellBox}}"><span class="sx-b">{{tellHead}}</span><span class="sb-sub">{{tellNote}}</span><span class="sb-sub">Reasons: "{{tellR}}"</span><div><button class="sb-btn b-gh" onClick="{{undoTell}}">Change the decision</button></div></div>
                </sc-if>
              </div>
              <div style="display: flex; flex-direction: column;">
                <div style="display: flex; justify-content: space-between; gap: 8px; padding-bottom: 6px;"><span class="sx-b">Actions</span><span class="sb-muted">{{actCount}}</span></div>
                <sc-for list="{{acts}}" as="a" hint-placeholder-count="7">
                  <div style="display: flex; gap: 12px; align-items: flex-start; padding: 8px 0; border-top: 1px solid var(--cs-border-subtle);">
                    <label class="sx-chk" style="flex: 1; min-width: 0;"><input type="checkbox" checked="{{a.done}}" onChange="{{a.flip}}"><span style="display: flex; flex-direction: column;"><span>{{a.t}}</span><span class="sb-muted">{{a.who}}</span></span></label>
                    <span class="{{a.cls}}">{{a.state}}</span>
                  </div>
                </sc-for>
              </div>
            </div>
          </section>
          <div style="flex: 2 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
            <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="clk-h">
              <h2 id="clk-h" class="sb-h2">The 72-hour clock</h2>
              <span class="sx-big">{{hoursLeft}} left</span>
              <div class="bar" aria-hidden="true"><span class="{{clockBar}}"></span></div>
              <div class="sx-kv" style="grid-template-columns: 120px minmax(0, 1fr);">
                <span>Aware</span><span>Mon 2 Nov 06:00, when the nightly check flagged it</span>
                <span>Window ends</span><span class="sx-b">Thu 5 Nov 06:00</span>
                <span>Our target</span><span>Decide by Tue 3 Nov 12:00, to leave time to write the report well</span>
                <span>Shown at</span><span>Mon 2 Nov 09:20</span>
              </div>
              <span class="sb-muted">Source: UK GDPR Art 33(1). Without undue delay and, where feasible, within 72 hours of becoming aware. Clock hours, so weekends count. A late report must give the reasons.</span>
            </section>
            <section class="sb-card" aria-labelledby="tl-h">
              <div class="sb-head"><h2 id="tl-h" class="sb-h2">What happened, from the audit log</h2></div>
              <sc-for list="{{timeline}}" as="l" hint-placeholder-count="8">
                <div class="sb-row" style="align-items: flex-start; padding-top: 9px; padding-bottom: 9px;"><span class="sb-sub" style="flex: 0 0 106px;">{{l.t}}</span><span style="flex: 1; min-width: 0; font-size: 13px; line-height: 18px;">{{l.x}}</span></div>
              </sc-for>
            </section>
            <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="oi-h">
              <h2 id="oi-h" class="sb-h2">Other incidents since go-live</h2>
              <div class="sx-box"><div style="display: flex; justify-content: space-between; gap: 8px;"><span class="sx-b">Near miss, Wed 14 Oct</span><span class="sb-chip c-ok">Closed</span></div><span class="sb-sub">A draft weekly update had another client's document attached. The Thursday second-person check caught it and it was never sent. Not a breach; recorded as a near miss. Lesson: the Hub now checks that every attachment belongs to the client.</span></div>
              <span class="sb-muted">"Start breach assessment" is on every unusual activity alert and every concern staff report. "Mark as expected" needs a reason, and the other super admin when a leaver is involved.</span>
            </section>
          </div>
        </div>
      </sc-if>

      <sc-if value="{{isLog}}" hint-placeholder-val="{{ false }}">
        <div class="sx-ok" style="flex-direction: row; gap: 14px; align-items: center; flex-wrap: wrap;">
          <span class="sb-chip c-ok">Integrity check passed 06:00</span>
          <span style="flex: 1; min-width: 300px;" class="sb-sub">The chain of 4,812 entries since go-live on Thu 1 Oct is unbroken, and the daily copy is in write-once storage outside the Hub's own admin rights. Entries cannot be edited or deleted by anyone, super admins included. The log is kept for 6 years (proposed, for the data protection lead).</span>
        </div>
        <section class="sb-card" aria-labelledby="log-h">
          <div class="sb-head"><h2 id="log-h" class="sb-h2">Audit log</h2><div style="display: flex; gap: 8px; flex-wrap: wrap;"><input aria-label="Search the audit log" class="sx-in" style="width: 300px;" placeholder="Search a name, a client or an action" value="{{q}}" onChange="{{onQ}}"><button class="sb-btn b-gh" onClick="{{doExport}}">{{exportLabel}}</button></div></div>
          <div style="padding: 0 20px 12px; display: flex; flex-direction: column; gap: 8px;">
            ''' + subtabs('typeTabs', 'Event type', 9) + '''
            <div style="display: flex; gap: 16px; flex-wrap: wrap; align-items: center;">
              ''' + subtabs('personTabs', 'Person', 6) + '''
              ''' + subtabs('dayTabs', 'When', 3) + '''
            </div>
          </div>
          <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 0 0 128px;">When</span><span class="sb-th" style="flex: 0 0 130px;">Who</span><span class="sb-th" style="flex: 0 0 170px;">Event</span><span class="sb-th" style="flex: 0 0 170px;">Client</span><span class="sb-th" style="flex: 1;">What happened</span></div>
          <sc-for list="{{log}}" as="l" hint-placeholder-count="10">
            <div class="sb-row" style="align-items: flex-start; padding-top: 9px; padding-bottom: 9px;"><span class="sb-sub" style="flex: 0 0 128px;">{{l.at}}</span><span class="sx-b" style="flex: 0 0 130px; font-size: 13px;">{{l.who}}</span><span style="flex: 0 0 170px;"><span class="{{l.cls}}">{{l.ev}}</span></span><span class="sb-sub" style="flex: 0 0 170px;">{{l.client}}</span><span style="flex: 1; min-width: 0; font-size: 13px; line-height: 18px;">{{l.what}}</span></div>
          </sc-for>
          <sc-if value="{{noLog}}" hint-placeholder-val="{{ false }}"><div class="sb-row"><span class="sb-sub">Nothing matches. Try another word or filter.</span></div></sc-if>
          <div class="sb-row"><span class="sb-muted">{{logCount}}</span></div>
        </section>
        <div class="sx-cols">
          <section class="sb-card" style="flex: 3 1 560px; min-width: 0;" aria-labelledby="ar-h">
            <div class="sb-head"><h2 id="ar-h" class="sb-h2">Alert rules</h2><span class="sb-sub">Each alert opens as New, then Looking into it, Expected (with a reason) or Escalated to an incident</span></div>
            <sc-for list="{{rules}}" as="r" hint-placeholder-count="10">
              <div class="sb-row" style="align-items: flex-start;">
                <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">{{r.name}}</span><span class="sb-sub">{{r.th}}</span><span class="sb-muted">To: {{r.to}}. Last: {{r.last}}</span>
                  <sc-if value="{{r.isBulk}}" hint-placeholder-val="{{ false }}"><span style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap; padding-top: 4px;"><span class="{{bulkCls}}">{{bulkMode}}</span><sc-if value="{{bulkCan}}" hint-placeholder-val="{{ true }}"><button class="sb-btn b-sec" onClick="{{makeRealtime}}">Make it real time</button></sc-if></span></sc-if>
                </span>
                <sc-if value="{{r.locked}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-neutral">Locked: always on</span></sc-if>
                <button class="{{r.swCls}}" role="switch" aria-checked="{{r.aria}}" aria-label="{{r.swLabel}}" onClick="{{r.flip}}"><span></span></button>
              </div>
            </sc-for>
          </section>
          <div style="flex: 2 1 360px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
            <section class="sb-card" aria-labelledby="ra-h">
              <div class="sb-head"><h2 id="ra-h" class="sb-h2">Recent alerts</h2><span class="sb-sub">Both handled. "Mark as expected" always needs a reason</span></div>
              <sc-for list="{{alerts}}" as="a" hint-placeholder-count="2">
                <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px;">
                  <div style="display: flex; justify-content: space-between; gap: 8px;"><span class="sx-b">{{a.t}}</span><span class="{{a.cls}}">{{a.state}}</span></div>
                  <span class="sb-sub">{{a.x}}</span>
                </div>
              </sc-for>
            </section>
            <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="ev-h">
              <h2 id="ev-h" class="sb-h2">What the log records</h2>
              <sc-for list="{{evTypes}}" as="e" hint-placeholder-count="10">
                <div style="display: flex; flex-direction: column; gap: 4px;"><span class="sx-lbl">{{e.g}}</span><span style="font-size: 13px; line-height: 18px;">{{e.x}}</span></div>
              </sc-for>
              <span class="sb-muted">The client's privacy page reads from this same log, so what they see always matches.</span>
            </section>
            <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="ox-h">
              <h2 id="ox-h" class="sb-h2">Access outside the Hub</h2>
              <span class="sb-sub">Developers reach the live database only through just-in-time access, approved by a super admin and logged here: 0 sessions in the last 30 days. The automations tool, the AI prompt logs and the PDF tool keep their own logs, copied in every night (we check what each tool can export).</span>
            </section>
          </div>
        </div>
      </sc-if>

      <sc-if value="{{isVault}}" hint-placeholder-val="{{ false }}">
        <div class="sx-cols">
          <section class="sb-card sx-pad" style="flex: 3 1 560px; min-width: 0; padding-top: 18px;" aria-labelledby="vr-h">
            <h2 id="vr-h" class="sb-h2">Rules for every login</h2>
            <sc-for list="{{vRules}}" as="r" hint-placeholder-count="5">
              <div style="display: flex; gap: 10px; align-items: flex-start;"><span class="sb-chip c-neutral" style="flex: 0 0 auto;">Locked</span><span style="font-size: 14px; line-height: 20px;">{{r}}</span></div>
            </sc-for>
            <div class="sx-box" style="gap: 8px;">
              <span class="sx-b">Try it: Sunrise Homecare Ltd, CQC sign-in mailbox</span>
              <label class="sx-lbl" for="v-ta">Why do you need it? Needed to reveal and to copy</label>
              <textarea id="v-ta" class="sx-ta" value="{{vReason}}" onChange="{{onVReason}}" placeholder="For example: check the Notice of Proposal email from CQC"></textarea>
              <sc-if value="{{vErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Write a reason first. Copying needs one too.</span></sc-if>
              <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-gh" onClick="{{vCopy}}">Copy without showing</button><button class="sb-btn b-sec" onClick="{{vShow}}">Reveal for 30 seconds</button></div>
              <sc-if value="{{vDoneShow}}" hint-placeholder-val="{{ false }}"><div class="sx-ok"><span class="sx-b">{{vDoneText}}</span><span class="sb-sub">Logged with your reason. Priya sees "{{vDoneClient}}" on her privacy page.</span></div></sc-if>
            </div>
          </section>
          <section class="sb-card" style="flex: 2 1 380px; min-width: 0;" aria-labelledby="rp-h">
            <div class="sb-head"><h2 id="rp-h" class="sb-h2">Reveals and copies per person</h2><span class="sb-sub">Mon 26 Oct to Sun 1 Nov: {{revTotal}}</span></div>
            <sc-for list="{{reveals}}" as="r" hint-placeholder-count="6">
              <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 4px; padding-top: 8px; padding-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; gap: 8px;"><span class="sx-b" style="font-size: 13px;">{{r.who}}</span><span class="{{r.cls}}">{{r.n}}</span></div>
                <div class="bar" aria-hidden="true"><span class="{{r.w}}"></span></div>
                <span class="sb-muted">{{r.note}}</span>
              </div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">Alert threshold: {{revLimit}} in 7 days per person (proposed). Nobody went over it. The mailbox connection should bring these numbers down.</span></div>
          </section>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
          <sc-for list="{{methods}}" as="m" hint-placeholder-count="4">
            <div class="sb-card sb-kpi"><span class="sb-sub">{{m.k}}</span><span class="sb-kv">{{m.v}}</span><span class="{{m.cls}}" style="white-space: normal; align-self: flex-start;">{{m.note}}</span></div>
          </sc-for>
        </div>
        <section class="sb-card" aria-labelledby="ve-h">
          <div class="sb-head"><h2 id="ve-h" class="sb-h2">Vault entries</h2>''' + subtabs('vmTabs', 'Access method', 5) + '''</div>
          <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 2 1 200px;">Client and system</span><span class="sb-th" style="flex: 0 0 150px;">Access method</span><span class="sb-th" style="flex: 1 1 160px;">Written authority</span><span class="sb-th" style="flex: 2 1 220px;">Last reveal or copy</span><span class="sb-th" style="flex: 0 0 110px;">Review</span><span class="sb-th" style="flex: 0 0 170px;">State</span></div>
          <sc-for list="{{entries}}" as="e" hint-placeholder-count="10">
            <div class="sb-row" style="align-items: flex-start;">
              <span style="flex: 2 1 200px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">{{e.client}}</span><span class="sb-sub">{{e.sys}}</span><sc-if value="{{e.code}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-info" style="align-self: flex-start;">Client mobile code on</span></sc-if></span>
              <span style="flex: 0 0 150px;"><span class="{{e.mCls}}">{{e.m}}</span></span>
              <span class="sb-sub" style="flex: 1 1 160px; min-width: 0;">{{e.auth}}</span>
              <span style="flex: 2 1 220px; min-width: 0; font-size: 13px; line-height: 18px;">{{e.last}}</span>
              <span class="sb-sub" style="flex: 0 0 110px;">{{e.rev}}</span>
              <span style="flex: 0 0 170px; display: flex; flex-direction: column; gap: 6px; align-items: flex-start;"><span class="{{e.sCls}}" style="white-space: normal;">{{e.state}}</span><sc-if value="{{e.hasAct}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" onClick="{{e.act}}">{{e.actLabel}}</button></sc-if></span>
            </div>
          </sc-for>
          <div class="sb-row"><span class="sb-muted">{{entryCount}} Every entry names its access method, the signed authority, a review date and the last rotation. Clients add their own logins (board 27); staff typing one in is a logged fallback.</span></div>
        </section>
        <div class="sx-cols">
          <section class="sb-card" style="flex: 3 1 560px; min-width: 0;" aria-labelledby="hb-h">
            <div class="sb-head"><h2 id="hb-h" class="sb-h2">Hand-back at the end of the work</h2><span class="sb-sub">Requested, access removed, connection and tokens revoked, entry deleted, client confirmed the password changed (or declined, recorded)</span></div>
            <sc-for list="{{handback}}" as="h" hint-placeholder-count="3">
              <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px;">
                <div style="display: flex; justify-content: space-between; gap: 8px; flex-wrap: wrap;"><span class="sx-b">{{h.client}}</span><span class="{{h.cls}}">{{h.state}}</span></div>
                <div class="sx-step"><sc-for list="{{h.steps}}" as="st" hint-placeholder-count="5"><span class="{{st.cls}}">{{st.label}}</span></sc-for></div>
                <sc-if value="{{h.canNext}}" hint-placeholder-val="{{ false }}"><div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-sec" onClick="{{h.next}}">{{h.nextLabel}}</button><sc-if value="{{h.canDecline}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" onClick="{{h.decline}}">Client declined: record it</button></sc-if></div></sc-if>
              </div>
            </sc-for>
          </section>
          <section class="sb-card" style="flex: 2 1 360px; min-width: 0;" aria-labelledby="lp-h">
            <div class="sb-head"><h2 id="lp-h" class="sb-h2">Old places logins were kept</h2><span class="sb-sub">One-time clear-out, owner Collins, by Fri 13 Nov</span></div>
            <sc-for list="{{purge}}" as="p" hint-placeholder-count="3">
              <div class="sb-row" style="align-items: flex-start;"><label class="sx-chk" style="flex: 1; min-width: 0;"><input type="checkbox" checked="{{p.done}}" onChange="{{p.flip}}"><span style="display: flex; flex-direction: column;"><span>{{p.t}}</span><span class="sb-muted">{{p.note}}</span></span></label><span class="{{p.cls}}">{{p.state}}</span></div>
            </sc-for>
          </section>
        </div>
      </sc-if>

      <sc-if value="{{isElev}}" hint-placeholder-val="{{ false }}">
        <div class="sx-cols">
          <section class="sb-card" style="flex: 1 1 460px; min-width: 0;" aria-labelledby="cv-h">
            <div class="sb-head"><h2 id="cv-h" class="sb-h2">Cover delegation: planned leave</h2><span class="{{covCls}}">{{covState}}</span></div>
            <div class="sx-pad">
              <span class="sb-sub">When leave is booked, a manager approves cover for named clients and dates, including vault reveal for those clients. It ends by itself.</span>
              <div class="sx-kv" style="grid-template-columns: 130px minmax(0, 1fr);">
                <span>Who is away</span><span>Olu, on leave Mon 2 to Fri 6 Nov</span>
                <span>Covering</span><span class="sx-b">Daniel Mensah</span>
                <span>Clients</span><span>Riverside Homecare, Greenway Support, Lagan View Care, Willow Bank Supported Living (4)</span>
                <span>Vault</span><span>Reveal included for those 4 clients only</span>
                <span>Booked</span><span>Collins, Wed 28 Oct</span>
                <span>Approved</span><span>Rachel Turner, Fri 30 Oct</span>
                <span>Ends</span><span class="sx-b">{{covEnds}}</span>
              </div>
              <div class="sx-box"><span class="sx-lbl">Vault use under this cover</span><sc-for list="{{covUse}}" as="u" hint-placeholder-count="2"><span style="font-size: 13px; line-height: 18px;">{{u}}</span></sc-for></div>
              <span class="sb-muted">Each of the 4 clients sees "Daniel Mensah is covering for Olu this week" on their privacy page, with every look he takes.</span>
              <sc-if value="{{covActive}}" hint-placeholder-val="{{ true }}">
                <label class="sx-lbl" for="cv-ta">Reason to end it early</label>
                <textarea id="cv-ta" class="sx-ta" value="{{coverR}}" onChange="{{onCoverR}}" placeholder="For example: Olu came back early"></textarea>
                <sc-if value="{{coverErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Write a reason first.</span></sc-if>
                <div><button class="sb-btn b-gh" onClick="{{endCover}}">End the cover now</button></div>
              </sc-if>
            </div>
          </section>
          <section class="sb-card" style="flex: 1 1 460px; min-width: 0;" aria-labelledby="bg-h">
            <div class="sb-head"><h2 id="bg-h" class="sb-h2">Break-glass: emergencies only</h2><span class="sb-chip c-ok">None in the last 30 days</span></div>
            <div class="sx-pad">
              <ol class="sx-ol">
                <sc-for list="{{bgRules}}" as="r" hint-placeholder-count="5"><li>{{r}}</li></sc-for>
              </ol>
              <span class="sb-muted">States: Requested, Active, Ended, Reviewed, or Misuse found (which opens an incident). None used since go-live on Thu 1 Oct; planned leave always uses cover instead.</span>
              <div class="sx-box" style="gap: 8px;">
                <span class="sx-b">Ask for break-glass</span>
                <span class="sx-lbl">Client</span>
                ''' + subtabs('bgTabs', 'Client', 3) + '''
                <label class="sx-lbl" for="bg-ta">What is the emergency?</label>
                <textarea id="bg-ta" class="sx-ta" value="{{bgR}}" onChange="{{onBgR}}" placeholder="For example: CQC needs a reply today and the case owner cannot be reached"></textarea>
                <sc-if value="{{bgErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Choose a client and describe the emergency.</span></sc-if>
                <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-sec" onClick="{{bgAsk}}">Ask Rachel Turner to approve</button><button class="sb-btn b-gh" onClick="{{bgSelf}}">No one can be reached: self-authorise</button></div>
                <sc-if value="{{bgShow}}" hint-placeholder-val="{{ false }}"><div class="sx-amb"><span class="sx-b">{{bgHead}}</span><span class="sb-sub">{{bgNote}}</span></div></sc-if>
              </div>
            </div>
          </section>
        </div>
        <div class="sx-cols">
          <section class="sb-card" style="flex: 3 1 560px; min-width: 0;" aria-labelledby="va-h">
            <div class="sb-head"><h2 id="va-h" class="sb-h2">View-as sessions, last 30 days</h2><a class="sx-link" href="ViewAs.dc.html">Open View as (board 88)</a></div>
            <sc-for list="{{viewas}}" as="v" hint-placeholder-count="3">
              <div class="sb-row" style="align-items: flex-start;"><span class="sb-sub" style="flex: 0 0 120px;">{{v.at}}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">{{v.who}}</span><span class="sb-sub">{{v.x}}</span></span><span class="sb-chip c-info">Read only</span></div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">View as is read only, with a banner, and only for clients the person may already see. The client sees an entry on their privacy page for each page that showed their information.</span></div>
          </section>
          <section class="sb-card sx-pad" style="flex: 2 1 360px; min-width: 0; padding-top: 18px;" aria-labelledby="ja-h">
            <h2 id="ja-h" class="sb-h2">Developer and supplier access</h2>
            <div class="sx-kv" style="grid-template-columns: 130px minmax(0, 1fr);">
              <span>Live database</span><span>Just in time only, approved by a super admin, ends by itself</span>
              <span>Last 30 days</span><span>0 sessions</span>
              <span>Last session</span><span>Wed 30 Sep, the go-live data import, 2 hours, approved by Collins</span>
              <span>Hosting console</span><span>2 named accounts, two-step on</span>
            </div>
          </section>
        </div>
      </sc-if>

      <sc-if value="{{isSign}}" hint-placeholder-val="{{ false }}">
        <div class="sx-cols">
          <section class="sb-card" style="flex: 1 1 460px; min-width: 0;" aria-labelledby="sp-h">
            <div class="sb-head"><h2 id="sp-h" class="sb-h2">Staff sign-in</h2><span class="sb-sub">Through Google Workspace</span></div>
            <div class="sx-pad">
              <div class="sx-kv">
                <span>Idle time-out</span><span class="sx-b">{{idle}}</span>
                <span>Absolute time-out</span><span>10 hours, then sign in again</span>
                <span>Sign in again before</span><span>Opening the vault, any export, and approving a decision</span>
                <span>Two-step</span><span>{{twoStep}}</span>
                <span>Read from Google</span><span>Mon 2 Nov 06:00. If Google stops enforcing two-step, this screen and System health turn red.</span>
              </div>
              <div class="{{femiBox}}"><span class="sx-b">{{femiHead}}</span><span class="sb-sub">{{femiNote}}</span><sc-if value="{{femiAsk}}" hint-placeholder-val="{{ true }}"><div><button class="sb-btn b-sec" onClick="{{askFemi}}">Ask Femi to switch</button></div></sc-if></div>
              <span class="sb-muted">The idle time-out is set once in Rules and promises (board 80) and read here.</span>
            </div>
          </section>
          <section class="sb-card" style="flex: 1 1 460px; min-width: 0;" aria-labelledby="cp-h">
            <div class="sb-head"><h2 id="cp-h" class="sb-h2">Client sign-in</h2><span class="sb-sub">Magic link, no password</span></div>
            <div class="sx-pad">
              <div class="sx-kv">
                <span>Known device</span><span class="sx-b">{{deviceDays}}</span>
                <span>Mobile code</span><span>When Care Sync holds the login to the client's sign-in mailbox, a code goes to the client's mobile on a new device and before signing, approving, downloading everything or changing contact details.</span>
                <span>Applies today</span><span>9 clients whose sign-in mailbox login is in the vault</span>
                <span>Mailbox connection</span><span>Never files Hub sign-in or e-signature emails (locked)</span>
                <span>E-signatures</span><span>Signer check by text message in DocuSeal: we check what DocuSeal supports</span>
                <span>Alert</span><span>A client signing in from a Care Sync device or network</span>
              </div>
              <span class="sb-muted">Client screens that must match: Sign in, Account, Security page and Sign (the code step).</span>
            </div>
          </section>
        </div>
        <section class="sb-card" aria-labelledby="dv-h">
          <div class="sb-head"><h2 id="dv-h" class="sb-h2">Devices</h2>''' + subtabs('dvTabs', 'Devices for', 2) + '''</div>
          <sc-if value="{{isStaffDev}}" hint-placeholder-val="{{ true }}">
            <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 0 0 130px;">Person</span><span class="sb-th" style="flex: 2 1 200px;">Device</span><span class="sb-th" style="flex: 0 0 90px;">Owned by</span><span class="sb-th" style="flex: 1 1 160px;">First and last seen</span><span class="sb-th" style="flex: 0 0 210px;">State</span><span class="sb-th" style="flex: 0 0 150px;"></span></div>
            <sc-for list="{{devices}}" as="d" hint-placeholder-count="9">
              <div class="sb-row" style="align-items: flex-start;">
                <span class="sx-b" style="flex: 0 0 130px; font-size: 13px;">{{d.who}}</span>
                <span style="flex: 2 1 200px; min-width: 0; display: flex; flex-direction: column;"><span>{{d.dev}}</span><span class="sb-muted">{{d.place}}</span></span>
                <span class="sb-sub" style="flex: 0 0 90px;">{{d.kind}}</span>
                <span class="sb-sub" style="flex: 1 1 160px; min-width: 0;">{{d.seen}}</span>
                <span style="flex: 0 0 210px;"><span class="{{d.cls}}" style="white-space: normal;">{{d.state}}</span></span>
                <span style="flex: 0 0 150px; display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end;"><sc-if value="{{d.canTrust}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-sec" onClick="{{d.trust}}">Trust</button></sc-if><sc-if value="{{d.canRevoke}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" onClick="{{d.revoke}}">Revoke</button></sc-if></span>
              </div>
            </sc-for>
            <div class="sb-row" style="gap: 8px; flex-wrap: wrap;"><span class="sb-sub" style="flex: 1; min-width: 280px;">Sign a person out of every device, the Hub and Google Workspace together. Suspending someone does this too (People and access, board 83).</span>
              <sc-for list="{{outBtns}}" as="o" hint-placeholder-count="3"><button class="sb-btn b-gh" onClick="{{o.go}}">{{o.label}}</button></sc-for>
            </div>
          </sc-if>
          <sc-if value="{{isClientDev}}" hint-placeholder-val="{{ false }}">
            <div class="sb-row" style="align-items: flex-start;"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">Sunrise Homecare Ltd: Priya Shah</span><span class="sb-sub">Sign-in mailbox login is in the vault, so the mobile code is on</span></span><button class="sb-btn b-sec" onClick="{{clientOutGo}}">{{clientOutLabel}}</button></div>
            <sc-for list="{{cdev}}" as="d" hint-placeholder-count="2">
              <div class="sb-row" style="align-items: flex-start;"><span style="flex: 2 1 220px;">{{d.dev}}</span><span class="sb-sub" style="flex: 2 1 260px;">{{d.seen}}</span><span class="{{d.cls}}">{{d.state}}</span></div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">The client can do the same from Account ("Your devices"). Staff use this when a client reports a lost phone.</span></div>
          </sc-if>
        </section>
        <section class="sb-card" aria-labelledby="si-h">
          <div class="sb-head"><h2 id="si-h" class="sb-h2">Recent sign-ins worth a look</h2><span class="sb-sub">Everything else is in the audit log</span></div>
          <sc-for list="{{signins}}" as="s" hint-placeholder-count="4">
            <div class="sb-row" style="align-items: flex-start;"><span class="sb-sub" style="flex: 0 0 130px;">{{s.at}}</span><span class="sx-b" style="flex: 0 0 130px; font-size: 13px;">{{s.who}}</span><span style="flex: 1; min-width: 0; font-size: 13px; line-height: 18px;">{{s.x}}</span><span class="{{s.cls}}">{{s.state}}</span></div>
          </sc-for>
        </section>
      </sc-if>

      <sc-if value="{{isRes}}" hint-placeholder-val="{{ false }}">
        <div class="sx-col3">
          <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="bk-h">
            <div style="display: flex; justify-content: space-between; gap: 8px;"><h2 id="bk-h" class="sb-h2">Backups</h2><span class="sb-chip c-ok">OK</span></div>
            <div class="sx-kv" style="grid-template-columns: 96px minmax(0, 1fr);">
              <span>Last run</span><span>Mon 2 Nov 02:00, done in 14 minutes</span>
              <span>What</span><span>The database every night, files kept as versions</span>
              <span>Where</span><span>UK (London) region, in a separate account</span>
              <span>Encrypted</span><span>Yes, with its own key</span>
              <span>Kept</span><span>35 days (proposed, for the data protection lead), so deleted items leave the backups 35 days after a deletion run</span>
            </div>
          </section>
          <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="rt-h">
            <div style="display: flex; justify-content: space-between; gap: 8px;"><h2 id="rt-h" class="sb-h2">Restore tests</h2><span class="sb-chip c-ok">Passed</span></div>
            <div class="sx-kv" style="grid-template-columns: 96px minmax(0, 1fr);">
              <span>Last test</span><span class="sx-b">Tue 13 Oct, passed</span>
              <span>Restored</span><span>The whole database and 200 sample files, to a test copy</span>
              <span>Took</span><span>48 minutes, against a target of 4 hours (proposed)</span>
              <span>Data loss</span><span>At most since the last nightly backup, target 24 hours (proposed)</span>
              <span>By</span><span>Collins, with the developer</span>
              <span>Next due</span><span>By Mon 11 Jan (every 90 days; overdue after that)</span>
            </div>
            <span class="sb-muted">Before that: Tue 29 Sep, before go-live, passed.</span>
          </section>
          <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="ky-h">
            <h2 id="ky-h" class="sb-h2">Keys</h2>
            <sc-for list="{{keys}}" as="k" hint-placeholder-count="5">
              <div style="display: flex; flex-direction: column; gap: 2px; padding-bottom: 6px; border-bottom: 1px solid var(--cs-border-subtle);"><span class="sx-b" style="font-size: 14px;">{{k.k}}</span><span class="sb-muted">{{k.x}}</span></div>
            </sc-for>
            <span class="sb-muted">No super admin can export the vault or field keys. Integration keys are masked on System health (board 86).</span>
          </section>
        </div>
        <div class="sx-cols">
          <section class="sb-card" style="flex: 1 1 100%; min-width: 0;" aria-labelledby="ct-h">
            <div class="sb-head"><h2 id="ct-h" class="sb-h2">Contacts in an incident</h2></div>
            <sc-for list="{{contacts}}" as="c" hint-placeholder-count="9">
              <div class="sb-row" style="align-items: flex-start;"><span class="sb-sub" style="flex: 0 0 220px;">{{c.role}}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">{{c.who}}</span><span class="sb-sub">{{c.how}}</span></span><sc-if value="{{c.check}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-warn">check before go-live</span></sc-if></div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">Yearly practice run (tabletop exercise): not yet held since go-live. Booked for Thu 10 Dec, 10:00, Collins and Rachel Turner.</span></div>
          </section>
          <section class="sb-card" style="flex: 1 1 100%; min-width: 0;" aria-labelledby="rb-h">
            <div class="sb-head"><h2 id="rb-h" class="sb-h2">Runbook: one page</h2><span class="sb-sub">Printed and kept with the contacts</span></div>
            <div class="sx-col3" style="padding: 0 20px 18px;">
              <sc-for list="{{runbook}}" as="r" hint-placeholder-count="3">
                <div class="sx-box" style="gap: 8px;"><span class="sx-b">{{r.h}}</span><ol class="sx-ol" style="font-size: 13px; line-height: 18px;"><sc-for list="{{r.s}}" as="x" hint-placeholder-count="5"><li>{{x}}</li></sc-for></ol></div>
              </sc-for>
            </div>
          </section>
        </div>
      </sc-if>
'''

SEC_S = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { t: 'inc', rep: false, repText: '', repErr: false, repSent: false, like: 'low', sev: 'high',
      ico: '', icoR: '', icoErr: false, icoSaved: false, tell: '', tellR: '', tellErr: false, tellSaved: false, acts: { a1: true, a2: true },
      q: '', lt: 'all', lp: 'all', ld: 't', exported: false, sw: {}, realtime: false, al: {}, alR: {}, alErr: {},
      vm: 'all', vReason: '', vErr: false, vDone: '', hb: { fern: 6, north: 4, blue: 2 }, purge: { p1: true }, wbAsked: false, rvAsked: false,
      covEnded: false, coverR: '', coverErr: false, bgC: '', bgR: '', bgErr: false, bgSent: '',
      dv: 'staff', dev: {}, outAll: {}, femi: false, clientOut: false };
  }
  renderVals() {
    const s = this.state;
''' + JSHELP + r'''
    const T = [['inc', 'Incidents (1 open)'], ['log', 'Audit log and alerts'], ['vault', 'Vault'], ['elev', 'Elevated access'], ['sign', 'Sign-in and devices'], ['res', 'Resilience and contacts']];
    // 72-hour clock, shown at Mon 2 Nov 09:00
    const aware = new Date(2026, 10, 2, 6, 0), ends = new Date(2026, 10, 5, 6, 0), now = new Date(2026, 10, 2, 9, 20);
    const minsLeft = Math.round((ends - now) / 60000);
    const hoursLeft = Math.floor(minsLeft / 60) + ' h ' + (minsLeft % 60) + ' min';
    const used = Math.round(((now - aware) / (ends - aware)) * 20) * 5;
    // Incident decisions
    const icoDone = s.icoSaved, tellDone = s.tellSaved;
    const icoYes = s.ico === 'yes', tellYes = s.tell === 'yes';
    let incState = 'Assessing', incK = 'warn';
    if (icoDone && icoYes) { incState = 'Reported to the ICO'; incK = 'info'; }
    if (icoDone && !icoYes) { incState = 'Not reportable, reason kept'; incK = 'neutral'; }
    if (icoDone && tellDone && tellYes) { incState = 'People told'; incK = 'info'; }
    const stepNames = ['Reported', 'Assessing', icoDone ? (icoYes ? 'Reported to the ICO' : 'Not reportable, reason kept') : 'Reported to the ICO, or not reportable', 'People told, if needed', 'Closed'];
    const cur = !icoDone ? 1 : (tellDone ? 3 : 2);
    const steps = stepNames.map((label, i) => ({ label, cls: i < cur ? 'st-done' : (i === cur ? 'st-now' : 'st-next') }));
    const facts = [
      ['Reported by', 'The Hub: unusual activity alert, Mon 2 Nov 06:00'],
      ['Aware since', 'Mon 2 Nov 06:00 (the clock starts here)'],
      ['Person involved', 'Sam Patel, consultant, suspended since 08:25 pending this review, leaving Fri 6 Nov'],
      ['What happened', '38 client documents downloaded one by one on Sun 1 Nov, 21:40 to 22:05 (usual: under 5 a day), from the files of Sam\'s 6 clients, onto Care Sync laptop CS-LT-07 at home'],
      ['Data', '9 CVs and references; 5 identity documents (2 passports, 3 proofs of address); 2 DBS certificate copies (criminal offence data); 22 draft policies and plans (names only)'],
      ['People and records', 'About 11 people (directors and proposed managers), 38 records'],
      ['Clients', 'Kingsway Care, Cedar Lodge Care, Rosehill Homecare, Thornbury Living, Hollybush Care, Bramley Support'],
      ['Our role', 'Controller (we check this with the data protection lead)'],
      ['Supplier involved', 'None'],
      ['Led by', 'Collins, data protection lead, since 08:10. Rachel Turner reviews the decisions (second pair of eyes)']
    ].map(([k, v]) => ({ k, v }));
    const contain = [['06:01', 'Sam\'s downloads paused by the Hub, automatically'], ['08:25', 'Hub and Google Workspace access suspended pending the review; 2 devices signed out, phone work data wiped'], ['08:30', 'Legal hold on Sam\'s account and the records of the 38 documents (Data and privacy, board 85)'], ['08:40', 'Sam asked to hand laptop CS-LT-07 to Rachel at 14:00 for a check']].map(([t, x]) => ({ t, x }));
    const LV = [['low', 'Low'], ['med', 'Medium'], ['high', 'High']];
    const likeTabs = LV.map(([k, l]) => ({ label: l, on: s.like === k, off: s.like !== k, pick: () => this.setState({ like: k }) }));
    const sevTabs = LV.map(([k, l]) => ({ label: l, on: s.sev === k, off: s.sev !== k, pick: () => this.setState({ sev: k }) }));
    const score = { low: 1, med: 2, high: 3 };
    const sc = score[s.like] * score[s.sev];
    const riskText = (sc >= 6 ? 'Likely high risk: report to the ICO and tell the people affected.' : (sc >= 3 ? 'A risk to people is possible: a report to the ICO is likely needed unless the checks show the files stayed on the managed laptop.' : 'Unlikely to result in a risk: record the reasons and keep the record.')) + ' Today: the files went to a managed, encrypted company laptop and nothing yet shows they were shared. Severity would be high if they were, because of the identity and DBS documents. Keep assessing until the laptop and Google checks at 12:00 and 14:00.';
    const icoTabs = [['yes', 'Yes, report to the ICO'], ['no', 'No, not reportable']].map(([k, l]) => ({ label: l, on: s.ico === k, off: s.ico !== k, pick: () => this.setState({ ico: k, icoErr: false }) }));
    const tellTabs = [['yes', 'Yes, tell them'], ['no', 'No, not high risk']].map(([k, l]) => ({ label: l, on: s.tell === k, off: s.tell !== k, pick: () => this.setState({ tell: k, tellErr: false }) }));
    const A = [
      ['a1', 'List the 38 documents and the people in them', 'Collins, done 08:50'],
      ['a2', 'Speak to Sam Patel', 'Rachel Turner, done 08:40: Sam says they were handover copies'],
      ['a3', 'Check Google Workspace for sharing, forwarding or uploads outside Care Sync', 'Collins (Google admin), by 12:00 today'],
      ['a4', 'Check laptop CS-LT-07 and confirm any copies are deleted', 'Rachel Turner, today 14:00'],
      ['a5', 'Decide on the ICO report, with reasons', 'Collins (data protection lead), reviewed by Rachel Turner, by Tue 3 Nov 12:00'],
      ['a6', 'If people must be told: email 9.4, approved by Rachel Turner (Messages and automations, board 82). The 6 clients hear from their new consultants either way', 'Collins signs it, Rachel Turner approves it, after the decision'],
      ['a7', 'Lesson: make bulk download alerts real time, not nightly', 'Collins, by Fri 13 Nov']
    ];
    const acts = A.map(([id, t, who]) => { const done = !!s.acts[id]; return { t, who, done, state: done ? 'Done' : 'To do', cls: ch(done ? 'ok' : 'warn'), flip: () => this.setState({ acts: up(s.acts, id, !done) }) }; });
    const actDone = acts.filter(a => a.done).length;
    const timeline = [
      ['Sun 1 Nov 21:38', 'Sam Patel signed in from home on laptop CS-LT-07 (known device)'],
      ['21:40 to 22:05', '38 single downloads from 6 clients\' files'],
      ['Mon 2 Nov 06:00', 'Nightly check flagged it. Both super admins and the data protection lead told'],
      ['06:01', 'The Hub paused Sam\'s downloads'],
      ['08:10', 'Collins, the data protection lead, started the assessment'],
      ['08:25', 'Rachel suspended Sam\'s access pending the review'],
      ['08:30', 'Legal hold placed'],
      ['08:40', 'Rachel spoke to Sam by phone'],
      ['08:45', 'Rachel exported Sam\'s audit entries for the record (logged)']
    ].map(([t, x]) => ({ t, x }));

    // Audit log
    const L = [
      ['Mon 2 Nov 09:02', 't', 'Collins', 'elev', 'View-as ended', 'Harbour Lane Care Ltd', 'ended the view as Amara saw it on Fri 30 Oct, after 12 minutes'],
      ['Mon 2 Nov 08:52', 't', 'Daniel Mensah', 'vault', 'Vault revealed', 'Greenway Support Ltd', 'revealed the shared document folder login, reason "find the 3 waiting documents". Under Olu\'s cover'],
      ['Mon 2 Nov 08:50', 't', 'Collins', 'elev', 'View-as started', 'Harbour Lane Care Ltd', 'viewed the Hub as Amara saw it on Fri 30 Oct, reason "Complaint check C-001". Read only'],
      ['Mon 2 Nov 08:45', 't', 'Rachel Turner', 'exp', 'Audit log exported', '', 'exported Sam Patel\'s audit entries, 1 Oct to 2 Nov (212 rows), for incident 2026-01. Link expires 17:00'],
      ['Mon 2 Nov 08:40', 't', 'Daniel Mensah', 'vault', 'Vault revealed', 'Lagan View Care Ltd', 'revealed the RQIA Web Portal login, reason "check for messages from RQIA". Under Olu\'s cover'],
      ['Mon 2 Nov 08:40', 't', 'Rachel Turner', 'dp', 'Incident step', '', 'spoke to Sam Patel by phone: Sam says the files were handover copies. Laptop due back at 14:00'],
      ['Mon 2 Nov 08:15', 't', 'Rachel Turner', 'dp', 'Alert looked at', '', 'marked Femi Ade\'s new laptop alert as looked at: two-step passed, only the Xero sync page opened. Not an incident'],
      ['Mon 2 Nov 08:30', 't', 'Rachel Turner', 'dp', 'Legal hold placed', '', 'placed a legal hold on Sam Patel\'s account and the records of the 38 documents, reason "incident 2026-01"'],
      ['Mon 2 Nov 08:25', 't', 'Rachel Turner', 'acc', 'Access suspended', '', 'suspended Sam Patel\'s Hub and Google Workspace access pending the incident review; 2 devices signed out'],
      ['Mon 2 Nov 08:10', 't', 'Collins', 'dp', 'Incident step', '', 'started the breach assessment for incident 2026-01 as data protection lead; Sam Patel\'s downloads stay paused'],
      ['Mon 2 Nov 06:00', 't', 'The Hub', 'dp', 'Alert', '', 'flagged unusual activity: Sam Patel downloaded 38 client documents on Sun 1 Nov from 21:40 (usual: under 5 a day)'],
      ['Mon 2 Nov 06:00', 't', 'The Hub', 'chg', 'Integrity check', '', 'checked the audit log chain: passed, 4,812 entries'],
      ['Mon 2 Nov 06:00', 't', 'The Hub', 'dp', 'Deletion run notice', '', 'gave 7 days\' notice of the deletion run on Mon 9 Nov: 14 identity documents, legal hold check clear'],
      ['Sun 1 Nov 22:05', 'w', 'Sam Patel', 'doc', 'Document downloaded', 'Bramley Support Ltd', 'downloaded the 38th document in 25 minutes (a DBS certificate copy)'],
      ['Sun 1 Nov 21:40', 'w', 'Sam Patel', 'doc', 'Document downloaded', 'Kingsway Care Ltd', 'downloaded the first of 38 documents from 6 clients\' files, on laptop CS-LT-07'],
      ['Sun 1 Nov 21:38', 'w', 'Sam Patel', 'sign', 'Sign-in success', '', 'signed in from home on laptop CS-LT-07 (known device)'],
      ['Sun 1 Nov 22:15', 'w', 'Femi Ade', 'sign', 'Sign-in success', '', 'signed in on a new laptop, two-step passed; opened only the Xero sync page. Alert raised'],
      ['Fri 30 Oct 16:40', 'w', 'Rachel Turner', 'acc', 'Cover approved', '', 'approved cover: Daniel Mensah covers Olu\'s 4 clients, Mon 2 to Fri 6 Nov 17:30, vault reveal included'],
      ['Fri 30 Oct 15:20', 'w', 'Daniel Mensah', 'vault', 'Vault revealed', 'Oakleaf Living Ltd', 'revealed the website login, reason "update the services page"'],
      ['Fri 30 Oct 14:05', 'w', 'Daniel Mensah', 'elev', 'View-as started', 'Harbour Lane Care Ltd', 'viewed the Hub as Amara sees it, reason "answer her question about the home office". Read only, 6 minutes'],
      ['Fri 30 Oct 14:05', 'w', 'Daniel Mensah', 'send', 'Sent as the client', 'Elm Tree Care Ltd', 'sent CQC the interview availability from Femi Adebayo\'s mailbox, approved by Femi Adebayo'],
      ['Fri 30 Oct 11:15', 'w', 'Daniel Mensah', 'send', 'AI request', 'Sunrise Homecare Ltd', 'asked the drafting assistant to check the Notice of Proposal reply against the notice; no logins or ID numbers sent'],
      ['Thu 29 Oct 11:10', 'w', 'Daniel Mensah', 'vault', 'Vault copied', 'Harbour Lane Care Ltd', 'copied the business email login without showing it, reason "sign in to check the CQC filter works"'],
      ['Thu 29 Oct 11:05', 'w', 'Grace', 'chg', 'Form version saved', '', 'saved draft v8 of the CQC onboarding form'],
      ['Thu 29 Oct 10:12', 'w', 'Daniel Mensah', 'elev', 'View-as started', 'Bright Path Care Ltd', 'viewed the Hub as Joy sees it, reason "check what Joy sees before session 2". Read only, 4 minutes'],
      ['Thu 29 Oct 09:40', 'w', 'Daniel Mensah', 'vault', 'Vault revealed', 'Harbour Lane Care Ltd', 'revealed the business email login for 30 seconds, reason "set up the CQC filter"'],
      ['Wed 28 Oct 14:20', 'w', 'Collins', 'dp', 'Rights request step', '', 'logged a request from a former referee asking what we hold about them (received by email)'],
      ['Wed 28 Oct 09:00', 'w', 'Collins', 'acc', 'Cover booked', '', 'booked Olu\'s leave, Mon 2 to Fri 6 Nov, and asked for Daniel Mensah to cover 4 clients'],
      ['Tue 27 Oct 14:30', 'w', 'Collins', 'acc', 'Leaver started', '', 'started offboarding for Sam Patel, last day Fri 6 Nov'],
      ['Thu 8 Oct 10:00', 'm', 'Collins', 'chg', 'Integration key change', '', 'rotated the Stripe key; the old key was revoked']
    ];
    const GRP = { sign: ['Sign-in', 'c-neutral'], doc: ['Documents', 'c-info'], vault: ['Vault', 'c-brand'], exp: ['Exports', 'c-warn'], elev: ['Access and elevated', 'c-info'], acc: ['Access and elevated', 'c-neutral'], chg: ['Changes', 'c-neutral'], dp: ['Data protection', 'c-warn'], send: ['Sending and AI', 'c-brand'] };
    const extraLog = [];
    if (s.exported) extraLog.push(['Mon 2 Nov 09:20', 't', 'Collins', 'exp', 'Audit log exported', '', 'exported ' + 'the filtered audit log (this view). Link expires in 24 hours']);
    if (s.realtime) extraLog.push(['Mon 2 Nov 09:20', 't', 'Collins', 'chg', 'Alert rule changed', '', 'made the bulk download alert real time']);
    if (s.vDone) extraLog.push(['Mon 2 Nov 09:20', 't', 'Collins', 'vault', s.vDone === 'copy' ? 'Vault copied' : 'Vault revealed', 'Sunrise Homecare Ltd', (s.vDone === 'copy' ? 'copied without showing' : 'revealed for 30 seconds') + ' the CQC sign-in mailbox login, reason "' + s.vReason.trim() + '"']);
    const ALL = extraLog.concat(L);
    const TT = [['all', 'All'], ['sign', 'Sign-in'], ['doc', 'Documents'], ['vault', 'Vault'], ['exp', 'Exports'], ['elev', 'Access and elevated'], ['chg', 'Changes'], ['dp', 'Data protection'], ['send', 'Sending and AI']];
    const inType = l => s.lt === 'all' || l[3] === s.lt || (s.lt === 'elev' && l[3] === 'acc');
    const PP = [['all', 'Everyone'], ['Sam Patel', 'Sam Patel'], ['Daniel Mensah', 'Daniel Mensah'], ['Rachel Turner', 'Rachel Turner'], ['Collins', 'Collins'], ['The Hub', 'The Hub']];
    const inP = l => s.lp === 'all' || l[2] === s.lp;
    const DD = [['t', 'Today'], ['7', 'Last 7 days'], ['30', 'Last 30 days']];
    const inD = l => s.ld === '30' || (s.ld === '7' ? l[1] !== 'm' : l[1] === 't');
    const q = s.q.trim().toLowerCase();
    const inQ = l => !q || (l[0] + ' ' + l[2] + ' ' + l[4] + ' ' + l[5] + ' ' + l[6]).toLowerCase().includes(q);
    const log = ALL.filter(l => inType(l) && inP(l) && inD(l) && inQ(l)).map(l => ({ at: l[0], who: l[2], ev: l[4], cls: 'sb-chip ' + GRP[l[3]][1], client: l[5] || 'None', what: l[6] }));
    const R = [
      ['bulk', 'Bulk download or export', 'More than 10 documents in a day (usual: under 5)', 'both super admins and the data protection lead', 'Mon 2 Nov 06:00, Sam Patel', false],
      ['ooh', 'Client documents opened out of hours', '20:00 to 07:00 and weekends, more than 3 documents', 'the data protection lead', 'Sun 1 Nov, Sam Patel', false],
      ['leaver', 'Leaver in notice period', 'Any download, export or vault reveal', 'both super admins', 'Sun 1 Nov, Sam Patel', false],
      ['rev', 'Vault reveals per person', 'More than ' + 15 + ' in 7 days (proposed)', 'the data protection lead', 'not fired since go-live', false],
      ['dev', 'New country or new device', 'Any staff sign-in', 'the person and the data protection lead', 'Sun 1 Nov 22:15, Femi Ade', false],
      ['two', 'Repeated two-step failures', '3 in 10 minutes', 'the data protection lead', 'not fired since go-live', false],
      ['una', 'Opening a client the person is not assigned to', 'Any, outside cover and view as', 'the data protection lead', 'not fired since go-live', false],
      ['cdev', 'Client signs in from a Care Sync device or network', 'Any', 'both super admins', 'not fired since go-live', false],
      ['bg', 'Break-glass started', 'Always', 'both super admins and the client, the same day', 'none since go-live', true],
      ['int', 'Audit log integrity check fails', 'Always', 'both super admins', 'never failed', true]
    ];
    const rules = R.map(([id, name, th, to, last, locked]) => { const on = locked || s.sw[id] !== false; return { name, th, to, last, locked, isBulk: id === 'bulk', aria: on ? 'true' : 'false', swLabel: name + (locked ? ', locked on' : ''), swCls: 'sx-sw ' + (locked ? 'sw-lock' : (on ? 'sw-on' : 'sw-off')), flip: () => { if (!locked) this.setState({ sw: up(s.sw, id, !on) }); } }; });
    const alerts = [
      ['Sam Patel: bulk download, leaver in notice period', '38 documents on Sun 1 Nov from 21:40. Escalated by Collins, the data protection lead, at 08:10.', 'Escalated to incident 2026-01', 'bad'],
      ['Femi Ade: new laptop', 'Sun 1 Nov 22:15. Two-step login passed and only the Xero sync page was opened. Marked as looked at by Rachel Turner, 08:15.', 'Looked at, not an incident', 'neutral']
    ].map(([t, x, state, k]) => ({ t, x, state, cls: ch(k) }));
    const evTypes = [
      ['Sign-in', 'Sign-in success and failure, two-step failure, session revoked, sign out everywhere'],
      ['Documents and fields', 'Document viewed, downloaded or uploaded; sensitive field revealed (DBS number, date of birth, ID number)'],
      ['Vault', 'Login added, revealed, copied, edited or deleted; hand-back steps'],
      ['Exports', 'Every export, including exports of this log'],
      ['Access and elevated', 'View as start and stop, break-glass start and stop, cover start and end, suspend, role or permission change'],
      ['Sending and AI', 'Sent as the client from their mailbox, signed in to the client\'s email, AI request (who, which client, which document)'],
      ['Changes', 'Prices, forms, emails, rules, integration keys, alert rules, retention schedule'],
      ['Data protection', 'Legal hold, deletion run, rights request step, incident step, approvals with the reason']
    ].map(([g, x]) => ({ g, x }));

    // Vault
    const revLimit = 15;
    const RV = [['Sam Patel', 14, 'Leaver: every reveal also alerts both super admins'], ['Daniel Mensah', 12, 'His own 8 clients'], ['Grace', 8, 'Adding logins for clients in onboarding'], ['Olu', 5, 'Before leave on Fri 30 Oct'], ['Collins', 2, 'Senior reviews'], ['Everyone else', 0, 'Rachel Turner, Divine, Millicent, Jo Martin, Femi Ade']];
    const revTotal = RV.reduce((a, r) => a + r[1], 0) + ' in total';
    const reveals = RV.map(([who, n, note]) => ({ who, n: n + ' of ' + revLimit, note, cls: ch(n > revLimit ? 'bad' : (n >= revLimit - 2 ? 'warn' : 'neutral')), w: 'w' + Math.min(100, Math.round(n / revLimit * 20) * 5) }));
    const methods = [['User added (no password held)', '18', 'Best: we are a user on their account', 'ok'], ['Delegated or connected', '9', 'Mailbox connection or shared folder', 'ok'], ['Stored password', '23', 'Review each one at its review date', 'neutral'], ['Authenticator held', '1', 'Target 0: Willow Bank, moving to delegation', 'bad']].map(([k, v, note, c]) => ({ k, v, note, cls: ch(c) }));
    const MN = { user: ['User added', 'c-ok'], deleg: ['Delegated', 'c-ok'], stored: ['Stored password', 'c-neutral'], auth: ['Authenticator held', 'c-bad'] };
    const VE = [
      ['Sunrise Homecare Ltd', 'CQC sign-in mailbox', 'stored', true, 'Engagement letter, Mon 7 Sep', 'Daniel, Thu 29 Oct: "check the Notice of Proposal email". Last rotated Mon 7 Sep', 'Mon 7 Dec', 'Active', 'ok', null],
      ['Westbrook Care Ltd', 'CQC sign-in mailbox', 'stored', true, 'Engagement letter, Mon 3 Aug', 'Daniel, Wed 28 Oct: "file the notice of decision". Last rotated Mon 3 Aug', 'Thu 3 Dec', 'Active', 'ok', null],
      ['Riverside Homecare Ltd', 'CQC sign-in mailbox', 'stored', true, 'Engagement letter, Mon 14 Sep', 'Not in the vault yet: 10 days (red after 7)', 'None', 'Missing', 'bad', 'rv'],
      ['Kingsway Care Ltd', 'CQC sign-in mailbox', 'stored', true, 'Engagement letter, Mon 21 Sep', 'Sam Patel, Fri 30 Oct: "file a CQC letter". Sam is suspended', 'Mon 21 Dec', 'Moves to the new owner', 'warn', null],
      ['Lagan View Care Ltd', 'RQIA Web Portal', 'stored', false, 'Engagement letter, Mon 24 Aug', 'Daniel (cover), today 08:40: "check for messages from RQIA"', 'Tue 3 Nov', 'Review due', 'warn', null],
      ['Oakleaf Living Ltd', 'Website hosting', 'stored', false, 'Engagement letter, Mon 5 Oct', 'Daniel, Fri 30 Oct: "update the services page"', 'Fri 4 Dec', 'Active', 'ok', null],
      ['Elm Tree Care Ltd', 'Business mailbox', 'deleg', false, 'Engagement letter, Mon 14 Sep', 'Mailbox connection only, never revealed', 'Mon 14 Dec', 'Active', 'ok', null],
      ['Greenway Support Ltd', 'Shared document folder', 'deleg', false, 'Engagement letter, Mon 12 Oct', 'Daniel (cover), today 08:52: "find the 3 waiting documents"', 'Tue 12 Jan', 'Active', 'ok', null],
      ['Afon Care Ltd', 'CIW Online', 'user', false, 'Engagement letter, Mon 31 Aug', 'Daniel is a user on Rhian\'s account. No password held', 'Mon 30 Nov', 'Active', 'ok', null],
      ['Oakleaf Living Ltd', 'Northshire tender portal', 'user', false, 'Engagement letter, Mon 5 Oct', 'Daniel is a user on Kemi\'s account. No password held', 'Fri 4 Dec', 'Active', 'ok', null],
      ['Willow Bank Supported Living Ltd', 'Website hosting, with its authenticator', 'auth', false, 'Engagement letter and a signed clause, Mon 19 Oct', 'Olu, Fri 30 Oct: "renew the domain"', 'Fri 13 Nov', 'Move to delegation by Fri 13 Nov', 'warn', 'wb']
    ];
    const VM = [['all', 'All'], ['user', 'User added'], ['deleg', 'Delegated'], ['stored', 'Stored password'], ['auth', 'Authenticator held']];
    const entries = VE.filter(e => s.vm === 'all' || e[2] === s.vm).map(e => {
      const act = e[9]; const asked = act === 'wb' ? s.wbAsked : s.rvAsked;
      return { client: e[0], sys: e[1], m: MN[e[2]][0], mCls: 'sb-chip ' + MN[e[2]][1], code: e[3], auth: e[4], last: e[5], rev: e[6],
        state: asked ? (act === 'wb' ? 'Asked David to add us as a user' : 'Asked Mark to add it himself') : e[7], sCls: ch(asked ? 'info' : e[8]), hasAct: !!act && !asked,
        actLabel: act === 'wb' ? 'Ask David to add us as a user' : 'Ask Mark to add it (board 27)', act: () => this.setState(act === 'wb' ? { wbAsked: true } : { rvAsked: true }) }; });
    const vRules = ['A reason is needed to reveal and to copy. "Copy without showing" asks for the same reason.', 'A revealed login hides again after 30 seconds.', 'Logins never appear in notes, messages, emails, exports or AI tools.', 'Every reveal and copy is on the client\'s privacy page, with the person and the reason.', 'Staff sign in again (with two-step) before the vault opens.'];
    const vDoneShow = !!s.vDone;
    const HBS = ['Requested', 'Access removed', 'Connection and tokens revoked', 'Entry deleted', 'Client confirmed the password changed'];
    const HB = [['fern', 'Fernhill Homecare Ltd (closed)', 'Declined'], ['north', 'Northgate Care Ltd (closed)', ''], ['blue', 'Bluebell Support Ltd (closed)', '']];
    const handback = HB.map(([id, client]) => { const n = s.hb[id]; const declined = n === 6;
      const steps = HBS.map((label, i) => ({ label: (i === 4 && declined) ? 'Client declined to change it, recorded' : label, cls: (i < n || declined) ? 'st-done' : (i === n ? 'st-now' : 'st-next') }));
      return { client, steps, canNext: n < 5, canDecline: n === 4, nextLabel: n < 5 ? 'Mark done: ' + HBS[n].toLowerCase() : '', state: n >= 5 ? (declined ? 'Closed, declined recorded' : 'Closed') : 'Step ' + (n + 1) + ' of 5', cls: ch(n >= 5 ? 'ok' : 'warn'),
        next: () => this.setState({ hb: up(s.hb, id, n + 1) }), decline: () => this.setState({ hb: up(s.hb, id, 6) }) }; });
    const PU = [['p1', 'Old tender Google Form responses that held portal passwords', '17 responses deleted, and the question removed'], ['p2', 'The logins spreadsheet in Drive', 'Move each login into the vault, then delete the file and empty the trash'], ['p3', 'The interim 1Password vault', '31 items moved, 6 left. Sam Patel removed from it at 08:25']];
    const purge = PU.map(([id, t, note]) => { const done = !!s.purge[id]; return { t, note, done, state: done ? 'Done' : 'To do', cls: ch(done ? 'ok' : 'warn'), flip: () => this.setState({ purge: up(s.purge, id, !done) }) }; });

    // Elevated access
    const covActive = !s.covEnded;
    const bgH = G('break-glass-hours', 4);
    const bgRules = ['Only for an emergency, never for planned leave (that is cover).', 'Approved by a super admin who is not the person asking. If no one can be reached, the person may self-authorise with a written reason.', 'Always ' + bgH + ' hours, then it ends by itself.', 'Both super admins and the client are told the same day. The client reads: "A senior member of the Care Sync team approved it."', 'Reviewed within 1 working day, with every reveal listed.'];
    const BGC = [['sun', 'Sunrise Homecare'], ['elm', 'Elm Tree Care'], ['afon', 'Afon Care']];
    const bgTabs = BGC.map(([k, l]) => ({ label: l, on: s.bgC === k, off: s.bgC !== k, pick: () => this.setState({ bgC: k, bgErr: false }) }));
    const bgName = (BGC.find(x => x[0] === s.bgC) || ['', ''])[1];
    const bgGo = mode => { if (!s.bgC || !s.bgR.trim()) { this.setState({ bgErr: true }); return; } this.setState({ bgSent: mode, bgErr: false }); };
    const viewas = [['Today 08:50 to 09:02', 'Collins: Harbour Lane Care Ltd', 'As Amara saw it on Fri 30 Oct. Reason: "Complaint check C-001". 12 minutes, ended'], ['Fri 30 Oct 14:05', 'Daniel Mensah: Harbour Lane Care Ltd', 'As Amara sees it. Reason: "answer her question about the home office". 6 minutes, ended'], ['Thu 29 Oct 10:12', 'Daniel Mensah: Bright Path Care Ltd', 'As Joy sees it. Reason: "check what Joy sees before session 2". 4 minutes, ended']].map(([at, who, x]) => ({ at, who, x }));

    // Sign-in and devices
    const idle = G('staff-idle-timeout', '30 minutes') + ' without use';
    const dd = G('client-device-days', 30);
    const D = [
      ['c1', 'Collins', 'MacBook CS-LT-01', 'Company', 'Office and home', 'Thu 1 Oct to today 08:48', 'tr'],
      ['c2', 'Collins', 'iPhone', 'Company', 'Mobile', 'Thu 1 Oct to today 07:15', 'tr'],
      ['r1', 'Rachel Turner', 'Laptop CS-LT-02', 'Company', 'Office', 'Thu 1 Oct to today 08:45', 'tr'],
      ['d1', 'Daniel Mensah', 'Laptop CS-LT-04', 'Company', 'Office', 'Thu 1 Oct to today 08:52', 'tr'],
      ['g1', 'Grace', 'Laptop CS-LT-05', 'Company', 'Office', 'Thu 1 Oct to Fri 30 Oct 17:20', 'tr'],
      ['s1', 'Sam Patel', 'Laptop CS-LT-07', 'Company', 'Home', 'Thu 1 Oct to Sun 1 Nov 22:07', 'rv', 'Revoked 08:25. Back to Rachel at 14:00'],
      ['s2', 'Sam Patel', 'iPhone, work profile', 'Personal', 'Mobile', 'Thu 1 Oct to Sun 1 Nov 20:10', 'rv', 'Revoked 08:25. Work data wiped'],
      ['f2', 'Femi Ade', 'New laptop', 'Company', 'Home, first time', 'Sun 1 Nov 22:15 to 22:31', 'new'],
      ['f1', 'Femi Ade', 'Laptop CS-LT-10', 'Company', 'Home', 'Mon 5 Oct to Fri 30 Oct', 'tr']
    ];
    const devices = D.map(([id, who, dev, kind, place, seen, st0, note]) => { const st = s.dev[id] || (s.outAll[who] && st0 !== 'rv' ? 'out' : st0);
      const lab = { tr: 'Trusted', new: 'New: looked at, only Xero sync opened', rv: note || 'Revoked', rv2: 'Revoked by Collins, just now', out: 'Signed out everywhere, just now' }[st];
      return { who, dev, kind, place, seen, state: lab, cls: ch({ tr: 'ok', new: 'warn', rv: 'neutral', rv2: 'neutral', out: 'info' }[st]), canTrust: st === 'new', canRevoke: st === 'tr' || st === 'new',
        trust: () => this.setState({ dev: up(s.dev, id, 'tr') }), revoke: () => this.setState({ dev: up(s.dev, id, 'rv2') }) }; });
    const outBtns = ['Femi Ade', 'Daniel Mensah', 'Grace'].map(p => ({ label: s.outAll[p] ? p + ': signed out' : 'Sign out everywhere: ' + p, go: () => this.setState({ outAll: up(s.outAll, p, true) }) }));
    const cdev = [['iPhone', 'Known since a code check on Mon 26 Oct; stays signed in to Wed 25 Nov'], ['Laptop, Chrome', 'Known since a code check on Thu 15 Oct; stays signed in to Sat 14 Nov']].map(([dev, seen]) => ({ dev, seen, state: s.clientOut ? 'Signed out' : 'Known', cls: ch(s.clientOut ? 'neutral' : 'ok') }));
    const signins = [
      ['Sun 1 Nov 22:15', 'Femi Ade', 'New laptop. Two-step passed; only the Xero sync page opened', 'Looked at', 'neutral'],
      ['Sun 1 Nov 21:38', 'Sam Patel', 'Signed in from home on a known laptop, then 38 downloads', 'In incident 2026-01', 'bad'],
      ['Mon 26 Oct 19:02', 'Priya Shah (client)', 'New device: iPhone. Mobile code sent to her phone and entered', 'Code checked', 'ok']
    ].map(([at, who, x, state, k]) => ({ at, who, x, state, cls: ch(k) }));

    // Resilience
    const keys = [['Vault key', 'Logins only. Created Thu 1 Oct. Held in the hosting key service'], ['Sensitive fields key', 'DBS numbers, dates of birth and ID numbers. Thu 1 Oct'], ['File storage key', 'All documents. Thu 1 Oct'], ['Backup key', 'In the separate backup account. Thu 1 Oct'], ['Integration keys', 'Stripe rotated Thu 8 Oct. Others at go-live. Yearly rotation (proposed)']].map(([k, x]) => ({ k, x }));
    const contacts = [
      ['Data protection lead', 'Collins (deputy: Rachel Turner)', 'Phone and email in Google Workspace', false],
      ['Super admins', 'Collins and Rachel Turner', 'Both get every security alert', false],
      ['Google Workspace admin', 'Collins (backup admin: Rachel Turner)', 'Suspends accounts and wipes work data', false],
      ['Hosting and developer on call', 'Supplier to name', 'On-call phone number to add', true],
      ['Cyber insurer', 'Check whether Care Sync has cyber cover', 'Policy number and claims line to add', true],
      ['Bank and Stripe', 'Bank fraud line; Stripe through its dashboard', 'Bank fraud number to add', true],
      ['ICO', 'Helpline 0303 123 1113', 'Or the ICO\'s online personal data breach report form', true],
      ['Action Fraud', '0300 123 2040', 'If a crime may be involved', true]
    ].map(([role, who, how, check]) => ({ role, who, how, check }));
    const runbook = [
      ['First hour', ['Contain: pause downloads, suspend the account, sign out every device (Suspend now, board 83).', 'Write down when we became aware. The 72-hour clock starts there.', 'Tell the data protection lead and both super admins.', 'Keep evidence: place a legal hold. Do not wipe a company device that needs checking.', 'Open the incident record on this screen.']],
      ['First 24 hours', ['Find out what data, how many people and which clients.', 'Check where it went: the device, Google Workspace, sharing links.', 'Score how likely and how bad the harm could be.', 'Suppliers who process for us must tell us without undue delay (Art 33(2)).', 'Call the insurer if we have cover.']],
      ['By 72 hours', ['Decide: report to the ICO or not, with reasons. The record is kept either way.', 'If reporting, use the ICO\'s online form. If late, give the reasons.', 'Decide whether to tell the people affected (Art 34).', 'Agree actions and lessons, then the data protection lead closes it.']]
    ].map(([h, steps]) => ({ h, s: steps }));

    return {
      theme: this.props.theme ?? 'light', three: 7, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      repOpen: s.rep, repLabel: s.rep ? 'Close the report' : 'Report a concern or incident', toggleRep: () => this.setState({ rep: !s.rep, repErr: false }),
      repText: s.repText, repErr: s.repErr, repSent: s.repSent, onRep: e => this.setState({ repText: e.target.value, repErr: false, repSent: false }),
      sendRep: () => { if (!s.repText.trim()) { this.setState({ repErr: true }); return; } this.setState({ repSent: true, repText: '' }); },
      tiles: [
        ['inc', 'Open incidents', '1', hoursLeft + ' left to decide on the ICO', 'bad'],
        ['log', 'New alerts', '0', '2 since Sunday, both handled', 'ok'],
        ['vault', 'Vault reveals, 7 days', '41', 'Nobody over ' + revLimit, 'neutral'],
        ['elev', 'Break-glass, 30 days', '0', 'Leave uses cover instead', 'ok'],
        ['sign', 'Two-step sign-in', '10 of 10', 'Read from Google Workspace', 'ok'],
        ['res', 'Last restore test', 'Tue 13 Oct', 'Passed. Next by Mon 11 Jan', 'ok']
      ].map(([k, l, v, note, c]) => ({ k: l, v, note, cls: ch(c), aria: l + ': ' + v + '. ' + note + '. Open', go: () => this.setState({ t: k }) })),
      tabs: T.map(([k, label]) => ({ label, on: s.t === k, off: s.t !== k, pick: () => this.setState({ t: k }) })),
      isInc: s.t === 'inc', isLog: s.t === 'log', isVault: s.t === 'vault', isElev: s.t === 'elev', isSign: s.t === 'sign', isRes: s.t === 'res',
      incState, incCls: ch(incK), steps, facts, contain, likeTabs, sevTabs, riskText,
      icoTabs, icoOpen: !icoDone, icoDone, icoR: s.icoR, icoErr: s.icoErr, icoErrText: s.ico ? 'Write the reasons. The record is kept either way.' : 'Choose yes or no, and write the reasons.',
      icoPh: s.ico === 'yes' ? 'For example: identity and DBS documents left our control; we cannot yet rule out sharing' : 'For example: files stayed on the managed, encrypted laptop; checks found no sharing; copies deleted and confirmed',
      onIcoR: e => this.setState({ icoR: e.target.value, icoErr: false }),
      saveIco: () => { if (!s.ico || !s.icoR.trim()) { this.setState({ icoErr: true }); return; } this.setState({ icoSaved: true, acts: up(s.acts, 'a5', true) }); },
      undoIco: () => this.setState({ icoSaved: false }),
      icoBox: icoYes ? 'sx-amb' : 'sx-box', icoHead: icoYes ? 'Decision: report to the ICO. Decided by Collins (data protection lead), Mon 2 Nov 09:20. Rachel Turner reviews it' : 'Decision: not reportable. Decided by Collins (data protection lead), Mon 2 Nov 09:20. Rachel Turner reviews it',
      icoNote: icoYes ? 'Collins sends the report on the ICO\'s online form before Thu 5 Nov 06:00 and adds the ICO reference here. Incident state: Reported to the ICO.' : 'The reasons stay in the breach record. If new facts appear, the decision is reopened and the clock still runs from Mon 2 Nov 06:00.',
      tellTabs, tellOpen: !tellDone, tellDone, tellR: s.tellR, tellErr: s.tellErr, tellErrText: s.tell ? 'Write the reasons.' : 'Choose yes or no, and write the reasons.',
      onTellR: e => this.setState({ tellR: e.target.value, tellErr: false }),
      saveTell: () => { if (!s.tell || !s.tellR.trim()) { this.setState({ tellErr: true }); return; } this.setState({ tellSaved: true }); },
      undoTell: () => this.setState({ tellSaved: false }),
      tellBox: tellYes ? 'sx-amb' : 'sx-box', tellHead: tellYes ? 'Decision: tell the 11 people affected. Decided by Collins (data protection lead); Rachel Turner reviews it' : 'Decision: not telling the people affected. Decided by Collins (data protection lead); Rachel Turner reviews it',
      tellNote: tellYes ? 'Each gets email 9.4 "We need to tell you about a data incident" (Messages and automations, board 82), filled from this record: what happened, what was involved, what we did and who to contact. Collins signs it as data protection lead and Rachel Turner approves it before it goes; it is never sent automatically. Each send is logged here.' : 'The reasons stay in the breach record. The 6 clients are still told as a courtesy.',
      acts, actCount: actDone + ' of ' + acts.length + ' done',
      hoursLeft, clockBar: 'w' + Math.max(5, used), timeline,
      q: s.q, onQ: e => this.setState({ q: e.target.value }), doExport: () => this.setState({ exported: true }), exportLabel: s.exported ? 'Exported (logged)' : 'Export this view',
      typeTabs: TT.map(([k, label]) => ({ label, on: s.lt === k, off: s.lt !== k, pick: () => this.setState({ lt: k }) })),
      personTabs: PP.map(([k, label]) => ({ label, on: s.lp === k, off: s.lp !== k, pick: () => this.setState({ lp: k }) })),
      dayTabs: DD.map(([k, label]) => ({ label, on: s.ld === k, off: s.ld !== k, pick: () => this.setState({ ld: k }) })),
      log, noLog: log.length === 0, logCount: 'Showing ' + log.length + ' of ' + ALL.length + ' entries in this design. Entries cannot be edited or deleted. Exporting the log is itself logged.',
      rules, bulkMode: s.realtime ? 'Checked in real time' : 'Checked nightly at 06:00', bulkCls: ch(s.realtime ? 'ok' : 'warn'), bulkCan: !s.realtime, makeRealtime: () => this.setState({ realtime: true, acts: up(s.acts, 'a7', true) }),
      alerts, evTypes,
      vRules, vReason: s.vReason, vErr: s.vErr, onVReason: e => this.setState({ vReason: e.target.value, vErr: false, vDone: '' }),
      vCopy: () => { if (!s.vReason.trim()) { this.setState({ vErr: true }); return; } this.setState({ vDone: 'copy' }); },
      vShow: () => { if (!s.vReason.trim()) { this.setState({ vErr: true }); return; } this.setState({ vDone: 'show' }); },
      vDoneShow, vDoneText: s.vDone === 'copy' ? 'Copied without showing. The clipboard is cleared after 30 seconds where the browser allows.' : 'Shown for 30 seconds, then hidden again.',
      vDoneClient: s.vDone === 'copy' ? 'Collins copied your email login: ' + s.vReason.trim() : 'Collins looked at your email login: ' + s.vReason.trim(),
      reveals, revTotal, revLimit: String(revLimit), methods,
      vmTabs: VM.map(([k, label]) => ({ label, on: s.vm === k, off: s.vm !== k, pick: () => this.setState({ vm: k }) })),
      entries, entryCount: 'Showing ' + entries.length + ' of 51 entries.', handback, purge,
      covActive, covState: covActive ? 'Active' : 'Ended early', covCls: ch(covActive ? 'info' : 'neutral'), covEnds: covActive ? 'Fri 6 Nov 17:30, by itself' : 'Ended by Collins just now: "' + s.coverR.trim() + '"',
      covUse: ['Today 08:40: Lagan View, RQIA Web Portal, "check for messages from RQIA"', 'Today 08:52: Greenway Support, shared document folder, "find the 3 waiting documents"'],
      coverR: s.coverR, coverErr: s.coverErr, onCoverR: e => this.setState({ coverR: e.target.value, coverErr: false }),
      endCover: () => { if (!s.coverR.trim()) { this.setState({ coverErr: true }); return; } this.setState({ covEnded: true }); },
      bgRules, bgTabs, bgR: s.bgR, bgErr: s.bgErr, onBgR: e => this.setState({ bgR: e.target.value, bgErr: false, bgSent: '' }),
      bgAsk: () => bgGo('ask'), bgSelf: () => bgGo('self'), bgShow: !!s.bgSent,
      bgHead: s.bgSent === 'self' ? 'Self-authorised: ' + bgName + ', ' + bgH + ' hours from now' : 'Sent to Rachel Turner: ' + bgName,
      bgNote: s.bgSent === 'self' ? 'Rachel Turner and ' + bgName + ' are told now. Rachel reviews it within 1 working day, with every reveal listed. Reason: "' + s.bgR.trim() + '"' : 'Nothing opens until Rachel approves. If she approves, it lasts ' + bgH + ' hours, the client is told the same day, and it is reviewed within 1 working day.',
      viewas,
      idle, twoStep: 'Enforced for everyone by Google Workspace. 10 of 10 people enrolled: 9 with a security key or app, 1 with text message codes',
      femiBox: s.femi ? 'sx-box' : 'sx-amb', femiHead: s.femi ? 'Asked Femi Ade to switch, just now' : 'Femi Ade uses text message codes',
      femiNote: s.femi ? 'Femi gets a short guide. This turns green when Google shows an app or key.' : 'Codes by text are weaker than an app or a security key. Femi signed in on a new laptop on Sunday, a good moment to set up an app or a key.', femiAsk: !s.femi, askFemi: () => this.setState({ femi: true }),
      deviceDays: dd + ' days, then a new link',
      dvTabs: [['staff', 'Staff (10 people)'], ['client', 'A client']].map(([k, label]) => ({ label, on: s.dv === k, off: s.dv !== k, pick: () => this.setState({ dv: k }) })),
      isStaffDev: s.dv === 'staff', isClientDev: s.dv === 'client', devices, outBtns, cdev,
      clientOutLabel: s.clientOut ? 'Signed out of 2 devices' : 'Sign Priya out everywhere', clientOutGo: () => this.setState({ clientOut: true }),
      signins, keys, contacts, runbook
    };
  }
}'''

build_sa(os.path.join(OUT, 'SecurityCentre.dc.html'), 'Security', 'Security', H_SEC, SEC_B, SEC_S, 'security', CSS)

# ---------------------------------------------------------------------------------------------
# 85. Data and privacy
# ---------------------------------------------------------------------------------------------
PRIV_B = header('Data and privacy', 'How long we keep things, deletions and legal holds, people\'s rights requests, our records, suppliers and exports. Shown at Monday 2 November, 09:20. Collins is the data protection lead; schedule changes and early deletions need both super admins.') + TILES + tabs('Data and privacy areas') + '''
      <sc-if value="{{isRet}}" hint-placeholder-val="{{ true }}">
        <section class="sb-card" aria-labelledby="v2-h">
          <div class="sb-head"><h2 id="v2-h" class="sb-h2">Retention schedule v2: waiting for Rachel Turner</h2><span class="{{v2Cls}}">{{v2State}}</span></div>
          <div class="sx-pad">
            <div class="sx-col2">
              <div class="sx-box"><span class="sx-lbl">What changes</span><span>Identity document images and DBS certificate images are deleted <span class="sx-b">once the regulator has made its decision</span>, instead of being kept until our work for the client ends. The Hub keeps a record: who saw it, the date, the document type, and the DBS number and issue date.</span></div>
              <div class="sx-box"><span class="sx-lbl">Impact today</span><span>17 clients have a regulator decision. Their 46 identity images and 12 DBS images would go into the next deletion run, after 7 days' notice. Client screens that read this schedule: Account and the Security page ("How long we keep things").</span></div>
            </div>
            <span class="sb-sub">Proposed by Collins as data protection lead, Fri 30 Oct. A schedule change needs the other super admin, so only Rachel Turner can approve it. Decision 7 of 7 on Home.</span>
            <sc-if value="{{v2Open}}" hint-placeholder-val="{{ true }}"><div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;"><span class="sx-lbl">See this as</span>''' + subtabs('v2As', 'See this as', 2) + '''</div></sc-if>
            <sc-if value="{{v2Own}}" hint-placeholder-val="{{ true }}"><div class="sx-box" style="gap: 8px;"><span class="sx-b">Rachel Turner must approve this</span><span class="sb-sub">You proposed this change, and nobody can approve their own request. It waits for Rachel Turner.</span><div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;"><button class="sb-btn b-sec" onClick="{{v2Remind}}">Remind Rachel</button><span class="sb-muted">{{v2RemindNote}}</span></div></div></sc-if>
            <sc-if value="{{v2CanDecide}}" hint-placeholder-val="{{ false }}">
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <span class="sx-lbl">Applies to</span>
                ''' + subtabs('v2When', 'Applies to', 2) + '''
                <label class="sx-lbl" for="v2-ta">Your reason (written to the audit log)</label>
                <textarea id="v2-ta" class="sx-ta" value="{{v2R}}" onChange="{{onV2R}}" placeholder="For example: we only need the images for the regulator's checks; the record is enough after that"></textarea>
                <sc-if value="{{v2Err}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Write a reason before you approve or decline.</span></sc-if>
                <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{v2Yes}}">Approve v2</button><button class="sb-btn b-gh" onClick="{{v2No}}">Decline</button></div>
              </div>
            </sc-if>
            <sc-if value="{{v2Done}}" hint-placeholder-val="{{ false }}"><div class="{{v2Box}}"><span class="sx-b">{{v2Head}}</span><span class="sb-sub">{{v2Note}}</span></div></sc-if>
          </div>
        </section>
        <section class="sb-card" aria-labelledby="rs-h">
          <div class="sb-head"><h2 id="rs-h" class="sb-h2">Retention schedule, per document type</h2>''' + subtabs('verTabs', 'Version', 2) + '''</div>
          <div style="padding: 0 20px 10px;" class="sb-sub">{{verNote}}</div>
          <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 2 1 210px;">Document or data</span><span class="sb-th" style="flex: 2 1 200px;">How long, from when</span><span class="sb-th" style="flex: 2 1 220px;">Why, and the source</span><span class="sb-th" style="flex: 1 1 150px;">Systems to clear</span><span class="sb-th" style="flex: 0 0 150px;">Status</span></div>
          <sc-for list="{{sched}}" as="r" hint-placeholder-count="18">
            <div class="sb-row" style="align-items: flex-start; padding-top: 9px; padding-bottom: 9px;">
              <span class="sx-b" style="flex: 2 1 210px; min-width: 0; font-size: 13px; line-height: 18px;">{{r.type}}</span>
              <span style="flex: 2 1 200px; min-width: 0; display: flex; flex-direction: column; gap: 2px; font-size: 13px; line-height: 18px;"><span>{{r.period}}</span><sc-if value="{{r.was}}" hint-placeholder-val="{{ false }}"><span class="sb-muted">Was (v1): {{r.wasText}}</span></sc-if></span>
              <span class="sb-sub" style="flex: 2 1 220px; min-width: 0;">{{r.basis}}</span>
              <span class="sb-muted" style="flex: 1 1 150px; min-width: 0;">{{r.sys}}</span>
              <span style="flex: 0 0 150px;"><span class="{{r.cls}}" style="white-space: normal;">{{r.status}}</span></span>
            </div>
          </sc-for>
          <div class="sb-row"><span class="sb-muted">Every row ends in deletion, not archiving. Values marked "proposed" are for the data protection lead to confirm. Routine deletions inside the live schedule run by themselves with 7 days' notice. History: v1 approved by Collins and Rachel Turner at go-live, Thu 1 Oct.</span></div>
        </section>
      </sc-if>

      <sc-if value="{{isDel}}" hint-placeholder-val="{{ false }}">
        <div class="sx-cols">
          <section class="sb-card" style="flex: 3 1 600px; min-width: 0;" aria-labelledby="dr-h">
            <div class="sb-head"><h2 id="dr-h" class="sb-h2">Deletion run: Mon 9 Nov, 06:00</h2><span class="{{runCls}}">{{runState}}</span></div>
            <div class="sx-pad">
              <span class="sb-sub">14 identity documents from 3 closed clients, under schedule v1. Notice given Mon 2 Nov 06:00 (7 days). It runs by itself unless someone stops it.</span>
              <div class="sx-box" style="padding: 0; overflow: hidden; gap: 0;">
                <div style="display: grid; grid-template-columns: 1.4fr 1.3fr 1fr; gap: 10px; padding: 8px 14px;"><span class="sx-lbl">Document</span><span class="sx-lbl">Closed client</span><span class="sx-lbl">Retention ended</span></div>
                <sc-for list="{{delDocs}}" as="d" hint-placeholder-count="14">
                  <div style="display: grid; grid-template-columns: 1.4fr 1.3fr 1fr; gap: 10px; padding: 5px 14px; border-top: 1px solid var(--cs-border-subtle); font-size: 13px; line-height: 18px;"><span>{{d.t}}</span><span>{{d.c}}</span><span>{{d.e}}</span></div>
                </sc-for>
              </div>
              <div class="sx-ok"><span class="sx-b">Legal hold check: clear</span><span class="sb-sub">None of the 3 clients has a legal hold, an open complaint, a regulator query, a payment dispute or a rights request that covers these documents. (The open rights request covers a reference letter for Northgate Care Ltd, which is not in this run.) Checked by the Hub today at 06:00.</span></div>
              <div style="display: flex; flex-direction: column;">
                <div style="display: flex; justify-content: space-between; gap: 8px; padding-bottom: 6px;"><span class="sx-b">Systems to clear outside the Hub</span><span class="sb-muted">{{sysCount}}</span></div>
                <sc-for list="{{delSys}}" as="x" hint-placeholder-count="7">
                  <div style="display: flex; gap: 12px; align-items: flex-start; padding: 8px 0; border-top: 1px solid var(--cs-border-subtle);"><label class="sx-chk" style="flex: 1; min-width: 0;"><input type="checkbox" checked="{{x.done}}" onChange="{{x.flip}}"><span style="display: flex; flex-direction: column;"><span>{{x.t}}</span><span class="sb-muted">{{x.note}}</span></span></label><span class="{{x.cls}}">{{x.state}}</span></div>
                </sc-for>
              </div>
              <span class="sb-muted">If a system is not ticked by the run, the run shows "Partly done" and stays open. A certificate of deletion (what, when, systems cleared, backup expiry) is kept, never the documents.</span>
              <sc-if value="{{runOpen}}" hint-placeholder-val="{{ true }}">
                <label class="sx-lbl" for="stop-ta">Reason to stop the run</label>
                <textarea id="stop-ta" class="sx-ta" value="{{stopR}}" onChange="{{onStopR}}" placeholder="For example: Northgate's director has raised a complaint"></textarea>
                <sc-if value="{{stopErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Write a reason first.</span></sc-if>
                <div><button class="sb-btn b-gh" onClick="{{stopRun}}">Stop this run</button></div>
              </sc-if>
              <sc-if value="{{runStopped}}" hint-placeholder-val="{{ false }}"><div class="sx-amb"><span class="sx-b">Stopped by Collins, just now</span><span class="sb-sub">Reason: "{{stopR}}". Nothing is deleted. Restarting needs a new 7 days' notice.</span><div><button class="sb-btn b-gh" onClick="{{restart}}">Restart with new notice</button></div></div></sc-if>
            </div>
          </section>
          <section class="sb-card" style="flex: 2 1 380px; min-width: 0;" aria-labelledby="lh-h">
            <div class="sb-head"><h2 id="lh-h" class="sb-h2">Legal holds</h2><span class="sb-sub">{{holdCount}}</span></div>
            <sc-for list="{{holds}}" as="h" hint-placeholder-count="3">
              <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 6px;">
                <div style="display: flex; justify-content: space-between; gap: 8px;"><span class="sx-b">{{h.scope}}</span><span class="{{h.cls}}">{{h.state}}</span></div>
                <span class="sb-sub">{{h.why}}</span>
                <span class="sb-muted">{{h.meta}}</span>
                <sc-if value="{{h.on}}" hint-placeholder-val="{{ true }}"><div><button class="sb-btn b-gh" onClick="{{h.release}}">Release, with a reason</button></div></sc-if>
                <sc-if value="{{h.asking}}" hint-placeholder-val="{{ false }}">
                  <input aria-label="{{h.relLabel}}" class="sx-in" value="{{h.r}}" onChange="{{h.onR}}" placeholder="Reason for releasing it">
                  <sc-if value="{{h.err}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Write a reason first.</span></sc-if>
                  <div style="display: flex; gap: 8px;"><button class="sb-btn b-sec" onClick="{{h.confirm}}">Release the hold</button><button class="sb-btn b-gh" onClick="{{h.cancel}}">Keep it</button></div>
                </sc-if>
              </div>
            </sc-for>
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px;">
              <span class="sx-b">Place a legal hold</span>
              <input aria-label="What the hold covers" class="sx-in" value="{{nhScope}}" onChange="{{onNhScope}}" placeholder="What it covers, for example: Riverside Homecare Ltd, call notes">
              <input aria-label="Why" class="sx-in" value="{{nhWhy}}" onChange="{{onNhWhy}}" placeholder="Why, for example: concern raised on Fri 30 Oct">
              <sc-if value="{{nhErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Say what it covers and why.</span></sc-if>
              <div><button class="sb-btn b-sec" onClick="{{addHold}}">Place the hold</button></div>
              <span class="sb-muted">A hold stops every deletion it covers, including routine runs, until it is released with a reason.</span>
            </div>
          </section>
        </div>
      </sc-if>

      <sc-if value="{{isRights}}" hint-placeholder-val="{{ false }}">
        <div class="sx-cols">
          <section class="sb-card" style="flex: 3 1 600px; min-width: 0;" aria-labelledby="rr-h">
            <div class="sb-head"><h2 id="rr-h" class="sb-h2">Request 2026-01: a former referee asks what we hold</h2><span class="{{rrCls}}">{{rrState}}</span></div>
            <div class="sx-pad">
              <div class="sx-step"><sc-for list="{{rrSteps}}" as="st" hint-placeholder-count="5"><span class="{{st.cls}}">{{st.label}}</span></sc-for></div>
              <div class="sx-kv">
                <sc-for list="{{rrFacts}}" as="f" hint-placeholder-count="9"><span>{{f.k}}</span><span>{{f.v}}</span></sc-for>
              </div>
              <div style="display: flex; flex-direction: column;">
                <div style="display: flex; justify-content: space-between; gap: 8px; padding-bottom: 6px;"><span class="sx-b">Systems searched</span><span class="sb-muted">{{srCount}}</span></div>
                <sc-for list="{{searched}}" as="x" hint-placeholder-count="9">
                  <div style="display: flex; gap: 12px; align-items: flex-start; padding: 7px 0; border-top: 1px solid var(--cs-border-subtle);"><label class="sx-chk" style="flex: 1; min-width: 0;"><input type="checkbox" checked="{{x.done}}" onChange="{{x.flip}}"><span style="display: flex; flex-direction: column;"><span>{{x.t}}</span><span class="sb-muted">{{x.note}}</span></span></label><span class="{{x.cls}}">{{x.state}}</span></div>
                </sc-for>
              </div>
              <div class="sx-box" style="gap: 8px;">
                <span class="sx-b">Other people's details</span>
                <span class="sb-sub">The reference is about Northgate's former manager. Hannah wrote it, so she gets it, but our covering emails also hold the manager's home address and DBS number: those are removed before sending.</span>
                <label class="sx-chk"><input type="checkbox" checked="{{redacted}}" onChange="{{flipRed}}"><span>Redaction done and checked by a second person (Rachel Turner)</span></label>
              </div>
              <div class="sx-box" style="gap: 8px;">
                <span class="sx-b">Send the response</span>
                <span class="sb-sub">By a secure link from the Hub that expires after 14 days. The download is logged. No fee (normally free: Art 12(5)).</span>
                <sc-if value="{{sendErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">{{sendErrText}}</span></sc-if>
                <sc-if value="{{rrOpen}}" hint-placeholder-val="{{ true }}"><div><button class="sb-btn b-pri" onClick="{{sendRr}}">Send the response to Hannah</button></div></sc-if>
                <sc-if value="{{rrSent}}" hint-placeholder-val="{{ false }}"><div class="sx-ok"><span class="sx-b">Sent by Collins, Mon 2 Nov 09:20, 25 days before the due date</span><span class="sb-sub">The link expires Mon 16 Nov. The request closes when Hannah opens it, or when the link expires.</span></div></sc-if>
              </div>
            </div>
          </section>
          <div style="flex: 2 1 360px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
            <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="rc-h">
              <h2 id="rc-h" class="sb-h2">The one-month clock</h2>
              <span class="sx-big">25 days left</span>
              <div class="bar" aria-hidden="true"><span class="w20"></span></div>
              <div class="sx-kv" style="grid-template-columns: 110px minmax(0, 1fr);">
                <span>Received</span><span>Wed 28 Oct</span>
                <span>Due</span><span class="sx-b">Fri 27 Nov</span>
                <span>Shown at</span><span>Mon 2 Nov 09:20</span>
              </div>
              <span class="sb-muted">Source: UK GDPR Art 12(3) and the ICO's right of access guidance. Within one month of receipt, worked out the safe way (a day early). Up to two more months for complex or many requests, only if we tell the person within the first month. Pausing the clock while we wait for ID: ICO guidance allows it, and the Data (Use and Access) Act 2025 puts it in law (check it has commenced).</span>
            </section>
            <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="ra2-h">
              <h2 id="ra2-h" class="sb-h2">Requests from anyone</h2>
              <span class="sb-sub">"Download everything" serves the client's account holder. Everyone else comes here: registered managers, co-directors, referees, landlords, GPs named on forms, prospects and staff. Requests count however they arrive: email, phone, a message or a letter. Every staff screen has "Log a request".</span>
              <span class="sb-sub">Types: access, correction, erasure, restriction, objection, portability, complaint. "Correct something we hold" on the client's Account page lands here too.</span>
              <div class="sx-box"><span class="sx-lbl">Closed since go-live</span><span style="font-size: 13px; line-height: 18px;">1 correction: Bright Path Care Ltd changed Joy's phone number through "Correct something we hold", Thu 15 Oct, done the same day.</span></div>
              <span class="sb-muted">To decide with the data protection lead: what each role's "Download everything" contains (for example, a director's download and the registered manager's DBS details). Data protection complaints: acknowledge within 30 days (check whether this part of the Data (Use and Access) Act 2025 has commenced).</span>
            </section>
          </div>
        </div>
      </sc-if>

      <sc-if value="{{isRec}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card" aria-labelledby="ropa-h">
          <div class="sb-head"><h2 id="ropa-h" class="sb-h2">Record of processing</h2><span class="sb-sub">UK GDPR Art 30. Needed even under 250 staff, because the processing is regular and includes criminal offence data (Art 30(5))</span></div>
          <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 2 1 190px;">Activity and purpose</span><span class="sb-th" style="flex: 2 1 200px;">People and data</span><span class="sb-th" style="flex: 2 1 210px;">Lawful basis and condition</span><span class="sb-th" style="flex: 0 0 120px;">Our role</span><span class="sb-th" style="flex: 2 1 180px;">Suppliers and place</span></div>
          <sc-for list="{{ropa}}" as="r" hint-placeholder-count="10">
            <div class="sb-row" style="align-items: flex-start; padding-top: 9px; padding-bottom: 9px;">
              <span style="flex: 2 1 190px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b" style="font-size: 13px;">{{r.a}}</span><span class="sb-muted">{{r.p}}</span></span>
              <span class="sb-sub" style="flex: 2 1 200px; min-width: 0;">{{r.d}}</span>
              <span class="sb-sub" style="flex: 2 1 210px; min-width: 0;">{{r.b}}</span>
              <span class="sb-sub" style="flex: 0 0 120px;">{{r.role}}</span>
              <span class="sb-muted" style="flex: 2 1 180px; min-width: 0;">{{r.s}}</span>
            </div>
          </sc-for>
          <div class="sb-row"><span class="sb-muted">Each row links to its retention row and supplier records. "Check" means the data protection lead confirms it before the next review.</span></div>
        </section>
        <div class="sx-cols">
          <section class="sb-card" style="flex: 3 1 560px; min-width: 0;" aria-labelledby="dp-h">
            <div class="sb-head"><h2 id="dp-h" class="sb-h2">Data protection impact assessments</h2><span class="sb-sub">Art 35. If high risk remains after the measures, we consult the ICO first (Art 36)</span></div>
            <sc-for list="{{dpias}}" as="d" hint-placeholder-count="6">
              <div class="sb-row" style="align-items: flex-start;">
                <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">{{d.t}}</span><span class="sb-sub">{{d.m}}</span><span class="sb-muted">{{d.meta}}</span></span>
                <span style="display: flex; flex-direction: column; gap: 6px; align-items: flex-end;"><span class="{{d.cls}}">{{d.state}}</span><span class="sb-chip c-neutral">{{d.res}}</span></span>
              </div>
            </sc-for>
          </section>
          <div style="flex: 2 1 360px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
            <section class="sb-card sx-pad" style="padding-top: 18px;" aria-labelledby="apd-h">
              <h2 id="apd-h" class="sb-h2">Appropriate policy document</h2>
              <div class="sx-kv" style="grid-template-columns: 100px minmax(0, 1fr);"><span>Version</span><span>v1, Mon 28 Sep 2026</span><span>Owner</span><span>Collins, data protection lead</span><span>Review</span><span>Tue 28 Sep 2027</span><span>Covers</span><span>DBS information (criminal offence data). The Schedule 1 condition, and whether Part 4 needs this document: check</span></div>
              <span class="sb-muted">Source: UK GDPR Art 10; Data Protection Act 2018 s.10 and Schedule 1.</span>
            </section>
            <section class="sb-card" aria-labelledby="pn-h">
              <div class="sb-head"><h2 id="pn-h" class="sb-h2">Privacy notices</h2></div>
              <sc-for list="{{notices}}" as="n" hint-placeholder-count="3">
                <div class="sb-row" style="align-items: flex-start;"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">{{n.t}}</span><span class="sb-sub">{{n.x}}</span></span><span class="{{n.cls}}">{{n.state}}</span></div>
              </sc-for>
              <div class="sb-row"><span class="sb-muted">The privacy notice is information, not consent. Consent is asked separately, only where it is the basis: call recording, WhatsApp updates (later) and holding an authenticator.</span></div>
            </section>
          </div>
        </div>
      </sc-if>

      <sc-if value="{{isSup}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card" aria-labelledby="su-h">
          <div class="sb-head"><h2 id="su-h" class="sb-h2">Suppliers who process our data</h2>''' + subtabs('supTabs', 'Show', 3) + '''</div>
          <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 2 1 190px;">Supplier and purpose</span><span class="sb-th" style="flex: 2 1 190px;">Data</span><span class="sb-th" style="flex: 1 1 140px;">Where stored</span><span class="sb-th" style="flex: 1 1 130px;">Transfer safeguard</span><span class="sb-th" style="flex: 1 1 150px;">Contract</span><span class="sb-th" style="flex: 0 0 90px;">Review</span><span class="sb-th" style="flex: 0 0 120px;">State</span></div>
          <sc-for list="{{sups}}" as="r" hint-placeholder-count="16">
            <div class="sb-row" style="align-items: flex-start; padding-top: 9px; padding-bottom: 9px;">
              <span style="flex: 2 1 190px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b" style="font-size: 13px;">{{r.n}}</span><span class="sb-muted">{{r.p}}</span></span>
              <span style="flex: 2 1 190px; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span class="sb-sub">{{r.d}}</span><sc-if value="{{r.sp}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-warn" style="align-self: flex-start;">Special or criminal data</span></sc-if></span>
              <span class="sb-sub" style="flex: 1 1 140px; min-width: 0;">{{r.w}}</span>
              <span class="sb-sub" style="flex: 1 1 130px; min-width: 0;">{{r.tx}}</span>
              <span style="flex: 1 1 150px; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span class="sb-sub">{{r.c}}</span><sc-if value="{{r.canCheck}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" style="align-self: flex-start;" onClick="{{r.check}}">Contract checked</button></sc-if></span>
              <span class="sb-sub" style="flex: 0 0 90px;">{{r.rv}}</span>
              <span style="flex: 0 0 120px;"><span class="{{r.cls}}" style="white-space: normal;">{{r.state}}</span></span>
            </div>
          </sc-for>
          <div class="sb-row"><span class="sb-muted">Not processors, listed so nothing is missed: Companies House, CQC data, Ordnance Survey and HM Land Registry (public data we look up; only search terms leave us). The Interview Preparation Hub is our own system; its hosting is checked like a supplier. Each supplier is one record; the 7 with a live connection (Google Workspace, Stripe, Xero, DocuSeal, GoHighLevel, email sending and texts) also show on System health (board 86). Every processor needs a written contract (Art 28(3)).</span></div>
        </section>
        <div class="sx-inf"><span class="sx-b">What the client's Security page should say</span><span class="sb-sub">"Your Hub's database and files are in the UK. Some of our trusted suppliers process data elsewhere, under UK safeguards." It shows the list of suppliers from this screen, and the ICO registration number once it is entered on Go-live readiness.</span></div>
      </sc-if>

      <sc-if value="{{isExp}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card" aria-labelledby="ex-h">
          <div class="sb-head"><h2 id="ex-h" class="sb-h2">Exports register</h2><span class="sb-sub">Every export, its purpose and who approved it</span></div>
          <sc-for list="{{exps}}" as="x" hint-placeholder-count="5">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px;">
              <div style="display: flex; gap: 14px; align-items: flex-start; flex-wrap: wrap;">
                <span class="sb-sub" style="flex: 0 0 120px;">{{x.at}}</span>
                <span style="flex: 2 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">{{x.what}}</span><span class="sb-sub">{{x.who}}. {{x.n}}. Purpose: {{x.why}}</span></span>
                <span class="sb-sub" style="flex: 1 1 200px; min-width: 0;">{{x.ap}}</span>
                <span class="sb-sub" style="flex: 1 1 170px; min-width: 0;">{{x.exp}}</span>
                <span style="flex: 0 0 170px;"><span class="{{x.cls}}" style="white-space: normal;">{{x.state}}</span></span>
              </div>
              <sc-if value="{{x.open}}" hint-placeholder-val="{{ false }}">
                <div style="display: flex; flex-direction: column; gap: 8px; padding-left: 134px;">
                  <label class="sx-lbl" for="ex-ta">Your reason (written to the audit log)</label>
                  <textarea id="ex-ta" class="sx-ta" value="{{exR}}" onChange="{{onExR}}" placeholder="For example: outreach list for the Northshire framework; contact details only, link for 24 hours"></textarea>
                  <sc-if value="{{exErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Write a reason before you approve or decline.</span></sc-if>
                  <div style="display: flex; gap: 8px;"><button class="sb-btn b-pri" onClick="{{exYes}}">Approve the export</button><button class="sb-btn b-gh" onClick="{{exNo}}">Decline</button></div>
                </div>
              </sc-if>
            </div>
          </sc-for>
        </section>
        <div class="sx-cols">
          <section class="sb-card sx-pad" style="flex: 1 1 460px; min-width: 0; padding-top: 18px;" aria-labelledby="er-h">
            <h2 id="er-h" class="sb-h2">Export rules</h2>
            <ol class="sx-ol">
              <li>Consultants download single documents only; no bulk export.</li>
              <li>A bulk export needs approval by someone else, and appears here.</li>
              <li>Links expire after 24 hours. Every download is logged.</li>
              <li>Logins never appear in an export (locked).</li>
              <li>A client's own "Download everything" needs the mobile code when we hold their sign-in mailbox login.</li>
            </ol>
            <span class="sb-muted">Who may export is set per role on People and access (board 83).</span>
          </section>
          <section class="sb-card sx-pad" style="flex: 1 1 460px; min-width: 0; padding-top: 18px;" aria-labelledby="es-h">
            <h2 id="es-h" class="sb-h2">States</h2>
            <span class="sb-sub">Requested, Approved, Ready, Expired. Downloads outside an approved export, like the 38 single downloads on Sun 1 Nov, show here as flagged and open the incident on Security (board 84).</span>
          </section>
        </div>
      </sc-if>
'''

PRIV_S = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { t: 'ret', ver: 'v1', v2When: 'all', v2R: '', v2Err: false, v2Dec: '', v2As: 'collins', v2Reminded: false, sys: { gmail: true, dsl: true, ghl: true, iph: true }, stopR: '', stopErr: false, stopped: false,
      rel: {}, relAsk: {}, relR: {}, relErr: {}, nh: [], nhScope: '', nhWhy: '', nhErr: false,
      sr: { hub: true, gmail: true, drive: true, ghl: true, xero: true, dsl: true }, redacted: false, sendErr: false, rrSent: false,
      sup: 'all', supChk: {}, exR: '', exErr: false, exDec: '' };
  }
  renderVals() {
    const s = this.state;
''' + JSHELP + r'''
    const T = [['ret', 'Retention'], ['del', 'Deletions and holds'], ['rights', 'Rights requests (1)'], ['rec', 'Records'], ['sup', 'Suppliers'], ['exp', 'Exports']];
    const V1 = 'Kept until our work for the client ends';
    const SC = [
      ['Identity document images (passport, driving licence, proof of address)', V1, 'Deleted once the regulator has made its decision', 'Needed only for the regulator\'s checks. A record is kept: seen by, date, document type', 'Hub, Gmail, Drive, staff phones', 'p'],
      ['DBS certificate images', V1, 'Deleted once the regulator has made its decision', 'Criminal offence data (Art 10; DPA 2018 Schedule 1 condition: check). DBS guidance for registered bodies says normally no longer than 6 months: check whether it applies to us', 'Hub, Gmail, Drive, staff phones', 'p'],
      ['DBS record (number, issue date, who saw it, when)', '6 years after the work ends', '', 'Evidence of what we checked; contract claims (Limitation Act 1980 s.5)', 'Hub', 'p'],
      ['GP medical reference forms (CIW and RQIA)', 'Deleted once the regulator has made its decision', '', 'Health data (Art 9 condition: check)', 'Hub, Gmail', 'p'],
      ['CVs, employment history and references', '12 months after the work ends', '', 'Questions after registration', 'Hub, Gmail, Drive, Interview Preparation Hub', 'p'],
      ['Application packs, policies and plans we wrote', '6 years after the work ends', '', 'Contract claims (Limitation Act 1980 s.5)', 'Hub, Drive', 'p'],
      ['Engagement letters, agreements and signature records', '6 years after the work ends', '', 'Contract claims (Limitation Act 1980 s.5)', 'Hub, DocuSeal', 'c'],
      ['Invoices, payments and VAT records', '6 years after the financial year ends', '', 'HMRC record keeping (check); Companies Act 2006 s.388: 3 years for a private company\'s accounts (check)', 'Hub, Xero, Stripe', 'c'],
      ['Messages, emails and call notes with the client', '6 years after the work ends', '', 'Evidence of the advice we gave; complaints', 'Hub, Gmail, GoHighLevel', 'p'],
      ['Regulator letters filed from the client\'s mailbox', '6 years after the work ends', '', 'Evidence of the advice we gave', 'Hub', 'p'],
      ['Vault logins', 'Deleted at hand-back, at the end of the work', '', 'Settled in the design (spec 41.3)', 'Hub', 'c'],
      ['Voice notes', 'Deleted once transcribed and checked, unless the client asks to keep them', '', 'Settled in the design (spec 13)', 'Hub, speech-to-text supplier', 'c'],
      ['Prospects who did not buy (GoHighLevel, Tender Radar)', '2 years after the last contact', '', 'Legitimate interests (check)', 'GoHighLevel, Hub', 'p'],
      ['Call recordings (only with consent)', '90 days', '', 'Consent', 'GoHighLevel', 'p'],
      ['AI prompt logs', '30 days', '', 'Quality checks only', 'AI prompt log tool', 'p'],
      ['Audit log', '6 years', '', 'Evidence of who saw what; contract claims', 'Hub, write-once copy', 'p'],
      ['Staff Hub accounts after leaving', 'Disabled on the last day, deleted after 12 months; audit entries stay', '', 'HR records are kept separately', 'Hub, Google Workspace', 'p'],
      ['Backups', '35 days, rolling', '', 'Recovery after a failure', 'Backup account', 'p']
    ];
    const v2Approved = s.v2Dec === 'yes';
    const showV2 = s.ver === 'v2' || v2Approved;
    const sched = SC.map(([type, v1, v2, basis, sys, st]) => { const changed = !!v2 && showV2;
      return { type, period: changed ? v2 : v1, was: changed, wasText: v1, basis, sys, status: changed ? (v2Approved ? 'Live in v2, proposed for the data protection lead' : 'Changed in v2, waiting for Rachel Turner') : (st === 'c' ? 'Confirmed by the data protection lead' : 'Proposed, for the data protection lead'), cls: ch(changed ? (v2Approved ? 'info' : 'warn') : (st === 'c' ? 'ok' : 'neutral')) }; });
    const v2Open = !s.v2Dec;
    const v2Go = val => { if (!s.v2R.trim()) { this.setState({ v2Err: true }); return; } this.setState({ v2Dec: val, v2Err: false }); };
    const delDocs = [
      ['Passport (director)', 'Fernhill Homecare Ltd', '15 Oct 2026'], ['Driving licence (director)', 'Fernhill Homecare Ltd', '15 Oct 2026'], ['Utility bill (director)', 'Fernhill Homecare Ltd', '15 Oct 2026'], ['Passport (manager)', 'Fernhill Homecare Ltd', '15 Oct 2026'], ['Bank statement (manager)', 'Fernhill Homecare Ltd', '15 Oct 2026'],
      ['Passport (director)', 'Northgate Care Ltd', '22 Oct 2026'], ['Birth certificate (director)', 'Northgate Care Ltd', '22 Oct 2026'], ['Council tax bill (director)', 'Northgate Care Ltd', '22 Oct 2026'], ['Driving licence (manager)', 'Northgate Care Ltd', '22 Oct 2026'], ['Bank statement (manager)', 'Northgate Care Ltd', '22 Oct 2026'],
      ['Passport (director)', 'Bluebell Support Ltd', '31 Oct 2026'], ['Driving licence (director)', 'Bluebell Support Ltd', '31 Oct 2026'], ['Utility bill (manager)', 'Bluebell Support Ltd', '31 Oct 2026'], ['DBS certificate copy (manager)', 'Bluebell Support Ltd', '31 Oct 2026']
    ].map(([t, c, e]) => ({ t, c, e }));
    const DS = [
      ['gmail', 'Gmail: search staff mailboxes for these attachments', 'Rachel Turner. 3 found and deleted, trash emptied'],
      ['drive', 'Google Drive: staff working copies', 'Rachel Turner, by Fri 6 Nov'],
      ['phones', 'Staff phones: photos or downloads of these documents', 'Each case owner confirms, by Fri 6 Nov'],
      ['dsl', 'DocuSeal', 'Identity documents are never sent for signing. Confirmed not held'],
      ['ghl', 'GoHighLevel notes', 'Confirmed not held'],
      ['iph', 'Interview Preparation Hub', 'Confirmed not held'],
      ['bk', 'Backups', 'They expire by themselves by Mon 14 Dec (35 days after the run). Tick when confirmed']
    ];
    const delSys = DS.map(([id, t, note]) => { const done = !!s.sys[id]; return { t, note, done, state: done ? 'Cleared' : 'To do', cls: ch(done ? 'ok' : 'warn'), flip: () => this.setState({ sys: up(s.sys, id, !done) }) }; });
    const sysDone = delSys.filter(x => x.done).length;
    const HL = [
      ['inc', 'Sam Patel\'s account and the records of the 38 documents', 'Incident 2026-01, the bulk download (Security, board 84)', 'Placed by Rachel Turner, Mon 2 Nov 08:30. Review when the incident closes'],
      ['wb', 'Westbrook Care Ltd: everything', 'Refused. The appeal window to the tribunal closes Sun 22 Nov (worked out the safe way; confirm with a legal adviser) and the resubmission is under way', 'Placed by Collins, Mon 26 Oct. Review Mon 23 Nov'],
      ['sun', 'Sunrise Homecare Ltd: everything', 'Notice of Proposal. Written representations due by Tue 17 Nov', 'Placed by Collins, Thu 22 Oct. Review after CQC\'s decision']
    ].concat(s.nh.map((h, i) => ['n' + i, h.scope, h.why, 'Placed by Collins, just now. Review in 3 months']));
    const holds = HL.map(([id, scope, why, meta]) => { const released = !!s.rel[id]; const asking = !released && !!s.relAsk[id]; const r = s.relR[id] || '';
      return { scope, why: released ? why + '. Released: "' + s.rel[id] + '"' : why, meta, on: !released && !asking, asking, state: released ? 'Released' : 'On hold', cls: ch(released ? 'neutral' : 'warn'), r, err: !!s.relErr[id], relLabel: 'Reason for releasing ' + scope,
        release: () => this.setState({ relAsk: up(s.relAsk, id, true) }), cancel: () => this.setState({ relAsk: up(s.relAsk, id, false) }),
        onR: e => this.setState({ relR: up(s.relR, id, e.target.value), relErr: up(s.relErr, id, false) }),
        confirm: () => { if (!r.trim()) { this.setState({ relErr: up(s.relErr, id, true) }); return; } this.setState({ rel: up(s.rel, id, r.trim()) }); } }; });
    const holdsOn = holds.filter(h => h.state === 'On hold').length;
    const SR = [
      ['hub', 'The Hub', 'Found: the reference letter, our request email and 2 reminders'],
      ['gmail', 'Gmail', 'Found: 3 emails with Hannah'],
      ['drive', 'Google Drive', 'Nothing found'],
      ['ghl', 'GoHighLevel', 'Not held'],
      ['xero', 'Xero', 'Not held'],
      ['dsl', 'DocuSeal', 'Not held'],
      ['wa', 'Staff phones and WhatsApp', 'To search: ask the case owner who handled Northgate'],
      ['iph', 'Interview Preparation Hub', 'To search'],
      ['ai', 'AI prompt logs', 'To search: logs older than 30 days are already gone']
    ];
    const searched = SR.map(([id, t, note]) => { const done = !!s.sr[id]; return { t, note, done, state: done ? 'Searched' : 'To do', cls: ch(done ? 'ok' : 'warn'), flip: () => this.setState({ sr: up(s.sr, id, !done), sendErr: false }) }; });
    const srDone = searched.filter(x => x.done).length;
    const rrSteps = ['Received', 'Verifying', 'In progress', 'Sent', 'Closed'].map((label, i) => { const cur = s.rrSent ? 3 : 2; return { label, cls: i < cur ? 'st-done' : (i === cur ? 'st-now' : 'st-next') }; });
    const rrFacts = [
      ['Received', 'Wed 28 Oct, by email to hello@caresyncexperts.co.uk'],
      ['Person', 'Hannah Price, who gave a reference for Northgate Care Ltd\'s former manager (a closed client)'],
      ['Request', 'Access: what do you hold about me?'],
      ['Identity', 'Checked Thu 29 Oct: matched to the email address and phone number on the reference. No copy of ID kept'],
      ['Due', 'Fri 27 Nov (one month)'],
      ['Extension', 'Not needed'],
      ['Clock paused', 'No'],
      ['Owner', 'Collins, data protection lead'],
      ['Fee', 'None']
    ].map(([k, v]) => ({ k, v }));
    const sendRr = () => { if (srDone < SR.length || !s.redacted) { this.setState({ sendErr: true }); return; } this.setState({ rrSent: true, sendErr: false }); };
    const leftParts = []; if (srDone < SR.length) leftParts.push((SR.length - srDone) + ' systems still to search'); if (!s.redacted) leftParts.push('the redaction check');
    const ropa = [
      ['Registration work', 'Prepare and submit registrations', 'Directors, nominated individuals, managers: contact details, CVs, employment history, references', 'Contract with the client company; legitimate interests for the people in it (check)', 'Controller (check)', 'Hosting (UK), Google Workspace, DocuSeal, AI provider'],
      ['Identity and DBS checks', 'Evidence for the regulator\'s fit person checks', 'Identity documents; DBS certificates (criminal offence data)', 'Legitimate interests (check); Art 10 with a DPA 2018 Schedule 1 condition (check); appropriate policy document v1', 'Controller (check)', 'Hosting (UK)'],
      ['GP medical references', 'CIW and RQIA applications', 'Health data about managers and individuals', 'Art 9 condition: check', 'Controller (check)', 'Hosting (UK), Gmail'],
      ['Mailbox monitoring and sending as the client', 'Watch for regulator emails; send replies the client approved', 'Regulator emails only; never Hub sign-in or e-signature emails', 'Contract, with written authority in the engagement letter. DPIA done', 'Processor for the client (check)', 'Google or Microsoft connection'],
      ['The vault', 'Act on portals for the client', 'Logins to client accounts', 'Contract, with written authority. DPIA done', 'Controller (check)', 'Hosting (UK)'],
      ['AI drafting and checks', 'Staff drafting and quality checks', 'Client documents; never logins or ID numbers', 'Legitimate interests (check). DPIA done', 'Controller (check)', 'AI provider; AI prompt log tool'],
      ['Sales and prospecting', 'Find and contact providers who may need us', 'Names, work contact details, public CQC data', 'Legitimate interests (check); marketing email rules under PECR (check)', 'Controller', 'GoHighLevel'],
      ['Billing', 'Invoices, payments and VAT', 'Payer names, company details, payment records', 'Contract; legal obligation', 'Controller', 'Stripe, Xero'],
      ['Interview preparation', 'Practice and coaching for regulator interviews', 'Names, answers, session notes', 'Contract', 'Controller (check)', 'Interview Preparation Hub (our own)'],
      ['Staff and monitoring', 'Run the team; the audit log watches access', 'Staff details, sign-ins, actions', 'Contract; legitimate interests, explained in the staff privacy notice (check ICO employment monitoring guidance)', 'Controller', 'Google Workspace, Hub']
    ].map(([a, p, d, b, role, sp]) => ({ a, p, d, b, role, s: sp }));
    const dpias = [
      ['The Hub as a whole', 'UK hosting, encryption, two-step for staff, audit log, roles by client', 'v1 signed off Mon 28 Sep, during setup mode and before go-live. Owner Collins. Review Mon 29 Mar', 'Approved', 'ok', 'Residual risk: medium'],
      ['Mailbox monitoring and sending as the client', 'Files regulator emails only; never sign-in or e-signature emails; client mobile code when we hold the sign-in mailbox login', 'Owner Collins. Review Mon 29 Mar', 'Approved', 'ok', 'Residual risk: low'],
      ['The vault and stored authenticators', 'Reason for reveal and copy, reveal threshold, authenticators target 0', 'Owner Collins. Review due now: Willow Bank still has an authenticator held', 'Review due', 'warn', 'Residual risk: medium'],
      ['AI drafting on client documents', 'No logins or ID numbers sent; prompt logs kept 30 days; supplier terms to check', 'Owner Collins. Review Mon 29 Mar', 'Approved', 'ok', 'Residual risk: low'],
      ['Criminal offence data (DBS)', 'Images deleted once the regulator decides, if schedule v2 is approved; record kept', 'Owner Collins. Review after the v2 decision', 'Approved', 'ok', 'Residual risk: medium'],
      ['Bulk downloads and exports', 'New, from incident 2026-01: real-time alerts, no bulk export for consultants, export register', 'Owner Collins. Draft by Fri 20 Nov', 'Draft', 'info', 'Residual risk: to assess']
    ].map(([t, m, meta, state, k, res]) => ({ t, m, meta, state, cls: ch(k), res }));
    const notices = [
      ['Client privacy notice v1', 'Live since Thu 1 Oct, on the website and every client\'s privacy page', 'Live', 'ok'],
      ['Client privacy notice v1.1', 'Draft: adds the supplier list, "some of our trusted suppliers process data elsewhere under UK safeguards", how long we keep things (read from the schedule), and the ICO registration number once entered', 'Draft', 'info'],
      ['Staff privacy notice v1', 'Live since Thu 1 Oct. Explains the audit log and alerts (check ICO employment monitoring guidance)', 'Live', 'ok']
    ].map(([t, x, state, k]) => ({ t, x, state, cls: ch(k) }));
    const SU = [
      ['host', 'Hosting provider (name to confirm)', 'Database and files', 'All client data', true, 'UK (London) region', 'Check backups and support access', 'Signed before go-live (check the processing terms)', 'Sep 2027', 'ok'],
      ['gws', 'Google Workspace', 'Staff email, calendar, Drive, staff sign-in', 'Staff and client emails, working documents', true, 'Check', 'Check', 'Online processing terms accepted (record the date)', 'Dec 2026', 'chk'],
      ['ghl', 'GoHighLevel', 'Sales CRM, call recordings', 'Prospects\' and clients\' contact details, call notes', false, 'Check', 'Check', 'Check', 'Dec 2026', 'chk'],
      ['str', 'Stripe', 'Payments and instalments', 'Payer names; card details held by Stripe', false, 'Check', 'Check', 'Stripe terms accepted (record the date)', 'Dec 2026', 'chk'],
      ['xero', 'Xero', 'Accounts and invoices', 'Client company and contact names, amounts', false, 'Check', 'Check', 'Check', 'Dec 2026', 'chk'],
      ['dsl', 'DocuSeal', 'E-signatures', 'Signers\' names, emails, signatures', false, 'Cloud or our own hosting: check', 'Check', 'Check', 'Dec 2026', 'chk'],
      ['mail', 'Transactional email service (name to confirm)', 'Hub emails from hello@caresyncexperts.co.uk', 'Names, email addresses, message content', false, 'Check', 'Check', 'Check', 'Dec 2026', 'chk'],
      ['sms', 'Text message provider (name to confirm)', 'Sign-in codes, introduction call and urgent deadline texts', 'Mobile numbers, short messages', false, 'Check', 'Check', 'Check', 'Dec 2026', 'chk'],
      ['ai', 'AI provider (Claude)', 'Staff drafting and checks', 'Client documents (may include special category data)', true, 'Check', 'Check', 'Check', 'Dec 2026', 'chk'],
      ['lf', 'AI prompt log tool (Langfuse)', 'Quality checks on AI use', 'Prompts and answers, kept 30 days', true, 'Our own hosting or cloud: check', 'Check', 'Check', 'Dec 2026', 'chk'],
      ['stt', 'Speech-to-text provider (name to confirm)', 'Voice notes', 'Recordings until transcribed', false, 'Check', 'Check', 'Check', 'Dec 2026', 'chk'],
      ['virus', 'Virus scanning', 'Every file on upload', 'Files, briefly', true, 'Check (may run in our hosting)', 'Check', 'Check', 'Dec 2026', 'chk'],
      ['n8n', 'Automations tool (n8n)', 'Reminders, chasers and alerts', 'Names, dates, message content', false, 'Our own hosting: check', 'Check', 'Not needed if our own hosting (check)', 'Dec 2026', 'chk'],
      ['op', '1Password (interim)', 'Logins until moved into the vault', 'Logins', false, 'Check', 'Check', 'Ends after the clear-out, by Fri 13 Nov', 'Fri 13 Nov', 'end'],
      ['wa', 'WhatsApp Business (Meta)', 'Later phase: off', 'None yet', false, 'Check before use', 'Check before use', 'None yet', 'Before use', 'off'],
      ['ab', 'AssuredBid (partner)', 'Partner access to tender packs', 'None yet', false, 'Check before use', 'Check before use', 'Data sharing or processor agreement needed first', 'Before use', 'off']
    ];
    const SST = { ok: ['Approved', 'ok'], chk: ['Check', 'warn'], end: ['Ending', 'neutral'], off: ['Not live', 'neutral'], done: ['Contract checked', 'ok'] };
    const supF = { all: () => true, chk: r => r[9] === 'chk' && !s.supChk[r[0]], off: r => r[9] === 'off' || r[9] === 'end' };
    const sups = SU.filter(supF[s.sup]).map(r => { const st = (r[9] === 'chk' && s.supChk[r[0]]) ? 'done' : r[9];
      return { n: r[1], p: r[2], d: r[3], sp: r[4], w: r[5], tx: r[6], c: st === 'done' ? 'Checked by Collins, just now' : r[7], rv: r[8], state: SST[st][0], cls: ch(SST[st][1]), canCheck: st === 'chk', check: () => this.setState({ supChk: up(s.supChk, r[0], true) }) }; });
    const nChk = SU.filter(r => r[9] === 'chk' && !s.supChk[r[0]]).length;
    const exGo = val => { if (!s.exR.trim()) { this.setState({ exErr: true }); return; } this.setState({ exDec: val, exErr: false }); };
    const exps = [
      ['Today 08:55', 'Tender Radar prospects list (spreadsheet)', 'Jo Martin', '140 rows, contact details only', 'outreach for the Northshire framework', s.exDec === 'yes' ? 'Approved by Collins (data protection lead), just now: "' + s.exR.trim() + '"' : (s.exDec === 'no' ? 'Declined by Collins (data protection lead), just now: "' + s.exR.trim() + '"' : 'The data protection lead (Collins) decides. Jo cannot decide her own request. Not a super admin decision'), s.exDec === 'yes' ? 'Link expires Tue 3 Nov 09:20. Not downloaded yet' : 'No link yet', s.exDec === 'yes' ? 'Ready' : (s.exDec === 'no' ? 'Declined' : 'Requested'), s.exDec === 'yes' ? 'ok' : (s.exDec === 'no' ? 'neutral' : 'warn'), !s.exDec],
      ['Today 08:45', 'Sam Patel\'s audit entries, 1 Oct to 2 Nov', 'Rachel Turner', '212 rows', 'incident 2026-01', 'Collins, data protection lead; logged on Security', 'Link expires today 17:00. Downloaded', 'Ready', 'ok', false],
      ['Sun 1 Nov 21:40', '38 single downloads, not an export request', 'Sam Patel', '38 files from 6 clients', 'none given', 'No approval: single downloads added up to a bulk export', 'Downloaded to laptop CS-LT-07', 'Flagged: incident 2026-01', 'bad', false],
      ['Fri 30 Oct 16:00', 'October invoices list for the accountant', 'Femi Ade', '52 rows', 'month close', 'Approved by Collins', 'Expired Sat 31 Oct. Downloaded', 'Expired', 'neutral', false],
      ['Wed 28 Oct 19:30', 'Download everything: Bright Path Care Ltd', 'Joy Adeyemi (client)', '61 files', 'the client\'s own copy', 'The client\'s own right; no approval needed', 'Expired Thu 29 Oct. Downloaded', 'Expired', 'neutral', false]
    ].map(([at, what, who, n, why, ap, exp, state, k, open]) => ({ at, what, who, n, why, ap, exp, state, cls: ch(k), open }));

    return {
      theme: this.props.theme ?? 'light', three: 7, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      tiles: [
        ['ret', 'Retention schedule', v2Approved ? 'v2 live' : 'v1 live', v2Approved ? 'Approved just now' : (s.v2Dec === 'no' ? 'v2 declined' : 'v2 waiting for Rachel Turner'), v2Approved ? 'ok' : 'warn'],
        ['del', 'Next deletion run', s.stopped ? 'Stopped' : 'Mon 9 Nov', '14 identity documents', s.stopped ? 'warn' : 'neutral'],
        ['del', 'Legal holds', String(holdsOn), 'Incident, Westbrook, Sunrise', 'info'],
        ['rights', 'Open rights requests', s.rrSent ? '0' : '1', s.rrSent ? 'Sent today' : '25 days left: due Fri 27 Nov', s.rrSent ? 'ok' : 'warn'],
        ['sup', 'Suppliers to check', String(nChk), 'Where stored and safeguards', nChk ? 'warn' : 'ok'],
        ['exp', 'Exports waiting', s.exDec ? '0' : '1', s.exDec ? 'Decided' : 'Jo Martin\'s prospects list', s.exDec ? 'ok' : 'warn']
      ].map(([k, l, v, note, c]) => ({ k: l, v, note, cls: ch(c), aria: l + ': ' + v + '. ' + note + '. Open', go: () => this.setState({ t: k }) })),
      tabs: T.map(([k, label]) => ({ label, on: s.t === k, off: s.t !== k, pick: () => this.setState({ t: k }) })),
      isRet: s.t === 'ret', isDel: s.t === 'del', isRights: s.t === 'rights', isRec: s.t === 'rec', isSup: s.t === 'sup', isExp: s.t === 'exp',
      v2State: v2Approved ? 'Approved' : (s.v2Dec === 'no' ? 'Declined' : 'Waiting for Rachel Turner'), v2Cls: ch(v2Approved ? 'ok' : (s.v2Dec === 'no' ? 'neutral' : 'warn')),
      v2When: [['all', 'Everyone, from the next run'], ['new', 'New clients only']].map(([k, label]) => ({ label, on: s.v2When === k, off: s.v2When !== k, pick: () => this.setState({ v2When: k }) })),
      v2R: s.v2R, v2Err: s.v2Err, onV2R: e => this.setState({ v2R: e.target.value, v2Err: false }), v2Open, v2Done: !v2Open,
      v2As: [['collins', 'Collins (proposed it)'], ['rachel', 'Rachel Turner']].map(([k, label]) => ({ label, on: s.v2As === k, off: s.v2As !== k, pick: () => this.setState({ v2As: k, v2Err: false }) })),
      v2Own: v2Open && s.v2As === 'collins', v2CanDecide: v2Open && s.v2As === 'rachel',
      v2Remind: () => this.setState({ v2Reminded: true }), v2RemindNote: s.v2Reminded ? 'Rachel was reminded just now, in the Hub and by email.' : 'Rachel sees it on Home as decision 7.',
      v2Yes: () => v2Go('yes'), v2No: () => v2Go('no'), v2Box: v2Approved ? 'sx-ok' : 'sx-box',
      v2Head: v2Approved ? 'Approved by Rachel Turner, just now. Schedule v2 is live' : 'Declined by Rachel Turner, just now. v1 stays live; Collins is told',
      v2Note: (v2Approved ? (s.v2When === 'all' ? 'The next deletion run lists the 46 identity images and 12 DBS images, with 7 days\' notice. ' : 'Applies to clients added from today; existing clients stay on v1. ') + 'Account and the Security page now read v2. ' : '') + 'Reason: "' + s.v2R.trim() + '". Written to the audit log. Home shows 6 decisions waiting.',
      verTabs: [['v1', 'v1, live'], ['v2', 'v2, proposed']].map(([k, label]) => ({ label, on: s.ver === k, off: s.ver !== k, pick: () => this.setState({ ver: k }) })),
      verNote: showV2 ? 'Showing v2. The 2 changed rows show what v1 said.' : 'Showing v1, live since Thu 1 Oct. Switch to v2 to see the 2 proposed changes.', sched,
      runState: s.stopped ? 'Stopped' : 'Scheduled', runCls: ch(s.stopped ? 'warn' : 'info'), delDocs, delSys, sysCount: sysDone + ' of ' + delSys.length + ' cleared',
      runOpen: !s.stopped, runStopped: s.stopped, stopR: s.stopR, stopErr: s.stopErr, onStopR: e => this.setState({ stopR: e.target.value, stopErr: false }),
      stopRun: () => { if (!s.stopR.trim()) { this.setState({ stopErr: true }); return; } this.setState({ stopped: true }); }, restart: () => this.setState({ stopped: false, stopR: '' }),
      holds, holdCount: holdsOn + ' on hold', nhScope: s.nhScope, nhWhy: s.nhWhy, nhErr: s.nhErr,
      onNhScope: e => this.setState({ nhScope: e.target.value, nhErr: false }), onNhWhy: e => this.setState({ nhWhy: e.target.value, nhErr: false }),
      addHold: () => { if (!s.nhScope.trim() || !s.nhWhy.trim()) { this.setState({ nhErr: true }); return; } this.setState({ nh: s.nh.concat([{ scope: s.nhScope.trim(), why: s.nhWhy.trim() }]), nhScope: '', nhWhy: '' }); },
      rrState: s.rrSent ? 'Sent' : 'In progress', rrCls: ch(s.rrSent ? 'ok' : 'info'), rrSteps, rrFacts, searched, srCount: srDone + ' of ' + SR.length + ' searched',
      redacted: s.redacted, flipRed: () => this.setState({ redacted: !s.redacted, sendErr: false }),
      sendErr: s.sendErr, sendErrText: 'Before sending: ' + leftParts.join(' and ') + '.', rrOpen: !s.rrSent, rrSent: s.rrSent, sendRr,
      ropa, dpias, notices,
      supTabs: [['all', 'All (' + SU.length + ')'], ['chk', 'To check (' + nChk + ')'], ['off', 'Not live or ending']].map(([k, label]) => ({ label, on: s.sup === k, off: s.sup !== k, pick: () => this.setState({ sup: k }) })), sups,
      exps, exR: s.exR, exErr: s.exErr, onExR: e => this.setState({ exR: e.target.value, exErr: false }), exYes: () => exGo('yes'), exNo: () => exGo('no')
    };
  }
}'''

build_sa(os.path.join(OUT, 'DataPrivacy.dc.html'), 'Data and privacy', 'Data and privacy', H_PRIV, PRIV_B, PRIV_S, 'privacy', CSS)

# ---------------------------------------------------------------------------------------------
# 83. People and access
# ---------------------------------------------------------------------------------------------
PPL_B = header('People and access', 'The 10 people with access, what each role can do, joiners, leavers, the access review and cover. Shown at Monday 2 November, 09:20. Permission changes need the other super admin.') + TILES + tabs('People and access areas') + '''
      <sc-if value="{{isPeople}}" hint-placeholder-val="{{ true }}">
        <section class="sb-card" aria-labelledby="pp-h">
          <div class="sb-head"><h2 id="pp-h" class="sb-h2">People with access</h2><span class="sb-sub">Two-step status is read from Google Workspace at 06:00</span></div>
          <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 2 1 190px;">Person and role</span><span class="sb-th" style="flex: 2 1 200px;">Clients</span><span class="sb-th" style="flex: 2 1 190px;">Vault and export</span><span class="sb-th" style="flex: 0 0 120px;">Two-step</span><span class="sb-th" style="flex: 0 0 200px;">State</span></div>
          <sc-for list="{{people}}" as="p" hint-placeholder-count="10">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px;">
              <div style="display: flex; gap: 14px; align-items: flex-start;">
                <span style="flex: 2 1 190px; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span class="sx-b">{{p.name}}</span><span class="sb-muted">{{p.job}}</span><span style="display: flex; gap: 4px; flex-wrap: wrap;"><sc-for list="{{p.roles}}" as="r" hint-placeholder-count="2"><span class="{{r.cls}}">{{r.t}}</span></sc-for></span></span>
                <span class="sb-sub" style="flex: 2 1 200px; min-width: 0;">{{p.clients}}</span>
                <span class="sb-sub" style="flex: 2 1 190px; min-width: 0;">{{p.vault}}</span>
                <span style="flex: 0 0 120px;"><span class="{{p.twoCls}}" style="white-space: normal;">{{p.two}}</span></span>
                <span style="flex: 0 0 200px; display: flex; flex-direction: column; gap: 6px; align-items: flex-start;"><span class="{{p.cls}}" style="white-space: normal;">{{p.state}}</span><sc-if value="{{p.canSuspend}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" onClick="{{p.ask}}">Suspend now</button></sc-if></span>
              </div>
              <sc-if value="{{p.asking}}" hint-placeholder-val="{{ false }}">
                <div class="sx-amb" style="gap: 8px;">
                  <span class="sx-b">Suspend {{p.name}} now?</span>
                  <span class="sb-sub">Stops the Hub and Google Workspace at once, signs out every device and pauses downloads. Their clients stay with their cover or manager. Both super admins and the data protection lead are told.</span>
                  <input aria-label="{{p.rLabel}}" class="sx-in" value="{{p.r}}" onChange="{{p.onR}}" placeholder="Reason (written to the audit log)">
                  <sc-if value="{{p.err}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Write a reason first.</span></sc-if>
                  <div style="display: flex; gap: 8px;"><button class="sb-btn b-pri" onClick="{{p.go}}">Suspend now</button><button class="sb-btn b-gh" onClick="{{p.cancel}}">Cancel</button></div>
                </div>
              </sc-if>
            </div>
          </sc-for>
          <div class="sb-row"><span class="sb-muted">States: Invited, Active, Covering, Suspended, Leaving, Left. Directors and managers see all clients; everyone else sees assigned and covered clients. Menu items a role cannot use are hidden.</span></div>
        </section>
      </sc-if>

      <sc-if value="{{isRoles}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card" aria-labelledby="rg-h">
          <div class="sb-head"><h2 id="rg-h" class="sb-h2">Roles and permissions</h2><span class="sb-sub">Click a cell to change it. Nothing changes until the other super admin approves</span></div>
          <div style="overflow-x: auto; padding: 0 20px 16px;">
            <div style="display: grid; grid-template-columns: 150px repeat(8, minmax(0, 1fr)); gap: 6px; min-width: 1000px;">
              <span class="sb-th">Role</span>
              <sc-for list="{{areas}}" as="a" hint-placeholder-count="8"><span class="sb-th">{{a}}</span></sc-for>
              <sc-for list="{{grid}}" as="g" hint-placeholder-count="8">
                <span class="sx-b" style="font-size: 13px; line-height: 18px; align-self: center;">{{g.role}}</span>
                <sc-for list="{{g.cells}}" as="c" hint-placeholder-count="8"><button class="{{c.cls}}" aria-label="{{c.aria}}" onClick="{{c.next}}">{{c.t}}</button></sc-for>
              </sc-for>
            </div>
          </div>
          <sc-if value="{{hasChanges}}" hint-placeholder-val="{{ false }}">
            <div class="sx-pad">
              <div class="sx-amb" style="gap: 8px;">
                <span class="sx-b">{{chgHead}}</span>
                <sc-for list="{{chgList}}" as="x" hint-placeholder-count="2"><span style="font-size: 13px; line-height: 18px;">{{x}}</span></sc-for>
                <span class="sb-sub">{{chgImpact}}</span>
                <label class="sx-lbl" for="pc-ta">Reason (written to the audit log)</label>
                <textarea id="pc-ta" class="sx-ta" value="{{pcR}}" onChange="{{onPcR}}" placeholder="For example: finance needs to see the payment status of every client for month close"></textarea>
                <sc-if value="{{pcErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">Write a reason first.</span></sc-if>
                <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{sendPc}}">Send to Rachel Turner to approve</button><button class="sb-btn b-gh" onClick="{{resetPc}}">Undo the changes</button></div>
              </div>
            </div>
          </sc-if>
          <sc-if value="{{pcSent}}" hint-placeholder-val="{{ false }}"><div class="sx-pad"><div class="sx-inf"><span class="sx-b">Sent to Rachel Turner, just now</span><span class="sb-sub">It waits on Home as a new decision (8 waiting). The grid above shows the current permissions until she approves. Reason: "{{pcR}}"</span></div></div></sc-if>
        </section>
        <div class="sx-cols">
          <section class="sb-card sx-pad" style="flex: 1 1 460px; min-width: 0; padding-top: 18px;" aria-labelledby="sa-h">
            <h2 id="sa-h" class="sb-h2">Super admin: a flag on a role</h2>
            <div class="sx-kv" style="grid-template-columns: 140px minmax(0, 1fr);">
              <span>Holders</span><span>Collins (director, manager and data protection lead roles) and Rachel Turner (operations manager, manager role). Two named super admins, as go-live needs</span>
              <span>Adds</span><span>Enters prices; approves discounts, permission changes, form versions, emails with legal wording, retention changes, early deletions and break-glass. Reads and exports the whole audit log</span>
              <span>Rule</span><span>Nobody approves their own request. Inviting a super admin needs the other super admin</span>
              <span>Since</span><span>Setup mode ran Mon 14 Sep to Wed 30 Sep; dual control on since Thu 1 Oct</span>
            </div>
          </section>
          <section class="sb-card sx-pad" style="flex: 1 1 460px; min-width: 0; padding-top: 18px;" aria-labelledby="wr-h">
            <h2 id="wr-h" class="sb-h2">What each role sees inside a client</h2>
            <sc-for list="{{roleNotes}}" as="n" hint-placeholder-count="8">
              <div style="display: flex; gap: 10px;"><span class="sx-b" style="flex: 0 0 140px; font-size: 13px;">{{n.r}}</span><span style="font-size: 13px; line-height: 18px;">{{n.x}}</span></div>
            </sc-for>
          </section>
        </div>
      </sc-if>

      <sc-if value="{{isJoin}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card" aria-labelledby="jn-h">
          <div class="sb-head"><h2 id="jn-h" class="sb-h2">Joiner: Chloe Dunn, consultant, starts Mon 16 Nov</h2><span class="{{joinCls}}">{{joinState}}</span></div>
          <div class="sx-pad">
            <span class="sb-sub">Replaces Sam Patel's capacity. Line manager: Collins. Client scope: none until a manager assigns clients. Not yet one of the 10 people with access.</span>
            <div class="sx-col2">
              <div class="sx-box" style="gap: 8px;">
                <span class="sx-b">Gates before any client data</span>
                <sc-for list="{{gates}}" as="g" hint-placeholder-count="3">
                  <label class="sx-chk"><input type="checkbox" checked="{{g.done}}" onChange="{{g.flip}}"><span style="display: flex; flex-direction: column;"><span>{{g.t}}</span><span class="sb-muted">{{g.note}}</span></span></label>
                </sc-for>
                <div class="{{vaultBox}}"><span class="sx-b">{{vaultHead}}</span><span class="sb-sub">The vault and client documents open only when all 3 gates pass.</span></div>
              </div>
              <div class="sx-box" style="gap: 8px;">
                <span class="sx-b">Accounts in each system</span>
                <sc-for list="{{prov}}" as="x" hint-placeholder-count="7">
                  <div style="display: flex; gap: 10px; align-items: flex-start;"><label class="sx-chk" style="flex: 1; min-width: 0;"><input type="checkbox" checked="{{x.done}}" onChange="{{x.flip}}"><span style="display: flex; flex-direction: column;"><span>{{x.t}}</span><span class="sb-muted">{{x.note}}</span></span></label><span class="{{x.cls}}">{{x.state}}</span></div>
                </sc-for>
              </div>
            </div>
            <span class="sb-muted">Invites expire after 7 days and need two-step login. Once active, Chloe appears in Add a client, reassignment and cover lists.</span>
          </div>
        </section>
      </sc-if>

      <sc-if value="{{isLeave}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card" aria-labelledby="lv-h">
          <div class="sb-head"><h2 id="lv-h" class="sb-h2">Leaver: Sam Patel, consultant, last day Fri 6 Nov</h2><span class="sb-chip c-bad">Suspended</span></div>
          <div class="sx-pad">
            <div class="sx-red" style="flex-direction: row; gap: 14px; align-items: center; flex-wrap: wrap;">
              <span style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">Suspended since Mon 2 Nov 08:25 by Rachel Turner, pending the incident review</span><span class="sb-sub">"Suspend now" already ran: Hub and Google Workspace stopped, every device signed out, downloads paused since 08:10. Lifting it needs the incident to close and the other super admin. Incident 2026-01 is on Security (board 84).</span></span>
              <button class="sb-btn b-gh" onClick="{{noop}}" aria-disabled="true">{{suspLabel}}</button>
            </div>
            <div style="display: flex; flex-direction: column;">
              <div style="display: flex; justify-content: space-between; gap: 8px; padding-bottom: 6px;"><span class="sx-b">Every system</span><span class="sb-muted">{{lvCount}}</span></div>
              <sc-for list="{{leaver}}" as="x" hint-placeholder-count="12">
                <div style="display: flex; gap: 12px; align-items: flex-start; padding: 8px 0; border-top: 1px solid var(--cs-border-subtle);">
                  <label class="sx-chk" style="flex: 1; min-width: 0;"><input type="checkbox" checked="{{x.done}}" onChange="{{x.flip}}"><span style="display: flex; flex-direction: column;"><span class="sx-b">{{x.t}}</span><span class="sb-sub">{{x.note}}</span></span></label>
                  <span class="sb-muted" style="flex: 0 0 130px;">{{x.who}}</span>
                  <span style="flex: 0 0 100px;"><span class="{{x.cls}}">{{x.state}}</span></span>
                </div>
              </sc-for>
            </div>
            <div class="sx-col2">
              <div class="sx-box"><span class="sx-b">Sam's 6 clients</span><span class="sb-sub">Kingsway Care and Cedar Lodge Care move to Olu from Mon 9 Nov: asked by Grace on Fri 30 Oct 16:10, waiting for a super admin (decision 5 on Home). Rosehill Homecare, Thornbury Living, Hollybush Care and Bramley Support still need a new owner: reassign in Team and cover (board 78), each with a handover note.</span></div>
              <div class="sx-box"><span class="sx-b">This Friday</span><span class="sb-sub">Sam's 6 weekly updates due Fri 6 Nov are sent by Collins this week. Sam's Questions inbox items moved to Collins at 08:25.</span></div>
            </div>
          </div>
        </section>
      </sc-if>

      <sc-if value="{{isReview}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card" aria-labelledby="ar-h">
          <div class="sb-head"><h2 id="ar-h" class="sb-h2">Quarterly access review</h2><span class="{{revCls}}">{{revState}}</span></div>
          <div style="padding: 0 20px 12px;" class="sb-sub">Reviewers: Rachel Turner with Collins. Last review: at go-live, Thu 1 Oct. Brought forward because of Sam's leaving and the export incident: due by Fri 13 Nov. Mark each grant keep or remove, with a reason.</div>
          <sc-for list="{{grants}}" as="g" hint-placeholder-count="11">
            <div class="sb-row" style="align-items: flex-start; gap: 12px; flex-wrap: wrap;">
              <span style="flex: 2 1 300px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sx-b">{{g.who}}</span><span class="sb-sub">{{g.what}}</span></span>
              <input aria-label="{{g.rLabel}}" class="sx-in" style="flex: 1 1 220px; min-width: 0;" value="{{g.r}}" onChange="{{g.onR}}" placeholder="{{g.ph}}">
              <span style="display: flex; gap: 6px;"><sc-for list="{{g.opts}}" as="o" hint-placeholder-count="2"><sc-if value="{{o.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" aria-pressed="true" onClick="{{o.pick}}">{{o.label}}</button></sc-if><sc-if value="{{o.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" aria-pressed="false" onClick="{{o.pick}}">{{o.label}}</button></sc-if></sc-for></span>
            </div>
          </sc-for>
          <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px;">
            <span class="sb-sub">{{revProgress}}</span>
            <sc-if value="{{revErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">{{revErrText}}</span></sc-if>
            <sc-if value="{{revOpen}}" hint-placeholder-val="{{ true }}"><div><button class="sb-btn b-pri" onClick="{{signOff}}">Sign off the review</button></div></sc-if>
            <sc-if value="{{revDone}}" hint-placeholder-val="{{ false }}"><div class="sx-ok"><span class="sx-b">Signed off by Collins, Mon 2 Nov 09:20</span><span class="sb-sub">{{revDoneNote}}</span></div></sc-if>
            <span class="sb-muted">States: Due, In progress, Signed off, Overdue. The next review is due 3 months after sign-off.</span>
          </div>
        </section>
      </sc-if>

      <sc-if value="{{isCover}}" hint-placeholder-val="{{ false }}">
        <div class="sx-cols">
          <section class="sb-card" style="flex: 3 1 560px; min-width: 0;" aria-labelledby="co-h">
            <div class="sb-head"><h2 id="co-h" class="sb-h2">Cover delegations</h2><span class="sb-chip c-info">1 active</span></div>
            <div class="sx-pad">
              <div class="sx-box" style="gap: 8px;">
                <div style="display: flex; justify-content: space-between; gap: 8px;"><span class="sx-b">Daniel Mensah covers Olu</span><span class="sb-chip c-info">Active</span></div>
                <div class="sx-kv" style="grid-template-columns: 120px minmax(0, 1fr);">
                  <span>Leave</span><span>Olu, Mon 2 to Fri 6 Nov</span>
                  <span>Clients</span><span>Riverside Homecare, Greenway Support, Lagan View Care, Willow Bank Supported Living</span>
                  <span>Vault</span><span>Reveal included for those 4 clients only</span>
                  <span>Booked</span><span>Collins, Wed 28 Oct</span>
                  <span>Approved</span><span>Rachel Turner, Fri 30 Oct</span>
                  <span>Ends</span><span class="sx-b">Fri 6 Nov 17:30, by itself</span>
                </div>
                <span class="sb-muted">Brookside Homecare (aftercare, not urgent) waits for Olu. Every look Daniel takes shows on that client's privacy page. Details and early end: Security, Elevated access (board 84).</span>
              </div>
              <span class="sb-muted">Earlier cover since go-live: none. Planned leave always uses cover; break-glass is for emergencies only.</span>
            </div>
          </section>
          <section class="sb-card" style="flex: 2 1 380px; min-width: 0;" aria-labelledby="nc-h">
            <div class="sb-head"><h2 id="nc-h" class="sb-h2">Set up cover for leave</h2></div>
            <div class="sx-pad">
              <span class="sx-lbl">Who is away</span>
              ''' + subtabs('awayTabs', 'Who is away', 3) + '''
              <span class="sx-lbl">Who covers</span>
              ''' + subtabs('covTabs', 'Who covers', 3) + '''
              <label class="sx-lbl" for="nc-in">Dates</label>
              <input id="nc-in" class="sx-in" value="{{ncDates}}" onChange="{{onNcDates}}" placeholder="For example: Mon 23 to Fri 27 Nov">
              <label class="sx-chk"><input type="checkbox" checked="{{ncVault}}" onChange="{{flipNcVault}}"><span>Include vault reveal for the covered clients</span></label>
              <sc-if value="{{ncErr}}" hint-placeholder-val="{{ false }}"><span class="sx-err">{{ncErrText}}</span></sc-if>
              <div><button class="sb-btn b-sec" onClick="{{sendNc}}">Send to a manager to approve</button></div>
              <sc-if value="{{ncSent}}" hint-placeholder-val="{{ false }}"><div class="sx-inf"><span class="sx-b">{{ncHead}}</span><span class="sb-sub">Rachel Turner approves it (you booked it, so not you). It starts and ends by itself, and each client sees who is covering.</span></div></sc-if>
            </div>
          </section>
        </div>
      </sc-if>
'''

PPL_S = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { t: 'people', susp: {}, sAsk: {}, sR: {}, sErr: {}, perm: {}, pcR: '', pcErr: false, pcSent: false,
      gates: { conf: true }, prov: { gws: true, xero: true, stripe: true },
      lv: { hub: true, gws: true, xero: true, stripe: true, iph: true, pw: true },
      rv: {}, rvR: {}, revErr: false, revSigned: false, away: '', cov: '', ncDates: '', ncVault: true, ncErr: false, ncSent: false };
  }
  renderVals() {
    const s = this.state;
''' + JSHELP + r'''
    const T = [['people', 'People (10)'], ['roles', 'Roles and permissions'], ['join', 'Joiners (1)'], ['leave', 'Leavers (1)'], ['review', 'Access review'], ['cover', 'Cover (1)']];
    const RC = { 'Manager': 'c-info', 'Data protection lead': 'c-warn', 'Super admin': 'c-brand' };
    const P = [
      ['col', 'Collins', 'Director', ['Manager', 'Data protection lead', 'Super admin'], 'All clients', 'Vault: reveal for his own and covered clients; others by break-glass. Export: approves bulk exports; rights request and incident exports', 'Security key', 'ok', 'Active', 'ok'],
      ['rac', 'Rachel Turner', 'Operations manager', ['Manager', 'Super admin'], 'All clients', 'Vault: as a manager. Export: approves bulk exports', 'Security key', 'ok', 'Active', 'ok'],
      ['dan', 'Daniel Mensah', 'Consultant', ['Consultant'], '8 of his own, plus Olu\'s 4 covered until Fri 6 Nov 17:30', 'Vault: reveal for those 12. Export: single documents', 'App', 'ok', 'Covering Olu', 'info'],
      ['olu', 'Olu', 'Consultant', ['Consultant'], '5 of his own (4 covered by Daniel this week)', 'Vault: reveal for his 5. Export: single documents', 'App', 'ok', 'Active, on leave to Fri 6 Nov', 'neutral'],
      ['sam', 'Sam Patel', 'Consultant', ['Consultant'], '6, being reassigned', 'None while suspended', 'App', 'ok', 'Suspended since 08:25. Leaving Fri 6 Nov', 'bad'],
      ['gra', 'Grace', 'Onboarding lead', ['Onboarding lead'], '6 in onboarding, including Harbour Lane', 'Vault: add logins for onboarding clients, no reveal. Export: single documents', 'Security key', 'ok', 'Active', 'ok'],
      ['div', 'Divine', 'Client care', ['Client care'], 'Assigned: contact details and how clients feel', 'None', 'App', 'ok', 'Active', 'ok'],
      ['mil', 'Millicent', 'Coach', ['Coach'], 'Assigned: sessions only', 'None', 'App', 'ok', 'Active', 'ok'],
      ['jo', 'Jo Martin', 'Sales', ['Sales'], 'Prospects; existing clients only once the case owner agrees', 'Export: prospect lists, with approval', 'App', 'ok', 'Active', 'ok'],
      ['fem', 'Femi Ade', 'Finance, part time', ['Finance'], 'Billing details for all clients', 'Export: accountant exports, with approval', 'Text codes: weaker', 'warn', 'Active', 'ok']
    ];
    const people = P.map(([id, name, job, roles, clients, vault, two, twoK, state, k]) => { const sus = !!s.susp[id]; const asking = !sus && !!s.sAsk[id]; const r = s.sR[id] || '';
      return { name, job, roles: roles.map(t => ({ t, cls: 'sb-chip ' + (RC[t] || 'c-neutral') })), clients, vault: sus ? 'None while suspended' : vault, two, twoCls: ch(twoK),
        state: sus ? 'Suspended by Collins, just now: "' + r.trim() + '"' : state, cls: ch(sus ? 'bad' : k), canSuspend: id !== 'sam' && id !== 'col' && !sus && !asking, asking, r, err: !!s.sErr[id], rLabel: 'Reason for suspending ' + name,
        ask: () => this.setState({ sAsk: up(s.sAsk, id, true) }), cancel: () => this.setState({ sAsk: up(s.sAsk, id, false) }),
        onR: e => this.setState({ sR: up(s.sR, id, e.target.value), sErr: up(s.sErr, id, false) }),
        go: () => { if (!r.trim()) { this.setState({ sErr: up(s.sErr, id, true) }); return; } this.setState({ susp: up(s.susp, id, true) }); } }; });
    // Roles grid
    const areas = ['Clients', 'Vault', 'Export', 'Prices', 'Forms', 'Approvals', 'Money', 'Audit log'];
    const LV = [
      ['None', 'Assigned', 'Assigned and covered', 'Billing only, all', 'All'],
      ['None', 'Add only', 'Reveal: assigned and covered', 'Reveal: all, by break-glass'],
      ['None', 'Single documents', 'Bulk, with approval', 'Approves bulk'],
      ['None', 'View', 'Suggest', 'Enter (super admin)'],
      ['None', 'View', 'Draft', 'Approve (super admin)'],
      ['None', 'Gates', 'Handovers and cover', 'Data protection decisions', 'All (super admin)'],
      ['None', 'Payment status', 'View all', 'Manage'],
      ['None', 'Own actions', 'Team', 'All, read and export']
    ];
    const RG = [
      ['Manager', [4, 2, 3, 2, 1, 2, 2, 2]],
      ['Consultant', [2, 2, 1, 2, 1, 0, 1, 1]],
      ['Onboarding lead', [1, 1, 1, 2, 2, 1, 1, 1]],
      ['Client care', [1, 0, 0, 1, 1, 0, 1, 1]],
      ['Coach', [1, 0, 0, 0, 0, 0, 0, 1]],
      ['Sales', [1, 0, 2, 2, 0, 0, 0, 1]],
      ['Finance', [3, 0, 2, 1, 0, 0, 3, 1]],
      ['Data protection lead', [4, 2, 3, 2, 1, 3, 2, 3]]
    ];
    const changes = [];
    const grid = RG.map(([role, base]) => ({ role, cells: base.map((b, i) => { const key = role + '|' + i; const v = Object.prototype.hasOwnProperty.call(s.perm, key) ? s.perm[key] : b; const changed = v !== b;
      if (changed) changes.push(role + ', ' + areas[i] + ': ' + LV[i][b] + ' becomes ' + LV[i][v]);
      return { t: LV[i][v], cls: 'sx-cell' + (changed ? ' cell-ch' : (v === 0 ? ' cell-no' : '')), aria: role + ', ' + areas[i] + ': ' + LV[i][v] + '. Click to change',
        next: () => { const nv = (v + 1) % LV[i].length; const np = Object.assign({}, s.perm); if (nv === b) delete np[key]; else np[key] = nv; this.setState({ perm: np, pcSent: false, pcErr: false }); } }; }) }));
    const roleNotes = [['Manager', 'Everything in every client, and the money. Approves handovers and cover'], ['Consultant', 'Their own and covered clients in full'], ['Onboarding lead', 'Clients in onboarding: forms, gates, documents'], ['Client care', 'Contact details, how clients feel, payment status. Never the vault'], ['Coach', 'Session notes and interview practice only'], ['Sales', 'Prospects and the Radar; an existing client only once the case owner agrees'], ['Finance', 'Billing details, invoices and payments for every client; nothing else'], ['Data protection lead', 'As a manager, plus rights requests, incidents, retention and the whole audit log. Signs off form questions that collect special category, criminal offence or login data']].map(([r, x]) => ({ r, x }));
    const counts = { Manager: 2, Consultant: 3, 'Onboarding lead': 1, 'Client care': 1, Coach: 1, Sales: 1, Finance: 1, 'Data protection lead': 1 };
    const rolesHit = [...new Set(changes.map(c => c.split(',')[0]))];
    const nPeople = rolesHit.reduce((a, r) => a + (counts[r] || 0), 0);
    // Joiner
    const G1 = [['conf', 'Confidentiality agreement signed', 'Signed in DocuSeal, Fri 30 Oct'], ['train', 'Data protection training passed', 'Academy module, booked for Mon 16 Nov 09:30'], ['dev', 'Device check done', 'Laptop CS-LT-11: encryption, screen lock, managed by Google Workspace']];
    const gates = G1.map(([id, t, note]) => { const done = !!s.gates[id]; return { t, note, done, flip: () => this.setState({ gates: up(s.gates, id, !done) }) }; });
    const gDone = gates.filter(g => g.done).length;
    const PV = [
      ['gws', 'Google Workspace', 'Account created, suspended until Mon 16 Nov 08:00; two-step required'],
      ['hub', 'Hub', 'Invite sent on her first morning; consultant role; no clients until assigned'],
      ['iph', 'Interview Preparation Hub', 'Staff account through its API, after the gates'],
      ['ghl', 'GoHighLevel', 'User (not admin), to see her clients\' sales history'],
      ['dsl', 'DocuSeal', 'Sender, after the gates'],
      ['xero', 'Xero', 'Not needed for consultants'],
      ['stripe', 'Stripe', 'Not needed for consultants']
    ];
    const prov = PV.map(([id, t, note]) => { const done = !!s.prov[id]; const na = id === 'xero' || id === 'stripe'; return { t, note, done, state: na ? 'Not needed' : (done ? 'Done' : 'To do'), cls: ch(na ? 'neutral' : (done ? 'ok' : 'warn')), flip: () => this.setState({ prov: up(s.prov, id, !done) }) }; });
    const pDone = prov.filter(x => x.done).length;
    // Leaver
    const LS = [
      ['hub', 'Hub', 'Suspended Mon 2 Nov 08:25 by Rachel Turner pending the incident review; disabled for good Fri 6 Nov 17:30', 'Rachel Turner', 'Suspended'],
      ['gws', 'Google Workspace', 'Sign-in suspended 08:25 and every session signed out. Mail still arrives and forwards to Collins for 90 days', 'Collins', 'Suspended'],
      ['gmail', 'Gmail delegation and Drive ownership', 'Delegate access removed 08:25. 214 Drive files move to Collins on Fri 6 Nov, kept under the legal hold until the incident closes', 'Collins', ''],
      ['ghl', 'GoHighLevel', 'Deactivate Sam\'s user; notes and calls move to the new owners', 'Jo Martin', ''],
      ['xero', 'Xero', 'Consultants have no access: nothing to remove', 'None', 'Not used'],
      ['stripe', 'Stripe', 'Consultants have no access: nothing to remove', 'None', 'Not used'],
      ['dsl', 'DocuSeal', '2 envelopes waiting for signature move to the new owners; sender account closed', 'Collins', ''],
      ['iph', 'Interview Preparation Hub', 'Staff account disabled through its API at 08:26', 'The Hub', ''],
      ['dev', 'Devices returned', 'Laptop CS-LT-07 to Rachel today at 14:00 for the incident check; phone work profile wiped 08:25', 'Rachel Turner', ''],
      ['mbox', 'Client mailbox connections handed to the new owner', '3 connected under Sam (Kingsway, Rosehill, Hollybush). The watch keeps running under Collins until each new owner is approved', 'Collins', ''],
      ['tell', 'Clients told with email 9.3 "Your new consultant"', 'Sent to each client when their new owner is approved; their screens then show the new name. 0 of 6 sent', 'New case owners', ''],
      ['pw', 'Interim 1Password vault', 'Removed from the shared vault at 08:25', 'Collins', '']
    ];
    const leaver = LS.map(([id, t, note, who, fixed]) => { const done = !!s.lv[id]; return { t, note, who, done, state: done ? (fixed || 'Done') : 'To do', cls: ch(done ? (fixed === 'Suspended' ? 'bad' : (fixed === 'Not used' ? 'neutral' : 'ok')) : 'warn'), flip: () => this.setState({ lv: up(s.lv, id, !done) }) }; });
    const lvDone = leaver.filter(x => x.done).length;
    // Access review
    const GR = [
      ['dc', 'Daniel Mensah', 'Cover access to Olu\'s 4 clients, vault reveal included, ends Fri 6 Nov 17:30', 'keep', 'Approved cover; ends by itself'],
      ['sam', 'Sam Patel', 'All access (suspended, leaving Fri 6 Nov)', 'remove', 'Leaver'],
      ['jo', 'Jo Martin', 'GoHighLevel admin rights (a user account is enough)', 'remove', 'Least access'],
      ['fe', 'Femi Ade', 'Stripe admin, to prepare refunds a super admin approves', 'keep', ''],
      ['gr', 'Grace', 'Vault: add logins for onboarding clients, no reveal', 'keep', ''],
      ['mi', 'Millicent', 'Interview Preparation Hub admin', 'keep', ''],
      ['ol', 'Olu', 'Vault reveal for his 5 clients', 'keep', ''],
      ['sa', 'Collins and Rachel Turner', 'Super admin flag', 'keep', ''],
      ['keys', 'Integration keys', '5 keys (Stripe, Xero, DocuSeal, GoHighLevel, Google)', 'keep', ''],
      ['dev', 'Developers', 'Standing access to the live database: none (just in time only)', 'keep', ''],
      ['part', 'Partners', 'AssuredBid access: none yet', 'keep', '']
    ];
    const grants = GR.map(([id, who, what, sug]) => { const v = s.rv[id] || ''; const r = s.rvR[id] || '';
      return { who, what, r, rLabel: 'Reason for ' + who, ph: v === 'remove' ? 'Reason to remove (needed)' : 'Reason (needed to remove)', onR: e => this.setState({ rvR: up(s.rvR, id, e.target.value), revErr: false }),
        opts: [['keep', 'Keep'], ['remove', 'Remove']].map(([k, label]) => ({ label: label + (sug === k && !v ? ' (suggested)' : ''), on: v === k, off: v !== k, pick: () => this.setState({ rv: up(s.rv, id, k), revErr: false }) })) }; });
    const marked = GR.filter(g => s.rv[g[0]]).length;
    const removes = GR.filter(g => s.rv[g[0]] === 'remove');
    const missingR = removes.filter(g => !(s.rvR[g[0]] || '').trim()).length;
    const revState = s.revSigned ? 'Signed off' : (marked ? 'In progress' : 'Due by Fri 13 Nov');
    // Cover form
    const AW = [['grace', 'Grace'], ['mil', 'Millicent'], ['dan', 'Daniel Mensah']];
    const CV = [['olu', 'Olu'], ['rac', 'Rachel Turner'], ['col', 'Collins']];
    const nm = (L, k) => (L.find(x => x[0] === k) || ['', ''])[1];
    const ncProblem = !s.away || !s.cov ? 'Choose who is away and who covers.' : (!s.ncDates.trim() ? 'Add the dates.' : '');
    return {
      theme: this.props.theme ?? 'light', three: 7, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      tiles: [
        ['people', 'People with access', '10', '2 super admins', 'neutral'],
        ['people', 'Two-step sign-in', '10 of 10', '1 on text codes (Femi Ade)', 'warn'],
        ['join', 'Joiners', '1', 'Chloe Dunn, Mon 16 Nov', 'info'],
        ['leave', 'Leavers', '1', 'Sam Patel: suspended', 'bad'],
        ['review', 'Access review', s.revSigned ? 'Done' : 'Due', s.revSigned ? 'Signed off today' : 'By Fri 13 Nov', s.revSigned ? 'ok' : 'warn'],
        ['cover', 'Cover', '1 active', 'Daniel for Olu, to Fri 6 Nov', 'info']
      ].map(([k, l, v, note, c]) => ({ k: l, v, note, cls: ch(c), aria: l + ': ' + v + '. ' + note + '. Open', go: () => this.setState({ t: k }) })),
      tabs: T.map(([k, label]) => ({ label, on: s.t === k, off: s.t !== k, pick: () => this.setState({ t: k }) })),
      isPeople: s.t === 'people', isRoles: s.t === 'roles', isJoin: s.t === 'join', isLeave: s.t === 'leave', isReview: s.t === 'review', isCover: s.t === 'cover',
      people, areas, grid, roleNotes, hasChanges: changes.length > 0 && !s.pcSent, chgList: changes,
      chgHead: changes.length + (changes.length === 1 ? ' change' : ' changes') + ' to send for approval',
      chgImpact: 'Affects ' + nPeople + (nPeople === 1 ? ' person' : ' people') + ' today (' + rolesHit.join(', ') + '). Their menus and screens change once approved.',
      pcR: s.pcR, pcErr: s.pcErr, onPcR: e => this.setState({ pcR: e.target.value, pcErr: false }),
      sendPc: () => { if (!s.pcR.trim()) { this.setState({ pcErr: true }); return; } this.setState({ pcSent: true, perm: {} }); }, resetPc: () => this.setState({ perm: {}, pcErr: false }), pcSent: s.pcSent,
      gates, prov, joinState: gDone === 3 ? 'Ready to start' : 'Gates: ' + gDone + ' of 3', joinCls: ch(gDone === 3 ? 'ok' : 'warn'),
      vaultBox: gDone === 3 ? 'sx-ok' : 'sx-box', vaultHead: gDone === 3 ? 'All 3 gates passed: client data opens on Mon 16 Nov' : 'Client data closed: ' + gDone + ' of 3 gates passed. Accounts: ' + pDone + ' of 7',
      suspLabel: 'Suspended', noop: () => {}, leaver, lvCount: lvDone + ' of ' + leaver.length + ' done',
      grants, revState, revCls: ch(s.revSigned ? 'ok' : (marked ? 'info' : 'warn')), revProgress: marked + ' of ' + GR.length + ' grants marked. ' + removes.length + ' to remove.',
      revErr: s.revErr, revErrText: marked < GR.length ? 'Mark every grant first.' : 'Write a reason for each removal.', revOpen: !s.revSigned, revDone: s.revSigned,
      signOff: () => { if (marked < GR.length || missingR) { this.setState({ revErr: true }); return; } this.setState({ revSigned: true }); },
      revDoneNote: removes.length + ' grants are removed now, each logged with its reason. Next review due Tue 2 Feb.',
      awayTabs: AW.map(([k, label]) => ({ label, on: s.away === k, off: s.away !== k, pick: () => this.setState({ away: k, ncErr: false, ncSent: false }) })),
      covTabs: CV.map(([k, label]) => ({ label, on: s.cov === k, off: s.cov !== k, pick: () => this.setState({ cov: k, ncErr: false, ncSent: false }) })),
      ncDates: s.ncDates, onNcDates: e => this.setState({ ncDates: e.target.value, ncErr: false, ncSent: false }), ncVault: s.ncVault, flipNcVault: () => this.setState({ ncVault: !s.ncVault }),
      ncErr: s.ncErr, ncErrText: ncProblem || 'Check the details.', sendNc: () => { if (ncProblem) { this.setState({ ncErr: true }); return; } this.setState({ ncSent: true }); }, ncSent: s.ncSent,
      ncHead: 'Sent: ' + nm(CV, s.cov) + ' covers ' + nm(AW, s.away) + ', ' + s.ncDates.trim() + (s.ncVault ? ', vault reveal included' : ', no vault reveal')
    };
  }
}'''

build_sa(os.path.join(OUT, 'PeopleAccess.dc.html'), 'People and access', 'People and access', H_PPL, PPL_B, PPL_S, 'people', CSS)
