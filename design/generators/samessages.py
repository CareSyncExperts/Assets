# Super admin boards by agent C: Messages and automations (82) and View as and history (88).
# Run from SP/gen:  python3 samessages.py [H82] [H88]
import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from staffboard import build_sa
from sa_common import BOARDS
import samsg_data as D
import saviewas
OUT = '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/hub-canvas/project'
H82 = int(sys.argv[1]) if len(sys.argv) > 1 else 2400
H88 = int(sys.argv[2]) if len(sys.argv) > 2 else 2000

def js(x):
    return json.dumps(x, ensure_ascii=False).replace('</', '<\\/')

CSS = '''
.ml-sec{width:100%;display:flex;align-items:center;gap:12px;padding:10px 20px;border:0;border-top:1px solid var(--cs-border-subtle);background:var(--cs-surface-subtle);color:var(--cs-text-primary);font:inherit;font-size:14px;line-height:20px;text-align:left;cursor:pointer;min-height:44px}
.ml-grid{display:grid;grid-template-columns:52px minmax(0,2.3fr) minmax(0,1.5fr) 40px minmax(0,1fr) minmax(0,170px);gap:12px;align-items:start}
.ml-row{width:100%;padding:10px 20px;border:0;border-top:1px solid var(--cs-border-subtle);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:13px;line-height:18px;text-align:left;cursor:pointer}
.ml-on{box-shadow:inset 4px 0 0 var(--cs-action-primary);background:var(--cs-surface-brand)}
.ml-row:focus-visible,.ml-sec:focus-visible,.au-main:focus-visible,.sw:focus-visible,.pick:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:-2px}
.num{font-weight:600;font-variant-numeric:tabular-nums}
.em-frame{border:1px solid var(--cs-border-subtle);border-radius:12px;overflow:hidden;background:var(--cs-surface-raised)}
.em-meta{padding:12px 18px;display:grid;grid-template-columns:70px minmax(0,1fr);gap:4px 10px;font-size:13px;line-height:18px;background:var(--cs-surface-subtle);border-bottom:1px solid var(--cs-border-subtle)}
.em-body{padding:18px 22px;display:flex;flex-direction:column;gap:12px;font-size:15px;line-height:23px}
.em-p{margin:0;white-space:pre-line}
.tx{}
.mg{background:var(--cs-surface-brand);color:var(--cs-text-brand);border-radius:4px;padding:0 3px;font-weight:500}
.rg{background:var(--cs-status-info-bg);color:var(--cs-status-info-text);border-radius:4px;padding:0 3px;font-weight:500}
.em-btn{align-self:flex-start;min-height:40px;padding:0 18px;border-radius:999px;background:var(--cs-action-primary);color:var(--cs-action-on-primary);display:inline-flex;align-items:center;font-size:14px;font-weight:500}
.em-foot{font-size:12px;line-height:17px;color:var(--cs-text-muted);border-top:1px solid var(--cs-border-subtle);padding-top:10px}
.sms{align-self:flex-start;max-width:85%;background:var(--cs-surface-subtle);border-radius:16px 16px 16px 4px;padding:10px 14px;font-size:14px;line-height:20px}
.ta{width:100%;box-sizing:border-box;padding:10px 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;line-height:20px;resize:vertical}
.ta-big{min-height:420px;font-size:13px;line-height:19px}
.ta-sm{min-height:64px}
.in{box-sizing:border-box;min-height:40px;padding:0 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px}
.kv{display:grid;grid-template-columns:132px minmax(0,1fr);gap:8px 12px;font-size:13px;line-height:18px}
.kv-k{color:var(--cs-text-muted)}
.ck{display:flex;gap:10px;align-items:flex-start;padding:9px 0;border-top:1px solid var(--cs-border-subtle);font-size:13px;line-height:18px}
.cmp{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
.cmp-c{padding:10px 14px;font-size:14px;line-height:21px;border-top:1px solid var(--cs-border-subtle);white-space:pre-line}
.d-same{color:var(--cs-text-secondary)}
.d-old{background:var(--cs-status-error-bg);color:var(--cs-status-error-text)}
.d-new{background:var(--cs-status-success-bg);color:var(--cs-status-success-text)}
.au-row{display:flex;gap:12px;align-items:flex-start;padding:10px 20px;border-top:1px solid var(--cs-border-subtle)}
.au-main{flex:1;min-width:0;display:grid;grid-template-columns:42px minmax(0,2.6fr) minmax(0,1fr) minmax(0,1.5fr) 150px;gap:12px;align-items:start;border:0;background:transparent;color:var(--cs-text-primary);font:inherit;font-size:13px;line-height:18px;text-align:left;cursor:pointer;padding:0;min-height:36px}
.sw{width:46px;height:28px;flex-shrink:0;border:0;border-radius:999px;padding:3px;display:flex;align-items:center;cursor:pointer;margin-top:2px}
.sw-on{background:var(--cs-action-primary);justify-content:flex-end}
.sw-off{background:var(--cs-border-default);justify-content:flex-start}
.sw span{width:22px;height:22px;border-radius:999px;background:var(--cs-surface-raised);display:block}
.lockbox{width:46px;height:28px;flex-shrink:0;border-radius:999px;background:var(--cs-surface-brand);color:var(--cs-text-brand);display:flex;align-items:center;justify-content:center;margin-top:2px}
.au-det{margin:0 20px 12px 78px;padding:14px 16px;border-radius:12px;background:var(--cs-surface-subtle);display:flex;flex-direction:column;gap:12px}
.box{padding:12px 14px;border-radius:10px;font-size:13px;line-height:19px;display:flex;flex-direction:column;gap:8px}
.bx-bad{background:var(--cs-status-error-bg);color:var(--cs-status-error-text)}
.bx-ok{background:var(--cs-status-success-bg);color:var(--cs-status-success-text)}
.bx-brand{background:var(--cs-surface-brand);color:var(--cs-text-brand)}
.bx-warn{background:var(--cs-status-warning-bg);color:var(--cs-status-warning-text)}
.bx-plain{background:var(--cs-surface-raised);color:var(--cs-text-primary);border:1px solid var(--cs-border-subtle)}
.lk{flex:1 1 300px;min-width:0;padding:14px 16px;border:1px solid var(--cs-border-subtle);border-radius:12px;display:flex;flex-direction:column;gap:6px;background:var(--cs-surface-raised)}
.pick{min-height:36px;padding:0 12px;border-radius:999px;font:inherit;font-size:13px;cursor:pointer}
.chips{display:flex;gap:6px;flex-wrap:wrap}
.sg-row{display:flex;gap:14px;align-items:flex-start;padding:12px 20px;border-top:1px solid var(--cs-border-subtle);font-size:14px;line-height:20px}
'''

TABS = '''      <div role="tablist" aria-label="Show" style="display: flex; gap: 6px; flex-wrap: wrap;">
        <sc-for list="{{tabs}}" as="tb" hint-placeholder-count="3">
          <button class="{{tb.cls}}" role="tab" aria-selected="{{tb.sel}}" onClick="{{tb.pick}}">{{tb.label}}</button>
        </sc-for>
      </div>
'''

B82 = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px; max-width: 820px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Messages and automations</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Every email and text the Hub sends to clients, the rules that send them, and how they sound. Timings come from Rules and promises (board 80), so a change there shows here and in every email at once.</span>
        </div>
        <span class="sb-sub">Signed in as Collins, super admin 1. Mon 2 Nov</span>
      </div>
      <div class="{{dec.cls}}" style="padding: 14px 18px; border-radius: 12px; display: flex; gap: 14px; align-items: center; flex-wrap: wrap;">
        <x-import component-from-global-scope="CareSync.Icon" name="{{dec.icon}}" size="{{n20}}"></x-import>
        <span style="flex: 1 1 520px; font-size: 14px; line-height: 20px;"><b style="font-weight: 600;">{{dec.title}}</b> {{dec.text}}</span>
        <button class="sb-btn b-pri" onClick="{{goNop}}">{{dec.cta}}</button>
      </div>
      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="4">
          <div class="sb-card sb-kpi"><span class="sb-muted">{{k.label}}</span><span class="sb-kv">{{k.value}}</span><span class="sb-sub">{{k.note}}</span></div>
        </sc-for>
      </div>
