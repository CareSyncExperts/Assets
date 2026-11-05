import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from staffboard import build
OUT = sys.argv[1]

TABS = '''      <div role="tablist" aria-label="Show" style="display: flex; gap: 6px; flex-wrap: wrap;">
        <sc-for list="{{tabs}}" as="tb" hint-placeholder-count="5">
          <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
          <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
        </sc-for>
      </div>
'''

# 68. Clients list
B1 = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Clients</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">{{summary}}</span>
        </div>
        <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
          <input aria-label="Find a client" placeholder="Find a client, person or company number" style="min-height: 40px; width: 320px; padding: 0 12px; border-radius: 10px; border: 1px solid var(--cs-border-control); background: var(--cs-surface-raised); color: var(--cs-text-primary); font: inherit; font-size: 14px;">
          <button class="sb-btn b-gh" aria-expanded="{{exOpenAria}}" onClick="{{exToggle}}">Request an export</button>
        </div>
      </div>
      <sc-if value="{{exOpen}}" hint-placeholder-val="{{ false }}">
      <section class="sb-card" aria-labelledby="ex-h" style="padding: 16px 20px; display: flex; flex-direction: column; gap: 10px;">
        <h2 id="ex-h" class="sb-h2">Request an export of this list</h2>
        <span class="sb-sub">Consultants download single documents only; there is no bulk export. A list export needs approval from a manager or the data protection lead, and it is recorded in the exports register on Data and privacy (board 85). If it is approved, the link works for {{exHours}} hours and every download is logged. Logins never appear in an export.</span>
        <sc-if value="{{exNotSent}}" hint-placeholder-val="{{ true }}">
          <label style="display: flex; flex-direction: column; gap: 4px; font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">Why do you need it? (written to the audit log)<input aria-label="Why do you need the export" value="{{exWhy}}" onChange="{{onExWhy}}" placeholder="For example: list of my clients and next deadlines for the team meeting" style="min-height: 40px; padding: 0 12px; border-radius: 10px; border: 1px solid var(--cs-border-control); background: var(--cs-surface-raised); color: var(--cs-text-primary); font: inherit; font-size: 14px;"></label>
          <sc-if value="{{exErr}}" hint-placeholder-val="{{ false }}"><span style="font-size: 13px; line-height: 18px; color: var(--cs-status-error-text); font-weight: 500;">Write a reason first.</span></sc-if>
          <div style="display: flex; gap: 8px;"><button class="sb-btn b-pri" onClick="{{exSend}}">Send the request</button><button class="sb-btn b-gh" onClick="{{exToggle}}">Cancel</button></div>
        </sc-if>
        <sc-if value="{{exSent}}" hint-placeholder-val="{{ false }}"><span class="sb-chip c-info" style="align-self: flex-start; white-space: normal;">{{exMsg}}</span></sc-if>
      </section>
      </sc-if>
''' + TABS + '''      <section class="sb-card" aria-label="Clients">
        <div class="sb-row" style="border-top: 0; gap: 10px;"><span class="sb-th" style="flex: 2 1 210px;">Client</span><span class="sb-th" style="flex: 1 1 150px;">Stage</span><span class="sb-th" style="flex: 1 1 120px;">Waiting on</span><span class="sb-th" style="flex: 1 1 150px;">Next deadline</span><span class="sb-th" style="flex: 1 1 110px;">Last contact</span><span class="sb-th" style="flex: 1 1 110px;">Weekly update</span><span class="sb-th" style="flex: 0 0 96px;">Owner</span><span class="sb-th" style="flex: 0 0 70px;">Feeling</span></div>
        <sc-for list="{{rows}}" as="r" hint-placeholder-count="8">
          <div class="sb-row" style="gap: 10px; align-items: flex-start;">
            <span style="flex: 2 1 210px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{r.name}}</span><span style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;"><span class="{{r.regCls}}">{{r.reg}}</span><span class="sb-muted">{{r.contact}}</span></span></span>
            <span style="flex: 1 1 150px; min-width: 0;" class="sb-sub">{{r.stage}}</span>
            <span style="flex: 1 1 120px; min-width: 0;"><span class="{{r.waitCls}}" style="white-space: normal;">{{r.wait}}</span></span>
            <span style="flex: 1 1 150px; min-width: 0;" class="sb-sub">{{r.next}}</span>
            <span style="flex: 1 1 110px; min-width: 0;" class="sb-sub">{{r.last}}</span>
            <span style="flex: 1 1 110px; min-width: 0;"><span class="{{r.updCls}}" style="white-space: normal;">{{r.upd}}</span></span>
            <span style="flex: 0 0 96px;" class="sb-sub">{{r.owner}}</span>
            <span style="flex: 0 0 70px;"><span class="{{r.feelCls}}">{{r.feel}}</span></span>
          </div>
        </sc-for>
      </section>
      <span class="sb-muted">{{footNote}}</span>
