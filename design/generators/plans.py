import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from phoneboard import build, tabs

# 59. Joined-up timeline for a client with registration and tenders
BODY1 = '''  <div style="padding: 24px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 4px;">
      <span class="pb-sub">Willow Bank Supported Living Ltd</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">Your plan: registration, then tenders</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Most care contracts need you to be registered, so registration comes first. Your tender profile is built alongside it, so you are ready to bid the day CQC registers you.</span>
    </header>
    <div style="display: flex; gap: 12px; flex-wrap: wrap;" aria-hidden="true">
      <span style="display: flex; gap: 6px; align-items: center; font-size: 12px; color: var(--cs-text-secondary);"><span class="dot d-done" style="margin: 0;"></span>Done</span>
      <span style="display: flex; gap: 6px; align-items: center; font-size: 12px; color: var(--cs-text-secondary);"><span class="dot d-now" style="margin: 0;"></span>Now</span>
      <span style="display: flex; gap: 6px; align-items: center; font-size: 12px; color: var(--cs-text-secondary);"><span class="dot d-next" style="margin: 0;"></span>Next</span>
      <span style="display: flex; gap: 6px; align-items: center; font-size: 12px; color: var(--cs-text-secondary);"><span class="dot d-ten" style="margin: 0;"></span>Tenders</span>
    </div>
    <ol class="pb-card" style="list-style: none; margin: 0; padding: 4px 0;">
      <sc-for list="{{steps}}" as="s" hint-placeholder-count="10">
        <li class="pb-row"><span class="{{s.dot}}"></span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{s.title}}</span><span class="pb-muted">{{s.sub}}</span></span><span class="pb-sub" style="white-space: nowrap;">{{s.when}}</span></li>
      </sc-for>
    </ol>
    <div class="pb-note n-info">{{note}}</div>
    <a href="BidDecision.dc.html" class="pb-btn pb-sec" style="min-height: 48px;">See the tenders we are watching for you</a>
  </div>
'''
SCRIPT1 = r'''class Component extends DCLogic {
  renderVals() {
    const S = [
      ['done', 'Onboarding form', 'Checked and approved', '27 Oct'],
      ['now', 'Your documents', '3 small things need you', 'by 20 Nov'],
      ['next', 'We write your registration pack', 'Policies, Statement of Purpose, business plan', 'Dec'],
      ['ten', 'Your tender profile', 'About 40 minutes, once. We reuse it for every bid', 'Dec'],
      ['next', 'You review and sign', 'Comment on drafts, then sign once', 'early Jan'],
      ['next', 'We send your application to CQC', 'You get the receipt the same day', 'target Jan'],
      ['next', 'CQC checks and your interview', 'Millicent prepares you. We answer CQC\'s questions with you', 'after sending'],
      ['next', 'Registered', 'The day CQC confirms, your tender profile goes live', 'when CQC decides'],
      ['ten', 'Your first bids', 'Eastford supported living framework reopens in April. It suits a new provider', 'from Apr'],
      ['ten', 'Open all year: dynamic markets', 'Lower effort ways onto council lists. We apply as soon as you are registered', 'after registration']
    ];
    const day = window.CSR ? CSR.get('weekly-update-day', 'Friday') : 'Friday';
    return { theme: this.props.theme ?? 'light', note: 'These are our target dates. We check them every ' + day + ' and tell you straight away if one moves, and why. CQC sets its own pace once your application is in.', steps: S.map(([k, title, sub, when]) => ({ dot: 'dot d-' + k, title, sub, when })) };
  }
}'''
build(sys.argv[1] + '/TwoServices.dc.html', 'Your plan', 1300, BODY1, SCRIPT1)

