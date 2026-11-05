import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from phoneboard import build, tabs

# 65. Client: CQC refused, we resubmit
BODY = tabs('Demo: the three parts of this page', 'Refusal and resubmission') + '''
  <div style="padding: 20px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 4px;">
      <span class="pb-sub">Harbour Lane Care Ltd</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">{{heading}}</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">{{intro}}</span>
    </header>
    <sc-if value="{{isWhat}}" hint-placeholder-val="{{ true }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-note n-ok"><span style="font-weight: 600;">We resubmit for you, at no cost to you, as part of your package.</span> A refusal is not the end. Daniel has already read the decision, and your new application starts today.</div>
        <h2 class="pb-h2">What CQC said, in plain English</h2>
        <div class="pb-card">
          <sc-for list="{{reasons}}" as="r" hint-placeholder-count="3">
            <div class="pb-row" style="flex-direction: column; gap: 6px;">
              <span style="font-weight: 500;">{{r.reason}}</span>
              <span class="pb-sub">{{r.plain}}</span>
              <span style="display: flex; gap: 8px; align-items: flex-start; font-size: 13px; line-height: 18px;"><span class="pb-chip c-brand">Our fix</span><span>{{r.fix}}</span></span>
            </div>
          </sc-for>
        </div>
        <a href="#" class="pb-btn pb-ghost" style="min-height: 44px;">Read CQC's letter in full</a>
      </div>
    </sc-if>
    <sc-if value="{{isPlan}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 4px;"><span class="pb-muted">Target to resubmit</span><span style="font-size: 20px; line-height: 28px; font-weight: 600;">Friday 9 April</span><span class="pb-sub">{{targetSub}}</span></div>
        <ol class="pb-card" style="list-style: none; margin: 0; padding: 4px 0;">
          <sc-for list="{{steps}}" as="s" hint-placeholder-count="7">
            <li class="pb-row"><span class="{{s.dot}}"></span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{s.title}}</span><span class="pb-sub">{{s.sub}}</span></span><span class="pb-muted" style="white-space: nowrap;">{{s.who}}</span></li>
          </sc-for>
        </ol>
        <div class="pb-note n-info">Your new application says honestly that CQC refused the first one, and shows what has changed. CQC asks this, and being open about it is what makes a resubmission strong.</div>
      </div>
    </sc-if>
    <sc-if value="{{isChoice}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-card">
          <sc-for list="{{options}}" as="o" hint-placeholder-count="2">
            <div class="pb-row" style="flex-direction: column; gap: 6px;">
              <div style="display: flex; justify-content: space-between; gap: 8px; width: 100%;"><span style="font-weight: 500;">{{o.name}}</span><span class="{{o.cls}}">{{o.tag}}</span></div>
              <span class="pb-sub">{{o.when}}</span>
              <span style="font-size: 13px; line-height: 18px;">{{o.detail}}</span>
            </div>
          </sc-for>
        </div>
        <div class="pb-note n-warn">An appeal must reach the tribunal within 28 days of CQC's decision. We work the date out the safe way, with the day the notice was served as day 1, and you confirm it with a legal adviser. So we talk it through with you this week, even if resubmitting is the plan.</div>
        <a href="#" class="pb-btn pb-pri" style="min-height: 48px;">Book a call with Daniel</a>
      </div>
    </sc-if>
  </div>
'''
SCRIPT = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { tab: 'what' }; }
  renderVals() {
    const tab = this.state.tab;
    const day = window.CSR ? CSR.get('weekly-update-day', 'Friday') : 'Friday';
    const T = [['what', 'What happened'], ['plan', 'Our plan'], ['choice', 'Resubmit or appeal']];
    const H = { what: ['CQC has refused the application', 'This is hard news. Here is exactly why, and what we are doing about it.'], plan: ['Your resubmission plan', 'Every reason fixed, everything checked again, then we send it.'], choice: ['Resubmit or appeal?', 'You have two routes. We will be honest about which is better for you.'] };
    const reasons = [
      ['Staffing was not clear enough', 'CQC was not sure you could cover visits safely in your first months.', 'A clearer staffing plan with named staff, a recruitment timetable and cover for sickness.'],
      ['The manager\'s answers at interview', 'Some answers about safeguarding referrals were not confident enough.', 'Two practice sessions with Millicent and the interview portal before the new interview.'],
      ['The office address', 'CQC was not shown the landlord\'s permission to use the flat as an office.', 'The landlord\'s letter, already requested through your Hub.']
    ].map(([reason, plain, fix]) => ({ reason, plain, fix }));
    const steps = [
      ['done', 'Daniel reads the decision with you', 'A call to go through each reason, and how you feel about it', 'Daniel, done'],
      ['now', 'Fix every reason CQC gave', 'Staffing plan, office permission, interview preparation', 'Daniel and you'],
      ['now', 'Check everything again, not only the reasons', 'Our own rules: a DBS under 12 months old and references under 6 months old on the day we resubmit. Ruth\'s DBS will be older, so a new one is on its way. Insurance renewal and plans dated this month too', 'Grace'],
      ['next', 'Interview practice', 'Two sessions with Millicent, and the interview portal', 'Millicent and Ruth'],
      ['next', 'A senior review', 'A second consultant reads the whole pack against CQC\'s reasons before anything is sent', 'Senior consultant'],
      ['next', 'You review and sign', 'Only the parts that changed are marked for you', 'You'],
      ['next', 'We resubmit to CQC', 'Receipt the same day', 'Daniel']
    ].map(([k, title, sub, who]) => ({ dot: 'dot d-' + k, title, sub, who }));
    const options = [
      ['Resubmit', 'Our usual advice', 'ok', 'When CQC\'s reasons are fair and can be fixed', 'We fix every reason and send a new application, as part of your package. For most clients this is the practical route.'],
      ['Appeal to the tribunal', 'Sometimes right', 'neutral', 'When CQC got the facts wrong, or did not follow its own process', 'An independent tribunal looks again at CQC\'s decision. It must be lodged within 28 days of the decision. We tell you honestly if we think an appeal could succeed, and what it would involve.']
    ].map(([name, tag, k, when, detail]) => ({ name, tag, when, detail, cls: 'pb-chip c-' + k }));
    return {
      theme: this.props.theme ?? 'light',
      tabs: T.map(([k, label]) => ({ label, on: tab === k, off: tab !== k, pick: () => this.setState({ tab: k }) })),
      heading: H[tab][0], intro: H[tab][1], isWhat: tab === 'what', isPlan: tab === 'plan', isChoice: tab === 'choice', reasons, steps, options,
      targetSub: 'Our own target, about 5 weeks away. We check the date every ' + day + ' and tell you if it moves.'
    };
  }
}'''
build(sys.argv[1] + '/Resubmit.dc.html', 'Refused, we resubmit', 1300, BODY, SCRIPT)