'''
S1 = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { t: 'list', ex: false, exWhy: '', exErr: false, exSent: false }; }
  renderVals() {
    const t = this.state.t, s = this.state;
    // name, contact, reg, service, stage, wait, waitK, next, last, upd, updK, owner, feel, feelK, group
    const R = [
      ['Sunrise Homecare Ltd', 'Priya Shah', 'CQC', 'Domiciliary care', 'Stage 10 of 11: Notice of Proposal', 'Us: written representations', 'bad', 'Legal deadline Tue 17 Nov. Our target Tue 10 Nov', 'Thu 29 Oct, call', 'Due Fri 6 Nov', 'neutral', 'Daniel', 'Unsure', 'warn', 'own'],
      ['Riverside Homecare Ltd', 'Mark Evans', 'CQC', 'Domiciliary care', 'Stage 8 of 11: with CQC', 'Us: CQC email login, 10 days', 'bad', 'Add the login today. Collins calls today', 'Fri 30 Oct, call', 'Due Fri 6 Nov', 'neutral', 'Olu (Daniel covering)', 'Worried', 'bad', 'cover'],
      ['Greenway Support Ltd', 'Tunde Bello', 'CQC', 'Supported living', 'Stage 3 of 11: your documents', 'Client, 10 days', 'bad', 'Call today and fix the email address', 'Thu 22 Oct, upload', 'Overdue: bounced', 'bad', 'Olu (Daniel covering)', 'Unsure', 'warn', 'cover'],
      ['Bright Path Care Ltd', 'Joy Adeyemi', 'CQC', 'Domiciliary, full start-up', 'Stage 4 of 11: drafting', 'Us: Statement of Purpose check', 'info', 'Session 2 today 10:00. Provider form check Wed 11 Nov', 'Fri 30 Oct, update', 'Due Fri 6 Nov', 'neutral', 'Daniel', 'Happy', 'ok', 'own'],
      ['Afon Care Ltd', 'Rhian Example', 'CIW', 'Domiciliary support', 'Stage 8 of 11: with CIW since 14 Oct', 'Referee, 3 days', 'warn', 'Nudge Sarah today. Interview Thu 26 Nov', 'Thu 29 Oct, email', 'Due Fri 6 Nov', 'neutral', 'Daniel', 'Happy', 'ok', 'own'],
      ['Westbrook Care Ltd', 'Sade Johnson', 'CQC', 'Domiciliary care', 'Stage 10 of 11: refused, we resubmit', 'Us: new pack', 'info', 'Appeal window closes Sun 22 Nov. Senior review Thu 12 Nov. Resubmit Mon 30 Nov', 'Wed 28 Oct, call', 'Due Fri 6 Nov', 'neutral', 'Daniel', 'Unsure', 'warn', 'own'],
      ['Elm Tree Care Ltd', 'Femi Adebayo', 'CQC', 'Domiciliary care', 'Stage 9 of 11: interview', 'Us: CQC questions', 'info', 'Answers to CQC by Fri 6 Nov. Interview Tue 24 Nov', 'Fri 30 Oct, email', 'Due Fri 6 Nov', 'neutral', 'Daniel', 'Happy', 'ok', 'own'],
      ['Oakleaf Living Ltd', 'Kemi Adebola', 'Tender', 'Northshire and Eastford', 'Tender: 2 bids', 'Client: case study', 'ok', 'Case study Wed 11 Nov. Draft to Kemi Tue 17 Nov. We submit Fri 27 Nov', 'Fri 30 Oct, update', 'Due Fri 6 Nov', 'neutral', 'Daniel', 'Happy', 'ok', 'own'],
      ['Lagan View Care Ltd', 'Niamh Example', 'RQIA', 'Domiciliary care agency', 'Stage 8 of 11: with RQIA since 30 Sep', 'Regulator', 'neutral', 'Interviews Tue 8 Dec', 'Fri 30 Oct, update', 'Due Fri 6 Nov', 'neutral', 'Olu (Daniel covering)', 'Happy', 'ok', 'cover'],
      ['Willow Bank Supported Living Ltd', 'David Clarke', 'CQC', 'Registration then tenders', 'Stage 3 of 11: your documents', 'Client, 1 day', 'ok', 'Documents by Fri 27 Nov', 'Today, question', 'Due Fri 6 Nov', 'neutral', 'Olu (Daniel covering)', 'Happy', 'ok', 'cover'],
      ['Harbour Lane Care Ltd', 'Amara Okafor', 'CQC', 'Domiciliary, full start-up', 'Stage 1 of 11: onboarding checks', 'Client: 2 fixes. Landlord letter', 'warn', 'Gates 5 of 8 passed. Then manager approval', 'Fri 30 Oct, Grace', 'Starts at handover', 'neutral', 'Grace, then Daniel', 'Happy', 'ok', 'onb'],
      ['Meadow View Care Ltd', 'Ade Ola', 'CQC', 'Domiciliary, full start-up', 'Stage 1 of 11: welcome', 'Us: introduction call', 'warn', 'Paid today 10:02. Call by 12:02', 'Today, payment', 'Starts after onboarding', 'neutral', 'Divine, then Grace', 'New', 'neutral', 'team']
    ];
    const inList = r => r[14] !== 'team';
    const test = { all: () => true, list: inList, own: r => r[14] === 'own', cover: r => r[14] === 'cover', att: r => inList(r) && (r[6] === 'bad' || r[10] === 'bad' || r[13] === 'bad'), cqc: r => inList(r) && r[2] === 'CQC', ciw: r => inList(r) && r[2] === 'CIW', rqia: r => inList(r) && r[2] === 'RQIA', tender: r => inList(r) && r[2] === 'Tender' };
    const T = [['list', 'My list'], ['own', 'My own'], ['cover', 'Covering for Olu'], ['att', 'Needs attention'], ['cqc', 'CQC'], ['ciw', 'CIW'], ['rqia', 'RQIA'], ['tender', 'Tenders'], ['all', 'All']];
    const rows = R.filter(test[t]).map(r => ({
      name: r[0], contact: r[1], reg: r[2], regCls: 'sb-chip ' + (r[2] === 'Tender' ? 'c-info' : 'c-brand'), service: r[3], stage: r[4], wait: r[5], waitCls: 'sb-chip c-' + r[6], next: r[7], last: r[8], upd: r[9], updCls: 'sb-chip c-' + r[10], owner: r[11], feel: r[12], feelCls: 'sb-chip c-' + r[13]
    }));
    const label = T.find(x => x[0] === t)[1];
    const G = (id, fb) => (window.CSR ? window.CSR.get(id, fb) : fb);
    const footNote = '"Waiting on" turns amber after ' + G('waiting-amber-days', 5) + ' days and red after ' + G('waiting-red-days', 10) + '. Worried clients get no sales or growth messages until the concern is resolved, and the manager calls within 1 working day. Weekly updates go every ' + G('weekly-update-day', 'Friday') + ' by ' + G('weekly-update-time', '16:00') + '; the next are due Fri 6 Nov.';
    return {
      theme: this.props.theme ?? 'light', three: 3, user: { name: 'Daniel Mensah', initials: 'DM' }, nav: __NAV__, footNote,
      exOpen: s.ex, exOpenAria: s.ex ? 'true' : 'false', exToggle: () => this.setState({ ex: !s.ex, exErr: false }), exHours: String(G('export-link-hours', 24)),
      exWhy: s.exWhy, onExWhy: e => this.setState({ exWhy: e.target.value, exErr: false }), exErr: s.exErr, exSent: s.exSent, exNotSent: !s.exSent,
      exSend: () => { if (!s.exWhy.trim()) return this.setState({ exErr: true }); this.setState({ exSent: true, exErr: false }); },
      exMsg: 'Requested just now: "' + s.exWhy.trim() + '". It waits in the exports register for a manager or the data protection lead. You get the link if it is approved.',
      tabs: T.map(([k, l]) => ({ label: l + ' (' + R.filter(test[k]).length + ')', on: t === k, off: t !== k, pick: () => this.setState({ t: k }) })),
      rows, summary: t === 'all' ? 'All: your 11 clients, plus Meadow View Care, who paid today and is with Divine for the introduction call. The team has 52 active clients.' : t === 'list' ? 'Your list: 11 clients. 6 your own, 4 covering for Olu this week, 1 coming from onboarding. Most urgent first. The team has 52 active clients.' : label + ': ' + rows.length + (rows.length === 1 ? ' client' : ' clients') + ' from your list of 11. Most urgent first.'
    };
  }
}'''
build(OUT + '/ClientsList.dc.html', 'Clients', 'Clients', 1240, B1, S1, 'clients')

