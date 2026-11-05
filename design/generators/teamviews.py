import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from phoneboard import build, tabs
BODY = tabs('Demo: who is signed in', 'Person') + '''
  <div style="padding: 20px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 4px;">
      <span class="pb-sub">{{who}}</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">{{title}}</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">{{intro}}</span>
    </header>
    <sc-if value="{{isSign}}" hint-placeholder-val="{{ false }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-card">
          <sc-for list="{{signers}}" as="g" hint-placeholder-count="2">
            <div class="pb-row"><span style="width: 36px; height: 36px; flex-shrink: 0; border-radius: 999px; background: var(--cs-surface-brand); color: var(--cs-text-brand); display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 500;">{{g.in}}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{g.name}}</span><span class="pb-sub">{{g.sub}}</span></span><span class="{{g.cls}}">{{g.state}}</span></div>
          </sc-for>
        </div>
        <sc-if value="{{waiting}}" hint-placeholder-val="{{ true }}"><button class="pb-btn pb-sec" style="min-height: 48px;" onClick="{{remind}}">{{remindLabel}}</button></sc-if>
        <sc-if value="{{allSigned}}" hint-placeholder-val="{{ false }}"><div class="pb-note n-ok">Both directors have signed. Daniel sends your application today and tells you both when it is in.</div></sc-if>
        <div class="pb-note n-info">Your pack is only sent when every person who needs to sign has signed. Each signs on their own phone or computer.</div>
        <button class="pb-link" onClick="{{simulate}}" style="align-self: center;">Demo: Peter signs now</button>
      </div>
    </sc-if>
    <sc-if value="{{isList}}" hint-placeholder-val="{{ true }}">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div class="pb-card">
          <sc-for list="{{tasks}}" as="t" hint-placeholder-count="5">
            <div class="pb-row"><span class="{{t.dot}}"></span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{t.title}}</span><span class="pb-sub">{{t.sub}}</span></span><sc-if value="{{t.hasCta}}" hint-placeholder-val="{{ true }}"><button class="pb-btn pb-sec">{{t.cta}}</button></sc-if></div>
          </sc-for>
        </div>
        <div class="pb-card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 6px;"><span style="font-weight: 500;">What {{shortName}} can see</span><span class="pb-sub">{{sees}}</span></div>
      </div>
    </sc-if>
  </div>
'''
SCRIPT = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { tab: 'co', reminded: false, peter: false }; }
  renderVals() {
    const { tab, reminded, peter } = this.state;
    const T = [['co', 'Co-director'], ['rm', 'Registered manager'], ['sign', 'Signing together']];
    const V = {
      co: ['Peter Okafor. Director, Harbour Lane Care Ltd', 'Good morning, Peter', 'Amara added you as a co-director. You see everything she sees, and these things are yours to do.', 'Peter', 'Everything on the account, including payments. Amara and Peter each have their own sign-in, and every look at the file is recorded.', [
        ['now', 'Verify your identity for Companies House', 'Online with photo ID. You get a code to give us', 'Start'],
        ['now', 'Photos of your ID', 'Passport or photocard licence, and proof of address', 'Add'],
        ['next', 'Sign the declaration', 'Opens when your pack is ready. Amara signs too', ''],
        ['done', 'Your details in the onboarding form', 'Amara filled them in. Please check they are right', 'Check']]],
      rm: ['Ruth Bennett. Registered manager', 'Hello, Ruth', 'Amara named you as the registered manager. These are your things to do. You do not see the company\'s money or other people\'s details.', 'Ruth', 'Your own tasks, the Statement of Purpose and policies you will use, and your interview practice. Not payments, not the directors\' personal details.', [
        ['now', 'Your CV', 'Full work history with dates. We check it for gaps with you', 'Upload'],
        ['now', 'Your DBS', 'A photo, or we help you apply', 'Add'],
        ['next', 'Read your policies', 'Before your CQC interview, so you know them well', 'Open'],
        ['next', 'Interview practice', 'In your interview portal, plus a session with Millicent', 'Open'],
        ['done', 'Your GP and referee details', 'Amara added them. CQC may contact them', '']]]
    };
    const isSign = tab === 'sign';
    const v = V[tab] || V.co;
    const tasks = v[5].map(([k, title, sub, cta]) => ({ dot: 'dot d-' + k, title, sub, cta, hasCta: !!cta }));
    const signers = [
      { in: 'AO', name: 'Amara Okafor, director', sub: 'Signed Monday 11 January, 09:14', state: 'Signed', cls: 'pb-chip c-ok' },
      { in: 'PO', name: 'Peter Okafor, director', sub: peter ? 'Signed Monday 11 January, 18:02' : (reminded ? 'Reminder sent just now' : 'We sent the link on Monday morning'), state: peter ? 'Signed' : 'Waiting', cls: 'pb-chip ' + (peter ? 'c-ok' : 'c-warn') }
    ];
    return {
      theme: this.props.theme ?? 'light',
      tabs: T.map(([k, label]) => ({ label, on: tab === k, off: tab !== k, pick: () => this.setState({ tab: k }) })),
      who: isSign ? 'Harbour Lane Care Ltd' : v[0], title: isSign ? 'Signing your pack together' : v[1],
      intro: isSign ? 'Two directors, so two signatures. Here is where each one is.' : v[2],
      shortName: v[3], sees: v[4], tasks, isList: !isSign, isSign, signers,
      waiting: !peter, allSigned: peter,
      remindLabel: reminded ? 'Reminder sent to Peter' : 'Send Peter a reminder',
      remind: () => this.setState({ reminded: true }), simulate: () => this.setState({ peter: true })
    };
  }
}'''
build(sys.argv[1], 'Team views', 1100, BODY, SCRIPT)
