# Running the business, as used by Collins (director, super admin 1).
# Builds: ManagerDash, FormBuilder, PriceBook, TeamCover, MoneyExports. (SuperAdmin is built by another generator.)
# Run from SP/gen:  python3 bizpages.py ../hub-canvas/project
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from staffboard import build, build_sa
OUT = sys.argv[1]

CSS = '''.bz-in{min-height:40px;padding:0 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;box-sizing:border-box}
.bz-ta{width:100%;min-height:60px;padding:8px 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;line-height:20px;box-sizing:border-box;resize:vertical}
.bz-in:focus-visible,.bz-ta:focus-visible,.bz-link:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:1px}
.bz-err{font-size:13px;line-height:18px;color:var(--cs-status-error-text);font-weight:500}
.bz-box{padding:12px 14px;border-radius:10px;background:var(--cs-surface-subtle);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-red{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-error-border);background:var(--cs-status-error-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-amb{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-warning-border);background:var(--cs-status-warning-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-ok{padding:12px 14px;border-radius:10px;border:1px solid var(--cs-status-success-border);background:var(--cs-status-success-bg);display:flex;flex-direction:column;gap:6px;font-size:14px;line-height:20px}
.bz-lbl{font-size:12px;line-height:16px;color:var(--cs-text-muted);font-weight:500}
.bz-b{font-weight:500}
.bz-link{display:inline-flex;align-items:center;gap:8px;text-decoration:none;box-sizing:border-box}
.bz-pill{display:inline-flex;align-items:center;justify-content:center;min-width:22px;height:22px;padding:0 6px;border-radius:999px;background:var(--cs-status-warning-bg);color:var(--cs-status-warning-text);font-size:12px;font-weight:600}
.bz-big{font-size:24px;line-height:32px;font-weight:600}
.bz-cols{display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start}
.bz-bar{display:grid;grid-template-columns:170px minmax(0,1fr) 84px;gap:10px;align-items:center;font-size:13px;line-height:18px}
.bz-bar2{display:grid;grid-template-columns:96px minmax(0,1fr) 84px;gap:10px;align-items:center;font-size:13px;line-height:18px}
.bz-gh{padding:10px 20px 4px;font-size:12px;line-height:16px;color:var(--cs-text-muted);font-weight:600;letter-spacing:0;border-top:1px solid var(--cs-border-subtle)}
.bar.red span{background:var(--cs-status-error-text)}
.bar.amb span{background:var(--cs-status-warning-text)}
'''

TABS = '''<div role="tablist" aria-label="__LABEL__" style="display: flex; gap: 6px; flex-wrap: wrap;">
          <sc-for list="{{__LIST__}}" as="tb" hint-placeholder-count="4">
            <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
            <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
          </sc-for>
        </div>'''
def tabs(lst, label):
    return TABS.replace('__LIST__', lst).replace('__LABEL__', label)

H = {}

# ---------------------------------------------------------------- 1. Manager dashboard
B_MD = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Monday 2 November</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Good morning, Collins. 52 active clients. Money, the team, refusal risk and tenders, all in one place.</span>
        </div>
        <a class="sb-btn b-pri bz-link" href="SuperAdmin.dc.html">Super admin decisions <span class="bz-pill">7</span><span class="sr-only"> waiting on super admin Home</span></a>
      </div>

      <div class="bz-cols">
        <div style="flex: 3 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
        <section class="sb-card" style="padding-bottom: 6px;" aria-labelledby="nd-h">
          <div class="sb-head"><h2 id="nd-h" class="sb-h2">Needs you today</h2><span class="sb-sub">{{todoLeft}}</span></div>
          <sc-for list="{{todo}}" as="t" hint-placeholder-count="5">
            <div class="sb-row" style="align-items: flex-start;">
              <span class="{{t.cls}}" style="width: 92px; justify-content: center; flex-shrink: 0;">{{t.kind}}</span>
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{t.title}}</span><span class="sb-sub">{{t.why}}</span></span>
              <sc-if value="{{t.open}}" hint-placeholder-val="{{ true }}"><button class="sb-btn b-sec" onClick="{{t.act}}">{{t.cta}}</button></sc-if>
              <sc-if value="{{t.done}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-ok">{{t.doneText}}</span></sc-if>
            </div>
          </sc-for>
        </section>
          <section class="sb-card" style="padding: 0 20px 18px;" aria-labelledby="wg-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="wg-h" class="sb-h2">Watch gaps</h2><span class="sb-sub">Red after 7 days</span></div>
            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div class="bz-red">
                <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">Riverside Homecare: CQC email login missing</span><span class="sb-chip c-bad">10 days</span></div>
                <span class="sb-sub">Submitted to CQC on Fri 23 Oct. Without the login the Hub cannot watch for CQC emails. Olu's client, Daniel covering. Ask Mark Evans for it on your call today.</span>
              </div>
              <div class="bz-amb">
                <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">Greenway Support: gone quiet</span><span class="sb-chip c-warn">10 days</span></div>
                <span class="sb-sub">Likely reason: the Friday 30 Oct weekly update bounced at 17:02, so Tunde Bello may not know 3 documents are waiting. Fix the email address first, then Daniel calls.</span>
              </div>
            </div>
          </section>
        </div>
        <div style="flex: 2 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
          <section class="sb-card" aria-labelledby="ap-h">
            <div class="sb-head"><h2 id="ap-h" class="sb-h2">{{mgrLeft}}</h2><span class="sb-sub">Yours as a manager. Directors count as managers</span></div>
            <sc-for list="{{mgr}}" as="a" hint-placeholder-count="2">
              <div class="sb-row" style="align-items: flex-start;"><span class="{{a.cls}}" style="flex-shrink: 0;">{{a.state}}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{a.title}}</span><span class="sb-sub">{{a.text}}</span></span><a class="sb-btn b-gh bz-link" href="{{a.href}}">{{a.cta}}</a></div>
            </sc-for>
            <div class="bz-gh" style="display: flex; justify-content: space-between; align-items: center; gap: 8px;"><span>Super admin decisions: 7</span><a class="bz-link" href="SuperAdmin.dc.html" style="font-size: 13px; color: var(--cs-text-brand); font-weight: 500; min-height: 36px;">Open super admin Home</a></div>
            <sc-for list="{{approvals}}" as="a" hint-placeholder-count="7">
              <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-chip c-warn" style="flex: 0 0 96px; justify-content: center;">{{a.kind}}</span><span style="flex: 1; min-width: 0;" class="sb-sub">{{a.text}}</span></div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">These need Collins or Rachel Turner, and never the person who asked. They are decided on super admin Home, not here.</span></div>
          </section>
        </div>
      </div>

      <section class="sb-card" aria-labelledby="mn-h">
        <div class="sb-head"><h2 id="mn-h" class="sb-h2">Money</h2><span style="display: flex; gap: 8px; align-items: center;"><span class="sb-chip c-ok">Xero: synced 09:00</span><span class="sb-sub">Syncs every hour. Amounts exclude VAT. </span><a class="bz-link" href="MoneyExports.dc.html" style="font-size: 13px; color: var(--cs-text-brand); font-weight: 500; min-height: 36px;">Open Money and exports</a></span></div>
        <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border-top: 1px solid var(--cs-border-subtle);">
          <sc-for list="{{money}}" as="m" hint-placeholder-count="4">
            <div class="sb-kpi"><span class="sb-muted">{{m.k}}</span><span class="sb-kv">{{m.v}}</span><span class="sb-sub">{{m.note}}</span></div>
          </sc-for>
        </div>
        <div style="display: flex; flex-wrap: wrap; border-top: 1px solid var(--cs-border-subtle);">
          <div style="flex: 1 1 300px; min-width: 0; padding: 16px 20px; display: flex; flex-direction: column; gap: 10px;">
            <span class="bz-lbl">Overdue by age</span>
            <sc-for list="{{aged}}" as="g" hint-placeholder-count="3">
              <div class="bz-bar2"><span>{{g.k}}</span><span class="{{g.barCls}}" aria-hidden="true"><span class="{{g.w}}"></span></span><span style="text-align: right; font-weight: 500;">{{g.v}}</span></div>
              <span class="sb-muted">{{g.who}}</span>
            </sc-for>
          </div>
          <div style="flex: 1 1 300px; min-width: 0; padding: 16px 20px; display: flex; flex-direction: column; gap: 10px; border-left: 1px solid var(--cs-border-subtle);">
            <span class="bz-lbl">Instalments due in the next 90 days</span>
            <sc-for list="{{inst}}" as="g" hint-placeholder-count="3">
              <div class="bz-bar2"><span>{{g.k}}</span><span class="bar" aria-hidden="true"><span class="{{g.w}}"></span></span><span style="text-align: right; font-weight: 500;">{{g.v}}</span></div>
            </sc-for>
            <span class="sb-muted">14 instalments, £31,916.67 in all, paid through Stripe. Reminders go a week before each one.</span>
          </div>
          <div style="flex: 1.3 1 360px; min-width: 0; padding: 16px 20px; display: flex; flex-direction: column; gap: 8px; border-left: 1px solid var(--cs-border-subtle);">
            <span class="bz-lbl">Revenue by package, this year so far</span>
            <sc-for list="{{rev}}" as="g" hint-placeholder-count="7">
              <div class="bz-bar"><span>{{g.k}}</span><span class="bar" aria-hidden="true"><span class="{{g.w}}"></span></span><span style="text-align: right; font-weight: 500;">{{g.v}}</span></div>
            </sc-for>
            <div class="bz-bar" style="border-top: 1px solid var(--cs-border-subtle); padding-top: 8px;"><span class="bz-b">Total</span><span></span><span style="text-align: right; font-weight: 600;">£220,850</span></div>
          </div>
        </div>
      </section>

      <section class="sb-card" aria-labelledby="tw-h">
        <div class="sb-head"><h2 id="tw-h" class="sb-h2">Team workload this week</h2><a class="bz-link" href="TeamCover.dc.html" style="font-size: 13px; color: var(--cs-text-brand); font-weight: 500; min-height: 36px;">Open Team and cover</a></div>
        <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 0 0 150px;">Person</span><span class="sb-th" style="flex: 1 1 170px;">Clients as case owner</span><span class="sb-th" style="flex: 0 0 130px;">Weekly updates</span><span class="sb-th" style="flex: 0 0 110px;">Overdue tasks</span><span class="sb-th" style="flex: 0 0 150px;">Legal deadlines, next 14 days</span><span class="sb-th" style="flex: 1 1 220px;">Leave and cover</span></div>
        <sc-for list="{{team}}" as="p" hint-placeholder-count="7">
          <div class="sb-row" style="align-items: flex-start;">
            <span style="flex: 0 0 150px; display: flex; flex-direction: column;"><span class="bz-b">{{p.name}}</span><span class="sb-muted">{{p.role}}</span></span>
            <span style="flex: 1 1 170px; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span>{{p.clients}}</span><sc-if value="{{p.hasGap}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-bad" style="white-space: normal; align-self: flex-start;">{{p.gap}}</span></sc-if></span>
            <span style="flex: 0 0 130px;"><span class="{{p.updCls}}">{{p.upd}}</span></span>
            <span style="flex: 0 0 110px;"><span class="{{p.odCls}}">{{p.od}}</span></span>
            <span style="flex: 0 0 150px;" class="sb-sub">{{p.legal}}</span>
            <span style="flex: 1 1 220px; min-width: 0;"><span class="{{p.leaveCls}}" style="white-space: normal;">{{p.leave}}</span></span>
          </div>
        </sc-for>
        <div class="sb-row"><span class="sb-muted">A client with no case owner always shows red. Sam's clients need a new owner and a handover note before Friday.</span></div>
      </section>

      <div class="bz-cols">
        <section class="sb-card" style="flex: 1 1 520px; min-width: 0;" aria-labelledby="rk-h">
          <div class="sb-head"><h2 id="rk-h" class="sb-h2">Refusal risk</h2>''' + tabs('regTabs', 'Regulator') + '''</div>
          <sc-for list="{{risks}}" as="r" hint-placeholder-count="2">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px;">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center; flex-wrap: wrap;"><span style="display: flex; gap: 8px; align-items: center;"><span class="{{r.cls}}">{{r.kind}}</span><span class="bz-b">{{r.client}}</span><span class="sb-chip c-brand">{{r.reg}}</span></span><span class="{{r.daysCls}}">{{r.days}}</span></div>
              <span class="sb-sub">{{r.text}}</span>
              <div class="bar" aria-hidden="true"><span class="{{r.w}}"></span></div>
              <span class="sb-muted">{{r.barNote}}</span>
              <div style="display: flex; gap: 6px; flex-wrap: wrap;"><sc-for list="{{r.gates}}" as="g" hint-placeholder-count="3"><span class="{{g.cls}}">{{g.t}}</span></sc-for></div>
            </div>
          </sc-for>
          <sc-if value="{{noRisk}}" hint-placeholder-val="{{ false }}"><div class="sb-row"><span class="sb-sub">{{noRiskText}}</span></div></sc-if>
          <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--cs-border-subtle);">
            <sc-for list="{{split}}" as="x" hint-placeholder-count="3">
              <div class="sb-kpi"><span class="bz-b">{{x.r}}</span><span class="sb-sub">{{x.t}}</span></div>
            </sc-for>
          </div>
          <div class="sb-row"><span class="bz-big" style="white-space: nowrap;">45 hours</span><span class="sb-sub">spent on resubmissions at no charge to the client this year: Westbrook so far 14 hours, and 1 earlier client, 31 hours (registered on resubmission in July). A resubmission is always at no charge to the client.</span></div>
        </section>

        <section class="sb-card" style="flex: 1 1 460px; min-width: 0;" aria-labelledby="td-h">
          <div class="sb-head"><h2 id="td-h" class="sb-h2">Tenders</h2><span class="sb-sub">2 live bids. Bids are written in Word by the bid team</span></div>
          <sc-for list="{{bids}}" as="b" hint-placeholder-count="2">
            <div class="sb-row" style="align-items: flex-start;">
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{b.name}}</span><span class="sb-sub">{{b.detail}}</span></span>
              <span class="{{b.cls}}">{{b.due}}</span>
            </div>
          </sc-for>
          <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 10px; background: var(--cs-surface-subtle);">
            <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">Accept the bid work: Maple Court Care</span><span class="{{bidChipCls}}">{{bidChip}}</span></div>
            <span>Maple Court Care has decided to bid for the Northshire home care framework, <span class="bz-b">Lot 2 South</span>. Bid deadline Tue 1 Dec 12:00. Care Sync would submit Fri 27 Nov.</span>
            <span class="sb-sub">The client decides whether to bid; Care Sync decides whether to accept the work. Found on the Radar by Jo Martin. Maple Court is an existing client, so Daniel (case owner) spoke to them first; sales has not contacted them. Same tender check: Oakleaf Living bids Lot 1 North only, so the lots do not clash. Capacity check: the bid team has room after Oakleaf's draft goes to Kemi on Tue 17 Nov.</span>
            <sc-if value="{{bidOpen}}" hint-placeholder-val="{{ true }}">
              <label class="bz-lbl" for="bid-r">Your reason (goes to the audit log, Daniel and Jo Martin)</label>
              <textarea id="bid-r" class="bz-ta" value="{{bidReason}}" onChange="{{onBidReason}}" placeholder="For example: good fit for Lot 2, the bid team has room after Tue 17 Nov"></textarea>
              <sc-if value="{{bidErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Write a reason first. Every bid decision keeps its reason.</span></sc-if>
              <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{bidYes}}">Accept the bid work</button><button class="sb-btn b-gh" onClick="{{bidNo}}">Do not accept</button></div>
            </sc-if>
            <sc-if value="{{bidDone}}" hint-placeholder-val="{{ false }}">
              <div class="{{bidBoxCls}}"><span class="bz-b">{{bidResult}}</span><span class="sb-sub">{{bidResultNote}}</span><button class="sb-btn b-gh" style="align-self: flex-start;" onClick="{{bidUndo}}">Change my decision</button></div>
            </sc-if>
          </div>
        </section>
      </div>

      <div class="bz-cols">
        <section class="sb-card" style="flex: 3 1 560px; min-width: 0; padding-bottom: 10px;" aria-labelledby="st-h">
          <div class="sb-head"><h2 id="st-h" class="sb-h2">Active clients by stage</h2><span class="sb-sub">48 registration clients in the 11 stages, plus 4 tender only clients: 52</span></div>
          <sc-for list="{{stageGroups}}" as="sg" hint-placeholder-count="5">
            <div class="bz-gh">{{sg.label}}</div>
            <div style="padding: 4px 20px 8px; display: flex; flex-direction: column; gap: 6px;">
              <sc-for list="{{sg.rows}}" as="s" hint-placeholder-count="3">
                <div class="bz-bar" title="{{s.title}}"><span>{{s.k}}</span><span class="bar" aria-hidden="true"><span class="{{s.w}}"></span></span><span style="text-align: right; font-weight: 500;">{{s.v}}</span></div>
                <sc-if value="{{s.hasNote}}" hint-placeholder-val="{{ false }}"><span class="sb-muted" style="padding-left: 180px;">{{s.note}}</span></sc-if>
              </sc-for>
            </div>
          </sc-for>
        </section>
        <section class="sb-card" style="flex: 2 1 340px; min-width: 0; padding-bottom: 8px;" aria-labelledby="fl-h">
          <div class="sb-head"><h2 id="fl-h" class="sb-h2">How clients feel</h2><span class="sb-sub">From calls, sessions and check-ins</span></div>
          <sc-for list="{{feel}}" as="f" hint-placeholder-count="3">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 6px;"><div style="display: flex; justify-content: space-between;"><span class="bz-b">{{f.k}}</span><span>{{f.v}}</span></div><div class="bar" aria-hidden="true"><span class="{{f.bar}}"></span></div></div>
          </sc-for>
          <div class="sb-row"><span class="sb-sub">The 1 worried client is Riverside Homecare. A worried client gets a call from a manager within 1 working day (a director if the manager is involved). No sales or growth messages until it is resolved. The review invitation at registration is never held back.</span></div>
        </section>
      </div>
'''

S_MD = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { done: {}, reg: 'all', bid: '', bidReason: '', bidErr: false }; }
  renderVals() {
    const s = this.state;
    const T = [
      ['call', 'Worried', 'bad', 'A worried client: Riverside Homecare', 'Mark Evans felt rushed on Friday\'s call. You are calling him today. No sales or growth messages until it is resolved; the review invitation is never held back. Ask for the CQC email login too.', 'Log the call', 'Call logged, 1 follow-up set'],
      ['sam', 'Leaver', 'bad', 'Sam Patel leaves on Friday: 4 clients have no new owner yet', '2 of 6 handed over with a note: Kingsway and Cedar Lodge go to Olu from Mon 9 Nov once a super admin approves the permission change. Rosehill Homecare, Thornbury Living, Hollybush Care and Bramley Support still need an owner.', 'Remind me Thursday', 'Reminder set for Thu 5 Nov'],
      ['nop', 'Review', 'warn', 'Your senior review: Sunrise Homecare reply to the Notice of Proposal', 'Daniel has drafted the written representations. Your review is Mon 9 Nov, our target to send is Tue 10 Nov, the legal deadline is Tue 17 Nov.', 'Add to my calendar', 'On your calendar, Mon 9 Nov'],
      ['wb', 'Assign', 'warn', 'Name a senior reviewer: Westbrook Care resubmission pack', 'CQC refused on Mon 26 Oct and the client chose to resubmit. The senior review on Thu 12 Nov needs a name.', 'Assign to me', 'Assigned to you, Thu 12 Nov'],
      ['ho', 'Handover', 'warn', 'Approve the handover: Binnian Care Ltd (RQIA)', 'All 8 onboarding gates passed Fri 30 Oct. Grace asked you to approve. Proposed case owner: Olu, back Mon 9 Nov. No application work starts before you approve.', 'Mark as approved', 'Approved by you, just now'],
      ['bid', 'Tender', 'info', 'Accept the bid work: Maple Court Care, Northshire Lot 2 South', 'Maple Court decided to bid. Waiting on you to accept the work. See Tenders below.', 'Go to the decision', 'Decision made']
    ];
    const bidDecided = !!s.bid;
    const todo = T.map(([id, kind, k, title, why, cta, doneText]) => {
      const done = id === 'bid' ? bidDecided : !!s.done[id];
      return { kind, cls: 'sb-chip c-' + k, title, why, cta, doneText, open: !done, done,
        act: () => { if (id === 'bid') { const el = document.getElementById('bid-r'); if (el) { el.scrollIntoView({ block: 'center' }); el.focus(); } return; } this.setState({ done: Object.assign({}, s.done, { [id]: true }) }); } };
    });
    const left = todo.filter(t => t.open).length;
    const approvals = [
      ['Price', 'Full start-up package £8,500 + VAT, entered by Collins 2 Nov. Waiting for Rachel Turner'],
      ['Discount', 'Lindenfield Care Ltd: £3,800 + VAT instead of £4,000 + VAT. Asked by Jo Martin'],
      ['Discount', 'Ashby Care: PIR writing for 2 service types, £1,350 + VAT instead of £1,500 + VAT. Asked by Daniel'],
      ['Form', 'CQC onboarding form v8, drafted by Grace Thu 29 Oct. 3 clients on v7 have not finished'],
      ['Permission', 'Olu takes Kingsway and Cedar Lodge from Sam Patel, from Mon 9 Nov. Asked by Grace, Fri 30 Oct 16:10'],
      ['Email', '5.2 Notice of Proposal v3, drafted by Daniel'],
      ['Retention', 'Schedule v2: identity and DBS images deleted once the regulator decides. Proposed by Collins as data protection lead. Waiting for Rachel Turner']
    ].map(([kind, text]) => ({ kind, text }));
    const mgrDone = { ho: !!s.done.ho, bid: !!s.bid };
    const mgr = [
      ['ho', 'Handover: Binnian Care Ltd', 'RQIA. All 8 gates passed. Grace asked you on Fri 30 Oct', 'Handover.dc.html', 'Open'],
      ['bid', 'Accept the bid work: Maple Court Care', 'Northshire Lot 2 South. The client has decided to bid', '#bid-r', 'Go to it']
    ].map(([id, title, text, href, cta]) => ({ title, text, href, cta, state: mgrDone[id] ? 'Decided' : 'Waiting', cls: 'sb-chip ' + (mgrDone[id] ? 'c-ok' : 'c-warn') }));
    const mgrLeft = mgr.filter(m => m.state === 'Waiting').length;
    const money = [
      ['Invoiced this month', '£9,600', '5 invoices on 1 and 2 Nov'],
      ['Collected this month', '£4,150', '3 payments through Stripe. Payments after 09:00 show at 10:00'],
      ['Overdue', '£5,300', '4 invoices. Reminders running'],
      ['Instalments due, next 90 days', '£31,916.67', '14 instalments to 31 Jan']
    ].map(([k, v, note]) => ({ k, v, note }));
    const aged = [
      ['0 to 30 days', '£3,050', 'w60', 'amb', '2 invoices. Reminder 2 sent'],
      ['31 to 60 days', '£1,500', 'w30', 'amb', '1 invoice. Case owner has called'],
      ['Over 60 days', '£750', 'w15', 'red', '1 invoice. Needs your decision: payment plan or pause work']
    ].map(([k, v, w, c, who]) => ({ k, v, w, barCls: 'bar ' + c, who }));
    const inst = [['November', '£11,583.33', 'w100'], ['December', '£10,666.67', 'w90'], ['January', '£9,666.67', 'w85']].map(([k, v, w]) => ({ k, v, w }));
    const rev = [
      ['CQC domiciliary care', '£72,000', 'w100'], ['Full start-up', '£51,000', 'w70'], ['CQC supported living', '£35,000', 'w50'],
      ['Tender writing', '£21,600', 'w30'], ['CIW registration', '£18,000', 'w25'], ['RQIA registration', '£13,500', 'w20'], ['Add-ons and single services', '£9,750', 'w15']
    ].map(([k, v, w]) => ({ k, v, w }));
    const team = [
      ['Rachel Turner', 'Operations manager, super admin 2', 'None as owner. Reviews the decisions on the Sam Patel export (Collins leads it as data protection lead). The window for an ICO report, if one is needed, ends Thu 5 Nov 06:00', '', 'None', 'neutral', 'None', 'ok', 'None', 'In all week', 'ok'],
      ['Daniel Mensah', 'Consultant', '6 active and 2 in aftercare, plus 4 covering for Olu', '', '10 due Fri 6 Nov', 'warn', '1 overdue', 'bad', 'None. Next: Sunrise, 17 Nov (day 15)', 'Covering Olu: Riverside, Greenway, Lagan View, Willow Bank, with vault reveal. Approved by Rachel Turner Fri 30 Oct', 'info'],
      ['Olu', 'Consultant', '5: 4 covered by Daniel, and Brookside (aftercare) waits for Olu', '', '4 moved to Daniel', 'neutral', '1 in outbox', 'warn', 'None', 'On leave Mon 2 to Fri 6 Nov. Back Mon 9 Nov', 'warn'],
      ['Sam Patel', 'Consultant', '6, being reassigned', 'No owner after Friday: Rosehill, Thornbury, Hollybush, Bramley', '6 due Fri 6 Nov', 'neutral', '2', 'bad', 'None', 'Leaving Fri 6 Nov. Downloads paused while the export is checked', 'bad'],
      ['Grace', 'Onboarding lead', '6 in onboarding, until each handover', '', 'None', 'neutral', 'None', 'ok', 'None', 'In all week', 'ok'],
      ['Divine', 'Client care', 'None as owner. 3 calls today', '', 'None', 'neutral', 'None', 'ok', 'None', 'In all week', 'ok'],
      ['Millicent', 'Coach', 'None as owner. 7 sessions this week', '', 'None', 'neutral', 'None', 'ok', 'None', 'In all week', 'ok'],
      ['Jo Martin', 'Sales', 'None as owner. 12 Radar matches today', '', 'None', 'neutral', 'None', 'ok', 'None', 'In all week', 'ok'],
      ['Femi Ade', 'Finance, part time', 'None as owner. Closing October; 4 overdue invoices, 1 refund for a manager', '', 'None', 'neutral', 'None', 'ok', 'None', 'Works Mon, Wed and Thu', 'ok']
    ].map(([name, role, clients, gap, upd, uc, od, oc, legal, leave, lc]) => ({ name, role, clients, gap, hasGap: !!gap, upd, updCls: 'sb-chip c-' + uc, od, odCls: 'sb-chip c-' + oc, legal, leave, leaveCls: 'sb-chip c-' + lc }));
    const R = [
      { reg: 'CQC', kind: 'Notice of Proposal', cls: 'sb-chip c-bad', client: 'Sunrise Homecare Ltd', days: '15 days to the legal deadline', daysCls: 'sb-chip c-warn',
        text: 'Served (received) Wed 21 Oct. Written representations by Tue 17 Nov (28 days). Our target to send: Tue 10 Nov, 8 days. Reply drafted by Daniel; your senior review Mon 9 Nov.',
        w: 'w45', barNote: '13 of 28 days used', gates: [['Reply drafted', 'ok'], ['Senior review Mon 9 Nov', 'warn'], ['Sent by Tue 10 Nov', 'neutral']] },
      { reg: 'CQC', kind: 'Refused, we resubmit', cls: 'sb-chip c-warn', client: 'Westbrook Care Ltd', days: 'Appeal window closes Sun 22 Nov', daysCls: 'sb-chip c-info',
        text: 'Notice of decision received Mon 26 Oct. Appeal window worked out the safe way (confirm with a legal adviser). Client chose to resubmit (recorded 28 Oct), so no appeal. Senior review of the new pack Thu 12 Nov. Resubmit target Mon 30 Nov. At no charge to the client.',
        w: 'w50', barNote: 'Steps: 3 of 6 done. Gate before sending: 1 of 7 ticked', gates: [['Reasons mapped', 'ok'], ['Client choice recorded', 'ok'], ['Fix plan agreed', 'ok'], ['New pack drafted', 'warn'], ['Senior review Thu 12 Nov', 'neutral'], ['Resubmit Mon 30 Nov', 'neutral']] }
    ];
    const risks = R.filter(r => s.reg === 'all' || r.reg === s.reg).map(r => Object.assign({}, r, { gates: r.gates.map(([t, k]) => ({ t, cls: 'sb-chip c-' + k })) }));
    const bids = [
      ['Northshire County Council home care framework 2027, Lot 1 North', 'Oakleaf Living. Clarification questions close Fri 13 Nov 17:00. Next: case study from Kemi, Wed 11 Nov. Draft to Kemi Tue 17 Nov, Kemi approves Tue 24 Nov, we submit Fri 27 Nov.', 'Bid deadline Tue 1 Dec', 'warn'],
      ['Eastford Borough Council supported living (dynamic purchasing system)', 'Oakleaf Living. Deciding scope, profile check under way.', 'Deadline Fri 4 Dec', 'info']
    ].map(([name, detail, due, k]) => ({ name, detail, due, cls: 'sb-chip c-' + k }));
    const decide = v => { if (!s.bidReason.trim()) { this.setState({ bidErr: true }); return; } this.setState({ bid: v, bidErr: false }); };
    const reason = s.bidReason.trim();
    const G = [
      ['Onboarding', [['1 Welcome', 6, 'w60', 'Includes the onboarding form and gates. Harbour Lane: 5 of 8 gates passed']]],
      ['Building the application (no work starts before handover)', [['2 CV review', 2, 'w20'], ['3 Your documents', 7, 'w70'], ['4 Drafting', 6, 'w60'], ['5 Your review', 3, 'w30'], ['6 Final pack sign-off', 2, 'w20']]],
      ['With the regulator', [['7 Submitted', 1, 'w10'], ['8 With the regulator', 7, 'w70', '5 CQC, 1 CIW, 1 RQIA'], ['9 Interview', 2, 'w20']]],
      ['Outcome (stage 10)', [['10 Notice of Proposal', 1, 'w10', 'Sunrise Homecare'], ['10 Refused, we resubmit', 1, 'w10', 'Westbrook Care'], ['10 Registered this week', 0, 'w0']]],
      ['After registration', [['11 Aftercare', 10, 'w100']]],
      ['Not in the 11 stages', [['Tender only clients', 4, 'w40', 'Oakleaf Living and 3 others']]]
    ];
    const stageGroups = G.map(([label, rows]) => ({ label, rows: rows.map(([k, v, w, note]) => ({ k, v: String(v), w, note: note || '', hasNote: !!note, title: k + ': ' + v + ' clients' })) }));
    return {
      theme: this.props.theme ?? 'light', three: 3, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      todo, todoLeft: left === 0 ? 'All done for now' : left + ' to do',
      approvals, mgr, mgrLeft: 'Manager decisions: ' + mgrLeft, money, aged, inst, rev, team,
      regTabs: [['all', 'All'], ['CQC', 'CQC'], ['CIW', 'CIW'], ['RQIA', 'RQIA']].map(([k, label]) => ({ label, on: s.reg === k, off: s.reg !== k, pick: () => this.setState({ reg: k }) })),
      risks, noRisk: risks.length === 0, noRiskText: 'No Notices of Proposal or refusals open with ' + s.reg + '.',
      split: [['CQC', '1 Notice of Proposal, 1 refusal'], ['CIW', 'None open'], ['RQIA', 'None open']].map(([r, t]) => ({ r, t })),
      bids, bidOpen: !bidDecided, bidDone: bidDecided, bidErr: s.bidErr, bidReason: s.bidReason,
      onBidReason: e => this.setState({ bidReason: e.target.value, bidErr: false }),
      bidYes: () => decide('yes'), bidNo: () => decide('no'), bidUndo: () => this.setState({ bid: '' }),
      bidChip: !bidDecided ? 'Waiting on you' : (s.bid === 'yes' ? 'Accepted' : 'Not accepted'),
      bidChipCls: 'sb-chip ' + (!bidDecided ? 'c-warn' : (s.bid === 'yes' ? 'c-ok' : 'c-neutral')),
      bidBoxCls: s.bid === 'yes' ? 'bz-ok' : 'bz-box',
      bidResult: s.bid === 'yes' ? 'Bid work accepted by Collins, just now. Daniel tells Maple Court today and the bid team plans Lot 2 South.' : 'Not accepted by Collins, just now. Daniel explains to Maple Court today and offers a bid review instead.',
      bidResultNote: 'Reason: "' + reason + '". Written to the audit log. Daniel and Jo Martin are told.',
      stageGroups,
      feel: [['Happy', '46', 'w90'], ['Unsure', '5', 'w10'], ['Worried', '1', 'w5']].map(([k, v, bar]) => ({ k, v, bar }))
    };
  }
}'''
H['md'] = 3920
build(OUT + '/ManagerDash.dc.html', 'Manager dashboard', 'Manager dashboard', H['md'], B_MD, S_MD, 'manager', CSS + '.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}\n')

