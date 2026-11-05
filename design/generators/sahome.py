# Super admin: Home (board 24), Go-live readiness (board 79), System health (board 86).
# Follows SP/superadmin/ia.md (agent A rows) and SP/superadmin/decisions.md.
# Run from SP/gen:  python3 sahome.py ../hub-canvas/project
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from staffboard import build_sa
OUT = sys.argv[1]

CSS = '''.bz-in{min-height:40px;padding:0 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;box-sizing:border-box}
.bz-ta{width:100%;min-height:60px;padding:8px 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;line-height:20px;box-sizing:border-box;resize:vertical}
.bz-in:focus-visible,.bz-ta:focus-visible,.bz-link:focus-visible,.bz-a:focus-visible,.bz-tile:focus-visible,.bz-rowbtn:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:2px}
.bz-err{font-size:13px;line-height:18px;color:var(--cs-status-error-text);font-weight:500}
.bz-box{padding:12px 14px;border-radius:10px;background:var(--cs-surface-subtle);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px;min-width:0}
.bz-red{padding:14px 16px;border-radius:12px;border:1px solid var(--cs-status-error-border);background:var(--cs-status-error-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-amb{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-warning-border);background:var(--cs-status-warning-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-ok{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-success-border);background:var(--cs-status-success-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-inf{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-info-border);background:var(--cs-status-info-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-lbl{font-size:12px;line-height:16px;color:var(--cs-text-muted);font-weight:500}
.bz-b{font-weight:500}
.bz-h3{margin:0;font-size:16px;line-height:22px;font-weight:600}
.bz-t15{font-size:15px;line-height:22px;font-weight:500}
.bz-link{display:inline-flex;align-items:center;justify-content:center;gap:8px;text-decoration:none;box-sizing:border-box}
.bz-a{color:var(--cs-text-brand);font-weight:500;font-size:14px;line-height:20px;text-decoration:underline;text-underline-offset:3px;border-radius:4px}
.bz-big{font-size:24px;line-height:32px;font-weight:600}
.bz-cols{display:flex;gap:18px;flex-wrap:wrap;align-items:flex-start}
.bz-g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.bz-g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.bz-g4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.bz-g5{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}
.bz-item{padding:16px 20px;border-top:1px solid var(--cs-border-subtle);display:flex;flex-direction:column;gap:10px}
.bz-ico{width:36px;height:36px;flex-shrink:0;border-radius:10px;background:var(--cs-surface-subtle);color:var(--cs-text-secondary);display:flex;align-items:center;justify-content:center}
.bz-tile{display:flex;flex-direction:column;gap:4px;padding:14px 16px;border-radius:12px;background:var(--cs-surface-raised);box-shadow:var(--cs-elevation-1);text-decoration:none;color:var(--cs-text-primary);min-width:0}
.bz-tile:hover{box-shadow:var(--cs-elevation-2)}
.bz-num{font-size:12px;line-height:16px;color:var(--cs-text-muted)}
.bz-dot{width:8px;height:8px;border-radius:999px;flex-shrink:0;display:inline-block}
.d-ok{background:var(--cs-status-success-text)}.d-warn{background:var(--cs-status-warning-text)}.d-bad{background:var(--cs-status-error-text)}.d-off{background:var(--cs-text-muted)}
.bz-rowbtn{width:100%;border:0;background:transparent;font:inherit;color:inherit;text-align:left;cursor:pointer;padding:12px 20px;display:flex;gap:14px;align-items:center;min-height:56px;box-sizing:border-box}
.bz-rowbtn:hover{background:var(--cs-action-ghost-hover)}
.bz-sel{background:var(--cs-surface-page)}
.bz-ul{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:4px}
.bz-step{display:flex;gap:12px;align-items:flex-start}
.bz-stepn{width:28px;height:28px;border-radius:999px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600}
.bz-mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;letter-spacing:0}
.bar.red span{background:var(--cs-status-error-text)}
.bar.amb span{background:var(--cs-status-warning-text)}
.bar.ok span{background:var(--cs-status-success-text)}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
'''

TABS = '''<div role="tablist" aria-label="__LABEL__" style="display: flex; gap: 6px; flex-wrap: wrap;">
          <sc-for list="{{__LIST__}}" as="tb" hint-placeholder-count="4">
            <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
            <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
          </sc-for>
        </div>'''
def tabs(lst, label):
    return TABS.replace('__LIST__', lst).replace('__LABEL__', label)

# Shared JS helpers (registry access with fallbacks, money).
JS_R = r'''const R = (window.CSR && typeof window.CSR.get === 'function') ? window.CSR : { get: (k, f) => f };
    const money = n => { const v = Number(n); return '£' + v.toLocaleString('en-GB', { minimumFractionDigits: (Math.round(v * 100) % 100) ? 2 : 0, maximumFractionDigits: 2 }); };'''

H = {}

