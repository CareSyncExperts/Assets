import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from phoneboard import build, tabs
BODY = tabs('Demo: the three parts of your tender workspace', 'Tender workspace') + '''
  <div style="padding: 20px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 2px;">
      <span class="pb-sub">Oakleaf Living. Your bid lead: Daniel</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">{{heading}}</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">{{intro}}</span>
    </header>

    <sc-if value="{{isWeek}}" hint-placeholder-val="{{ true }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-card">
          <sc-for list="{{week}}" as="w" hint-placeholder-count="5">
            <div class="pb-row">
              <span style="width: 58px; flex-shrink: 0; display: flex; flex-direction: column;"><span style="font-size: 12px; line-height: 16px; color: var(--cs-text-muted);">{{w.dow}}</span><span style="font-size: 16px; line-height: 22px; font-weight: 600;">{{w.date}}</span></span>
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{w.text}}</span><span class="pb-muted">{{w.bid}}. {{w.time}}</span>
                <sc-if value="{{w.canPass}}" hint-placeholder-val="{{ false }}"><button class="pb-link" style="align-self: flex-start; min-height: 32px; font-size: 13px;">Pass to someone in your team</button></sc-if>
              </span>
              <button class="pb-btn pb-sec">{{w.cta}}</button>
            </div>
          </sc-for>
        </div>
        <div class="pb-note n-info">Everything across all your bids, in date order. Our dates leave time before each buyer's deadline, so nothing is rushed at the end.</div>
      </div>
    </sc-if>

    <sc-if value="{{isDocs}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-note n-ok">Upload each document once. We use the latest version in every bid, and tell you a month before anything expires or goes out of date.</div>
        <div class="pb-card">
          <sc-for list="{{docs}}" as="d" hint-placeholder-count="8">
            <div class="pb-row">
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{d.name}}</span><span class="pb-muted">{{d.meta}}</span></span>
              <span class="{{d.cls}}">{{d.state}}</span>
            </div>
          </sc-for>
        </div>
        <button class="pb-btn pb-pri" style="min-height: 48px;">Upload a document</button>
      </div>
    </sc-if>

    <sc-if value="{{isSign}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 4px;">
          <span class="pb-muted">Northshire home support, lot 1</span>
          <span style="font-size: 16px; line-height: 24px; font-weight: 500;">We submit by Friday 27 November, 12:00</span>
          <span class="pb-sub">The buyer's deadline is Tuesday 1 December, 12:00. We keep two working days spare in case the portal has problems.</span>
        </div>
        <h2 class="pb-h2">1. Read the drafts</h2>
        <div class="pb-card">
          <sc-for list="{{drafts}}" as="q" hint-placeholder-count="5">
            <div class="pb-row">
              <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{q.name}}</span><span class="pb-muted">{{q.meta}}</span></span>
              <span class="{{q.cls}}">{{q.state}}</span>
            </div>
          </sc-for>
        </div>
        <h2 class="pb-h2">2. Approve for submission</h2>
        <div class="pb-card" style="padding: 6px 0;">
          <sc-for list="{{checks}}" as="c" hint-placeholder-count="4">
            <sc-if value="{{c.on}}" hint-placeholder-val="{{ false }}"><button role="checkbox" aria-checked="true" onClick="{{c.flip}}" style="width: 100%; min-height: 48px; padding: 8px 16px; border: 0; background: transparent; font: inherit; font-size: 14px; line-height: 20px; text-align: left; display: flex; gap: 12px; align-items: center; color: var(--cs-text-primary); cursor: pointer;"><span aria-hidden="true" style="width: 20px; height: 20px; flex-shrink: 0; border-radius: 5px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center; font-size: 13px;">✓</span>{{c.text}}</button></sc-if>
            <sc-if value="{{c.off}}" hint-placeholder-val="{{ true }}"><button role="checkbox" aria-checked="false" onClick="{{c.flip}}" style="width: 100%; min-height: 48px; padding: 8px 16px; border: 0; background: transparent; font: inherit; font-size: 14px; line-height: 20px; text-align: left; display: flex; gap: 12px; align-items: center; color: var(--cs-text-primary); cursor: pointer;"><span aria-hidden="true" style="width: 20px; height: 20px; flex-shrink: 0; border-radius: 5px; border: 2px solid var(--cs-border-control); box-sizing: border-box;"></span>{{c.text}}</button></sc-if>
          </sc-for>
        </div>
        <sc-if value="{{ready}}" hint-placeholder-val="{{ false }}"><button class="pb-btn pb-pri" style="min-height: 52px; font-size: 16px;" onClick="{{approve}}">I approve. Please submit this bid</button></sc-if>
        <sc-if value="{{notReady}}" hint-placeholder-val="{{ true }}"><button class="pb-btn pb-dis" style="min-height: 52px; font-size: 16px;" aria-disabled="true">Tick each item to approve</button></sc-if>
        <sc-if value="{{approved}}" hint-placeholder-val="{{ false }}"><div class="pb-note n-ok">Approved by Kemi at 16:42. Daniel submits by Friday 27 November and sends you the portal receipt the same day.</div></sc-if>
      </div>
    </sc-if>
    <sc-if value="{{isPast}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px;">
          <sc-for list="{{stats}}" as="st" hint-placeholder-count="3">
            <div class="pb-card" style="padding: 12px; display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 20px; line-height: 28px; font-weight: 600;">{{st.v}}</span><span class="pb-muted">{{st.k}}</span></div>
          </sc-for>
        </div>
        <div class="pb-card">
          <sc-for list="{{past}}" as="b" hint-placeholder-count="4">
            <div class="pb-row" style="flex-direction: column; gap: 6px;">
              <div style="display: flex; gap: 10px; width: 100%;"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{b.name}}</span><span class="pb-muted">{{b.meta}}</span></span><span class="{{b.cls}}">{{b.result}}</span></div>
              <span class="pb-sub">{{b.note}}</span>
            </div>
          </sc-for>
        </div>
        <h2 class="pb-h2">Contracts coming up for renewal</h2>
        <div class="pb-card">
          <sc-for list="{{renew}}" as="n" hint-placeholder-count="2">
            <div class="pb-row"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{n.name}}</span><span class="pb-muted">{{n.meta}}</span></span><span class="pb-chip c-info">{{n.when}}</span></div>
          </sc-for>
        </div>
        <div class="pb-note n-ok">Every answer you have submitted is kept, with the buyer's scores and feedback, so your best answers are reused and improved for the next bid.</div>
      </div>
    </sc-if>
  </div>
'''
SCRIPT = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { tab: 'week', c: [true, true, false, false], approved: false }; }
  renderVals() {
    const { tab, c, approved } = this.state;
    const T = [['week', 'This week'], ['docs', 'Documents'], ['sign', 'Review and sign-off'], ['past', 'Past bids']];
    const heads = { week: ['What we need from you', '5 things across 2 bids. The next one is due on Friday.'], docs: ['Your tender documents', 'One store for every bid.'], sign: ['Review and sign-off', 'Read the drafts, then approve once. We never submit without your approval.'], past: ['Your past bids', 'Results, scores and feedback, and what is coming up for renewal.'] };
    const week = [
      ['Fri', '13 Nov', 'One case study about a hospital discharge', 'Northshire home support', 'About 15 minutes', 'Add it', false],
      ['Mon', '16 Nov', 'Staff numbers and turnover for the workforce answer', 'Northshire home support', 'About 10 minutes', 'Add them', true],
      ['Tue', '17 Nov', 'Decide: go for lots 1 and 3?', 'Eastford supported living framework', 'Read our advice first', 'Decide', false],
      ['Fri', '20 Nov', 'Read and comment on the draft answers', 'Northshire home support', 'About 40 minutes', 'Open', false],
      ['Wed', '25 Nov', 'Approve your prices and the bid for submission', 'Northshire home support', 'About 10 minutes', 'Review', false]
    ].map(([dow, date, text, bid, time, cta, canPass]) => ({ dow, date, text, bid, time, cta, canPass }));
    const docs = [
      ['Employer\'s liability insurance', 'Expires 31 March 2027. Used in 3 bids', 'In date', 'ok'],
      ['Public liability insurance', 'Expires 31 March 2027. Used in 3 bids', 'In date', 'ok'],
      ['Accounts for 2024 to 2025', 'Used in 4 bids', 'In date', 'ok'],
      ['Safeguarding policy', 'Reviewed January 2026', 'In date', 'ok'],
      ['Business continuity plan', 'Last reviewed 2023. Buyers usually want one reviewed in the last 12 months', 'Review due', 'warn'],
      ['Training matrix', 'Northshire asks for it', 'Missing', 'bad'],
      ['Modern slavery statement', 'Used in 2 bids', 'In date', 'ok'],
      ['Social value plan', 'We draft this with you for each bid', 'Per bid', 'neutral']
    ].map(([name, meta, state, k]) => ({ name, meta, state, cls: 'pb-chip c-' + k }));
    const drafts = [
      ['Quality and person-centred care (40% of the marks)', 'Draft ready. You left 2 comments, both answered', 'Read', 'ok'],
      ['Safeguarding (15%)', 'Draft ready', 'To read', 'warn'],
      ['Workforce (20%)', 'Waiting for your staff figures', 'Needs you', 'bad'],
      ['Social value (10%)', 'Draft ready', 'To read', 'warn'],
      ['Pricing schedule (15%)', 'Hourly rates prepared with you on 6 November', 'To approve', 'warn']
    ].map(([name, meta, state, k]) => ({ name, meta, state, cls: 'pb-chip c-' + k }));
    const ct = ['I have read every answer', 'I approve the prices', 'I have checked the declarations the buyer asks for', 'I authorise Care Sync Experts to submit this bid for us'];
    const checks = ct.map((text, i) => ({ text, on: !!c[i], off: !c[i], flip: () => { const n = c.slice(); n[i] = !n[i]; this.setState({ c: n, approved: false }); } }));
    const ready = c.every(Boolean) && !approved;
    return {
      theme: this.props.theme ?? 'light',
      tabs: T.map(([k, label]) => ({ label, on: tab === k, off: tab !== k, pick: () => this.setState({ tab: k }) })),
      heading: heads[tab][0], intro: heads[tab][1],
      isWeek: tab === 'week', isDocs: tab === 'docs', isSign: tab === 'sign', isPast: tab === 'past',
      stats: [['2 of 4', 'bids won'], ['£1.1m', 'contracts won'], ['74%', 'average score']].map(([v, k]) => ({ v, k })),
      past: [['Brookside home care', 'Submitted November 2025. Lot 1', 'Won', 'ok', 'Scored 81%. Highest marks for safeguarding. Contract started March 2026.'], ['Riverbank, lot 2', 'Submitted October 2025', 'Not this time', 'neutral', 'Scored 68%. Feedback used to improve 3 answers. The framework reopens in April and we will remind you.'], ['Westvale community support', 'Submitted 28 October 2026', 'Waiting', 'warn', 'The buyer expects to decide in early December.'], ['Ashby reablement', 'Submitted June 2025', 'Won', 'ok', 'Scored 72%. Two-year contract with an option to extend.']].map(([name, meta, result, k, note]) => ({ name, meta, result, note, cls: 'pb-chip c-' + k })),
      renew: [['Ashby reablement', 'Ends June 2027. The council usually re-tenders 6 months before', 'Re-tender likely Dec 2026'], ['Brookside home care', 'Ends March 2029, option to extend 1 year', '2028']].map(([name, meta, when]) => ({ name, meta, when })),
      week, docs, drafts, checks, ready, notReady: !c.every(Boolean) && !approved, approved,
      approve: () => this.setState({ approved: true })
    };
  }
}'''
build(sys.argv[1], 'Tender workspace', 1500, BODY, SCRIPT)