# ---------------------------------------------------------------- 2. Super admin
B_SA = '''      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Super admin</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Good morning, Collins. {{pendingText}}. 11 of 12 connections healthy, 1 needs attention. Sensitive changes always need a second super admin.</span>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <button class="sb-btn b-gh" onClick="{{toggleSum}}">{{sumLabel}}</button>
          <a class="sb-btn b-pri bz-link" href="TeamCover.dc.html">Invite a person</a>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="4">
          <div class="sb-card sb-kpi"><span class="sb-muted">{{k.k}}</span><span class="sb-kv">{{k.v}}</span><span class="{{k.cls}}" style="align-self: flex-start;">{{k.note}}</span></div>
        </sc-for>
      </div>

      <div class="{{unCls}}" role="status" style="flex-direction: row; align-items: center; gap: 14px; flex-wrap: wrap;">
        <span class="{{unChipCls}}">{{unChip}}</span>
        <span style="flex: 1 1 420px; min-width: 0;">{{unText}}</span>
        <sc-if value="{{unOpen}}" hint-placeholder-val="{{ true }}"><span style="display: flex; gap: 8px;"><button class="sb-btn b-sec" onClick="{{unLook}}">Look into it</button><button class="sb-btn b-gh" onClick="{{unFine}}">Mark as expected</button></span></sc-if>
      </div>

      <sc-if value="{{showSum}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card" aria-labelledby="ws-h">
          <div class="sb-head"><h2 id="ws-h" class="sb-h2">Weekly super admin summary: Mon 26 Oct to Sun 1 Nov</h2><span class="sb-sub">Sent to both super admins every Monday at 07:00</span></div>
          <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));">
            <sc-for list="{{summary}}" as="w" hint-placeholder-count="8">
              <div class="sb-row" style="align-items: flex-start;"><span class="{{w.cls}}" style="width: 96px; justify-content: center; flex-shrink: 0;">{{w.k}}</span><span class="sb-sub" style="flex: 1; min-width: 0;">{{w.t}}</span></div>
            </sc-for>
          </div>
        </section>
      </sc-if>

      <div class="bz-cols">
        <section class="sb-card" style="flex: 3 1 600px; min-width: 0;" aria-labelledby="ap-h">
          <div class="sb-head"><h2 id="ap-h" class="sb-h2">Needs your approval: {{pendingVal}}</h2><span class="sb-sub">Write a reason, then approve or decline. Try it</span></div>
          <sc-for list="{{approvals}}" as="a" hint-placeholder-count="3">
            <div style="padding: 16px 20px; border-top: 1px solid var(--cs-border-subtle); display: flex; flex-direction: column; gap: 10px;">
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <span aria-hidden="true" style="width: 36px; height: 36px; flex-shrink: 0; border-radius: 10px; background: var(--cs-surface-subtle); display: flex; align-items: center; justify-content: center;"><x-import component-from-global-scope="CareSync.Icon" name="{{a.icon}}" size="{{n20}}"></x-import></span>
                <div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;">
                  <span style="font-size: 15px; line-height: 22px; font-weight: 500;">{{a.title}}</span>
                  <span class="sb-sub">{{a.detail}}</span>
                  <span class="sb-muted">{{a.meta}}</span>
                </div>
                <span class="{{a.chipCls}}">{{a.chip}}</span>
              </div>
              <sc-if value="{{a.isBg}}" hint-placeholder-val="{{ false }}">
                <div class="bz-box"><span class="bz-lbl">Why break-glass is needed</span><span>Olu is the case owner and holds this entry. Daniel's cover access this week lets him see Olu's clients but not reveal their logins. Access ends automatically after 4 hours, every reveal is logged, and Greenway sees it on their privacy page.</span></div>
              </sc-if>
              <sc-if value="{{a.isPerm}}" hint-placeholder-val="{{ false }}">
                <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px;">
                  <div class="bz-box"><span class="bz-lbl">Before</span><sc-for list="{{permBefore}}" as="x" hint-placeholder-count="3"><span>{{x}}</span></sc-for></div>
                  <div class="bz-ok"><span class="bz-lbl">After, from Mon 9 Nov</span><sc-for list="{{permAfter}}" as="x" hint-placeholder-count="3"><span>{{x}}</span></sc-for></div>
                </div>
              </sc-if>
              <sc-if value="{{a.isDel}}" hint-placeholder-val="{{ false }}">
                <div class="bz-box" style="gap: 0; padding: 0; overflow: hidden;">
                  <div style="display: grid; grid-template-columns: 1.3fr 1.3fr 1fr; gap: 10px; padding: 8px 14px;"><span class="bz-lbl">Document</span><span class="bz-lbl">Closed client</span><span class="bz-lbl">Retention ended</span></div>
                  <sc-for list="{{delDocs}}" as="d" hint-placeholder-count="14">
                    <div style="display: grid; grid-template-columns: 1.3fr 1.3fr 1fr; gap: 10px; padding: 5px 14px; border-top: 1px solid var(--cs-border-subtle); font-size: 13px; line-height: 18px;"><span>{{d.t}}</span><span>{{d.c}}</span><span>{{d.e}}</span></div>
                  </sc-for>
                </div>
                <div class="bz-ok"><span class="bz-b">Legal hold check: clear</span><span class="sb-sub">None of the 3 clients has a legal hold, an open complaint, a regulator query or a payment dispute. Checked by the Hub today at 06:00. A record of the decision is kept, never the documents.</span></div>
              </sc-if>
              <sc-if value="{{a.open}}" hint-placeholder-val="{{ true }}">
                <label class="bz-lbl" for="{{a.taId}}">Your reason (written to the audit log)</label>
                <textarea id="{{a.taId}}" class="bz-ta" value="{{a.reason}}" onChange="{{a.onReason}}" placeholder="{{a.ph}}"></textarea>
                <sc-if value="{{a.err}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Write a reason before you approve or decline.</span></sc-if>
                <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{a.approve}}">{{a.approveLabel}}</button><button class="sb-btn b-gh" onClick="{{a.decline}}">Decline</button></div>
              </sc-if>
              <sc-if value="{{a.done}}" hint-placeholder-val="{{ false }}">
                <div class="{{a.doneBox}}"><span class="bz-b">{{a.doneText}}</span><span class="sb-sub">{{a.doneNote}}</span></div>
              </sc-if>
            </div>
          </sc-for>
          <div style="padding: 12px 20px 16px; border-top: 1px solid var(--cs-border-subtle);" class="sb-muted">Nobody can approve their own request. Every decision is written to the audit log with the reason.</div>
        </section>

        <div style="flex: 2 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 18px;">
          <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="au-h">
            <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="au-h" class="sb-h2">Automations</h2><span class="sb-sub">46 rules on</span></div>
            <div class="bz-red" style="gap: 8px;">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center;"><span class="bz-b">Weekly update to Greenway Support</span><span class="sb-chip c-bad">Failed</span></div>
              <span class="sb-sub">The Friday 30 Oct update bounced at 17:02: the mailbox does not exist. It is waiting in Olu's outbox. Olu is on leave, so Daniel is covering and has been told.</span>
              <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-sec" onClick="{{toggleFix}}">Fix email address</button><button class="sb-btn b-gh" onClick="{{toggleLog}}">See run log</button></div>
              <sc-if value="{{showFix}}" hint-placeholder-val="{{ false }}">
                <label class="bz-lbl" for="fx-in">Tunde Bello's email address</label>
                <input id="fx-in" class="bz-in" value="{{fixVal}}" onChange="{{onFix}}">
                <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{saveFix}}">Save and resend</button><span class="sb-muted">{{fixNote}}</span></div>
              </sc-if>
              <sc-if value="{{showLog}}" hint-placeholder-val="{{ false }}">
                <div style="display: flex; flex-direction: column; gap: 4px; padding-top: 4px; border-top: 1px solid var(--cs-status-error-border);">
                  <sc-for list="{{runLog}}" as="l" hint-placeholder-count="5"><span style="font-size: 13px; line-height: 18px;"><span class="bz-b">{{l.t}}</span> {{l.x}}</span></sc-for>
                </div>
              </sc-if>
            </div>
            <sc-for list="{{autos}}" as="u" hint-placeholder-count="4">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center; font-size: 14px; line-height: 20px;"><span>{{u.k}}</span><span class="sb-chip c-ok">{{u.v}}</span></div>
            </sc-for>
            <span class="sb-muted">Failures are always shown here and to the owner. Nothing fails silently.</span>
          </section>
          <section class="sb-card" aria-labelledby="cn-h">
            <div class="sb-head"><h2 id="cn-h" class="sb-h2">Connections: 11 of 12 healthy</h2><span class="sb-sub">1 needs attention</span></div>
            <sc-for list="{{conns}}" as="i" hint-placeholder-count="12">
              <div style="padding: 10px 20px; border-top: 1px solid var(--cs-border-subtle); display: flex; justify-content: space-between; align-items: center; gap: 10px;">
                <span style="display: flex; flex-direction: column; min-width: 0;"><span class="bz-b" style="font-size: 14px; line-height: 20px;">{{i.name}}</span><span class="sb-muted">{{i.note}}</span></span>
                <span class="{{i.cls}}">{{i.state}}</span>
              </div>
            </sc-for>
          </section>
        </div>
      </div>

      <section class="sb-card" aria-labelledby="lg-h">
        <div class="sb-head"><h2 id="lg-h" class="sb-h2">Audit log</h2><button class="sb-btn b-gh" onClick="{{doExport}}">{{exportLabel}}</button></div>
        <div style="padding: 0 20px 12px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
          <input aria-label="Search the audit log" class="bz-in" style="width: 340px;" placeholder="Search: a name, a client or an action" value="{{q}}" onChange="{{onQ}}">
          ''' + tabs('logTabs', 'Filter the audit log') + '''
        </div>
        <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 0 0 130px;">When</span><span class="sb-th" style="flex: 0 0 150px;">Who</span><span class="sb-th" style="flex: 1;">What happened</span><span class="sb-th" style="flex: 0 0 110px;">Type</span></div>
        <sc-for list="{{log}}" as="l" hint-placeholder-count="8">
          <div class="sb-row" style="align-items: flex-start;"><span class="sb-sub" style="flex: 0 0 130px;">{{l.at}}</span><span class="bz-b" style="flex: 0 0 150px;">{{l.actor}}</span><span style="flex: 1; min-width: 0;">{{l.action}}</span><span style="flex: 0 0 110px;"><span class="{{l.cls}}">{{l.type}}</span></span></div>
        </sc-for>
        <sc-if value="{{noLog}}" hint-placeholder-val="{{ false }}"><div class="sb-row"><span class="sb-sub">Nothing matches. Try another word or filter.</span></div></sc-if>
        <div class="sb-row"><span class="sb-muted">{{logCount}}</span></div>
      </section>
'''