# 69. Sessions: Millicent's coaching and interview readiness
B2 = '''      <div style="display: flex; flex-direction: column; gap: 4px;">
        <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Sessions</h1>
        <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Millicent's week. Each client has 3 sessions included: kick-off, going through documents, and interview practice.</span>
      </div>
      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <section class="sb-card" style="flex: 3 1 560px; min-width: 0;" aria-labelledby="wk-h">
          <div class="sb-head"><h2 id="wk-h" class="sb-h2">Week starting Monday 2 November, and next week</h2><span class="sb-sub">All by video. Sessions start after handover. Clients book Millicent's open times in their Hub</span></div>
          <sc-for list="{{week}}" as="s" hint-placeholder-count="6">
            <div class="sb-row">
              <span style="width: 92px; flex-shrink: 0; display: flex; flex-direction: column;"><span class="sb-muted">{{s.day}}</span><span style="font-weight: 600;">{{s.time}}</span></span>
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{s.client}}</span><span class="sb-sub">{{s.what}}</span></span>
              <span class="{{s.cls}}">{{s.used}}</span>
              <button class="sb-btn b-sec">{{s.cta}}</button>
            </div>
          </sc-for>
        </section>
        <section class="sb-card" style="flex: 2 1 380px; min-width: 0;" aria-labelledby="iv-h">
          <div class="sb-head"><h2 id="iv-h" class="sb-h2">Interview readiness</h2><span class="sb-sub">Everyone with a regulator interview booked</span></div>
          <sc-for list="{{ready}}" as="r" hint-placeholder-count="4">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 6px;">
              <div style="display: flex; justify-content: space-between; gap: 8px;"><span style="font-weight: 500;">{{r.who}}</span><span class="sb-sub">{{r.when}}</span></div>
              <div class="bar" aria-hidden="true"><span class="{{r.bar}}"></span></div>
              <span class="sb-muted">{{r.note}}</span>
            </div>
          </sc-for>
        </section>
      </div>
      <section class="sb-card" aria-labelledby="nt-h">
        <div class="sb-head"><h2 id="nt-h" class="sb-h2">After a session: notes in 2 minutes</h2><span class="sb-sub">Saved to the client page. The client sees the summary and next steps, never the private notes</span></div>
        <div class="sb-row" style="align-items: flex-start; gap: 20px; flex-wrap: wrap;">
          <span style="flex: 1 1 260px; display: flex; flex-direction: column; gap: 4px;"><span class="sb-th">Session</span><span>Bright Path Care Ltd, session 1: kick-off and your plan (Tue 13 Oct)</span></span>
          <span style="flex: 1 1 260px; display: flex; flex-direction: column; gap: 4px;"><span class="sb-th">For the client</span><span>We agreed your plan and dates. Next: session 2 on Mon 2 Nov to go through your documents, with Daniel.</span></span>
          <span style="flex: 1 1 260px; display: flex; flex-direction: column; gap: 4px;"><span class="sb-th">Private note for the team</span><span>Joy is confident on the business side. Patience, the manager, would like help with the medication policy. Cover it in session 2.</span></span>
        </div>
      </section>
'''
S2 = r'''class Component extends DCLogic {
  renderVals() {
    const week = [
      ['Mon 2 Nov', '10:00', 'Bright Path Care Ltd', 'Session 2: going through documents, with Joy. Daniel joins as case owner', '2 of 3', 'info', 'Join'],
      ['Tue 3 Nov', '14:00', 'Willow Bank Supported Living Ltd', 'Session 2: going through documents, with David. Daniel joins, covering for Olu', '2 of 3', 'info', 'Prepare'],
      ['Thu 5 Nov', '11:00', 'Elm Tree Care Ltd', 'Session 3: interview practice for Claire (CQC interview Tue 24 Nov)', '3 of 3', 'warn', 'Prepare'],
      ['Mon 9 Nov', '10:00', 'Afon Care Ltd', 'Session 3: interview practice for Rhian (CIW suitability interview Thu 26 Nov)', '3 of 3', 'warn', 'Prepare'],
      ['Tue 10 Nov', '15:00', 'Westbrook Care Ltd', 'Extra session: interview practice for Leon. Included in the resubmission, at no charge to the client', 'Extra', 'brand', 'Prepare'],
      ['Wed 11 Nov', '10:00', 'Lagan View Care Ltd', 'Session 3: interview practice for Niamh and the manager (RQIA interviews Tue 8 Dec)', '3 of 3', 'warn', 'Prepare']
    ].map(([day, time, client, what, used, k, cta]) => ({ day, time, client, what, used, cls: 'sb-chip c-' + k, cta }));
    const ready = [
      ['Claire Hughes, Elm Tree (CQC)', 'Tue 24 Nov', 'w40', 'Interview portal 40% done. Practice on Thu 5 Nov. Weak spot: weekend cover'],
      ['Rhian, Afon Care (CIW)', 'Thu 26 Nov', 'w50', 'Interview portal half done. Practice on Mon 9 Nov. Knows her Statement of Purpose well'],
      ['Niamh and the manager, Lagan View (RQIA)', 'Tue 8 Dec', 'w30', 'Interview portal started. Practice on Wed 11 Nov. Weak spot: Minimum Standards on medicines'],
      ['Leon Grant, Westbrook (CQC resubmission)', 'After resubmission', 'w20', 'Extra practice on Tue 10 Nov, because CQC\'s refusal mentioned interview answers on safeguarding referrals']
    ].map(([who, when, bar, note]) => ({ who, when, bar, note }));
    return { theme: this.props.theme ?? 'light', three: 3, user: { name: 'Millicent', initials: 'MI' }, nav: __NAV__, week, ready };
  }
}'''
build(OUT + '/CoachSessions.dc.html', 'Sessions', 'Sessions', 975, B2, S2, 'sessions')