# 60. Plan and costs, including what happens if CQC says no
BODY2 = tabs('Demo: the three parts of this page', 'Plan and costs') + '''
  <div style="padding: 20px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 2px;">
      <span class="pb-sub">Harbour Lane Care Ltd. Domiciliary care, full package</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">{{heading}}</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">{{intro}}</span>
    </header>
    <sc-if value="{{isDates}}" hint-placeholder-val="{{ true }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-card">
          <sc-for list="{{dates}}" as="d" hint-placeholder-count="5">
            <div class="pb-row"><span class="{{d.dot}}"></span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{d.title}}</span><span class="pb-muted">{{d.sub}}</span></span><span class="pb-sub" style="white-space: nowrap;">{{d.when}}</span></div>
          </sc-for>
        </div>
        <div class="pb-note n-info">{{decisionNote}}</div>
        <div class="pb-card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 6px;"><span style="font-weight: 500;">What can make it take longer</span><span class="pb-sub">Documents we are waiting for, a referee or GP who is slow to reply, a DBS that needs redoing, or CQC asking extra questions. We tell you as soon as we see one coming.</span></div>
      </div>
    </sc-if>
    <sc-if value="{{isMoney}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-card">
          <div class="pb-row" style="flex-direction: column; gap: 2px;"><span style="display: flex; justify-content: space-between; width: 100%; font-weight: 500;"><span>Your package</span><span>{{pkgPrice}}</span></span><span class="pb-muted">{{pkgNote}}</span></div>
          <sc-for list="{{pays}}" as="p" hint-placeholder-count="3">
            <div class="pb-row"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{p.name}}</span><span class="pb-muted">{{p.when}}</span></span><span style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px;"><span style="font-weight: 500;">{{p.amount}}</span><span class="{{p.cls}}">{{p.state}}</span></span></div>
          </sc-for>
        </div>
        <div class="pb-note n-info">You pay each instalment through Stripe, by card or another way Stripe offers.</div>
        <h2 class="pb-h2">Extras, only if you want them</h2>
        <div class="pb-card">
          <sc-for list="{{extras}}" as="x" hint-placeholder-count="4">
            <div class="pb-row"><span style="flex: 1; min-width: 0;">{{x.name}}</span><span style="font-weight: 500; white-space: nowrap;">{{x.price}}</span></div>
          </sc-for>
        </div>
        <div class="pb-note n-ok">We never add a cost without asking. Every extra is priced and agreed with you before we start.</div>
      </div>
    </sc-if>
    <sc-if value="{{isNo}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-note n-ok"><span style="font-weight: 600;">If CQC refuses, we resubmit for you, as part of your package.</span> A question or a returned application is not a refusal. Here is every step, so nothing comes as a surprise.</div>
        <ol class="pb-card" style="list-style: none; margin: 0; padding: 4px 0;">
          <sc-for list="{{nosteps}}" as="n" hint-placeholder-count="5">
            <li class="pb-row"><span style="width: 26px; height: 26px; flex-shrink: 0; border-radius: 999px; background: var(--cs-surface-brand); color: var(--cs-text-brand); display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600;">{{n.no}}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{n.title}}</span><span class="pb-sub">{{n.sub}}</span></span></li>
          </sc-for>
        </ol>
        <div class="pb-card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 4px;"><span style="font-weight: 500;">What it costs</span><span class="pb-sub">If CQC refuses, we resubmit as part of your package. Answering CQC's questions and resending a returned application are part of the work too. If anything ever costs extra, we agree it with you before we start.</span></div>
      </div>
    </sc-if>
  </div>
'''
SCRIPT2 = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { tab: 'dates' }; }
  renderVals() {
    const tab = this.state.tab;
    const get = (k, f) => (window.CSR ? CSR.get(k, f) : f);
    const day = get('weekly-update-day', 'Friday');
    const m = n => '£' + Number(n).toLocaleString('en-GB', { minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2 });
    const price = get('price-full', 8500), third = Math.floor(price / 3 * 100) / 100, last = Math.round((price - 2 * third) * 100) / 100;
    const T = [['dates', 'Key dates'], ['money', 'Costs'], ['no', 'If CQC says no']];
    const H = { dates: ['Your key dates', 'Targets we work to, checked every ' + day + '.'], money: ['What you pay, and when', 'No surprises. Your full package, and anything extra.'], no: ['If CQC says no', 'What happens, step by step, and what we do at each one.'] };
    const dates = [['done', 'Onboarding form approved', 'Your project started', '27 Oct'], ['now', 'Your documents', '3 small things need you', 'by 20 Nov'], ['next', 'Your pack is ready to review', 'Policies, Statement of Purpose, business plan', 'mid Dec'], ['next', 'You sign, we send to CQC', 'Receipt the same day', 'target Jan'], ['next', 'CQC decision', 'After checks and your interview', 'CQC sets the pace']].map(([k, title, sub, when]) => ({ dot: 'dot d-' + k, title, sub, when }));
    const pays = [['First instalment', 'When you accepted, signed and paid. Paid 19 October through Stripe. Receipt saved', m(third) + ' + VAT', 'Paid', 'ok'], ['Second instalment', 'When you sign off your final pack. We remind you a week before', m(third) + ' + VAT', 'Not due yet', 'neutral'], ['Third instalment', 'When we submit your application', m(last) + ' + VAT', 'Not due yet', 'neutral']].map(([name, when, amount, state, k]) => ({ name, when, amount, state, cls: 'pb-chip c-' + k }));
    const extras = [['Extra interview preparation', m(get('price-interview', 750)) + ' including VAT'], ['Adding supported living later', m(get('price-sl-addon', 1500)) + ' including VAT'], ['Provider Information Return when CQC asks', m(get('price-pir', 750)) + ' + VAT'], ['Tender writing', 'from ' + m(get('price-tender-from', 1500)) + ' + VAT']].map(([name, price]) => ({ name, price }));
    const nosteps = [
      ['1', 'CQC asks questions', 'Very common. We write the answers with you.'],
      ['2', 'CQC returns the application', 'Not a refusal. Something was missing. We fix it and send it again.'],
      ['3', 'Notice of proposal', 'CQC tells you it plans to refuse, and why. You have 28 days to send your side in writing, counted the safe way from the day it was served. We prepare it with you.'],
      ['4', 'Notice of decision', 'If CQC still refuses after reading your side, it sends its decision.'],
      ['5', 'We resubmit for you', 'As part of your package. We fix every reason CQC gave, check everything again, and send a new application.'],
      ['6', 'Or appeal, if CQC got it wrong', 'An independent tribunal can look again, if you apply within 28 days of the decision. We tell you honestly which route is better.']
    ].map(([no, title, sub]) => ({ no, title, sub }));
    return {
      theme: this.props.theme ?? 'light',
      tabs: T.map(([k, label]) => ({ label, on: tab === k, off: tab !== k, pick: () => this.setState({ tab: k }) })),
      heading: H[tab][0], intro: H[tab][1], isDates: tab === 'dates', isMoney: tab === 'money', isNo: tab === 'no', dates, pays, extras, nosteps,
      pkgPrice: m(price) + ' + VAT',
      pkgNote: 'Your full start-up package: everything in your agreement, from the onboarding form to the decision, plus ' + get('aftercare-months', 12) + ' months of aftercare. Paid in 3 instalments.',
      decisionNote: 'CQC does not promise a time for its decision, and neither do we. Once your application is in, we update you every ' + day + ' until it comes.'
    };
  }
}'''
build(sys.argv[1] + '/PlanCosts.dc.html', 'Plan and costs', 1250, BODY2, SCRIPT2)