S_SA = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { dec: {}, reasons: {}, errs: {}, un: '', showSum: true, showFix: false, showLog: false, fix: 'tunde@greenwaysupport.example', fixSaved: false, q: '', f: 'all', exported: false };
  }
  renderVals() {
    const s = this.state;
    const base = [
      { id: 'bg', icon: 'lock', isBg: true, title: 'Break-glass access: Greenway Support Ltd vault entry', detail: 'Daniel Mensah asks for the client\'s document folder login. Olu, the case owner, is on leave this week, and 3 documents are waiting in that folder.', meta: 'Requested by Daniel Mensah, today 08:12. Ends automatically after 4 hours. The client is emailed today and sees it on their privacy page.', approveLabel: 'Approve for 4 hours', ph: 'For example: Olu on leave, 3 documents waiting, 4 hours is enough', log: 'break-glass access for Daniel Mensah to Greenway Support\'s vault entry, 4 hours', type: 'Vault' },
      { id: 'perm', icon: 'shield-check', isPerm: true, title: 'Permission change: Olu takes 2 of Sam Patel\'s clients', detail: 'Sam leaves on Friday. Kingsway Care and Cedar Lodge Care move to Olu when Olu is back on Mon 9 Nov.', meta: 'Requested by Grace, Fri 30 Oct 16:10. Made in Team and cover.', approveLabel: 'Approve', ph: 'For example: Olu knows both services, handover notes are written', log: 'the permission change for Olu (2 clients from Sam Patel, from Mon 9 Nov)', type: 'People' },
      { id: 'del', icon: 'file-clock', isDel: true, title: 'Scheduled deletion: 14 identity documents', detail: 'The retention period has ended for 3 closed clients. The documents are listed below.', meta: 'Prepared by the Hub today at 06:00. Deleted 7 days after approval, so it can still be stopped.', approveLabel: 'Approve deletion', ph: 'For example: retention ended, legal hold check clear', log: 'the scheduled deletion of 14 identity documents from 3 closed clients', type: 'Data' }
    ];
    const set = (k, id, v) => this.setState({ [k]: Object.assign({}, s[k], { [id]: v }) });
    const approvals = base.map(a => {
      const v = s.dec[a.id]; const r = (s.reasons[a.id] || '');
      const go = val => { if (!r.trim()) { set('errs', a.id, true); return; } this.setState({ dec: Object.assign({}, s.dec, { [a.id]: val }), errs: Object.assign({}, s.errs, { [a.id]: false }) }); };
      return Object.assign({ isBg: false, isPerm: false, isDel: false }, a, {
        open: !v, done: !!v, reason: r, err: !!s.errs[a.id], taId: 'r-' + a.id,
        onReason: e => this.setState({ reasons: Object.assign({}, s.reasons, { [a.id]: e.target.value }), errs: Object.assign({}, s.errs, { [a.id]: false }) }),
        approve: () => go('yes'), decline: () => go('no'),
        chip: !v ? 'Waiting' : (v === 'yes' ? 'Approved' : 'Declined'), chipCls: 'sb-chip ' + (!v ? 'c-warn' : (v === 'yes' ? 'c-ok' : 'c-neutral')),
        doneBox: v === 'yes' ? 'bz-ok' : 'bz-box',
        doneText: v === 'yes' ? (a.id === 'bg' ? 'Approved by you, just now. Access ends at 12:30 today.' : (a.id === 'del' ? 'Approved by you, just now. Deletion runs on Mon 9 Nov.' : 'Approved by you, just now. Starts Mon 9 Nov.')) : 'Declined by you, just now. The requester is told.',
        doneNote: 'Reason: "' + r.trim() + '". Written to the audit log.'
      });
    });
    const pending = approvals.filter(a => a.open).length;
    const delDocs = [
      ['Passport (director)', 'Fernhill Homecare Ltd', '15 Oct 2026'], ['Driving licence (director)', 'Fernhill Homecare Ltd', '15 Oct 2026'], ['Utility bill (director)', 'Fernhill Homecare Ltd', '15 Oct 2026'], ['Passport (manager)', 'Fernhill Homecare Ltd', '15 Oct 2026'], ['Bank statement (manager)', 'Fernhill Homecare Ltd', '15 Oct 2026'],
      ['Passport (director)', 'Northgate Care Ltd', '22 Oct 2026'], ['Birth certificate (director)', 'Northgate Care Ltd', '22 Oct 2026'], ['Council tax bill (director)', 'Northgate Care Ltd', '22 Oct 2026'], ['Driving licence (manager)', 'Northgate Care Ltd', '22 Oct 2026'], ['Bank statement (manager)', 'Northgate Care Ltd', '22 Oct 2026'],
      ['Passport (director)', 'Bluebell Support Ltd', '31 Oct 2026'], ['Driving licence (director)', 'Bluebell Support Ltd', '31 Oct 2026'], ['Utility bill (manager)', 'Bluebell Support Ltd', '31 Oct 2026'], ['DBS certificate copy (manager)', 'Bluebell Support Ltd', '31 Oct 2026']
    ].map(([t, c, e]) => ({ t, c, e }));
    const conns = [
      ['Google Workspace', 'Care Sync mailboxes and calendars', 'Healthy', 'ok'], ['Xero', 'Invoices and payments. Synced 08:00, every hour', 'Healthy', 'ok'], ['Stripe', 'Every instalment, by card or another method Stripe supports', 'Healthy', 'ok'],
      ['E-signature (DocuSeal)', 'Agreements and sign-offs', 'Healthy', 'ok'], ['Companies House', 'Company and officer checks', 'Healthy', 'ok'], ['CQC email watch', 'Riverside Homecare: login not in the vault, 10 days', 'Needs attention', 'bad'],
      ['CIW Online watch', 'Afon Care. Checked 07:00', 'Healthy', 'ok'], ['RQIA Web Portal watch', 'Lagan View Care. Checked 07:00', 'Healthy', 'ok'], ['Interview Preparation Hub API', 'Creates the client\'s account when the interview stage starts, with regulator, service type and role. If it cannot, a staff task with the details to copy', 'Healthy', 'ok'],
      ['GoHighLevel', 'Sales CRM. Won deals start journeys', 'Healthy', 'ok'], ['SMS and WhatsApp', 'Reminders and nudges', 'Healthy', 'ok'], ['File storage and backup', 'Nightly backup done 02:00', 'Healthy', 'ok']
    ].map(([name, note, state, k]) => ({ name, note, state, cls: 'sb-chip c-' + k }));
    const L = [
      ['Today 08:12', 'Daniel Mensah', 'requested break-glass access to Greenway Support\'s vault entry (Olu on leave)', 'Vault'],
      ['Today 06:00', 'The Hub', 'flagged unusual activity: Sam Patel exported 38 client documents on Sun 1 Nov at 21:40', 'Unusual'],
      ['Today 06:00', 'The Hub', 'prepared the scheduled deletion of 14 identity documents; legal hold check clear', 'Data'],
      ['Sun 1 Nov 21:40', 'Sam Patel', 'exported 38 client documents (usual: under 5 a day)', 'Unusual'],
      ['Fri 30 Oct 17:30', 'Collins', 'price change: PIR writing now reads "£750 + VAT per PIR, one PIR per service type". Requested by Grace, approved by Collins. For new clients from 1 Nov', 'Prices'],
      ['Fri 30 Oct 17:02', 'The Hub', 'weekly update to Greenway Support bounced; moved to Olu\'s outbox', 'Automation'],
      ['Fri 30 Oct 16:10', 'Grace', 'requested a permission change for Olu (2 clients from Sam Patel)', 'People'],
      ['Fri 30 Oct 15:20', 'Daniel Mensah', 'revealed the Oakleaf Living website login, reason "update the services page"', 'Vault'],
      ['Thu 29 Oct 11:05', 'Grace', 'saved draft v8 of the CQC Registration Information Form (2 added, 1 removed, 3 reworded)', 'Forms'],
      ['Wed 28 Oct 09:00', 'Collins', 'set Olu\'s leave, Mon 2 to Fri 6 Nov, with Daniel Mensah covering 4 clients', 'People'],
      ['Tue 27 Oct 14:30', 'Collins', 'started offboarding for Sam Patel, last day Fri 6 Nov', 'People']
    ];
    const typeCls = { Vault: 'c-brand', Unusual: 'c-warn', Data: 'c-neutral', Prices: 'c-info', Automation: 'c-bad', People: 'c-neutral', Forms: 'c-info', Approval: 'c-ok' };
    const newLog = base.filter(a => s.dec[a.id]).map(a => ['Just now', 'Collins', (s.dec[a.id] === 'yes' ? 'approved ' : 'declined ') + a.log + '. Reason: "' + (s.reasons[a.id] || '').trim() + '"', 'Approval']);
    const extra = s.un ? [['Just now', 'Collins', s.un === 'look' ? 'opened a check on Sam Patel\'s export and paused Sam\'s downloads' : 'marked Sam Patel\'s export as expected (handover copies)', 'Unusual']] : [];
    const fixLog = s.fixSaved ? [['Just now', 'Collins', 'changed Greenway Support\'s email address to ' + s.fix + '; resend waits for Daniel to confirm it with Tunde', 'Automation']] : [];
    const all = newLog.concat(extra, fixLog, L);
    const q = s.q.trim().toLowerCase();
    const F = { all: null, ap: ['Approval'], vault: ['Vault'], prices: ['Prices'], people: ['People'], unusual: ['Unusual'] };
    const log = all.filter(l => (!F[s.f] || F[s.f].includes(l[3])) && (!q || (l[0] + ' ' + l[1] + ' ' + l[2] + ' ' + l[3]).toLowerCase().includes(q))).map(([at, actor, action, type]) => ({ at, actor, action, type, cls: 'sb-chip ' + typeCls[type] }));
    const unText = s.un === 'look' ? 'You opened a check. Sam Patel\'s downloads are paused, and Sam and Daniel are told why.' : (s.un === 'fine' ? 'Marked as expected (handover copies). The note is in the audit log.' : 'Sam Patel exported 38 client documents on Sun 1 Nov at 21:40. Usual: under 5 a day. Sam leaves on Friday.');
    return {
      theme: this.props.theme ?? 'light', n20: 20, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      three: pending, pendingVal: String(pending),
      pendingText: pending === 0 ? 'Nothing is waiting for you' : (pending === 1 ? '1 approval is waiting for you' : pending + ' approvals are waiting for you'),
      kpis: [
        ['Staff with access', '8', 'All use two-step login', 'ok'],
        ['Waiting for your approval', String(pending), pending ? 'Reason needed for each' : 'All clear', pending ? 'warn' : 'ok'],
        ['Automations failed', '1', 'Shown, never silent', 'bad'],
        ['Connections healthy', '11 of 12', '1 needs attention', 'warn']
      ].map(([k, v, note, c]) => ({ k, v, note, cls: 'sb-chip c-' + c })),
      unCls: s.un ? 'bz-box' : 'bz-amb', unChip: s.un ? 'Handled' : 'Unusual activity', unChipCls: 'sb-chip ' + (s.un ? 'c-ok' : 'c-warn'), unText, unOpen: !s.un,
      unLook: () => this.setState({ un: 'look' }), unFine: () => this.setState({ un: 'fine' }),
      showSum: s.showSum, toggleSum: () => this.setState({ showSum: !s.showSum }), sumLabel: s.showSum ? 'Hide the weekly summary' : 'Show the weekly summary',
      summary: [
        ['Approvals', '4 decided last week, all with a reason. 3 wait today.', 'c-info'],
        ['Vault', '41 logins revealed, each with a reason. No break-glass used.', 'c-brand'],
        ['Unusual', '1 alert: Sam Patel\'s export on Sunday night (see above).', 'c-warn'],
        ['Automations', '1,284 runs, 1 failure: the Greenway weekly update bounce.', 'c-bad'],
        ['Connections', '11 of 12 healthy all week. CQC email watch needs Riverside\'s login.', 'c-warn'],
        ['Prices', '1 change approved: PIR writing wording (Grace asked, Collins approved).', 'c-info'],
        ['People', 'Olu on leave this week, Daniel covering. Sam Patel leaves Fri 6 Nov.', 'c-neutral'],
        ['Data', '14 identity documents due for deletion, legal hold check clear.', 'c-neutral']
      ].map(([k, t, c]) => ({ k, t, cls: 'sb-chip ' + c })),
      approvals, permBefore: ['Case owner: 5 clients (Riverside, Greenway, Lagan View, Willow Bank, Brookside)', 'Vault: reveal logins for those 5', 'Weekly updates: 5'],
      permAfter: ['Case owner: 7 clients (adds Kingsway Care and Cedar Lodge Care)', 'Vault: reveal logins for those 7', 'Weekly updates: 7'], delDocs,
      showFix: s.showFix, showLog: s.showLog, toggleFix: () => this.setState({ showFix: !s.showFix }), toggleLog: () => this.setState({ showLog: !s.showLog }),
      fixVal: s.fix, onFix: e => this.setState({ fix: e.target.value, fixSaved: false }), saveFix: () => this.setState({ fixSaved: true }),
      fixNote: s.fixSaved ? 'Saved. The resend waits until Daniel confirms the address with Tunde by phone.' : 'The current address bounced. Check it with the client first.',
      runLog: [['Fri 30 Oct 17:00', 'weekly update built from the week\'s progress'], ['17:01', 'sent to ' + 'tunde@greenwaysupport.example'], ['17:02', 'bounced: the mailbox does not exist'], ['17:02', 'moved to Olu\'s outbox; Olu and Daniel told'], ['Mon 2 Nov 07:00', 'still waiting; Daniel covering this week']].map(([t, x]) => ({ t, x })),
      autos: [['Payment received, introduction call for Divine', 'Ran 3 times last week'], ['CQC email received, tell the client', 'Ran 5 times last week'], ['Document waiting 5 days, gentle nudge', 'Ran 19 times last week'], ['Weekly updates on Friday', '41 of 42 delivered']].map(([k, v]) => ({ k, v })),
      conns,
      q: s.q, onQ: e => this.setState({ q: e.target.value }),
      logTabs: [['all', 'All'], ['ap', 'Approvals'], ['vault', 'Vault'], ['prices', 'Prices'], ['people', 'People'], ['unusual', 'Unusual']].map(([k, label]) => ({ label, on: s.f === k, off: s.f !== k, pick: () => this.setState({ f: k }) })),
      log, noLog: log.length === 0, logCount: 'Showing ' + log.length + ' of ' + all.length + ' entries. Entries cannot be edited or deleted.',
      doExport: () => this.setState({ exported: true }), exportLabel: s.exported ? 'Export ready: audit-log.csv' : 'Export'
    };
  }
}'''
H['sa'] = 3160
# Moved to gen/sahome.py (super admin home). Kept for reference:
# build(OUT + '/SuperAdmin.dc.html', 'Super admin', 'Super admin', H['sa'], B_SA, S_SA, 'admin', CSS)

FDATA = r'''    const F = {
      cqc: ['CQC Registration Information Form', 'Used by: CQC domiciliary, CQC supported living, full start-up', [
        ['Company Registration Status', '', 'Always', ['Is your limited company already registered with Companies House? (Yes / No, please register it for me)']],
        ['Company Information', 'If the company is registered', 'When "Is your company registered?" is Yes', ['Registered Business Name', 'Trading Name (if different)', 'Company Registration Number', 'Registered Office Address', 'Correspondence Address (if different)', 'Business Telephone Number (required)', 'Company Email Address', 'Website', 'Type of Legal Entity', 'Partners or owners who are not directors']],
        ['Care Sync to Set Up Your Limited Company (3 pages)', 'If the company is not registered', 'When "Is your company registered?" is No', ['Service type (5 options) with SIC codes worked out automatically', '1st, 2nd and 3rd choice company names, trading name', 'Type of company, registered office', 'Director 1: legal name, date of birth, nationality, residence, service address, occupation, Companies House identity code', 'PSCs, shares, Companies House email and mobile', 'Authorisation and confirmation of accuracy']],
        ['Directors', '"Another director?" adds the next', 'Always. Director 2, 3 and 4 appear only when "Is there another director?" is Yes', ['Director: full name, date of birth, mobile, email', 'Is there another director?', 'More than four directors?']],
        ['Primary Service Type and CQC Service User Bands', '', 'Always', ['Regulated activities (5 options)', 'Service user bands (13 options)']],
        ['Registered Manager Details', '', 'Always', ['Title (6 options), full name, date of birth, email, mobile, current address', 'Registered with a professional body? (Yes / No)', 'CV']],
        ['Registered Manager Professional Registration', 'If registered with a professional body', 'When "Registered with a professional body?" is Yes', ['Professional body (11 options)', 'Professional registration number']],
        ['GP Details', 'Registered Manager only', 'Always', ["GP's name, surgery, address lines 1 and 2, town, county, postcode", 'Permission for CQC to contact the doctor']],
        ['Reference Details', 'Registered Manager only', 'Always', ['Must be the last employer (rules shown)', "Referee's title, first and last name, address, town, postcode, email, telephone", 'Permission for CQC to contact the referee']],
        ['Registered Manager and Nominated Individual Confirmation', '', 'Always', ['Will the same person serve as both? (Yes / No)', 'If Yes: the Nominated Individual pages are skipped and nothing is entered twice']],
        ['Nominated Individual Details', 'Only if a different person', 'When "Same person?" is No', ['Full name, date of birth, email, mobile, current address', 'Registered with a professional body?', 'CV']],
        ['Nominated Individual Professional Registration', 'Different person and registered', 'When "Same person?" is No and "Registered?" is Yes', ['Professional body (11 options)', 'Registration number']],
        ['DBS Check for Nominated Individual', 'Only if a different person', 'When "Same person?" is No', ['Enhanced DBS with Adult Workforce barred list and countersignature done? (Yes / No)']],
        ['Nominated Individual DBS Certificate Details', 'If their DBS is done', 'When "Same person?" is No and the DBS is done', ['Certificate number (12 digits)', 'Issue date (within 12 months)', 'Upload']],
        ['Nominated Individual: DBS application details', 'If their DBS is not done', 'When "Same person?" is No and the DBS is not done', ['Three forms of ID (6 options)', '5-year address history, addresses 1 to 5']],
        ['DBS Check for Registered Manager', '', 'Always. If the same person, this is the one DBS', ['Enhanced DBS done? (Yes / No)']],
        ['Registered Manager DBS Certificate Details', 'If the DBS is done', 'When the Registered Manager\'s DBS is done. No ID or address history is asked', ['Certificate number (12 digits)', 'Issue date (within 12 months, otherwise it must be redone)', 'Upload']],
        ['Registered Manager: DBS application details', 'If the DBS is not done', 'When the Registered Manager\'s DBS is not done', ['Three forms of ID (6 options)', '5-year address history, addresses 1 to 5, and more if needed']],
        ['Declaration', '', 'Always, last', ['Declaration statement', 'Signatory full name, position, signature, date']]
      ]],
      tender: ['Tender Preparation Questionnaire', 'Used by: tender writing', [
        ['This tender', '', 'Always', ['1.1 to 1.8: portal link, tender name, closing date, portal registration, PDFs, authority to submit. Portal passwords are never asked', '1.9 Completed this form before?']],
        ['What has changed', 'Returning clients', 'When 1.9 is "Yes, for an earlier tender". The profile pages below are then skipped', ['R.1 What has changed since you last filled in this form?', 'New or renewed documents']],
        ['About your company', 'First time only', 'When 1.9 is "No, this is our first time"', ['3.1 to 3.16. The share code (3.14) shows only if registered on the Central Digital Platform']],
        ['Your regulator', 'First time only', 'When 1.9 is No', ['2.1 Which regulator (7 options)', '2.2 More than one regulator']],
        ['CQC: 4A, 5A, 6A', 'If CQC', 'When 2.1 is CQC', ['Provider and location IDs, web page, inspection date, rating, conditions (4A.7 only if Yes)', 'Regulated activities (15), service types (15), service user bands (12)']],
        ['CIW: 4B, 5B, 6B', 'If CIW', 'When 2.1 is CIW', ['Provider ID, web page, inspection date, Regional Partnership Boards, Welsh Active Offer', 'Service types (11), range of needs (11)']],
        ['RQIA: 4C, 5C, 6C', 'If RQIA', 'When 2.1 is RQIA', ['Registration number, web page, inspection date, HSC Trusts', 'Service types (12), service user groups (10)']],
        ['5D. Your services and registration position', 'If not registered or not regulated', 'When 2.1 is Ofsted, Scotland, applying now, or not regulated', ['5D.1 Services and registration position']],
        ['6D. Ages and specialisms', 'First time only', 'When 1.9 is No', ['Youngest and oldest age, criteria, specialisms (28 options)']],
        ['7. Key people', 'First time only', 'When 1.9 is No', ['Owner, Nominated or Responsible Individual, Registered Manager, other senior staff', 'CVs']],
        ['Finance and insurance', 'First time only', 'When 1.9 is No', ['F.1 to F.6. F.4 shows only for a new company']],
        ['8. Track record and examples', 'First time only', 'When 1.9 is No. Examples 2 and 3 each on their own page when "another?" is Yes', ['8.1 Experience (4 options)', 'Contract examples 1 to 3 (8.2 to 8.34)']],
        ['Private client experience', 'If they have it', 'When 8.A is Yes. Examples 2 and 3 on their own pages', ['PRIV1 to PRIV3, initials only']],
        ['9. Workforce', 'First time only', 'When 1.9 is No', ['9.1 to 9.18, including visas and lowest hourly rate']],
        ['13. Partnerships and social value', 'First time only', 'When 1.9 is No', ['13.1 to 13.4']],
        ['14. Documents and policies', 'First time only', 'When 1.9 is No', ['14.1 documents (22), 14.2 policies (13), 14.3 to 14.5. A policy quote "Yes" creates a sales task']],
        ['Your evidence', 'First time only', 'When 1.9 is No', ['E.1 to E.7']],
        ['Lots', '', 'Always', ['L.1 to L.4']],
        ['Your services for this tender', '', 'Always', ['Home care? Supported living? Care home? Community support?']],
        ['Home care', 'If in the lots', 'When home care is Yes', ['11.1 to 11.8']],
        ['Supported living', 'If in the lots', 'When supported living is Yes', ['10.1 to 10.4']],
        ['Supported living property', 'If we provide it', 'When 10.4 is "We do, or our landlord partner does"', ['10.5 to 10.19']],
        ['Care home', 'If in the lots', 'When care home is Yes', ['12.1 to 12.9. 12.4 only for specialist provision']],
        ['Community support', 'If in the lots', 'When community support is Yes', ['C.1 to C.4']],
        ['Sign-off', '', 'Always, last', ['16.1 to 16.5']]
      ]],
      ciw: ['CIW Registration Information Form', 'Used by: CIW registration', [['Before You Start', 'Added', 'Always', ['Your name; authority to apply (3 options); CIW Online account (Yes / No)']], ['Organisation Information', '', 'Always. Filled from Companies House for a company or LLP', ['Legal entity (6 options)', 'Name, trading name, number, registered office, postcode', 'Office in Wales if different (shown only when Yes)', 'Telephone, email, website, preferred language, ICO']], ['Organisation History and Group', 'Added', 'Always. Details only when Yes', ['Ever registered with a regulator?', 'Owned 50% or more by another company?']], ['Organisation Officers', '"Another officer?" adds the next', 'Officer 2 and 3 only when Yes', ['Name, date of birth (dd/mm/yyyy), position, email, telephone, home address']], ['Service Details', '', 'Always. Councils list follows the areas ticked', ['Areas: tick boxes, one Statement of Purpose per area', 'Councils within the chosen areas', 'Range of needs (3, as CIW Online), with a check against the age range', 'Weekly hours (8 bands, as CIW Online)', 'Client groups (12, as used in Wales), Other opens a box', 'Start date (at least 14 weeks), taking over a service, office ownership, shared office']], ['How You Will Work', 'Added', 'Experience question only if learning disability or autism is ticked', ['Personal care, medicines, money, Welsh speakers']], ['RI Details', '', 'Always. Copied from the chosen officer', ['Place of birth, previous surnames, NI number, 5-year address history']], ['DBS Information', 'Done already? No ID', 'Certificate details when Yes; three IDs when No; Update Service ID only when subscribed', ['Full 12-digit number (was last 4)', 'Issue date, warn at 3 months', 'Checked against; Update Service']], ['RI Qualifications and Experience', 'Added', 'Details only when Yes', ['Qualifications, professional body, investigations, eligibility']], ['Registration History', '', 'A note only when an answer is Yes', ['Five questions from the form plus other business interests']], ['Every other officer: Checks and GP, References (2 pages each)', 'Added', 'For each officer who is not the RI, because CIW Online keeps a full People record for every officer', ['DBS (same rule as the RI), GP medical reference, history', 'Two referees with the same CIW checks']], ['RI References', '', 'Warnings when a referee is a relative or a company director, or neither employed the RI', ['Two referees, employed 3 months?']], ['RI GP Details', '', 'Always', ['GP details; CIW GP form sent early']], ['Registered Manager Details', '', 'Nothing more if not chosen yet; only qualifications if the RI is the manager', ['Social Care Wales status and number, Level 5, qualifications']], ['Registered Manager: DBS, References, GP and History (3 pages)', 'Only if a different person', 'When the manager is chosen and is not the RI', ['Same DBS rule as the RI', 'Two referees with the same CIW checks', 'GP, registration history']], ['Your CIW Choices', 'Added', 'Always. Warnings when a choice would delay the application', ['Legal notices by email, sharing with Social Care Wales and Dewis Cymru', 'Areas and RI as conditions of registration']], ['Required Documents', '', 'Uploads match the answers', ['CV per person, DBS ID only when needed, documents you already have']], ['Declaration', '', 'Always last, after Check your answers', ['Three ticks, name, position, signature, date']]]],
      rqia: ['RQIA Registration Information Form', 'Used by: RQIA registration', [['Organisation Information', '', 'Always. Filled from Companies House for a company or LLP', ['Legal entity (7 options), name, trading name, number, address', 'Telephone, email, website, ICO, RQIA Web Portal login']], ['Organisation Officers', '"Another officer?" adds the next', 'Officer 2 and 3 only when Yes', ['Name, date of birth (dd/mm/yyyy), position, email, telephone']], ['Service Details', '', 'Always', ['Service type (4 options), name, address', 'HSC Trust areas: tick boxes', 'Age range, service users, groups (9), start date']], ['How You Will Work', 'Added', 'Experience question only if learning disability or autism is ticked', ['Personal care, medicines, money, starting staff numbers']], ['RI Details', '', 'Always. Copied from the chosen officer', ['Place of birth, previous surnames, address, 5-year address history']], ['AccessNI Information', 'Always three IDs', 'RQIA runs its own AccessNI check for registration, so three IDs are always collected; certificate details are optional', ['Certificate number and date (optional)', 'Three IDs: at least one photo ID and one proof of address']], ['RI Qualifications and Experience', 'Added', 'Details only when Yes', ['Qualifications, professional body, investigations, experience']], ['Registration History', '', 'A note only when an answer is Yes', ['Five questions']], ['RI References', '', 'Warning when a referee is related', ['Two referees; relationship asked for both']], ['RI GP Details', '', 'Always', ['GP details']], ['Registered Manager Details', '', 'Only qualifications if the RI is the manager', ['NISCC/NMC/HCPC number, Level 5', 'If different: details and address history']], ['Registered Manager: AccessNI, References, GP and History (3 pages)', 'Only if a different person', 'When the manager is not the RI', ['The same AccessNI check as the RI', 'Two referees, one the current or most recent employer', 'GP, registration history']], ['Required Documents', '', 'Uploads match the answers', ['CV per person, AccessNI ID only when needed, documents you already have']], ['Declaration', '', 'Always last, after Check your answers', ['Three ticks, name, position, signature, date']]]]
    };
'''
FB_ADDONS = r'''    const D = {
      sladd: ['Supported living add-on', 'Adding supported living to a CQC registration', [
        ['Your registration', '', 'Always. Filled in from your Hub record where we have it', ['CQC provider ID and location ID', 'Regulated activities you hold now', 'Upload your current registration certificate']],
        ['Who you will support', '', 'Always', ['Service user bands for supported living', 'Will you support autistic people or people with a learning disability? (Yes / No)', 'How many people, and in how many homes', 'Start date you are aiming for']],
        ['Housing and care', '', 'Always', ['Who is the landlord or housing provider?', 'Are housing and care provided by different organisations? (Yes / No)', 'Tenancy agreements: upload an example if you have one']],
        ['Your manager', '', 'Always', ['Will your registered manager stay the same? (Yes / No)', 'Experience of supported living, in a few lines']],
        ['Declaration', '', 'Always, last', ['Name, position, signature, date']]
      ]],
      int: ['CQC interview preparation', 'Application already in, interview booked or expected', [
        ['Your application', '', 'Always', ['Which regulator (CQC, CIW, RQIA)', 'Date the application went in', 'Interview date, if booked']],
        ['Who is being interviewed', '"Another person?" adds the next', 'Always', ['Name, role (registered manager, nominated individual, responsible individual)', 'Email for their Interview Preparation Hub account (the Hub creates it with the regulator, service type and role)']],
        ['Your service', '', 'Always', ['Service type and service user bands', 'Upload your Statement of Purpose']],
        ['Your sessions', '', 'Always', ['Best days and times for 3 sessions with Millicent', 'Anything you feel unsure about']]
      ]],
      pir: ['PIR writing', 'When a Provider Information Return arrives', [
        ['The PIR', '', 'Always', ['Date the PIR request arrived', 'Deadline shown in the email', 'Location and service types (one PIR each)']],
        ['Your service in numbers', '', 'Always', ['People supported now', 'Staff numbers and vacancies', 'Complaints, compliments and safeguarding referrals in the last 12 months', 'Notifications sent in the last 12 months']],
        ['Briefing', '', 'Always', ['Best times for a 60 to 90 minute briefing with the registered manager', 'Who can confirm the final answers?']]
      ]],
      var: ['Registration variation', 'Adding a location, a service or a band', [
        ['What is changing', '', 'Always', ['Add a location, add a service, add a service user band, or remove something', 'When you want the change to start']],
        ['Your registration now', '', 'Always. Filled in from your Hub record where we have it', ['Provider and location IDs', 'Upload your current certificate']],
        ['New location', 'If adding a location', 'When "Add a location" is chosen', ['Address and how you hold it (owned or rented)', 'Landlord letter or lease (we can ask the landlord for you)', 'Manager for this location']],
        ['New service or band', 'If adding a service or band', 'When "Add a service" or "Add a band" is chosen', ['Service type or band', 'Staff training for it, in a few lines']],
        ['Declaration', '', 'Always, last', ['Name, position, signature, date']]
      ]],
      web: ['Website or marketing', 'Brand, website and Google profile', [
        ['Your brand', '', 'Always', ['Trading name', 'Logo and colours, if you have them', 'Three words that describe your service']],
        ['Your website', '', 'Always', ['Do you have a website or domain now? (Yes / No)', 'Login for the domain (goes to the vault)', 'Services and areas to show']],
        ['Photos and stories', '', 'Always', ['Photos you can use, with permission', 'Can we quote a happy family? (only with their consent)']],
        ['Google Business Profile', '', 'Always', ['Do you have one? (Yes / No)', 'Office address and opening hours']]
      ]]
    };
