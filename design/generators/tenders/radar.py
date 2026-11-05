import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from staffboard import build
OUT = '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/hub-canvas/project/Radar.dc.html'
H = 1320

CSS = '''main{max-width:none!important}
.rd-tl{display:flex;flex-direction:column;gap:10px;padding:16px;border-radius:12px;background:var(--cs-surface-raised);box-shadow:var(--cs-elevation-1)}
.rd-sel{outline:2px solid var(--cs-action-primary)}
.rd-kpi{padding:12px;border-radius:10px;background:var(--cs-surface-page);display:flex;flex-direction:column}
.rd-box{padding:14px;border-radius:10px;border:1px solid var(--cs-border-subtle);display:flex;flex-direction:column;gap:6px}
.rd-warn{background:var(--cs-status-warning-bg);border-color:transparent}
.rd-mr{padding:12px 14px;display:flex;gap:12px;align-items:flex-start;border-top:1px solid var(--cs-border-subtle);font-size:14px;line-height:20px}
.rd-mr:first-child{border-top:0}
.rd-lock{border:1px dashed var(--cs-border-default);background:var(--cs-surface-subtle);color:var(--cs-text-muted);cursor:not-allowed}
'''

BODY = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Tender Radar</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Mon 2 Nov. 12 new today from BidSuite, Find a Tender and council portals. Eligibility comes from each provider's real registration status on the CQC register and in our client records.</span>
        </div>
        <div role="tablist" aria-label="Radar lists" style="display: flex; gap: 6px; flex-wrap: wrap;">
          <sc-for list="{{tabs}}" as="tb" hint-placeholder-count="4">
            <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
            <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
          </sc-for>
        </div>
      </div>

      <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 16px; border-radius: 12px; background: var(--cs-status-info-bg); color: var(--cs-status-info-text);">
        <x-import component-from-global-scope="CareSync.Icon" name="shield-check" size="{{n20}}"></x-import>
        <span style="font-size: 14px; line-height: 20px; color: var(--cs-text-primary);">Existing Care Sync clients are never contacted by sales directly. Each match goes to the client's case owner first, and sales waits until the case owner agrees. The client decides whether to bid. When there is a capacity or same-lot question, a director accepts the bid work on the manager dashboard.</span>
      </div>

      <div style="display: flex; gap: 24px; flex-wrap: wrap; align-items: flex-start;">
        <section aria-label="{{listLabel}}" style="flex: 2 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 10px;">
          <sc-for list="{{cards}}" as="c" hint-placeholder-count="4">
            <div class="{{c.cls}}">
              <div style="display: flex; justify-content: space-between; gap: 8px; align-items: flex-start;"><span style="font-size: 16px; line-height: 24px; font-weight: 500;">{{c.title}}</span><span class="{{c.chipCls}}">{{c.chip}}</span></div>
              <span style="font-size: 14px; line-height: 20px; color: var(--cs-text-secondary);">{{c.sub}}</span>
              <div style="display: flex; gap: 16px; flex-wrap: wrap; font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);"><span>{{c.a}}</span><span>{{c.b}}</span><span style="color: var(--cs-text-brand); font-weight: 500;">{{c.c}}</span></div>
            </div>
          </sc-for>
          <span class="sb-muted">{{listNote}}</span>
        </section>

        <section aria-labelledby="d-h" class="sb-card" style="flex: 3 1 620px; min-width: 0; padding: 24px; display: flex; flex-direction: column; gap: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; flex-wrap: wrap;">
            <div style="display: flex; flex-direction: column; gap: 2px;">
              <h2 id="d-h" style="margin: 0; font-size: 22px; line-height: 30px; font-weight: 500;">Northshire County Council home care framework 2027</h2>
              <span style="font-size: 14px; line-height: 20px; color: var(--cs-text-secondary);">Framework with 2 lots: Lot 1 North and Lot 2 South. Light touch. Reference NS/2026/114.</span>
            </div>
            <x-import component-from-global-scope="CareSync.Button" variant="ghost" size="small" icon-end="external-link">Open pack</x-import>
          </div>

          <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
            <sc-for list="{{kpis}}" as="k" hint-placeholder-count="4">
              <div class="rd-kpi"><span class="sb-muted">{{k.k}}</span><span style="font-size: 16px; line-height: 24px; font-weight: 500;">{{k.v}}</span></div>
            </sc-for>
          </div>

          <div style="display: flex; gap: 12px; flex-wrap: wrap;">
            <div class="rd-box" style="flex: 1 1 260px;">
              <span style="font-size: 14px; line-height: 20px; font-weight: 500;">Key eligibility</span>
              <span class="sb-sub">Registered with CQC for personal care. Rated Good, or newly registered and not yet rated. Office within the county. Employer's liability £10m. A company still applying for registration is not eligible.</span>
            </div>
            <div class="rd-box rd-warn" style="flex: 1 1 260px;">
              <span style="font-size: 14px; line-height: 20px; font-weight: 500; color: var(--cs-status-warning-text); display: inline-flex; align-items: center; gap: 6px;"><x-import component-from-global-scope="CareSync.Icon" name="triangle-alert" size="{{n16}}"></x-import>Conflict check: 1 client already bidding</span>
              <span style="font-size: 13px; line-height: 18px; color: var(--cs-text-primary);">1 client already bidding on this tender: Oakleaf Living (Lot 1 North). Any new client or provider on Lot 1 North would bid against Oakleaf, so they are flagged as a conflict and not offered. Lot 2 South: no conflict.</span>
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 12px; flex-wrap: wrap;"><h3 style="margin: 0; font-size: 16px; line-height: 24px; font-weight: 500;">Our clients on this tender</h3><span class="sb-sub">Never called by sales. The case owner decides first</span></div>
            <div style="border: 1px solid var(--cs-border-subtle); border-radius: 10px; overflow: hidden;">
              <div class="rd-mr">
                <span class="sb-chip c-info">Bidding</span>
                <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">Oakleaf Living Ltd</span><span class="sb-sub">Already bidding on Lot 1 North. Case owner Daniel. Care Sync submits Fri 27 Nov</span></span>
              </div>
              <div class="rd-mr" style="flex-direction: column; gap: 10px;">
                <div style="display: flex; gap: 12px; align-items: flex-start; width: 100%;">
                  <span class="{{bsChipCls}}">{{bsChip}}</span>
                  <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">Brookside Homecare</span><span class="sb-sub">Registered with CQC 2 weeks ago, not yet rated, so eligible. Aftercare month 1. Lot 2 South, no conflict with Oakleaf</span><span style="font-size: 13px; line-height: 18px; color: var(--cs-text-primary);">{{bsText}}</span></span>
                  <sc-if value="{{bsLocked}}" hint-placeholder-val="{{ true }}"><button class="sb-btn rd-lock" aria-disabled="true">Contact locked</button></sc-if>
                  <sc-if value="{{bsCanCall}}" hint-placeholder-val="{{ false }}"><button class="sb-btn b-pri" onClick="{{bsTask}}">{{bsTaskLabel}}</button></sc-if>
                </div>
                <div style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;" role="tablist" aria-label="Olu's answer, demo">
                  <span class="sb-muted">Demo, Olu's answer:</span>
                  <sc-for list="{{bsStates}}" as="s" hint-placeholder-count="3">
                    <sc-if value="{{s.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{s.pick}}">{{s.label}}</button></sc-if>
                    <sc-if value="{{s.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{s.pick}}">{{s.label}}</button></sc-if>
                  </sc-for>
                </div>
              </div>
              <div class="rd-mr">
                <span class="sb-chip c-neutral">Not eligible yet</span>
                <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">Harbour Lane Care Ltd</span><span class="sb-sub">Not eligible yet: not registered. Stage 1 of 11, onboarding checks. Not suggested to anyone. The Radar looks again once CQC registers them</span></span>
              </div>
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 12px; flex-wrap: wrap;"><h3 style="margin: 0; font-size: 16px; line-height: 24px; font-weight: 500;">Providers to call, Lot 2 South only</h3><span class="sb-sub">Not our clients. All screened against TPS and CTPS in the last 28 days</span></div>
            <div style="border: 1px solid var(--cs-border-subtle); border-radius: 10px; overflow: hidden;">
              <sc-for list="{{providers}}" as="p" hint-placeholder-count="4">
                <div class="rd-mr" style="align-items: center;">
                  <span class="{{p.cls}}">{{p.tag}}</span>
                  <span style="flex: 1; min-width: 0;"><span style="font-weight: 500;">{{p.name}}</span> <span class="sb-sub">{{p.why}}</span></span>
                  <span class="sb-muted">{{p.conf}}</span>
                </div>
              </sc-for>
              <div class="rd-mr"><span class="sb-sub">And 10 more providers for Lot 2 South, all rated Good or newly registered.</span></div>
            </div>
          </div>

          <sc-if value="{{created}}" hint-placeholder-val="{{ false }}"><div role="status" style="padding: 12px 14px; border-radius: 10px; background: var(--cs-status-success-bg); color: var(--cs-status-success-text); font-size: 14px; line-height: 20px; font-weight: 500;">12 call tasks created for Jo, all Lot 2 South. Brookside is not included: Daniel decides first.</div></sc-if>
          <div style="display: flex; gap: 10px; justify-content: flex-end; flex-wrap: wrap;">
            <button class="sb-btn b-gh">Not for outreach</button>
            <sc-if value="{{notCreated}}" hint-placeholder-val="{{ true }}"><button class="sb-btn b-pri" onClick="{{create}}">Create 12 provider call tasks</button></sc-if>
          </div>
        </section>
      </div>
