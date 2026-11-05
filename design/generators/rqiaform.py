import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from engine import build
# RQIA Registration Information Form, rebuilt from the live Google Form with smart rules.
# Every question on the live form is kept (labels tidied to British English). Hub additions say so in their tips.
JS = r'''
    const yn = [['y', 'Yes'], ['n', 'No']];
    const ltd = A.entity === 'ltd' || A.entity === 'llp';
    const sole = A.entity === 'sole';
    const E = { name: '', dob: '', email: '', tel: '', home: '', pc: '' };
    const P1 = ltd ? { name: 'Niamh Example', dob: '12/05/1982', dobOk: 'Month and year from Companies House. You added the day.', email: 'niamh@laganviewcare.co.uk', tel: '07700 900333', home: '9 Example Avenue, Belfast', pc: 'BT9 6AA' } : E;
    const P2 = ltd ? { name: 'Ciaran Example', dob: '__/03/1979', dobOk: 'Companies House shows only the month and year. Please add the day.', email: 'ciaran@laganviewcare.co.uk', tel: '07700 900444', home: '5 Example Park, Lisburn', pc: 'BT27 4AA' } : E;
    const posOpts = [['dir', 'Director'], ['part', 'Partner'], ['trus', 'Trustee'], ['sec', 'Company Secretary'], ['oth', 'Other']];
    const sameOffice = A.princ !== 'n';

    const org = [C('Legal Entity Type (Select one)', 'entity', [['sole', 'Individual (Sole Trader)'], ['ltd', 'Limited Company'], ['llp', 'Limited Liability Partnership (LLP)'], ['part', 'Partnership'], ['char', 'Charity/Voluntary Organisation'], ['hsc', 'HSC Trust'], ['oth', 'Other']]),
      ltd ? I('Type your company name or number and we fill in the rest from Companies House, including your officers on the next page.', 'ok') : I('As you are not a limited company, please fill these in yourself.'),
      T('Organisation/Provider Name', ltd ? 'Lagan View Care Ltd' : '', { req: true, ok: ltd ? 'From Companies House' : '' }),
      T('Trading Name (if different)'),
      T('Company/Charity Number (if applicable)', ltd ? 'NI000202' : '', { ok: ltd ? 'From Companies House' : '' }),
      T('Registered Office Address', ltd ? '7 Example Street, Belfast' : '', { req: true, ok: ltd ? 'From Companies House' : '' }), T('Postcode', ltd ? 'BT1 1AA' : '', { req: true }),
      C('Will the agency be run from this address?', 'princ', [['y', 'Yes'], ['n', 'No, from a different office']], { tip: 'Added by the Hub. If it is, we fill in the service address for you.' })];
    if (A.princ === 'n') org.push(T('Office address (where the agency will be run from)', '', { req: true, tip: 'Type the postcode to find the address. We use it on the service page too.' }));
    org.push(T('Organisation Telephone', '028 9000 0000', { req: true }), T('Organisation Email', 'hello@laganviewcare.co.uk', { req: true }), T('Website (if applicable)'),
      C('Are you registered with the Information Commissioner (ICO)?', 'ico', [['y', 'Yes'], ['n', 'No, please help us register']], { tip: 'Added by the Hub. Care providers hold personal and health information, so this is needed. We can help you do it.' }));
    if (A.ico === 'y') org.push(T('ICO registration number', '', { tip: 'Starts with ZA or ZB.' }));
    org.push(C('Do you already have a login for the RQIA Web Portal?', 'portal', [['y', 'Yes'], ['n', 'No, please help us request one']], { tip: 'Added by the Hub. RQIA issues the login after checking who you are, so we start this early.' }));
    S.push({ id: 'org', title: 'Organisation Information', intro: 'About the organisation that will be registered with RQIA.', fields: org });

    const offP = (n, p) => [T('Officer ' + n + ': Full Name', p.name, { req: true, ok: ltd && p.name ? 'From Companies House' : '' }), T('Officer ' + n + ': Date of Birth (dd/mm/yyyy)', p.dob, { req: true, ok: ltd ? (p.dobOk || '') : '' }),
      C('Officer ' + n + ': Position', 'pos' + n, posOpts), T('Officer ' + n + ': Email', p.email, { req: true }), T('Officer ' + n + ': Telephone', p.tel, { req: true })];
    const off = [sole ? I('As a sole trader, you are the provider. Please enter your own details as Officer 1.') : I(ltd ? 'Filled in from Companies House. Please check each one and add an email and telephone number.' : 'List ALL directors, partners, or trustees of the organisation.', ltd ? 'ok' : 'info')].concat(offP(1, P1));
    if (!sole) off.push(C('Is there another director, partner or trustee?', 'o2', yn));
    if (!sole && A.o2 === 'y') off.push(...offP(2, P2), C('Is there another director, partner or trustee?', 'o3', yn));
    if (!sole && A.o2 === 'y' && A.o3 === 'y') off.push(...offP(3, E), P('More than three officers?', '', { tip: 'For each one: full name, date of birth, position, email and telephone.' }));
    S.push({ id: 'off', title: 'Organisation Officers', intro: 'Every director, partner or trustee, one after another.', fields: off });

    const groups = A.groups || [];
    const svc = [C('Service Type (Select one)', 'svcType', [['dca', 'Domiciliary Care Agency'], ['nurse', 'Nursing Agency'], ['apa', 'Adult Placement Agency'], ['oth', 'Other']])];
    if (A.svcType === 'dca') svc.push(C('Which kind of domiciliary care agency?', 'dcaKind', [['conv', 'Conventional (care in people\'s own homes)'], ['sl', 'Supported living']], { tip: 'Added by the Hub. RQIA registers these as two kinds of agency.' }));
    if (A.svcType === 'oth') svc.push(T('Other service type: please describe', '', { req: true }));
    svc.push(T('Service/Agency Name', 'Lagan View Care', { req: true, tip: 'Must match your Statement of Purpose exactly. We keep them the same for you.' }),
      T('Service Address', sameOffice ? (ltd ? '7 Example Street, Belfast' : '') : '(the office address you gave on page 1)', { req: true, ok: sameOffice ? (ltd ? 'Same as your registered office' : '') : 'Copied from page 1' }),
      T('Postcode', sameOffice && ltd ? 'BT1 1AA' : '', { req: true }),
      C('Use the organisation telephone and email for the agency?', 'svcSame', yn),
      T('Service Telephone', A.svcSame === 'n' ? '' : '028 9000 0000', { ok: A.svcSame === 'n' ? '' : 'Same as the organisation' }), T('Service Email', A.svcSame === 'n' ? '' : 'hello@laganviewcare.co.uk', { ok: A.svcSame === 'n' ? '' : 'Same as the organisation' }),
      M('HSC Trust Area(s) (Select where your service will operate)', 'trusts', ['Belfast HSC Trust', 'South Eastern HSC Trust', 'Northern HSC Trust', 'Southern HSC Trust', 'Western HSC Trust'], { req: true, tip: 'Tick every Trust area you will work in.' }),
      T('Specific Areas (if not covering entire Trust area)', '', { tip: 'For example the towns or council areas you will cover.' }),
      C('Age Range Supported', 'age', [['18', '18+'], ['65', '65+'], ['all', 'All ages']]),
      T('Expected Number of Service Users', '20', { req: true, tip: 'In your first 12 months. We use the same number in your business plan.' }),
      M('Service User Groups Supported (Select all that apply)', 'groups', ['Older People', 'Dementia', 'Physical Disability', 'Learning Disability', 'Autism', 'Mental Health', 'Sensory Impairment', 'End of Life Care', 'Other'], { req: true, tip: 'Only tick groups you are ready to support. RQIA expects your staff training to match.' }));
    if (groups.includes(8)) svc.push(T('Other service user group: please describe', '', { req: true }));
    svc.push(T('When would you like to start providing care? (month and year)', '', { tip: 'Added by the Hub. Helps us plan your timeline. You cannot start until RQIA registers you.' }));
    S.push({ id: 'svc', title: 'Service Details', intro: 'The service you are registering with RQIA.', fields: svc });

    const how = [C('Will you provide personal care (for example washing, dressing, help with the toilet)?', 'pc', yn),
      C('What help with medicines will you give?', 'meds', [['none', 'None'], ['prompt', 'Reminding (prompting) only'], ['admin', 'Giving medicines (administering)']]),
      C('Will staff help people with their money (for example shopping)?', 'money', yn),
      T('How many care staff do you plan to start with?', '', { tip: 'A rough number is fine. RQIA looks for a staffing plan that fits the number of people you support.' }),
      T('Roughly what will you charge per hour?', '', { tip: 'A rough figure is fine. Your Service User Guide sets out your fees, and we use it in your business plan.' }),
      M('Who will pay for the care?', 'funders', ['HSC Trusts', 'People paying for themselves', 'Other'], { tip: 'Tick all you expect.' })];
    if (A.pc === 'n') how.splice(1, 0, I('A domiciliary care agency provides personal care, so without it you may not need to register in the same way. Your consultant will check this with you before anything else.', 'warn'));
    if (groups.includes(3) || groups.includes(4)) how.push(P('Your experience supporting people with a learning disability or autism', '', { req: true, tip: 'You ticked learning disability or autism. RQIA will want to see the RI and manager have experience here.' }));
    S.push({ id: 'how', title: 'How You Will Work', intro: 'Added by the Hub. Short answers that shape your Statement of Purpose, policies and staffing plan, so we do not have to ask later.', fields: how });

    const offList = [['o1', 'Officer 1' + (P1.name ? ': ' + P1.name : '')]].concat(!sole && A.o2 === 'y' ? [['o2', 'Officer 2' + (P2.name ? ': ' + P2.name : '')]] : []).concat(!sole && A.o2 === 'y' && A.o3 === 'y' ? [['o3', 'Officer 3']] : []).concat(sole || A.entity === 'part' ? [] : [['other', 'Someone else, such as a manager or company secretary']]);
    const R = A.riWho === 'o2' ? P2 : ((A.riWho === 'o3' || A.riWho === 'other') ? E : P1);
    const cp = v => v ? 'Copied from the officers page' : '';
    S.push({ id: 'ri', title: 'Responsible Individual (RI) Details', intro: sole ? 'As a sole trader, you carry on the agency yourself, so RQIA checks that you are fit. These are your own details.' : A.entity === 'part' ? 'In a partnership, the partners carry on the agency. Choose the partner who will lead, for example on training.' : 'The RI is the person with strategic oversight of the service. For an organisation, the RI must be a director, manager, secretary or other officer.', fields: [
      C('Which officer will be the Responsible Individual?', 'riWho', offList, { tip: 'Their details are copied from the officers page, so you do not type them twice.' }),
      I('Personal Details'),
      T('Full Name', R.name, { req: true, ok: cp(R.name) }), T('Date of Birth (dd/mm/yyyy)', R.dob, { req: true, ok: cp(R.dob) }),
      T('Place of Birth', '', { req: true }), T('Any Previous Surnames', '', { tip: 'Write "None" if there are none.' }),
      T('Current Address', R.home, { req: true, tip: 'Type the postcode to find the address.' }), T('Postcode', R.pc, { req: true }),
      T('Telephone'), T('Mobile', R.tel, { req: true, ok: cp(R.tel) }), T('Email', R.email, { req: true, ok: cp(R.email) }), T('Position in Organisation', R.name ? 'Director' : '', { req: true, ok: cp(R.name) }), T('National Insurance number', '', { tip: 'Added by the Hub. Needed for the AccessNI check.' }),
      I('5-Year Address History (Complete history with no gaps)\nAdd each address with the month and year you moved in and out. We check the dates join up and tell you if there is a gap.'),
      T('Address 1 (current): Address (including Postcode), From (MM/YYYY) to present', R.home ? R.home + ' ' + R.pc + ', from 02/2018' : '', { req: true, ok: R.home ? 'Copied from the current address above. Just add the date you moved in.' : '' }),
      T('Address 2: Address (including Postcode), From (MM/YYYY) to (MM/YYYY)'), T('Address 3: Address (including Postcode), From (MM/YYYY) to (MM/YYYY)'),
      I('Add another address appears when you need it. The 5 years are covered when the bar fills.', 'ok')] });

    const ID2 = ['Current valid passport', 'Driving licence (photocard)', 'eVisa (we check it online with a share code)', 'Biometric residence permit (an expired one showing indefinite leave may still be accepted)', 'Electoral Identity Card (NI)', 'Birth certificate', 'Utility bill (within last 3 months)', 'Bank statement (within last 3 months)'];
    const aniBlock = (who, k) => {
      const f = [C(who + 'Do you have a current Enhanced AccessNI Disclosure?', k + 'Ani', yn)];
      if (A[k + 'Ani'] === 'y') f.push(T(who + 'AccessNI Certificate Number', ''), T(who + 'Date Issued (dd/mm/yyyy)', ''),
        I('Thank you. RQIA checks the people it registers through its own AccessNI application, and AccessNI certificates do not move with you the way a DBS on the Update Service can. So we still collect your ID documents for RQIA\'s check.', 'info'));
      f.push(I('If applying new, note RQIA PIN: 497850\nWe use this when we apply for the AccessNI check with you.', 'warn'),
        M(who + 'Provide THREE of the following ID documents', k + 'Ids', ID2, { req: true, tip: 'Tick three, including at least one photo ID (passport, photocard licence or eVisa) and at least one showing your current address. We ask for a photo of each on the documents page.' }));
      return f;
    };
    S.push({ id: 'ani', title: 'AccessNI Information', intro: 'For the Responsible Individual. RQIA runs the check, and we prepare it with you.', fields: aniBlock('', 'ri') });

    const ql = [P('Relevant qualifications', '', { tip: 'Added by the Hub. List each one. Copies go on the documents page.' }),
      C('Are you registered with a professional body (for example NISCC or the NMC)?', 'riProf', yn, { tip: 'Added by the Hub.' })];
    if (A.riProf === 'y') ql.push(T('Professional body and registration number', '', { req: true }));
    ql.push(C('Have you ever been investigated by a professional regulator, in any country?', 'riInv', yn, { tip: 'Added by the Hub.' }));
    if (A.riInv === 'y') ql.push(P('Please tell us what happened', '', { req: true }));
    ql.push(P('Your experience of care and of running things', '', { tip: 'Added by the Hub. A few lines. RQIA wants to see the RI understands how to oversee a care service, so we build this into a strong answer with you.' }));
    S.push({ id: 'riq', title: 'RI Qualifications and Experience', intro: 'Added by the Hub. RQIA looks at these for the RI.', fields: ql });
    const hist = [['h1', 'Previously registered with RQIA to provide regulated care?'], ['h2', 'Ever refused registration by RQIA or other UK regulator?'], ['h3', 'Ever had registration cancelled by enforcement action?'], ['h4', 'Ever prosecuted relating to a regulated service?'], ['h5', 'Any other business interests in regulated care?']];
    const hf = [];
    hist.forEach(([k, q]) => { hf.push(C(q, k, yn, k === 'h2' ? { tip: 'Include CQC, CIW, the Care Inspectorate in Scotland and Ofsted.' } : {})); if (A[k] === 'y') hf.push(P('Please tell us more', '', { req: true, tip: 'Added by the Hub. RQIA will ask, so a short note now saves time: when, which regulator or service, and what happened.' })); });
    S.push({ id: 'hist', title: 'Registration History', intro: 'For the Responsible Individual. A Yes does not stop an application, but leaving something out can.', fields: hf });

    const refBlock = (who, k) => {
      const yo = who ? 'the manager' : 'you';
      const f = [I((who ? 'The manager needs their own TWO references. ' : 'RQIA requires TWO references. ') + 'One MUST be from ' + (who ? 'their' : 'your') + ' present or most recent employer, if there is one.', 'warn')];
      ['1', '2'].forEach(n => f.push(I(who + 'Referee ' + n + (n === '1' ? ': must be current/most recent employer (if any)' : '')), T(who + 'Referee ' + n + ': Full Name', '', { req: true }), T(who + 'Referee ' + n + ': Job Title / Position', '', { req: true }), T(who + 'Referee ' + n + ': Organisation', '', { req: true }),
        T(who + 'Referee ' + n + (who ? ': Relationship to the Manager' : ': Relationship to You'), '', { req: true, tip: 'And how long they have known ' + yo + '. For example: ' + (who ? 'their' : 'my') + ' line manager at Example Care from 2019 to 2024.' }),
        T(who + 'Referee ' + n + ': Email', '', { req: true }), T(who + 'Referee ' + n + ': Telephone', '', { req: true })));
      f.push(C(who + 'Please confirm: is Referee 1 from ' + (who ? 'their' : 'your') + ' present or most recent employer?', k + 'Cur', [['y', 'Yes'], ['n', 'No'], ['none', 'There is no previous employer']], { tip: 'Added by the Hub.' }));
      if (A[k + 'Cur'] === 'n') f.push(I('The regulations ask for one reference from the present or most recent employer, if there is one. Please change Referee 1, or tell your consultant why that is not possible.', 'warn'));
      if (A[k + 'Cur'] === 'none') f.push(I('That is fine. Choose two people who know ' + (who ? 'them' : 'you') + ' well through work or volunteering, and who are not relatives.', 'ok'));
      f.push(C(who + 'Is either referee related to ' + yo + '?', k + 'Rel', yn, { tip: 'Added by the Hub. A relative is not a strong reference, so we flag it now rather than after RQIA asks.' }));
      if (A[k + 'Rel'] === 'y') f.push(I('Please choose a different referee who is not a relative. Your consultant can help you think of one.', 'warn'));
      return f;
    };
    S.push({ id: 'refs', title: 'RI References', intro: 'Two people who can speak about your work.', fields: refBlock('', 'ri') });
    const gpBlock = who => [T(who + 'GP Name', '', { req: true }), T(who + 'Surgery/Practice Name', '', { req: true, ok: 'Searching the practice fills in the address' }), T(who + 'Surgery Address', '', { req: true }), T(who + 'Postcode', '', { req: true }), T(who + 'Surgery Telephone', '', { req: true })];
    S.push({ id: 'gp', title: 'RI GP Details', intro: 'RQIA requires a health declaration.', fields: gpBlock('') });

    const rmDiff = A.riRm === 'n';
    const rm = [C('Will the RI also be the Registered Manager?', 'riRm', yn)];
    if (A.riRm === 'y') rm.push(I("We use the RI's details, AccessNI, references and GP for the manager too, so you only need the qualification and registration below.", 'ok'));
    else rm.push(I('The manager also applies to RQIA to be registered as manager. We prepare that with them.', 'ok'), T('Full Name', '', { req: true }), T('Date of Birth (dd/mm/yyyy)', '', { req: true }), T('Address', '', { req: true }), T('Postcode', '', { req: true }), T('Telephone', '', { req: true }), T('Email', '', { req: true }));
    rm.push(T('NISCC/NMC/HCPC Registration Number', '', { tip: 'The manager of a domiciliary care agency registers with NISCC. If not yet registered, write "applying".' }),
      C('Level 5 qualification in health and social care management', 'l5', [['held', 'Held'], ['prog', 'Working towards it'], ['no', 'Not started']], { tip: 'Added by the Hub. RQIA looks for this, so we plan for it early.' }));
    if (A.l5 === 'no') rm.push(I('RQIA expects the manager to hold Level 5 or be working towards it. Your consultant will go through the options with you.', 'warn'));
    rm.push(P('Relevant Qualifications'));
    if (rmDiff) rm.push(T('Manager: Place of Birth', '', { req: true, tip: 'Added by the Hub. Needed for their AccessNI check.' }), T('Manager: Any Previous Surnames', '', { tip: 'Write "None" if there are none.' }), T('Manager: National Insurance number'), I('Manager 5-Year Address History'), T('Manager Address 1 (current): Address (including Postcode), From (MM/YYYY) to present', '', { req: true }), T('Manager Address 2: Address (including Postcode), From (MM/YYYY) To (MM/YYYY)'));
    S.push({ id: 'rm', title: 'Registered Manager Details', intro: 'The person in day-to-day charge of the agency.', fields: rm });
    if (rmDiff) {
      S.push({ id: 'rmani', title: 'Registered Manager: AccessNI', intro: 'Added by the Hub. RQIA runs an AccessNI check for the manager too.', fields: aniBlock('Manager: ', 'rm') });
      const rh = [C('Manager: has any of these ever applied to them?', 'rmHist', yn, { tip: 'Previously registered with RQIA; refused registration by RQIA or another UK regulator; registration cancelled by enforcement; prosecuted relating to a regulated service; investigated by a professional regulator; other business interests in regulated care.' })];
      if (A.rmHist === 'y') rh.push(P('Manager: please tell us which, and what happened', '', { req: true }));
      S.push({ id: 'rmref', title: 'Registered Manager: References', intro: 'Added by the Hub. The manager is registered with RQIA in their own right, so we collect their references now.', fields: refBlock('Manager: ', 'rm') });
      S.push({ id: 'rmgp', title: 'Registered Manager: GP and History', intro: 'Added by the Hub. For the manager\'s own health declaration and fitness checks.', fields: gpBlock('Manager: ').concat([I('Registration history')], rh) });
    } else skipped.push('Registered Manager: AccessNI', 'Registered Manager: References', 'Registered Manager: GP and History');

    const docs = [I('For ALL Directors/Officers/Responsible Individual/Registered Manager: a CV for each person (full employment history, no gaps, with start/end dates). One upload per person, so nothing gets mixed up.'),
      F('CV: Officer 1' + (P1.name ? ', ' + P1.name : ''), 'CV received', { req: true, ok: 'Received. We check it for gaps and ask you about any.' })];
    if (!sole && A.o2 === 'y') docs.push(F('CV: Officer 2' + (P2.name ? ', ' + P2.name : ''), 'Add file', { req: true }));
    if (rmDiff) docs.push(F('CV: Registered Manager', 'Add file', { req: true }));
    docs.push(F('For AccessNI (for RI and Manager): RI ID documents (the THREE you ticked)', 'Add photos', { req: true }));
    if (rmDiff) docs.push(F('For AccessNI (for RI and Manager): manager ID documents (the THREE you ticked)', 'Add photos', { req: true }));
    docs.push(F('Qualification certificates (RI and manager)', 'Add files', { tip: 'Added by the Hub. Photos are fine.' }),
      F('Proof of right to work in the UK (only if not a British or Irish citizen)', 'Add file', { tip: 'Added by the Hub. For example a share code or visa.' }),
      M('Which of these do you already have? (we create the rest with you)', 'have', ['Statement of Purpose', 'Service User Guide', 'Policies and procedures', 'Staffing plan and training plan', 'Business plan and financial forecast', 'Bank letter or statement showing funds', "Employer's and public liability insurance", 'An office for the agency'], { tip: 'Added by the Hub. This shapes your documents list. Leave a box empty if you are not sure.' }));
    S.push({ id: 'docs', title: 'Required Documents', intro: 'Upload now or later from your documents page. Your progress is saved either way.', fields: docs });
    S.push({ id: 'decl', title: 'Declaration', intro: 'Last of all.', fields: [
      M('Please confirm each statement', 'decl', ['I confirm the information provided is true and accurate', 'I understand that providing false information may result in refusal or cancellation of registration', 'I consent to RQIA processing this information for regulatory purposes', 'I agree to Care Sync Experts using these answers to prepare and make our RQIA application with us'], { req: true, tip: 'The last statement lets us act for you. We never submit anything without your approval.' }),
      T('Full Name', P1.name, { req: true }), T('Position', P1.name ? 'Director' : '', { req: true }), SG('Signature', P1.name, { req: true, tip: 'Sign with your finger or mouse. No need to print or scan.' }), T('Date', '04/11/2026', { ok: 'Filled in for you' })] });
'''
INIT = "{ entity: 'ltd', princ: 'y', ico: 'n', portal: 'n', pos1: 'dir', pos2: 'dir', o2: 'y', o3: 'n', svcType: 'dca', trusts: [0, 1], age: '18', groups: [0, 1, 2], pc: 'y', meds: 'prompt', money: 'n', riWho: 'o1', riAni: 'n', riIds: [0, 1, 6], h1: 'n', h2: 'n', h3: 'n', h4: 'n', h5: 'n', riCur: 'y', riRel: 'n', riRm: 'y', l5: 'held', rmAni: 'n', rmIds: [], rmCur: 'y', rmRel: 'n', rmHist: 'n', dcaKind: 'conv', svcSame: 'y', funders: [], riProf: 'n', riInv: 'n', have: [], decl: [] }"
build(sys.argv[1], 'RQIA Registration Information Form', 'RQIA Registration Information Form', 'Niamh', 1900, JS, INIT, 'refs',
      'Grace checks it now. As soon as it passes, your project starts and your consultant begins your RQIA pack. A copy of your answers comes to you by email.')