'''
# ---------------------------------------------------------------- 3. Forms (super admin menu, board 44)
B_FB = '''      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 4px; max-width: 760px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Forms</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Every onboarding form, its versions, and every screen that reads it. Grace drafts. A new version goes live only when a super admin who did not draft or edit it approves it.</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px; align-items: flex-start;">
          <span class="bz-lbl">You are acting as</span>
          ''' + tabs('asTabs', 'Acting as') + '''
        </div>
      </div>

      <section class="sb-card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 10px;" aria-labelledby="fm-h">
        <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 12px; flex-wrap: wrap;"><h2 id="fm-h" class="sb-h2" style="font-size: 16px;">Forms</h2><span class="{{statusCls}}">{{status}}</span></div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: stretch;">
          <sc-for list="{{forms}}" as="p" hint-placeholder-count="9">
            <sc-if value="{{p.on}}" hint-placeholder-val="{{ false }}"><button class="fb-pkg" aria-pressed="true" onClick="{{p.pick}}" style="border: 2px solid var(--cs-action-primary); background: var(--cs-selection-bg); color: var(--cs-selection-text);"><span style="font-weight: 600;">{{p.label}}</span><span class="{{p.chipCls}}" style="align-self: flex-start;">{{p.chip}}</span></button></sc-if>
            <sc-if value="{{p.off}}" hint-placeholder-val="{{ true }}"><button class="fb-pkg" aria-pressed="false" onClick="{{p.pick}}" style="border: 1px solid var(--cs-border-subtle); background: var(--cs-surface-raised); color: var(--cs-text-primary);"><span style="font-weight: 500;">{{p.label}}</span><span class="{{p.chipCls}}" style="align-self: flex-start;">{{p.chip}}</span></button></sc-if>
          </sc-for>
        </div>
        <span class="sb-muted">{{usedBy}}</span>
      </section>

      <sc-if value="{{isCqc}}" hint-placeholder-val="{{ true }}">
        <section class="sb-card" aria-labelledby="v8-h">
          <div class="sb-head"><h2 id="v8-h" class="sb-h2">{{v8Title}}</h2><span style="display: flex; gap: 8px; flex-wrap: wrap;"><span class="{{liveChipCls}}">{{liveChip}}</span><span class="{{draftChipCls}}">{{draftChip}}</span></span></div>
          <div class="sb-row" style="border-top: 0; padding-top: 0;"><span class="sb-sub">Drafted by Grace on Thu 29 Oct and sent for approval. It adds a "Your office" page, because the office address gate needs it; rewords 1 question so a missing second director is caught early; and removes "Type of Legal Entity", which now comes from Companies House. Collins or Rachel Turner approves.</span></div>
          <div style="padding: 0 20px 12px;">''' + tabs('v8Tabs', 'Draft v8') + '''</div>

          <sc-if value="{{tChanges}}" hint-placeholder-val="{{ true }}">
            <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--cs-border-subtle);">
              <sc-for list="{{changes}}" as="c" hint-placeholder-count="3">
                <div style="padding: 14px 20px; display: flex; flex-direction: column; gap: 8px; border-right: 1px solid var(--cs-border-subtle);">
                  <span style="display: flex; gap: 8px; align-items: center;"><span class="{{c.cls}}">{{c.k}}</span><span class="sb-sub">{{c.n}}</span></span>
                  <sc-for list="{{c.items}}" as="i" hint-placeholder-count="1">
                    <div class="bz-box" style="gap: 2px;"><span class="bz-lbl">{{i.page}}</span><span style="font-size: 13px; line-height: 18px;">{{i.now}}</span><sc-if value="{{i.hasWas}}" hint-placeholder-val="{{ false }}"><span class="sb-muted">{{i.was}}</span></sc-if></div>
                  </sc-for>
                </div>
              </sc-for>
            </div>
            <sc-if value="{{hasMyEdits}}" hint-placeholder-val="{{ false }}"><div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 4px;"><span class="bz-lbl">{{editorLine}}</span><sc-for list="{{myEdits}}" as="m" hint-placeholder-count="1"><span class="sb-sub">{{m}}</span></sc-for></div></sc-if>
          </sc-if>

          <sc-if value="{{tImpact}}" hint-placeholder-val="{{ false }}">
            <div class="sb-row" style="border-top: 1px solid var(--cs-border-subtle); padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 0 0 250px;">Where it is used</span><span class="sb-th" style="flex: 1 1 400px;">What changes with v8</span><span class="sb-th" style="flex: 0 0 120px;"></span></div>
            <sc-for list="{{impact}}" as="im" hint-placeholder-count="6">
              <div class="sb-row" style="align-items: flex-start;">
                <span style="flex: 0 0 250px; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{im.where}}</span><span class="sb-muted">{{im.board}}</span></span>
                <span style="flex: 1 1 400px; min-width: 0;" class="sb-sub">{{im.what}}</span>
                <span style="flex: 0 0 120px; display: flex; justify-content: flex-end;"><a class="sb-btn b-gh bz-link" href="{{im.href}}" aria-label="{{im.aria}}">Open</a></span>
              </div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">Clients affected today: 3 on v7 who have not finished. Every new CQC, supported living and full start-up client gets v8 from the day it is approved. Nothing changes for a client until they are moved.</span></div>
          </sc-if>

          <sc-if value="{{tClients}}" hint-placeholder-val="{{ false }}">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px; border-top: 1px solid var(--cs-border-subtle);">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center; flex-wrap: wrap;"><span class="bz-b">{{halfTitle}}</span><sc-if value="{{canMoveAll}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-sec" onClick="{{moveAll}}">Move all to v8</button></sc-if></div>
              <span class="sb-sub">{{halfNote}}</span>
              <sc-for list="{{half}}" as="h" hint-placeholder-count="3">
                <div style="display: flex; gap: 12px; align-items: center; padding: 8px 0; border-top: 1px solid var(--cs-border-subtle);">
                  <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{h.name}}</span><span class="sb-sub">{{h.where}}</span><span class="sb-muted">{{h.after}}</span></span>
                  <span class="{{h.cls}}">{{h.ver}}</span>
                  <sc-if value="{{h.canMove}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" onClick="{{h.move}}">Move to v8</button></sc-if>
                </div>
              </sc-for>
              <span class="sb-muted">All 3 are in Grace's onboarding queue (board 73).</span>
            </div>
          </sc-if>

          <sc-if value="{{tMsg}}" hint-placeholder-val="{{ false }}">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 10px; border-top: 1px solid var(--cs-border-subtle);">
              <span class="sb-sub">Sent when a client is moved to v8, from hello@caresyncexperts.co.uk with Grace's name, and shown in the client's Hub. Never sent between 8pm and 8am. Edit the wording in Messages and automations (board 82).</span>
              <div style="display: flex; gap: 8px; flex-wrap: wrap;">''' + tabs('msgTabs', 'Message for') + '''</div>
              <div class="bz-box" style="gap: 8px;">
                <span class="bz-lbl">{{msg.subjectK}}</span><span class="bz-b">{{msg.subject}}</span>
                <sc-for list="{{msg.lines}}" as="ml" hint-placeholder-count="4"><span style="font-size: 14px; line-height: 21px;">{{ml}}</span></sc-for>
              </div>
            </div>
          </sc-if>

          <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 10px; background: var(--cs-surface-subtle);">
            <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center; flex-wrap: wrap;"><span style="display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{apTitle}}</span><span class="sb-sub">{{apNote}}</span></span><span class="{{apChipCls}}">{{apChip}}</span></div>
            <sc-if value="{{needDp}}" hint-placeholder-val="{{ false }}">
              <div class="bz-amb"><span class="bz-b">Data protection lead needed</span><span class="sb-sub">{{dpText}}</span><sc-if value="{{canDp}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-sec" style="align-self: flex-start;" onClick="{{dpAgree}}">Agree as data protection lead</button></sc-if></div>
            </sc-if>
            <sc-if value="{{canApprove}}" hint-placeholder-val="{{ true }}">
              <span class="bz-lbl">Who gets v8</span>
              <div style="display: flex; gap: 8px; flex-wrap: wrap;">''' + tabs('rollTabs', 'Who gets v8') + '''</div>
              <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">Your reason (written to the audit log)</span><textarea class="bz-ta" value="{{apReason}}" onChange="{{onApReason}}" placeholder="For example: the office page lets gate 3 start on day one"></textarea></label>
              <sc-if value="{{apErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Write a reason first.</span></sc-if>
              <span style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{approve}}">Approve v8</button><button class="sb-btn b-gh" onClick="{{back}}">Send back to Grace</button></span>
            </sc-if>
            <sc-if value="{{cannotNote}}" hint-placeholder-val="{{ false }}"><span class="sb-sub">{{cannotText}}</span></sc-if>
            <sc-if value="{{isLive}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-gh" style="align-self: flex-start;" onClick="{{undoLive}}">Reset the demo</button></sc-if>
          </div>
        </section>
      </sc-if>

      <sc-if value="{{isDraft}}" hint-placeholder-val="{{ false }}">
        <div class="bz-amb"><span class="bz-b">Draft, not live yet</span><span class="sb-sub">{{draftNote}}</span></div>
      </sc-if>
      <sc-if value="{{isOtherLive}}" hint-placeholder-val="{{ false }}">
        <div class="bz-box" style="flex-direction: row; justify-content: space-between; align-items: center; flex-wrap: wrap;"><span><span class="bz-b">{{verLine}}</span> {{otherNote}}</span></div>
      </sc-if>

      <div class="bz-cols" style="flex-wrap: nowrap;">
        <section aria-labelledby="pg-h" class="sb-card" style="flex: 0 0 300px; min-width: 0; padding: 14px; display: flex; flex-direction: column; gap: 6px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin: 0 2px 4px; gap: 8px;">
            <h2 id="pg-h" style="margin: 0; font-size: 16px; line-height: 24px; font-weight: 500;">Pages, in order</h2>
            <span class="sb-muted">{{pageCount}}</span>
          </div>
          <sc-if value="{{isCqc}}" hint-placeholder-val="{{ true }}"><div style="display: flex; gap: 6px;">''' + tabs('verTabs', 'Version shown') + '''</div></sc-if>
          <div class="fb-list" style="display: flex; flex-direction: column; gap: 5px; max-height: 760px; overflow-y: auto; padding: 2px;">
          <sc-for list="{{pages}}" as="m" hint-placeholder-count="12">
            <sc-if value="{{m.sel}}" hint-placeholder-val="{{ false }}">
              <button class="fb-mod" onClick="{{m.pick}}" style="border: 2px solid var(--cs-action-primary); background: var(--cs-selection-bg);">
                <span style="width: 24px; height: 24px; flex-shrink: 0; border-radius: 7px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600;">{{m.n}}</span>
                <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px; min-width: 0;"><span style="font-size: 13px; line-height: 18px; font-weight: 500;">{{m.name}}</span><sc-if value="{{m.hasRule}}" hint-placeholder-val="{{ false }}"><span class="fb-rule">{{m.rule}}</span></sc-if><sc-if value="{{m.hasFlag}}" hint-placeholder-val="{{ false }}"><span class="{{m.flagCls}}" style="align-self: flex-start;">{{m.flag}}</span></sc-if></span>
              </button>
            </sc-if>
            <sc-if value="{{m.unsel}}" hint-placeholder-val="{{ true }}">
              <button class="fb-mod" onClick="{{m.pick}}" style="border: 1px solid var(--cs-border-subtle); background: var(--cs-surface-raised);">
                <span style="width: 24px; height: 24px; flex-shrink: 0; border-radius: 7px; background: var(--cs-surface-brand); color: var(--cs-text-brand); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600;">{{m.n}}</span>
                <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px; min-width: 0;"><span style="font-size: 13px; line-height: 18px; font-weight: 500;">{{m.name}}</span><sc-if value="{{m.hasRule}}" hint-placeholder-val="{{ false }}"><span class="fb-rule">{{m.rule}}</span></sc-if><sc-if value="{{m.hasFlag}}" hint-placeholder-val="{{ false }}"><span class="{{m.flagCls}}" style="align-self: flex-start;">{{m.flag}}</span></sc-if></span>
              </button>
            </sc-if>
          </sc-for>
          </div>
          <span class="sb-muted" style="padding: 6px 2px 0;">Scroll for every page. Blue tags are the skip rules. Answers are never asked twice, pages that do not apply are skipped, every answer saves as you go, and the client can stop and come back.</span>
        </section>

        <section aria-labelledby="qs-h" class="sb-card" style="flex: 1 1 380px; min-width: 0; padding: 16px 18px; display: flex; flex-direction: column; gap: 10px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px;">
            <h2 id="qs-h" style="margin: 0; font-size: 16px; line-height: 24px; font-weight: 500;">{{cur.name}}</h2>
            <span class="sb-muted">{{cur.ver}}</span>
          </div>
          <div class="bz-box" style="gap: 2px;"><span class="bz-lbl">Show this page</span><span style="font-size: 13px; line-height: 18px; font-weight: 500;">{{cur.when}}</span></div>
          <sc-for list="{{qs}}" as="q" hint-placeholder-count="4">
            <div style="border-radius: 10px; border: 1px solid var(--cs-border-subtle); display: flex; flex-direction: column;">
              <div style="padding: 8px 10px 8px 12px; display: flex; justify-content: space-between; gap: 8px; align-items: center;">
                <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span style="font-size: 13px; line-height: 18px;">{{q.w}}</span><span style="display: flex; gap: 6px; flex-wrap: wrap;"><span class="{{q.tagCls}}">{{q.tag}}</span><span class="sb-chip c-neutral">{{q.v}}</span><sc-if value="{{q.hasFlag}}" hint-placeholder-val="{{ false }}"><span class="{{q.flagCls}}">{{q.flag}}</span></sc-if></span></span>
                <button class="sb-btn b-gh" onClick="{{q.edit}}" aria-label="{{q.aria}}"><span style="display: inline-flex; gap: 6px; align-items: center;"><x-import component-from-global-scope="CareSync.Icon" name="pencil-line" size="{{n16}}"></x-import>Edit</span></button>
              </div>
              <sc-if value="{{q.open}}" hint-placeholder-val="{{ false }}">
                <div style="padding: 12px; border-top: 2px solid var(--cs-action-primary); display: flex; flex-direction: column; gap: 10px;">
                  <span class="sb-sub">{{edNote}}</span>
                  <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">Wording the client sees</span><textarea class="bz-ta" value="{{edW}}" onChange="{{onEdW}}"></textarea></label>
                  <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">Help text (also used by Questions inbox suggested replies)</span><textarea class="bz-ta" value="{{edH}}" onChange="{{onEdH}}" placeholder="One or two plain sentences"></textarea></label>
                  <span class="bz-lbl">Validation</span>
                  <div style="display: flex; gap: 6px; flex-wrap: wrap;">''' + tabs('valTabs', 'Validation') + '''</div>
                  <span class="bz-lbl">Data category</span>
                  <div style="display: flex; gap: 6px; flex-wrap: wrap;">''' + tabs('tagTabs', 'Data category') + '''</div>
                  <span class="sb-muted">{{tagHelp}}</span>
                  <sc-if value="{{edDp}}" hint-placeholder-val="{{ false }}"><div class="bz-amb"><span class="bz-b">Needs the data protection lead</span><span class="sb-sub">Adding special category, criminal offence or credential data needs Collins (data protection lead) to agree before this version can be approved. Collins sees why it is needed, who can see it and how long it is kept.</span></div></sc-if>
                  <sc-if value="{{edErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">The wording cannot be empty.</span></sc-if>
                  <span style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{edSave}}">{{edSaveLabel}}</button><button class="sb-btn b-gh" onClick="{{edCancel}}">Cancel</button></span>
                </div>
              </sc-if>
            </div>
          </sc-for>
          <sc-if value="{{savedMsg}}" hint-placeholder-val="{{ false }}"><div class="bz-ok"><span class="sb-sub">{{savedText}}</span></div></sc-if>
        </section>

        <section aria-labelledby="pv-h" class="sb-card" style="flex: 0 0 340px; min-width: 0; padding: 16px; display: flex; flex-direction: column; gap: 10px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px;"><h2 id="pv-h" style="margin: 0; font-size: 16px; line-height: 24px; font-weight: 500;">Preview as the client</h2><span class="sb-muted">{{pvVer}}</span></div>
          <div style="border-radius: 22px; border: 1px solid var(--cs-border-default); background: var(--cs-surface-page); padding: 16px 14px; display: flex; flex-direction: column; gap: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center;"><span class="sb-muted">{{pv.step}}</span><span class="sb-muted">{{pv.time}}</span></div>
            <div class="bar" aria-hidden="true"><span class="{{pv.bar}}"></span></div>
            <span style="font-size: 18px; line-height: 24px; font-weight: 600;">{{pv.title}}</span>
            <sc-for list="{{pv.qs}}" as="pq" hint-placeholder-count="3">
              <div style="display: flex; flex-direction: column; gap: 4px;">
                <span style="font-size: 14px; line-height: 20px; font-weight: 500;">{{pq.w}}</span>
                <sc-if value="{{pq.hasHelp}}" hint-placeholder-val="{{ false }}"><span class="sb-sub">{{pq.h}}</span></sc-if>
                <div style="min-height: 40px; border-radius: 10px; border: 1px solid var(--cs-border-control); background: var(--cs-surface-raised); display: flex; align-items: center; padding: 0 12px; font-size: 13px; color: var(--cs-text-muted);">{{pq.ph}}</div>
                <span style="font-size: 12px; line-height: 16px; color: var(--cs-text-brand); font-weight: 500;">Not sure? Ask us</span>
              </div>
            </sc-for>
            <sc-if value="{{pv.more}}" hint-placeholder-val="{{ false }}"><span class="sb-muted">{{pv.moreText}}</span></sc-if>
            <div style="min-height: 44px; border-radius: 12px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 500;">Save and continue</div>
            <span class="sb-muted" style="text-align: center;">Your answers save as you go</span>
          </div>
          <span class="sb-muted">Shows the selected page with any changes not yet saved, as a phone shows it.</span>
        </section>
      </div>