# 70. Client care: Divine's queue
B3 = '''      <div style="display: flex; flex-direction: column; gap: 4px;">
        <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Client care</h1>
        <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">How every client feels, and the calls that keep them close. Divine leads; anyone can pick up a call.</span>
      </div>
      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="4">
          <div class="sb-card sb-kpi"><span class="sb-kv">{{k.v}}</span><span class="sb-sub">{{k.k}}</span></div>
        </sc-for>
      </div>
      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <section class="sb-card" style="flex: 3 1 560px; min-width: 0;" aria-labelledby="cq-h">
          <div class="sb-head"><h2 id="cq-h" class="sb-h2">Calls and follow-ups, most urgent first</h2></div>
          <sc-for list="{{queue}}" as="q" hint-placeholder-count="6">
            <div class="sb-row" style="align-items: flex-start;">
              <span class="{{q.cls}}" style="width: 120px; justify-content: center;">{{q.kind}}</span>
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{q.client}}</span><span class="sb-sub">{{q.why}}</span></span>
              <span class="sb-sub" style="width: 120px; flex-shrink: 0;">{{q.due}}</span>
              <button class="sb-btn b-sec">{{q.cta}}</button>
            </div>
          </sc-for>
        </section>
        <section class="sb-card" style="flex: 2 1 340px; min-width: 0; padding-bottom: 8px;" aria-labelledby="fl-h">
          <div class="sb-head"><h2 id="fl-h" class="sb-h2">How clients feel</h2><span class="sb-sub">From calls, sessions and one-tap check-ins</span></div>
          <sc-for list="{{feel}}" as="f" hint-placeholder-count="3">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 6px;"><div style="display: flex; justify-content: space-between;"><span style="font-weight: 500;">{{f.k}}</span><span>{{f.v}}</span></div><div class="bar" aria-hidden="true"><span class="{{f.bar}}"></span></div></div>
          </sc-for>
          <div class="sb-row"><span class="sb-sub">Unhappy feedback goes to the manager, who calls within 1 working day (a director if the manager is involved) and shares it with the consultant with care. Worried clients get no sales or growth messages until it is resolved. The review invitation is never held back.</span></div>
        </section>
      </div>
'''
S3 = r'''class Component extends DCLogic {
  renderVals() {
    const queue = [
      ['Introduction call', 'warn', 'Meadow View Care Ltd', 'Paid today at 10:02. Target: within 2 working hours. The onboarding form goes after the call', 'By 12:02', 'Take the call'],
      ['Concern', 'bad', 'Riverside Homecare Ltd', 'Mark felt rushed on Friday\'s call. Acknowledged within 1 working day. Collins calls today, Daniel sends Collins notes first', 'Today', 'See the concern'],
      ['Gone quiet', 'warn', 'Greenway Support Ltd', 'No reply or upload for 10 days, 3 documents waiting. Friday\'s update bounced at 17:02, likely why. Daniel calls today', 'Today', 'Call'],
      ['Check-in', 'info', 'Westbrook Care Ltd', 'Refused, decision received Mon 26 Oct. A kind check-in a week after the decision, about how Sade is, not the paperwork', 'Today', 'Plan the call'],
      ['Review', 'ok', 'Brookside Homecare', 'Invited once, at registration 2 weeks ago, to review on Google or Trustpilot (Brookside chose). The one reminder went after 7 days. They left a Google review on Fri 30 Oct: reply within 2 working days', 'Tue 3 Nov', 'Reply'],
      ['Aftercare', 'neutral', 'Maple Court Care', 'Month 6 of 12. Monthly check-in with Daniel is booked', 'Mon 9 Nov', 'Open']
    ].map(([kind, k, client, why, due, cta]) => ({ kind, cls: 'sb-chip c-' + k, client, why, due, cta }));
    const kpis = [['1', 'introduction call today'], ['1', 'concern open'], ['1', 'client gone quiet'], ['46 of 52', 'clients happy']].map(([v, k]) => ({ v, k }));
    const feel = [['Happy', '46', 'w90'], ['Unsure', '5', 'w10'], ['Worried', '1', 'w5']].map(([k, v, bar]) => ({ k, v, bar }));
    return { theme: this.props.theme ?? 'light', three: 3, user: { name: 'Divine', initials: 'DV' }, nav: __NAV__, queue, kpis, feel };
  }
}'''
build(OUT + '/ClientCare.dc.html', 'Client care', 'Client care', 960, B3, S3, 'care')