# ====================================================================== 24. Home
B_HOME = '''      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 4px; flex: 1 1 560px; min-width: 0;">
          <span class="sb-muted">Super admin home. Monday 2 November, 09:20</span>
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">{{greeting}}</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">{{headline}}</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px; align-items: flex-end;">
          <span class="bz-lbl">Demo: see this page as</span>
          ''' + tabs('asTabs', 'Demo: see this page as') + '''
        </div>
      </div>

      <div class="bz-g5">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="5">
          <a class="bz-tile" href="{{k.href}}"><span class="sb-muted">{{k.k}}</span><span class="sb-kv">{{k.v}}</span><span class="{{k.cls}}" style="align-self: flex-start;">{{k.note}}</span></a>
        </sc-for>
      </div>

      <section class="bz-red" aria-labelledby="inc-h" style="flex-direction: row; gap: 20px; align-items: stretch; flex-wrap: wrap;">
        <div style="flex: 1 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 8px;">
          <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><span class="sb-chip c-bad">Open incident</span><span class="sb-chip c-warn">Assessing</span><h2 id="inc-h" class="bz-h3">Sam Patel exported 38 client documents</h2></div>
          <span>Sun 1 Nov at 21:40. Usual: under 5 a day. Sam leaves on Fri 6 Nov. The Hub flagged it at 06:00 today, so Care Sync became aware then and the clock started. Sam's downloads are paused. Collins, the data protection lead, started the breach assessment at 08:10 and leads it. Rachel Turner reviews the decision as the second pair of eyes.</span>
          <span class="sb-sub">Not yet decided whether it must be reported. If it must, the ICO expects it without undue delay and, where feasible, within 72 hours of becoming aware: by Thu 5 Nov 06:00. The decision and the reasons are recorded either way.</span>
        </div>
        <div style="flex: 0 1 300px; min-width: 240px; display: flex; flex-direction: column; gap: 6px; justify-content: center;">
          <span class="bz-lbl">72-hour window</span>
          <span class="bz-big">68 h 40 min left</span>
          <div class="bar red" aria-hidden="true"><span class="w5"></span></div>
          <span class="sb-muted">Started Mon 2 Nov 06:00. Ends Thu 5 Nov 06:00.</span>
          <a class="sb-btn b-pri bz-link" style="margin-top: 4px;" href="SecurityCentre.dc.html">Open the incident (Security, board 84)</a>
        </div>
      </section>

      <div class="bz-cols">
        <div style="flex: 3 1 620px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
          <section class="sb-card" aria-labelledby="dc-h">
            <div class="sb-head"><h2 id="dc-h" class="sb-h2">Decisions waiting for a super admin: {{pendingVal}}</h2><span class="sb-sub">{{decSub}}</span></div>
            <div style="padding: 0 20px 14px;">''' + tabs('decTabs', 'Filter decisions') + '''</div>
            <sc-for list="{{decs}}" as="a" hint-placeholder-count="7">
              <div class="bz-item">
                <div style="display: flex; gap: 12px; align-items: flex-start;">
                  <span class="bz-ico" aria-hidden="true"><x-import component-from-global-scope="CareSync.Icon" name="{{a.icon}}" size="{{n20}}"></x-import></span>
                  <div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;">
                    <span class="bz-num">{{a.num}}</span>
                    <span class="bz-t15">{{a.title}}</span>
                    <span class="sb-sub">{{a.change}}</span>
                    <span class="sb-muted">{{a.meta}}</span>
                  </div>
                  <div style="display: flex; flex-direction: column; gap: 8px; align-items: flex-end; flex-shrink: 0;">
                    <span class="{{a.chipCls}}">{{a.chip}}</span>
                    <button class="sb-btn b-gh" aria-expanded="{{a.exp}}" onClick="{{a.toggle}}">{{a.toggleLabel}}</button>
                  </div>
                </div>
                <sc-if value="{{a.isOpen}}" hint-placeholder-val="{{ false }}">
                  <div class="bz-g2">
                    <div class="bz-box"><span class="bz-lbl">{{a.extraLabel}}</span><sc-for list="{{a.extra}}" as="x" hint-placeholder-count="3"><span>{{x}}</span></sc-for></div>
                    <div class="bz-box"><span class="bz-lbl">What it affects</span><sc-for list="{{a.affects}}" as="x" hint-placeholder-count="4"><span>{{x}}</span></sc-for></div>
                  </div>
                  <sc-if value="{{a.isPerm}}" hint-placeholder-val="{{ false }}">
                    <div class="bz-g2">
                      <div class="bz-box"><span class="bz-lbl">Olu before</span><sc-for list="{{a.before}}" as="x" hint-placeholder-count="3"><span>{{x}}</span></sc-for></div>
                      <div class="bz-ok"><span class="bz-lbl">Olu after, from Mon 9 Nov</span><sc-for list="{{a.after}}" as="x" hint-placeholder-count="3"><span>{{x}}</span></sc-for></div>
                    </div>
                  </sc-if>
                  <div style="display: flex; gap: 14px; align-items: center; flex-wrap: wrap; justify-content: space-between;"><span class="sb-sub" style="flex: 1 1 360px;">{{a.clients}}</span><a class="bz-a" href="{{a.href}}">{{a.boardLabel}}</a></div>
                  <sc-if value="{{a.own}}" hint-placeholder-val="{{ false }}">
                    <div class="bz-amb" role="note">
                      <span class="bz-b">{{a.ownTitle}}</span>
                      <span class="sb-sub">{{a.ownText}}</span>
                      <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;"><button class="sb-btn b-sec" onClick="{{a.remind}}">{{a.remindLabel}}</button><span class="sb-muted">{{a.remindNote}}</span></div>
                    </div>
                  </sc-if>
                  <sc-if value="{{a.canDecide}}" hint-placeholder-val="{{ true }}">
                    <label class="bz-lbl" for="{{a.taId}}">Your reason (written to the audit log)</label>
                    <textarea id="{{a.taId}}" class="bz-ta" value="{{a.reason}}" onChange="{{a.onReason}}" placeholder="{{a.ph}}"></textarea>
                    <sc-if value="{{a.err}}" hint-placeholder-val="{{ false }}"><span class="bz-err" role="alert">Write a reason before you approve or decline.</span></sc-if>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{a.approve}}">{{a.approveLabel}}</button><button class="sb-btn b-gh" onClick="{{a.decline}}">Decline</button></div>
                  </sc-if>
                </sc-if>
                <sc-if value="{{a.done}}" hint-placeholder-val="{{ false }}">
                  <div class="{{a.doneBox}}"><span class="bz-b">{{a.doneText}}</span><span class="sb-sub">{{a.doneNote}}</span><div style="display: flex; gap: 8px;"><button class="sb-btn b-gh" onClick="{{a.undo}}">Undo (demo)</button></div></div>
                </sc-if>
              </div>
            </sc-for>
            <sc-if value="{{noDecs}}" hint-placeholder-val="{{ false }}"><div class="bz-item"><span class="sb-sub">Nothing in this group. Try All.</span></div></sc-if>
            <div style="padding: 12px 20px 16px; border-top: 1px solid var(--cs-border-subtle);" class="sb-muted">Nobody can approve their own request. Every decision is written to the audit log with the reason, and entries cannot be edited or deleted. In the Hub each super admin signs in with their own account and two-step login.</div>
          </section>

          <section class="sb-card" aria-labelledby="mg-h">
            <div class="sb-head"><h2 id="mg-h" class="sb-h2">Also waiting: 3</h2><span class="sb-sub">Not in the 7: none of these is a super admin decision. Two wait for a manager on the Manager dashboard (board 43); one waits for the data protection lead (Collins) on Data and privacy (board 85).</span></div>
            <sc-for list="{{mgr}}" as="m" hint-placeholder-count="3">
              <div class="sb-row" style="align-items: flex-start;">
                <span class="sb-chip c-info" style="width: 96px; justify-content: center; flex-shrink: 0;">{{m.kind}}</span>
                <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{m.title}}</span><span class="sb-sub">{{m.why}}</span></span>
                <a class="sb-btn b-gh bz-link" href="{{m.href}}">{{m.cta}}</a>
              </div>
            </sc-for>
          </section>

          <section class="sb-card" aria-labelledby="lg-h">
            <div class="sb-head"><h2 id="lg-h" class="sb-h2">Audit log: today</h2><a class="bz-a" href="SecurityCentre.dc.html">Full audit log (Security, board 84)</a></div>
            <sc-for list="{{log}}" as="l" hint-placeholder-count="5">
              <div class="sb-row" style="align-items: flex-start;"><span class="sb-sub" style="flex: 0 0 76px;">{{l.at}}</span><span class="bz-b" style="flex: 0 0 120px;">{{l.who}}</span><span style="flex: 1; min-width: 0;">{{l.what}}</span></div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">Entries cannot be edited or deleted. Your decisions on this page appear here straight away.</span></div>
          </section>
        </div>

        <div style="flex: 2 1 400px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="hl-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="hl-h" class="sb-h2">System health</h2><span class="sb-chip c-warn">13 of 15 healthy</span></div>
            <sc-for list="{{attn}}" as="t" hint-placeholder-count="2">
              <div style="display: flex; gap: 10px; align-items: flex-start;"><span class="bz-dot d-bad" style="margin-top: 7px;" aria-hidden="true"></span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column;"><span class="bz-b">{{t.k}}</span><span class="sb-sub">{{t.v}}</span></span></div>
            </sc-for>
            <div class="bz-red" style="gap: 8px;">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">Weekly update to Greenway Support</span><span class="{{fixChipCls}}">{{fixChip}}</span></div>
              <span class="sb-sub">The Friday 30 Oct update bounced at 17:02: the mailbox does not exist. It is waiting in Olu's outbox. Olu is on leave, so Daniel is covering and has been told.</span>
              <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-sec" aria-expanded="{{fixExp}}" onClick="{{toggleFix}}">Fix email address</button><button class="sb-btn b-gh" aria-expanded="{{logExp}}" onClick="{{toggleLog}}">See run log</button></div>
              <sc-if value="{{showFix}}" hint-placeholder-val="{{ false }}">
                <label class="bz-lbl" for="fx-in">Tunde Bello's email address</label>
                <input id="fx-in" class="bz-in" value="{{fixVal}}" onChange="{{onFix}}">
                <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{saveFix}}">Save and resend</button><span class="sb-muted" style="flex: 1 1 200px;">{{fixNote}}</span></div>
              </sc-if>
              <sc-if value="{{showLog}}" hint-placeholder-val="{{ false }}">
                <div style="display: flex; flex-direction: column; gap: 4px; padding-top: 6px; border-top: 1px solid var(--cs-status-error-border);">
                  <sc-for list="{{runLog}}" as="l" hint-placeholder-count="5"><span style="font-size: 13px; line-height: 18px;"><span class="bz-b">{{l.t}}</span> {{l.x}}</span></sc-for>
                </div>
              </sc-if>
            </div>
            <sc-for list="{{healthLines}}" as="t" hint-placeholder-count="3">
              <div style="display: flex; justify-content: space-between; gap: 10px; font-size: 14px; line-height: 20px;"><span class="sb-sub" style="flex: 0 0 96px;">{{t.k}}</span><span style="flex: 1; min-width: 0; text-align: right;">{{t.v}}</span></div>
            </sc-for>
            <span class="sb-muted">Every failure shows here and to its owner. Nothing fails silently.</span>
            <a class="sb-btn b-gh bz-link" href="Health.dc.html">Open System health (board 86)</a>
          </section>

          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="un-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="un-h" class="sb-h2">Unusual activity</h2><span class="sb-sub">Since Fri 30 Oct</span></div>
            <div class="{{unCls}}" role="status">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">Femi Ade signed in from a new device</span><span class="{{unChipCls}}">{{unChip}}</span></div>
              <span class="sb-sub">{{unText}}</span>
              <sc-if value="{{unOpen}}" hint-placeholder-val="{{ true }}">
                <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-sec" onClick="{{unLook}}">Look into it</button><button class="sb-btn b-gh" aria-expanded="{{unAskExp}}" onClick="{{unAsk}}">Mark as expected</button></div>
                <sc-if value="{{unAsking}}" hint-placeholder-val="{{ false }}">
                  <label class="bz-lbl" for="un-r">Why is it expected? (written to the audit log)</label>
                  <textarea id="un-r" class="bz-ta" value="{{unReason}}" onChange="{{onUnReason}}" placeholder="For example: Femi told me about the new laptop on Friday"></textarea>
                  <sc-if value="{{unErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err" role="alert">Write a reason first.</span></sc-if>
                  <div><button class="sb-btn b-pri" onClick="{{unFine}}">Mark as expected</button></div>
                </sc-if>
              </sc-if>
              <sc-if value="{{unLooked}}" hint-placeholder-val="{{ false }}"><a class="bz-a" href="SecurityCentre.dc.html">Open the assessment (Security, board 84)</a></sc-if>
            </div>
            <div class="bz-box">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">Sam Patel's export, Sun 1 Nov 21:40</span><span class="sb-chip c-bad">Now an incident</span></div>
              <span class="sb-sub">38 client documents, usual under 5 a day. Looked into at 06:00, downloads paused, breach assessment open (see the incident above).</span>
            </div>
          </section>

          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="ea-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="ea-h" class="sb-h2">Cover and emergency access</h2></div>
            <div class="bz-ok">
              <span class="bz-b">Cover: Daniel covers Olu's 4 clients</span>
              <span class="sb-sub">Riverside, Greenway, Lagan View and Willow Bank, including vault reveal for those 4 clients only. Olu is on leave Mon 2 to Fri 6 Nov. Approved by Rachel Turner on Fri 30 Oct. Ends automatically Fri 6 Nov 17:30.</span>
            </div>
            <span class="sb-sub">{{bgText}}</span>
            <a class="bz-a" href="PeopleAccess.dc.html">Cover and access (People and access, board 83)</a>
          </section>

          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="dp-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="dp-h" class="sb-h2">Data and privacy</h2></div>
            <sc-for list="{{dataLines}}" as="t" hint-placeholder-count="3">
              <div style="display: flex; flex-direction: column; gap: 2px; padding-top: 8px; border-top: 1px solid var(--cs-border-subtle);"><div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">{{t.k}}</span><span class="{{t.cls}}">{{t.chip}}</span></div><span class="sb-sub">{{t.v}}</span></div>
            </sc-for>
            <a class="bz-a" href="DataPrivacy.dc.html">Open Data and privacy (board 85)</a>
          </section>

          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="gl-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="gl-h" class="sb-h2">Go-live readiness</h2><span class="sb-chip c-warn">12 of 16 done</span></div>
            <div class="bar amb" aria-hidden="true"><span class="w75"></span></div>
            <span class="sb-sub">Live since Thu 1 Oct 2026, dual control on. Still open:</span>
            <ul class="bz-ul">
              <sc-for list="{{golive}}" as="g" hint-placeholder-count="4"><li style="font-size: 14px; line-height: 20px;">{{g}}</li></sc-for>
            </ul>
            <a class="bz-a" href="GoLive.dc.html">Open Go-live readiness (board 79)</a>
          </section>

        </div>
      </div>

      <section class="sb-card" aria-labelledby="ru-h">
        <div class="sb-head"><h2 id="ru-h" class="sb-h2">Promises in force today</h2><span class="sb-sub">Read from Rules and promises. Every screen and email uses the same values; a change shows where it is used, then needs approval.</span></div>
        <div class="bz-g5" style="padding: 0 20px 16px;">
          <sc-for list="{{rules}}" as="r" hint-placeholder-count="5">
            <div class="bz-box" style="gap: 2px;"><span class="bz-lbl">{{r.k}}</span><span class="bz-b">{{r.v}}</span></div>
          </sc-for>
        </div>
        <div style="padding: 0 20px 16px;"><a class="bz-a" href="Rules.dc.html">Open Rules and promises (board 80)</a></div>
      </section>

      <section class="sb-card" aria-labelledby="ws-h">
        <div class="sb-head"><h2 id="ws-h" class="sb-h2">Weekly super admin summary: Mon 26 Oct to Sun 1 Nov</h2><div style="display: flex; gap: 10px; align-items: center;"><span class="sb-sub">Sent to Collins and Rachel every Monday at 07:00</span><button class="sb-btn b-gh" aria-expanded="{{sumExp}}" onClick="{{toggleSum}}">{{sumLabel}}</button></div></div>
        <sc-if value="{{showSum}}" hint-placeholder-val="{{ true }}">
          <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));">
            <sc-for list="{{summary}}" as="w" hint-placeholder-count="8">
              <div class="sb-row" style="align-items: flex-start;"><span class="{{w.cls}}" style="width: 104px; justify-content: center; flex-shrink: 0;">{{w.k}}</span><span class="sb-sub" style="flex: 1; min-width: 0;">{{w.t}}</span></div>
            </sc-for>
          </div>
        </sc-if>
      </section>

      <section aria-labelledby="ql-h" style="display: flex; flex-direction: column; gap: 12px;">
        <h2 id="ql-h" class="sb-h2">Every area</h2>
        <div class="bz-g4">
          <sc-for list="{{areas}}" as="q" hint-placeholder-count="13">
            <a class="bz-tile" href="{{q.href}}">
              <span style="display: flex; gap: 10px; align-items: center;"><span class="bz-ico" aria-hidden="true"><x-import component-from-global-scope="CareSync.Icon" name="{{q.icon}}" size="{{n20}}"></x-import></span><span style="display: flex; flex-direction: column; min-width: 0;"><span class="bz-b" style="font-size: 15px; line-height: 20px;">{{q.name}}</span><span class="bz-num">{{q.num}}</span></span></span>
              <span class="sb-sub">{{q.note}}</span>
            </a>
          </sc-for>
        </div>
      </section>
'''