'''
FB_CSS = '''.fb-list>*,.fb-list button{flex-shrink:0}
.fb-pkg{min-height:44px;padding:6px 10px;border-radius:10px;font:inherit;font-size:12px;text-align:left;cursor:pointer;display:flex;flex-direction:column;gap:4px}
.fb-pkg:focus-visible,.fb-mod:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:2px}
.fb-mod{width:100%;min-height:38px;padding:5px 8px;border-radius:10px;font:inherit;text-align:left;cursor:pointer;display:flex;align-items:center;gap:10px;color:var(--cs-text-primary)}
.fb-rule{display:inline-flex;align-items:center;gap:6px;padding:2px 8px;border-radius:999px;background:var(--cs-status-info-bg);color:var(--cs-status-info-text);font-size:11px;line-height:16px;font-weight:500;align-self:flex-start}
'''
S_FB = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { as: 'collins', form: 'cqc', ver: 'v8', page: 4, v8: 'waiting', tab: 'changes', msgFor: 'oh', moved: {}, edits: {}, editors: [], dpNeed: [], dpOk: false,
      openQ: '', edW: '', edH: '', edV: '', edT: '', edErr: false, saved: '', roll: 'new', apReason: '', apErr: false, decided: '' };
  }
  renderVals() {
''' + FDATA + FB_ADDONS + r'''
    const s = this.state;
    const ME = s.as === 'collins' ? 'Collins' : 'Rachel Turner';
    // v8 of the CQC form, as decision 4: adds "Your office", rewords 1 question, removes "Type of Legal Entity".
    const OLD_DIR = 'Is there another director?';
    const NEW_DIR = 'Companies House lists every director. Is there another director to add?';
    const v7 = F.cqc[2];
    const v8 = [];
    v7.forEach(p => {
      let qs = p[3].slice();
      if (p[0] === 'Company Information') qs = qs.filter(q => q !== 'Type of Legal Entity');
      if (p[0] === 'Directors') qs = qs.map(q => q === OLD_DIR ? NEW_DIR : q);
      v8.push([p[0], p[1], p[2], qs, p[0] === 'Company Information' ? ['Removed', 'bad', '1 removed'] : (p[0] === 'Directors' ? ['Reworded', 'info', '1 reworded'] : null)]);
      if (p[0] === 'Directors') v8.push(['Your office', 'New in v8', 'Always. Feeds gate 3, office address evidence', ['Office address (postcode lookup)', 'Do you own or rent the office? (Own / Rent)', 'Landlord name and email (we ask the landlord for the letter for you)', 'Tenancy, lease or proof of ownership (upload)', 'Is this also your registered office? (Yes / No)'], ['Added', 'ok', 'New page']]);
    });
    const HELP = {
      'Office address (postcode lookup)': 'The address where you will run the service from. CQC needs evidence you can use it.',
      'Landlord name and email (we ask the landlord for the letter for you)': 'We email your landlord a short form to confirm you can use the office for care work. You do not need to chase them.',
      [NEW_DIR]: 'We check Companies House for you. Every director listed there must be on this form.',
      'Certificate number (12 digits)': 'The 12 numbers at the top right of the certificate.',
      "GP's name, surgery, address lines 1 and 2, town, county, postcode": 'CQC may ask your GP to confirm you are fit to manage the service.'
    };
    const tagOf = q => /DBS|barred|AccessNI|investigation|Registration History|registration history|criminal/i.test(q) ? 'criminal' : (/GP|doctor|medical|health/i.test(q) ? 'special' : (/password|login|vault|identity code/i.test(q) ? 'credential' : (/^Office address|own or rent|^Tenancy|registered office\?/i.test(q) ? 'business' : (/Business Name|Trading Name|Company Registration|Registered Office|Business Telephone|Company Email|Website|Legal Entity|Service type|Regulated activities|Service user bands|SIC|Type of company|tender|portal|Lots|L\.1/i.test(q) ? 'business' : 'personal'))));
    const valOf = q => /Upload|upload|CV$|Tenancy|lease/.test(q) ? 'upload' : (/12 digits/.test(q) ? 'digits12' : (/Yes \/ No|Own \/ Rent|another/.test(q) ? 'yesno' : (/date of birth|Issue date|date/i.test(q) ? 'date' : (/email/i.test(q) ? 'email' : (/mobile|telephone/i.test(q) ? 'phone' : 'text')))));
    const TAGS = [['business', 'Business only', 'c-neutral'], ['personal', 'Personal', 'c-info'], ['special', 'Special category', 'c-warn'], ['criminal', 'Criminal offence', 'c-bad'], ['credential', 'Credential', 'c-brand']];
    const VALS = [['text', 'Required text'], ['yesno', 'Choice'], ['date', 'Date, dd/mm/yyyy'], ['email', 'Email address'], ['phone', 'UK phone number'], ['digits12', 'Exactly 12 digits'], ['upload', 'Upload, PDF or photo'], ['optional', 'Optional']];
    const PH = { text: 'Type your answer', yesno: 'Choose one', date: 'dd/mm/yyyy', email: 'name@example.co.uk', phone: '07700 900000', digits12: '12 digits', upload: 'Choose a file or take a photo', optional: 'Optional' };
    const tagName = k => TAGS.find(t => t[0] === k)[1];
    const tagCls = k => 'sb-chip ' + TAGS.find(t => t[0] === k)[2];
    const valName = k => VALS.find(v => v[0] === k)[1];
    const SENS = ['special', 'criminal', 'credential'];

    const VER = { cqc: 'Live v7', ciw: 'Live v3', rqia: 'Live v2', tender: 'Live v5' };
    const MATCH = { cqc: 'matches the Google Form', tender: 'matches the Google Form', ciw: 'mapped to CIW Online', rqia: 'mapped to the RQIA Web Portal' };
    const all = Object.assign({}, F, D);
    const order = ['cqc', 'ciw', 'rqia', 'tender', 'sladd', 'int', 'pir', 'var', 'web'];
    const live8 = s.v8 === 'live';
    const verOf = k => k === 'cqc' && live8 ? 'Live v8' : VER[k];
    const isD = !!D[s.form];
    const isCqc = s.form === 'cqc';
    const forms = order.map(k => {
      const d = !!D[k];
      const chip = d ? 'Draft' : (k === 'cqc' ? (live8 ? 'Live v8' : 'Live v7. v8 waiting') : verOf(k));
      return { label: all[k][0].replace(' Registration Information Form', '').replace(' Preparation Questionnaire', ''), on: k === s.form, off: k !== s.form,
        pick: () => this.setState({ form: k, page: 0, openQ: '', saved: '', ver: 'v8' }), chip, chipCls: 'sb-chip ' + (d ? 'c-warn' : (k === 'cqc' && !live8 ? 'c-info' : 'c-ok')) };
    });
    const showVer = isCqc ? (live8 ? 'v8' : s.ver) : 'live';
    const list = isCqc ? (showVer === 'v8' ? v8 : v7.map(p => p.concat([null]))) : all[s.form][2].map(p => p.concat([null]));
    const pi = Math.min(s.page, list.length - 1);
    const pages = list.map((p, i) => ({ n: String(i + 1), name: p[0], rule: p[1], hasRule: !!p[1] && !p[4], sel: i === pi, unsel: i !== pi,
      hasFlag: !!p[4], flag: p[4] ? p[4][2] : '', flagCls: 'sb-chip c-' + (p[4] ? p[4][1] : 'neutral'), pick: () => this.setState({ page: i, openQ: '', saved: '' }) }));
    const c = list[pi];
    const keyBase = s.form + ':' + showVer + ':' + c[0] + ':';
    const draftName = isCqc ? 'draft v8' : 'a new draft';
    const qObj = (q, i) => {
      const k = keyBase + i; const e = s.edits[k] || {};
      const base = { w: q, h: HELP[q] || '', v: valOf(q), t: tagOf(q) };
      const cur = Object.assign({}, base, e);
      const isNew = isCqc && showVer === 'v8' && c[0] === 'Your office';
      const rew = isCqc && showVer === 'v8' && q === NEW_DIR;
      const flag = e.w || e.h || e.v || e.t ? 'Edited by ' + e.by : (isNew ? 'New in v8' : (rew ? 'Reworded in v8' : ''));
      return { k, base, cur, flag };
    };
    const QO = c[3].map(qObj);
    const editable = !isD && !(isCqc && live8 && showVer === 'v8' && false);
    const qs = QO.map((o, i) => ({ w: o.cur.w, tag: tagName(o.cur.t), tagCls: tagCls(o.cur.t), v: valName(o.cur.v), hasFlag: !!o.flag, flag: o.flag, flagCls: 'sb-chip ' + (o.flag.indexOf('Edited') === 0 ? 'c-warn' : (o.flag.indexOf('New') === 0 ? 'c-ok' : 'c-info')),
      aria: 'Edit question: ' + o.cur.w, open: s.openQ === o.k,
      edit: () => { if (isCqc && showVer === 'v7') { this.setState({ ver: 'v8', openQ: '', saved: 'Changes go into draft v8, never into the live v7. Showing v8: choose the question again to edit it.' }); return; }
        this.setState({ openQ: s.openQ === o.k ? '' : o.k, edW: o.cur.w, edH: o.cur.h, edV: o.cur.v, edT: o.cur.t, edErr: false, saved: '' }); } }));
    const openObj = QO.find(o => o.k === s.openQ);
    const edDp = !!openObj && SENS.indexOf(s.edT) >= 0 && SENS.indexOf(openObj.base.t) < 0 && s.edT !== openObj.base.t;
    const edSave = () => {
      if (!s.edW.trim()) { this.setState({ edErr: true }); return; }
      const o = openObj; const ch = { by: ME };
      if (s.edW.trim() !== o.base.w) ch.w = s.edW.trim();
      if (s.edH.trim() !== o.base.h) ch.h = s.edH.trim();
      if (s.edV !== o.base.v) ch.v = s.edV;
      if (s.edT !== o.base.t) ch.t = s.edT;
      const changed = ch.w || ch.h || ch.v || ch.t;
      const edits = Object.assign({}, s.edits); if (changed) edits[o.k] = ch; else delete edits[o.k];
      const editors = changed && s.editors.indexOf(ME) < 0 ? s.editors.concat([ME]) : s.editors;
      const dpNeed = edDp ? s.dpNeed.filter(x => x !== o.k).concat([o.k]) : s.dpNeed.filter(x => x !== o.k);
      this.setState({ edits, editors, dpNeed, dpOk: edDp ? false : s.dpOk, openQ: '', saved: changed ? 'Saved to ' + draftName + ' by ' + ME + '. ' + (isCqc ? 'Because you edited the draft, ' + (ME === 'Collins' ? 'Rachel Turner' : 'Collins') + ' approves it.' : 'Grace reviews it before it goes for approval.') : 'No change made.' });
    };
    // Preview as the client: uses unsaved editor values for the open question.
    const pvQs = QO.slice(0, 4).map(o => { const live = s.openQ === o.k ? { w: s.edW, h: s.edH, v: s.edV } : o.cur; return { w: live.w || ' ', h: live.h, hasHelp: !!live.h, ph: PH[live.v] || 'Type your answer' }; });
    const mins = Math.max(1, Math.round(QO.length * 0.6));
    const pv = { step: 'Page ' + (pi + 1) + ' of ' + list.length, time: 'About ' + mins + (mins === 1 ? ' minute' : ' minutes'), bar: 'w' + Math.max(5, Math.round((pi + 1) / list.length * 20) * 5), title: c[0], qs: pvQs, more: QO.length > 4, moreText: '+ ' + (QO.length - 4) + ' more on this page' };

    // Changes view (decision 4)
    const changes = [
      ['Added', 'ok', 'Your office: 1 new page, 5 questions', [['Page 5 of 20, after Directors', 'Your office: address, own or rent, landlord, tenancy or lease, registered office', '']]],
      ['Reworded', 'info', '1 question', [['Directors', NEW_DIR, 'Was: ' + OLD_DIR]]],
      ['Removed', 'bad', '1 question', [['Company Information', 'Type of Legal Entity', 'Now read from Companies House, so it is not asked']]]
    ].map(([k, cls, n, items]) => ({ k, cls: 'sb-chip c-' + cls, n, items: items.map(([page, now, was]) => ({ page, now, was, hasWas: !!was })) }));
    const myEdits = Object.keys(s.edits).filter(k => k.indexOf('cqc:v8:') === 0).map(k => { const e = s.edits[k]; const parts = k.split(':'); const bits = []; if (e.w) bits.push('wording'); if (e.h) bits.push('help text'); if (e.v) bits.push('validation to ' + valName(e.v)); if (e.t) bits.push('data category to ' + tagName(e.t)); return parts[2] + ', question ' + (parseInt(parts[3], 10) + 1) + ': ' + bits.join(', ') + ' (' + e.by + ')'; });
    const impact = [
      ['Onboarding gates', 'Board 8, Onboarding', 'Gate 3, office address evidence, starts from the "Your office" answers: address, own or rent, and the landlord, who is asked for the letter straight away. Gate 1, company and directors, uses the reworded director question.', 'Onboarding.dc.html'],
      ['Form checks', 'Board 13, Form received', 'New check rows: office address against the tenancy or lease and the landlord letter. The legal entity check compares Companies House only, because the form no longer asks it.', 'FormStaff.dc.html'],
      ['CQC application sheet', 'Board 13, Form received', '"Type of legal entity" is filled from Companies House. The location address and how the office is held come from "Your office". Copy buttons stay the same.', 'FormStaff.dc.html'],
      ['Questions inbox suggested replies', 'Board 67, Questions', 'Suggested replies follow the form\'s help text. 2 change: the director question and the new office help text. 6 past questions about the office address are now answered by the help text.', 'Questions.dc.html'],
      ['Add a client form preview', 'Board 51, Add a client', 'For CQC packages, "Your office" is added as a new section and Company Information drops to 9 questions. Until v8 is live it shows v7 with a note about v8.', 'AddClient.dc.html'],
      ['Client fix list and reminders', 'Client Hub and emails 2.3 to 2.5', 'Fix list wording for gate 3 uses the new help text. Reminder timings do not change (after 2 days and 4 days, then Grace calls on day 6).', 'Onboarding.dc.html']
    ].map(([where, board, what, href]) => ({ where, board, what, href, aria: 'Open ' + where }));
    const HC = [
      ['oh', 'Oak Hollow Care Ltd', 'CQC registration, supported living. Stopped at section 8 of 13 (Reference Details), last answer Tue 27 Oct', 'If moved: answers kept. "Your office" is added before the pages still to do, and the reworded director question shows on the Directors page for a quick check.'],
      ['hl', 'Harbour Lane Care Ltd', 'Full start-up, domiciliary care. Form arrived Thu 29 Oct; the fix list reopens 2 answers (second director, CV gap)', 'If moved: "Your office" is filled in from gate 3 (Flat 2, 14 Harbour Road, rented, landlord Tom Reid already asked) for Amara to check. Her fix list stays exactly 2 items.'],
      ['mv', 'Meadow View Care Ltd', 'Full start-up, domiciliary care. Deal won in GoHighLevel; paying today. The form goes out after Divine\'s introduction call', 'If v8 is approved before the call, Ade starts on v8 and is never moved. Otherwise moving keeps any answers.']
    ];
    const movedN = HC.filter(h => s.moved[h[0]]).length;
    const stay = HC.length - movedN;
    const half = HC.map(([id, name, where, after]) => { const m = !!s.moved[id]; return { name, where, after: m ? 'Moved to v8 just now. Answers kept. ' + (id === 'mv' ? 'No message needed: the form has not gone out yet.' : 'The message below was sent.') : after, ver: m ? 'v8' : 'On v7', cls: 'sb-chip ' + (m ? 'c-ok' : 'c-neutral'), canMove: live8 && !m, move: () => this.setState({ moved: Object.assign({}, s.moved, { [id]: true }) }) }; });
    const MSG = {
      oh: ['Lena Brooks, Oak Hollow Care Ltd', 'We have made your onboarding form a little easier', ['Hi Lena,', 'We have improved our onboarding form. Everything you have already answered is saved.', 'There is one new page, "Your office", with 5 short questions about where you will run the service. We have taken out the question about your type of company, because we read it from Companies House.', 'You can carry on from where you stopped, at Reference Details. If anything is unclear, press "Not sure? Ask us" on any question.', 'Grace, Care Sync Experts']],
      hl: ['Amara Okafor, Harbour Lane Care Ltd', 'One new page to check in your onboarding form', ['Hi Amara,', 'We have improved our onboarding form. Your answers are saved.', 'There is a new page, "Your office". We have filled it in from what you already told us (Flat 2, 14 Harbour Road, rented). Please check it. We have already asked Tom Reid for the landlord letter, so there is nothing to chase.', 'Your 2 fixes are unchanged: Kwame Okafor\'s details as second director, and one line about the gap on Ruth\'s CV.', 'Grace, Care Sync Experts']],
      mv: ['Ade Ola, Meadow View Care Ltd', 'No message', ['Ade has not been sent the form yet, so there is nothing to tell them. They simply get the version that is live when Divine\'s call ends.']]
    };
    const m = MSG[s.msgFor];
    const msg = { subjectK: 'To ' + m[0], subject: m[1], lines: m[2] };
    // Approval: Grace drafted; anyone who edited the draft cannot approve it.
    const dpPending = s.dpNeed.length > 0 && !s.dpOk;
    const meEdited = s.editors.indexOf(ME) >= 0;
    const canApprove = isCqc && s.v8 === 'waiting' && !meEdited && !dpPending;
    const AP = {
      waiting: ['Waiting for a super admin: Collins or Rachel Turner', 'Grace drafted v8, so either super admin may approve it, unless they edited it too. Decision 4 on super admin Home.'],
      back: ['Sent back to Grace', 'Grace sees your note in her tasks and can send it again. Decision 4 leaves super admin Home until she does.'],
      live: ['v8 is live from just now', '']
    };
    const liveNote = 'Approved by ' + (s.decided || ME) + '. ' + (s.roll === 'move' ? 'New clients get v8, and the 3 clients on v7 were moved with their answers kept.' : 'New clients get v8. The 3 clients on v7 stay on it until you move them.') + ' Written to the audit log, with v7 kept for the record.';
    const cannotText = s.v8 !== 'waiting' ? '' : (meEdited ? 'You edited this draft, so you cannot approve it. ' + (ME === 'Collins' ? 'Rachel Turner' : 'Collins') + ' approves it. Switch at the top to try.' : (dpPending ? 'Approval opens once the data protection lead agrees.' : ''));
    const approve = () => { if (!s.apReason.trim()) { this.setState({ apErr: true }); return; } const moved = s.roll === 'move' ? { oh: true, hl: true, mv: true } : s.moved; this.setState({ v8: 'live', decided: ME, apErr: false, moved, ver: 'v8' }); };
    const T = [['changes', 'Changes'], ['impact', 'Impact'], ['clients', 'Clients on v7 (' + stay + ')'], ['msg', 'Message to moved clients']];
    const USED = { cqc: 'Used by: CQC registration, domiciliary care; CQC registration, supported living; Full start-up package. Grace owns every form question.', ciw: 'Used by: CIW registration (Wales).', rqia: 'Used by: RQIA registration (Northern Ireland).', tender: 'Used by: Tender writing, and every tender package.' };
    return {
      theme: this.props.theme ?? 'light', three: 3, n16: 16, nav: __NAV__,
      user: s.as === 'collins' ? { name: 'Collins', initials: 'C' } : { name: 'Rachel Turner', initials: 'RT' },
      asTabs: [['collins', 'Collins'], ['rachel', 'Rachel Turner (super admin 2)']].map(([k, label]) => ({ label, on: s.as === k, off: s.as !== k, pick: () => this.setState({ as: k, openQ: '' }) })),
      status: isD ? 'Draft add-on form, not live yet' : (verOf(s.form) + ', ' + MATCH[s.form]), statusCls: 'sb-chip ' + (isD ? 'c-warn' : 'c-ok'),
      usedBy: isD ? 'Used by: ' + all[s.form][0] + ' (' + all[s.form][1] + '). Not offered to clients until the form, price and journey are ready.' : USED[s.form],
      forms, pages, pageCount: pages.length + ' pages',
      verTabs: (live8 ? [['v8', 'Live v8']] : [['v7', 'Live v7'], ['v8', 'Draft v8']]).map(([k, label]) => ({ label, on: showVer === k, off: showVer !== k, pick: () => this.setState({ ver: k, page: 0, openQ: '', saved: '' }) })),
      cur: { name: c[0], when: c[2], ver: isD ? 'Draft' : (isCqc ? (showVer === 'v8' ? (live8 ? 'Live v8' : 'Draft v8') : 'Live v7') : verOf(s.form)) },
      qs, edW: s.edW, edH: s.edH, edErr: s.edErr, edDp,
      edNote: isCqc ? 'Editing draft v8. The live version does not change until v8 is approved.' : (isD ? 'Editing this draft add-on form.' : 'Changes go into a new draft for Grace. The live version does not change.'),
      onEdW: e => this.setState({ edW: e.target.value, edErr: false }), onEdH: e => this.setState({ edH: e.target.value }),
      valTabs: VALS.map(([k, label]) => ({ label, on: s.edV === k, off: s.edV !== k, pick: () => this.setState({ edV: k }) })),
      tagTabs: TAGS.map(([k, label]) => ({ label, on: s.edT === k, off: s.edT !== k, pick: () => this.setState({ edT: k }) })),
      tagHelp: { business: 'About the company, not a person.', personal: 'About a named person: kept as the retention schedule says.', special: 'Health and other special category data: only people who need it can see it.', criminal: 'DBS and offence information: seen by named staff only, images deleted once the regulator decides (proposed).', credential: 'A login or code: never kept in form answers. It goes to the vault, and every reveal needs a reason.' }[s.edT] || '',
      edSave, edSaveLabel: 'Save to ' + draftName, edCancel: () => this.setState({ openQ: '' }),
      savedMsg: !!s.saved, savedText: s.saved,
      pv, pvVer: isCqc ? (showVer === 'v8' ? (live8 ? 'Live v8' : 'Draft v8') : 'Live v7') : (isD ? 'Draft' : verOf(s.form)),
      isCqc, isDraft: isD, isOtherLive: !isD && !isCqc,
      draftNote: 'Drafted by Grace from the add-on list in Add a client. These questions are not on any Google Form yet, so they need agreeing with the team. A super admin who did not draft it approves it before any client gets it.',
      verLine: verOf(s.form) + ', ' + MATCH[s.form] + '.', otherNote: 'No draft open. Editing a question starts a draft for Grace.',
      liveChip: live8 ? 'Live v8' : 'Live v7, matches the Google Form', liveChipCls: 'sb-chip c-ok',
      draftChip: live8 ? 'v7 kept for the record' : (s.v8 === 'back' ? 'Draft v8: back with Grace' : 'Draft v8: waiting for approval'), draftChipCls: 'sb-chip ' + (live8 ? 'c-neutral' : 'c-warn'),
      v8Tabs: T.map(([k, label]) => ({ label, on: s.tab === k, off: s.tab !== k, pick: () => this.setState({ tab: k }) })),
      tChanges: s.tab === 'changes', tImpact: s.tab === 'impact', tClients: s.tab === 'clients', tMsg: s.tab === 'msg',
      v8Title: live8 ? 'CQC form: v8 is live' : (s.v8 === 'back' ? 'CQC form: draft v8, back with Grace' : 'CQC form: draft v8'),
      changes, myEdits, hasMyEdits: myEdits.length > 0, editorLine: 'Also changed in this draft by ' + s.editors.join(' and '), impact,
      halfTitle: 'On v7 and not finished: ' + stay + (stay === 1 ? ' client' : ' clients'),
      halfNote: live8 ? 'Move a client to v8 and their answers are kept; only the new page is added. They get the message on the last tab.' : 'Nobody is moved while v8 waits for approval. Once it is live you can move them, keeping their answers.',
      half, canMoveAll: live8 && stay > 0, moveAll: () => this.setState({ moved: { oh: true, hl: true, mv: true } }),
      msgTabs: [['oh', 'Oak Hollow'], ['hl', 'Harbour Lane'], ['mv', 'Meadow View']].map(([k, label]) => ({ label, on: s.msgFor === k, off: s.msgFor !== k, pick: () => this.setState({ msgFor: k }) })), msg,
      apTitle: AP[s.v8][0], apNote: s.v8 === 'live' ? liveNote : AP[s.v8][1],
      apChip: s.v8 === 'live' ? 'Approved' : (s.v8 === 'back' ? 'With Grace' : 'Waiting'), apChipCls: 'sb-chip ' + (s.v8 === 'live' ? 'c-ok' : (s.v8 === 'back' ? 'c-neutral' : 'c-warn')),
      needDp: s.dpNeed.length > 0 && s.v8 === 'waiting', canDp: dpPending && s.as === 'collins',
      dpText: s.dpOk ? 'Agreed by Collins, data protection lead, just now.' : (s.dpNeed.length + (s.dpNeed.length === 1 ? ' question now collects' : ' questions now collect') + ' special category, criminal offence or credential data. Collins, data protection lead, must agree first.' + (s.as === 'collins' ? '' : ' Switch to Collins at the top to try.')),
      dpAgree: () => this.setState({ dpOk: true }),
      canApprove, rollTabs: [['new', 'New clients only'], ['move', 'New clients, and move the 3 on v7 now']].map(([k, label]) => ({ label, on: s.roll === k, off: s.roll !== k, pick: () => this.setState({ roll: k }) })),
      apReason: s.apReason, apErr: s.apErr, onApReason: e => this.setState({ apReason: e.target.value, apErr: false }),
      approve, back: () => this.setState({ v8: 'back' }),
      cannotNote: !!cannotText, cannotText, isLive: s.v8 !== 'waiting',
      undoLive: () => this.setState({ v8: 'waiting', moved: {}, decided: '', apReason: '' })
    };
  }
}'''
H['fb'] = 1980
build_sa(OUT + '/FormBuilder.dc.html', 'Forms', 'Forms', H['fb'], B_FB, S_FB, 'forms', CSS + FB_CSS)