''' + TABS + '''
      <sc-if value="{{isLib}}" hint-placeholder-val="{{ true }}">
      <section class="sb-card" aria-labelledby="lib-h">
        <div class="sb-head">
          <div style="display: flex; flex-direction: column; gap: 2px;"><h2 id="lib-h" class="sb-h2">Email library</h2><span class="sb-sub">{{libSummary}}</span></div>
          <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
            <input class="in" aria-label="Find an email" placeholder="Find by number, name or trigger" value="{{q}}" onChange="{{onQ}}" style="width: 280px;">
            <button class="sb-btn b-gh" onClick="{{toggleAll}}">{{allLabel}}</button>
          </div>
        </div>
        <div class="ml-grid" style="padding: 6px 20px 8px;"><span class="sb-th">No.</span><span class="sb-th">Email and trigger</span><span class="sb-th">Timing (from Rules and promises)</span><span class="sb-th">Ver.</span><span class="sb-th">Last changed by</span><span class="sb-th">Status</span></div>
        <sc-for list="{{secs}}" as="s" hint-placeholder-count="11">
          <button class="ml-sec" aria-expanded="{{s.exp}}" onClick="{{s.toggle}}">
            <x-import component-from-global-scope="CareSync.Icon" name="{{s.icon}}" size="{{n16}}"></x-import>
            <span style="font-weight: 500;">{{s.name}}</span><span class="sb-muted">{{s.count}}</span>
            <sc-for list="{{s.flags}}" as="f" hint-placeholder-count="1"><span class="{{f.cls}}">{{f.t}}</span></sc-for>
          </button>
          <sc-if value="{{s.open}}" hint-placeholder-val="{{ false }}">
            <sc-for list="{{s.rows}}" as="e" hint-placeholder-count="6">
              <button class="{{e.cls}}" onClick="{{e.pick}}" aria-pressed="{{e.pressed}}">
                <span class="ml-grid">
                  <span class="num">{{e.num}}</span>
                  <span style="display: flex; flex-direction: column; gap: 2px; min-width: 0;"><span style="font-weight: 500; font-size: 14px;">{{e.name}}</span><span class="sb-muted">{{e.trig}}</span></span>
                  <span class="sb-sub">{{e.timing}}</span>
                  <span>{{e.ver}}</span>
                  <span class="sb-sub">{{e.changed}}</span>
                  <span class="chips"><sc-for list="{{e.tags}}" as="t" hint-placeholder-count="2"><span class="{{t.cls}}">{{t.t}}</span></sc-for></span>
                </span>
              </button>
            </sc-for>
          </sc-if>
        </sc-for>
        <div class="sb-row sb-muted" style="justify-content: space-between;"><span>From the client emails spec of 2 November 2026. Every email follows section 12: timings from the registry, no regulator timescales, never "free".</span><span>{{libFoot}}</span></div>
      </section>

      <section class="sb-card" aria-labelledby="pv-h">
        <div class="sb-head">
          <div style="display: flex; flex-direction: column; gap: 2px;">
            <h2 id="pv-h" class="sb-h2">{{pv.title}}</h2>
            <span class="sb-sub">Preview as a real client: {{pv.clientLabel}}. Merge fields are filled from the client record; <span class="mg">teal</span> is client data, <span class="rg">blue</span> comes from Rules and promises.</span>
          </div>
          <sc-if value="{{pv.isNop}}" hint-placeholder-val="{{ true }}">
            <div class="chips" role="group" aria-label="Version">
              <sc-for list="{{modes}}" as="m" hint-placeholder-count="3"><button class="{{m.cls}}" aria-pressed="{{m.sel}}" onClick="{{m.pick}}">{{m.label}}</button></sc-for>
            </div>
          </sc-if>
        </div>
        <div style="padding: 0 20px 20px; display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
          <div style="flex: 3 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 10px;">
            <sc-if value="{{pv.showMail}}" hint-placeholder-val="{{ true }}">
            <div class="em-frame">
              <div class="em-meta">
                <span class="kv-k">From</span><span>{{pv.from}}</span>
                <span class="kv-k">Reply to</span><span>{{pv.reply}}</span>
                <span class="kv-k">To</span><span>{{pv.to}}</span>
                <span class="kv-k">Subject</span><span style="font-weight: 500;"><sc-for list="{{pv.subject}}" as="g" hint-placeholder-count="2"><span class="{{g.cls}}">{{g.t}}</span></sc-for></span>
              </div>
              <div class="em-body">
                <sc-for list="{{pv.texts}}" as="x" hint-placeholder-count="0">
                  <span class="sb-muted">{{x.label}}</span>
                  <div class="sms"><sc-for list="{{x.segs}}" as="g" hint-placeholder-count="3"><span class="{{g.cls}}">{{g.t}}</span></sc-for></div>
                </sc-for>
                <sc-for list="{{pv.paras}}" as="p" hint-placeholder-count="5">
                  <p class="em-p"><sc-for list="{{p.segs}}" as="g" hint-placeholder-count="3"><span class="{{g.cls}}">{{g.t}}</span></sc-for></p>
                </sc-for>
                <sc-if value="{{pv.hasBtn}}" hint-placeholder-val="{{ true }}"><span class="em-btn">{{pv.button}}</span></sc-if>
                <sc-if value="{{pv.growth}}" hint-placeholder-val="{{ false }}"><span class="em-foot">You are receiving this because you are a Care Sync client. You can choose which updates you get in your Hub, or reply "stop".</span></sc-if>
              </div>
            </div>
            </sc-if>
            <sc-if value="{{pv.showCmp}}" hint-placeholder-val="{{ false }}">
            <div class="em-frame">
              <div class="cmp"><span class="cmp-c sb-th" style="border-top: 0;">{{cmpLeft}}</span><span class="cmp-c sb-th" style="border-top: 0;">{{cmpRight}}</span></div>
              <sc-for list="{{cmp}}" as="c" hint-placeholder-count="6">
                <div class="cmp"><span class="{{c.lc}}">{{c.a}}</span><span class="{{c.rc}}">{{c.b}}</span></div>
              </sc-for>
            </div>
            <span class="sb-muted">{{cmpNote}}</span>
            </sc-if>
            <span class="sb-sub">{{pv.note}}</span>
          </div>
          <div style="flex: 2 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 14px;">
            <div class="box bx-plain">
              <span style="font-weight: 500; font-size: 14px;">Merge fields, filled</span>
              <div class="kv"><sc-for list="{{pv.fields}}" as="f" hint-placeholder-count="4"><span class="kv-k">{{f.k}}</span><span>{{f.v}}</span></sc-for></div>
            </div>
            <sc-if value="{{pv.isNop}}" hint-placeholder-val="{{ true }}">
            <div class="box bx-plain">
              <span style="font-weight: 500; font-size: 14px;">Sunrise Homecare: dates worked out the safe way</span>
              <div class="kv"><sc-for list="{{nopDates}}" as="f" hint-placeholder-count="6"><span class="kv-k">{{f.k}}</span><span>{{f.v}}</span></sc-for></div>
              <span class="sb-muted">The day of service counts as day 1, so 28 days ends 27 days after service. If the service date is unclear, the earliest possible date is used. Worked out the safe way; confirm with a legal adviser.</span>
            </div>
            </sc-if>
            <div class="box bx-plain">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: baseline;"><span style="font-weight: 500; font-size: 14px;">Brand voice check</span><span class="{{voice.cls}}">{{voice.sum}}</span></div>
              <sc-for list="{{voice.items}}" as="v" hint-placeholder-count="6">
                <div class="ck"><span class="{{v.cls}}">{{v.state}}</span><span style="display: flex; flex-direction: column;"><span style="font-weight: 500;">{{v.label}}</span><span class="sb-muted">{{v.note}}</span></span></div>
              </sc-for>
            </div>
            <div class="box bx-plain">
              <span style="font-weight: 500; font-size: 14px;">Sent by, and where it shows</span>
              <sc-for list="{{pv.usedBy}}" as="u" hint-placeholder-count="2"><span class="sb-sub">{{u}}</span></sc-for>
              <sc-if value="{{pv.lockNote}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-brand">{{pv.lockNote}}</span></sc-if>
            </div>
          </div>
        </div>
      </section>

      <sc-if value="{{pv.isNop}}" hint-placeholder-val="{{ true }}">
      <section class="sb-card" aria-labelledby="ap-h">
        <div class="sb-head">
          <div style="display: flex; flex-direction: column; gap: 2px;"><h2 id="ap-h" class="sb-h2">Version 3: draft and approval</h2><span class="sb-sub">Legal wording, so it needs a super admin who did not write or change it (decision 6 on Home). Emails already sent are never changed.</span></div>
          <span class="{{ap.cls}}">{{ap.chip}}</span>
        </div>
        <div style="padding: 0 20px 20px; display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
          <div style="flex: 3 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 8px;">
            <label for="draft" class="sb-th">The draft. Merge fields are written in square brackets, for example [deadline]. Type to try the brand voice check (add the word "free", or a dash).</label>
            <textarea id="draft" class="ta ta-big" value="{{draft}}" onChange="{{onDraft}}"></textarea>
            <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;"><button class="sb-btn b-gh" onClick="{{resetDraft}}">Undo my changes</button><span class="sb-muted">{{draftNote}}</span></div>
          </div>
          <div style="flex: 2 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 12px;">
            <div class="box bx-plain">
              <span style="font-weight: 500; font-size: 14px;">History of this version</span>
              <sc-for list="{{ap.hist}}" as="h" hint-placeholder-count="2"><span class="sb-sub">{{h}}</span></sc-for>
            </div>
            <div style="display: flex; flex-direction: column; gap: 6px;">
              <span class="sb-th">Acting as (demo switch)</span>
              <div class="chips"><sc-for list="{{whos}}" as="w" hint-placeholder-count="3"><button class="{{w.cls}}" aria-pressed="{{w.sel}}" onClick="{{w.pick}}">{{w.label}}</button></sc-for></div>
            </div>
            <label for="apr" class="sb-th">{{ap.reasonLabel}}</label>
            <textarea id="apr" class="ta ta-sm" placeholder="{{ap.ph}}" value="{{reason}}" onChange="{{onReason}}"></textarea>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <sc-if value="{{ap.canSend}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-pri" onClick="{{sendAp}}">Send for approval</button></sc-if>
              <sc-if value="{{ap.canDecide}}" hint-placeholder-val="{{ true }}"><button class="sb-btn b-pri" onClick="{{approve}}">Approve version 3</button><button class="sb-btn b-gh" onClick="{{decline}}">Send back to the author</button></sc-if>
              <sc-if value="{{ap.done}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" onClick="{{restart}}">Reset the demo</button></sc-if>
            </div>
            <sc-if value="{{msg}}" hint-placeholder-val="{{ false }}"><div class="box bx-warn">{{msg}}</div></sc-if>
            <sc-if value="{{ap.doneText}}" hint-placeholder-val="{{ false }}"><div class="box bx-ok">{{ap.doneText}}</div></sc-if>
            <span class="sb-muted">Approvals are logged in the audit log (Security, board 84) and the weekly super admin summary.</span>
          </div>
        </div>
      </section>
      </sc-if>
      </sc-if>

      <sc-if value="{{isAuto}}" hint-placeholder-val="{{ false }}">
      <section class="sb-card" aria-labelledby="lk-h">
        <div class="sb-head"><div style="display: flex; flex-direction: column; gap: 2px;"><h2 id="lk-h" class="sb-h2">Rules nobody can switch off</h2><span class="sb-sub">These protect clients and Care Sync's reputation. Their wording and timings can change; the rule itself cannot. Spec section 51.4.</span></div><span class="sb-chip c-brand">{{lockCount}}</span></div>
        <div style="padding: 0 20px 20px; display: flex; gap: 12px; flex-wrap: wrap;">
          <sc-for list="{{lockTiles}}" as="l" hint-placeholder-count="5">
            <div class="lk"><span style="display: flex; gap: 8px; align-items: center; font-weight: 500; font-size: 14px;"><x-import component-from-global-scope="CareSync.Icon" name="lock" size="{{n16}}"></x-import>{{l.t}}</span><span class="sb-sub">{{l.d}}</span><span class="sb-muted">{{l.r}}</span></div>
          </sc-for>
        </div>
      </section>
      <section class="sb-card" aria-labelledby="au-h">
        <div class="sb-head">
          <div style="display: flex; flex-direction: column; gap: 2px;"><h2 id="au-h" class="sb-h2">Automations: when this happens, do that</h2><span class="sb-sub">{{autoSummary}}</span></div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
            <div class="chips" role="group" aria-label="Filter"><sc-for list="{{filts}}" as="f" hint-placeholder-count="4"><button class="{{f.cls}}" aria-pressed="{{f.sel}}" onClick="{{f.pick}}">{{f.label}}</button></sc-for></div>
            <button class="sb-btn b-gh" onClick="{{toggleGroups}}">{{grpLabel}}</button>
          </div>
        </div>
        <div style="display: flex; gap: 12px; padding: 6px 20px 8px;"><span class="sb-th" style="width: 46px;">On</span><span style="flex: 1; display: grid; grid-template-columns: 42px minmax(0,2.6fr) minmax(0,1fr) minmax(0,1.5fr) 150px; gap: 12px;"><span class="sb-th">Id</span><span class="sb-th">When this happens, do that</span><span class="sb-th">Owner</span><span class="sb-th">Last run</span><span class="sb-th">Last 7 days</span></span></div>
        <sc-for list="{{groups}}" as="g" hint-placeholder-count="9">
          <button class="ml-sec" aria-expanded="{{g.exp}}" onClick="{{g.toggle}}">
            <x-import component-from-global-scope="CareSync.Icon" name="{{g.icon}}" size="{{n16}}"></x-import>
            <span style="font-weight: 500;">{{g.name}}</span><span class="sb-muted">{{g.count}}</span>
            <sc-for list="{{g.flags}}" as="f" hint-placeholder-count="1"><span class="{{f.cls}}">{{f.t}}</span></sc-for>
          </button>
          <sc-if value="{{g.open}}" hint-placeholder-val="{{ false }}">
            <sc-for list="{{g.rows}}" as="r" hint-placeholder-count="6">
              <div class="au-row">
                <sc-if value="{{r.isLock}}" hint-placeholder-val="{{ false }}"><span class="lockbox" title="Locked" aria-label="Locked: cannot be switched off"><x-import component-from-global-scope="CareSync.Icon" name="lock" size="{{n16}}"></x-import></span></sc-if>
                <sc-if value="{{r.isSw}}" hint-placeholder-val="{{ true }}"><button class="{{r.swCls}}" role="switch" aria-checked="{{r.ariaOn}}" aria-label="{{r.swLabel}}" onClick="{{r.flip}}"><span></span></button></sc-if>
                <sc-if value="{{r.later}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-neutral" style="width: 46px; justify-content: center; margin-top: 4px;">Later</span></sc-if>
                <button class="au-main" aria-expanded="{{r.exp}}" onClick="{{r.toggle}}">
                  <span class="num">{{r.id}}</span>
                  <span style="display: flex; flex-direction: column; gap: 2px; min-width: 0;"><span style="font-weight: 500; font-size: 14px;">{{r.name}}</span><span class="sb-muted">When: {{r.trig}}</span></span>
                  <span class="sb-sub">{{r.owner}}</span>
                  <span class="sb-sub">{{r.last}}</span>
                  <span class="chips"><span class="sb-chip c-neutral">{{r.runs}}</span><span class="{{r.failCls}}">{{r.failT}}</span></span>
                </button>
              </div>
              <sc-if value="{{r.open}}" hint-placeholder-val="{{ false }}">
                <div class="au-det">
                  <div class="kv" style="grid-template-columns: 120px minmax(0,1fr);">
                    <span class="kv-k">When</span><span>{{r.trig}}</span>
                    <span class="kv-k">Then</span><span>{{r.act}}</span>
                    <span class="kv-k">Timing</span><span>{{r.timing}}</span>
                    <span class="kv-k">Owner</span><span>{{r.owner}}</span>
                    <span class="kv-k">If it fails</span><span>{{r.retry}}</span>
                    <span class="kv-k">Clients today</span><span>{{r.aff}}</span>
                  </div>
                  <div style="display: flex; flex-direction: column; gap: 6px;"><span class="sb-th">What depends on this</span>
                    <div class="chips"><sc-for list="{{r.emails}}" as="m" hint-placeholder-count="2"><span class="sb-chip c-info">{{m}}</span></sc-for><sc-for list="{{r.screens}}" as="m" hint-placeholder-count="2"><span class="sb-chip c-neutral">{{m}}</span></sc-for></div>
                  </div>
                  <sc-if value="{{r.lock}}" hint-placeholder-val="{{ false }}"><div class="box bx-brand"><span style="font-weight: 500;">Locked. Why it cannot be switched off</span><span>{{r.lock}}</span></div></sc-if>
                  <sc-if value="{{r.later}}" hint-placeholder-val="{{ false }}"><div class="box bx-plain">WhatsApp is a later phase. It stays off until it is built and switched on in Sending and wording. Phase 1 uses email, the Hub bell, and texts only for the introduction call and urgent legal deadlines.</div></sc-if>
                  <sc-if value="{{r.isGw}}" hint-placeholder-val="{{ false }}">
                    <div class="{{gw.cls}}">
                      <span style="font-weight: 500;">{{gw.title}}</span>
                      <span>{{gw.text}}</span>
                      <sc-if value="{{gw.blocked}}" hint-placeholder-val="{{ true }}">
                        <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
                          <input class="in" aria-label="New email address for Tunde Bello" placeholder="New address, confirmed with Tunde by phone" value="{{gwAddr}}" onChange="{{onGw}}" style="flex: 1 1 280px;">
                          <button class="sb-btn b-pri" onClick="{{gwSave}}">Save the confirmed address</button>
                          <span class="sb-chip c-neutral">Retry now: blocked</span>
                        </div>
                      </sc-if>
                      <sc-if value="{{gw.fixed}}" hint-placeholder-val="{{ false }}"><div><button class="sb-btn b-pri" onClick="{{gwRetry}}">Retry now</button></div></sc-if>
                      <sc-if value="{{gwMsg}}" hint-placeholder-val="{{ false }}"><span>{{gwMsg}}</span></sc-if>
                    </div>
                  </sc-if>
                  <sc-if value="{{r.asking}}" hint-placeholder-val="{{ false }}">
                    <div class="box bx-warn">
                      <span style="font-weight: 500;">Switch off {{r.id}}? Clients affected today: {{r.aff}}</span>
                      <span>The emails and screens above stop getting what this rule does. Switching off is logged and shows on System health (board 86) until it is back on.</span>
                      <textarea class="ta ta-sm" aria-label="Reason for switching off" placeholder="Reason (required)" value="{{offWhy}}" onChange="{{onOffWhy}}"></textarea>
                      <div style="display: flex; gap: 8px;"><button class="sb-btn b-pri" onClick="{{confirmOff}}">Switch off</button><button class="sb-btn b-gh" onClick="{{cancelOff}}">Keep it on</button></div>
                      <sc-if value="{{offMsg}}" hint-placeholder-val="{{ false }}"><span>{{offMsg}}</span></sc-if>
                    </div>
                  </sc-if>
                  <sc-if value="{{r.offNote}}" hint-placeholder-val="{{ false }}"><div class="box bx-warn">{{r.offNote}}</div></sc-if>
                </div>
              </sc-if>
            </sc-for>
          </sc-if>
        </sc-for>
      </section>
      </sc-if>

      <sc-if value="{{isSend}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; gap: 18px; flex-wrap: wrap; align-items: flex-start;">
        <div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
          <section class="sb-card" aria-labelledby="ad-h">
            <div class="sb-head"><h2 id="ad-h" class="sb-h2">Sending addresses</h2><span class="sb-chip c-ok">Domain checks passed</span></div>
            <sc-for list="{{addrs}}" as="a" hint-placeholder-count="4">
              <div class="sg-row"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{a.t}}</span><span class="sb-sub">{{a.v}}</span><span class="sb-muted">{{a.n}}</span></span><span class="chips" style="justify-content: flex-end; max-width: 220px;"><sc-for list="{{a.chips}}" as="c" hint-placeholder-count="2"><span class="sb-chip c-ok">{{c}}</span></sc-for></span></div>
            </sc-for>
            <div class="sg-row sb-muted">Last domain check Mon 2 Nov 06:00. Bounces and failed checks show on System health (board 86).</div>
          </section>
          <section class="sb-card" aria-labelledby="sig-h">
            <div class="sb-head"><h2 id="sig-h" class="sb-h2">Signatures</h2><span class="sb-sub">Every email is signed by a real person. Replies go to them and into the Hub</span></div>
            <div style="padding: 0 20px 16px; display: flex; flex-direction: column; gap: 10px;">
              <div class="chips"><sc-for list="{{sigs}}" as="g" hint-placeholder-count="5"><button class="{{g.cls}}" aria-pressed="{{g.sel}}" onClick="{{g.pick}}">{{g.label}}</button></sc-for></div>
              <div class="box bx-plain" style="font-size: 14px; line-height: 21px;"><span style="white-space: pre-line;">{{sigText}}</span></div>
              <span class="sb-muted">{{sigNote}}</span>
            </div>
          </section>
          <section class="sb-card" aria-labelledby="ch-h">
            <div class="sb-head"><h2 id="ch-h" class="sb-h2">Channels</h2><span class="sb-sub">Phase 1. The client chooses the channel for the weekly update; they cannot switch the update off</span></div>
            <sc-for list="{{chans}}" as="c" hint-placeholder-count="4">
              <div class="sg-row"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{c.t}}</span><span class="sb-sub">{{c.n}}</span></span><span class="{{c.cls}}">{{c.s}}</span></div>
            </sc-for>
          </section>
        </div>
        <div style="flex: 1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
          <section class="sb-card" aria-labelledby="qh-h">
            <div class="sb-head"><h2 id="qh-h" class="sb-h2">Quiet hours</h2><span class="sb-chip c-brand">Always on: locked</span></div>
            <div style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 10px;">
              <span style="font-size: 26px; line-height: 34px; font-weight: 600;">{{quiet}}</span>
              <span class="sb-sub">No automated emails or texts in these hours. They wait and go at the end of quiet hours. The hours are set once in Rules and promises (board 80); clients can choose wider quiet hours in their account (board 29).</span>
              <span class="sb-th">What still goes through</span>
              <sc-for list="{{through}}" as="t" hint-placeholder-count="3"><span class="sb-sub">{{t}}</span></sc-for>
              <div class="box bx-plain"><span class="sb-th">Example this week</span><span>Harbour Lane's form arrived Thu 29 Oct at 21:46. Email 2.3 waited and went at 08:00 on Fri 30 Oct.</span></div>
              <div class="kv"><span class="kv-k">Working hours</span><span>{{workHours}}</span><span class="kv-k">Bank holidays</span><span>{{bankHol}}</span></div>
            </div>
          </section>
          <section class="sb-card" aria-labelledby="ww-h">
            <div class="sb-head"><h2 id="ww-h" class="sb-h2">Words we never use with clients</h2><span class="sb-sub">The brand voice check uses this list</span></div>
            <sc-for list="{{wordRows}}" as="w" hint-placeholder-count="8">
              <div class="sg-row" style="padding: 9px 20px;"><span style="flex: 0 0 140px; font-weight: 500;">{{w.w}}</span><span class="sb-sub" style="flex: 1;">{{w.u}}</span></div>
            </sc-for>
            <div class="sg-row" style="flex-wrap: wrap;">
              <input class="in" aria-label="Word to add" placeholder="Add a word or phrase" value="{{newWord}}" onChange="{{onWord}}" style="flex: 1 1 200px;">
              <button class="sb-btn b-sec" onClick="{{addWord}}">Add to the list</button>
            </div>
            <sc-if value="{{wordMsg}}" hint-placeholder-val="{{ false }}"><div class="sg-row sb-sub">{{wordMsg}}</div></sc-if>
          </section>
          <section class="sb-card" aria-labelledby="wr-h">
            <div class="sb-head"><h2 id="wr-h" class="sb-h2">Wording rules on every message</h2></div>
            <sc-for list="{{wrules}}" as="w" hint-placeholder-count="7">
              <div class="sg-row" style="padding: 9px 20px;"><span style="flex: 1;">{{w.t}}</span><span class="{{w.cls}}">{{w.s}}</span></div>
            </sc-for>
          </section>
        </div>
      </div>
      </sc-if>