'''

SCRIPT = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { t: 'review', bs: 'wait', created: false, task: false }; }
  renderVals() {
    const { t, bs, created, task } = this.state;
    const chip = k => 'sb-chip c-' + k;
    const BS = {
      wait: ['Suggested to Olu', 'warn', 'Suggested to Olu (case owner) on Mon 2 Nov, 09:40. Olu is on leave until Mon 9 Nov. Brookside is not one of the 4 clients in Daniel\'s cover this week, and it is not urgent, so it waits for Olu. Sales cannot contact until Olu agrees.'],
      yes: ['Olu agreed', 'ok', 'Olu agreed and told Brookside first. Jo can now book a tender planning call. If Brookside decides to bid on Lot 2 South, Collins checks capacity and accepts the bid work on the manager dashboard.'],
      no: ['Olu said no', 'neutral', 'Olu said no for now: Brookside is settling in after registration. Not contacted. The Radar asks Olu again at month 3.']
    };
    const C = {
      review: [
        ['Northshire home care framework 2027', 'Go', 'ok', 'Northshire County Council. 2 lots. Framework.', 'Bid deadline Tue 1 Dec, 12:00', '21 working days', '1 client bidding, 1 client match, 12 providers', true],
        ['Supported Living Framework 2027', 'Check', 'warn', 'Westvale Borough Council. 4 lots. Rating rule unclear.', 'Closes Fri 11 Dec', '29 working days', 'No eligible clients, 9 providers', false],
        ['Reablement Care Service', 'Too close', 'bad', 'Eastmoor City Council. 1 lot. Block contract.', 'Closes Thu 19 Nov', '13 working days', 'Under 15 working days: flagged to Collins', false],
        ['Autism Community Support Service', 'Go', 'ok', 'Northshire County Council. 1 lot. Dynamic market.', 'Closes Fri 18 Dec', '34 working days', 'No eligible clients, 6 providers', false]
      ],
      owner: [
        ['Brookside Homecare', BS[bs][0], BS[bs][1], 'Northshire home care framework 2027, Lot 2 South. Case owner Olu.', 'Suggested Mon 2 Nov', 'Bid deadline Tue 1 Dec, 12:00', 'Sales cannot contact until Olu agrees', false]
      ],
      bidding: [
        ['Northshire home care framework 2027', 'Writing', 'info', 'Oakleaf Living. Lot 1 North. Bid written in Word by the bid team.', 'Clarifications close Fri 13 Nov, 17:00', 'Bid deadline Tue 1 Dec, 12:00', 'Care Sync submits Fri 27 Nov', false],
        ['Eastford Borough Council supported living', 'Deciding scope', 'info', 'Oakleaf Living. Dynamic purchasing system.', 'Application deadline Fri 4 Dec', 'Profile check under way', 'Case owner Daniel', false]
      ],
      closed: [
        ['Riverbank home care, lot 2', 'Not this time', 'neutral', 'Oakleaf Living. Submitted October 2025.', 'Scored 68%', 'Reopens April 2027', 'Daniel reminds Kemi', false]
      ]
    };
    const notes = { review: 'Showing 4 of 12 new today. The other 8 have no eligible clients and no providers in range.', owner: 'A suggestion stays here until the case owner answers. Sales sees it but cannot call.', bidding: 'Open the Tenders list for each bid record.', closed: 'Results and feedback are kept on each tender record.' };
    const T = [['review', 'To review (4)'], ['owner', 'Waiting for case owner (' + (bs === 'wait' ? 1 : 0) + ')'], ['bidding', 'Bidding (2)'], ['closed', 'Closed (1)']];
    const cards = C[t].map(r => ({ title: r[0], chip: r[1], chipCls: chip(r[2]), sub: r[3], a: r[4], b: r[5], c: r[6], cls: 'rd-tl' + (r[7] ? ' rd-sel' : '') }));
    const providers = [
      ['Provider', 'neutral', 'Meadowbank Home Support', 'Rated Good. Office in Lot 2 South. CQC register', 'High confidence'],
      ['Provider', 'neutral', 'Kestrel Care at Home', 'Rated Good. Lot 2 South, 4 miles over the border. The pack allows it', 'High confidence'],
      ['Conflict', 'warn', 'Larkspur Care', 'Office in Lot 1 North only, so it would bid against Oakleaf. Not offered', 'Excluded'],
      ['Excluded', 'bad', 'Holmfield Homecare', 'Rated Requires Improvement, below the minimum', 'Excluded']
    ].map(p => ({ tag: p[0], cls: chip(p[1]), name: p[2], why: p[3], conf: p[4] }));
    return {
      theme: this.props.theme ?? 'light', three: 3, n16: 16, n20: 20,
      user: { name: 'Jo Martin', initials: 'JM' },
      nav: __NAV__,
      tabs: T.map(([k, label]) => ({ label, on: t === k, off: t !== k, pick: () => this.setState({ t: k }) })),
      listLabel: T.find(x => x[0] === t)[1], cards, listNote: notes[t],
      kpis: [['Clarifications close', 'Fri 13 Nov, 17:00'], ['Bid deadline', 'Tue 1 Dec, 12:00'], ['Working days left', '21 (we submit in 19)'], ['Scoring', '60 / 30 / 10']].map(([k, v]) => ({ k, v })),
      bsChip: BS[bs][0], bsChipCls: chip(BS[bs][1]), bsText: BS[bs][2] + (bs === 'yes' && task ? ' Call task created for Jo.' : ''),
      bsLocked: bs !== 'yes', bsCanCall: bs === 'yes', bsTaskLabel: task ? 'Call task created' : 'Create call task for Jo',
      bsTask: () => this.setState({ task: true }),
      bsStates: [['wait', 'Waiting for Olu'], ['yes', 'Olu agreed'], ['no', 'Olu said no']].map(([k, label]) => ({ label, on: bs === k, off: bs !== k, pick: () => this.setState({ bs: k, task: false }) })),
      providers, created, notCreated: !created, create: () => this.setState({ created: true })
    };
  }
}'''

build(OUT, 'Tender Radar', 'Tender Radar', H, BODY, SCRIPT, 'tenders', CSS)
s = open(OUT).read().replace('"$preview":{"width":1440,', '"$preview":{"width":2158,')
open(OUT, 'w').write(s)