# ---------------------------------------------------------------- 4. Price book (super admin menu, board 77)
B_PB = '''      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 4px; max-width: 800px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Price book</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Every package and add-on, with VAT, instalments, where each price is used, and its history. Anyone may suggest a price; only a super admin enters it, and the other super admin approves it. Anything not set says "Price to set" and nobody quotes it.</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px; align-items: flex-start;">
          <span class="bz-lbl">You are acting as</span>
          ''' + tabs('asTabs', 'Acting as') + '''
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="4">
          <div class="sb-card sb-kpi"><span class="sb-muted">{{k.k}}</span><span class="sb-kv">{{k.v}}</span><span class="sb-sub">{{k.note}}</span></div>
        </sc-for>
      </div>

      <div class="bz-box" style="flex-direction: row; gap: 10px; align-items: flex-start;"><x-import component-from-global-scope="CareSync.Icon" name="info" size="{{n20}}"></x-import><span>{{infoText}} <a href="SuperAdmin.dc.html" style="color: var(--cs-text-brand); font-weight: 500;">Open super admin Home</a></span></div>

      <section class="sb-card" aria-labelledby="pr-h">
        <div class="sb-head"><h2 id="pr-h" class="sb-h2">Packages and add-ons</h2><span class="sb-sub">Try it: change a price and its instalments, then approve it as the other super admin</span></div>
        <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 2 1 250px;">Package or add-on</span><span class="sb-th" style="flex: 0 0 100px;">Price</span><span class="sb-th" style="flex: 0 0 76px;">VAT</span><span class="sb-th" style="flex: 1 1 250px;">Instalments</span><span class="sb-th" style="flex: 0 0 136px;">Status</span><span class="sb-th" style="flex: 0 0 246px;"></span></div>
        <sc-for list="{{groups}}" as="g" hint-placeholder-count="3">
          <div class="bz-gh">{{g.label}}</div>
          <sc-for list="{{g.rows}}" as="r" hint-placeholder-count="5">
            <div style="border-top: 1px solid var(--cs-border-subtle);">
              <div class="sb-row" style="border-top: 0; align-items: flex-start;">
                <span style="flex: 2 1 250px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{r.name}}</span><span class="sb-muted">{{r.what}}</span></span>
                <span style="flex: 0 0 100px;" class="{{r.priceCls}}">{{r.price}}</span>
                <span style="flex: 0 0 76px;" class="sb-sub">{{r.vat}}</span>
                <span style="flex: 1 1 250px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="sb-sub">{{r.stages}}</span><sc-for list="{{r.parts}}" as="pt" hint-placeholder-count="2"><span class="sb-sub">{{pt}}</span></sc-for></span>
                <span style="flex: 0 0 136px; display: flex; flex-direction: column; gap: 4px;"><span class="{{r.stCls}}" style="white-space: normal; align-self: flex-start;">{{r.status}}</span><span class="sb-muted">{{r.eff}}</span></span>
                <span style="flex: 0 0 246px; display: flex; gap: 6px; justify-content: flex-end; flex-wrap: wrap;"><sc-if value="{{r.canEdit}}" hint-placeholder-val="{{ true }}"><button class="sb-btn b-sec" onClick="{{r.edit}}" aria-label="{{r.editAria}}">{{r.editLabel}}</button></sc-if><button class="sb-btn b-gh" onClick="{{r.used}}" aria-label="{{r.usedAria}}" aria-expanded="{{r.usedExp}}">Used in</button><button class="sb-btn b-gh" onClick="{{r.hist}}" aria-label="{{r.histAria}}" aria-expanded="{{r.histExp}}">History</button></span>
              </div>
              <sc-if value="{{r.editing}}" hint-placeholder-val="{{ false }}">
                <div style="margin: 0 20px 14px; padding: 14px; border-radius: 10px; border: 2px solid var(--cs-action-primary); display: flex; flex-direction: column; gap: 12px;">
                  <span class="bz-b">{{r.editTitle}}</span>
                  <div style="display: flex; gap: 16px; flex-wrap: wrap; align-items: flex-end;">
                    <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">New price in pounds</span><input class="bz-in" style="width: 150px;" value="{{fPrice}}" onChange="{{onPrice}}" placeholder="{{r.pricePh}}"></label>
                    <span style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">VAT</span>''' + tabs('vatTabs', 'VAT') + '''</span>
                    <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">Effective from (new clients only)</span><input class="bz-in" style="width: 190px;" value="{{fEff}}" onChange="{{onEff}}"></label>
                  </div>
                  <div style="display: flex; flex-direction: column; gap: 8px; padding: 12px; border-radius: 10px; background: var(--cs-surface-subtle);">
                    <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center; flex-wrap: wrap;"><span class="bz-b">Instalments</span><span style="display: flex; gap: 6px; align-items: center;"><span class="bz-lbl">How many</span>''' + tabs('nTabs', 'Number of instalments') + '''</span></div>
                    <sc-for list="{{inst}}" as="it" hint-placeholder-count="2">
                      <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap; padding: 6px 0; border-top: 1px solid var(--cs-border-subtle);">
                        <span class="bz-b" style="flex: 0 0 52px;">{{it.n}}</span>
                        <label style="display: flex; gap: 6px; align-items: center;"><input class="bz-in" style="width: 84px;" value="{{it.pct}}" onChange="{{it.onPct}}" aria-label="{{it.pctAria}}"><span class="sb-sub">%</span></label>
                        <span style="display: flex; gap: 6px; flex-wrap: wrap; flex: 1 1 420px;"><sc-for list="{{it.whens}}" as="w" hint-placeholder-count="5"><sc-if value="{{w.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" aria-pressed="true" onClick="{{w.pick}}">{{w.label}}</button></sc-if><sc-if value="{{w.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" aria-pressed="false" onClick="{{w.pick}}">{{w.label}}</button></sc-if></sc-for></span>
                        <span class="bz-b" style="flex: 0 0 150px; text-align: right;">{{it.amt}}</span>
                      </div>
                    </sc-for>
                    <span class="{{instCheckCls}}">{{instCheck}}</span>
                    <button class="sb-btn b-gh" style="align-self: flex-start;" onClick="{{equalise}}">Split equally</button>
                  </div>
                  <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">Reason (written to the audit log)</span><textarea class="bz-ta" value="{{fReason}}" onChange="{{onReason}}" placeholder="For example: more policies now included"></textarea></label>
                  <sc-if value="{{fErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">{{fErrText}}</span></sc-if>
                  <div style="display: flex; gap: 8px;"><button class="sb-btn b-pri" onClick="{{submit}}">Send to the other super admin</button><button class="sb-btn b-gh" onClick="{{cancel}}">Cancel</button></div>
                </div>
              </sc-if>
              <sc-if value="{{r.pending}}" hint-placeholder-val="{{ false }}">
                <div class="bz-amb" style="margin: 0 20px 14px;">
                  <span class="bz-b">{{r.pendText}}</span>
                  <span class="sb-sub">{{r.pendPlan}}</span>
                  <span class="sb-sub">{{r.pendReason}}</span>
                  <sc-if value="{{r.mine}}" hint-placeholder-val="{{ false }}"><span class="sb-sub">{{r.mineText}}</span></sc-if>
                  <sc-if value="{{r.canApprove}}" hint-placeholder-val="{{ false }}">
                    <textarea class="bz-ta" aria-label="Reason for your decision" value="{{r.apReason}}" onChange="{{r.onApReason}}" placeholder="Your reason (written to the audit log)"></textarea>
                    <sc-if value="{{r.apErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Write a reason first.</span></sc-if>
                    <span style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{r.approve}}">{{r.approveLabel}}</button><button class="sb-btn b-gh" onClick="{{r.decline}}">Decline</button></span>
                  </sc-if>
                </div>
              </sc-if>
              <sc-if value="{{r.showUsed}}" hint-placeholder-val="{{ false }}">
                <div class="bz-box" style="margin: 0 20px 14px; gap: 4px;">
                  <span class="bz-lbl">Where this price is used</span>
                  <sc-for list="{{r.usedIn}}" as="u" hint-placeholder-count="9"><div style="display: flex; gap: 12px; font-size: 13px; line-height: 18px; padding: 3px 0;"><span class="bz-b" style="flex: 0 0 230px;">{{u.where}}</span><span class="sb-sub" style="flex: 1; min-width: 0;">{{u.what}}</span></div></sc-for>
                  <span class="sb-sub" style="padding-top: 4px;">{{r.affected}}</span>
                </div>
              </sc-if>
              <sc-if value="{{r.showHist}}" hint-placeholder-val="{{ false }}">
                <div class="bz-box" style="margin: 0 20px 14px;">
                  <span class="bz-lbl">History</span>
                  <sc-for list="{{r.history}}" as="h" hint-placeholder-count="2"><span style="font-size: 13px; line-height: 18px;">{{h}}</span></sc-for>
                </div>
              </sc-if>
            </div>
          </sc-for>
        </sc-for>
      </section>

      <section class="sb-card" aria-labelledby="dc-h">
        <div class="sb-head"><h2 id="dc-h" class="sb-h2">{{discLeft}}</h2><span class="sb-sub">Asked from Add a client or a client record, with an amount and a reason. A super admin who did not ask decides</span></div>
        <sc-for list="{{discounts}}" as="d" hint-placeholder-count="2">
          <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px;">
            <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center; flex-wrap: wrap;"><span class="bz-b">{{d.title}}</span><span style="display: flex; gap: 8px; align-items: center;"><span class="sb-chip c-neutral">{{d.num}}</span><span class="{{d.chipCls}}">{{d.chip}}</span></span></div>
            <span>{{d.ask}}</span>
            <span class="sb-sub">{{d.why}}</span>
            <sc-if value="{{d.open}}" hint-placeholder-val="{{ true }}">
              <textarea class="bz-ta" aria-label="{{d.taLabel}}" value="{{d.reason}}" onChange="{{d.onReason}}" placeholder="Your reason (written to the audit log)"></textarea>
              <sc-if value="{{d.err}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Write a reason first.</span></sc-if>
              <span style="display: flex; gap: 8px;"><button class="sb-btn b-pri" onClick="{{d.approve}}">Approve the discount</button><button class="sb-btn b-gh" onClick="{{d.decline}}">Decline</button></span>
            </sc-if>
            <sc-if value="{{d.done}}" hint-placeholder-val="{{ false }}"><div class="{{d.doneBox}}"><span class="bz-b">{{d.doneText}}</span><span class="sb-sub">{{d.doneNote}}</span><button class="sb-btn b-gh" style="align-self: flex-start;" onClick="{{d.undo}}">Change my decision</button></div></sc-if>
            <div style="display: flex; flex-direction: column; gap: 0; border-radius: 10px; border: 1px solid var(--cs-border-subtle);">
              <div class="bz-gh" style="border-top: 0;">{{d.flowTitle}}</div>
              <sc-for list="{{d.flow}}" as="f" hint-placeholder-count="5"><div style="display: flex; gap: 12px; padding: 6px 20px; font-size: 13px; line-height: 18px; border-top: 1px solid var(--cs-border-subtle);"><span class="bz-b" style="flex: 0 0 230px;">{{f.where}}</span><span class="sb-sub" style="flex: 1; min-width: 0;">{{f.what}}</span></div></sc-for>
            </div>
          </div>
        </sc-for>
        <div class="sb-row"><span class="sb-muted">The price book itself never changes for a discount. Discounts given are listed in Money and exports (board 87) for the accountant.</span></div>
      </section>
'''
S_PB = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { as: 'me', edit: '', fPrice: '', fVat: '+ VAT', fEff: 'Mon 16 Nov 2026', fReason: '', fErr: '', fN: 2, fPct: ['50', '50'], fWhen: [0, 3], fEqual: true,
      pend: { full: { price: 850000, vat: '+ VAT', eff: 'Mon 2 Nov 2026', reason: 'Checked price for the full start-up package. Rachel to confirm £8,500 rather than £8,000 before it is approved', by: 'Collins', n: 3, pct: null, when: [0, 2, 3] } },
      upd: {}, hist: {}, used: {}, apReason: {}, apErr: {}, disc: {}, dReason: {}, dErr: {} };
  }
  renderVals() {
    const s = this.state;
    const C = (id, fb) => (window.CSR ? window.CSR.get(id, fb) : fb);
    const VAT = Number(C('vat-rate', 20));
    const WHEN = ['At accept, sign and pay', 'At handover approval', 'At final pack sign-off', 'When the application is submitted', 'At signing', 'Before submission'];
    const PLAN = { two: [2, [0, 3]], three: [3, [0, 2, 3]], tender: [2, [4, 5]], one: [1, [0]] };
    const pounds = (p, dec) => '£' + (p / 100).toLocaleString('en-GB', { minimumFractionDigits: dec ? 2 : 0, maximumFractionDigits: dec ? 2 : 0 });
    const split = (total, n, pct) => {
      if (!pct) { const base = Math.floor(total / n); return Array.from({ length: n }, (x, i) => i < n - 1 ? base : total - base * (n - 1)); }
      let used = 0; return pct.map((p, i) => { if (i === n - 1) return total - used; const a = Math.floor(total * Number(p) / 100); used += a; return a; });
    };
    const amtsText = (total, n, pct, when, vat, from, short) => { const a = split(total, n, pct); const dec = a.some(x => x % 100 !== 0); return a.map((x, i) => (short ? '' : (i + 1) + ' of ' + n + ': ') + (from ? 'from ' : '') + pounds(x, dec) + (vat === '+ VAT' ? ' + VAT' : '') + ', ' + WHEN[when[i]].toLowerCase()); };
    const P = id => Math.round(Number(C(id, 0)) * 100);
    // [id, name, what, pence or null, vat, plan, status, eff, history, extra used, signed this year]
    const R = [
      ['reg', 'Registration packages', [
        ['dom', 'CQC registration: domiciliary care', 'England. Every policy and document, 3 sessions with Millicent, every CQC letter answered', P('price-dom'), '+ VAT', 'two', 'live', '1 Oct 2026', ['1 Oct 2026: £4,000 + VAT, set in setup mode by Collins before go-live'], 18],
        ['sl', 'CQC registration: supported living', 'England. Includes the easy read guide and the financial viability statement', P('price-sl'), '+ VAT', 'two', 'live', '1 Oct 2026', ['1 Oct 2026: £5,000 + VAT, set in setup mode by Collins before go-live'], 7],
        ['ciw', 'CIW registration (Wales)', 'The ten CIW Online policies, Statement of Purpose, Active Offer in every document', P('price-ciw'), '+ VAT', 'two', 'live', '1 Oct 2026', ['1 Oct 2026: £4,500 + VAT, set in setup mode by Collins before go-live'], 4],
        ['rqia', 'RQIA registration (Northern Ireland)', 'Ten core policies mapped to the Minimum Standards', P('price-rqia'), '+ VAT', 'two', 'live', '1 Oct 2026', ['1 Oct 2026: £4,500 + VAT, set in setup mode by Collins before go-live', 'Before: £3,500 in the old package document, now out of date'], 3],
        ['full', 'Full start-up package', 'Company set-up, branding, website, business plan, registration, and 12 months of aftercare (the only package that includes aftercare)', P('price-full'), '+ VAT', 'three', 'check', '1 Oct 2026', ['2 Nov 2026: £8,500 + VAT entered by Collins as the checked price. Waiting for Rachel Turner', '1 Oct 2026: £8,500 + VAT, set in setup mode by Collins, marked "to check against £8,000"'], 6]
      ]],
      ['add', 'Add-ons and single services', [
        ['sladd', 'Supported living add-on', 'Adding supported living to a CQC registration. Policies quoted separately', P('price-sl-addon'), 'incl. VAT', 'one', 'live', '1 Oct 2026', ['1 Oct 2026: £1,500 including VAT, set in setup mode by Collins'], 0],
        ['int', 'CQC interview preparation', 'Practice sessions with Millicent (number set on the package) and the Interview Preparation Hub', P('price-interview'), 'incl. VAT', 'one', 'live', '1 Oct 2026', ['1 Oct 2026: £750 including VAT, set in setup mode by Collins'], 0],
        ['pir', 'PIR writing', 'Per PIR, one PIR per service type', P('price-pir'), '+ VAT', 'one', 'live', '1 Nov 2026', ['30 Oct 2026: wording now "per PIR, one PIR per service type". Suggested by Grace, entered by Collins, approved by Rachel Turner. From 1 Nov, new clients only', '1 Oct 2026: £750 + VAT, set in setup mode by Collins'], 0],
        ['after', 'Aftercare, 12 months', 'For registration-only clients. Included in the full start-up package', null, '', 'one', 'set', '', ['No price set yet. Decided 4 Nov: registration-only clients can buy aftercare as an add-on'], 0],
        ['extra', 'Extra sessions', 'Sessions beyond those included in a package', null, '', 'one', 'set', '', ['No price set yet'], 0],
        ['single', 'Single services', 'For example a policy refresh or a business plan', 50000, '+ VAT', 'one', 'from', '1 Oct 2026', ['1 Oct 2026: from £500 + VAT, 1 payment in full'], 0],
        ['rebrand', 'Policy rebrand, branding and business forms', 'Single service', 50000, '+ VAT', 'one', 'confirm', '1 Oct 2026', ['1 Oct 2026: from £500 + VAT, still to confirm. Not quoted above "from £500" until confirmed'], 0],
        ['var', 'Registration variation', 'Adding a location, a service or a band. Its form is still a draft', null, '', 'one', 'set', '', ['No price set yet'], 0],
        ['mock', 'Mock inspection', 'For registration-only clients. Included in the full start-up package', null, '', 'one', 'set', '', ['No price set yet'], 0],
        ['web', 'Website or marketing', 'Website, search and Google profile', null, '', 'one', 'quote', '', ['Quoted for each client'], 0]
      ]],
      ['ten', 'Tenders', [
        ['tender', 'Tender writing', 'Full quotation after we review the tender', P('price-tender-from'), '+ VAT', 'tender', 'from', '1 Oct 2026', ['1 Oct 2026: from £1,500 + VAT, set in setup mode by Collins'], 0],
        ['bid', 'Bid review', 'For a bid the client wrote. Around £500', 50000, 'To confirm', 'one', 'vat', '', ['Around £500. VAT still to confirm'], 0],
        ['ret', 'Retained tender package', 'Several bids a year. Never promise a lower rate', null, '', 'one', 'set', '', ['No price set yet'], 0],
        ['fw', 'Framework or dynamic purchasing application', 'Often shorter than a full tender', null, '', 'one', 'set', '', ['No price set yet'], 0],
        ['pol', 'Policy writing for a tender', 'Extra to the tender fee. Quoted for each tender', null, '', 'one', 'quote', '', ['Quoted for each tender'], 0]
      ]]
    ];
    const who = s.as === 'me' ? 'Collins' : 'Rachel Turner';
    const other = s.as === 'me' ? 'Rachel Turner' : 'Collins';
    const ST = { live: ['Live', 'c-ok'], from: ['Live, from price', 'c-ok'], check: ['Check: £8,500 or £8,000', 'c-warn'], set: ['Price to set', 'c-warn'], quote: ['Quote per client', 'c-neutral'], vat: ['VAT to confirm', 'c-warn'], confirm: ['To confirm', 'c-warn'] };
    const USED = [
      ['Add a client (board 51)', 'Package list, total and instalments'],
      ['Plan and costs (board 60, client Hub)', 'The client\'s price and payment stages'],
      ['Account (board 29, client Hub)', 'Invoices and receipts'],
      ['Packages and journeys (board 81)', 'The package record'],
      ['Manager dashboard (board 43)', 'Revenue by package, instalments due'],
      ['Money and exports (board 87)', 'VAT split, accountant export, discounts given'],
      ['Agreement (DocuSeal)', 'Price and payment stages the client signs'],
      ['Stripe instalments', 'Each amount and the moment it is taken'],
      ['Xero invoice', 'Invoice lines and VAT, synced every hour']
    ];
    let live = 0, toSet = 0;
    const groups = R.map(([gk, label, rows]) => ({ label, rows: rows.map(([id, name, what, pence0, vat0, plan0, st0, eff0, h0, signed]) => {
      const u = s.upd[id] || {}; const p = s.pend[id];
      const pence = u.price !== undefined ? u.price : pence0, vat = u.vat || vat0, eff = u.eff || eff0;
      const st = u.price !== undefined ? 'live' : st0;
      const n = u.n || PLAN[plan0][0], when = u.when || PLAN[plan0][1], pct = u.n ? u.pct : null;
      if (['live', 'from', 'check'].indexOf(st) >= 0) live++; if (st === 'set') toSet++;
      const from = st === 'from' || st === 'confirm' || st0 === 'from';
      const priced = pence !== null && st !== 'quote';
      const history = (u.hist || []).concat(h0);
      const price = priced ? (from ? 'From ' : (st === 'vat' ? 'Around ' : '')) + pounds(pence, pence % 100 !== 0) : (st === 'quote' ? 'Quote' : 'Price to set');
      const parts = priced && st !== 'vat' ? amtsText(pence, n, pct, when, vat, from, true).map(t => t.charAt(0).toUpperCase() + t.slice(1)) : [];
      const stages = !priced ? (st === 'quote' ? 'Agreed with each quote' : 'Set with the price') : (st === 'vat' ? 'To set with the VAT' : (n === 1 ? '1 payment in full' : n + ' instalments' + (pct ? ' (custom split)' : '')));
      const pendText = !p ? '' : (id === 'full' && priced && p.price === pence && p.vat === vat ? 'Waiting for ' + (p.by === 'Collins' ? 'Rachel Turner' : 'Collins') + ' to confirm ' + price + ' ' + vat + ' as the checked price (rather than £8,000), from ' + p.eff + '. Entered by ' + p.by + '.' : 'Waiting for ' + (p.by === 'Collins' ? 'Rachel Turner' : 'Collins') + ': ' + (priced ? price + ' ' + vat : 'no price') + ' to ' + pounds(p.price, p.price % 100 !== 0) + ' ' + p.vat + ', from ' + p.eff + '. Entered by ' + p.by + '.');
      const affected = signed ? 'Clients affected today: none. A new price applies to new clients only, from its date. The ' + signed + ' clients who signed this year keep the price in their agreement.' : 'Clients affected today: none. A new price applies to new clients only, from its date. Anyone who already bought it keeps their price.';
      const usedIn = USED.concat(id === 'full' ? [['Aftercare (board 30)', '12 months included'], ['Go-live readiness (board 79)', 'Full start-up price check']] : (id === 'tender' ? [['Tender record', 'The quote for each bid']] : [])).map(([where, w]) => ({ where, what: w }));
      return { name, what, price, priceCls: priced ? 'bz-b' : 'sb-sub', vat: priced ? vat : ' ', stages, parts,
        status: p ? 'Waiting for ' + (p.by === 'Collins' ? 'Rachel Turner' : 'Collins') : ST[st][0], stCls: 'sb-chip ' + (p ? 'c-warn' : ST[st][1]), eff: eff ? 'From ' + eff : (st === 'quote' ? 'Quoted each time' : 'Not set'),
        canEdit: !p && s.edit !== id && st !== 'quote', editLabel: priced && st !== 'vat' ? 'Change' : 'Set a price', editAria: (priced ? 'Change the price of ' : 'Set a price for ') + name,
        edit: () => { const ww = when.slice(); this.setState({ edit: id, fPrice: '', fVat: vat0 && vat0 !== 'To confirm' ? vat0 : '+ VAT', fEff: 'Mon 16 Nov 2026', fReason: '', fErr: '', fN: n, fWhen: ww, fPct: pct ? pct.slice() : Array.from({ length: n }, () => (100 / n).toFixed(2).replace(/\.00$/, '')), fEqual: !pct, editBase: pence || 0 }); },
        editing: s.edit === id, editTitle: (priced ? 'Change ' + name + '. Now: ' + price + ' ' + vat + '.' : 'Set a price for ' + name + '.') + ' You enter it; ' + other + ' approves it.',
        pricePh: priced ? 'Now ' + (pence / 100) : 'For example 1200',
        used: () => this.setState({ used: Object.assign({}, s.used, { [id]: !s.used[id] }) }), usedAria: 'Where the price of ' + name + ' is used', usedExp: String(!!s.used[id]), showUsed: !!s.used[id], usedIn, affected,
        hist: () => this.setState({ hist: Object.assign({}, s.hist, { [id]: !s.hist[id] }) }), histAria: 'History of ' + name, histExp: String(!!s.hist[id]), showHist: !!s.hist[id], history,
        pending: !!p, pendText, pendPlan: p ? 'Instalments: ' + amtsText(p.price, p.n, p.pct, p.when, p.vat, false).join('; ') : '', pendReason: p ? 'Reason: "' + p.reason + '"' : '',
        mine: !!p && p.by === who, mineText: 'You entered this, so you cannot approve it. Only ' + other + ' can. Switch at the top to try.', canApprove: !!p && p.by !== who,
        approveLabel: p ? 'Approve ' + pounds(p.price, p.price % 100 !== 0) + ' ' + p.vat : '',
        apReason: s.apReason[id] || '', apErr: !!s.apErr[id], onApReason: e => this.setState({ apReason: Object.assign({}, s.apReason, { [id]: e.target.value }), apErr: Object.assign({}, s.apErr, { [id]: false }) }),
        approve: () => {
          const r = (s.apReason[id] || '').trim(); if (!r) { this.setState({ apErr: Object.assign({}, s.apErr, { [id]: true }) }); return; }
          const line = 'Just now: ' + pounds(p.price, p.price % 100 !== 0) + ' ' + p.vat + ' from ' + p.eff + '. Entered by ' + p.by + ', approved by ' + who + '. Reason: "' + r + '"';
          const np = Object.assign({}, s.pend); delete np[id];
          this.setState({ pend: np, upd: Object.assign({}, s.upd, { [id]: { price: p.price, vat: p.vat, eff: p.eff, n: p.n, pct: p.pct, when: p.when, hist: [line].concat(u.hist || []) } }), hist: Object.assign({}, s.hist, { [id]: true }) });
        },
        decline: () => {
          const r = (s.apReason[id] || '').trim(); if (!r) { this.setState({ apErr: Object.assign({}, s.apErr, { [id]: true }) }); return; }
          const line = 'Just now: ' + pounds(p.price, p.price % 100 !== 0) + ' ' + p.vat + ' declined by ' + who + '. Entered by ' + p.by + '. Reason: "' + r + '"';
          const np = Object.assign({}, s.pend); delete np[id];
          this.setState({ pend: np, upd: Object.assign({}, s.upd, { [id]: Object.assign({}, u, { hist: [line].concat(u.hist || []) }) }), hist: Object.assign({}, s.hist, { [id]: true }) });
        }
      };
    }) }));
    // Edit form: instalments with exact penny rounding.
    const fTotal = (() => { const v = parseFloat(String(s.fPrice).replace(/[^0-9.]/g, '')); return isNaN(v) ? (s.editBase || 0) : Math.round(v * 100); })();
    const pctNums = s.fPct.map(x => parseFloat(String(x).replace(/[^0-9.]/g, '')));
    const pctSum = Math.round(pctNums.reduce((a, b) => a + (isNaN(b) ? 0 : b), 0) * 1000) / 1000;
    const pctOk = s.fEqual || (pctNums.every(x => !isNaN(x) && x > 0) && Math.abs(pctSum - 100) < 0.001);
    const fAm = pctOk ? split(fTotal, s.fN, s.fEqual ? null : pctNums) : [];
    const dec = fAm.some(x => x % 100 !== 0);
    const vx = s.fVat === '+ VAT' ? ' + VAT' : (s.fVat === 'incl. VAT' ? ' incl. VAT' : '');
    const inst = Array.from({ length: s.fN }, (x, i) => ({ n: (i + 1) + ' of ' + s.fN, pct: s.fEqual ? (100 / s.fN).toFixed(2).replace(/\.00$/, '') : s.fPct[i], pctAria: 'Instalment ' + (i + 1) + ' percentage',
      onPct: e => { const fp = (s.fEqual ? Array.from({ length: s.fN }, () => (100 / s.fN).toFixed(2).replace(/\.00$/, '')) : s.fPct.slice()); fp[i] = e.target.value; this.setState({ fPct: fp, fEqual: false, fErr: '' }); },
      whens: WHEN.map((w, k) => ({ label: w, on: s.fWhen[i] === k, off: s.fWhen[i] !== k, pick: () => { const fw = s.fWhen.slice(); fw[i] = k; this.setState({ fWhen: fw }); } })),
      amt: pctOk && fTotal ? pounds(fAm[i], dec) + vx : 'Not worked out' }));
    const setN = n => { const base = [[0], [0, 3], [0, 2, 3], [0, 1, 2, 3]][n - 1]; this.setState({ fN: n, fWhen: base, fEqual: true, fPct: Array.from({ length: n }, () => (100 / n).toFixed(2).replace(/\.00$/, '')) }); };
    const instCheck = !fTotal ? 'Enter a price to see the amounts.' : (!pctOk ? 'The percentages add up to ' + pctSum + '%. They must add up to 100%.' : 'Adds up to ' + pounds(fTotal, true) + vx + ' exactly. Each amount is rounded down to the penny and the last instalment takes the rounding.' + (s.fVat === '+ VAT' ? ' VAT at ' + VAT + '% is added to each.' : ''));
    const submit = () => {
      const v = parseFloat(String(s.fPrice).replace(/[^0-9.]/g, ''));
      if (isNaN(v) || v <= 0) { this.setState({ fErr: 'Enter the new price in pounds.' }); return; }
      if (!pctOk) { this.setState({ fErr: 'The instalment percentages must add up to 100%.' }); return; }
      if (!s.fReason.trim()) { this.setState({ fErr: 'Write a reason first.' }); return; }
      this.setState({ pend: Object.assign({}, s.pend, { [s.edit]: { price: Math.round(v * 100), vat: s.fVat, eff: s.fEff.trim() || 'Mon 16 Nov 2026', reason: s.fReason.trim(), by: who, n: s.fN, pct: s.fEqual ? null : pctNums, when: s.fWhen.slice() } }), edit: '', fErr: '' });
    };
    // Discounts (decisions 2 and 3 on super admin Home)
    const vatOf = p => Math.round(p * VAT / 100);
    const DS = [
      ['lind', '2', 'Lindenfield Care Ltd: CQC registration: domiciliary care', P('price-dom'), 380000, 2, [0, 3], 'Asked by Jo Martin from Add a client, today 08:05.', 'Ready to sign today and price is the last blocker. Jo offered to trade scope first; the client wants the full package.', 'Jo Martin'],
      ['ashby', '3', 'Ashby Care: PIR writing for 2 service types', P('price-pir') * 2, 135000, 1, [0], 'Asked by Daniel Mensah from the client record, Fri 30 Oct.', 'Aftercare client, month 12, handover 18 Nov, happy. Both PIRs share most of the same evidence.', 'Daniel']
    ];
    const discounts = DS.map(([id, num, title, list, ask, n, when, by, why, asker]) => {
      const v = s.disc[id]; const r = s.dReason[id] || '';
      const off = list - ask;
      const go = val => { if (!r.trim()) { this.setState({ dErr: Object.assign({}, s.dErr, { [id]: true }) }); return; } this.setState({ disc: Object.assign({}, s.disc, { [id]: val }) }); };
      const am = split(ask, n, null); const dec = am.some(x => x % 100 !== 0) || true;
      const yes = v === 'yes';
      const flow = [
        ['Agreement (DocuSeal)', 'List price ' + pounds(list) + ' + VAT. Discount ' + pounds(off) + '. Agreed price ' + pounds(ask) + ' + VAT, with the approver\'s name and date.'],
        ['Stripe instalments', am.map((x, i) => (i + 1) + ' of ' + n + ': ' + pounds(x, dec) + ' + VAT ' + pounds(vatOf(x), true) + ' = ' + pounds(x + vatOf(x), true) + ', ' + WHEN[when[i]].toLowerCase()).join('. ')],
        ['Xero invoice', 'Line at the list price ' + pounds(list, true) + ', then "Discount agreed by Care Sync" ' + pounds(off, true) + ' off. VAT at ' + VAT + '% on ' + pounds(ask, true) + ': ' + pounds(vatOf(ask), true) + '. Total ' + pounds(ask + vatOf(ask), true) + '.'],
        ['Plan and costs (board 60)', 'The client sees "Your price: ' + pounds(ask) + ' + VAT. This includes a ' + pounds(off) + ' discount agreed by Care Sync."'],
        ['Money and exports (board 87)', 'Listed under discounts given: amount, client, who asked, who approved, reason.']
      ].map(([where, w]) => ({ where, what: w }));
      return { title, num: 'Decision ' + num + ' on Home', ask: 'Asks for ' + pounds(ask) + ' + VAT instead of ' + pounds(list) + ' + VAT (' + pounds(off) + ' off).', why: by + ' ' + why,
        open: !v, done: !!v, reason: r, err: !!s.dErr[id], taLabel: 'Reason for your decision on ' + title,
        onReason: e => this.setState({ dReason: Object.assign({}, s.dReason, { [id]: e.target.value }), dErr: Object.assign({}, s.dErr, { [id]: false }) }),
        approve: () => go('yes'), decline: () => go('no'), undo: () => { const d = Object.assign({}, s.disc); delete d[id]; this.setState({ disc: d }); },
        chip: !v ? 'Waiting' : (yes ? 'Approved' : 'Declined'), chipCls: 'sb-chip ' + (!v ? 'c-warn' : (yes ? 'c-ok' : 'c-neutral')),
        doneBox: yes ? 'bz-ok' : 'bz-box',
        doneText: (yes ? 'Approved' : 'Declined') + ' by ' + who + ', just now. ' + asker + ' is told, and decision ' + num + ' leaves super admin Home.',
        doneNote: 'Reason: "' + r.trim() + '". Written to the audit log.' + (yes ? ' The changes below are made now.' : ' The client is quoted the price book price.'),
        flowTitle: yes ? 'What changed when it was approved' : (v ? 'Nothing changes: the price book price stands' : 'If approved, this is what changes'), flow };
    });
    const nPend = Object.keys(s.pend).length;
    const nDisc = DS.filter(d => !s.disc[d[0]]).length;
    const vatOpts = ['+ VAT', 'incl. VAT'];
    return {
      theme: this.props.theme ?? 'light', three: 3, n20: 20, nav: __NAV__,
      user: s.as === 'me' ? { name: 'Collins', initials: 'C' } : { name: 'Rachel Turner', initials: 'RT' },
      asTabs: [['me', 'Collins'], ['second', 'Rachel Turner (super admin 2)']].map(([k, label]) => ({ label, on: s.as === k, off: s.as !== k, pick: () => this.setState({ as: k, edit: '' }) })),
      kpis: [['Live prices', String(live), 'Quoted by sales from here'], ['Price to set', String(toSet), 'Never quoted until set'], ['Price changes waiting', String(nPend), nPend ? 'The other super admin decides' : 'Nothing waiting'], ['Discount requests', String(nDisc), nDisc ? 'A super admin who did not ask decides' : 'All decided']].map(([k, v, note]) => ({ k, v, note })),
      infoText: (nPend + nDisc) + ' of the 7 decisions on super admin Home are here: the full start-up price (decision 1) and two discounts (decisions 2 and 3). A new price applies only to new clients from its date; clients who have signed keep the price in their agreement. Payments go through Stripe; bank transfer only by agreement, marked paid by finance. VAT is ' + VAT + '%, a setting in Rules and promises.',
      groups, fPrice: s.fPrice, fEff: s.fEff, fReason: s.fReason, fErr: !!s.fErr, fErrText: s.fErr,
      onPrice: e => this.setState({ fPrice: e.target.value, fErr: '' }), onEff: e => this.setState({ fEff: e.target.value }), onReason: e => this.setState({ fReason: e.target.value, fErr: '' }),
      vatTabs: vatOpts.map(k => ({ label: k, on: s.fVat === k, off: s.fVat !== k, pick: () => this.setState({ fVat: k }) })),
      nTabs: [1, 2, 3, 4].map(k => ({ label: String(k), on: s.fN === k, off: s.fN !== k, pick: () => setN(k) })),
      inst, instCheck, instCheckCls: pctOk ? 'sb-sub' : 'bz-err', equalise: () => setN(s.fN),
      submit, cancel: () => this.setState({ edit: '', fErr: '' }), discounts, discLeft: 'Discount requests: ' + nDisc
    };
  }
}'''
H['pb'] = 3460
build_sa(OUT + '/PriceBook.dc.html', 'Price book', 'Price book', H['pb'], B_PB, S_PB, 'prices', CSS)

# ---------------------------------------------------------------- 5. Team and cover (manager screen, board 78)
B_TC = '''      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 4px; max-width: 820px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Team and cover</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Who does what, who is away and who covers. Olu is on leave this week. Sam Patel is suspended pending the incident review and leaves on Friday. Cover is set up when leave is booked, so nobody needs emergency access for planned leave.</span>
        </div>
        <span style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{toggleLeave}}">{{leaveLabel}}</button><a class="sb-btn b-gh bz-link" href="PeopleAccess.dc.html">Invite a person</a></span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="4">
          <div class="sb-card sb-kpi"><span class="sb-muted">{{k.k}}</span><span class="sb-kv">{{k.v}}</span><span class="{{k.cls}}" style="align-self: flex-start;">{{k.note}}</span></div>
        </sc-for>
      </div>

      <sc-if value="{{showLeave}}" hint-placeholder-val="{{ false }}">
        <section class="sb-card" style="padding: 0 20px 18px; display: flex; flex-direction: column; gap: 12px;" aria-labelledby="lv-h">
          <div class="sb-head" style="padding-left: 0; padding-right: 0;"><h2 id="lv-h" class="sb-h2">Book leave and cover</h2><span class="sb-sub">A manager approves the cover when the leave is booked. It starts and ends by itself</span></div>
          <span class="bz-lbl">Who is away</span>
          <div style="display: flex; gap: 6px; flex-wrap: wrap;">''' + tabs('lvWho', 'Who is away') + '''</div>
          <div style="display: flex; gap: 16px; flex-wrap: wrap;">
            <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">First day away</span><input class="bz-in" style="width: 200px;" value="{{lvFrom}}" onChange="{{onLvFrom}}"></label>
            <label style="display: flex; flex-direction: column; gap: 4px;"><span class="bz-lbl">Back on</span><input class="bz-in" style="width: 200px;" value="{{lvTo}}" onChange="{{onLvTo}}"></label>
          </div>
          <span class="bz-lbl">Covered by</span>
          <div style="display: flex; gap: 6px; flex-wrap: wrap;">''' + tabs('lvCover', 'Covered by') + '''</div>
          <span class="sb-muted">Chloe Dunn (consultant) joins Mon 16 Nov and appears here once her account is active.</span>
          <span class="sb-sub">{{lvWhat}}</span>
          <div style="display: flex; gap: 6px; flex-wrap: wrap;">''' + tabs('lvVault', 'Vault reveal') + '''</div>
          <sc-if value="{{lvErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Choose who is away, both dates and who covers.</span></sc-if>
          <div><button class="sb-btn b-pri" onClick="{{lvSend}}">Send to a manager for approval</button></div>
        </section>
      </sc-if>

      <section class="sb-card" aria-labelledby="pp-h">
        <div class="sb-head"><h2 id="pp-h" class="sb-h2">People: 10 with access</h2><span class="sb-sub">Capacity is this week's planned work against that person's normal week</span></div>
        <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 0 0 210px;">Person</span><span class="sb-th" style="flex: 1 1 260px;">Clients and work</span><span class="sb-th" style="flex: 0 0 180px;">Capacity</span><span class="sb-th" style="flex: 1 1 240px;">Leave and cover</span></div>
        <sc-for list="{{people}}" as="p" hint-placeholder-count="10">
          <div class="sb-row" style="align-items: flex-start;">
            <span style="flex: 0 0 210px; display: flex; flex-direction: column;"><span class="bz-b">{{p.name}}</span><span class="sb-muted">{{p.role}}</span></span>
            <span style="flex: 1 1 260px; min-width: 0;" class="sb-sub">{{p.work}}</span>
            <span style="flex: 0 0 180px; display: flex; flex-direction: column; gap: 4px;"><span class="{{p.barCls}}" aria-hidden="true"><span class="{{p.w}}"></span></span><span class="sb-muted">{{p.cap}}</span></span>
            <span style="flex: 1 1 240px; min-width: 0;"><span class="{{p.leaveCls}}" style="white-space: normal;">{{p.leave}}</span></span>
          </div>
        </sc-for>
      </section>

      <section class="sb-card" aria-labelledby="cv-h">
        <div class="sb-head"><h2 id="cv-h" class="sb-h2">Cover this week: Olu on leave</h2><span class="sb-chip c-ok">Approved by Rachel Turner, Fri 30 Oct</span></div>
        <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border-top: 1px solid var(--cs-border-subtle);">
          <sc-for list="{{coverFacts}}" as="f" hint-placeholder-count="4"><div class="sb-kpi"><span class="sb-muted">{{f.k}}</span><span class="bz-b">{{f.v}}</span></div></sc-for>
        </div>
        <div class="sb-row"><span class="sb-sub">Daniel Mensah covers 4 of Olu's clients from Mon 2 Nov to Fri 6 Nov at 17:30. The cover includes the client pages, tasks, weekly updates and vault reveal for these 4 clients only, approved when Olu booked the leave. Every reveal still needs a reason and is logged; Olu sees the list when back. It ends by itself. Brookside Homecare (aftercare, month 1) is not urgent, so it waits for Olu.</span></div>
        <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));">
          <sc-for list="{{cover}}" as="c" hint-placeholder-count="4">
            <div class="sb-row" style="align-items: flex-start;">
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{c.name}}</span><span class="sb-sub">{{c.what}}</span></span>
              <span style="display: flex; flex-direction: column; gap: 4px; align-items: flex-end;"><span class="{{c.cls}}">{{c.flag}}</span><span class="sb-chip c-brand">Vault reveal: yes</span></span>
            </div>
          </sc-for>
        </div>
        <div class="sb-row"><span class="sb-muted">Break-glass is for emergencies only, never for planned leave. None in the last 30 days. See Security (board 84).</span></div>
        <sc-for list="{{booked}}" as="b" hint-placeholder-count="1">
          <div class="sb-row" style="align-items: flex-start; background: var(--cs-surface-subtle);">
            <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{b.title}}</span><span class="sb-sub">{{b.text}}</span></span>
            <span class="{{b.cls}}">{{b.chip}}</span>
            <sc-if value="{{b.canApprove}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-sec" onClick="{{b.approve}}">Approve as a manager</button></sc-if>
          </div>
        </sc-for>
      </section>

      <section class="sb-card" aria-labelledby="sp-h">
        <div class="sb-head"><h2 id="sp-h" class="sb-h2">Sam Patel: suspended, leaves Fri 6 Nov</h2><span class="{{offCls}}">{{offChip}}</span></div>
        <div style="display: flex; flex-wrap: wrap; align-items: flex-start; border-top: 1px solid var(--cs-border-subtle);">
          <div style="flex: 1 1 420px; min-width: 0;">
            <div class="bz-gh" style="border-top: 0;">Checklist</div>
            <sc-for list="{{checks}}" as="c" hint-placeholder-count="6">
              <div class="sb-row">
                <span class="{{c.cls}}" style="width: 96px; justify-content: center; flex-shrink: 0;">{{c.state}}</span>
                <span style="flex: 1; min-width: 0; display: flex; flex-direction: column;"><span class="bz-b">{{c.k}}</span><span class="sb-sub">{{c.note}}</span></span>
                <sc-if value="{{c.hasBtn}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-sec" onClick="{{c.act}}">{{c.btn}}</button></sc-if>
              </div>
            </sc-for>
            <div class="sb-row" style="background: var(--cs-surface-subtle);"><span style="flex: 1; min-width: 0;" class="sb-sub">Each system has its own step (Google Workspace, the Hub, the Interview Preparation Hub, GoHighLevel, Xero, Stripe, DocuSeal). "Suspend now" already ran at 08:25.</span><a class="sb-btn b-gh bz-link" href="PeopleAccess.dc.html">Open People and access</a></div>
          </div>
          <div style="flex: 1.3 1 520px; min-width: 0; border-left: 1px solid var(--cs-border-subtle);">
            <div class="bz-gh" style="border-top: 0;">Reassign Sam's 6 clients. None go to Daniel, who is at capacity this week</div>
            <sc-for list="{{sams}}" as="r" hint-placeholder-count="6">
              <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px;">
                <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center; flex-wrap: wrap;"><span style="display: flex; flex-direction: column;"><span class="bz-b">{{r.name}}</span><span class="sb-muted">{{r.what}}</span></span><span style="display: flex; gap: 8px; align-items: center;"><span class="{{r.cls}}" style="white-space: normal;">{{r.chip}}</span><sc-if value="{{r.closed}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-sec" onClick="{{r.openIt}}">Reassign</button></sc-if></span></div>
                <sc-if value="{{r.done}}" hint-placeholder-val="{{ false }}"><span class="sb-sub">{{r.noteLine}}</span></sc-if>
                <sc-if value="{{r.open}}" hint-placeholder-val="{{ true }}">
                  <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><span class="bz-lbl">New case owner</span>
                    <sc-for list="{{r.opts}}" as="o" hint-placeholder-count="3">
                      <sc-if value="{{o.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" aria-pressed="true" onClick="{{o.pick}}">{{o.label}}</button></sc-if>
                      <sc-if value="{{o.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" aria-pressed="false" onClick="{{o.pick}}">{{o.label}}</button></sc-if>
                    </sc-for>
                    <span class="sb-muted">Daniel: at capacity. Chloe Dunn: joins Mon 16 Nov, shown here once active</span>
                  </div>
                  <textarea class="bz-ta" aria-label="{{r.taLabel}}" value="{{r.note}}" onChange="{{r.onNote}}" placeholder="Handover note: where things are, what is next, anything the client prefers"></textarea>
                  <sc-if value="{{r.err}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Choose a new owner and write a handover note.</span></sc-if>
                  <div style="display: flex; gap: 8px;"><button class="sb-btn b-pri" onClick="{{r.save}}">Save and send for approval</button><button class="sb-btn b-gh" onClick="{{r.close}}">Cancel</button></div>
                </sc-if>
              </div>
            </sc-for>
            <div class="sb-row"><span class="sb-muted">A new case owner is a permission change, so a super admin approves it on super admin Home. The reassignment then sends email 9.3 "Your new consultant" to the client on the day it moves (Messages and automations, board 82, rule A35).</span></div>
          </div>
        </div>
      </section>

      <section class="sb-card" aria-labelledby="rp-h">
        <div class="sb-head"><h2 id="rp-h" class="sb-h2">Roles and access</h2><a class="sb-btn b-gh bz-link" href="PeopleAccess.dc.html">Open People and access</a></div>
        <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--cs-border-subtle);">
          <sc-for list="{{roles}}" as="r" hint-placeholder-count="3"><div class="sb-kpi" style="gap: 4px;"><span class="bz-b">{{r.k}}</span><span class="sb-sub">{{r.v}}</span></div></sc-for>
        </div>
        <div class="sb-row"><span class="sb-muted">Roles, permissions, joiners, leavers and the quarterly access review are managed in People and access (board 83). Any change to a person's role or access needs a super admin, and the other super admin approves it.</span></div>
      </section>
