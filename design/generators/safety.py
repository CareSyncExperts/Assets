import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from phoneboard import build

# 61. Address history as cards (used in every form)
BODY1 = '''  <div style="padding: 24px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 4px;">
      <span class="pb-sub">CQC Registration Information Form. Page 13 of 16</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">Where have you lived in the last 5 years?</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Start with where you live now. Type a postcode to find each address, then pick the month you moved in.</span>
    </header>
    <div style="display: flex; flex-direction: column; gap: 6px;">
      <div style="display: flex; justify-content: space-between;"><span class="pb-sub">{{covered}}</span><span class="pb-sub">5 years</span></div>
      <div aria-hidden="true" style="height: 10px; border-radius: 999px; background: var(--cs-surface-subtle); overflow: hidden;"><div class="{{barCls}}" style="height: 10px; border-radius: 999px; background: var(--cs-action-primary);"></div></div>
    </div>
    <sc-for list="{{cards}}" as="c" hint-placeholder-count="3">
      <div>
        <sc-if value="{{c.isGap}}" hint-placeholder-val="{{ false }}">
          <div class="pb-note n-warn" style="display: flex; flex-direction: column; gap: 8px;">
            <span style="font-weight: 500;">{{c.title}}</span>
            <span>Were you living somewhere else, or between homes? Either is fine. We just need to know.</span>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;"><button class="pb-btn pb-pri" onClick="{{c.fix}}">Add an address</button><button class="pb-btn pb-ghost">Tell us why</button></div>
          </div>
        </sc-if>
        <sc-if value="{{c.isAddr}}" hint-placeholder-val="{{ true }}">
          <div class="pb-card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center;"><span class="pb-muted">{{c.label}}</span><button class="pb-link" style="min-height: 32px;">Change</button></div>
            <span style="font-size: 15px; line-height: 22px; font-weight: 500;">{{c.title}}</span>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
              <span style="display: flex; flex-direction: column; gap: 2px; padding: 8px 10px; border-radius: 8px; background: var(--cs-surface-page);"><span class="pb-muted">Moved in</span><span style="font-weight: 500;">{{c.from}}</span></span>
              <span style="display: flex; flex-direction: column; gap: 2px; padding: 8px 10px; border-radius: 8px; background: var(--cs-surface-page);"><span class="pb-muted">Moved out</span><span style="font-weight: 500;">{{c.to}}</span></span>
            </div>
          </div>
        </sc-if>
      </div>
    </sc-for>
    <button class="pb-btn pb-ghost" style="min-height: 48px;">+ Add another address</button>
    <sc-if value="{{complete}}" hint-placeholder-val="{{ false }}"><div class="pb-note n-ok">All 5 years are covered, with no gaps. Thank you.</div></sc-if>
    <span class="pb-muted" style="text-align: center;">Used the same way for the RI, manager and every director, on every form.</span>
  </div>
'''
SCRIPT1 = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { fixed: false }; }
  renderVals() {
    const fixed = this.state.fixed;
    const cards = [{ isAddr: true, label: 'Where you live now', title: '22 Willow Court, Stevenage SG2 7AB', from: 'September 2022', to: 'Now' }];
    if (fixed) cards.push({ isAddr: true, label: 'Address 2', title: 'Flat 4, 9 Example Street, Luton LU1 2AA', from: 'May 2022', to: 'August 2022' });
    else cards.push({ isGap: true, title: 'Gap: May 2022 to August 2022' });
    cards.push({ isAddr: true, label: fixed ? 'Address 3' : 'Address 2', title: '5 Example Gardens, Hitchin SG4 9AA', from: 'June 2019', to: 'April 2022' });
    const out = cards.map(c => Object.assign({ isGap: false, isAddr: false, label: '', from: '', to: '', fix: () => this.setState({ fixed: true }) }, c));
    return { theme: this.props.theme ?? 'light', cards: out, covered: fixed ? '5 years covered' : '4 years 8 months covered', barCls: fixed ? 'w100' : 'w90', complete: fixed };
  }
}'''
build(sys.argv[1] + '/AddressCards.dc.html', 'Address history', 1200, BODY1, SCRIPT1)

# 62. Security and privacy, in plain words
BODY2 = '''  <div style="padding: 24px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 4px;">
      <span class="pb-sub">Your account</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">How we keep your information safe</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Your Hub holds passports, DBS details and business documents. Here is exactly how we look after them.</span>
    </header>
    <div class="pb-card">
      <sc-for list="{{facts}}" as="f" hint-placeholder-count="8">
        <div class="pb-row"><span style="width: 32px; height: 32px; flex-shrink: 0; border-radius: 8px; background: var(--cs-surface-brand); color: var(--cs-text-brand); display: flex; align-items: center; justify-content: center;"><x-import component-from-global-scope="CareSync.Icon" name="{{f.icon}}" size="{{n16}}"></x-import></span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{f.title}}</span><span class="pb-sub">{{f.text}}</span></span></div>
      </sc-for>
    </div>
    <div class="pb-card" style="padding: 14px 16px; display: flex; flex-direction: column; gap: 8px;">
      <span style="display: flex; justify-content: space-between; align-items: center; gap: 8px;"><span style="font-weight: 500;">Signing in</span><span class="pb-chip c-ok">Code to your mobile: on</span></span>
      <span class="pb-sub">{{signText}}</span>
      <span class="pb-sub">{{codeText}}</span>
    </div>
    <div style="display: flex; flex-direction: column; gap: 8px;">
      <a href="Account.dc.html" class="pb-btn pb-sec" style="min-height: 48px;">See every time we looked at your file</a>
      <button class="pb-btn pb-ghost" style="min-height: 48px;">Download everything we hold about you</button>
      <button class="pb-link" style="align-self: center;">Something worries you? Tell a manager</button>
    </div>
  </div>
