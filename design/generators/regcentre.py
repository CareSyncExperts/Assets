import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from phoneboard import build
BODY = '''  <div style="padding: 10px 12px; background: var(--cs-surface-subtle); display: flex; flex-direction: column; gap: 8px;">
    <span style="font-size: 11px; line-height: 14px; color: var(--cs-text-muted);">Demo: regulator, then the moment</span>
    <div role="tablist" aria-label="Regulator" style="display: flex; gap: 6px;">
      <sc-for list="{{regs}}" as="g" hint-placeholder-count="2">
        <sc-if value="{{g.on}}" hint-placeholder-val="{{ false }}"><button class="pb-tab pb-on" role="tab" aria-selected="true" onClick="{{g.pick}}">{{g.label}}</button></sc-if>
        <sc-if value="{{g.off}}" hint-placeholder-val="{{ true }}"><button class="pb-tab pb-off" role="tab" aria-selected="false" onClick="{{g.pick}}">{{g.label}}</button></sc-if>
      </sc-for>
    </div>
    <div role="tablist" aria-label="Moment" style="display: flex; flex-wrap: wrap; gap: 6px;">
      <sc-for list="{{moments}}" as="m" hint-placeholder-count="5">
        <sc-if value="{{m.on}}" hint-placeholder-val="{{ false }}"><button class="pb-tab pb-on" role="tab" aria-selected="true" onClick="{{m.pick}}">{{m.label}}</button></sc-if>
        <sc-if value="{{m.off}}" hint-placeholder-val="{{ true }}"><button class="pb-tab pb-off" role="tab" aria-selected="false" onClick="{{m.pick}}">{{m.label}}</button></sc-if>
      </sc-for>
    </div>
  </div>
  <div style="padding: 20px 20px 40px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 4px;">
      <span class="pb-sub">{{client}}</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">{{title}}</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">{{intro}}</span>
    </header>
    <sc-if value="{{hasBanner}}" hint-placeholder-val="{{ false }}"><div class="{{bannerCls}}">{{banner}}</div></sc-if>
    <div class="pb-card">
      <sc-for list="{{rows}}" as="r" hint-placeholder-count="5">
        <div class="pb-row"><span class="{{r.dot}}"></span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{r.title}}</span><span class="pb-sub">{{r.sub}}</span></span><sc-if value="{{r.hasChip}}" hint-placeholder-val="{{ false }}"><span class="{{r.chipCls}}">{{r.chip}}</span></sc-if></div>
      </sc-for>
    </div>
    <sc-if value="{{hasAction}}" hint-placeholder-val="{{ true }}"><a href="{{actionHref}}" class="pb-btn pb-pri" style="min-height: 48px;">{{action}}</a></sc-if>
    <div class="pb-note n-info">{{foot}}</div>
  </div>
'''
SCRIPT = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { reg: 'ciw', m: 'before' }; }
  renderVals() {
    const { reg, m } = this.state;
    const get = (k, f) => (window.CSR ? CSR.get(k, f) : f);
    const day = get('weekly-update-day', 'Friday');
    const addOn = 'Your package covers registration. If you would like more support, ' + get('aftercare-months', 12) + ' months of aftercare can be added, including an inspection readiness check in month ' + get('inspection-readiness-month', 4) + '. Ask Daniel.';
    const M = [['before', 'Before we submit'], ['sent', 'Submitted'], ['q', 'Questions'], ['int', 'Interview'], ['done', 'Registered']];
    const D = {
      ciw: { label: 'CIW', client: 'Afon Care Ltd. Domiciliary support service, Wales', portal: 'CIW Online',
        before: ['Your CIW application', 'We complete CIW Online with you. CIW sends each person their own invitation to fill in their part, and we help every one of them.', '', '', [
          ['done', 'CIW Online account set up', 'You and your consultant can both work on it', 'Done', 'ok'],
          ['done', 'Organisation, service and officers', 'Copied from your onboarding form', 'Done', 'ok'],
          ['now', 'People: RI, manager and Owen', '2 of 3 records complete. Owen has his invitation from CIW Online', '2 of 3', 'warn'],
          ['now', 'References', 'CIW emails each referee directly. Sarah has not replied yet (sent 3 days ago)', 'Waiting', 'warn'],
          ['next', 'Declarations', 'They open in CIW Online when every record is complete. Each person ticks their own', 'Not open yet', 'neutral']],
          'Nudge Sarah about her reference', '#', 'You submit in CIW Online yourself, with your consultant beside you on a call. We never submit without you.'],
        sent: ['Submitted to CIW', 'Sent in CIW Online on Tuesday 12 January. CIW confirmed it has your application.', 'Your CIW reference is saved on your Today page.', 'n-ok', [
          ['done', 'Submitted in CIW Online', '12 January, 14:20. Copy saved to your documents', 'Done', 'ok'],
          ['now', 'CIW checks your application', 'CIW reads everything, checks the references and DBS, and may ask questions', 'Now', 'info'],
          ['next', 'Suitability interview', 'CIW may invite the RI to an interview. Practise in your interview portal', '', ''],
          ['next', 'CIW decision', 'CIW sets its own pace. We update you every ' + day, '', '']],
          'Go to Interview Preparation Hub', '#', 'We check CIW Online every working day, so nothing is missed. And if CIW ever refuses, we resubmit for you, as part of your package.'],
        q: ['CIW asked for more information', 'A normal part of the process. Here is what CIW asked, in plain English, and our plan.', 'Asked in CIW Online on 20 January. Reply by 3 February.', 'n-warn', [
          ['now', 'Your business continuity plan', 'CIW wants to see how you would keep visits going in bad weather. Daniel is updating it', 'Daniel', 'brand'],
          ['now', 'One gap in the RI\'s work history', 'March to June 2019. A short note from you is all we need', 'You', 'warn'],
          ['next', 'We send the reply in CIW Online', 'Target 30 January, before the deadline', '', '']],
          'Write your note about 2019', '#', 'Answering questions is common, and does not mean anything is wrong. Even if CIW refused, we would resubmit for you, as part of your package.'],
        int: ['Your suitability interview', 'CIW has invited Rhian, your RI, to a suitability interview by video.', 'Thursday 11 February, 10:00, by video. Language: English.', 'n-info', [
          ['done', 'Interview booked', 'The invitation is saved in your documents', 'Booked', 'ok'],
          ['now', 'Practise with your interview portal', 'Questions CIW tends to ask an RI, with model answers', 'Practise', 'brand'],
          ['next', 'Practice session with Millicent', 'One hour by video, the week before', '', '']],
          'Go to Interview Preparation Hub', '#', 'Bring your Statement of Purpose. Millicent goes through the regulations an RI is expected to know.'],
        done: ['Registered with CIW', 'Congratulations. CIW has registered Afon Care for domiciliary support in Cardiff and Vale, and West Glamorgan.', 'Your certificate and conditions are saved in your documents.', 'n-ok', [
          ['done', 'Certificate and conditions', 'The areas and your RI are named as conditions, as you agreed', 'Saved', 'ok'],
          ['now', 'Your Registration File and handover call', 'Every final document in one place. Daniel walks you through it and what comes next', 'Ready', 'ok'],
          ['next', 'RI visits every 3 months', 'The RI visits the service and writes it up (regulation 73). Your handover includes a template', '', ''],
          ['next', 'Quality of care review every 6 months', 'Regulation 80. We help with the first one', '', ''],
          ['next', 'Annual return', 'Through CIW Online each year. We remind you', '', '']],
          'Open your Registration File', '#', addOn] },
      rqia: { label: 'RQIA', client: 'Lagan View Care Ltd. Domiciliary care agency, Northern Ireland', portal: 'the RQIA Web Portal',
        before: ['Your RQIA application', 'We complete the RQIA Web Portal with you: the service application, the RI application and the manager\'s application.', '', '', [
          ['done', 'RQIA Web Portal login', 'Issued by RQIA after checking who you are', 'Done', 'ok'],
          ['done', 'Service application', 'Copied from your onboarding form', 'Done', 'ok'],
          ['now', 'RI and manager applications', 'CVs, references and health declarations', 'Nearly', 'warn'],
          ['now', 'AccessNI', 'RQIA runs the checks for the RI and the manager, using its PIN. ID documents ready', 'Ready', 'ok'],
          ['now', 'Manager\'s NISCC registration', 'Applied for. RQIA expects it to be in place or underway', 'Underway', 'warn']],
          'See what is still needed', '#', 'You submit with your consultant on a call. We never submit without you.'],
        sent: ['Submitted to RQIA', 'Sent on the RQIA Web Portal on Monday 18 January. RQIA confirmed it has your application.', 'Your RQIA reference is saved on your Today page.', 'n-ok', [
          ['done', 'Submitted on the RQIA Web Portal', '18 January, 11:05. Copy saved to your documents', 'Done', 'ok'],
          ['now', 'RQIA checks your application', 'Including AccessNI checks for the RI and the manager', 'Now', 'info'],
          ['next', 'Fit person interviews', 'For the RI and the manager. Practise in your interview portal', '', ''],
          ['next', 'RQIA decision', 'RQIA sets its own pace. We update you every ' + day, '', '']],
          'Go to Interview Preparation Hub', '#', 'We check the RQIA Web Portal every working day and your business email every few minutes, so nothing is missed. And if RQIA ever refuses, we resubmit for you, as part of your package.'],
        q: ['RQIA asked for more information', 'A normal part of the process. Here is what RQIA asked, in plain English, and our plan.', 'Asked on 26 January. Reply by 9 February.', 'n-warn', [
          ['now', 'Your staffing plan', 'RQIA wants to see how 8 staff cover 20 service users. Daniel is updating it', 'Daniel', 'brand'],
          ['now', 'The manager\'s NISCC reference number', 'Once NISCC confirms the application', 'Manager', 'warn'],
          ['next', 'We send the reply on the portal', 'Target 5 February, before the deadline', '', '']],
          'Add the NISCC reference', '#', 'Answering questions is common, and does not mean anything is wrong. Even if RQIA refused, we would resubmit for you, as part of your package.'],
        int: ['Your fit person interviews', 'RQIA has invited Niamh (RI) and the manager to fit person interviews.', 'Wednesday 17 February, 10:00 and 11:30.', 'n-info', [
          ['done', 'Interviews booked', 'The invitation is saved in your documents', 'Booked', 'ok'],
          ['now', 'Practise with your interview portal', 'The Minimum Standards, safeguarding and scenarios', 'Practise', 'brand'],
          ['next', 'Practice session with Millicent', 'One hour by video, the week before', '', '']],
          'Go to Interview Preparation Hub', '#', 'Know your Statement of Purpose and the Minimum Standards for domiciliary care agencies.'],
        done: ['Registered with RQIA', 'Congratulations. RQIA has registered Lagan View Care as a domiciliary care agency.', 'Your certificate is saved in your documents.', 'n-ok', [
          ['done', 'Certificate', 'Display it at your office', 'Saved', 'ok'],
          ['now', 'Your Registration File and handover call', 'Every final document in one place. Daniel walks you through it and what comes next', 'Ready', 'ok'],
          ['next', 'Monthly quality monitoring', 'The registered person reviews quality every month and writes it up. Your handover includes a template', '', ''],
          ['next', 'RQIA inspections', 'Against the Minimum Standards. We help you get ready', '', '']],
          'Open your Registration File', '#', addOn] }
    };
    const d = D[reg], s = d[m];
    const rows = s[4].map(([k, title, sub, chip, cc]) => ({ dot: 'dot d-' + k, title, sub, chip, hasChip: !!chip, chipCls: 'pb-chip c-' + (cc || 'neutral') }));
    return {
      theme: this.props.theme ?? 'light',
      regs: ['ciw', 'rqia'].map(k => ({ label: D[k].label, on: k === reg, off: k !== reg, pick: () => this.setState({ reg: k }) })),
      moments: M.map(([k, label]) => ({ label, on: k === m, off: k !== m, pick: () => this.setState({ m: k }) })),
      client: d.client, title: s[0], intro: s[1], banner: s[2], hasBanner: !!s[2], bannerCls: 'pb-note ' + (s[3] || 'n-info'), rows,
      action: s[5], actionHref: s[6], hasAction: !!s[5], foot: s[7]
    };
  }
}'''
build(sys.argv[1], 'Your regulator', 1150, BODY, SCRIPT)