'''
S_TC = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = {
      re: { kings: { to: 'olu', note: 'Drafting the policies. Client prefers calls after 2pm. Next: draft to the client Thu 12 Nov.', ok: false }, cedar: { to: 'olu', note: 'Manager CV checked. References next. Director is new to care and likes things in writing.', ok: false } },
      pick: {}, notes: {}, errs: {}, openId: 'rose', tasks: false, leave: false, lvWho: '', lvFrom: '', lvTo: '', lvCover: '', lvVault: 'yes', lvErr: false, booked: []
    };
  }
  renderVals() {
    const s = this.state;
    const OWN = { olu: 'Olu, from Mon 9 Nov', rachel: 'Rachel Turner', collins: 'Collins' };
    const SAMS = [
      ['kings', 'Kingsway Care Ltd', 'CQC, domiciliary care. Stage 4 of 11: drafting'],
      ['cedar', 'Cedar Lodge Care Ltd', 'CQC, domiciliary care. Stage 2 of 11: CV review'],
      ['rose', 'Rosehill Homecare Ltd', 'CQC, domiciliary care. Stage 8 of 11: with the regulator'],
      ['thorn', 'Thornbury Living Ltd', 'CQC, supported living. Stage 3 of 11: your documents'],
      ['holly', 'Hollybush Care Ltd', 'CIW, domiciliary support. Stage 5 of 11: your review'],
      ['bram', 'Bramley Support Ltd', 'CQC, supported living. Stage 11 of 11: aftercare, month 3']
    ];
    const nRe = SAMS.filter(x => s.re[x[0]]).length;
    const sams = SAMS.map(([id, name, what]) => {
      const done = s.re[id]; const pk = s.pick[id] || ''; const note = s.notes[id] || '';
      const isOpen = !done && s.openId === id;
      return { name, what, done: !!done, open: isOpen, closed: !done && !isOpen, openIt: () => this.setState({ openId: id }), close: () => this.setState({ openId: '' }),
        chip: done ? 'To ' + OWN[done.to] + '. Waiting for a super admin' : 'No owner after Friday', cls: 'sb-chip ' + (done ? 'c-warn' : 'c-bad'),
        noteLine: done ? 'Handover note: ' + done.note + ' Email 9.3 "Your new consultant" goes to the client on the day it moves.' : '',
        opts: Object.keys(OWN).map(k => ({ label: OWN[k], on: pk === k, off: pk !== k, pick: () => this.setState({ pick: Object.assign({}, s.pick, { [id]: k }), errs: Object.assign({}, s.errs, { [id]: false }) }) })),
        note, taLabel: 'Handover note for ' + name, err: !!s.errs[id],
        onNote: e => this.setState({ notes: Object.assign({}, s.notes, { [id]: e.target.value }), errs: Object.assign({}, s.errs, { [id]: false }) }),
        save: () => { if (!pk || !note.trim()) { this.setState({ errs: Object.assign({}, s.errs, { [id]: true }) }); return; } this.setState({ re: Object.assign({}, s.re, { [id]: { to: pk, note: note.trim() } }), openId: '' }); }
      };
    });
    const left = 6 - nRe;
    const checks = [
      ['6 clients reassigned, each with a handover note', nRe + ' of 6 have a new owner and a note, waiting for super admin approval (Kingsway and Cedar Lodge to Olu: asked by Grace, Fri 30 Oct 16:10, decision 5 on Home). ' + (left ? left + ' still have no owner after Friday' : 'Every client has a new owner'), left ? 'To do' : 'Done', left ? 'bad' : 'ok', '', null],
      ['Friday updates for Sam\'s clients', 'Collins sends Sam\'s 6 weekly updates due Fri 6 Nov. Sam is suspended, so he sends none', 'Planned', 'info', '', null],
      ['Open tasks and Questions moved', s.tasks ? '14 of 14 tasks and 1 question moved to the new owners' : '9 of 14 tasks moved. 5 belong to clients with no owner yet', s.tasks ? 'Done' : 'To do', s.tasks ? 'ok' : 'warn', s.tasks ? '' : 'Move the other 5', () => this.setState({ tasks: true })],
      ['Access suspended', 'Since Mon 2 Nov 08:25, by Rachel Turner, pending the incident review: Hub, Google Workspace and vault stopped, every device signed out. Disabled for good Fri 6 Nov 17:30. Sam\'s emails forward to Collins for 90 days', 'Suspended', 'bad', '', null],
      ['Downloads paused', 'Since Mon 2 Nov 06:01, paused by the Hub. Collins, the data protection lead, has been assessing the export of 38 documents on Sun 1 Nov since 08:10 (Security, board 84)', 'Paused', 'warn', '', null],
      ['Every step written to the audit log', 'Including each reassignment and its approval', 'Logging', 'ok', '', null]
    ].map(([k, note, state, c, btn, act]) => ({ k, note, state, cls: 'sb-chip c-' + c, btn, hasBtn: !!btn, act }));
    const toOlu = SAMS.filter(x => s.re[x[0]] && s.re[x[0]].to === 'olu').length;
    const toCol = SAMS.filter(x => s.re[x[0]] && s.re[x[0]].to === 'collins').length;
    const toRach = SAMS.filter(x => s.re[x[0]] && s.re[x[0]].to === 'rachel').length;
    const P = [
      ['Collins', 'Director, super admin 1, data protection lead', 'Leads the Sam Patel export assessment (window for an ICO report, if needed, ends Thu 5 Nov 06:00). Senior reviews: Sunrise Mon 9 Nov, Westbrook Thu 12 Nov. Calls Riverside today. Sends Sam\'s 6 weekly updates on Fri 6 Nov. Super admin decisions: 7, shared with Rachel Turner' + (toCol ? '. Case owner for ' + toCol + ' of Sam\'s clients from Mon 9 Nov' : ''), 75 + toCol * 5, 'In all week', 'ok'],
      ['Rachel Turner', 'Operations manager, super admin 2', 'Reviews the decisions on the Sam Patel export (second pair of eyes). Approved Olu\'s cover on Fri 30 Oct. Super admin decisions: 7, shared with Collins' + (toRach ? '. Case owner for ' + toRach + ' of Sam\'s clients from Mon 9 Nov' : ''), 80 + toRach * 5, 'In all week', 'ok'],
      ['Daniel Mensah', 'Consultant', '6 active, 2 in aftercare, plus 4 covering for Olu: 12 this week. Weekly updates: 10 due Fri 6 Nov', 95, 'Covering Olu until Fri 6 Nov 17:30', 'info'],
      ['Olu', 'Consultant', '5 clients: 4 covered by Daniel (Riverside, Greenway, Lagan View, Willow Bank), and Brookside Homecare in aftercare, which waits for Olu' + (toOlu ? '. From Mon 9 Nov also ' + toOlu + ' of Sam\'s clients, once approved' : ''), 0, 'On leave Mon 2 to Fri 6 Nov. Back Mon 9 Nov', 'warn'],
      ['Sam Patel', 'Consultant', '6 clients, ' + (left ? left + ' still to reassign' : 'all reassigned') + '. No client work while suspended; Collins covers his Friday updates', 0, 'Suspended since Mon 2 Nov 08:25, pending the incident review. Leaving Fri 6 Nov', 'bad'],
      ['Grace', 'Onboarding lead', '6 clients in onboarding, including Harbour Lane (5 of 8 gates passed). Owns every form question; CQC form v8 waiting for approval', 70, 'In all week', 'ok'],
      ['Divine', 'Client care', '3 calls today, including Meadow View\'s introduction call. 1 concern open (Riverside), 3 clients gone quiet', 60, 'In all week', 'ok'],
      ['Millicent', 'Coach', '7 sessions this week, including Bright Path session 2 today at 10:00', 75, 'In all week', 'ok'],
      ['Jo Martin', 'Sales', '12 Radar matches today, 4 providers in outreach. Asked for the Lindenfield discount', 55, 'In all week', 'ok'],
      ['Femi Ade', 'Finance, part time', 'Closing October: 2 unmatched payments, 1 refund for a manager to approve, 4 overdue invoices', 65, 'Works Mon, Wed and Thu', 'neutral']
    ];
    const people = P.map(([name, role, work, cap, leave, lc]) => ({ name, role, work,
      w: 'w' + Math.min(100, Math.round(cap / 5) * 5), barCls: 'bar' + (cap >= 90 ? ' red' : (cap >= 80 ? ' amb' : '')),
      cap: name === 'Olu' ? 'On leave' : name === 'Sam Patel' ? 'Suspended' : cap + '% of ' + (name === 'Femi Ade' ? 'a part-time week' : 'a normal week'), leave, leaveCls: 'sb-chip c-' + lc }));
    const cover = [
      ['Riverside Homecare Ltd', 'Stage 8 of 11: with CQC since Fri 23 Oct. Worried: Collins calls today', 'Login missing 10 days', 'bad'],
      ['Greenway Support Ltd', 'Stage 3 of 11: 3 documents waiting. Friday\'s weekly update bounced at 17:02', 'Gone quiet 10 days', 'warn'],
      ['Lagan View Care Ltd', 'Stage 8 of 11: with RQIA since Wed 30 Sep. Interviews Tue 8 Dec', 'On track', 'ok'],
      ['Willow Bank Supported Living Ltd', 'Stage 3 of 11: documents by Fri 27 Nov', 'On track', 'ok']
    ].map(([name, what, flag, k]) => ({ name, what, flag, cls: 'sb-chip c-' + k }));
    const coverFacts = [['Covered by', 'Daniel Mensah'], ['Dates', 'Mon 2 Nov to Fri 6 Nov, 17:30'], ['Clients', '4 of Olu\'s 5'], ['Ends', 'By itself, Fri 6 Nov 17:30']].map(([k, v]) => ({ k, v }));
    const WHO = [['millicent', 'Millicent'], ['grace', 'Grace'], ['divine', 'Divine'], ['daniel', 'Daniel Mensah']];
    const COV = { millicent: [['divine', 'Divine'], ['grace', 'Grace']], grace: [['divine', 'Divine'], ['rachel', 'Rachel Turner']], divine: [['grace', 'Grace'], ['jo', 'Jo Martin']], daniel: [['olu', 'Olu'], ['collins', 'Collins']] };
    const WHAT = { millicent: 'Covers sessions only. Coaches never see the vault, so no vault reveal is needed.', grace: 'Covers onboarding gates, form questions and fix lists for the clients in onboarding.', divine: 'Covers introduction calls, concerns and gone quiet clients.', daniel: 'Covers Daniel\'s 6 active and 2 aftercare clients: client pages, tasks, weekly updates.' };
    const needsVault = s.lvWho === 'daniel';
    const lvSend = () => { if (!s.lvWho || !s.lvFrom.trim() || !s.lvTo.trim() || !s.lvCover) { this.setState({ lvErr: true }); return; }
      const who = WHO.find(w => w[0] === s.lvWho)[1]; const cov = COV[s.lvWho].find(c => c[0] === s.lvCover)[1];
      this.setState({ booked: s.booked.concat([{ who, cov, from: s.lvFrom.trim(), to: s.lvTo.trim(), vault: needsVault && s.lvVault === 'yes', ok: false }]), leave: false, lvErr: false, lvWho: '', lvFrom: '', lvTo: '', lvCover: '' }); };
    const booked = s.booked.map((b, i) => ({ title: 'Leave booked: ' + b.who + ', ' + b.from + ' to ' + b.to + '. Covered by ' + b.cov, text: (b.vault ? 'Includes vault reveal for the covered clients and dates only. ' : 'No vault reveal. ') + 'Starts and ends by itself. ' + (b.ok ? 'Approved by Collins, just now. Both people and the clients\' records show the cover.' : 'Waiting for a manager. You are a director, so you can approve it.'),
      chip: b.ok ? 'Approved' : 'Waiting', cls: 'sb-chip ' + (b.ok ? 'c-ok' : 'c-warn'), canApprove: !b.ok,
      approve: () => { const nb = s.booked.slice(); nb[i] = Object.assign({}, b, { ok: true }); this.setState({ booked: nb }); } }));
    const roles = [
      ['10 people, 8 roles', 'Manager, consultant (case owner), onboarding lead, client care, coach, sales, finance and data protection lead. Super admin is a flag on top of a role: Collins and Rachel Turner.'],
      ['Who sees which clients', 'Directors and managers see every client. Everyone else sees the clients assigned to them and the clients they cover, for the dates of the cover.'],
      ['Waiting now', 'Olu takes Kingsway and Cedar Lodge from Mon 9 Nov, asked by Grace Fri 30 Oct 16:10 (decision 5 on Home). The quarterly access review is due.']
    ].map(([k, v]) => ({ k, v }));
    return {
      theme: this.props.theme ?? 'light', three: 3, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      kpis: [['People with access', '10', 'All use two-step login', 'ok'], ['On leave this week', '1', 'Olu, Daniel covering', 'warn'], ['Leaving', '1', 'Sam Patel: suspended, leaves Fri 6 Nov', 'bad'], ['No owner after Friday', String(left), left ? 'Reassign before Friday' : 'All reassigned', left ? 'bad' : 'ok']].map(([k, v, note, c]) => ({ k, v, note, cls: 'sb-chip c-' + c })),
      showLeave: s.leave, toggleLeave: () => this.setState({ leave: !s.leave, lvErr: false }), leaveLabel: s.leave ? 'Close' : 'Book leave and cover',
      lvWho: WHO.map(([k, label]) => ({ label, on: s.lvWho === k, off: s.lvWho !== k, pick: () => this.setState({ lvWho: k, lvCover: '', lvErr: false }) })),
      lvCover: (COV[s.lvWho] || []).map(([k, label]) => ({ label, on: s.lvCover === k, off: s.lvCover !== k, pick: () => this.setState({ lvCover: k, lvErr: false }) })),
      lvWhat: s.lvWho ? WHAT[s.lvWho] : 'Choose who is away to see what the cover includes.',
      lvVault: needsVault ? [['yes', 'Include vault reveal for the covered clients and dates'], ['no', 'No vault reveal']].map(([k, label]) => ({ label, on: s.lvVault === k, off: s.lvVault !== k, pick: () => this.setState({ lvVault: k }) })) : [],
      lvFrom: s.lvFrom, lvTo: s.lvTo, onLvFrom: e => this.setState({ lvFrom: e.target.value, lvErr: false }), onLvTo: e => this.setState({ lvTo: e.target.value, lvErr: false }), lvErr: s.lvErr, lvSend,
      people, cover, coverFacts, booked, checks, sams, roles,
      offChip: left ? left + ' clients still need an owner' : 'Clients all reassigned', offCls: 'sb-chip ' + (left ? 'c-bad' : 'c-ok')
    };
  }
}'''
H['tc'] = 2680
build(OUT + '/TeamCover.dc.html', 'Team and cover', 'Team and cover', H['tc'], B_TC, S_TC, 'team', CSS)