# 71. Aftercare: 12 months after registration
B4 = '''      <div style="display: flex; flex-direction: column; gap: 4px;">
        <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Aftercare</h1>
        <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Clients in their 12 months of aftercare: their regulator's duties, the monthly check-in, and getting ready for the first inspection. Aftercare is included in the full start-up package only; other clients can buy it as an add-on.</span>
      </div>
''' + TABS + '''      <section class="sb-card" aria-label="Aftercare clients">
        <div class="sb-row" style="border-top: 0;"><span class="sb-th" style="flex: 2 1 200px;">Client</span><span class="sb-th" style="flex: 1 1 120px;">Month</span><span class="sb-th" style="flex: 2 1 260px;">Next regulator duty</span><span class="sb-th" style="flex: 1 1 150px;">Monthly check-in</span><span class="sb-th" style="flex: 1 1 150px;">First inspection</span><span class="sb-th" style="flex: 1 1 150px;">Growth</span></div>
        <sc-for list="{{rows}}" as="r" hint-placeholder-count="5">
          <div class="sb-row" style="align-items: flex-start;">
            <span style="flex: 2 1 200px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{r.name}}</span><span style="display: flex; gap: 6px; flex-wrap: wrap;"><span class="{{r.regCls}}">{{r.reg}}</span><span class="{{r.pkgCls}}">{{r.pkg}}</span></span></span>
            <span style="flex: 1 1 120px; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span class="sb-sub">{{r.month}}</span><span class="bar" aria-hidden="true"><span class="{{r.bar}}"></span></span></span>
            <span style="flex: 2 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span>{{r.duty}}</span><span class="{{r.dutyCls}}" style="align-self: flex-start;">{{r.dutyDue}}</span></span>
            <span style="flex: 1 1 150px; min-width: 0;" class="sb-sub">{{r.check}}</span>
            <span style="flex: 1 1 150px; min-width: 0;" class="sb-sub">{{r.insp}}</span>
            <span style="flex: 1 1 150px; min-width: 0;" class="sb-sub">{{r.grow}}</span>
          </div>
        </sc-for>
      </section>
      <span class="sb-muted">One growth idea at a time, no more than one new idea a month, and never during a concern or a refusal. The inspection readiness check is at month 4. At month 12 the consultant hands over with a summary of everything done and what is due next.</span>
'''
S4 = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { t: 'all' }; }
  renderVals() {
    const t = this.state.t;
    const R = [
      ['Brookside Homecare', 'CQC', 1, 'Tell CQC about any notifiable events as they happen. Check the provider portal account is set up', 'When Olu is back', 'neutral', 'Booked 12 Nov', 'Readiness check at month 4', 'Not yet, month 1', 'cqc', 'full'],
      ['Maple Court Care', 'CQC', 6, 'Provider Information Return if CQC asks. Keep the Statement of Purpose up to date', 'When asked', 'neutral', 'Booked 9 Nov', 'Mock inspection done, 2 actions', 'Supported living add-on: interested', 'cqc', 'full'],
      ['Bryn Glas Care', 'CIW', 4, 'RI visit and report (regulation 73), every 3 months', 'Due 30 Nov', 'warn', 'Booked 16 Nov', 'Readiness check (month 4) at the 16 Nov check-in', 'Tender for Powys home care', 'ciw', 'addon'],
      ['Bryn Glas Care', 'CIW', 4, 'Quality of care review (regulation 80), every 6 months', 'Due 31 Jan', 'neutral', '', '', '', 'ciw', 'addon'],
      ['Foyle Home Care', 'RQIA', 8, 'Monthly quality monitoring report by the registered person', 'Due 30 Nov', 'warn', 'Booked 20 Nov', 'First inspection was Good', 'Supported living: interested', 'rqia', 'addon'],
      ['Ashby Care', 'CQC', 12, 'Handover: summary of everything done and what is due next', 'Handover 18 Nov', 'info', 'Final check-in 18 Nov', 'Inspected: Good', 'Retained support, offered once', 'cqc', 'full']
    ];
    const T = [['all', 'All'], ['due', 'Duty due this month'], ['cqc', 'CQC'], ['ciw', 'CIW'], ['rqia', 'RQIA']];
    const rows = R.filter(r => t === 'all' || (t === 'due' ? r[5] === 'warn' : r[9] === t)).map(r => ({
      name: r[0], reg: r[1], regCls: 'sb-chip c-brand', pkg: r[10] === 'full' ? 'Full start-up' : 'Aftercare add-on', pkgCls: 'sb-chip ' + (r[10] === 'full' ? 'c-ok' : 'c-info'), month: 'Month ' + r[2] + ' of 12', bar: 'w' + Math.min(100, Math.round(r[2] / 12 * 20) * 5),
      duty: r[3], dutyDue: r[4], dutyCls: 'sb-chip c-' + r[5], check: r[6] || ' ', insp: r[7] || ' ', grow: r[8] || ' '
    }));
    return { theme: this.props.theme ?? 'light', three: 3, user: { name: 'Daniel Mensah', initials: 'DM' }, nav: __NAV__,
      tabs: T.map(([k, label]) => ({ label, on: t === k, off: t !== k, pick: () => this.setState({ t: k }) })), rows };
  }
}'''
build(OUT + '/AftercareStaff.dc.html', 'Aftercare', 'Aftercare', 950, B4, S4, 'after')

# 72. Reports for directors
B5 = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Reports</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">How the business is doing, and whether we keep our promises. Example figures for the design.</span>
        </div>
''' + TABS.replace('<div role="tablist"', '<div role="tablist" aria-label="Period"') .replace('aria-label="Show"', '') + '''      </div>
      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{kpis}}" as="k" hint-placeholder-count="8">
          <div class="sb-card sb-kpi"><span class="sb-muted">{{k.k}}</span><span class="sb-kv">{{k.v}}</span><span class="{{k.cls}}" style="align-self: flex-start;">{{k.note}}</span></div>
        </sc-for>
      </div>
      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <section class="sb-card" style="flex: 1 1 460px; min-width: 0; padding-bottom: 8px;" aria-labelledby="pr-h">
          <div class="sb-head"><h2 id="pr-h" class="sb-h2">Promises we make to clients</h2><span class="sb-sub">Target, and how often we met it</span></div>
          <sc-for list="{{promises}}" as="p" hint-placeholder-count="5">
            <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 6px;"><div style="display: flex; justify-content: space-between; gap: 8px;"><span style="font-weight: 500;">{{p.k}}</span><span>{{p.v}}</span></div><div class="bar" aria-hidden="true"><span class="{{p.bar}}"></span></div><span class="sb-muted">{{p.note}}</span></div>
          </sc-for>
        </section>
        <section class="sb-card" style="flex: 1 1 460px; min-width: 0; padding-bottom: 8px;" aria-labelledby="st-h">
          <div class="sb-head"><h2 id="st-h" class="sb-h2">Average days in each stage</h2><span class="sb-sub">Stages 1 to 10 of 11. Aftercare lasts 12 months</span></div>
          <sc-for list="{{stages}}" as="s" hint-placeholder-count="6">
            <div class="sb-row" style="gap: 12px;"><span style="width: 200px; flex-shrink: 0;">{{s.k}}</span><span class="bar" style="flex: 1;" aria-hidden="true"><span class="{{s.bar}}"></span></span><span style="width: 70px; text-align: right;">{{s.v}}</span></div>
          </sc-for>
          <div class="sb-row"><span class="sb-sub">With the regulator is outside our control. Of our own stages, documents is the slowest, mostly waiting for landlord letters and references. Starting both at the introduction call would save about a week.</span></div>
        </section>
      </div>
      <section class="sb-card" aria-labelledby="rg-h">
        <div class="sb-head"><h2 id="rg-h" class="sb-h2">Outcomes by regulator</h2><span class="sb-sub">Applications decided this quarter. A Notice of Proposal is not a decision yet, so it is counted separately</span></div>
        <div class="sb-row" style="border-top: 0;"><span class="sb-th" style="flex: 1;">Regulator</span><span class="sb-th" style="flex: 1;">Decided</span><span class="sb-th" style="flex: 1;">Registered first time</span><span class="sb-th" style="flex: 1;">Registered after a resubmission</span><span class="sb-th" style="flex: 1;">Refused</span><span class="sb-th" style="flex: 1;">Notice of Proposal open</span></div>
        <sc-for list="{{regs}}" as="g" hint-placeholder-count="4">
          <div class="{{g.cls}}"><span style="flex: 1; font-weight: 500;">{{g.r}}</span><span style="flex: 1;">{{g.d}}</span><span style="flex: 1;">{{g.f}}</span><span style="flex: 1;">{{g.a}}</span><span style="flex: 1;">{{g.x}}</span><span style="flex: 1;">{{g.n}}</span></div>
        </sc-for>
      </section>
      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <section class="sb-card" style="flex: 1 1 300px; min-width: 0;" aria-labelledby="td-h">
          <div class="sb-head"><h2 id="td-h" class="sb-h2">Tenders</h2><span class="sb-sub">Bids decided this quarter</span></div>
          <sc-for list="{{tenders}}" as="x" hint-placeholder-count="5">
            <div class="sb-row"><span style="flex: 1; min-width: 0;">{{x.k}}</span><span style="font-weight: 500; text-align: right;">{{x.v}}</span></div>
          </sc-for>
        </section>
        <section class="sb-card" style="flex: 1 1 360px; min-width: 0;" aria-labelledby="fb-h">
          <div class="sb-head"><h2 id="fb-h" class="sb-h2">Feedback by consultant</h2><span class="sb-sub">% happy. One tap, three faces, at three moments</span></div>
          <div class="sb-row" style="border-top: 0; gap: 8px;"><span class="sb-th" style="flex: 1.6;">Consultant</span><span class="sb-th" style="flex: 1;">After onboarding</span><span class="sb-th" style="flex: 1;">After submission</span><span class="sb-th" style="flex: 1;">After the decision</span></div>
          <sc-for list="{{feedback}}" as="f" hint-placeholder-count="3">
            <div class="sb-row" style="gap: 8px; align-items: flex-start;"><span style="flex: 1.6; min-width: 0; display: flex; flex-direction: column;"><span style="font-weight: 500;">{{f.who}}</span><span class="sb-muted">{{f.note}}</span></span><span style="flex: 1;">{{f.a}}</span><span style="flex: 1;">{{f.b}}</span><span style="flex: 1;">{{f.c}}</span></div>
          </sc-for>
        </section>
        <section class="sb-card" style="flex: 1 1 300px; min-width: 0;" aria-labelledby="fr-h">
          <div class="sb-head"><h2 id="fr-h" class="sb-h2">Resubmissions this year</h2><span class="sb-sub">Our promise if a regulator refuses: included, at no charge to the client</span></div>
          <sc-for list="{{resub}}" as="x" hint-placeholder-count="4">
            <div class="sb-row"><span style="flex: 1; min-width: 0;">{{x.k}}</span><span style="font-weight: 500; text-align: right;">{{x.v}}</span></div>
          </sc-for>
          <div class="sb-row"><span class="sb-sub">Staff time we absorb. Hours come from the time log on each resubmission project, and match the manager dashboard.</span></div>
        </section>
      </div>
'''
S5 = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { t: 'q' }; }
  renderVals() {
    const t = this.state.t;
    const T = [['m', 'This month'], ['q', 'This quarter'], ['y', 'This year']];
    const G = (id, fb) => (window.CSR ? window.CSR.get(id, fb) : fb);
    const kpis = [
      ['Active clients', '52', '+6 this quarter', 'ok'], ['New clients', '14', '9 CQC, 2 CIW, 1 RQIA, 2 tender', 'neutral'], ['Registered', '10', 'all first time this quarter', 'ok'], ['Tender win rate', '50%', '4 of 8 bids decided', 'info'],
      ['Paid on time', '82%', '2 overdue, reminders running', 'warn'], ['Average days to send', '62', 'from paying to sending (stages 1 to 6)', 'neutral'], ['Clients happy', '88%', '46 of 52. 1 worried', 'ok'], ['Reviews', '7', 'from 10 invitations, 1 per registered client', 'neutral']
    ].map(([k, v, note, c]) => ({ k, v, note, cls: 'sb-chip c-' + c }));
    const promises = [
      ['Introduction call within 2 working hours', '91%', 'w90', '2 late this quarter, both on busy Mondays'],
      ['Reply to client questions within ' + G('reply-client', '1 working day'), '97%', 'w95', 'Average reply 3 hours'],
      ['Weekly update every ' + G('weekly-update-day', 'Friday') + ' by ' + G('weekly-update-time', '16:00'), '94%', 'w95', '1 bounced on Fri 30 Oct (Greenway), being fixed today'],
      ['Tell the client the same day the regulator writes', '100%', 'w100', ''],
      ['Concerns acknowledged within 1 working day', '100%', 'w100', '1 open (Riverside), acknowledged']
    ].map(([k, v, bar, note]) => ({ k, v, bar, note }));
    const stages = [['1 Welcome and onboarding', '9 days', 'w10'], ['2 CV review', '3 days', 'w5'], ['3 Your documents', '19 days', 'w25'], ['4 Drafting', '21 days', 'w25'], ['5 Your review', '6 days', 'w10'], ['6 Final pack sign-off', '4 days', 'w5'], ['7 Submitted', '1 day', 'w5'], ['8 With the regulator', '81 days', 'w100'], ['9 Interview', '12 days', 'w15'], ['10 Outcome', '9 days', 'w10']].map(([k, v, bar]) => ({ k, v, bar }));
    const R = [['CQC', 8, 7, 0, 1, 1], ['CIW', 2, 2, 0, 0, 0], ['RQIA', 1, 1, 0, 0, 0]];
    const sum = i => R.reduce((a, r) => a + r[i], 0);
    const regs = R.concat([['All', sum(1), sum(2), sum(3), sum(4), sum(5)]]).map(([r, d, f, a, x, n]) => ({ r, d: String(d), f: String(f), a: String(a), x: String(x), n: String(n), cls: 'sb-row' + (r === 'All' ? '' : '') }));
    const tenders = [['Bids decided', '8'], ['Won', '4 (50%)'], ['Lost', '4'], ['Value of contracts won', '£2.4m over the contract terms'], ['In progress', '2: Northshire Lot 1 North (we submit Fri 27 Nov), Eastford']].map(([k, v]) => ({ k, v }));
    const feedback = [['Daniel Mensah', '100%', '100%', '75%', '9 replies. Most praised for clear Friday updates'], ['Olu', '100%', '67%', '100%', '7 replies. 1 worried after submission (Riverside)'], ['Sam Patel', '100%', '100%', '100%', '6 replies. Leaving Fri 6 Nov']].map(([who, a, b, c, note]) => ({ who, a, b, c, note }));
    const resub = [['Resubmissions this year', '2'], ['Registered after resubmitting', '1 earlier client, July: 31 hours'], ['In progress', 'Westbrook: 14 hours so far'], ['Staff hours this year', '45 hours in total']].map(([k, v]) => ({ k, v }));
    return { theme: this.props.theme ?? 'light', three: 3, user: { name: 'Collins', initials: 'C' }, nav: __NAV__,
      tabs: T.map(([k, label]) => ({ label, on: t === k, off: t !== k, pick: () => this.setState({ t: k }) })), kpis, promises, stages, regs, tenders, feedback, resub };
  }
}'''
build(OUT + '/Reports.dc.html', 'Reports', 'Reports', 1780, B5, S5, 'reports')