'''
SCRIPT2 = r'''class Component extends DCLogic {
  renderVals() {
    const get = (k, f) => (window.CSR ? CSR.get(k, f) : f);
    const ico = get('ico-number', '');
    const facts = [
      ['building-2', 'Where your information is kept', "Your Hub's database and files are in the UK, and encrypted. Some trusted suppliers process data elsewhere under UK safeguards."],
      ['users', 'Who can see it', 'Your consultant, the onboarding lead before your handover, your coach for session notes, client care for your contact details, and managers. If your consultant is on leave, a colleague covers for dates a manager approves.'],
      ['shield-alert', 'Emergencies only', 'If anyone else ever needs to look, it is for an emergency only. A senior member of the Care Sync team approved it first. It lasts ' + get('break-glass-hours', 4) + ' hours at most and we tell you the same day.'],
      ['history', 'Every look is recorded', 'Who opened what, when and why. You can see the list any time.'],
      ['lock', 'Passwords stay hidden', 'If you give us a login, it goes into an encrypted vault. Nobody can see it in the Hub or in emails.'],
      ['trash-2', 'ID and DBS images are deleted', 'Once the regulator has made its decision. We keep a short record: who checked them, when, the type of document, and the DBS number and issue date. Everything else follows our retention schedule.'],
      ['file-check', 'Registered with the Information Commissioner', ico ? 'Care Sync Experts is registered with the ICO. Our registration number is ' + ico + '.' : 'Our ICO registration number will be shown here.']
    ].map(([icon, title, text]) => ({ icon, title, text }));
    return { theme: this.props.theme ?? 'light', n16: 16, facts,
      signText: 'We email you a sign-in link, so there is no password. A phone or computer you have used before stays signed in for ' + get('client-device-days', 30) + ' days.',
      codeText: 'Because Care Sync holds the login to the email you sign in with, we text a code to your mobile on a new device, and before you sign, approve, download everything or change your contact details. This stays on while we hold that login.' };
  }
}'''
build(sys.argv[1] + '/Security.dc.html', 'Keeping your information safe', 1300, BODY2, SCRIPT2)
