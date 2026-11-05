import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from engine import build
JS = r'''
    const yn = [['y', 'Yes'], ['n', 'No']];
    const svc5 = [['1', '1. Home care'], ['2', '2. Supported living'], ['3', '3. Care home'], ['4', '4. Community support'], ['5', '5. Other']];
    const refYN = [['y', 'Yes'], ['n', 'Not yet']];
    S.push({ id: 'tender', title: 'This tender', intro: 'Thank you for choosing Care Sync Experts. This form gathers what we need to write your tender.', fields: [
      T('1.1 Link to the tender portal', 'https://northshire.proactis.example/tender/114'),
      T('1.2 Tender name or reference number', 'Northshire home support framework, NS/2026/114', { req: true }),
      T('1.3 Closing date and time', 'Tuesday 1 December, 12:00', { req: true, tip: 'If two documents give different times, use the earlier one.' }),
      T('1.4 Portal username', 'kemi@oakleafliving.co.uk'),
      T('1.5 Portal password', '', { ph: 'Goes straight into the secure vault', tip: 'Only our bid team can see this. If your portal lets you add extra users, you can add our bid lead instead and leave this blank. Please change your password after the contract is awarded.', ok: 'Stored in the encrypted vault, never shown in the form or in emails' }),
      C('1.6 Have you registered on the portal already?', 'reg', [['full', 'Yes, fully registered'], ['part', 'Started but not finished'], ['not', 'Not yet registered'], ['ns', 'Not sure']]),
      C('1.7 Have you saved PDF copies of the tender documents?', 'pdfs', [['y', 'Yes, I will send them'], ['n', 'No, please download them from the portal'], ['ns', 'I am not sure how to download them']], { req: false }),
      M('1.8 Authority to submit', 'auth', ['I authorise Care Sync Experts to upload and submit this tender on our behalf, once we have approved the final version and the declarations.'], { req: true }),
      C('1.9 Have you completed this form for Care Sync Experts before?', 'first', [['no', 'No, this is our first time'], ['yes', 'Yes, for an earlier tender']], { tip: 'When you are signed in, we answer this for you, so you will only see it if we are not sure.' }),
      C('Is your company already providing care?', 'trading', [['y', 'Yes'], ['n', 'No, we are a new company']], { tip: 'Added by the Hub. New companies get a shorter route: no track record pages, just your experience and plans.' })] });
    const back = A.first === 'yes';
    if (back) {
      S.push({ id: 'changed', title: 'What has changed', intro: 'Welcome back. Your answers from last time are kept, so just tell us what is different.', fields: [
        P('R.1 What has changed since you last filled in this form?', '', { req: true, tip: "For example key people, staff numbers, CQC rating or registration, insurance renewals, new contracts or new accreditations. Write 'nothing' if nothing has changed." }),
        F('New or renewed documents', 'Add files here instead of emailing them'),
        I('Your company, regulator, people, finance, track record, workforce, partners, documents and evidence are kept from last time, so those pages are skipped. Only this tender\'s pages follow.', 'ok')] });
      skipWord = 'kept from last time or not needed';
      skipped.push('About your company', 'Your regulator', 'Regulator details', 'Ages and specialisms', 'Key people', 'Finance and insurance', 'Track record', 'Private clients', 'Workforce', 'Partnerships', 'Documents and policies', 'Evidence');
    } else {
      skipped.push('What has changed');
      S.push({ id: 'company', title: 'About your company', intro: 'Filled in from Companies House where we could.', fields: [
        T('3.1 Legal name of the company', 'Oakleaf Living Ltd', { req: true, ok: 'From Companies House' }), T('3.2 Trading name (if different from the legal name)', 'Oakleaf Living'),
        T('3.3 Registered office address', '8 Station Road, Northshire NS1 2AB', { req: true }), T('3.4 Service delivery address (if different from the registered office)'),
        T('3.5 Main phone number', '07700 900321', { req: true }), T('3.6 Main email address', 'hello@oakleafliving.co.uk', { req: true }), T('3.7 Website address', 'oakleafliving.co.uk'),
        T('3.8 Date the company was registered', '04/03/2021', { ok: 'From Companies House' }), T('3.9 Company registration number', '99000555', { ok: 'From Companies House' }),
        T('3.10 Charity registration number (if applicable)'), T('3.11 VAT number (if registered for VAT)'), T("3.12 Information Commissioner's Office (ICO) registration number", 'ZA000000'),
        C('3.13 Have you registered on the Central Digital Platform (Find a Tender)?', 'cdp', [['y', 'Yes, and I have our share code'], ['n', 'Not registered yet'], ['ns', 'Not sure']], { req: false })]
        .concat(A.cdp === 'y' ? [T('3.14 Central Digital Platform share code', '', { tip: 'You will find it in your Find a Tender account.' })] : [])
        .concat([T('3.15 DUNS number (optional)'),
          C('3.16 Trading status', 'trading', [['st', 'Sole trader'], ['pa', 'Partnership'], ['llp', 'Limited Liability Partnership (LLP)'], ['ltd', 'Private limited company'], ['plc', 'Public limited company (PLC)'], ['clg', 'Company limited by guarantee'], ['cic', 'Community Interest Company (CIC)'], ['ch', 'Charity or charitable incorporated organisation'], ['oth', 'Other']])]) });
      S.push({ id: 'regulator', title: 'Your regulator', intro: 'Not registered yet, or not regulated? Choose that option and we will call you, because most care tenders need registration for the regulated activity.', fields: [
        C('2.1 Which regulator covers the service in this tender?', 'regu', [['cqc', 'CQC, Care Quality Commission (England)'], ['ciw', 'CIW, Care Inspectorate Wales (Wales)'], ['rqia', 'RQIA, Regulation and Quality Improvement Authority (Northern Ireland)'], ['ofsted', "Ofsted (children's services in England)"], ['scot', 'Care Inspectorate (Scotland)'], ['applying', 'Not yet registered, applying now'], ['none', 'Not regulated (for example non-regulated community support)']]),
        T('2.2 If you are registered with more than one regulator, which ones and in which countries?')] });
      if (A.regu === 'cqc') {
        S.push({ id: 'cqc4', title: '4A. Your CQC registration details', intro: 'Filled in from the CQC register where we could.', fields: [
          T('4A.1 CQC provider ID', '1-000000001', { tip: 'It starts with 1- and is shown on your CQC web page.', ok: 'From the CQC register' }), T('4A.2 CQC location ID for every location that would deliver this contract', '1-000000002', { tip: 'Location IDs also start with 1- and are different from your provider ID.' }),
          T('4A.3 Link to your CQC web page', 'cqc.org.uk/location/1-000000002'), T('4A.4 Date of your most recent CQC inspection', '12/05/2025'),
          C('4A.5 Overall CQC rating', 'rating', [['o', 'Outstanding'], ['g', 'Good'], ['ri', 'Requires improvement'], ['i', 'Inadequate'], ['nr', 'Not yet rated']], { req: false }),
          C('4A.6 Are you subject to any CQC conditions of registration?', 'cond', [['no', 'No conditions'], ['yes', 'Yes'], ['ns', 'Not sure']], { req: false })]
          .concat(A.cond === 'yes' ? [P('4A.7 If yes, please describe the conditions')] : []) });
        S.push({ id: 'cqc56', title: '5A and 6A. Your CQC services and service user bands', intro: 'Tick what is shown on your registration.', fields: [
          M('5A.1 Regulated activities on your CQC registration', 'acts', ['Personal care', 'Accommodation for persons who require nursing or personal care', 'Accommodation for persons who require treatment for substance misuse', 'Accommodation and nursing or personal care in the further education sector', 'Treatment of disease, disorder or injury', 'Assessment or medical treatment for persons detained under the Mental Health Act 1983', 'Surgical procedures', 'Diagnostic and screening procedures', 'Management of supply of blood and blood derived products', 'Transport services, triage and medical advice provided remotely', 'Maternity and midwifery services', 'Termination of pregnancies', 'Services in slimming clinics', 'Nursing care', 'Family planning'], { tip: 'Tick the activities shown on your registration.' }),
          M('5A.2 Service types on your CQC registration', 'types', ['Domiciliary care agency (DCA)', 'Supported living service (SLS)', 'Extra care housing service', 'Shared Lives service', 'Care home service with nursing (CHN)', 'Care home service without nursing (CHS)', 'Community based services for people with a learning disability (LDC)', 'Community based services for people with mental health needs (MHC)', 'Community based services for people who misuse substances (SMC)', 'Specialist college service', 'Hospice service', 'Hospice service at home', 'Dental service', 'Doctors consultation service', 'Doctors treatment service']),
          M('6A.1 CQC service user bands', 'bands', ['Older people (65 and over)', 'Younger adults (18 to 65)', 'Children (under 18)', 'Whole population', 'Dementia', 'Learning disability or autistic spectrum disorder', 'Mental health needs', 'Physical disability', 'Sensory impairment', 'Drug and alcohol misuse', 'Eating disorders', 'People detained under the Mental Health Act 1983'], { tip: 'Tick the bands shown on your CQC registration.' })] });
        skipped.push('CIW pages', 'RQIA pages', '5D');
      } else if (A.regu === 'ciw') {
        S.push({ id: 'ciw4', title: '4B, 5B and 6B. Your CIW registration', intro: 'Your Care Inspectorate Wales details.', fields: [
          T('4B.1 CIW provider ID'), T('4B.2 Link to your CIW web page'), T('4B.3 Date of your most recent CIW inspection'),
          M('4B.4 Regional Partnership Board areas you operate in', 'rpb', ['North Wales', 'Powys', 'West Wales', 'Cwm Taf Morgannwg', 'Cardiff and Vale', 'Gwent', 'Swansea Bay']),
          P('4B.5 Your Welsh language Active Offer arrangements'),
          M('5B.1 Service types you are registered for', 'ciwTypes', ['Domiciliary support service (home care in Wales)', 'Supported living (delivered under a domiciliary support service)', 'Extra care housing (delivered under a domiciliary support service)', 'Care home service (adults)', 'Care home service (children)', 'Secure accommodation service', 'Residential family centre service', 'Adoption service', 'Fostering service', 'Adult placement service', 'Advocacy service']),
          M('6B.1 CIW range of needs', 'ciwNeeds', ['Older adults (65 and over)', 'Younger adults (18 to 65)', 'Children and young people (under 18)', 'People with a learning disability', 'Autistic people', 'People with mental health needs', 'People with a physical disability', 'People with a sensory impairment', 'People living with dementia', 'People at the end of their life', 'People recovering from substance misuse'])] });
        skipped.push('CQC pages', 'RQIA pages', '5D');
      } else if (A.regu === 'rqia') {
        S.push({ id: 'rqia4', title: '4C, 5C and 6C. Your RQIA registration', intro: 'Your RQIA details.', fields: [
          T('4C.1 RQIA registration number'), T('4C.2 Link to your RQIA web page'), T('4C.3 Date of your most recent RQIA inspection'),
          M('4C.4 HSC Trust areas you cover', 'trusts', ['Belfast HSC Trust', 'Northern HSC Trust', 'South Eastern HSC Trust', 'Southern HSC Trust', 'Western HSC Trust']),
          M('5C.1 Service types you are registered for', 'rqTypes', ['Domiciliary care agency', 'Supported living (regulated as domiciliary care in Northern Ireland)', 'Nursing home', 'Residential care home', 'Day care setting', "Children's home", 'Adult placement agency', 'Independent clinic', 'Independent hospital', 'Boarding school', 'Voluntary adoption agency', 'Day nursery']),
          M('6C.1 RQIA service user groups', 'rqGroups', ['Older people (65 and over)', 'Younger adults (18 to 65)', 'Children and young people (under 18)', 'People with a learning disability', 'Autistic people', 'People with mental health needs', 'People with a physical disability', 'People with a sensory impairment', 'People living with dementia', 'People at the end of their life'])] });
        skipped.push('CQC pages', 'CIW pages', '5D');
      } else {
        S.push({ id: '5d', title: '5D. Your services and registration position', intro: 'We will call you, because most care tenders need registration for the regulated activity.', fields: [
          P('5D.1 Tell us about the services you offer and your registration position', '', { tip: 'If you are applying for registration, tell us which regulator and where the application is up to.' })] });
        skipped.push('CQC pages', 'CIW pages', 'RQIA pages');
      }
      S.push({ id: '6d', title: '6D. Ages and specialisms', intro: '', fields: [
        T('6D.1 Youngest age you support', '18', { ok: 'Checked: a number' }), T('6D.2 Oldest age you support', '', { tip: 'Leave blank if there is no upper limit.' }), P('6D.3 Any inclusion or exclusion criteria?'),
        M('6D.4 Specialisms and conditions your team has experience with', 'spec', ['Learning disabilities', 'Autistic people', 'Mental health conditions', 'Dementia', 'Physical disabilities', 'Sensory impairment (sight or hearing)', 'Complex health conditions', "Long term conditions (multiple sclerosis, Parkinson's, motor neurone disease)", 'End of life and palliative care', 'Acquired brain injury', 'Substance misuse (drugs and alcohol)', 'Homelessness', 'Rough sleepers', 'Adults after a hospital discharge', 'Social isolation and befriending', "Young adults moving from children's to adult services", 'Care leavers', 'Looked after children', 'Ex-offenders', 'Modern slavery survivors', 'Asylum seekers and refugees', 'Domestic abuse survivors', 'Behaviour that challenges (positive behaviour support)', 'Eating disorders', 'Bariatric care', 'Hospital patient transport', 'Reablement and intermediate care', 'Other'])] });
      S.push({ id: 'people', title: '7. Key people in your organisation', intro: 'Owner, Nominated or Responsible Individual, and Registered Manager.', fields: [
        I('Owner, director or partner'), T('7.1 Full name', 'Kemi Adeyemi', { req: true }), T('7.2 Role in the organisation', 'Director'), T('7.3 Phone number', '07700 900321'), T('7.4 Email address', 'kemi@oakleafliving.co.uk'),
        I('Nominated Individual (CQC) or Responsible Individual (CIW and RQIA)'), T('7.5 Full name', 'Kemi Adeyemi', { ok: 'Same as 7.1? One tap fills it in' }), T('7.6 Job title'), T('7.7 Phone number'), T('7.8 Email address'),
        I('Registered Manager'), T('7.9 Full name'), T('7.10 Qualification'), T('7.11 Phone number'), T('7.12 Email address'),
        P('7.13 Other senior staff, directors or trustees'), F('CVs of your senior management team', 'Add files here instead of emailing them')] });
      S.push({ id: 'finance', title: 'Finance and insurance', intro: 'Buyers check these before they read any of your answers, so accuracy here matters.', fields: [
        T('F.1 Turnover in your last full financial year', '£640,000', { req: true, tip: 'Approximate is fine, in pounds. New company and not trading yet? Write "Not trading yet" and we will plan the bid around that.' }), T('F.2 Turnover in the year before', '£510,000'),
        C('F.3 Are your accounts filed and up to date at Companies House?', 'accounts', [['y', 'Yes'], ['over', 'No, they are overdue'], ['new', 'New company, none filed yet']], { ok: 'Checked at Companies House: up to date' })]
        .concat(A.accounts === 'new' ? [M('F.4 If you are a new company, what could you offer instead?', 'alt', ['Management accounts', 'Financial forecasts', 'A bank reference letter', 'A parent company guarantee', 'Not sure'])] : [])
        .concat([P('F.5 Insurance cover and expiry dates', '', { req: true, tip: "Employer's liability, public liability and professional indemnity: the amount of cover and the expiry date for each." }), T("F.6 Your accountant's name and email")]) });
      if (A.trading === 'n') {
        skipped.push('Track record', 'Contract examples', 'Private clients');
        S.push({ id: 'startup', title: 'Your experience and plans', intro: 'Added by the Hub. For a new company, buyers look at the people behind it and how you will start.', fields: [
          P('Care experience of the directors and the manager', '', { req: true, tip: 'Where you worked, your roles and for how long. This takes the place of a track record.' }),
          P('Any services you have led or managed before, for another provider', '', { tip: 'For example a team, a branch or a contract you ran as an employee.' }),
          T('How many care staff do you plan to start with?', '', { tip: 'A rough number is fine.' }),
          T('Who would lead the start of a new contract?', ''),
          F('Letters of support (optional)', 'Add file', { tip: 'For example from a local organisation you will work with.' }),
          I('We pick tenders that suit a new provider, such as dynamic markets and smaller lots, and tell you honestly when one is not worth the effort yet.', 'ok')] });
      } else {
        const tr = [C('8.1 What experience do you have of delivering care?', 'exp', [['pub', 'Public sector clients (councils, the NHS or other public bodies)'], ['priv', 'Private clients only (people or families paying for their own care)'], ['both', 'Both public sector and private clients'], ['none', 'None yet, this would be our first contract']], { tip: 'Private clients count too. If this would be your first contract, that is fine: we will talk about references in the meeting.' })];
        if (A.exp === 'pub' || A.exp === 'both') {
          const ex = (n, a) => [I('Contract or framework example ' + n + '. Ask your contact\'s permission before naming them as a referee.'), T('8.' + a + ' Customer or commissioner'), C('8.' + (a + 1) + ' Service type', 'ex' + n + 't', svc5, { req: false }),
            T('8.' + (a + 2) + ' Contact name at the customer'), T('8.' + (a + 3) + ' Contact job title'), T('8.' + (a + 4) + ' Contact email address'), C('8.' + (a + 5) + ' Has this contact agreed to be a referee?', 'ex' + n + 'r', refYN, { req: false }),
            P('8.' + (a + 6) + ' Short description of what you delivered'), T('8.' + (a + 7) + ' People supported and hours a week'), T('8.' + (a + 8) + ' Contract start date'), T('8.' + (a + 9) + " Contract end date, or 'ongoing'"), T('8.' + (a + 10) + ' Approximate annual value', '', { tip: 'In pounds. Approximate is fine.' })];
          tr.push(...ex(1, 2));
          tr.push(C('Do you have another contract example to add?', 'more1', yn));
        }
        S.push({ id: 'track', title: '8. Your track record', intro: '', fields: tr });
        if ((A.exp === 'pub' || A.exp === 'both') && A.more1 === 'y') {
          const ex = (n, a) => [I('Contract or framework example ' + n + '.'), T('8.' + a + ' Customer or commissioner'), C('8.' + (a + 1) + ' Service type', 'ex' + n + 't', svc5, { req: false }),
            T('8.' + (a + 2) + ' Contact name at the customer'), T('8.' + (a + 3) + ' Contact job title'), T('8.' + (a + 4) + ' Contact email address'), C('8.' + (a + 5) + ' Has this contact agreed to be a referee?', 'ex' + n + 'r', refYN, { req: false }),
            P('8.' + (a + 6) + ' Short description of what you delivered'), T('8.' + (a + 7) + ' People supported and hours a week'), T('8.' + (a + 8) + ' Contract start date'), T('8.' + (a + 9) + " Contract end date, or 'ongoing'"), T('8.' + (a + 10) + ' Approximate annual value', '', { tip: 'In pounds. Approximate is fine.' })];
          S.push({ id: 'ex2', title: 'Contract or framework example 2', intro: '', fields: ex(2, 13).concat([C('Do you have another contract example to add?', 'more2', yn)]) });
          if (A.more2 === 'y') S.push({ id: 'ex3', title: 'Contract or framework example 3', intro: '', fields: ex(3, 24) });
        }
        const pv = [C('8.A Do you also have private client experience to share?', 'priv', [['y', 'Yes, take me to the private client examples'], ['n', 'No, move on']])];
        if (A.priv === 'y') {
          const px = (n) => [I('Private client example ' + n + '. Use initials only for the person you supported.'), T('PRIV' + n + '.1 Private client initials'), C('PRIV' + n + '.2 Service type', 'p' + n + 't', svc5, { req: false }),
            T('PRIV' + n + '.3 Full name of the point of contact for the private client'), T('PRIV' + n + '.4 Their relationship to the private client'), T('PRIV' + n + '.5 Point of contact email address'),
            C('PRIV' + n + '.6 Has this contact agreed to be a referee?', 'p' + n + 'r', refYN, { req: false }), P('PRIV' + n + '.7 Short description of the care you delivered'), T('PRIV' + n + '.8 Hours of care a week'),
            T('PRIV' + n + '.9 Start date of care'), T('PRIV' + n + ".10 End date of care, or 'ongoing'"), T('PRIV' + n + '.11 Approximate weekly or annual value', '', { tip: 'In pounds. Approximate is fine.' })];
          pv.push(...px(1), C('Do you have another private client example to add?', 'pm1', yn));
        }
        S.push({ id: 'private', title: 'Private client experience', intro: '', fields: pv });
        if (A.priv === 'y' && A.pm1 === 'y') {
          const px = (n) => [T('PRIV' + n + '.1 Private client initials'), C('PRIV' + n + '.2 Service type', 'p' + n + 't', svc5, { req: false }),
            T('PRIV' + n + '.3 Full name of the point of contact for the private client'), T('PRIV' + n + '.4 Their relationship to the private client'), T('PRIV' + n + '.5 Point of contact email address'),
            C('PRIV' + n + '.6 Has this contact agreed to be a referee?', 'p' + n + 'r', refYN, { req: false }), P('PRIV' + n + '.7 Short description of the care you delivered'), T('PRIV' + n + '.8 Hours of care a week'),
            T('PRIV' + n + '.9 Start date of care'), T('PRIV' + n + ".10 End date of care, or 'ongoing'"), T('PRIV' + n + '.11 Approximate weekly or annual value', '', { tip: 'In pounds. Approximate is fine.' })];
          S.push({ id: 'pv2', title: 'Private client example 2', intro: 'Use initials only for the person you supported.', fields: px(2).concat([C('Do you have another private client example to add?', 'pm2', yn)]) });
          if (A.pm2 === 'y') S.push({ id: 'pv3', title: 'Private client example 3', intro: 'Use initials only for the person you supported.', fields: px(3) });
        }
      }
      S.push({ id: 'workforce', title: '9. Your workforce', intro: 'Approximate figures are fine. Tell us if you are not sure.', fields: [
        T('9.1 Total number of staff employed', '34', { req: true, tip: A.trading === 'n' ? 'New company? Give the number you plan to start with.' : '' }), C('9.2 Employee size band', 'band', [['micro', '1 to 10 (micro)'], ['small', '11 to 50 (small)'], ['med', '51 to 200 (medium)'], ['large', '201 to 1,000 (large)'], ['ent', '1,001 or more (enterprise)']], { req: false, ok: 'Worked out from 9.1' }),
        T('9.3 Number of care or support workers', '28', { req: true }), T('9.4 Number of senior care workers, team leaders or coordinators'), T('9.5 Number of registered nurses, if any'), T('9.6 Number of office and management staff'),
        T('9.7 Staff turnover in the last 12 months', '', { tip: 'A percentage, or how many left out of how many.' }), T('9.8 Current vacancies'), T('9.9 Staff who have completed Oliver McGowan training', '', { tip: 'A percentage, with Tier 1 and Tier 2 if you know them.' }),
        C('9.10 Do any of your staff hold sponsored work visas?', 'visa', [['n', 'No'], ['active', 'Yes, and our sponsor licence is active'], ['advice', 'Yes, and we need advice']], { req: false }),
        T('9.11 Drivers and non-drivers', '', { tip: 'A rough split is fine.' }), T('9.12 Languages spoken in your team'),
        T('9.13 Lowest hourly rate for care or support workers, and any enhancements', '', { req: true, tip: 'For example weekends, nights, travel time or mileage.', ok: 'We check it against the lawful wage' }),
        C('9.14 Who is responsible for staff training?', 'train', [['in', 'In house training team'], ['ext', 'External training provider'], ['mix', 'A mix of both'], ['el', 'eLearning platform']], { req: false }),
        T('9.15 Name of your training provider or eLearning platform'), T('9.16 Who is responsible for staff wellbeing, and health and safety?'), T('9.17 Which HR system do you use?'),
        P('9.18 Which systems do you use for care planning, rostering and call monitoring, medication records and incident reporting?', '', { tip: "Name each one, or write 'paper based'." })] });
      S.push({ id: 'partners', title: '13. Partnerships and social value', intro: '', fields: [
        M('13.1 Types of partnerships you have in place', 'ptypes', ['IT or software partners', 'Health partners (GPs, district nurses, mental health teams)', 'Housing providers or registered social landlords', 'Advocacy organisations', 'Community and voluntary organisations', 'Education and employment support providers', 'Transport providers', 'Equipment supply or maintenance', 'Training providers', 'Pharmacies', 'Local authority commissioning teams', 'Other']),
        P('13.2 Please name your most important partners and what they help with'), P('13.3 What do you already do for your local community?', '', { tip: 'For example local jobs, apprenticeships, volunteering, charity links, buying locally or cutting mileage.' }),
        P('13.4 What could you commit to every year of a contract, and who would own it?', '', { tip: 'Only include what you could really deliver. Social value commitments become part of the contract.' })] });
      S.push({ id: 'docs', title: '14. Documents and policies', intro: 'Upload here instead of emailing.', fields: [
        M('14.1 Company documents you can send us', 'docs', ['Statement of Purpose', 'Latest inspection report or action plan', "Employer's liability insurance certificate", 'Public liability insurance certificate', 'Professional indemnity insurance certificate', 'ICO registration', "Last two years' accounts", 'Organisation chart', 'Training matrix', 'Business continuity plan', 'Quality assurance and audit framework', 'Complaints log for the last 12 months', 'Equality monitoring data', 'Carbon reduction plan', 'Social value plan', 'DSPT submission', 'Cyber Essentials certificate', 'Modern slavery statement (if turnover is £36 million or more)', 'Property documents: gas safety, EPC, fire risk assessment', 'Feedback from previous tenders', 'Thank you cards or testimonials, anonymised', 'Photographs of staff or services, with consent']),
        I('About policies: policies are not part of your tender writing package. Tell us which policies you already have and keep up to date. If a tender asks for a policy you do not have, or yours is out of date, we can write or update it for an extra fee.'),
        M('14.2 Which of these policies do you already have, reviewed in the last 12 months?', 'pols', ['Safeguarding', 'Whistleblowing', 'Recruitment and selection', 'Medication', 'Health and safety', 'Equality, diversity and inclusion', 'Complaints', 'Data protection', 'Infection prevention and control', 'Business continuity', 'Modern slavery', 'Cyber security', 'None of these']),
        T('14.3 Who writes and reviews your policies?'), C('14.4 Would you like a quote for writing or updating any policies?', 'quote', [['y', 'Yes'], ['n', 'No'], ['d', "Let's discuss it in the meeting"]], { tip: 'If you say Yes, your consultant sends you a price. There is no obligation.' }),
        P('14.5 Anything missing?'), F('Your documents', 'Add files')] });
      S.push({ id: 'evidence', title: 'Your evidence', intro: 'This is the part that moves an answer from good to top marks. Give real figures from your records, with the period they cover.', fields: [
        P('E.1 What makes your service different from your competitors?', '', { tip: 'Give examples, not adjectives. What do you do that others do not?' }), P('E.2 What outcomes are you proudest of?'),
        P('E.3 Your figures for the last 12 months', '', { tip: 'Visits on time, missed visits, how many regular carers each person sees, time from referral to first visit, complaints and compliments, satisfaction survey results, incidents over time.' }),
        M('E.4 Accreditations and memberships you hold', 'accr', ['Cyber Essentials', 'Cyber Essentials Plus', 'DSPT Standards Met or above', 'Real Living Wage employer', 'ISO 9001', 'Investors in People', 'Disability Confident', 'Homecare Association member', 'Other']),
        P('E.5 Awards, praise or outside feedback', '', { tip: "For example a line from your CQC report, a council monitoring visit, a social worker's email or a family's card. Leave out the names of people you support." }),
        C('E.6 Can you give us four to six case studies?', 'cases', [['send', 'Yes, I will send them'], ['call', 'Please book a 15 minute call so I can talk them through'], ['not', 'Not yet']], { tip: 'A case study is a short, true story about someone you supported: what they needed, what your team did, and what changed.' }),
        P('E.7 Any concerns about this tender?')] });
    }
    S.push({ id: 'lots', title: 'Lots', intro: 'A lot is one part of the tender, with its own requirements, scoring and winner. You can usually bid for one lot or several.', fields: [
      P('L.1 Which lots do you want to bid for?', 'Lot 1 Home support North', { req: true, tip: "List the lot number and name. Not sure? Write 'not sure' and we will decide together in the meeting." }),
      T('L.2 If you won every lot you are bidding for, how many extra hours a week could you safely start in the first month?', '', { req: true, tip: 'An honest estimate is fine.' }),
      T('L.3 How many staff would work on these lots?'), T('L.4 Who would lead the start up if you win?', '', { tip: 'Name and role.' })] });
    S.push({ id: 'settings', title: 'Your services for this tender', intro: 'Only the pages for the settings in your lots will follow.', fields: [
      C('Does any lot you are bidding for include home care?', 'hc', yn, { tip: 'This includes reablement, live-in care and care in extra care housing.' }),
      C('Does any lot include supported living?', 'sl', yn), C('Does any lot include a care home?', 'ch', yn),
      C('Does any lot include community, outreach, floating or day support?', 'cs', yn)] });
    if (A.hc === 'y') S.push({ id: 'hc', title: 'Home care', intro: '', fields: [
      T('11.1 Local authority or HSC Trust areas you currently cover'), T('11.2 Towns or postcodes you can cover for the lots in this tender', '', { req: true }), T('11.3 Maximum travel time you allow between visits'),
      C('11.4 Shortest visit you offer', 'visit', [['15', '15 minutes'], ['30', '30 minutes'], ['45', '45 minutes'], ['60', '60 minutes'], ['oth', 'Other']], { req: false }),
      C('11.5 Do you offer double handed visits?', 'dh', [['y', 'Yes'], ['n', 'No'], ['notice', 'Yes, but only with notice']], { req: false }),
      M('11.6 Do you offer waking nights or sleep-in support?', 'nights', ['Waking nights', 'Sleep-in', 'Neither']), P('11.7 How are visits scheduled and monitored?'),
      M('11.8 Which of these do you deliver?', 'hcdo', ['Reablement', 'Live-in care', 'Care in extra care housing', 'Hospital discharge support', 'Night support', 'None of these'])] });
    else skipped.push('Home care');
    if (A.sl === 'y') {
      S.push({ id: 'sl', title: 'Supported living', intro: '', fields: [
        T('10.1 Areas where you could support people for this tender', '', { req: true }), M('10.2 How do you support people?', 'slhow', ['Shared hours across a house', 'One to one', 'Two to one', "Outreach into people's own homes"], { req: true }),
        M('10.3 Night support you can provide', 'slnight', ['Sleep-in', 'Waking night', 'Neither']),
        C('10.4 Who provides the property for this tender?', 'prop', [['council', 'The council or a housing provider named in the tender (we provide the support only)'], ['us', 'We do, or our landlord partner does'], ['ns', 'Not sure, please check the tender pack']])] });
      if (A.prop === 'us') S.push({ id: 'prop', title: 'Supported living property', intro: 'Tell us about the property you would provide.', fields: [
        T('10.5 Property name or reference'), T('10.6 Property location (town and postcode)', '', { req: true }),
        C('10.7 Type of property', 'ptype', [['det', 'Detached house'], ['semi', 'Semi-detached house'], ['ter', 'Terraced house'], ['bung', 'Bungalow'], ['flat', 'Flat or apartment'], ['annexe', 'Self-contained annexe'], ['oth', 'Other']], { req: false }),
        T('10.8 Number of bedrooms'), T('10.9 Number of bathrooms'), T('10.10 Number of communal areas (lounge, dining)'), T('10.11 Number of kitchens'), T('10.12 Approximate total square footage (optional)'),
        M('10.13 Accessibility features', 'acc', ['Wheelchair accessible throughout', 'Stairlift fitted', 'Wet room', 'Level access entry', 'Adapted kitchen', 'Adapted bathroom', 'Ceiling track hoist', 'Other']),
        M('10.14 Safety and security features', 'safe', ['Mains wired fire alarm system', 'Burglar alarm', 'Emergency call system or pendant alarms', 'CCTV (external only)', 'Secure entry system', 'Window restrictors']),
        M('10.15 Outside areas', 'out', ['Private garden', 'Communal garden', 'Parking on site', 'Outdoor storage', 'Secure boundary']),
        M('10.16 Local amenities within about a mile', 'amen', ['Supermarket or local shop', 'GP surgery', 'Pharmacy', 'Bus stop or train station', 'Library', 'Place of worship', 'Park or green space', 'Cafes or restaurants', 'Leisure centre or gym', 'Cinema or community centre']),
        T('10.17 Landlord or housing provider'), T('10.18 Management company (if different)'),
        C('10.19 Are there any other properties to include?', 'moreprop', [['n', 'No, just the one'], ['y', 'Yes, add another property here']], { req: false })] });
      else skipped.push('Supported living property');
    } else skipped.push('Supported living');
    if (A.ch === 'y') S.push({ id: 'ch', title: 'Care home', intro: '', fields: [
      T('12.1 Name of the care home', '', { req: true }), T('12.2 Full address of the care home'),
      C('12.3 Type of care home', 'chtype', [['n', 'Care home with nursing'], ['r', 'Care home without nursing (residential)'], ['c', "Children's home"], ['s', 'Specialist provision']], { req: false })]
      .concat(A.chtype === 's' ? [T('12.4 If specialist provision, please describe')] : [])
      .concat([T('12.5 Total number of registered beds'), T('12.6 Current number of residents'), T('12.7 Number of single rooms'), T('12.8 Number of rooms with en-suite'), T('12.9 Specialisms')]) });
    else skipped.push('Care home');
    if (A.cs === 'y') S.push({ id: 'cs', title: 'Community support', intro: 'For lots such as community outreach, floating support, day opportunities or befriending.', fields: [
      M('C.1 What kind of community support do you deliver?', 'cstype', ["Outreach into people's own homes", 'Floating housing related support', 'Day opportunities or a day centre', 'Befriending and social inclusion', 'Employment and volunteering support', 'Other'], { req: true }),
      C('C.2 Does any of it include personal care?', 'cspc', [['cqc', 'Yes, under our CQC registration'], ['n', 'No'], ['ns', 'Not sure']], { tip: 'In England, personal care is a regulated activity, so it must be covered by your registration.' }),
      T('C.3 Areas you can cover for this tender', '', { req: true }), T('C.4 Roughly how many hours a week of community support do you deliver now?')] });
    else skipped.push('Community support');
    S.push({ id: 'sign', title: 'Sign-off', intro: 'Thank you. Please check your answers, then confirm below.', fields: [
      T('16.1 Full name', 'Kemi Adeyemi', { req: true }), T('16.2 Job title', 'Director', { req: true }), T('16.3 Date', '04/11/2026', { req: true }),
      M('16.4 Declaration', 'decl', ['I confirm the information in this form is true and complete to the best of my knowledge.'], { req: true }),
      M('16.5 Consent', 'consent', ['I agree that Care Sync Experts can hold this information to prepare our tenders, and I have permission to share the contact and CV details given.'], { req: true })] });
'''
INIT = "{ reg: 'full', pdfs: 'y', auth: [0], first: 'no', cdp: 'y', trading: 'ltd', regu: 'cqc', rating: 'g', cond: 'no', acts: [0], types: [0], bands: [0, 1], spec: [3, 4], accounts: 'y', exp: 'both', ex1t: '1', ex1r: 'y', more1: 'n', priv: 'y', p1t: '1', p1r: 'y', pm1: 'n', band: 'small', visa: 'n', train: 'mix', ptypes: [1, 4], docs: [0, 1, 2, 3, 4, 6], pols: [0, 1, 2, 3, 4], quote: 'd', accr: [3], cases: 'call', hc: 'y', sl: 'n', ch: 'n', cs: 'n', visit: '30', dh: 'notice', nights: [1], hcdo: [3], prop: 'council', decl: [], consent: [] }"
build(sys.argv[1], 'Tender Preparation Questionnaire', 'Tender Preparation Questionnaire', 'Kemi', 2400, JS, INIT, 'workforce',
      'Daniel has your answers for this tender. Next time, your answers are kept and you only tell us what has changed.')