S_HOME = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { as: 'collins', dec: {}, by: {}, reasons: {}, errs: {}, open: { price: true }, f: 'all', reminded: {}, un: '', unAsking: false, unReason: '', unErr: false, showSum: true, showFix: false, showLog: false, fix: 'tunde@greenwaysupport.example', fixSaved: false };
  }
  renderVals() {
    const s = this.state;
    ''' + JS_R + r'''
    const vat = Number(R.get('vat-rate', 20));
    const full = Number(R.get('price-full', 8500));
    const third = Math.floor(full * 100 / 3) / 100;
    const lastPart = Math.round((full - 2 * third) * 100) / 100;
    const dom = Number(R.get('price-dom', 4000));
    const pir = Number(R.get('price-pir', 750));
    const day = R.get('weekly-update-day', 'Friday');
    const legalDays = R.get('nop-legal-days', 28);
    const bgHours = R.get('break-glass-hours', 4);
    const me = s.as;
    const meName = me === 'collins' ? 'Collins' : 'Rachel Turner';
    const otherFirst = me === 'collins' ? 'Rachel' : 'Collins';
    const names = { collins: 'Collins', rachel: 'Rachel Turner' };
    const base = [
      { id: 'price', type: 'money', icon: 'file-check', asker: 'collins', askerName: 'Collins',
        title: 'Price: Full start-up package, ' + money(full) + ' + VAT',
        change: 'A first price for the package. Until now each set-up was quoted before work started.',
        meta: 'Entered by Collins today. Waiting for Rachel Turner, who also checks ' + money(full) + ' against £8,000.',
        extraLabel: 'The change', extra: ['New price: ' + money(full) + ' + VAT (' + money(full * (1 + vat / 100)) + ' with VAT at ' + vat + '%)', '3 instalments: ' + money(third) + ', ' + money(third) + ' and ' + money(lastPart) + ' + VAT, at accept, sign and pay; final pack sign-off; submission', 'Still to check: ' + money(full) + ' or £8,000. Rachel confirms before approving.'],
        affects: ['Add a client (board 51): package price and instalments', 'Plan and costs (board 60) and Your account (board 29) for new clients', 'Stripe: the 3 instalment payments', 'Xero: invoice lines', 'Packages and journeys (board 81)'],
        clients: 'Clients affected today: none. New clients only, from the day it is approved. Signed clients keep their agreed price.',
        href: 'PriceBook.dc.html', boardLabel: 'Open in Price book (board 77)', approveLabel: 'Approve the price', ph: 'For example: checked against £8,000, ' + money(full) + ' is right',
        ok: 'The price is live for new clients from today, as version 1 in the price book. Add a client, Plan and costs and Stripe read it now.', log: 'the Full start-up package price, ' + money(full) + ' + VAT' },
      { id: 'lind', type: 'money', icon: 'trending-down', asker: 'jo', askerName: 'Jo Martin',
        title: 'Discount: Lindenfield Care Ltd, CQC domiciliary care',
        change: '£3,800 + VAT instead of ' + money(dom) + ' + VAT (' + money(dom - 3800) + ' off).',
        meta: 'Asked by Jo Martin from Add a client, today 08:05.',
        extraLabel: 'Why Jo asked', extra: ['Ready to sign today, and price is the last blocker.', 'Jo offered to trade scope first; the client wants the full package.', 'The price book itself does not change.'],
        affects: ['Lindenfield\'s agreement to sign (board 19)', 'Stripe: 2 instalments of £1,900 + VAT instead of ' + money(dom / 2) + ' + VAT', 'Xero: the invoice shows the discount line', 'Plan and costs (board 60) for this client', 'Money and exports (board 87): discounts given'],
        clients: 'Clients affected: 1 (Lindenfield Care Ltd, not yet signed).',
        href: 'PriceBook.dc.html', boardLabel: 'Open in Price book (board 77)', approveLabel: 'Approve the discount', ph: 'For example: full package, ready to sign today',
        ok: 'Jo is told. Lindenfield\'s agreement and Stripe instalments show £3,800 + VAT.', log: 'the discount for Lindenfield Care Ltd (£3,800 + VAT)' },
      { id: 'ashby', type: 'money', icon: 'trending-down', asker: 'daniel', askerName: 'Daniel Mensah',
        title: 'Discount: Ashby Care, PIR writing for 2 service types',
        change: '£1,350 + VAT instead of ' + money(2 * pir) + ' + VAT (2 PIRs at ' + money(pir) + ' + VAT).',
        meta: 'Asked by Daniel Mensah, Fri 30 Oct.',
        extraLabel: 'Why Daniel asked', extra: ['Aftercare client, month 12, handover 18 Nov, happy.', 'Both PIRs share most of the same evidence.', 'The price book itself does not change.'],
        affects: ['Ashby\'s agreement for the PIR work (board 19)', 'Stripe: the payment for this work', 'Xero: the invoice shows the discount line', 'Aftercare (board 71): Ashby\'s month 12 plan', 'Money and exports (board 87): discounts given'],
        clients: 'Clients affected: 1 (Ashby Care).',
        href: 'PriceBook.dc.html', boardLabel: 'Open in Price book (board 77)', approveLabel: 'Approve the discount', ph: 'For example: shared evidence, long-standing client',
        ok: 'Daniel is told. Ashby\'s agreement shows £1,350 + VAT.', log: 'the discount for Ashby Care (£1,350 + VAT for 2 PIRs)' },
      { id: 'form', type: 'content', icon: 'pencil-line', asker: 'grace', askerName: 'Grace',
        title: 'Form: CQC onboarding form, version 8',
        change: 'Adds a "Your office" step, rewords 1 question and removes "Type of Legal Entity".',
        meta: 'Drafted by Grace (onboarding lead), Thu 29 Oct. Collins or Rachel can approve.',
        extraLabel: 'What changes', extra: ['Added: a "Your office" step, which the office address gate needs', 'Reworded: 1 question (the old wording is shown on the Forms board)', 'Removed: "Type of Legal Entity" (Companies House already tells us)'],
        affects: ['Onboarding gates (board 8): Office address evidence reads the new step', 'Form received checks and the CQC application sheet (board 13)', 'Questions inbox (board 67): suggested replies follow the form\'s help text', 'Add a client (board 51): the form preview', 'The client\'s onboarding form (board 46)'],
        clients: 'Clients affected: 3 halfway through version 7 stay on it unless moved (answers kept). New clients get version 8 once approved.',
        href: 'FormBuilder.dc.html', boardLabel: 'Open in Forms (board 44)', approveLabel: 'Approve version 8', ph: 'For example: catches this month\'s office address fixes',
        ok: 'Version 8 is live for new clients. The 3 clients halfway through stay on version 7 unless Grace moves them. Grace is told.', log: 'version 8 of the CQC onboarding form' },
      { id: 'perm', type: 'people', icon: 'users', asker: 'grace', askerName: 'Grace', isPerm: true,
        title: 'Permission: Olu takes 2 of Sam Patel\'s clients',
        change: 'Kingsway Care Ltd and Cedar Lodge Care Ltd move from Sam Patel to Olu from Mon 9 Nov.',
        meta: 'Asked by Grace in Team and cover, Fri 30 Oct 16:10. Sam leaves Fri 6 Nov.',
        extraLabel: 'Why', extra: ['Sam Patel leaves on Fri 6 Nov; 2 of Sam\'s 6 clients go to Olu.', 'Olu is back from leave on Mon 9 Nov.', 'Handover notes for both clients are written.'],
        affects: ['People and access (board 83) and Team and cover (board 78)', 'Olu\'s My day (board 7) and weekly updates', 'Vault: reveal for these 2 clients moves to Olu; Sam\'s access ends Fri 6 Nov 17:30', 'Both clients see Olu as their consultant and get email 9.3, "Your new consultant"'],
        before: ['Case owner: 5 clients (Riverside, Greenway, Lagan View, Willow Bank, Brookside)', 'Vault: reveal for those 5', 'Weekly updates: 5'],
        after: ['Case owner: 7 clients (adds Kingsway Care and Cedar Lodge Care)', 'Vault: reveal for those 7', 'Weekly updates: 7'],
        clients: 'Clients affected: 2.',
        href: 'PeopleAccess.dc.html', boardLabel: 'Open in People and access (board 83)', approveLabel: 'Approve', ph: 'For example: Olu knows both services, handover notes written',
        ok: 'From Mon 9 Nov Olu is case owner for both clients. Grace and Olu are told.', log: 'the permission change for Olu (2 clients from Sam Patel, from Mon 9 Nov)' },
      { id: 'email', type: 'content', icon: 'inbox', asker: 'daniel', askerName: 'Daniel Mensah',
        title: 'Email: 5.2 Notice of Proposal, version 3',
        change: 'Clearer legal wording about the ' + legalDays + ' days, worked out the safe way: the day of service counts as day 1.',
        meta: 'Drafted by Daniel Mensah, Fri 30 Oct. Emails with legal wording need a super admin\'s approval.',
        extraLabel: 'Preview with Sunrise Homecare\'s dates', extra: ['Served: Wed 21 Oct (day 1)', 'Legal deadline for written representations: Tue 17 Nov (' + legalDays + ' days)', 'Our target to send: Tue 10 Nov, a week before', 'Shown with: "Worked out the safe way; confirm with a legal adviser"'],
        affects: ['Messages and automations (board 82): the email library', 'The client\'s CQC centre (board 5) shows the same dates', 'Deadlines (board 75) and the legal deadline alerts', 'Answer the regulator (board 76)'],
        clients: 'Clients with a Notice of Proposal today: 1 (Sunrise, already emailed on Wed 21 Oct; not sent again). Used for every new Notice of Proposal once approved.',
        href: 'Messages.dc.html', boardLabel: 'Open in Messages and automations (board 82)', approveLabel: 'Approve version 3', ph: 'For example: dates match the safe way of counting',
        ok: 'Version 3 is used for every new Notice of Proposal. Emails already sent do not change. Daniel is told.', log: 'version 3 of email 5.2 Notice of Proposal' },
      { id: 'ret', type: 'data', icon: 'file-clock', asker: 'collins', askerName: 'Collins',
        title: 'Retention schedule, version 2',
        change: 'Identity and DBS certificate images are deleted once the regulator has made its decision. A record stays: seen by, date, document type, DBS number and issue date.',
        meta: 'Proposed by Collins as data protection lead, Fri 30 Oct. Waiting for Rachel Turner, the other super admin.',
        extraLabel: 'The change', extra: ['Version 1: identity and DBS images kept until our work for the client ends', 'Version 2: deleted once the regulator decides, with a record kept', 'Everything else stays as in version 1', 'Deletions inside the schedule run automatically with 7 days\' notice'],
        affects: ['Data and privacy (board 85): the schedule and the deletion runs', 'Your account (board 29) and How we keep your information safe (board 62): "How long we keep things"', 'Form received (board 13): the record kept after deletion', 'The privacy notice: a new version'],
        clients: 'Applies to every client\'s identity and DBS images once their regulator decides.',
        href: 'DataPrivacy.dc.html', boardLabel: 'Open in Data and privacy (board 85)', approveLabel: 'Approve version 2', ph: 'For example: we only need the number and issue date after the decision',
        ok: 'Version 2 is live. The client privacy pages read the new wording. Collins is told.', log: 'version 2 of the retention schedule' }
    ];
    const set = (k, id, v) => this.setState({ [k]: Object.assign({}, s[k], { [id]: v }) });
    const all = base.map((a, i) => {
      const v = s.dec[a.id]; const r = (s.reasons[a.id] || '');
      const own = !v && a.asker === me;
      const isOpen = !!s.open[a.id];
      const go = val => { if (!r.trim()) { set('errs', a.id, true); return; } this.setState({ dec: Object.assign({}, s.dec, { [a.id]: val }), by: Object.assign({}, s.by, { [a.id]: me }), errs: Object.assign({}, s.errs, { [a.id]: false }) }); };
      const byName = names[s.by[a.id]] || meName;
      return Object.assign({ isPerm: false, before: [], after: [] }, a, {
        num: 'Decision ' + (i + 1) + ' of 7',
        isOpen, exp: isOpen ? 'true' : 'false', toggle: () => set('open', a.id, !isOpen), toggleLabel: isOpen ? 'Close' : 'Open details',
        own, canDecide: !v && !own, done: !!v, reason: r, err: !!s.errs[a.id], taId: 'r-' + a.id,
        ownTitle: (a.asker === 'collins' ? 'Rachel' : 'Collins') + ' must approve this',
        ownText: (a.id === 'price' ? 'You entered this price' : 'You proposed this change') + ', and nobody can approve their own request. It waits for ' + (a.asker === 'collins' ? 'Rachel Turner' : 'Collins') + '.',
        remind: () => set('reminded', a.id, true), remindLabel: 'Remind ' + otherFirst,
        remindNote: s.reminded[a.id] ? otherFirst + ' was reminded just now, in the Hub and by email.' : '',
        onReason: e => this.setState({ reasons: Object.assign({}, s.reasons, { [a.id]: e.target.value }), errs: Object.assign({}, s.errs, { [a.id]: false }) }),
        approve: () => go('yes'), decline: () => go('no'),
        undo: () => { const d = Object.assign({}, s.dec); delete d[a.id]; this.setState({ dec: d }); },
        chip: v ? (v === 'yes' ? 'Approved' : 'Declined') : (a.asker === me ? 'Waiting for ' + otherFirst : 'Waiting for you'),
        chipCls: 'sb-chip ' + (v ? (v === 'yes' ? 'c-ok' : 'c-neutral') : (a.asker === me ? 'c-neutral' : 'c-warn')),
        doneBox: v === 'yes' ? 'bz-ok' : 'bz-box',
        doneText: v === 'yes' ? 'Approved by ' + byName + ', just now. ' + a.ok : 'Declined by ' + byName + ', just now. ' + a.askerName + ' is told, with the reason. Nothing changes.',
        doneNote: 'Reason: "' + r.trim() + '". Written to the audit log.'
      });
    });
    const pending = all.filter(a => !a.done).length;
    const mine = all.filter(a => !a.done && !a.own).length;
    const others = pending - mine;
    const F = { all: null, money: ['money'], content: ['content'], people: ['people'], data: ['data'] };
    const cnt = k => all.filter(a => !a.done && (!F[k] || F[k].includes(a.type))).length;
    const decs = all.filter(a => !F[s.f] || F[s.f].includes(a.type));
    const nav = __NAV__;
    if (pending) nav[1].items[0].badge = { text: String(pending), status: 'warning' }; else delete nav[1].items[0].badge;
    const L = [
      ['08:55', 'Jo Martin', 'asked to export the Tender Radar prospects list (140 rows); the data protection lead decides on Data and privacy'],
      ['08:50', 'Collins', 'viewed Harbour Lane Care Ltd as Amara saw it on Fri 30 Oct, reason "Complaint check C-001". Read only; ended 09:02 (12 minutes)'],
      ['08:25', 'Rachel Turner', 'suspended Sam Patel\'s access pending the incident review'],
      ['08:10', 'Collins', 'started the breach assessment, as data protection lead, for Sam Patel\'s export; awareness time Mon 2 Nov 06:00'],
      ['08:05', 'Jo Martin', 'asked for a discount for Lindenfield Care Ltd from Add a client'],
      ['06:01', 'The Hub', 'paused Sam Patel\'s downloads and told both super admins'],
      ['06:00', 'The Hub', 'flagged unusual activity: Sam Patel exported 38 client documents on Sun 1 Nov at 21:40'],
      ['06:00', 'The Hub', 'gave 7 days\' notice of the Mon 9 Nov deletion run (14 identity documents, legal hold check clear)']
    ];
    const newLog = base.filter(a => s.dec[a.id]).map(a => ['09:20', names[s.by[a.id]] || meName, (s.dec[a.id] === 'yes' ? 'approved ' : 'declined ') + a.log + '. Reason: "' + (s.reasons[a.id] || '').trim() + '"']);
    const unLog = s.un === 'look' ? [['09:20', meName, 'started a breach assessment for Femi Ade\'s new device sign-in']] : (s.un === 'fine' ? [['09:20', meName, 'marked Femi Ade\'s new device sign-in as expected. Reason: "' + s.unReason.trim() + '"']] : []);
    const fixLog = s.fixSaved ? [['09:20', meName, 'changed Greenway Support\'s email address to ' + s.fix + '; the resend waits for Daniel to confirm it with Tunde']] : [];
    const remLog = Object.keys(s.reminded).filter(k => s.reminded[k]).map(() => ['09:20', meName, 'sent ' + otherFirst + ' a reminder about a decision only ' + otherFirst + ' can make']);
    const log = newLog.concat(unLog, fixLog, remLog, L).map(([at, who, what]) => ({ at, who, what }));
    const unText = s.un === 'look' ? 'Breach assessment started on Security (board 84). The new device is paused until Femi confirms it. Collins leads it as data protection lead; Rachel Turner is told.' : (s.un === 'fine' ? 'Marked as expected: "' + s.unReason.trim() + '". Written to the audit log.' : 'Sun 1 Nov at 22:15, a new laptop. Two-step login passed. Femi opened the Xero sync page only. Usual: weekdays, on the office laptop.');
    return {
      theme: this.props.theme ?? 'light', n20: 20, nav,
      user: me === 'collins' ? { name: 'Collins', initials: 'C' } : { name: 'Rachel Turner', initials: 'RT' },
      three: pending,
      asTabs: [['collins', 'Collins'], ['rachel', 'Rachel Turner']].map(([k, label]) => ({ label, on: me === k, off: me !== k, pick: () => this.setState({ as: k }) })),
      greeting: 'Good morning, ' + (me === 'collins' ? 'Collins' : 'Rachel'),
      headline: (pending === 0 ? 'No decisions are waiting.' : pending + (pending === 1 ? ' decision waits' : ' decisions wait') + ' for a super admin.') + ' 1 open incident, 68 hours 40 minutes left on the clock. 13 of 15 connections healthy.',
      pendingVal: String(pending),
      decSub: pending === 0 ? 'All decided' : (mine + ' you can decide' + (others ? ', ' + others + (others === 1 ? ' needs ' : ' need ') + otherFirst : '')),
      decTabs: [['all', 'All'], ['money', 'Prices and discounts'], ['content', 'Forms and emails'], ['people', 'People'], ['data', 'Data']].map(([k, label]) => ({ label: label + ' ' + cnt(k), on: s.f === k, off: s.f !== k, pick: () => this.setState({ f: k }) })),
      decs, noDecs: decs.length === 0,
      kpis: [
        ['Decisions waiting', String(pending), pending ? mine + ' you can decide' : 'All clear', pending ? 'warn' : 'ok', '#dc-h'],
        ['Open incident', '68 h 40 min', 'To Thu 5 Nov 06:00', 'bad', 'SecurityCentre.dc.html'],
        ['Connections', '13 of 15', '2 need attention', 'warn', 'Health.dc.html'],
        ['Go-live readiness', '12 of 16', '4 still open', 'warn', 'GoLive.dc.html'],
        ['People with access', '10', 'Sam Patel suspended, leaves Fri', 'neutral', 'PeopleAccess.dc.html']
      ].map(([k, v, note, c, href]) => ({ k, v, note, href, cls: 'sb-chip c-' + c })),
      mgr: [
        ['Handover', 'Binnian Care Ltd: approve the handover', 'Grace asked Collins to approve the handover from onboarding to the case owner. A Northern Ireland company.', 'Handover.dc.html', 'Open handover'],
        ['Bid work', 'Accept the bid work: Maple Court Care, Northshire Lot 2 South', 'Oakleaf Living already bids on Lot 1 North of the same framework, so a director accepts the work.', 'ManagerDash.dc.html', 'Open dashboard'],
        ['Export', 'Jo Martin\'s export request: Tender Radar prospects list', '140 rows, contact details only, for Northshire outreach. Decided by the data protection lead (Collins) on Data and privacy. Not a super admin decision, and Jo cannot decide her own request.', 'DataPrivacy.dc.html', 'Open exports']
      ].map(([kind, title, why, href, cta]) => ({ kind, title, why, href, cta })),
      log,
      attn: [
        ['CQC email watch: Riverside Homecare', 'Login not in the vault for 10 days (red after ' + R.get('watch-gap-red-days', 7) + '). CQC emails to Mark are not seen.'],
        ['Email delivery: Greenway Support', 'Tunde Bello\'s address bounced on Fri 30 Oct at 17:02.']
      ].map(([k, v]) => ({ k, v })),
      fixChip: s.fixSaved ? 'Waiting for Daniel' : 'Failed', fixChipCls: 'sb-chip ' + (s.fixSaved ? 'c-warn' : 'c-bad'),
      showFix: s.showFix, showLog: s.showLog, fixExp: s.showFix ? 'true' : 'false', logExp: s.showLog ? 'true' : 'false',
      toggleFix: () => this.setState({ showFix: !s.showFix }), toggleLog: () => this.setState({ showLog: !s.showLog }),
      fixVal: s.fix, onFix: e => this.setState({ fix: e.target.value, fixSaved: false }), saveFix: () => this.setState({ fixSaved: true }),
      fixNote: s.fixSaved ? 'Saved. The resend waits until Daniel confirms the address with Tunde by phone.' : 'The current address bounced. Check it with the client first.',
      runLog: [['Fri 30 Oct 17:00', 'weekly update built from the week\'s progress'], ['17:01', 'sent to tunde@greenwaysupport.example'], ['17:02', 'bounced: the mailbox does not exist'], ['17:02', 'moved to Olu\'s outbox; Olu and Daniel told'], ['Mon 2 Nov 07:00', 'still waiting; Daniel covering this week']].map(([t, x]) => ({ t, x })),
      healthLines: [['Automations', '46 on, 1 failed this week, 0 waiting to retry'], ['Backups', 'Nightly 02:00 done'], ['Restore test', 'Tue 13 Oct, passed. Next by Mon 11 Jan']].map(([k, v]) => ({ k, v })),
      unCls: s.un ? (s.un === 'look' ? 'bz-inf' : 'bz-box') : 'bz-amb', unChip: s.un === 'look' ? 'Assessing' : (s.un === 'fine' ? 'Expected' : 'New'), unChipCls: 'sb-chip ' + (s.un === 'look' ? 'c-info' : (s.un === 'fine' ? 'c-ok' : 'c-warn')),
      unText, unOpen: !s.un, unLooked: s.un === 'look', unAsking: s.unAsking, unAskExp: s.unAsking ? 'true' : 'false',
      unLook: () => this.setState({ un: 'look', unAsking: false }), unAsk: () => this.setState({ unAsking: !s.unAsking }),
      unReason: s.unReason, unErr: s.unErr, onUnReason: e => this.setState({ unReason: e.target.value, unErr: false }),
      unFine: () => { if (!s.unReason.trim()) { this.setState({ unErr: true }); return; } this.setState({ un: 'fine', unAsking: false }); },
      bgText: 'Break-glass: none in the last 30 days. It is for emergencies only: ' + bgHours + ' hours, approved by a super admin who is not the requester, both super admins and the client told the same day, reviewed within 1 working day.',
      dataLines: [
        ['Rights request: a former referee', 'Asks what Care Sync holds about them. Received Wed 28 Oct by email, identity checked. Due Fri 27 Nov.', 'Open', 'c-info'],
        ['Deletion run: Mon 9 Nov', '14 identity documents from 3 closed clients (Fernhill, Northgate, Bluebell). Runs automatically after 7 days\' notice. Legal hold check clear.', 'Scheduled', 'c-neutral'],
        ['Retention schedule', 'Version 1 live. Version 2, proposed by Collins, waits for Rachel Turner (decision 7).', 'Waiting', 'c-warn']
      ].map(([k, v, chip, c]) => ({ k, v, chip, cls: 'sb-chip ' + c })),
      golive: ['ICO registration number: not entered, so the Security page claim stays hidden', '6 prices still to set', 'Full start-up price check: ' + money(full) + ' or £8,000 (decision 1)', 'Trustpilot review link not yet added'],
      rules: [
        ['Weekly update', 'Every ' + day + ' by ' + R.get('weekly-update-time', '16:00')],
        ['Reply to clients', 'Within ' + R.get('reply-client', '1 working day')],
        ['Senior questions', 'Within ' + R.get('reply-senior', '2 working hours')],
        ['Quiet hours', R.get('quiet-hours', '8pm to 8am') + ', automated emails and texts'],
        ['Break-glass', 'Emergencies only, ' + bgHours + ' hours']
      ].map(([k, v]) => ({ k, v })),
      showSum: s.showSum, sumExp: s.showSum ? 'true' : 'false', toggleSum: () => this.setState({ showSum: !s.showSum }), sumLabel: s.showSum ? 'Hide' : 'Show',
      summary: [
        ['Decisions', '3 decided last week, all with a reason. 7 wait today: 5 Collins can decide, 2 need Rachel (the price Collins entered and the retention schedule Collins proposed).', 'c-info'],
        ['Security', 'Sam Patel\'s Sunday night export, flagged 06:00 Monday. Now an incident being assessed.', 'c-bad'],
        ['Access', 'Every vault reveal and copy had a reason. No break-glass. Cover for Olu\'s 4 clients approved by Rachel on Fri 30 Oct.', 'c-brand'],
        ['Automations', '1,284 runs, 1 failure: the Greenway weekly update bounce.', 'c-bad'],
        ['Connections', '13 of 15 healthy. CQC email watch needs Riverside\'s login (10 days). Greenway\'s address bounced.', 'c-warn'],
        ['Prices', 'Full start-up ' + money(full) + ' + VAT entered by Collins on Mon 2 Nov, for Rachel to approve. 2 discount requests.', 'c-info'],
        ['People', 'Olu on leave this week, Daniel covering. Sam Patel leaves Fri 6 Nov.', 'c-neutral'],
        ['Data', '1 rights request open (due Fri 27 Nov). 14 identity documents to delete on Mon 9 Nov, legal hold check clear.', 'c-neutral']
      ].map(([k, t, c]) => ({ k, t, cls: 'sb-chip ' + c })),
      areas: [
        ['Go-live readiness', 'Board 79', '12 of 16 setup checks done', 'list-checks', 'GoLive.dc.html'],
        ['Rules and promises', 'Board 80', 'Every rule once, where it is used', 'clock', 'Rules.dc.html'],
        ['Packages and journeys', 'Board 81', 'Packages, stages, gates, sessions', 'clipboard-list', 'Packages.dc.html'],
        ['Price book', 'Board 77', '1 price and 2 discounts waiting', 'file-check', 'PriceBook.dc.html'],
        ['Forms', 'Board 44', 'CQC form version 8 waiting', 'pencil-line', 'FormBuilder.dc.html'],
        ['Messages and automations', 'Board 82', 'Email 5.2 version 3 waiting. 46 automations on', 'inbox', 'Messages.dc.html'],
        ['People and access', 'Board 83', '10 people. 1 permission change waiting', 'users', 'PeopleAccess.dc.html'],
        ['Security', 'Board 84', '1 open incident, assessing', 'shield-alert', 'SecurityCentre.dc.html'],
        ['Data and privacy', 'Board 85', 'Retention version 2 waiting. 1 rights request', 'lock', 'DataPrivacy.dc.html'],
        ['System health', 'Board 86', '13 of 15 connections healthy', 'refresh-cw', 'Health.dc.html'],
        ['Money and exports', 'Board 87', 'Invoiced £9,600, collected £4,150, overdue £5,300 in 4 invoices', 'download', 'MoneyExports.dc.html'],
        ['View as', 'Board 88', 'See a client\'s Hub as they saw it, with a reason', 'eye', 'ViewAs.dc.html'],
        ['How it fits together', 'Board 89', 'From each setting to the screens that read it', 'git-compare', 'FitsTogether.dc.html']
      ].map(([name, num, note, icon, href]) => ({ name, num, note, icon, href }))
    };
  }
}'''
H['home'] = 4000
build_sa(OUT + '/SuperAdmin.dc.html', 'Super admin home', 'Super admin', H['home'], B_HOME, S_HOME, 'home', CSS)

# ====================================================================== 79. Go-live readiness
B_GL = '''      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 4px; flex: 1 1 560px; min-width: 0;">
          <span class="sb-muted">Super admin. Monday 2 November</span>
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Go-live readiness</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">The Hub went live on Thu 1 Oct 2026. This list stays as the health of the setup: anything still open shows here and on Home until it is done.</span>
        </div>
        <div style="display: flex; gap: 8px; align-items: center;"><span class="sb-muted">{{checkedNote}}</span><button class="sb-btn b-gh" onClick="{{recheck}}">Check again</button></div>
      </div>

      <div class="bz-cols">
        <section class="sb-card" style="flex: 1 1 360px; min-width: 0; padding: 18px 20px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="sc-h">
          <h2 id="sc-h" class="sb-h2">Setup score</h2>
          <div style="display: flex; align-items: baseline; gap: 10px;"><span class="sb-kv">{{scoreVal}}</span><span class="sb-sub">{{scoreSub}}</span></div>
          <div class="{{barCls}}" aria-hidden="true"><span class="{{barW}}"></span></div>
          <span class="sb-sub">{{scoreNote}}</span>
        </section>
        <section class="sb-card" style="flex: 2 1 620px; min-width: 0; padding: 18px 20px; display: flex; flex-direction: column; gap: 14px;" aria-labelledby="sm-h">
          <div style="display: flex; justify-content: space-between; gap: 10px; align-items: baseline; flex-wrap: wrap;"><h2 id="sm-h" class="sb-h2">Setup mode and dual control</h2><span class="sb-chip c-ok">Dual control on since Thu 1 Oct</span></div>
          <div class="bz-g3">
            <sc-for list="{{steps}}" as="p" hint-placeholder-count="3">
              <div class="bz-step"><span class="{{p.cls}}">{{p.n}}</span><span style="display: flex; flex-direction: column; gap: 2px; min-width: 0;"><span class="bz-b">{{p.t}}</span><span class="sb-muted">{{p.when}}</span><span class="sb-sub">{{p.x}}</span></span></div>
            </sc-for>
          </div>
        </section>
      </div>

      <div class="bz-cols">
        <section class="sb-card" style="flex: 3 1 640px; min-width: 0;" aria-labelledby="cl-h">
          <div class="sb-head"><h2 id="cl-h" class="sb-h2">Checklist by area</h2><span class="sb-sub">Open a line to see where it shows and what is left</span></div>
          <div style="padding: 0 20px 12px;">''' + tabs('fTabs', 'Filter the checklist') + '''</div>
          <sc-for list="{{groups}}" as="g" hint-placeholder-count="5">
            <div style="padding: 12px 20px 4px; border-top: 1px solid var(--cs-border-subtle);" class="bz-lbl">{{g.name}}</div>
            <sc-for list="{{g.items}}" as="i" hint-placeholder-count="3">
              <div style="border-top: 1px solid var(--cs-border-subtle);">
                <button class="{{i.rowCls}}" aria-expanded="{{i.exp}}" onClick="{{i.toggle}}">
                  <span class="{{i.dot}}" aria-hidden="true"></span>
                  <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b" style="font-size: 15px; line-height: 22px;">{{i.t}}</span><span class="sb-sub">{{i.x}}</span></span>
                  <span class="sb-muted" style="flex: 0 0 150px; text-align: right;">{{i.when}}</span>
                  <span class="{{i.chipCls}}" style="width: 120px; justify-content: center;">{{i.chip}}</span>
                </button>
                <sc-if value="{{i.isOpen}}" hint-placeholder-val="{{ false }}">
                  <div style="padding: 0 20px 16px 42px; display: flex; flex-direction: column; gap: 10px;">
                    <div class="bz-box"><span class="bz-lbl">Where it shows</span><sc-for list="{{i.where}}" as="w" hint-placeholder-count="2"><span>{{w}}</span></sc-for></div>
                    <sc-if value="{{i.isIco}}" hint-placeholder-val="{{ false }}">
                      <div class="bz-g2">
                        <div style="display: flex; flex-direction: column; gap: 6px;"><label class="bz-lbl" for="ico-n">ICO registration number</label><input id="ico-n" class="bz-in" value="{{icoVal}}" onChange="{{onIco}}" placeholder="For example ZA123456"></div>
                        <div style="display: flex; flex-direction: column; gap: 6px;"><label class="bz-lbl" for="ico-d">Renewal date</label><input id="ico-d" class="bz-in" value="{{icoDate}}" onChange="{{onIcoDate}}" placeholder="For example 30/09/2027"></div>
                      </div>
                      <sc-if value="{{icoErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err" role="alert">{{icoErrText}}</span></sc-if>
                      <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{saveIco}}">Save the number</button><span class="sb-muted">Shown on the client Security page and the privacy notice. A reminder goes to Collins, the data protection lead, 6 weeks before renewal.</span></div>
                    </sc-if>
                    <sc-if value="{{i.isTp}}" hint-placeholder-val="{{ false }}">
                      <label class="bz-lbl" for="tp-in">Trustpilot review link</label>
                      <input id="tp-in" class="bz-in" value="{{tpVal}}" onChange="{{onTp}}" placeholder="https://uk.trustpilot.com/evaluate/...">
                      <sc-if value="{{tpErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err" role="alert">Paste the review link from your Trustpilot business account. It contains trustpilot.com.</span></sc-if>
                      <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{saveTp}}">Add the link</button><span class="sb-muted">Every registered client is invited once, whatever their feedback, and chooses Google or Trustpilot.</span></div>
                    </sc-if>
                    <sc-if value="{{i.hasNote}}" hint-placeholder-val="{{ false }}"><div class="bz-ok"><span class="bz-b">{{i.note}}</span></div></sc-if>
                    <sc-if value="{{i.hasLink}}" hint-placeholder-val="{{ false }}"><a class="bz-a" href="{{i.href}}">{{i.linkText}}</a></sc-if>
                  </div>
                </sc-if>
              </div>
            </sc-for>
          </sc-for>
        </section>

        <div style="flex: 2 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="sa-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="sa-h" class="sb-h2">The two super admins</h2></div>
            <sc-for list="{{admins}}" as="a" hint-placeholder-count="2">
              <div style="display: flex; gap: 12px; align-items: flex-start; padding-top: 10px; border-top: 1px solid var(--cs-border-subtle);">
                <span class="bz-ico bz-b" aria-hidden="true">{{a.ini}}</span>
                <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{a.name}}</span><span class="sb-sub">{{a.role}}</span><span class="sb-muted">{{a.since}}</span></span>
                <span class="sb-chip c-ok">Two-step on</span>
              </div>
            </sc-for>
          </section>

          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="dc2-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="dc2-h" class="sb-h2">What needs the other super admin</h2></div>
            <ul class="bz-ul">
              <sc-for list="{{dual}}" as="d" hint-placeholder-count="9"><li style="font-size: 14px; line-height: 20px;">{{d}}</li></sc-for>
            </ul>
            <div class="bz-box"><span class="bz-lbl">Without a second approval</span><span>Routine deletions inside the approved schedule run on their own, with 7 days' notice. Anyone with permission can suggest a price; only a super admin enters it.</span></div>
            <span class="sb-muted">Break-glass in a real emergency: if no other super admin can be reached, the person may self-authorise with a written reason. Always {{bgHours}} hours, both super admins and the client told the same day, reviewed within 1 working day.</span>
          </section>

          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="sm2-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="sm2-h" class="sb-h2">How setup mode worked</h2></div>
            <span class="sb-sub">Before go-live there was only one super admin, so nothing could be approved by a second person. In setup mode the first super admin could set things up alone, and every change was still logged. Go-live needed two active, named super admins. From that moment dual control switched on, and it stays on.</span>
            <a class="bz-a" href="SuperAdmin.dc.html">Back to Home (board 24)</a>
          </section>
        </div>
      </div>