# ---------------------------------------------------------------- 6. Money and exports (super admin menu, board 87)
B_MX = '''      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 4px; max-width: 820px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Money and exports</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Month close, the export for the accountant, Xero and Stripe, refunds and discounts. Femi Ade (finance) prepares it; a manager approves refunds; a super admin locks the month. Amounts exclude VAT unless they say otherwise.</span>
        </div>
        <span class="sb-chip c-ok">{{syncTime}}</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="4">
          <div class="sb-card sb-kpi"><span class="sb-muted">{{k.k}}</span><span class="sb-kv">{{k.v}}</span><span class="sb-sub">{{k.note}}</span></div>
        </sc-for>
      </div>

      <div class="bz-cols">
        <section class="sb-card" style="flex: 1 1 400px; min-width: 0;" aria-labelledby="mc-h">
          <div class="sb-head"><h2 id="mc-h" class="sb-h2">Month close: October 2026</h2><span class="{{closeChipCls}}">{{closeChip}}</span></div>
          <div style="padding: 0 20px 10px;"><div class="bar" aria-hidden="true"><span class="{{closeBar}}"></span></div></div>
          <sc-for list="{{close}}" as="c" hint-placeholder-count="8">
            <div class="sb-row" style="align-items: flex-start;">
              <span class="{{c.cls}}" style="width: 72px; justify-content: center; flex-shrink: 0;">{{c.state}}</span>
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span class="bz-b">{{c.k}}</span><span class="sb-sub">{{c.note}}</span></span>
            </div>
          </sc-for>
          <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px; background: var(--cs-surface-subtle);">
            <sc-if value="{{canLock}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-pri" style="align-self: flex-start;" onClick="{{lock}}">Send the export and lock October</button></sc-if>
            <sc-if value="{{cantLock}}" hint-placeholder-val="{{ true }}"><span class="sb-sub">{{cantLockText}}</span></sc-if>
            <sc-if value="{{locked}}" hint-placeholder-val="{{ false }}"><div class="bz-ok"><span class="bz-b">October is locked. The export went to the accountant just now.</span><span class="sb-sub">Locked by Collins. Any later change to October needs a credit note. Logged in the exports register (Data and privacy, board 85).</span></div></sc-if>
          </div>
        </section>

        <section class="sb-card" style="flex: 1.7 1 600px; min-width: 0;" aria-labelledby="ae-h">
          <div class="sb-head"><h2 id="ae-h" class="sb-h2">Export for the accountant: October</h2><span class="sb-sub">{{vatRate}}</span></div>
          <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 1 1 220px;">Line</span><span class="sb-th" style="flex: 0 0 44px; text-align: right;">Count</span><span class="sb-th" style="flex: 0 0 96px; text-align: right;">Net</span><span class="sb-th" style="flex: 0 0 86px; text-align: right;">VAT</span><span class="sb-th" style="flex: 0 0 96px; text-align: right;">Gross</span></div>
          <sc-for list="{{lines}}" as="l" hint-placeholder-count="8">
            <div class="sb-row" style="padding-top: 7px; padding-bottom: 7px; font-size: 13px;"><span style="flex: 1 1 220px; min-width: 0;" class="{{l.cls}}">{{l.k}}</span><span style="flex: 0 0 44px; text-align: right;">{{l.n}}</span><span style="flex: 0 0 96px; text-align: right;">{{l.net}}</span><span style="flex: 0 0 86px; text-align: right;">{{l.vat}}</span><span style="flex: 0 0 96px; text-align: right;">{{l.gross}}</span></div>
          </sc-for>
          <div class="sb-row"><span class="sb-muted">Prices that include VAT are split back out at the same rate. CN-0007: interview preparation was added to Elm Tree's registration package by mistake. No discounts were given in October.</span></div>
          <div class="bz-gh">Download</div>
          <div style="padding: 4px 20px 16px; display: flex; gap: 8px; flex-wrap: wrap;">
            <sc-for list="{{exports}}" as="x" hint-placeholder-count="5"><button class="{{x.cls}}" onClick="{{x.pick}}">{{x.label}}</button></sc-for>
          </div>
          <sc-if value="{{hasExp}}" hint-placeholder-val="{{ false }}"><div class="sb-row"><span class="sb-sub">{{expText}}</span></div></sc-if>
        </section>
      </div>

      <div class="bz-cols">
        <section class="sb-card" style="flex: 1 1 520px; min-width: 0;" aria-labelledby="sp-h">
          <div class="sb-head"><h2 id="sp-h" class="sb-h2">Stripe payouts and fees: October</h2><span class="sb-sub">Payments by card and other Stripe methods</span></div>
          <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span class="sb-th" style="flex: 1 1 140px;">Payout</span><span class="sb-th" style="flex: 0 0 80px; text-align: right;">Payments</span><span class="sb-th" style="flex: 0 0 110px; text-align: right;">Collected</span><span class="sb-th" style="flex: 0 0 90px; text-align: right;">Fees</span><span class="sb-th" style="flex: 0 0 110px; text-align: right;">Paid to bank</span></div>
          <sc-for list="{{payouts}}" as="p" hint-placeholder-count="6">
            <div class="sb-row" style="padding-top: 7px; padding-bottom: 7px; font-size: 13px;"><span style="flex: 1 1 140px;" class="{{p.cls}}">{{p.k}}</span><span style="flex: 0 0 80px; text-align: right;">{{p.n}}</span><span style="flex: 0 0 110px; text-align: right;">{{p.gross}}</span><span style="flex: 0 0 90px; text-align: right;">{{p.fee}}</span><span style="flex: 0 0 110px; text-align: right;">{{p.net}}</span></div>
          </sc-for>
          <div class="sb-row"><span class="sb-muted">Collected amounts include VAT. Bank transfer only by agreement: 1 in October (£2,700.00, Lagan View Care, RQIA instalment 2, marked paid by Femi Ade).</span></div>
        </section>

        <section class="sb-card" style="flex: 1 1 420px; min-width: 0;" aria-labelledby="xs-h">
          <div class="sb-head"><h2 id="xs-h" class="sb-h2">Xero sync</h2><button class="sb-btn b-gh" onClick="{{syncNow}}">{{syncLabel}}</button></div>
          <sc-for list="{{xero}}" as="x" hint-placeholder-count="7">
            <div class="sb-row" style="padding-top: 8px; padding-bottom: 8px;"><span style="flex: 1 1 160px;" class="sb-sub">{{x.k}}</span><span style="flex: 1 1 200px; min-width: 0;" class="bz-b">{{x.v}}</span><span class="{{x.cls}}">{{x.chip}}</span></div>
          </sc-for>
          <div class="sb-row"><span class="sb-muted">A failed sync shows on System health (board 86) with what it affects, and Femi and both super admins are told.</span></div>
        </section>
      </div>

      <div class="bz-cols">
        <section class="sb-card" style="flex: 1 1 520px; min-width: 0;" aria-labelledby="um-h">
          <div class="sb-head"><h2 id="um-h" class="sb-h2">{{umLeft}}</h2><span class="sb-sub">Money in that Xero cannot match to an invoice</span></div>
          <sc-for list="{{unmatched}}" as="u" hint-placeholder-count="2">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 6px;">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center; flex-wrap: wrap;"><span class="bz-b">{{u.title}}</span><span class="{{u.cls}}">{{u.chip}}</span></div>
              <span class="sb-sub">{{u.text}}</span>
              <sc-if value="{{u.open}}" hint-placeholder-val="{{ true }}"><span style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-sec" onClick="{{u.act}}">{{u.cta}}</button><button class="sb-btn b-gh" onClick="{{u.ask}}">{{u.askLabel}}</button></span></sc-if>
              <sc-if value="{{u.done}}" hint-placeholder-val="{{ false }}"><span class="sb-sub">{{u.doneText}}</span></sc-if>
            </div>
          </sc-for>
        </section>

        <section class="sb-card" style="flex: 1 1 420px; min-width: 0;" aria-labelledby="rf-h">
          <div class="sb-head"><h2 id="rf-h" class="sb-h2">{{rfLeft}}</h2></div>
          <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 8px; border-top: 0;">
            <div style="display: flex; justify-content: space-between; gap: 8px; align-items: center; flex-wrap: wrap;"><span class="bz-b">Thornbury Living Ltd: £3,000.00 to the card it came from</span><span class="{{rfChipCls}}">{{rfChip}}</span></div>
            <span class="sb-sub">Asked by Femi Ade, Fri 30 Oct. Reason: "Duplicate payment. The first instalment (£2,500.00 + VAT £500.00) was taken twice on Thu 29 Oct, 4 minutes apart, when the card was retried." No credit note is needed, because the invoice was only raised once.</span>
            <span class="sb-muted">A manager approves refunds, never the person who asked. Managers: Collins, Rachel Turner.</span>
            <sc-if value="{{rfOpen}}" hint-placeholder-val="{{ true }}">
              <textarea class="bz-ta" aria-label="Reason for the refund decision" value="{{rfReason}}" onChange="{{onRfReason}}" placeholder="Your reason (written to the audit log)"></textarea>
              <sc-if value="{{rfErr}}" hint-placeholder-val="{{ false }}"><span class="bz-err">Write a reason first.</span></sc-if>
              <span style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="sb-btn b-pri" onClick="{{rfYes}}">Approve the refund</button><button class="sb-btn b-gh" onClick="{{rfNo}}">Decline</button></span>
            </sc-if>
            <sc-if value="{{rfDone}}" hint-placeholder-val="{{ false }}"><div class="{{rfBox}}"><span class="bz-b">{{rfResult}}</span><span class="sb-sub">{{rfNote}}</span></div></sc-if>
          </div>
        </section>
      </div>

      <section class="sb-card" aria-labelledby="df-h">
        <div class="sb-head"><h2 id="df-h" class="sb-h2">How a discount flows through</h2><span style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><span class="sb-sub">Example: Lindenfield Care Ltd, decision 2 on super admin Home</span>''' + tabs('dfTabs', 'Discount example') + '''</span></div>
        <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--cs-border-subtle);">
          <sc-for list="{{flow}}" as="f" hint-placeholder-count="6">
            <div style="padding: 14px 20px; display: flex; flex-direction: column; gap: 6px; border-right: 1px solid var(--cs-border-subtle); border-bottom: 1px solid var(--cs-border-subtle);">
              <span style="display: flex; gap: 8px; align-items: center;"><span style="width: 24px; height: 24px; border-radius: 8px; background: var(--cs-surface-brand); color: var(--cs-text-brand); display: inline-flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600;">{{f.n}}</span><span class="bz-b">{{f.where}}</span></span>
              <span class="sb-sub">{{f.what}}</span>
              <span class="{{f.cls}}" style="align-self: flex-start;">{{f.state}}</span>
            </div>
          </sc-for>
        </div>
        <div class="sb-row"><span class="sb-muted">{{dfNote}}</span></div>
      </section>
'''
S_MX = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { um: {}, rf: '', rfReason: '', rfErr: false, exp: '', synced: false, locked: false, df: 'now' }; }
  renderVals() {
    const s = this.state;
    const C = (id, fb) => (window.CSR ? window.CSR.get(id, fb) : fb);
    const VAT = Number(C('vat-rate', 20));
    const gbp = p => (p < 0 ? '-' : '') + '£' + (Math.abs(p) / 100).toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    const vatOn = net => Math.round(net * VAT / 100);
    const gbp0 = p => p % 100 === 0 ? '£' + (p / 100).toLocaleString('en-GB') : gbp(p);
    const netOfGross = g => g - Math.round(g * VAT / (100 + VAT));
    // October invoice lines: [label, count, unit pence, incl VAT?]
    const L = [
      ['CQC domiciliary care, instalments', 6, Math.round(Number(C('price-dom', 4000)) * 50), false],
      ['CQC supported living, instalments', 2, Math.round(Number(C('price-sl', 5000)) * 50), false],
      ['Full start-up, first instalments', 3, Math.floor(Number(C('price-full', 8500)) * 100 / 3), false],
      ['CIW and RQIA, instalments', 2, Math.round(Number(C('price-ciw', 4500)) * 50), false],
      ['Tender writing, instalments', 4, 102500, false],
      ['PIR writing', 3, Math.round(Number(C('price-pir', 750)) * 100), false],
      ['Interview preparation (incl. VAT)', 2, Math.round(Number(C('price-interview', 750)) * 100), true],
      ['Supported living add-on (incl. VAT)', 1, Math.round(Number(C('price-sl-addon', 1500)) * 100), true]
    ];
    let tn = 0, tv = 0, cnt = 0;
    const lines = L.map(([k, n, unit, incl]) => { const uNet = incl ? netOfGross(unit) : unit; const uVat = incl ? unit - uNet : vatOn(unit); const net = uNet * n, vat = uVat * n; tn += net; tv += vat; cnt += n; return { k, n: String(n), net: gbp(net), vat: gbp(vat), gross: gbp(net + vat), cls: '' }; });
    const cnGross = Math.round(Number(C('price-interview', 750)) * 100), cnNet = netOfGross(cnGross);
    lines.unshift({ k: 'Invoices raised', n: String(cnt), net: gbp(tn), vat: gbp(tv), gross: gbp(tn + tv), cls: 'bz-b' });
    lines.push({ k: 'Credit note CN-0007, Elm Tree Care', n: '1', net: gbp(-cnNet), vat: gbp(-(cnGross - cnNet)), gross: gbp(-cnGross), cls: '' });
    lines.push({ k: 'Refunds paid', n: '0', net: gbp(0), vat: gbp(0), gross: gbp(0), cls: '' });
    lines.push({ k: 'Discounts given', n: '0', net: gbp(0), vat: gbp(0), gross: gbp(0), cls: '' });
    lines.push({ k: 'Sales for the VAT return', n: ' ', net: gbp(tn - cnNet), vat: gbp(tv - (cnGross - cnNet)), gross: gbp(tn + tv - cnGross), cls: 'bz-b' });
    const PO = [['Fri 2 Oct', 3, 631000, 9550], ['Fri 9 Oct', 5, 1002060, 15040], ['Fri 16 Oct', 4, 853000, 12740], ['Fri 23 Oct', 6, 1027200, 15360], ['Fri 30 Oct', 3, 704600, 6860]];
    let pn = 0, pg = 0, pf = 0;
    const payouts = PO.map(([k, n, g, f]) => { pn += n; pg += g; pf += f; return { k, n: String(n), gross: gbp(g), fee: gbp(f), net: gbp(g - f), cls: '' }; });
    payouts.push({ k: 'October', n: String(pn), gross: gbp(pg), fee: gbp(pf), net: gbp(pg - pf), cls: 'bz-b' });
    const umDone = k => !!s.um[k];
    const unmatched = [
      ['thorn', 'Stripe, £3,000.00, Thu 29 Oct: Thornbury Living Ltd', 'A second payment for invoice INV-1052 (first instalment, £2,500.00 + VAT), 4 minutes after the first. The card was retried.', 'Link to the refund request', 'Linked to the refund request below. It stays out of sales; Xero shows it as money to return.', 'Tell Femi it is a duplicate', 'Femi Ade is told.'],
      ['bryn', 'Bank transfer, £900.00, Fri 30 Oct, reference "BRYN GLAS"', 'Looks like half of INV-1038: Bryn Glas Care, tender writing instalment 1, £1,800.00 including VAT, 31 to 60 days overdue.', 'Match as a part payment', 'Matched to INV-1038 as a part payment. Overdue becomes £4,550.00 net in 4 invoices; the Manager dashboard shows it after the next sync.', 'Ask the case owner', 'Asked Daniel Mensah to confirm with Bryn Glas Care.']
    ].map(([k, title, text, cta, doneText, askLabel, askText]) => ({ title, text, cta, askLabel, open: !umDone(k), done: umDone(k), doneText: s.um[k] === 'ask' ? askText : doneText,
      chip: umDone(k) ? (s.um[k] === 'ask' ? 'Asked' : 'Sorted') : 'To sort', cls: 'sb-chip ' + (umDone(k) ? (s.um[k] === 'ask' ? 'c-info' : 'c-ok') : 'c-warn'),
      act: () => this.setState({ um: Object.assign({}, s.um, { [k]: 'done' }) }), ask: () => this.setState({ um: Object.assign({}, s.um, { [k]: 'ask' }) }) }));
    const umLeft = ['thorn', 'bryn'].filter(k => s.um[k] !== 'done').length;
    const rfDecided = !!s.rf;
    const rfGo = v => { if (!s.rfReason.trim()) { this.setState({ rfErr: true }); return; } this.setState({ rf: v, rfErr: false }); };
    const CL = [
      ['Every October invoice is in Xero', cnt + ' of ' + cnt + ' invoices synced, ' + gbp(tn) + ' net', true],
      ['Stripe payouts match the bank', '5 of 5 payouts found in the bank feed, ' + gbp(pg - pf) + ' in all', true],
      ['Unmatched payments sorted', umLeft ? umLeft + ' still to sort (below)' : 'Both sorted', umLeft === 0],
      ['Refunds decided by a manager', rfDecided ? 'Thornbury Living: ' + (s.rf === 'yes' ? 'approved' : 'declined') + ' by Collins' : '1 waiting: Thornbury Living, £3,000.00', rfDecided],
      ['Credit notes checked', '1: CN-0007, Elm Tree Care, Mon 19 Oct. Interview practice is already one of the 3 included sessions', true],
      ['Discounts given match an approval', 'None given in October. 2 asked for November are waiting on super admin Home', true],
      ['VAT split checked', 'At ' + VAT + '%, the rate in Rules and promises. Prices that include VAT are split back out', true],
      ['Export sent and October locked', s.locked ? 'Sent to the accountant and locked just now' : 'Opens when everything above is done', s.locked]
    ];
    const doneN = CL.filter(c => c[2]).length;
    const close = CL.map(([k, note, ok]) => ({ k, note, state: ok ? 'Done' : 'To do', cls: 'sb-chip ' + (ok ? 'c-ok' : 'c-warn') }));
    const ready = umLeft === 0 && rfDecided && !s.locked;
    const EX = [['csv', 'October accountant export (CSV)'], ['vat', 'VAT summary'], ['stripe', 'Stripe payouts and fees'], ['refunds', 'Refunds and credit notes'], ['disc', 'Discounts given']];
    const exLabel = EX.find(x => x[0] === s.exp);
    const dfOn = s.df === 'if';
    const dom = Math.round(Number(C('price-dom', 4000)) * 100), ask = 380000, off = dom - ask, half = Math.floor(ask / 2);
    const FL = [
      ['Asked in Add a client', 'Jo Martin asked for ' + gbp0(off) + ' off, with a reason: ready to sign today, price is the last blocker.', 'Done, today 08:05', 'ok'],
      ['Decided on super admin Home', 'Collins or Rachel Turner decides, never Jo. A reason is required and written to the audit log.', dfOn ? 'Approved' : 'Waiting', dfOn ? 'ok' : 'warn'],
      ['Agreement (DocuSeal)', 'List price ' + gbp0(dom) + ' + VAT, discount ' + gbp0(off) + ', agreed price ' + gbp0(ask) + ' + VAT. Sent for signature only after the decision.', dfOn ? 'Updated' : 'Not sent yet', dfOn ? 'ok' : 'neutral'],
      ['Stripe instalments', '2 of ' + gbp(half) + ' + VAT ' + gbp(vatOn(half)) + ' = ' + gbp(half + vatOn(half)) + ': at accept, sign and pay, and when the application is submitted.', dfOn ? 'Updated' : 'Not created yet', dfOn ? 'ok' : 'neutral'],
      ['Xero invoice', 'A line at ' + gbp(dom) + ', then "Discount agreed by Care Sync" ' + gbp(off) + ' off. VAT at ' + VAT + '% on ' + gbp(ask) + ': ' + gbp(vatOn(ask)) + '.', dfOn ? 'Updated' : 'Not raised yet', dfOn ? 'ok' : 'neutral'],
      ['Plan and costs (board 60)', 'The client sees "Your price: ' + gbp0(ask) + ' + VAT. This includes a ' + gbp0(off) + ' discount agreed by Care Sync." It also appears here under discounts given.', dfOn ? 'Updated' : 'Shows the price book price', dfOn ? 'ok' : 'neutral']
    ];
    const flow = FL.map(([where, what, state, k], i) => ({ n: String(i + 1), where, what, state, cls: 'sb-chip c-' + k }));
    return {
      theme: this.props.theme ?? 'light', three: 3, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      syncTime: 'Xero: connected, synced ' + (s.synced ? 'just now' : '09:00'), vatRate: 'VAT at ' + VAT + '%, from Rules and promises',
      kpis: [['Invoiced this month', '£9,600', '5 invoices on 1 and 2 Nov, as the Manager dashboard'], ['Collected this month', '£4,150', '3 payments through Stripe'], ['Overdue', '£5,300', '4 invoices. Reminders running'], ['October close', doneN + ' of 8', s.locked ? 'Locked' : 'Femi Ade prepares it']].map(([k, v, note]) => ({ k, v, note })),
      close, closeBar: 'w' + Math.round(doneN / 8 * 20) * 5, closeChip: s.locked ? 'Locked' : (ready ? 'Ready to lock' : (8 - doneN) + ' to do'), closeChipCls: 'sb-chip ' + (s.locked ? 'c-ok' : (ready ? 'c-info' : 'c-warn')),
      canLock: ready, cantLock: !ready && !s.locked, locked: s.locked, cantLockText: 'Sort the unmatched payments and decide the refund first. Then the export goes to the accountant and October is locked.', lock: () => this.setState({ locked: true }),
      lines, exports: EX.map(([k, label]) => ({ label, cls: 'sb-btn ' + (s.exp === k ? 'b-sec' : 'b-gh'), pick: () => this.setState({ exp: k }) })),
      hasExp: !!s.exp, expText: exLabel ? exLabel[1] + ' prepared just now for October. It holds company names and amounts only, no identity documents. Logged in the exports register (Data and privacy, board 85).' : '',
      payouts,
      xero: [['Connection', 'Connected, synced every hour', 'Healthy', 'ok'], ['Last sync', s.synced ? 'Just now' : 'Today 09:00. Next 10:00', 'Done', 'ok'], ['Invoices, October', cnt + ' synced', 'Done', 'ok'], ['Payments', (umLeft ? umLeft + ' unmatched' : 'All matched'), umLeft ? 'To sort' : 'Done', umLeft ? 'warn' : 'ok'], ['Credit notes', '1 synced (CN-0007)', 'Done', 'ok'], ['VAT rate used', VAT + '% (VAT on income)', 'Matches Rules', 'ok'], ['Errors, last 30 days', 'None', 'Clear', 'ok']].map(([k, v, chip, c]) => ({ k, v, chip, cls: 'sb-chip c-' + c })),
      syncNow: () => this.setState({ synced: true }), syncLabel: s.synced ? 'Synced just now' : 'Sync now',
      unmatched, umLeft: 'Unmatched payments: ' + umLeft,
      rfLeft: 'Refunds waiting for a manager: ' + (rfDecided ? '0' : '1'), rfOpen: !rfDecided, rfDone: rfDecided, rfReason: s.rfReason, rfErr: s.rfErr,
      onRfReason: e => this.setState({ rfReason: e.target.value, rfErr: false }), rfYes: () => rfGo('yes'), rfNo: () => rfGo('no'),
      rfChip: !rfDecided ? 'Waiting' : (s.rf === 'yes' ? 'Approved' : 'Declined'), rfChipCls: 'sb-chip ' + (!rfDecided ? 'c-warn' : (s.rf === 'yes' ? 'c-ok' : 'c-neutral')),
      rfBox: s.rf === 'yes' ? 'bz-ok' : 'bz-box',
      rfResult: s.rf === 'yes' ? 'Approved by Collins, just now. £3,000.00 goes back to the card through Stripe.' : 'Declined by Collins, just now. Femi Ade is told.',
      rfNote: 'Reason: "' + s.rfReason.trim() + '". Written to the audit log. ' + (s.rf === 'yes' ? 'The refund shows in the November export under refunds paid, and Thornbury Living is emailed a receipt.' : ''),
      dfTabs: [['now', 'Today: waiting'], ['if', 'If approved']].map(([k, label]) => ({ label, on: s.df === k, off: s.df !== k, pick: () => this.setState({ df: k }) })), flow,
      dfNote: 'The price book never changes for a discount. The same flow applies to Ashby Care (decision 3): PIR writing for 2 service types, ' + gbp0(135000) + ' + VAT instead of ' + gbp0(Math.round(Number(C('price-pir', 750)) * 200)) + ' + VAT, 1 payment in full.'
    };
  }
}'''
H['mx'] = 2280
build_sa(OUT + '/MoneyExports.dc.html', 'Money and exports', 'Money and exports', H['mx'], B_MX, S_MX, 'money', CSS)
