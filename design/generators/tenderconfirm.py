import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from phoneboard import build
BODY = '''  <div style="padding: 24px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 4px;">
      <span style="font-size: 13px; line-height: 18px; color: var(--cs-text-brand); font-weight: 500;">New tender: Eastford supported living framework</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">Check what we hold, then 3 new questions</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Your tender profile is kept for every bid. Nothing to retype: confirm each part, or change it if it is out of date.</span>
    </header>
    <div style="display: flex; flex-direction: column; gap: 6px;">
      <div style="display: flex; justify-content: space-between;"><span class="pb-sub">{{doneText}}</span><span class="pb-sub">About 10 minutes</span></div>
      <div aria-hidden="true" style="height: 8px; border-radius: 999px; background: var(--cs-surface-subtle); overflow: hidden;"><div class="{{barCls}}" style="height: 8px; border-radius: 999px; background: var(--cs-action-primary);"></div></div>
    </div>

    <h2 class="pb-h2">What we hold</h2>
    <div class="pb-card">
      <sc-for list="{{held}}" as="h" hint-placeholder-count="6">
        <div class="pb-row" style="flex-direction: column; gap: 8px;">
          <div style="display: flex; gap: 10px; align-items: flex-start; width: 100%;">
            <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{h.name}}</span><span style="font-size: 14px; line-height: 20px;">{{h.value}}</span><span class="pb-muted">{{h.meta}}</span></span>
            <span class="{{h.cls}}">{{h.state}}</span>
          </div>
          <sc-if value="{{h.ask}}" hint-placeholder-val="{{ true }}">
            <div style="display: flex; gap: 8px;"><button class="pb-btn pb-pri" onClick="{{h.ok}}">Still right</button><button class="pb-btn pb-ghost">Change</button></div>
          </sc-if>
        </div>
      </sc-for>
    </div>

    <h2 class="pb-h2">New for this tender</h2>
    <div class="pb-card">
      <sc-for list="{{fresh}}" as="f" hint-placeholder-count="3">
        <div class="pb-row"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{f.q}}</span><span class="pb-muted">{{f.why}}</span></span><button class="pb-btn pb-sec">Answer</button></div>
      </sc-for>
    </div>
    <div class="pb-note n-info">Your company, people, track record, workforce and policies are kept from your profile. If anything changes between bids, change it once in your profile and every future bid uses it.</div>
  </div>
'''
SCRIPT = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { ok: {} }; }
  renderVals() {
    const ok = this.state.ok;
    const H = [
      ['co', 'Company details', 'Oakleaf Living Ltd, 99000404, Ashford office', 'Checked against Companies House today', 'auto'],
      ['cqc', 'CQC registration and rating', 'Good overall. Home care and supported living', 'Checked against the CQC register today', 'auto'],
      ['ins', 'Insurance', 'Employer\'s liability £10m, public liability £5m. Expire 31 March 2027', 'You confirmed this 2 months ago', 'ask'],
      ['staff', 'Staff numbers', '60 staff, 7 vacancies, 18% turnover', 'You confirmed this 5 months ago. Buyers want recent figures', 'ask'],
      ['ex', 'Contract examples', '3 examples. Newest: Brookside home care, won March 2026', 'Both referees agreed last time', 'ask'],
      ['pol', 'Policies', '11 policies. Business continuity plan due for review', 'One needs updating before this bid', 'ask']
    ];
    const held = H.map(([k, name, value, meta, mode]) => {
      const auto = mode === 'auto', done = auto || !!ok[k];
      return { name, value, meta, state: auto ? 'Checked for you' : (done ? 'Confirmed' : 'Please check'), cls: 'pb-chip ' + (done ? 'c-ok' : 'c-warn'), ask: !done, ok: () => this.setState({ ok: Object.assign({}, ok, { [k]: true }) }) };
    });
    const n = held.filter(h => !h.ask).length;
    const fresh = [
      ['Which lots will you go for?', 'Eastford has 3 lots. We suggest 1 and 3, near your office'],
      ['Which landlords or housing providers do you work with in Eastford?', 'The buyer asks how housing and care are kept separate'],
      ['How many hours a week could you take on if you won?', 'So we do not promise more than you can staff']
    ].map(([q, why]) => ({ q, why }));
    return { theme: this.props.theme ?? 'light', held, fresh, doneText: n + ' of ' + held.length + ' parts confirmed', barCls: 'w' + Math.round(n / held.length * 10) * 10 };
  }
}'''
build(sys.argv[1], 'Check your tender profile', 1500, BODY, SCRIPT)