'''

S_GL = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { f: 'all', open: { ico: true }, ico: '', icoDate: '', icoErr: '', icoSaved: false, tp: '', tpErr: false, tpSaved: false, checked: false };
  }
  renderVals() {
    const s = this.state;
    ''' + JS_R + r'''
    const full = Number(R.get('price-full', 8500));
    const G = [
      ['People and control', [
        ['admins', 'Two named super admins', 'Collins and Rachel Turner, both active with two-step login.', 'done', 'Thu 1 Oct', ['People and access (board 83): super admin is a flag on a role', 'Every approval on Home, the Price book, Forms, Messages and Data and privacy'], 'PeopleAccess.dc.html', 'Open People and access (board 83)'],
        ['people', 'People and roles', '10 people with roles set, including finance and the data protection lead.', 'done', 'Wed 30 Sep', ['Every staff menu shows only what the role can use', 'Pickers such as "Proposed consultant" in Add a client (board 51)'], 'PeopleAccess.dc.html', 'Open People and access (board 83)']
      ]],
      ['Brand and sending', [
        ['brand', 'Branding', 'Logo, colours and the email footer.', 'done', 'Mon 21 Sep', ['Every client screen and email', 'Email signatures (Messages and automations, board 82)'], 'Messages.dc.html', 'Open Messages and automations (board 82)'],
        ['domain', 'Sending domain', 'hello@caresyncexperts.co.uk. Sending domain checks passed (SPF, DKIM and DMARC).', 'done', 'Tue 22 Sep', ['Every automated Hub email, including sign-in links', 'Personal messages go from each person\'s Google Workspace mailbox'], 'Health.dc.html', 'Open System health (board 86)'],
        ['tp', 'Review links', 'Google link added. Trustpilot link not yet added, so clients only see Google for now.', 'open', 'Since Thu 1 Oct', ['Registered, share your experience (board 20)', 'Email: You are registered (board 17)'], 'Rules.dc.html', 'Review platforms in Rules and promises (board 80)']
      ]],
      ['Legal and data', [
        ['legal', 'Legal wordings', 'Agreement, terms and privacy notice, version 1 of each, with dates.', 'done', 'Fri 25 Sep', ['Sign your pack (board 19): the agreement', 'First sign-in (board 53): the privacy notice'], 'DataPrivacy.dc.html', 'Open Data and privacy (board 85)'],
        ['ico', 'ICO registration number', 'Not entered. The client Security page hides "registered with the ICO" until it is.', 'open', 'Since Thu 1 Oct', ['How we keep your information safe (board 62)', 'The privacy notice'], 'DataPrivacy.dc.html', 'Open Data and privacy (board 85)'],
        ['ret', 'Retention schedule', 'Version 1 live. Version 2, proposed by Collins, waits for Rachel Turner on Home.', 'done', 'Thu 1 Oct', ['Your account (board 29): how long we keep things', 'Deletion runs (Data and privacy, board 85)'], 'DataPrivacy.dc.html', 'Open Data and privacy (board 85)']
      ]],
      ['What we sell', [
        ['packages', 'Packages', '7 packages: CQC domiciliary care, CQC supported living, Full start-up, CIW, RQIA, tender writing, and add-ons.', 'done', 'Fri 25 Sep', ['Add a client (board 51)', 'The client\'s journey (board 2) and Plan and costs (board 60)'], 'Packages.dc.html', 'Open Packages and journeys (board 81)'],
        ['prices', 'Prices', '6 prices still to set, including "Aftercare, 12 months" (add-on) and extra sessions. Nobody quotes a price that is not set.', 'open', 'Since Thu 1 Oct', ['Add a client (board 51) shows "Price to set" and blocks the quote', 'Plan and costs (board 60)'], 'PriceBook.dc.html', 'Open Price book (board 77)'],
        ['full', 'Full start-up price check', money(full) + ' + VAT entered by Collins on Mon 2 Nov. Rachel checks it against £8,000 and approves it (decision 1 on Home).', 'open', 'Since Mon 2 Nov', ['Add a client (board 51), Plan and costs (board 60), Stripe instalments'], 'SuperAdmin.dc.html', 'Open the decision on Home (board 24)'],
        ['forms', 'Forms', 'CQC (version 7), CIW, RQIA and tender forms live. CQC version 8 waits for approval.', 'done', 'Mon 28 Sep', ['Onboarding forms (boards 46, 47, 55, 56 and 38)', 'Form received checks (board 13)'], 'FormBuilder.dc.html', 'Open Forms (board 44)'],
        ['emails', 'Emails', 'The email library approved, each email with a version. 5.2 version 3 waits for approval.', 'done', 'Tue 29 Sep', ['Every email the Hub sends', 'Weekly update composer (board 9)'], 'Messages.dc.html', 'Open Messages and automations (board 82)']
      ]],
      ['Systems and clients', [
        ['integrations', 'Connections', 'All 15 set up. 2 need attention today: the CQC email watch for Riverside and a bounced address for Greenway.', 'warn', 'Tue 29 Sep', ['System health (board 86) shows each one and what depends on it'], 'Health.dc.html', 'Open System health (board 86)'],
        ['import', 'Clients already partway through', 'Imported at their current stage before go-live, for example Westbrook at stage 10 of 11.', 'done', 'Wed 30 Sep', ['Clients (board 68) and each client page (board 42)'], 'ClientsList.dc.html', 'Open Clients (board 68)'],
        ['test', 'A 3-client test', 'Three test clients went from welcome to submission in a test space, with test payments and signatures.', 'done', 'Tue 29 Sep', ['Run before go-live; run again after any big change'], '', '']
      ]]
    ];
    const isDone = id => (id === 'ico' && s.icoSaved) || (id === 'tp' && s.tpSaved);
    const items = G.map(([name, list]) => [name, list.map(([id, t, x, st, when, where, href, linkText]) => {
      const state = isDone(id) ? 'done' : st;
      const xx = id === 'ico' && s.icoSaved ? 'Saved: ' + s.ico.trim().toUpperCase() + (s.icoDate.trim() ? ', renews ' + s.icoDate.trim() : '') + '. The client Security page now shows it.' : (id === 'tp' && s.tpSaved ? 'Google and Trustpilot both added. Clients choose either.' : x);
      return { id, t, x: xx, state, when: isDone(id) ? 'Mon 2 Nov' : when, where, href, linkText };
    })]);
    const flat = [].concat(...items.map(g => g[1]));
    const total = flat.length; const done = flat.filter(i => i.state !== 'open').length; const open = total - done;
    const pct = Math.round(done / total * 100); const w = 'w' + Math.round(pct / 5) * 5;
    const F = { all: () => true, open: i => i.state === 'open' || isDone(i.id), done: i => i.state !== 'open' };
    const set = (k, id, v) => this.setState({ [k]: Object.assign({}, s[k], { [id]: v }) });
    const chipOf = { done: ['Done', 'c-ok', 'd-ok'], open: ['Still open', 'c-warn', 'd-warn'], warn: ['Done, 2 to watch', 'c-info', 'd-warn'] };
    const groups = items.map(([name, list]) => ({ name, items: list.filter(F[s.f]).map(i => {
      const isOpen = !!s.open[i.id];
      const note = i.id === 'ico' && s.icoSaved ? 'Saved by Collins, the data protection lead, just now. Rachel is told. Written to the audit log.' : (i.id === 'tp' && s.tpSaved ? 'Added by Collins just now. The next registered client can choose Trustpilot.' : '');
      return Object.assign({}, i, { isOpen, exp: isOpen ? 'true' : 'false', toggle: () => set('open', i.id, !isOpen),
        rowCls: 'bz-rowbtn' + (isOpen ? ' bz-sel' : ''), dot: 'bz-dot ' + chipOf[i.state][2], chip: chipOf[i.state][0], chipCls: 'sb-chip ' + chipOf[i.state][1],
        isIco: i.id === 'ico' && !s.icoSaved, isTp: i.id === 'tp' && !s.tpSaved, hasNote: !!note, note, hasLink: !!i.href });
    }) })).filter(g => g.items.length);
    return {
      theme: this.props.theme ?? 'light', nav: __NAV__, user: { name: 'Collins', initials: 'C' }, three: 7,
      bgHours: R.get('break-glass-hours', 4),
      checkedNote: s.checked ? 'Checked just now' : 'Checked today 06:00', recheck: () => this.setState({ checked: true }),
      scoreVal: done + ' of ' + total, scoreSub: pct + '% done', barCls: 'bar ' + (open ? 'amb' : 'ok'), barW: w,
      scoreNote: open ? open + (open === 1 ? ' thing is' : ' things are') + ' still open. None of them stops the Hub working, but each one is promised somewhere.' : 'Everything is done. New gaps appear here if a setting is removed.',
      steps: [
        ['1', 'Setup mode', 'Mon 14 Sep to Wed 30 Sep', 'Collins set things up alone. Every change was logged.', 'bz-stepn c-neutral'],
        ['2', 'Go-live', 'Thu 1 Oct 2026', 'Needed two active, named super admins with two-step login. The 3-client test had passed.', 'bz-stepn c-info'],
        ['3', 'Dual control', 'On since Thu 1 Oct', 'Sensitive changes need the other super admin. Nobody approves their own request.', 'bz-stepn c-ok']
      ].map(([n, t, when, x, cls]) => ({ n, t, when, x, cls })),
      fTabs: [['all', 'All ' + total], ['open', 'Still open ' + open], ['done', 'Done ' + done]].map(([k, label]) => ({ label, on: s.f === k, off: s.f !== k, pick: () => this.setState({ f: k }) })),
      groups,
      icoVal: s.ico, icoDate: s.icoDate, icoErr: !!s.icoErr, icoErrText: s.icoErr,
      onIco: e => this.setState({ ico: e.target.value, icoErr: '' }), onIcoDate: e => this.setState({ icoDate: e.target.value }),
      saveIco: () => { const v = s.ico.trim().toUpperCase(); if (!v) { this.setState({ icoErr: 'Enter the number from the ICO certificate.' }); return; } if (!/^Z[A-Z0-9]{7}$/.test(v)) { this.setState({ icoErr: 'ICO registration numbers start with Z and have 8 characters. Check the certificate.' }); return; } this.setState({ icoSaved: true, icoErr: '' }); },
      tpVal: s.tp, tpErr: s.tpErr, onTp: e => this.setState({ tp: e.target.value, tpErr: false }),
      saveTp: () => { if (!/trustpilot\.com/i.test(s.tp)) { this.setState({ tpErr: true }); return; } this.setState({ tpSaved: true }); },
      admins: [
        ['C', 'Collins', 'Director. Super admin 1 and data protection lead.', 'Super admin since setup began, Mon 14 Sep'],
        ['RT', 'Rachel Turner', 'Operations manager. Super admin 2.', 'Invited by Collins in setup mode on Mon 28 Sep. Active from Thu 1 Oct']
      ].map(([ini, name, role, since]) => ({ ini, name, role, since })),
      dual: ['Price changes and discounts', 'Permission changes and super admin invites', 'Form versions', 'Template and email versions with legal wording', 'Retention schedule changes', 'Early or unscheduled deletion', 'Break-glass, unless self-authorised in an emergency']
    };
  }
}'''
H['golive'] = 2400
build_sa(OUT + '/GoLive.dc.html', 'Go-live readiness', 'Go-live readiness', H['golive'], B_GL, S_GL, 'golive', CSS)