'''

S82 = r'''const LIB = __LIB__;
const RULES = __RULES__;
const GROUPS = __GROUPS__;
const BOARDS = __BOARDS__;
const V2 = __V2__;
const V3 = __V3__;
const D0 = new Date(2026, 10, 2);
const DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const addD = (d, n) => { const x = new Date(d.getTime()); x.setDate(x.getDate() + n); return x; };
const fL = d => DAYS[d.getDay()] + ' ' + d.getDate() + ' ' + MONTHS[d.getMonth()];
const fS = d => DAYS[d.getDay()].slice(0, 3) + ' ' + d.getDate() + ' ' + MONTHS[d.getMonth()].slice(0, 3);
const diff = (a, b) => Math.round((a - b) / 86400000);
const wdBefore = (d, n) => { let x = new Date(d.getTime()); while (n > 0) { x = addD(x, -1); if (x.getDay() !== 0 && x.getDay() !== 6) n--; } return x; };
const G = (k, f) => (window.CSR ? CSR.get(k, f) : f);
const money = n => '£' + Number(n).toLocaleString('en-GB');
const WORDS0 = [['free', 'Say "as part of your package" or "included". Staff screens say "no charge to the client"'], ['guarantee', 'Say what we will do. Never promise an outcome'], ['patient', 'Say "the people you support"'], ['cheap', 'Say "fixed fee"'], ['basic', 'Name what is included'], ['reach out', 'Say "get in touch"'], ['residents', 'In home care and supported living, say "the people you support"']];
const SA = ['Collins', 'Rachel Turner'];
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { tab: 'lib', open: { '5': true }, all: false, q: '', sel: '5.2', mode: 'v3', draft: V3, base: V3, who: 'Collins', reason: '', appr: 'waiting', authors: ['Daniel Mensah'], hist: ['Written by Daniel Mensah, Fri 30 Oct 16:40. Sent for approval: "Clearer legal wording about the 28 days, worked out the safe way."'], msg: '', doneText: '',
      grp: { del: true }, gall: false, filt: 'all', ropen: 'A16', on: {}, offAsk: '', offWhy: '', offMsg: '', offNotes: {}, gw: 'blocked', gwAddr: '', gwMsg: '', fails16: 1,
      words: WORDS0, newWord: '', wordMsg: '', sig: 'consultant' };
  }
  tokens() {
    const day = G('weekly-update-day', 'Friday');
    const nd = (() => { const i = DAYS.indexOf(day); let x = addD(D0, 1); while (x.getDay() !== i) x = addD(x, 1); return x; })();
    const sa = G('send-after-signing', '2 working days');
    const ts = Number(G('tender-submit-days-before', 2)), ta = Number(G('tender-approve-days-before', 5)), td = Number(G('tender-draft-days-before', 10));
    const dl = new Date(2026, 11, 1);
    const words = ['none', 'one', 'two', 'three', 'four', 'five', 'six'];
    const am = Number(G('aftercare-months', 12));
    return {
      update_day: day, update_time: G('weekly-update-time', '16:00'), quiet: G('quiet-hours', '8pm to 8am'),
      form_rem: G('form-reminders', 'after 2 days and 4 days; Grace calls on day 6; then weekly'), doc_rem: G('document-reminders', 'after 3 days, then weekly'),
      third_rem: G('third-party-reminders', 'after 3 working days, then weekly'), sig_rem: G('signature-reminders', 'after 2 days, then the consultant calls'),
      draft_rem: G('draft-review-reminder', 'after 3 days'), review_days: String(G('review-reminder-days', 7)), send_after: sa, send_days: String(parseInt(sa, 10) || 2),
      expiry_weeks: String(G('expiry-warning-weeks', 6)), sessions: String(G('sessions-included', 3)), insp_month: String(G('inspection-readiness-month', 4)),
      months_left: String(am - 1), aftercare_yes: 'Your ' + am + ' months of aftercare start today.',
      aftercare_no: 'Your Registration File has everything you need, and we will call you this week to hand over. If you would like us beside you for the first year, ask about aftercare.',
      bg_hours: String(G('break-glass-hours', 4)), rfi: String(G('rfi-target-days-before', 4)), intro_call: G('intro-call', '2 working hours'), unanswered: G('unanswered-red', '1 working day'),
      nop_draft: String(G('nop-draft-day', 14)), nop_review: String(G('nop-review-day', 20)), nop_send: String(G('nop-send-day', 21)),
      tender_submit: String(ts), tender_approve: String(ta), tender_draft: String(td), tender_submit_words: words[ts] || String(ts),
      t_submit: fL(wdBefore(dl, ts)), t_approve: fL(wdBefore(dl, ta)), t_draft: fL(wdBefore(dl, td)),
      price_pir: money(G('price-pir', 750)), price_sl_addon: money(G('price-sl-addon', 1500)),
      next_update: fL(nd), next_update2: fL(addD(nd, 7)), deadline: fL(addD(new Date(2026, 9, 21), Number(G('nop-legal-days', 28)) - 1))
    };
  }
  check(text) {
    const s = this.state, out = [];
    const am = (text.match(/\b(\w+(iz(e|es|ed|ing|ation)))\b/gi) || []).filter(w => !/^(size|sizes|sized|seize|seized|prize|prizes|citizen)/i.test(w)).concat(text.match(/\b(color|center|organization|program|behavior|favor|honor)\b/gi) || []);
    out.push({ label: 'British English', ok: !am.length, note: am.length ? 'Check: ' + am.join(', ') : 'No American spellings found' });
    const da = /[\u2013\u2014]| - /.test(text);
    out.push({ label: 'No dashes', ok: !da, note: da ? 'A dash was found. Use a comma, colon or full stop' : 'None found' });
    const hits = s.words.filter(w => new RegExp('\\b' + w[0].replace(/\s+/g, '\\s+') + '\\w*', 'i').test(text)).map(w => w[0]);
    out.push({ label: 'Words we never use', ok: !hits.length, note: hits.length ? 'Found: ' + hits.map(h => '"' + h + '"').join(', ') + '. ' + s.words.find(w => w[0] === hits[0])[1] : 'None of the ' + s.words.length + ' words on the list' });
    const sent = text.split(/(?<=[.?])\s+/).filter(x => /\b(CQC|CIW|RQIA|regulator|buyer|council|decision)\b/.test(x) && /\b(usually|normally|typically|most people|on average|expects? to|should hear|will decide|within \d+ (weeks?|months?)|in \d+ (weeks?|months?)|takes? (about|around|roughly))\b/i.test(x));
    out.push({ label: 'No promises about regulator or buyer timescales', ok: !sent.length, warn: true, note: sent.length ? 'Check: "' + sent[0].trim() + '" Only quote a date the regulator or buyer has published, and say it is theirs' : 'No timescale we do not control' });
    const ex = /!/.test(text);
    out.push({ label: 'No exclamation marks', ok: !ex, note: ex ? 'Remove the exclamation mark' : 'None found' });
    const n = (text.match(/[A-Za-z0-9£']+/g) || []).length;
    out.push({ label: 'About 120 words or fewer', ok: n <= 125, warn: true, note: n + ' words' });
    const items = out.map(o => ({ label: o.label, note: o.note, state: o.ok ? 'Pass' : (o.warn ? 'Check' : 'Fix'), cls: 'sb-chip ' + (o.ok ? 'c-ok' : (o.warn ? 'c-warn' : 'c-bad')) }));
    const bad = out.filter(o => !o.ok).length;
    return { items, sum: bad ? bad + (bad === 1 ? ' thing to look at' : ' things to look at') : 'Passes', cls: 'sb-chip ' + (bad ? 'c-warn' : 'c-ok') };
  }
  renderVals() {
    const s = this.state;
    const T = this.tokens();
    const tk = str => String(str).replace(/%%([a-z_0-9]+)%%/g, (m, k) => (T[k] !== undefined ? T[k] : k));
    const seg = g => g[1] === 2 ? { t: T[g[2]] !== undefined ? T[g[2]] : g[2], cls: 'rg' } : { t: g[0], cls: g[1] === 1 ? 'mg' : 'tx' };
    const segText = arr => arr.map(g => seg(g).t).join('');
    // Notice of Proposal dates (worked out the safe way)
    const served = new Date(2026, 9, 21);
    const legal = Number(G('nop-legal-days', 28));
    const dline = addD(served, legal - 1), target = addD(served, Number(G('nop-send-day', 21)) - 1);
    const dDraft = addD(served, Number(G('nop-draft-day', 14)) - 1), dRev = addD(served, Number(G('nop-review-day', 20)) - 1);
    const NV = { first_name: 'Priya', deadline: fL(dline), date_served: fL(served), our_target: fL(target), consultant_name: 'Daniel Mensah' };
    const fillBr = txt => txt.split(/\n\s*\n/).filter(p => p.trim()).map(p => p.split(/(\[[a-z_]+\])/).filter(x => x !== '').map(x => { const m = x.match(/^\[([a-z_]+)\]$/); return m ? { t: NV[m[1]] !== undefined ? NV[m[1]] : x, cls: NV[m[1]] !== undefined ? 'mg' : 'tx' } : { t: x, cls: 'tx' }; }));
    const plain = txt => fillBr(txt).map(p => p.map(g => g.t).join(''));
    const edited = s.draft !== s.base;
    const status = s.appr === 'waiting' && edited ? 'edited' : s.appr;
    const approved = s.appr === 'approved';
    // library rows
    const q = s.q.trim().toLowerCase();
    const all = LIB.reduce((a, x) => a + x.rows.length, 0);
    const sendersOf = num => RULES.filter(r => r.emails.indexOf(num) >= 0);
    const bname = f => BOARDS[f] ? BOARDS[f][1] + ' (board ' + BOARDS[f][0] + ')' : f;
    const secs = LIB.map(sc => {
      const rows = sc.rows.filter(e => !q || (e.num + ' ' + e.name + ' ' + e.trig).toLowerCase().indexOf(q) >= 0);
      const open = q ? rows.length > 0 : (s.all || !!s.open[sc.n]);
      const flags = [];
      if (sc.n === '5') flags.push({ t: approved ? 'v3 approved' : '1 waiting for approval', cls: 'sb-chip ' + (approved ? 'c-ok' : 'c-warn') });
      if (sc.rows.some(e => e.growth)) flags.push({ t: 'Growth: stopped for worried clients', cls: 'sb-chip c-info' });
      if (sc.n === '10' || sc.n === '11') flags.push({ t: 'Sent instead of sections 4 and 5', cls: 'sb-chip c-neutral' });
      if (sc.rows.some(e => e.manual && e.manual.length)) flags.push({ t: '9.4 is never sent automatically', cls: 'sb-chip c-warn' });
      return {
        name: sc.n + '. ' + sc.name, count: rows.length + (rows.length === 1 ? ' message' : ' messages'), open, exp: open ? 'true' : 'false', icon: open ? 'chevron-down' : 'chevron-right', flags,
        toggle: () => this.setState({ open: Object.assign({}, s.open, { [sc.n]: !s.open[sc.n] }), all: false }),
        rows: rows.map(e => {
          let tags = e.tags.map(t => ({ t: t[0], cls: 'sb-chip c-' + t[1] }));
          let ver = e.ver, changed = e.changed;
          if (e.num === '5.2' && approved) { tags = [{ t: 'Live', cls: 'sb-chip c-ok' }, { t: 'Legal wording', cls: 'sb-chip c-brand' }]; ver = 'v3'; changed = s.authors.join(' and ') + ', Mon 2 Nov'; }
          return { num: e.num, name: e.name, trig: tk(e.trig), timing: tk(e.timing), ver, changed, tags, cls: 'ml-row' + (s.sel === e.num ? ' ml-on' : ''), pressed: s.sel === e.num ? 'true' : 'false', pick: () => this.setState({ sel: e.num, msg: '' }) };
        })
      };
    });
    // preview
    const E = LIB.reduce((a, x) => a.concat(x.rows), []).find(e => e.num === s.sel) || LIB[4].rows[1];
    const isNop = E.num === '5.2';
    let paras, fields, text;
    if (isNop) {
      const src = s.mode === 'v2' ? V2 : s.draft;
      const fp = fillBr(src);
      paras = fp.map(p => ({ segs: p }));
      text = fp.map(p => p.map(g => g.t).join('')).join('\n\n');
      fields = [['first_name', 'Priya (client record)'], ['date_served', NV.date_served + ' (from the notice, entered by Daniel)'], ['deadline', NV.deadline + ' (worked out the safe way)'], ['our_target', NV.our_target + ' (day ' + G('nop-send-day', 21) + ' of ' + legal + ', Rules and promises)'], ['consultant_name', 'Daniel Mensah (case owner)']];
    } else {
      paras = E.paras.map(p => ({ segs: p.map(seg) }));
      text = E.paras.map(segText).join('\n\n') + (E.texts.length ? '\n\n' + E.texts.map(x => segText(x.segs)).join('\n\n') : '');
      fields = E.fields.map(f => [f[0], /^%%/.test(f[1]) ? tk(f[1]) + ' (Rules and promises)' : f[1]]);
    }
    const voice = this.check(text);
    const senders = sendersOf(E.num);
    const scr = [];
    senders.forEach(r => r.screens.forEach(f => { if (scr.indexOf(f) < 0) scr.push(f); }));
    const usedBy = senders.length ? senders.map(r => 'Automation ' + r.id + ': ' + r.name).concat(['Shows on: ' + scr.map(bname).join(', ')]) : (E.manual && E.manual.length ? E.manual : ['Sent by hand from the Hub, using this template']);
    const pv = {
      title: E.num + ' ' + E.name, clientLabel: E.clientLabel, isNop, showMail: !(isNop && s.mode === 'cmp'), showCmp: isNop && s.mode === 'cmp',
      from: E.signer + ' at Care Sync <hello@caresyncexperts.co.uk>', reply: E.reply + ', and into the Hub', to: E.to,
      subject: E.subject.map(seg), paras: E.kind === 'texts' ? [] : paras, texts: E.texts.map(x => ({ label: x.label, segs: x.segs.map(seg) })),
      hasBtn: !!E.button && E.kind !== 'texts', button: E.button, growth: E.growth, note: isNop ? (s.mode === 'v2' ? 'Version 2 is live. Sent to Priya on Wed 21 Oct.' : (approved ? 'Version 3 is live for new Notices of Proposal from Mon 2 Nov. Sunrise keeps the version 2 email it had on Wed 21 Oct.' : 'Version 3 is a draft waiting for approval. Nothing is sent from here.')) : tk(E.note),
      fields: fields.map(f => ({ k: f[0], v: f[1] })), usedBy, lockNote: E.lockNote
    };
    if (E.kind === 'texts') { pv.from = 'Care Sync text messages'; pv.reply = 'Replies come into the Hub for Divine'; pv.to = 'Ade Ola, mobile on the client record'; }
    // compare v2 and v3
    const a2 = plain(V2), a3 = plain(s.draft), n = Math.max(a2.length, a3.length), cmp = [];
    for (let i = 0; i < n; i++) { const a = a2[i] || '', b = a3[i] || '', same = a === b; cmp.push({ a: a || ' ', b: b || ' ', lc: 'cmp-c ' + (same ? 'd-same' : 'd-old'), rc: 'cmp-c ' + (same ? 'd-same' : 'd-new') }); }
    const changedN = cmp.filter(c => c.lc.indexOf('d-old') >= 0).length;
    // approval panel
    const isSA = SA.indexOf(s.who) >= 0;
    const ap = {
      chip: { waiting: 'Waiting for approval', edited: 'Changed, not yet sent for approval', approved: 'Approved, version 3 live', declined: 'Sent back to the author' }[status],
      cls: 'sb-chip ' + ({ waiting: 'c-warn', edited: 'c-info', approved: 'c-ok', declined: 'c-bad' }[status]),
      hist: s.hist, canSend: status === 'edited' || status === 'declined', canDecide: status === 'waiting', done: status === 'approved' || status === 'declined', doneText: s.doneText,
      reasonLabel: status === 'waiting' ? 'Reason for your decision (required)' : 'What changed and why (required)',
      ph: status === 'waiting' ? 'For example: checked the 28 day wording against the notice rules; clearer for clients' : 'For example: shorter second paragraph'
    };
    const set = o => this.setState(Object.assign({ msg: '' }, o));
    const whos = [['Collins', 'Collins, super admin 1'], ['Rachel Turner', 'Rachel Turner, super admin 2'], ['Daniel Mensah', 'Daniel Mensah, author']].map(([k, l]) => ({ label: l, sel: s.who === k ? 'true' : 'false', cls: 'pick ' + (s.who === k ? 't-on' : 't-off'), pick: () => set({ who: k }) }));
    const sendAp = () => {
      if (!s.reason.trim()) return set({ msg: 'Write what changed and why first.' });
      const authors = s.authors.indexOf(s.who) >= 0 ? s.authors : s.authors.concat([s.who]);
      this.setState({ appr: 'waiting', base: s.draft, authors, reason: '', doneText: '', hist: s.hist.concat(['Changed by ' + s.who + ', Mon 2 Nov 09:40. Sent for approval: "' + s.reason.trim() + '"']), msg: 'Sent for approval. ' + (authors.length > 1 ? 'Because ' + authors.join(' and ') + ' changed it, only ' + SA.filter(x => authors.indexOf(x) < 0).join(' or ') + ' can approve it.' : 'Collins or Rachel Turner can approve it.') });
    };
    const decide = ok => {
      if (!isSA) return set({ msg: 'Only a super admin can approve or send back. Daniel can change the draft and send it for approval.' });
      if (s.authors.indexOf(s.who) >= 0) return set({ msg: 'You wrote or changed this version, so the other super admin must decide.' });
      if (!s.reason.trim()) return set({ msg: 'Write a reason before you ' + (ok ? 'approve.' : 'send it back.') });
      const line = (ok ? 'Approved by ' : 'Sent back by ') + s.who + ', Mon 2 Nov 09:40: "' + s.reason.trim() + '"';
      this.setState({ appr: ok ? 'approved' : 'declined', reason: '', msg: '', hist: s.hist.concat([line]), doneText: ok ? 'Version 3 is live for new Notices of Proposal (CQC). Emails already sent stay as they were. Home now shows 6 decisions waiting, and the audit log has the entry.' : 'Sent back to ' + s.authors[s.authors.length - 1] + ' with your reason. Version 2 stays live. Home still lists it until a new version is sent.' });
    };
    // automations
    const isOn = r => r.later ? false : (s.on[r.id] !== undefined ? s.on[r.id] : true);
    const fails = r => r.id === 'A16' ? s.fails16 : r.fails;
    const filtFn = { all: () => true, att: r => fails(r) > 0, lock: r => !!r.lock, off: r => !isOn(r) };
    const onCount = RULES.filter(isOn).length, offCount = RULES.length - onCount, lockCount = RULES.filter(r => r.lock).length, failCount = RULES.reduce((a, r) => a + fails(r), 0);
    const groups = GROUPS.map(([gk, gname]) => {
      const rs = RULES.filter(r => r.g === gk && filtFn[s.filt](r));
      const open = s.filt !== 'all' ? rs.length > 0 : (s.gall || !!s.grp[gk]);
      const flags = [];
      const gf = rs.reduce((a, r) => a + fails(r), 0);
      if (gf) flags.push({ t: gf + ' failed', cls: 'sb-chip c-bad' });
      const gl = rs.filter(r => r.lock).length;
      if (gl) flags.push({ t: gl + ' locked', cls: 'sb-chip c-brand' });
      const goff = rs.filter(r => !r.later && !isOn(r)).length;
      if (goff) flags.push({ t: goff + ' switched off', cls: 'sb-chip c-warn' });
      return {
        name: gname, count: rs.filter(isOn).length + ' on of ' + rs.length, open, exp: open ? 'true' : 'false', icon: open ? 'chevron-down' : 'chevron-right', flags, show: rs.length > 0,
        toggle: () => this.setState({ grp: Object.assign({}, s.grp, { [gk]: !s.grp[gk] }), gall: false }),
        rows: rs.map(r => {
          const on = isOn(r), f = fails(r), opn = s.ropen === r.id || s.offAsk === r.id;
          return {
            id: r.id, name: r.name, trig: tk(r.trig), act: tk(r.act), timing: tk(r.timing), owner: r.owner, retry: r.id === 'A16' && s.gw !== 'sent' ? 'Retry blocked until the address is fixed. Daniel confirms it with Tunde by phone.' : r.retry,
            last: r.id === 'A16' && s.gw === 'sent' ? 'Today 09:40, Greenway resent' : r.last, runs: r.later ? 'Never run' : r.runs + (r.runs === 1 ? ' run' : ' runs'),
            failT: f ? f + ' failed' : '0 failed', failCls: 'sb-chip ' + (f ? 'c-bad' : 'c-ok'), aff: r.aff + (r.aff === 1 ? ' client' : ' clients'),
            emails: r.emails.map(m => 'Email ' + m), screens: r.screens.map(bname),
            isLock: !!r.lock, lock: r.lock, later: r.later, isSw: !r.lock && !r.later, swCls: 'sw ' + (on ? 'sw-on' : 'sw-off'), ariaOn: on ? 'true' : 'false', swLabel: (on ? 'Switch off ' : 'Switch on ') + r.id + ' ' + r.name,
            flip: () => { if (on) this.setState({ offAsk: r.id, ropen: r.id, offWhy: '', offMsg: '' }); else this.setState({ on: Object.assign({}, s.on, { [r.id]: true }), offNotes: Object.assign({}, s.offNotes, { [r.id]: '' }), ropen: r.id }); },
            open: opn, exp: opn ? 'true' : 'false', toggle: () => this.setState({ ropen: s.ropen === r.id ? '' : r.id }),
            isGw: r.id === 'A16', asking: s.offAsk === r.id, offNote: s.offNotes[r.id] || ''
          };
        })
      };
    }).filter(g => g.show);
    const gw = {
      blocked: s.gw === 'blocked', fixed: s.gw === 'fixed',
      cls: 'box ' + (s.gw === 'sent' ? 'bx-ok' : 'bx-bad'),
      title: s.gw === 'sent' ? 'Resent to Greenway Support' : 'Failed: weekly update to Greenway Support Ltd (Tunde Bello), Fri 30 Oct 17:02',
      text: s.gw === 'blocked' ? 'The address bounced: the receiving server says the mailbox does not exist. Retry is blocked until the address is fixed, so the same update cannot bounce again. Daniel covers Olu\'s clients this week and confirms the new address with Tunde by phone. Waiting to retry: 0.' : (s.gw === 'fixed' ? 'New address saved: ' + s.gwAddr.trim() + ', confirmed by Daniel by phone. Retry is now open.' : 'Sent Mon 2 Nov 09:40 to ' + s.gwAddr.trim() + '. Delivered. System health (board 86) clears the failure.')
    };
    const T2 = [['lib', 'Email library (' + all + ')'], ['auto', 'Automations (' + onCount + ' on)'], ['send', 'Sending and wording']];
    const sigs = { consultant: ['Consultant', 'Daniel Mensah\nConsultant, Care Sync Experts\nReplies come to me and into your Hub\ncaresyncexperts.co.uk', 'Used on delivery and regulator emails. The client\'s case owner signs.'],
      bid: ['Bid lead', 'Daniel Mensah\nBid lead, Care Sync Experts\nReplies come to me and into your tender workspace\ncaresyncexperts.co.uk', 'Used on tender emails (section 7).'],
      account: ['Account owner', 'Jo Martin\nAccount owner, Care Sync Experts\nReplies come to me and into your Hub\ncaresyncexperts.co.uk', 'Used on 6.3 only, after the case owner agrees.'],
      senior: ['Manager or director', 'Rachel Turner\nOperations manager, Care Sync Experts\nReplies come to me and into your Hub\ncaresyncexperts.co.uk', 'Used on 9.1 (emergency access, signed by whoever approved it) and on complaint replies. 9.2 is signed by a director.'],
      dpl: ['Data protection lead', 'Collins\nData protection lead, Care Sync Experts\nReplies come to me and into your Hub\ncaresyncexperts.co.uk', 'Used on 9.4 (a data incident) only. Collins signs as data protection lead; Rachel Turner, the other super admin, approves each one before it goes.'] };
    return {
      theme: this.props.theme ?? 'light', three: 3, n16: 16, n20: 20, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      tabs: T2.map(([k, l]) => ({ label: l, sel: s.tab === k ? 'true' : 'false', cls: 'sb-tab ' + (s.tab === k ? 't-on' : 't-off'), pick: () => this.setState({ tab: k }) })),
      isLib: s.tab === 'lib', isAuto: s.tab === 'auto', isSend: s.tab === 'send',
      dec: approved ? { cls: 'bx-ok', icon: 'circle-check', title: 'Decision 6 done.', text: 'Email 5.2 Notice of Proposal version 3 was approved by ' + (s.hist[s.hist.length - 1] || '').split(' by ')[1].split(',')[0] + '. Home now shows 6 decisions waiting.', cta: 'See it' }
        : { cls: 'bx-warn', icon: 'clock', title: 'Decision 6 of 7 on Home:', text: 'email 5.2 Notice of Proposal, version 3, written by ' + s.authors.join(' and ') + '. It has legal wording, so a super admin who did not write it approves it: ' + SA.filter(x => s.authors.indexOf(x) < 0).join(' or ') + '.', cta: 'Review it' },
      goNop: () => this.setState({ tab: 'lib', sel: '5.2', open: Object.assign({}, s.open, { '5': true }), mode: 'cmp' }),
      kpis: [
        { label: 'Emails and texts in the library', value: String(all), note: LIB.length + ' sections, from the client emails spec' },
        { label: 'Automations on', value: String(onCount), note: offCount + ' off: ' + (offCount === 2 ? 'WhatsApp, a later phase' : 'including WhatsApp, a later phase') },
        { label: 'Failed in the last 7 days', value: String(failCount), note: failCount ? 'Greenway weekly update, retry blocked until the address is fixed' : 'Nothing failed. Waiting to retry: 0' },
        { label: 'Waiting for approval', value: approved ? '0' : '1', note: approved ? '5.2 version 3 approved today' : '5.2 Notice of Proposal, version 3' }
      ],
      q: s.q, onQ: e => this.setState({ q: e.target.value }), secs, allLabel: s.all ? 'Close all sections' : 'Open all sections', toggleAll: () => this.setState({ all: !s.all, open: s.all ? {} : s.open }),
      libSummary: all + ' messages in ' + LIB.length + ' sections: ' + (all - 1) + ' emails (11.8 reuses the wording of 5.3b) and the introduction call texts (1.3). Choose one to preview it as a real client.',
      libFoot: 'Version 1 of every email was approved at go-live, Thu 1 Oct',
      pv, modes: [['v2', 'Version 2 (live)'], ['v3', approved ? 'Version 3 (live)' : 'Version 3 (waiting)'], ['cmp', 'Compare 2 and 3']].map(([k, l]) => ({ label: l, sel: s.mode === k ? 'true' : 'false', cls: 'pick ' + (s.mode === k ? 't-on' : 't-off'), pick: () => this.setState({ mode: k }) })),
      cmp, cmpLeft: 'Version 2, live since Wed 7 Oct', cmpRight: edited ? 'Version 3 with your changes' : 'Version 3, by Daniel Mensah', cmpNote: changedN + (changedN === 1 ? ' paragraph changed.' : ' paragraphs changed.') + ' Red is version 2, green is version 3, both filled for Sunrise.',
      nopDates: [['Served', fS(served) + ' (day 1)'], ['Today', fS(D0) + ' (day ' + (diff(D0, served) + 1) + ')'], ['Draft by', fS(dDraft) + ' (day ' + G('nop-draft-day', 14) + ')'], ['Senior review', fS(dRev) + ' (day ' + G('nop-review-day', 20) + '), Collins'], ['Our target to send', fS(target) + ' (day ' + G('nop-send-day', 21) + '), ' + diff(target, D0) + ' days away'], ['Legal deadline', fS(dline) + ' (day ' + legal + '), ' + diff(dline, D0) + ' days away'], ['Alerts', 'days 7, 14, 21 and 25, then daily in the last 3 days']].map(([k, v]) => ({ k, v })),
      voice, ap, whos, reason: s.reason, onReason: e => this.setState({ reason: e.target.value }), msg: s.msg,
      draft: s.draft, onDraft: e => this.setState({ draft: e.target.value, mode: s.mode === 'v2' ? 'v3' : s.mode }), resetDraft: () => set({ draft: s.base }),
      draftNote: edited ? 'Changed since it was sent for approval. Send it again, and whoever changed it cannot approve it.' : 'Same as the version sent for approval.',
      sendAp, approve: () => decide(true), decline: () => decide(false),
      restart: () => this.setState({ appr: 'waiting', draft: V3, base: V3, authors: ['Daniel Mensah'], hist: [this.state.hist[0]], msg: '', doneText: '', reason: '' }),
      lockCount: lockCount + ' locked rules', autoSummary: onCount + ' on, ' + offCount + ' off, ' + lockCount + ' locked. ' + failCount + ' failed in the last 7 days, 0 waiting to retry. Every failure shows on System health (board 86) and to its owner, never to the client as an error.',
      lockTiles: [
        { t: 'Review invitation to every registered client', d: 'Once, at registration, with one reminder after ' + T.review_days + ' days. Google and Trustpilot, the client chooses.', r: 'Nobody is held back or steered, whatever their feedback. A27 and A28.' },
        { t: 'Legal deadline alerts', d: 'Notice of Proposal and appeal deadlines, worked out the safe way, with alerts that go through quiet hours.', r: 'A22, A23 and A24. Sunrise (Tue 17 Nov) and Westbrook (Sun 22 Nov) today.' },
        { t: 'Complaint acknowledgement in 1 working day', d: 'To a manager or director not involved, full reply within 20 working days.', r: 'A33. Harbour Lane, Sat 31 Oct: acknowledged in 1 minute.' },
        { t: 'Worried clients get no sales or growth messages', d: 'Until a manager resolves it. Delivery emails and the review invitation still go.', r: 'A31. Riverside Homecare today.' },
        { t: 'Every look shown to the client', d: 'Including view as and emergency access, which also emails the client the same day.', r: 'A34. Collins viewed Harbour Lane today at 08:50.' },
        { t: 'A second person checks before anything goes', d: 'Every pack, regulator reply and weekly update. Absolute, it cannot be relaxed.', r: 'A46. Sunrise\'s draft reply was checked on Fri 30 Oct.' }
      ],
      filts: [['all', 'All ' + RULES.length], ['att', 'Failed ' + failCount], ['lock', 'Locked ' + lockCount], ['off', 'Off ' + offCount]].map(([k, l]) => ({ label: l, sel: s.filt === k ? 'true' : 'false', cls: 'pick ' + (s.filt === k ? 't-on' : 't-off'), pick: () => this.setState({ filt: k }) })),
      grpLabel: s.gall ? 'Close all groups' : 'Open all groups', toggleGroups: () => this.setState({ gall: !s.gall, grp: s.gall ? {} : s.grp }), groups,
      offWhy: s.offWhy, onOffWhy: e => this.setState({ offWhy: e.target.value }), offMsg: s.offMsg,
      confirmOff: () => { if (!s.offWhy.trim()) return this.setState({ offMsg: 'Write a reason first. It goes in the audit log.' }); this.setState({ on: Object.assign({}, s.on, { [s.offAsk]: false }), offNotes: Object.assign({}, s.offNotes, { [s.offAsk]: 'Switched off by Collins, Mon 2 Nov 09:40: "' + s.offWhy.trim() + '". Shows on System health (board 86) until it is back on. Use the switch to turn it on again.' }), offAsk: '', offWhy: '', offMsg: '' }); },
      cancelOff: () => this.setState({ offAsk: '', offWhy: '', offMsg: '' }),
      gw, gwAddr: s.gwAddr, gwMsg: s.gwMsg, onGw: e => this.setState({ gwAddr: e.target.value, gwMsg: '' }),
      gwSave: () => { const a = s.gwAddr.trim(); if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(a)) return this.setState({ gwMsg: 'Enter the full address Tunde confirmed, for example tunde@greenwaysupport.co.uk.' }); this.setState({ gw: 'fixed', gwMsg: '' }); },
      gwRetry: () => this.setState({ gw: 'sent', fails16: 0, gwMsg: '' }),
      addrs: [
        { t: 'Automated Hub messages', v: 'hello@caresyncexperts.co.uk', n: 'Shown as the signer\'s name, for example "Daniel Mensah at Care Sync". Replies go to the signer and into the Hub.', chips: ['SPF passed', 'DKIM passed', 'DMARC passed'] },
        { t: 'Personal emails from staff', v: 'Each person\'s own Google Workspace mailbox, for example daniel.mensah@caresyncexperts.co.uk', n: 'Sent from inside the Hub, so replies thread normally. Every email is saved on the client timeline.', chips: ['Google Workspace connected'] },
        { t: 'Emails to the regulator', v: 'From the client\'s own business email, never from Care Sync', n: 'The login sits in the vault. Logins never appear in any message.', chips: ['Vault'] },
        { t: 'Forwarded mail into the Hub', v: 'One private address per journey, for example brightpath-dom-2611@in.caresynchub.co.uk', n: 'Staff copy or forward regulator emails here. A person confirms before anything changes.', chips: ['Receiving'] }
      ],
      sigs: Object.keys(sigs).map(k => ({ label: sigs[k][0], sel: s.sig === k ? 'true' : 'false', cls: 'pick ' + (s.sig === k ? 't-on' : 't-off'), pick: () => this.setState({ sig: k }) })),
      sigText: sigs[s.sig][1], sigNote: sigs[s.sig][2] + ' No banners or offers in signatures. Growth emails add the opt-out sentence instead.',
      chans: [
        { t: 'Email', n: 'Every message in the library', s: 'On', cls: 'sb-chip c-ok' },
        { t: 'The Hub bell', n: '"Needs you" and "Everything", matching real tasks and news (board 41)', s: 'On', cls: 'sb-chip c-ok' },
        { t: 'Texts', n: 'Only for the introduction call (1.3) and urgent legal deadlines. Follow quiet hours, except legal deadlines', s: 'On, limited', cls: 'sb-chip c-info' },
        { t: 'WhatsApp', n: 'A later phase. L01 and L02 stay off until it is built', s: 'Later, off', cls: 'sb-chip c-neutral' }
      ],
      quiet: T.quiet, workHours: G('working-hours', '09:00 to 17:30, Monday to Friday'), bankHol: G('bank-holidays', 'England and Wales, or Northern Ireland, by the client\'s nation'),
      through: ['Legal deadline alerts for CQC, CIW and RQIA (A23)', 'Tender deadlines within 24 hours', 'Nothing else. Weekly updates go by ' + T.update_time + ', well inside the day'],
      wordRows: s.words.map(w => ({ w: w[0], u: w[1] })), newWord: s.newWord, onWord: e => this.setState({ newWord: e.target.value, wordMsg: '' }), wordMsg: s.wordMsg,
      addWord: () => { const w = s.newWord.trim().toLowerCase(); if (!w) return this.setState({ wordMsg: 'Type a word first.' }); if (s.words.some(x => x[0] === w)) return this.setState({ wordMsg: '"' + w + '" is already on the list.' }); this.setState({ words: s.words.concat([[w, 'Added by Collins today. Suggest a kinder word in the brand voice check']]), newWord: '', wordMsg: '"' + w + '" added. The brand voice check in the library now looks for it.' }); },
      wrules: [
        { t: 'British English and plain words', s: 'Locked', cls: 'sb-chip c-brand' }, { t: 'No dashes anywhere the client reads', s: 'Locked', cls: 'sb-chip c-brand' },
        { t: 'One job and one button, about 120 words, no bold, no exclamation marks', s: 'Setting', cls: 'sb-chip c-neutral' },
        { t: 'No promises about how long a regulator, buyer or decision will take', s: 'Locked', cls: 'sb-chip c-brand' },
        { t: 'Prices only from the price book (board 77)', s: 'Locked', cls: 'sb-chip c-brand' }, { t: 'They or them for anyone whose pronouns we do not know', s: 'Locked', cls: 'sb-chip c-brand' },
        { t: 'Dates as "Tue 17 November"; the Hub stays in English for CIW clients', s: 'Setting', cls: 'sb-chip c-neutral' }, { t: 'Claims only from the approved proof bank', s: 'Locked', cls: 'sb-chip c-brand' }
      ]
    };
  }
}'''

def boards_js():
    return {f: [n, name] for f, (n, name, kind) in BOARDS.items()}

def gen82():
    lib = D.build_library()
    script = (S82.replace('__LIB__', js(lib)).replace('__RULES__', js(D.RULES)).replace('__GROUPS__', js(D.G))
              .replace('__BOARDS__', js(boards_js())).replace('__V2__', js(D.NOP_V2)).replace('__V3__', js(D.NOP_V3)))
    build_sa(OUT + '/Messages.dc.html', 'Messages and automations', 'Super admin', H82, B82, script, 'messages', CSS)

if __name__ == '__main__':
    gen82()
    saviewas.gen88(OUT, H88, CSS, js, boards_js())
    print('ok', H82, H88)
