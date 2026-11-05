import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from engine import build
BODIES = "['1. Nursing and Midwifery Council (NMC)', '2. Social Work England (SWE)', '3. Health and Care Professions Council (HCPC)', '4. General Medical Council (GMC)', '5. General Pharmaceutical Council (GPhC)', '6. General Dental Council (GDC)', '7. General Optical Council (GOC)', '8. General Osteopathic Council (GOsC)', '9. General Chiropractic Council (GCC)', '10. Pharmaceutical Society of Northern Ireland (PSNI)', '11. Other UK or overseas health or social care professional body']"
IDS = "['Current valid passport', 'Driving licence photocard', 'eVisa (we check it online with a share code)', 'Biometric residence permit (an expired one showing indefinite leave is accepted for up to 18 months after expiry)', 'Utility Bill', 'Bank Statement', 'Council Tax']"
JS = r'''
    const bodies = __BODIES__.map((b, j) => ['b' + j, b]);
    const ids = __IDS__;
    const yn = [['y', 'Yes'], ['n', 'No']];
    S.push({ id: 'status', title: 'Company Registration Status', intro: 'First, tell us whether your limited company is already registered with Companies House.', fields: [
      C('Is your limited company already registered with Companies House?', 'formed', [['yes', 'Yes, my company is already registered with Companies House'], ['no', 'No, please register the company for me as part of my CQC package']], { tip: 'Tip: If you already have a Company Registration Number (CRN), you are registered. If you have not yet incorporated a company, choose No and we will register it for you as part of your package.' })] });
    if (A.formed === 'yes') {
      skipped.push('Care Sync to Set Up Your Limited Company');
      S.push({ id: 'info', title: 'Company Information', intro: 'Filled in from Companies House where we could. Please check each one.', fields: [
        T('Registered Business Name:', 'Harbour Lane Care Ltd', { ok: 'From Companies House' }), T('Trading Name (if different):'), T('Company Registration Number (if applicable):', '99000101', { ok: 'From Companies House' }),
        T('Registered Office Address:', 'Flat 3, 14 Orchard Way, Stevenage SG1 2AB'), T('Correspondence Address (if different):'), T('Business Telephone Number:', '07700 900456', { req: true }),
        T('Company Email Address', 'amara@harbourlanecare.co.uk'), T('Website (if applicable):', 'harbourlanecare.co.uk'), T('Type of Legal Entity:', 'Private limited company'),
        T('Partners or owners who are not directors (if any)'), I("Each director's details are asked for in the next section.")] });
    } else {
      skipped.push('Company Information');
      const t = A.svcType || [];
      const sic = [];
      if (t.includes(0) || t.includes(1)) sic.push('88100');
      if (t.includes(1)) sic.push('87900');
      if (t.includes(3)) sic.push('88910');
      if (t.includes(4)) sic.push('87200');
      if (t.includes(2)) sic.push('87100');
      S.push({ id: 'setup1', title: 'Care Sync to Set Up Your Limited Company', intro: 'We will register your limited company with Companies House on your behalf. Please give us the details below so we do this correctly.', fields: [
        I('Service Type and SIC Codes\nCompanies House requires every UK company to register with SIC codes that match its actual business. CQC checks this when reviewing your application. Tell us what service type you are registering for and we will set the correct SIC codes for you.'),
        M('What care service type are you registering for?', 'svcType', ['Domiciliary care', 'Supported living', 'Care home with nursing', 'Children services or any service for under-18s', 'Specialist Learning Disability, Autism or Mental Health service'], { req: true, tip: 'Tip: Tick everything that applies. We will set the matching SIC codes automatically.' }),
        I(sic.length ? 'SIC codes we will register for you: ' + sic.join(', ') + '. You do not need to do anything here.' : 'Tick a service type and we will show the SIC codes here.', 'ok'),
        T('1st choice company name', '', { req: true, tip: 'Tip: Include the suffix at the end, e.g. "Bright Care Ltd" or "Bright Care Limited". The name must not be identical to any existing UK company.' }),
        T('2nd choice company name (backup if 1st is taken)', '', { tip: 'Optional, but it saves time if your first choice is taken.' }), T('3rd choice company name (final fallback)', ''),
        T('Trading name preference (if different from company name)', '', { tip: 'Tip: Leave blank if you want to trade under your company name.' })] });
      S.push({ id: 'setup2', title: 'Company Basics and Director 1 (Lead Director)', intro: 'The details Companies House needs.', fields: [
        C('Type of company', 'coType', [['ltd', 'Private limited company by shares (Ltd)'], ['guar', 'Private limited company by guarantee'], ['llp', 'Limited Liability Partnership (LLP)'], ['oth', 'Other (we will contact you to discuss)']], { tip: 'Tip: Most UK care providers choose Private limited company by shares (Ltd). This is the default if you are unsure.' }),
        T('Registered office address', '', { req: true, tip: 'Tip: This is the official Companies House address. Letters from Companies House and HMRC go here. Include the full postal address with postcode.' }),
        T('Director 1: Full legal name', '', { req: true, tip: 'Tip: Use the name exactly as on your passport or driving licence.' }), T('Director 1: Date of birth (dd/mm/yyyy)', '', { req: true }),
        T('Director 1: Nationality', '', { req: true }), T('Director 1: Country of residence', '', { req: true }),
        T('Director 1: Service address', '', { req: true, tip: 'Tip: The address Companies House will use for director-specific post. You can write "same as registered office" if you want to use the company address.' }),
        T('Director 1: Occupation', '', { req: true }),
        T('Director 1: Companies House Identity Verification Code', '', { tip: 'Not done yet? Carry on with the form. Every director must verify their identity on GOV.UK before a new company can be registered. It is done online with photo ID, and you get a code at the end. We send you the steps, and can do it with you on a call. We need the code before we register your company, not before you finish this form.' }),
        P('Additional director details', '', { tip: 'Their name and date of birth are copied to the Directors page for you. For each additional director, give: full legal name, date of birth, nationality, country of residence, service address, occupation and their own Companies House Identity Verification Code. Leave blank if there is only one director.' })] });
      S.push({ id: 'setup3', title: 'Owners, Shares and Authorisation', intro: 'Persons with significant control, share structure, communications and authorisation.', fields: [
        C('Are the directors also the persons with significant control of this company?', 'psc', [['y', 'Yes, the directors are the PSCs'], ['n', 'No, the PSCs are different people']], { tip: 'Tip: A Person with Significant Control (PSC) is anyone who owns more than 25% of shares or voting rights, or has the right to appoint or remove directors. For most small care companies, the director is also the PSC.' })]
        .concat(A.psc === 'n' ? [P('PSC details (only if different from directors)', '', { tip: 'For each PSC who is not a director: full name, date of birth, nationality, country of residence, service address, percentage of voting shares.' })] : [])
        .concat([T('Number of shares to issue', '1', { req: true, tip: 'Tip: Default is 1. If you have multiple owners, you can issue 100 shares to split percentages (e.g. 60/40, 50/50).' }), T('Value per share', '£1', { req: true, tip: 'Tip: Default is £1. Keep it simple.' }),
          C('Will a single owner hold 100% of shares?', 'single', [['y', 'Yes, single owner with 100%'], ['n', 'No, multiple owners']])])
        .concat(A.single === 'n' ? [P('Share split (only if multiple owners)', '', { tip: 'List each owner with their percentage, e.g. "Jane Smith 60 percent, John Doe 40 percent".' })] : [])
        .concat([T('Email address for Companies House notices', '', { req: true, tip: 'Tip: Use an email you check regularly.' }), T('Mobile number for the lead director', '', { req: true, tip: 'Tip: Used for verification and two-factor authentication on the Companies House WebFiling service.' }),
          M('Authorisation to incorporate on your behalf', 'auth', ['I authorise Care Sync Experts to incorporate this company on my behalf and act as my filing agent with Companies House.'], { req: true }),
          M('Confirmation of accuracy', 'conf', ['I confirm the names, addresses, dates of birth and other personal information given above are accurate. I understand that giving false information to Companies House is a criminal offence.'], { req: true })]) });
    }
    const d1 = A.formed === 'yes' ? ['Amara Okafor', '14/03/1986', '07700 900456', 'amara@harbourlanecare.co.uk'] : ['', '', '', ''];
    const dirs = [I('We need these details for every director of the company. Add each director in turn.'),
      T('Director 1: Full name', d1[0], { req: true, tip: 'As shown on their passport or driving licence.', ok: A.formed === 'yes' ? 'From Companies House' : 'Filled in from your lead director' }), T('Director 1: Date of birth', d1[1], { req: true }),
      T('Director 1: Mobile number', d1[2], { req: true }), T('Director 1: Email address', d1[3], { req: true }), C('Is there another director?', 'd2', yn)];
    if (A.d2 === 'y') dirs.push(T('Director 2: Full name', A.formed === 'yes' ? 'Peter Okafor' : '', { req: true }), T('Director 2: Date of birth', A.formed === 'yes' ? '02/11/1983' : '', { req: true }), T('Director 2: Mobile number', '', { req: true }), T('Director 2: Email address', '', { req: true }), C('Is there another director?', 'd3', yn));
    if (A.d2 === 'y' && A.d3 === 'y') dirs.push(T('Director 3: Full name', '', { req: true }), T('Director 3: Date of birth', '', { req: true }), T('Director 3: Mobile number', '', { req: true }), T('Director 3: Email address', '', { req: true }), C('Is there another director?', 'd4', yn));
    if (A.d2 === 'y' && A.d3 === 'y' && A.d4 === 'y') dirs.push(T('Director 4: Full name', '', { req: true }), T('Director 4: Date of birth', '', { req: true }), T('Director 4: Mobile number', '', { req: true }), T('Director 4: Email address', '', { req: true }), P('More than four directors?', '', { tip: 'For each other director, give their full name, date of birth, mobile number and email address.' }));
    S.push({ id: 'dirs', title: 'Directors', intro: 'Every director of the company.', fields: dirs });
    S.push({ id: 'svc', title: 'Primary Service Type and CQC Service User Bands', intro: 'What you will provide, and who you will support.', fields: [
      M('Which CQC-regulated activities will you provide? (Select all that apply)', 'acts', ['Personal Care (Domiciliary Care)', 'Personal Care (Supported Living)', 'Personal Care and Nursing (Supported Living)', 'Accommodation for persons who require nursing or personal care', 'Other']),
      M('CQC Service User Bands (who you will support)', 'bands', ['Adults aged 18 to 65', 'Adults aged 65+', 'Physical disability', 'Dementia', 'Mental health', 'Sensory impairment', 'People detained under the Mental Health Act', 'People who misuse drugs or alcohol', 'People with an eating disorder', 'Learning disabilities and or autistic people', 'Children and young people aged 0 to 18', 'The whole population', 'Other'], { tip: 'Select all the service user bands you intend to support at this location. Tick all that apply.' })] });
    const sl = (A.acts || []).includes(1) || (A.acts || []).includes(2) || (A.svcType || []).includes(1);
    if (sl) {
      const pf = [I('Added by the Hub. You chose supported living, so CQC will look closely at the homes people live in and how their housing and care are kept separate. People should be able to change their care provider without losing their home.'),
        C('Do you have the properties yet?', 'slHave', [['y', 'Yes'], ['some', 'Some of them'], ['n', 'Not yet']])];
      if (A.slHave === 'n') pf.push(I('That is fine. We plan the properties with you and add them before your application goes in.', 'ok'));
      else pf.push(T('How many properties?', '2'),
        T('Property 1: address', '14 Example Road, Stevenage SG1 4AA', { req: true, ok: 'Found by postcode' }), T('Property 1: how many people will live there?', '3'),
        T('Property 1: landlord or housing provider', 'Example Housing Association', { req: true }),
        C('Is the landlord connected to you or your company (for example you, a director or a family member own it)?', 'slLinked', [['n', 'No'], ['y', 'Yes'], ['ns', 'Not sure']], { tip: 'This is allowed in some cases, but CQC will ask how people keep their home if they change care provider. We help you explain it.' }),
        C('What kind of tenancy will people have?', 'slTen', [['own', 'Their own tenancy with the landlord'], ['joint', 'A joint tenancy'], ['lic', 'A licence'], ['ns', 'Not sure yet']]),
        C('Will the care agreement be separate from the tenancy?', 'slSep', [['y', 'Yes, separate'], ['n', 'No, they are together'], ['ns', 'Not sure']]),
        I('Another property? Add it here. Each one gets the same questions.', 'ok'));
      if (A.slLinked === 'y' || A.slSep === 'n') pf.push(I('CQC will want to see that housing and care are separate, so people are not tied to your care to keep their home. Your consultant will go through this with you before anything is sent.', 'warn'));
      S.push({ id: 'slprop', title: 'Supported Living: Your Properties', intro: 'Added by the Hub. Only for supported living.', fields: pf });
    } else skipped.push('Supported Living: Your Properties');
    S.push({ id: 'rm', title: 'Registered Manager Details', intro: '(The person who will be in day-to-day charge of regulated activities)', fields: [
      I('The Registered Manager is the person who runs the care every day. In a small new company this is often you. Later we ask who answers to CQC for the company, and if it is the same person, you will not type anything twice.'),
      C('What is your title?', 'title', [['Mr', 'Mr'], ['Mrs', 'Mrs'], ['Miss', 'Miss'], ['Ms', 'Ms'], ['Mx', 'Mx'], ['Dr', 'Dr']]),
      T('Registered Manager: Full Name', 'Ruth Anne Bennett', { req: true }), T('Registered Manager: Date of Birth', '09/07/1979', { req: true, ok: 'Checked: a real date' }),
      T('Registered Manager: Email Address', 'ruth@harbourlanecare.co.uk', { req: true }), T('Registered Manager: Mobile Number', '07700 900123', { req: true }),
      T('Registered Manager: Current Address', '22 Willow Court, Stevenage SG2 7AB', { req: true, ok: 'Found by postcode' }),
      C('Is the Registered Manager currently registered with a health or social care professional body?', 'rmProf', yn, { tip: 'Tip: Select Yes only if the Registered Manager holds a current registration with a health or social care professional body. If Yes, you will be asked to select the body and enter the registration number exactly as it appears on the public register.' }),
      F('Registered Manager CV', 'CV received', { tip: 'A full, up-to-date CV: full employment history, start and end dates for each role, no gaps in employment (explain if any), relevant qualifications and training.' })] });
    if (A.rmProf === 'y') S.push({ id: 'rmreg', title: 'Registered Manager Professional Registration', intro: 'Complete this section only when the Registered Manager holds a current registration with a health or social care professional body.', fields: [
      C('Registered Manager: Professional body', 'rmBody', bodies), T('Registered Manager: Professional registration number', '79A1234E', { req: true, tip: 'Tip: Enter the registration number exactly as it appears on the professional body public register.', ok: 'We check it on the public register' })] });
    else skipped.push('Registered Manager Professional Registration');
    S.push({ id: 'gp', title: 'GP Details', intro: "Only about your Registered Manager. CQC may need to contact the Registered Manager's doctor about their application.", fields: [
      T("GP's name", 'Dr A Shah', { req: true }), T('Surgery (Practice name)', 'Orchard Medical Practice', { req: true, ok: 'Searching the surgery filled in the address' }), T('Surgery address line 1', '5 Orchard Grove', { req: true }),
      T('Surgery address line 2', 'Bedwell', { req: true }), T('GP Surgery Town/city', 'Stevenage', { req: true }), T('County', 'Hertfordshire'), T('Postcode', 'SG1 3AB', { req: true }),
      C('Do you give permission for CQC to contact your doctor or their surgery?', 'gpOk', yn)] });
    S.push({ id: 'ref', title: 'Reference Details', intro: "Only about your Registered Manager. CQC may need to contact a referee about the Registered Manager's application.", fields: [
      I("IMPORTANT: The referee must be the Registered Manager's last employer. If there is no last employer, the referee:\n- Must NOT be related to the applicant\n- Must be able to provide a reference as to their competence to manage the service\n- Must have employed or worked with them for at least three months", 'warn'),
      I('Worried about asking your current employer? Many people are, especially when starting their own company. Talk to Grace first: we help you choose the right referee and the right time to ask, before anything goes to CQC.', 'ok'),
      T("Referee's title", '', { req: true }), T("Referee's first name", '', { req: true }), T("Referee's last name", '', { req: true }), T("Referee's address line 1", '', { req: true }),
      T("Referee's address line 2", '', { req: true }), T('Referee Town/city', '', { req: true }), T('Postcode', '', { req: true }), T("Referee's email address", '', { req: true }),
      T("Referee's telephone number", '', { req: true }), C('Do you give permission for CQC to contact your referee?', 'refOk', yn)] });
    const confirm = [C('Will the same person serve as both your Registered Manager AND Nominated Individual?', 'same', [['yes', 'Yes, the same person serves as both'], ['no', 'No, different people']], { tip: 'The Nominated Individual is the person who answers to CQC for the company. The Registered Manager runs the care every day. CQC allows the same person to hold both roles in smaller providers. If you are a sole director and the only senior person in the company, it is normally the same person. If you have a separate operations lead and a separate clinical or care lead, they are usually different people.' })];
    if (A.same === 'yes') confirm.push(I("We will use the Registered Manager's details for the Nominated Individual. You do not need to enter anything twice.", 'ok'));
    S.push({ id: 'confirm', title: 'Registered Manager and Nominated Individual Confirmation', intro: 'Almost done with the people section. One quick question to make sure we do not ask you for the same information twice.', fields: confirm });
    if (A.same === 'no') {
      S.push({ id: 'ni', title: 'Nominated Individual Details', intro: '(The senior person representing the organisation to CQC)', fields: [
        T('Nominated Individual: Full Name', 'Amara Okafor', { req: true, ok: 'Filled in from your directors' }), T('Nominated Individual: Date of Birth', '14/03/1986', { req: true }),
        T('Nominated Individual: Email Address', 'amara@harbourlanecare.co.uk', { req: true }), T('Nominated Individual: Mobile Number', '07700 900456', { req: true }),
        T('Nominated Individual: Current Address', 'Flat 3, 14 Orchard Way, Stevenage SG1 2AB', { req: true }),
        C('Is the Nominated Individual currently registered with a health or social care professional body?', 'niProf', yn, { tip: 'Tip: Select Yes only if the Nominated Individual holds a current registration with a health or social care professional body.' }),
        F('Nominated Individual CV', 'Add file', { tip: 'A full, up-to-date CV: full employment history, start and end dates for each role, no gaps in employment (explain if any), relevant qualifications and training.' })] });
      if (A.niProf === 'y') S.push({ id: 'nireg', title: 'Nominated Individual Professional Registration', intro: 'Complete this section only when the Nominated Individual is a different person from the Registered Manager and holds a current registration with a health or social care professional body.', fields: [
        C('Nominated Individual: Professional body', 'niBody', bodies, { tip: 'Tip: Select the professional body from the list. If it is not listed, choose Other UK or overseas health or social care professional body.' }), T('Nominated Individual: Professional registration number', '', { req: true })] });
      else skipped.push('Nominated Individual Professional Registration');
      S.push({ id: 'nidbs', title: 'DBS Check for Nominated Individual', intro: 'Now tell us about the DBS check for your Nominated Individual.', fields: [
        C('Have you already completed an Enhanced DBS check for the Nominated Individual with the Adult Workforce barred list and a countersignature?', 'niDbs', [['y', 'Yes, the DBS check has already been completed'], ['n', 'No, the DBS check has not yet been done (Care Sync will help with the application)']], { tip: 'Tip: Same DBS requirements as the Registered Manager. Enhanced check, Adult Workforce barred list, countersigned, within the last 12 months.' })] });
      if (A.niDbs === 'y') { skipped.push('Nominated Individual: DBS application details');
        S.push({ id: 'nicert', title: 'Nominated Individual DBS Certificate Details', intro: 'Please give us the DBS certificate details for your Nominated Individual.', fields: [
          T('Nominated Individual: DBS Certificate Number', '', { req: true, tip: 'Tip: The 12-digit number printed on the DBS certificate.' }), T('Nominated Individual: DBS Issue Date (dd/mm/yyyy)', '', { req: true, tip: 'Tip: The date the DBS certificate was issued. Must be within the last 12 months.' }),
          F('Nominated Individual: DBS Certificate Upload', 'Add file', { req: true }), I('Because the DBS is already done, you do not need to give ID documents or an address history for the Nominated Individual.', 'ok')] }); }
      else { skipped.push('Nominated Individual DBS Certificate Details');
        S.push({ id: 'niapp', title: 'Nominated Individual: DBS application details', intro: 'As the Nominated Individual does not have a DBS check yet, we need these details to apply for one.', fields: [
          M('Nominated Individual: select the three forms of identification you can provide', 'niIds', ids, { req: true, tip: 'Choose three, including at least one photo ID (passport, photocard licence or eVisa) and at least one showing your current address. We ask for a photo of each.' }),
          I('Nominated Individual: 5-year address history\nList every address for the past 5 years with no gaps: full address, postcode, and the month and year you moved in and out.'),
          T('Nominated Individual: Address 1 (current): full address, postcode, from MM/YYYY to present', '', { req: true }), T('Nominated Individual: Address 2: full address, postcode, from MM/YYYY to MM/YYYY'),
          T('Nominated Individual: Address 3: full address, postcode, from MM/YYYY to MM/YYYY'), T('Nominated Individual: Address 4: full address, postcode, from MM/YYYY to MM/YYYY'), T('Nominated Individual: Address 5: full address, postcode, from MM/YYYY to MM/YYYY'),
          I('More than five addresses? Add them here instead of emailing them. Gaps in the 5 years are spotted for you.', 'ok')] }); }
    } else { skipped.push('Nominated Individual Details', 'DBS Check for Nominated Individual', 'Nominated Individual DBS pages'); }
    S.push({ id: 'rmdbs', title: 'DBS Check for Registered Manager', intro: 'Tell us about the DBS check for your Registered Manager. If the same person also serves as your Nominated Individual, this is the DBS for that one person.', fields: [
      I('Not sure which DBS you have? If you had a DBS for a care job in the last 12 months, choose Yes and send a photo of it. Grace checks it is the right type, and tells you if a new one is needed.', 'ok'),
      C('Have you already completed an Enhanced DBS check for the Registered Manager with the Adult Workforce barred list and a countersignature?', 'rmDbs', [['y', 'Yes, the DBS check has already been completed'], ['n', 'No, the DBS check has not yet been done (Care Sync will help with the application)']], { tip: 'Tip: For CQC, your DBS must be an Enhanced check, must include the Adult Workforce barred list, must be countersigned by a CQC-registered countersignatory (not just an Update Service basic), and must be dated within the last 12 months. If yours is older than 12 months it will need to be redone before your application can go in.' })] });
    if (A.rmDbs === 'y') { skipped.push('Registered Manager: DBS application details');
      S.push({ id: 'rmcert', title: 'Registered Manager DBS Certificate Details', intro: 'Please give us the DBS certificate details for your Registered Manager (or the one person if same as your Nominated Individual).', fields: [
        T('Registered Manager: DBS Certificate Number', '001234567890', { req: true, tip: 'Tip: The 12-digit number printed on the DBS certificate.', ok: 'Checked: 12 digits' }),
        T('Registered Manager: DBS Issue Date (dd/mm/yyyy)', '14/02/2026', { req: true, tip: 'Tip: The date the DBS certificate was issued. Must be within the last 12 months.', ok: 'Checked: within the last 12 months' }),
        F('Registered Manager: DBS Certificate Upload', 'Photo received', { req: true }),
        I('Because the DBS is already done, you do not need to give ID documents or a 5-year address history. If the issue date were more than 12 months ago, we would tell you here and ask for the application details instead.', 'ok')] }); }
    else { skipped.push('Registered Manager DBS Certificate Details');
      S.push({ id: 'rmapp', title: 'Registered Manager: DBS application details', intro: 'As the Registered Manager does not have a DBS check yet, we need these details to apply for one.', fields: [
        M('Registered Manager: select the three forms of identification you can provide', 'rmIds', ids, { req: true, tip: 'Choose three, including at least one photo ID (passport, photocard licence or eVisa) and at least one showing your current address. We ask for a photo of each.' }),
        I('Registered Manager: 5-year address history\nWe require a complete 5-year address history for DBS purposes. Please list ALL addresses for the past 5 years with no gaps: full address, postcode, from (MM/YYYY), to.'),
        T('Registered Manager: Address 1 (Current) Full Address | Postcode | From MM/YYYY | To Present', '22 Willow Court, Stevenage SG2 7AB | 10/2022 | Present', { req: true }),
        T('Registered Manager: Address 2 (Full Address | Postcode | From MM/YYYY | To MM/YYYY)'), T('Registered Manager: Address 3 (Full Address | Postcode | From MM/YYYY | To MM/YYYY)'),
        T('Registered Manager: Address 4 (Full Address | Postcode | From MM/YYYY | To MM/YYYY)'), T('Registered Manager: Address 5 (Full Address | Postcode | From MM/YYYY | To MM/YYYY)'),
        F('If you have lived at more than 5 addresses in the past 5 years, please attach a separate sheet with complete address history', 'Add file, or add more addresses above')] }); }
    S.push({ id: 'decl', title: 'Declaration', intro: 'Last of all.', fields: [
      I('I confirm that the information provided is accurate and complete. I understand that failure to submit accurate details or missing documents will delay the CQC application and DBS submission process.'),
      T('Signatory: Full Name', 'Amara Okafor'), T('Position in Organisation:', 'Director'), SG('Signature:', 'Amara Okafor'), T('Date:', '21/10/2026')] });
'''.replace('__BODIES__',BODIES).replace('__IDS__',IDS)
INIT = "{ slHave: 'y', slLinked: 'n', slTen: 'own', slSep: 'y', formed: 'yes', d2: 'y', d3: 'n', svcType: [0], coType: 'ltd', psc: 'y', single: 'y', auth: [0], conf: [0], acts: [0], bands: [0, 1, 2, 3], title: 'Ms', rmProf: 'y', rmBody: 'b0', gpOk: 'y', same: 'yes', niProf: 'n', niDbs: 'n', rmDbs: 'y', niIds: [], rmIds: [0, 1, 4] }"
build(sys.argv[1], 'CQC Registration Information Form', 'CQC Registration Information Form', 'Amara', 1800, JS, INIT, 'ref',
      'Grace checks it now. As soon as it passes, your project starts and Daniel begins your CQC pack. A copy of your answers comes to you by email.')