# ====================================================================== 86. System health
B_HE = '''      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 4px; flex: 1 1 560px; min-width: 0;">
          <span class="sb-muted">Super admin. Monday 2 November, 09:20</span>
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">System health</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">{{headline}}</span>
        </div>
      </div>

      <div class="bz-g5">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="5">
          <div class="sb-card sb-kpi"><span class="sb-muted">{{k.k}}</span><span class="sb-kv">{{k.v}}</span><span class="{{k.cls}}" style="align-self: flex-start;">{{k.note}}</span></div>
        </sc-for>
      </div>

      <section aria-labelledby="na-h" style="display: flex; flex-direction: column; gap: 12px;">
        <h2 id="na-h" class="sb-h2">{{attnTitle}}</h2>
        <div class="bz-g2" style="gap: 18px; align-items: start;">
          <div class="{{rvCls}}" style="gap: 8px;">
            <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">CQC email watch: Riverside Homecare Ltd</span><span class="{{rvChipCls}}">{{rvChip}}</span></div>
            <span class="sb-sub">Submitted to CQC on Fri 23 Oct. The CQC email login is not in the vault: 10 days without a watch, red after {{gapDays}} days. A CQC letter to Mark Evans could be missed. On My day and the manager dashboard since day {{gapDays}}. Olu is the case owner; Daniel is covering.</span>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-sec" onClick="{{rvAsk}}">Ask Mark to connect his email</button><a class="sb-btn b-gh bz-link" href="PortalWatch.dc.html">Open the watch (board 22)</a></div>
            <sc-if value="{{rvAsked}}" hint-placeholder-val="{{ false }}"><span class="sb-sub">Sent just now: Mark gets the "Your business email" link (board 27) by email, and Daniel has a task to call him today. Until it is connected, Mark can forward any CQC email to his Hub.</span></sc-if>
          </div>
          <div class="{{gwCls}}" style="gap: 8px;">
            <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">Email delivery: weekly update to Greenway Support</span><span class="{{gwChipCls}}">{{gwChip}}</span></div>
            <span class="sb-sub">The Friday 30 Oct update bounced at 17:02: the mailbox does not exist. It is waiting in Olu's outbox. Olu is on leave, so Daniel is covering and has been told.</span>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-sec" aria-expanded="{{fixExp}}" onClick="{{toggleFix}}">Fix email address</button><button class="sb-btn b-gh" aria-expanded="{{logExp}}" onClick="{{toggleLog}}">See run log</button><button class="sb-btn b-gh" onClick="{{retry}}">{{retryLabel}}</button></div>
            <sc-if value="{{retryErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err" role="alert">{{retryErrText}}</span></sc-if>
            <sc-if value="{{showFix}}" hint-placeholder-val="{{ false }}">
              <label class="bz-lbl" for="fx-in2">Tunde Bello's email address</label>
              <input id="fx-in2" class="bz-in" value="{{fixVal}}" onChange="{{onFix}}">
              <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{saveFix}}">Save</button><span class="sb-muted" style="flex: 1 1 200px;">{{fixNote}}</span></div>
            </sc-if>
            <sc-if value="{{showLog}}" hint-placeholder-val="{{ false }}">
              <div style="display: flex; flex-direction: column; gap: 4px; padding-top: 6px; border-top: 1px solid var(--cs-border-default);">
                <sc-for list="{{runLog}}" as="l" hint-placeholder-count="5"><span style="font-size: 13px; line-height: 18px;"><span class="bz-b">{{l.t}}</span> {{l.x}}</span></sc-for>
              </div>
            </sc-if>
          </div>
        </div>
      </section>

      <section class="sb-card" aria-labelledby="cn-h">
        <div class="sb-head"><h2 id="cn-h" class="sb-h2">Connections: {{okCount}} of 15 healthy</h2><span class="sb-sub">Open a connection to see what depends on it and what happens if it fails</span></div>
        <div style="padding: 0 20px 12px;">''' + tabs('cTabs', 'Filter connections') + '''</div>
        <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 0 0 8px;"></span><span class="sb-th" style="flex: 1;">Connection</span><span class="sb-th" style="flex: 0 0 210px;">Last success</span><span class="sb-th" style="flex: 0 0 150px;">Checked</span><span class="sb-th" style="flex: 0 0 132px; text-align: center;">Status</span></div>
        <sc-for list="{{conns}}" as="c" hint-placeholder-count="15">
          <div style="border-top: 1px solid var(--cs-border-subtle);">
            <button class="{{c.rowCls}}" aria-expanded="{{c.exp}}" onClick="{{c.toggle}}">
              <span class="{{c.dot}}" aria-hidden="true"></span>
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b" style="font-size: 15px; line-height: 22px;">{{c.name}}</span><span class="sb-sub">{{c.purpose}}</span></span>
              <span class="sb-sub" style="flex: 0 0 210px;">{{c.last}}</span>
              <span class="sb-muted" style="flex: 0 0 150px;">{{c.every}}</span>
              <span class="{{c.chipCls}}" style="width: 132px; justify-content: center;">{{c.chip}}</span>
            </button>
            <sc-if value="{{c.isOpen}}" hint-placeholder-val="{{ false }}">
              <div style="padding: 0 20px 18px 42px; display: flex; flex-direction: column; gap: 10px;">
                <div class="bz-g3">
                  <div class="bz-box"><span class="bz-lbl">Screens that depend on it</span><sc-for list="{{c.depends}}" as="x" hint-placeholder-count="3"><span>{{x}}</span></sc-for></div>
                  <div class="bz-box"><span class="bz-lbl">Automations that use it</span><sc-for list="{{c.autos}}" as="x" hint-placeholder-count="2"><span>{{x}}</span></sc-for></div>
                  <div class="bz-amb"><span class="bz-lbl">If it fails</span><span>{{c.fails}}</span><span class="sb-sub">Who is told: {{c.told}}</span></div>
                </div>
                <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
                  <span class="sb-sub" style="flex: 1 1 380px;"><span class="bz-lbl">Key or access: </span><span>{{c.key}}</span></span>
                  <span class="sb-muted">Owner: {{c.owner}}</span>
                  <button class="sb-btn b-gh" onClick="{{c.test}}">Test now</button>
                  <button class="sb-btn b-gh" onClick="{{c.reconnect}}">Reconnect</button>
                </div>
                <sc-if value="{{c.hasMsg}}" hint-placeholder-val="{{ false }}"><div class="{{c.msgCls}}"><span class="bz-b">{{c.msg}}</span></div></sc-if>
              </div>
            </sc-if>
          </div>
        </sc-for>
        <div class="sb-row" style="align-items: flex-start;">
          <span class="bz-dot d-off" style="margin-top: 7px;" aria-hidden="true"></span>
          <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">WhatsApp</span><span class="sb-sub">A later phase. Not connected and not offered to clients. Not counted in the 15.</span></span>
          <span class="sb-chip c-neutral" style="width: 132px; justify-content: center;">Later, off</span>
        </div>
        <div class="sb-row"><span class="sb-muted">Keys are never shown in full. Changing a key is written to the audit log and both super admins are told.</span></div>
        <div class="sb-row" style="align-items: flex-start; background: var(--cs-surface-subtle);">
          <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span class="bz-b">Connections and suppliers are two different lists</span>
          <span class="sb-sub">The 15 connections here are the systems the Hub talks to. Data and privacy (board 85) lists 16 suppliers that process our data. 7 of those suppliers are connections here: Google Workspace, Stripe, Xero, DocuSeal, GoHighLevel, email sending and texts. The other 9 have no connection on this page: the hosting provider runs the Hub itself, so its health is the uptime and backups below; 5 are services the Hub uses inside its own work (the AI provider, the prompt log, speech to text, virus scanning and the automations tool), and their failures show under Failed items; 1Password is interim and ends by Fri 13 Nov; WhatsApp and AssuredBid are not live. The 4 look-ups, 3 regulator watches and the Interview Preparation Hub here are not suppliers that process our data.</span></span>
          <a class="sb-btn b-gh bz-link" href="DataPrivacy.dc.html">Open suppliers (board 85)</a>
        </div>
      </section>

      <div class="bz-cols">
        <div style="flex: 3 1 600px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
          <section class="sb-card" aria-labelledby="fq-h">
            <div class="sb-head"><h2 id="fq-h" class="sb-h2">Failed items</h2><span class="sb-sub">{{failSub}}</span></div>
            <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 0 0 112px;">When</span><span class="sb-th" style="flex: 1;">What</span><span class="sb-th" style="flex: 0 0 118px;">Owner</span><span class="sb-th" style="flex: 0 0 130px; text-align: center;">State</span></div>
            <sc-for list="{{fails}}" as="f" hint-placeholder-count="3">
              <div class="sb-row" style="align-items: flex-start;"><span class="sb-sub" style="flex: 0 0 112px;">{{f.at}}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{f.t}}</span><span class="sb-sub">{{f.x}}</span></span><span class="sb-sub" style="flex: 0 0 118px;">{{f.owner}}</span><span style="flex: 0 0 130px; display: flex; justify-content: center;"><span class="{{f.cls}}">{{f.state}}</span></span></div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">Automations: 46 on. The full list, with on and off and "what depends on this", is in Messages and automations (board 82). Every failure shows here and to its owner. Nothing fails silently.</span></div>
          </section>

          <section class="sb-card" aria-labelledby="mw-h">
            <div class="sb-head"><h2 id="mw-h" class="sb-h2">Regulator watch by client</h2><span class="sb-sub">Clients waiting on CQC, CIW or RQIA</span></div>
            <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 1;">Client</span><span class="sb-th" style="flex: 0 0 190px;">How we watch</span><span class="sb-th" style="flex: 0 0 100px;">Last checked</span><span class="sb-th" style="flex: 0 0 120px; text-align: center;">State</span></div>
            <sc-for list="{{watch}}" as="w" hint-placeholder-count="6">
              <div class="sb-row"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column;"><span class="bz-b">{{w.c}}</span><span class="sb-muted">{{w.r}}</span></span><span class="sb-sub" style="flex: 0 0 190px;">{{w.how}}</span><span class="sb-sub" style="flex: 0 0 100px;">{{w.last}}</span><span style="flex: 0 0 120px; display: flex; justify-content: center;"><span class="{{w.cls}}">{{w.state}}</span></span></div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">CQC email every few minutes. CIW Online and the RQIA Web Portal every working day. The watch never files Hub sign-in or e-signature emails.</span></div>
          </section>
        </div>

        <div style="flex: 2 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="ed-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="ed-h" class="sb-h2">Email delivery</h2><span class="sb-chip c-ok">Domain checks passed</span></div>
            <span class="sb-sub">Automated Hub emails go from hello@caresyncexperts.co.uk. Personal messages go from each person's Google Workspace mailbox.</span>
            <sc-for list="{{domain}}" as="d" hint-placeholder-count="3">
              <div style="display: flex; justify-content: space-between; gap: 10px; align-items: center; padding-top: 8px; border-top: 1px solid var(--cs-border-subtle);"><span style="display: flex; flex-direction: column;"><span class="bz-b">{{d.k}}</span><span class="sb-muted">{{d.x}}</span></span><span class="sb-chip c-ok">Pass</span></div>
            </sc-for>
            <div style="display: flex; justify-content: space-between; gap: 10px; padding-top: 8px; border-top: 1px solid var(--cs-border-subtle); font-size: 14px; line-height: 20px;"><span class="sb-sub">Weekly updates, Fri 30 Oct</span><span class="bz-b">{{weeklyDelivered}}</span></div>
            <div style="display: flex; justify-content: space-between; gap: 10px; font-size: 14px; line-height: 20px;"><span class="sb-sub">Bounces this week</span><span class="bz-b">{{bounces}}</span></div>
            <div style="display: flex; justify-content: space-between; gap: 10px; font-size: 14px; line-height: 20px;"><span class="sb-sub">Quiet hours</span><span class="bz-b" style="text-align: right;">{{quiet}}</span></div>
            <span class="sb-muted">Legal deadline alerts and tender deadlines within 24 hours still go in quiet hours.</span>
          </section>

          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="tx-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="tx-h" class="sb-h2">Texts and WhatsApp</h2></div>
            <div style="display: flex; justify-content: space-between; gap: 10px; align-items: flex-start;"><span style="display: flex; flex-direction: column;"><span class="bz-b">Texts: urgent only</span><span class="sb-sub">The introduction call, urgent legal deadlines, and the sign-in code to a client's mobile when Care Sync holds their sign-in mailbox.</span></span><span class="sb-chip c-ok">On</span></div>
            <div style="display: flex; justify-content: space-between; gap: 10px; align-items: flex-start; padding-top: 8px; border-top: 1px solid var(--cs-border-subtle);"><span style="display: flex; flex-direction: column;"><span class="bz-b">WhatsApp</span><span class="sb-sub">A later phase. Clients are not offered it yet.</span></span><span class="sb-chip c-neutral">Later, off</span></div>
          </section>

          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="bk-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="bk-h" class="sb-h2">Backups and restore tests</h2><span class="sb-chip c-ok">On time</span></div>
            <sc-for list="{{backups}}" as="b" hint-placeholder-count="4">
              <div style="display: flex; justify-content: space-between; gap: 10px; font-size: 14px; line-height: 20px; padding-top: 8px; border-top: 1px solid var(--cs-border-subtle);"><span class="sb-sub" style="flex: 0 0 130px;">{{b.k}}</span><span style="flex: 1; min-width: 0; text-align: right;">{{b.v}}</span></div>
            </sc-for>
            <a class="bz-a" href="SecurityCentre.dc.html">Resilience and keys (Security, board 84)</a>
          </section>

          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="up-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="up-h" class="sb-h2">Uptime</h2><span class="sb-sub">Last 30 days</span></div>
            <div style="display: flex; align-items: baseline; gap: 10px;"><span class="sb-kv">99.98%</span><span class="sb-sub">The Hub, for clients and staff</span></div>
            <span class="sb-sub">One planned update, Sun 25 Oct 06:00 to 06:09, announced on the Friday. No unplanned outages.</span>
          </section>
        </div>
      </div>
'''

S_HE = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { f: 'all', open: { cqcmail: true }, msgs: {}, rvAsked: false, showFix: false, showLog: false, fix: 'tunde@greenwaysupport.example', fixSaved: false, confirmed: false, resent: false, retryErr: '' };
  }
  renderVals() {
    const s = this.state;
    ''' + JS_R + r'''
    const day = R.get('weekly-update-day', 'Friday');
    const gapDays = R.get('watch-gap-red-days', 7);
    const sig = R.get('signature-reminders', 'after 2 days, then the consultant calls');
    const C = [
      ['google', 'Google Workspace', 'biz', 'Staff sign-in with two-step login, staff mailboxes, calendars and Drive.', 'ok', 'Today 09:19', 'Every 5 minutes',
        ['Staff sign-in, for every staff screen', 'Personal emails from staff mailboxes', 'Session invites: Sessions (board 28) and Coach sessions (board 69)', 'People and access (board 83): joiners and leavers'],
        ['Session booked: add it to both calendars', 'Leaver: suspend the Google account on the last day'],
        'Staff cannot sign in. Anyone already signed in keeps working until their session ends. Session invites wait, and the coach gets a task instead.', 'Both super admins', 'Service account key ••••••••7Q2c, added Thu 1 Oct', 'Collins'],
      ['stripe', 'Stripe', 'biz', 'Every instalment, by card or another method Stripe supports.', 'ok', 'Today 09:02', 'Live, with each payment',
        ['Sign your pack (board 19): accept, sign and pay', 'Plan and costs (board 60) and Your account (board 29)', 'Add a client (board 51)', 'Manager dashboard money (board 43) and Money and exports (board 87)'],
        ['Payment received: introduction call for Divine', 'Payment received: start the stage that waits for it', 'Instalment due: remind the client'],
        'Clients see "Payment could not start; we have been told", and nobody is charged twice. Stages that wait for a payment stay where they are. Finance can mark a bank transfer paid where one was agreed.', 'Femi Ade (finance) and both super admins', 'Secret key sk_live_••••••••4f2a', 'Femi Ade'],
      ['xero', 'Xero', 'biz', 'Invoices and payments, synced every hour.', 'ok', 'Today 09:00', 'Every hour',
        ['Manager dashboard money (board 43)', 'Money and exports (board 87): month close and the accountant export', 'Reports (board 72)'],
        ['Payment received: mark the invoice paid', 'Discount approved: add the discount line to the invoice'],
        'Payments are still taken in Stripe. Invoices wait in a queue and sync when Xero is back; nothing is lost.', 'Femi Ade (finance)', 'Connected account, renewed Mon 26 Oct', 'Femi Ade'],
      ['docuseal', 'DocuSeal', 'biz', 'E-signatures: agreements, pack sign-off and signing together.', 'ok', 'Today 08:45', 'Every 15 minutes',
        ['Sign your pack (board 19)', 'Signing together (board 64)', 'Add a client (board 51): the agreement', 'Stage 6 of 11: final pack sign-off'],
        ['Signed: move to the next stage', 'Signature reminders: ' + sig],
        'Clients cannot sign. The Sign page says signing is paused for a moment and that we will tell them when it is back. No stage moves without a signature.', 'The case owner and both super admins', 'API key ••••••••k9Lw', 'Collins'],
      ['ghl', 'GoHighLevel', 'biz', 'Sales CRM: calls, enquiries and won deals.', 'ok', 'Today 09:10', 'Every 5 minutes',
        ['Add a client (board 51): won deals arrive here', 'Introduction call (board 33): calls through GoHighLevel', 'Tender Radar (board 10): outreach'],
        ['Won deal: prepare Add a client for the salesperson', 'Call ended: log it on the client page'],
        'Won deals do not arrive in Add a client, so Jo adds the client by hand. Calls are logged when it is back.', 'Jo Martin and Collins', 'API key ••••••••Hc31', 'Jo Martin'],
      ['ch', 'Companies House', 'look', 'Company and officer checks.', 'ok', 'Today 08:55', 'On each look-up',
        ['Find your company (board 23) and Directors and owners (board 36)', 'Onboarding gates (board 8): Company and directors', 'Form received checks (board 13)', 'Address and identity check (board 14)'],
        ['Form arrived: check the directors against Companies House'],
        'Gate 1 shows "Waiting for Companies House". Grace can check the Companies House website and record it; the check runs again when it is back.', 'Grace', 'API key ••••••••2bE8', 'Grace'],
      ['os', 'Ordnance Survey', 'look', 'Postcode and address look-up.', 'ok', 'Today 08:31', 'On each look-up',
        ['Address history cards (board 61)', 'The "Your office" step of the onboarding form (board 46)', 'Address and identity check (board 14)'],
        ['Address entered: match it to an official address'],
        'Clients type the address by hand. Grace sees "not matched" on the check and confirms it.', 'Grace', 'API key ••••••••Vx70', 'Grace'],
      ['lr', 'HM Land Registry', 'look', 'Who owns an office address, for the office address evidence.', 'ok', 'Fri 30 Oct 11:20', 'On each look-up',
        ['Onboarding gates (board 8): Office address evidence', 'Address and identity check (board 14)', 'One-task link for the landlord (board 37)'],
        ['Office address entered: look up the registered owner'],
        'The office address gate waits. Grace can order the title by hand and upload it.', 'Grace', 'Business account ••••••••0193', 'Grace'],
      ['cqcdata', 'CQC data', 'look', 'Public CQC register: providers, locations and ratings.', 'ok', 'Today 06:00', 'Every night',
        ['Tender Radar (board 10): who already provides care', 'Tender profile (board 48) and Confirm what we hold (board 58)', 'Aftercare (board 71): the register entry after registration'],
        ['New registration: copy the register entry to the client page'],
        'Screens show the last copy with its date. Nothing is sent to clients from it.', 'Jo Martin', 'Subscription key ••••••••d4Ra', 'Jo Martin'],
      ['cqcmail', 'CQC email watch', 'watch', 'Reads CQC emails in each CQC client\'s business mailbox. Never Hub sign-in or e-signature emails.', 'bad', 'Today 09:18, except Riverside', 'Every few minutes',
        ['Regulator and tender watch (board 22)', 'The client\'s CQC centre (board 5)', 'My day (board 7) and Deadlines (board 75)', 'Notice of Proposal and interview alerts'],
        ['CQC email received: tell the case owner and the client', 'Legal deadline found: add it to Deadlines'],
        'A CQC letter could be missed, including one with a legal deadline. A gap turns red after ' + gapDays + ' days and shows on My day and the manager dashboard.', 'The case owner, the manager and both super admins', 'One connection per client mailbox. No shared key.', 'Each case owner'],
      ['ciw', 'CIW Online watch', 'watch', 'Checks CIW Online for Afon Care Ltd.', 'ok', 'Today 07:30', 'Every working day',
        ['Your regulator (board 63)', 'Regulator and tender watch (board 22)', 'My day (board 7)'],
        ['New CIW message: alert the consultant the same hour'],
        'Daniel checks CIW Online by hand each working day until it is back.', 'Daniel Mensah', 'Daniel is a user on the client\'s account. No password held.', 'Daniel Mensah'],
      ['rqia', 'RQIA Web Portal watch', 'watch', 'Checks the RQIA Web Portal for Lagan View Care Ltd.', 'ok', 'Today 08:05', 'Every working day',
        ['Your regulator (board 63)', 'Regulator and tender watch (board 22)', 'My day (board 7)'],
        ['New RQIA message: alert the consultant the same hour'],
        'The consultant checks the Web Portal by hand each working day until it is back.', 'Daniel Mensah (covering for Olu)', 'Portal access for the case owner. No password held.', 'Olu (Daniel covering)'],
      ['iph', 'Interview Preparation Hub API', 'biz', 'Creates the client\'s account when the interview stage starts, with regulator, service type and role.', 'ok', 'Today 09:00', 'Every 15 minutes',
        ['The interview portal link on the CQC centre (board 5) and Your regulator (board 63)', 'Coach sessions (board 69)', 'People and access (board 83): staff accounts'],
        ['Interview stage starts: create the client\'s account'],
        'A staff task appears with the details to copy into the Interview Preparation Hub by hand.', 'Millicent and the case owner', 'API key ••••••••Pq5m', 'Collins'],
      ['email', 'Email sending', 'msg', 'Automated Hub emails from hello@caresyncexperts.co.uk: sign-in links, weekly updates and every email in the library.', 'bad', 'Today 09:17', 'Live, with each email',
        ['Sign in, no password (board 40): the sign-in link', 'Weekly update composer (board 9)', 'Messages and automations (board 82): every email', 'Notifications (board 41)'],
        ['Weekly updates every ' + day, 'Every reminder and nudge'],
        'Clients cannot get a sign-in link and emails queue until it is back. A bounce goes to the sender\'s outbox and is never sent again to the same address.', 'The sender and both super admins', 'Sending key ••••••••mT8e. Domain checks: SPF, DKIM, DMARC', 'Collins'],
      ['sms', 'Texts (urgent only)', 'msg', 'Texts for the introduction call, urgent legal deadlines and sign-in codes.', 'ok', 'Today 08:00', 'Every hour',
        ['Introduction call (board 33): the text before the call', 'Deadlines (board 75): urgent legal deadline alerts', 'Sign in (board 40): the code to the client\'s mobile when Care Sync holds their sign-in mailbox'],
        ['Payment received: text before the introduction call', 'Legal deadline within 24 hours: text the client'],
        'Texts and codes cannot be sent. The message goes by email instead, and the consultant phones about urgent legal deadlines.', 'Both super admins', 'API key ••••••••Za62', 'Collins']
    ];
    const greenwayOk = s.resent;
    const set = (k, id, v) => this.setState({ [k]: Object.assign({}, s[k], { [id]: v }) });
    const statusOf = id => { if (id === 'email' && greenwayOk) return 'ok'; return null; };
    const all = C.map(([id, name, grp, purpose, st, last, every, depends, autos, fails, told, key, owner]) => {
      const state = statusOf(id) || st;
      const isOpen = !!s.open[id];
      const m = s.msgs[id] || '';
      const msgText = m === 'test' ? (state === 'ok' ? 'Tested just now: working.' : (id === 'cqcmail' ? 'Tested just now: 4 mailboxes working. Riverside Homecare is still not connected.' : 'Tested just now: sending works. The Greenway bounce still needs a new address.')) : (m === 're' ? (id === 'cqcmail' ? 'Reconnect needs the client: ask Mark to connect his email (above).' : 'Reconnected just now. Written to the audit log, and both super admins are told.') : '');
      return { id, name, grp, purpose, state, last: (id === 'email' && greenwayOk) ? 'Today 09:20' : last, every, depends, autos, fails, told, key, owner, isOpen,
        exp: isOpen ? 'true' : 'false', toggle: () => set('open', id, !isOpen), rowCls: 'bz-rowbtn' + (isOpen ? ' bz-sel' : ''),
        dot: 'bz-dot ' + (state === 'ok' ? 'd-ok' : 'd-bad'), chip: state === 'ok' ? 'Healthy' : 'Needs attention', chipCls: 'sb-chip ' + (state === 'ok' ? 'c-ok' : 'c-bad'),
        test: () => set('msgs', id, 'test'), reconnect: () => set('msgs', id, 're'), hasMsg: !!msgText, msg: msgText,
        msgCls: (state === 'ok' || m === 're') && id !== 'cqcmail' ? 'bz-ok' : 'bz-amb' };
    });
    const okCount = all.filter(c => c.state === 'ok').length;
    const bad = 15 - okCount;
    const G = { all: () => true, attn: c => c.state !== 'ok', biz: c => c.grp === 'biz', look: c => c.grp === 'look', watch: c => c.grp === 'watch', msg: c => c.grp === 'msg' };
    const cnt = k => all.filter(G[k]).length;
    const conns = all.filter(G[s.f]);
    const retry = () => {
      if (s.resent) return;
      if (!s.fixSaved) { this.setState({ retryErr: 'Retrying now would bounce again. Fix the address first.' }); return; }
      if (!s.confirmed) { this.setState({ confirmed: true, retryErr: '' }); return; }
      this.setState({ resent: true, retryErr: '' });
    };
    const gwState = s.resent ? 'Delivered' : (s.fixSaved ? (s.confirmed ? 'Ready to resend' : 'Waiting for Daniel') : 'Failed');
    return {
      theme: this.props.theme ?? 'light', nav: __NAV__, user: { name: 'Collins', initials: 'C' }, three: 7,
      headline: okCount + ' of 15 connections healthy' + (bad ? ', ' + bad + (bad === 1 ? ' needs' : ' need') + ' attention' : '') + '. Every connection shows what depends on it, what happens when it fails, and who is told.',
      gapDays,
      kpis: [
        ['Connections', okCount + ' of 15', bad ? bad + (bad === 1 ? ' needs' : ' need') + ' attention' : 'All healthy', bad ? 'warn' : 'ok'],
        ['Automations', '46 on', '1 failed this week', 'bad'],
        ['Waiting to retry', '0', s.resent ? 'Greenway resent' : '1 needs a person first', s.resent ? 'ok' : 'warn'],
        ['Last backup', '02:00', 'Nightly, done today', 'ok'],
        ['Restore test', 'Tue 13 Oct', 'Passed. Next by Mon 11 Jan', 'ok']
      ].map(([k, v, note, c]) => ({ k, v, note, cls: 'sb-chip c-' + c })),
      attnTitle: 'Needs attention now: ' + bad,
      rvCls: s.rvAsked ? 'bz-amb' : 'bz-red', rvChip: s.rvAsked ? 'Client asked' : 'Red, 10 days', rvChipCls: 'sb-chip ' + (s.rvAsked ? 'c-warn' : 'c-bad'),
      rvAsked: s.rvAsked, rvAsk: () => this.setState({ rvAsked: true }),
      gwCls: s.resent ? 'bz-ok' : 'bz-red', gwChip: gwState, gwChipCls: 'sb-chip ' + (s.resent ? 'c-ok' : (s.fixSaved ? 'c-warn' : 'c-bad')),
      showFix: s.showFix, showLog: s.showLog, fixExp: s.showFix ? 'true' : 'false', logExp: s.showLog ? 'true' : 'false',
      toggleFix: () => this.setState({ showFix: !s.showFix }), toggleLog: () => this.setState({ showLog: !s.showLog }),
      fixVal: s.fix, onFix: e => this.setState({ fix: e.target.value, fixSaved: false, confirmed: false }), saveFix: () => this.setState({ fixSaved: true, retryErr: '' }),
      fixNote: s.fixSaved ? 'Saved. The resend waits until Daniel confirms the address with Tunde by phone.' : 'The current address bounced. Check it with the client first.',
      retry, retryLabel: s.resent ? 'Resent' : (s.fixSaved && s.confirmed ? 'Resend now' : (s.fixSaved ? 'Daniel confirmed it' : 'Retry')),
      retryErr: !!s.retryErr, retryErrText: s.retryErr,
      runLog: [['Fri 30 Oct 17:00', 'weekly update built from the week\'s progress'], ['17:01', 'sent to tunde@greenwaysupport.example'], ['17:02', 'bounced: the mailbox does not exist'], ['17:02', 'moved to Olu\'s outbox; Olu and Daniel told'], ['Mon 2 Nov 07:00', 'still waiting; Daniel covering this week']].concat(s.fixSaved ? [['09:20', 'address changed to ' + s.fix + ' by Collins']] : [], s.confirmed ? [['09:20', 'Daniel confirmed the address with Tunde by phone']] : [], s.resent ? [['09:20', 'resent and delivered']] : []).map(([t, x]) => ({ t, x })),
      okCount,
      cTabs: [['all', 'All'], ['attn', 'Needs attention'], ['biz', 'Business systems'], ['look', 'Look-ups'], ['watch', 'Regulator watches'], ['msg', 'Emails and texts']].map(([k, label]) => ({ label: label + ' ' + cnt(k), on: s.f === k, off: s.f !== k, pick: () => this.setState({ f: k }) })),
      conns,
      failSub: s.resent ? 'Nothing waiting. 3 fixed this week' : '1 waiting for a person. 2 fixed automatically this week',
      fails: [
        ['Fri 30 Oct 17:02', 'Weekly update to Greenway Support', 'Bounced: the mailbox does not exist. Not retried automatically, because it would bounce again.', 'Olu (Daniel covering)', s.resent ? 'Resent 09:20' : 'Waiting for a fix', s.resent ? 'c-ok' : 'c-bad'],
        ['Wed 28 Oct 10:12', 'Companies House look-up for a new form', 'Slow reply. Retried automatically at 10:13 and worked.', 'Grace', 'Fixed', 'c-ok'],
        ['Tue 27 Oct 14:00', 'Xero sync', 'Timed out. Retried automatically at 14:05; every invoice synced.', 'Femi Ade', 'Fixed', 'c-ok']
      ].map(([at, t, x, owner, state, c]) => ({ at, t, x, owner, state, cls: 'sb-chip ' + c })),
      watch: [
        ['Sunrise Homecare Ltd', 'CQC: Notice of Proposal', 'Client email connected', '09:18', 'Watched', 'c-ok'],
        ['Elm Tree Care Ltd', 'CQC: interview Tue 24 Nov', 'Client email connected', '09:12', 'Watched', 'c-ok'],
        ['Westbrook Care Ltd', 'CQC: refused, we resubmit', 'Client email connected', '09:12', 'Watched', 'c-ok'],
        ['Afon Care Ltd', 'CIW: with CIW since Wed 14 Oct', 'CIW Online, every working day', '07:30', 'Watched', 'c-ok'],
        ['Lagan View Care Ltd', 'RQIA: submitted Wed 30 Sep', 'Web Portal and client email', '08:05', 'Watched', 'c-ok'],
        ['Riverside Homecare Ltd', 'CQC: submitted Fri 23 Oct', 'Login not in the vault', '10 days ago', s.rvAsked ? 'Client asked' : 'Not watched', s.rvAsked ? 'c-warn' : 'c-bad']
      ].map(([c, r, how, last, state, k]) => ({ c, r, how, last, state, cls: 'sb-chip ' + k })),
      domain: [['SPF', 'Who may send for caresyncexperts.co.uk'], ['DKIM', 'Each email is signed'], ['DMARC', 'Receivers know what to do with fakes']].map(([k, x]) => ({ k, x })),
      weeklyDelivered: s.resent ? '42 of 42 delivered' : '41 of 42 delivered',
      bounces: s.resent ? '1, now fixed' : '1 (Greenway Support)',
      quiet: R.get('quiet-hours', '8pm to 8am') + ', automated emails and texts',
      backups: [['Nightly backup', 'Today 02:00, done'], ['Kept', 'Encrypted, apart from the live Hub'], ['Last restore test', 'Tue 13 Oct, passed'], ['Next restore test', 'Due by Mon 11 Jan']].map(([k, v]) => ({ k, v }))
    };
  }
}'''
H['health'] = 3400
build_sa(OUT + '/Health.dc.html', 'System health', 'System health', H['health'], B_HE, S_HE, 'health', CSS)
