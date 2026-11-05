# Builds SP/superadmin/registry.json from inventory.json + decisions.md (encoded below).
# One entry per rule, ids kept. Run: python3 registry_build.py
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sa_common import SP, BOARDS, bref, EMAILS, eref, SCOPES

INV = json.load(open(SP + '/superadmin/inventory.json'))
PROJ = SP + '/hub-canvas/project/'
GOLIVE = 'Thu 1 Oct 2026'
DEC_DATE = 'Wed 4 Nov 2026'

OWNER = {'Promises and timings': 'Collins', 'Journey and gates': 'Rachel Turner', 'Sessions and coaching': 'Rachel Turner', 'Regulators': 'Collins',
 'Tenders': 'Collins', 'Money': 'Collins, with Femi Ade (finance)', 'People and access': 'Rachel Turner', 'Security': 'Collins (data protection lead)',
 'Data and privacy': 'Collins (data protection lead)', 'Messages and notifications': 'Rachel Turner', 'Forms and templates': 'Grace drafts, Rachel Turner owns',
 'Branding and wording': 'Collins', 'Integrations': 'Rachel Turner', 'Aftercare and growth': 'Collins', 'Reviews and feedback': 'Collins'}
AREA_SCOPE = {'Promises and timings': 'all', 'Journey and gates': 'active', 'Sessions and coaching': 'sess', 'Regulators': 'pre', 'Tenders': 'tender',
 'Money': 'all', 'People and access': 'staff', 'Security': 'all', 'Data and privacy': 'all', 'Messages and notifications': 'all',
 'Forms and templates': 'onb', 'Branding and wording': 'all', 'Integrations': 'all', 'Aftercare and growth': 'after', 'Reviews and feedback': 'active'}
SCOPES = dict(SCOPES)
SCOPES['overdue'] = (4, 'clients with an overdue invoice (4 invoices, £5,300)')

OTHER, SA, MGR, LOCK = 'other super admin', 'super admin', 'manager', 'locked'
NEW, DATE = 'new clients only', 'everyone from a date'
PROMISE_REVIEW = 'Protected promise: every registered client is invited to review, once'
PROMISE_TIME = 'Protected promise: no promises about how long a regulator takes'
PROT = 'Protected by Care Sync: part of how the Hub keeps its promises'

# id: dict(v=value, u=unit, old=v1 value if decisions.md changed it, dec=True if decisions.md settles it,
#          ap=approval, ef=effective, sc=scope, src=source for locked/legal, csr=registry.js key, note=extra note, name=title)
R = {}
def D(i, v, u='', **k):
    k['v'] = v; k['u'] = u; R[i] = k

# Promises and timings
D('client-question-reply-time', '1 working day', 'working days', dec=1, ap=OTHER, csr='reply-client', name='Reply promise: client questions')
D('question-escalation-team-lead', '6 working hours', 'working hours', ap=SA, name='Unanswered question goes to the team lead')
D('unanswered-message-red', '1 working day', 'working days', dec=1, ap=SA, csr='unanswered-red', name='Unanswered message turns red')
D('senior-question-reply-time', '2 working hours', 'working hours', dec=1, old='2 hours', ap=OTHER, csr='reply-senior', name='Reply promise: senior questions')
D('introduction-call-target', 'Within 2 working hours of payment (paid late in the day: by 10:00 the next working morning)', 'working hours', ap=OTHER, sc='onb', csr='intro-call')
D('working-hours', '09:00 to 17:30, Monday to Friday, excluding bank holidays of the client\'s nation (England and Wales, or Northern Ireland)', 'hours', dec=1, old='Not stated', ap=OTHER, csr='working-hours')
D('enquiry-reply-time', '15 minutes in staffed hours', 'minutes', ap=SA, sc='prospect')
D('regulator-news-same-day', 'Same day for the client, same hour for staff', 'time', ap=OTHER, sc='reglr', name='Regulator news passed on')
D('promise-at-risk-warning', 'Warned before the promised date is missed', 'rule', ap=SA, name='Promise at risk warning')
D('no-regulator-dates-promised', 'No date is promised for a regulator, buyer or decision', 'rule', dec=1, ap=LOCK, src=PROMISE_TIME)
D('target-dates-checked-weekly', 'Every week, on the weekly update day (Friday)', 'day of the week', ap=SA, sc='active')
D('submit-after-final-signature', '2 working days', 'working days', dec=1, ap=OTHER, sc='build', csr='send-after-signing', name='Send to the regulator after the final signature')
D('consultant-change-notice', 'The client is told the same day (email 9.3)', 'time', ap=OTHER, sc='sam')
D('growth-plan-call', '5 working days', 'working days', ap=SA, sc='after')
D('morning-brief', '08:00 every working day', 'time', ap=SA, sc='staff')
# Journey and gates
D('onboarding-gates-list', '8 gates: Company and directors, Identity, Office address evidence, Registered manager, Employment history, References, DBS, Professional registers. Form complete is a precondition, not a gate', 'list', dec=1, old='8 gates, with "form complete" counted as a gate on some boards', ap=OTHER, sc='onb')
D('no-work-before-handover', 'No application work, kick-off or sessions until every gate passes and a manager approves the handover', 'rule', dec=1, old='Kick-off booked at welcome on some boards', ap=SA, sc='onb')
D('handover-approver', 'A manager (directors count as managers)', 'role', dec=1, old='Collins (director)', ap=SA, sc='onb')
D('unowned-client-red', 'Always red', 'rule', ap=LOCK)
D('stage-model', '11 stages; the staff sub-steps are statuses inside them', 'stages', dec=1, old='11 client stages and 13 staff stages', ap=OTHER, sc='reg')
D('stage-evidence-required', 'Evidence is required to close a stage', 'rule', ap=LOCK)
D('returned-application-recovery', 'Resubmit within 2 working days of a returned application', 'working days', ap=SA, sc='reglr')
D('critical-risk-alerts', 'Case owner and manager first; a director for legal deadlines', 'route', dec=1, old='Case owner and manager, or a director (boards differed)', ap=SA)
D('closure-and-archive', 'A manager approves closure; history kept for ever', 'rule', ap=SA)
D('interview-pass-not-completion', 'A passed interview is not registration: the client is told the same day what comes next', 'rule', ap=LOCK)
D('gate-failure-alerts-once', 'Once per failure', 'count', ap=SA, sc='onb')
D('fix-list-rules', 'Sent only when staff press Send', 'rule', ap=SA, sc='onb')
D('office-evidence-rules', 'Commercial lease; mortgaged home with lender permission and title; rented home with tenancy and landlord permission; owned with title. Virtual offices are not accepted', 'list', ap=SA, sc='onb')
D('address-match-strictness', 'Same building, different unit counts as a mismatch', 'rule', ap=SA, sc='onb')
D('pack-doctor-rules', '9 core documents, 3 supporting and 2 for the manager; a 12-month forecast month by month; links opened on submission day', 'list', ap=SA, sc='build')
D('quality-gate-second-person', 'A second person checks every pack, always. It cannot be relaxed', 'rule', dec=1, old='Relaxable per staff member on one board', ap=LOCK, sc='build', src='Protected rule, decided 4 November: absolute, cannot be relaxed')
D('signing-together', 'Every signer signs; a one-time code for the final pack', 'rule', ap=SA, sc='build')
D('regulator-submission-with-client', 'Submitted on a call with the client', 'rule', ap=LOCK, sc='build')
D('stage-waiting-colours', '"Waiting on" turns amber after 5 days and red after 10', 'days', dec=1, old='Stage target times not set', ap=SA, csr='waiting-amber-days')
D('gone-quiet', '10 days without a reply', 'days', ap=SA)
D('no-outbound-contact-red', '7 days', 'days', dec=1, ap=SA, csr='no-contact-red-days')
D('regulator-watch-cadence', 'CQC email every few minutes; CIW Online and the RQIA Web Portal every working day', 'frequency', dec=1, old='Manual check on Monday and Thursday on some boards', ap=SA, sc='reglr')
D('watch-gap-red', '7 days', 'days', dec=1, ap=SA, sc='reglr', csr='watch-gap-red-days')
# Sessions and coaching
D('sessions-included', '3 sessions: kick-off, documents, interview practice. Millicent runs them; the case owner joins session 2', 'sessions', ap=OTHER, ef=NEW, csr='sessions-included')
D('session-unlock-rules', 'Booked after handover approval; session 3 opens when the interview date is set', 'rule', dec=1, ap=SA)
D('session-reminders', 'On booking, 1 day before and 1 hour before', 'schedule', ap=SA)
D('session-length', '1 hour', 'hours', ap=SA, csr='session-length')
D('extra-sessions', 'Price to set; agreed and priced before any extra session', 'price', dec=1, ap=OTHER, ef=NEW)
D('callbacks-and-sessions', 'Callbacks are not counted as sessions', 'rule', ap=SA)
D('case-owner-joins-session-2', 'Session 2', 'session', ap=SA)
D('session-notes-visibility', 'The summary is visible to the client; private notes stay hidden', 'rule', ap=SA)
D('interview-reminders', '7 days before, 1 day before and the morning of', 'schedule', ap=SA, sc='interview')
D('interview-hub-account', 'Created when the interview stage starts', 'rule', ap=SA, sc='interview')
D('resubmission-interview-practice', 'An extra practice session, no charge to the client', 'rule', ap=OTHER, sc='refused')
# Regulators
D('nop-representation-deadline', '28 days from service, worked out the safe way: the day of service is day 1. Confirm with a legal adviser', 'days', dec=1, old='28 days, counted from the day after service on some boards', ap=LOCK, sc='nop', csr='nop-legal-days', legal=1,
  src='Law: Health and Social Care Act 2008 (written representations within 28 days of a notice of proposal). CIW and RQIA: as set out in the notice', name='Notice of Proposal: legal deadline')
D('nop-internal-targets', 'Draft by day 14, senior review and client approval by day 20, send by day 21 (a week before the legal deadline)', 'days', dec=1, old='Draft by day 14, client review by day 21, send by day 25', ap=SA, sc='nop', csr='nop-send-day', name='Notice of Proposal: our targets')
D('nop-alert-schedule', 'Day 7, 14, 21 and 25, then every day', 'schedule', dec=1, old='Day 7, 14, 21 and 25, and every day in the final 3 days', ap=SA, sc='nop', name='Notice of Proposal: alerts')
D('appeal-deadline', '28 days from the notice of decision, worked out the safe way (day of service is day 1). Confirm with a legal adviser', 'days', dec=1, old='28 days; Westbrook window shown as closing Mon 23 Nov', ap=LOCK, sc='refused', legal=1,
  src='Law: Health and Social Care Act 2008 (appeal to the First-tier Tribunal within 28 days). CIW and RQIA: as set out in the decision')
D('legal-alerts-always-on', 'Always on; nobody can switch them off', 'rule', ap=LOCK, sc='legal', src='Protected by Care Sync: legal deadlines are never missed silently')
D('resubmission-promise', 'Resubmission is included in the package, at no charge to the client', 'rule', ap=OTHER, ef=NEW, sc='reg')
D('resubmission-gate', '7 items checked before a resubmission is sent', 'count', dec=1, old='6 items', ap=SA, sc='refused')
D('resubmission-refresh-ages', 'At the resubmit date: DBS under 12 months and references under 6 months (our rules); insurance in date', 'months', dec=1, old='DBS within 12 months; references confirmed again', ap=SA, sc='refused')
D('refusal-same-day-actions', 'Same day', 'time', ap=SA, sc='refused')
D('refusal-kind-check-in', 'A week after the decision', 'days', ap=SA, sc='refused')
D('resubmission-target', 'About 5 weeks after the decision, set by the manager for each client', 'weeks', ap=MGR, sc='refused')
D('withdraw-before-notice', 'A client can withdraw only before a notice is served', 'rule', ap=LOCK, legal=1, src='Regulator process: withdrawal is possible before a notice of proposal is served (we check each case)')
D('rfi-reply-targets', 'Our target: 4 working days before the regulator\'s date', 'working days', dec=1, old='6 working days before CQC\'s date, or 2 days after receipt', ap=SA, sc='reglr', csr='rfi-target-days-before', name='Request for information: our target')
D('dbs-age-rules', 'CQC: issued within 12 months; CIW: a warning at 3 months', 'months', ap=LOCK, legal=1, src='Regulator guidance (CQC, CIW). We check the current version')
D('identity-documents', '3 documents: one photo ID and one showing the current address (RQIA: check)', 'count', dec=1, ap=LOCK, legal=1, src='Regulator guidance, as the forms ask (RQIA: check)')
D('brp-expiry-allowance', 'May still be accepted up to 18 months after expiry: check current Home Office guidance', 'months', ap=LOCK, legal=1, src='Home Office right to work guidance (check)')
D('proof-of-address-age', 'Utility bill or bank statement: 3 months; council tax statement: 12 months', 'months', ap=SA)
D('address-history-length', '5 years (CIW: check, open question 47)', 'years', dec=1, ap=LOCK, legal=1, src='Regulator guidance (CIW: check, open question 47)')
D('cv-gap-rules', 'Any gap longer than 4 weeks needs a line of explanation', 'weeks', dec=1, old='Every gap (spec) or more than 3 months (a form question)', ap=LOCK, legal=1, csr='cv-gap-weeks',
  src='Regulator requirement: a full employment history with gaps explained. Our threshold, decided 4 November: 4 weeks')
D('referee-rules', 'CQC: the last employer in care; CIW: employed at least 3 months, not a relative; RQIA: two written references, including the most recent employer', 'list', ap=LOCK, legal=1, src='Regulator guidance (CQC, CIW, RQIA)')
D('format-checks', 'DBS number 12 digits; Companies House identity code 11 characters; UK dates, no impossible future dates', 'format', ap=LOCK, legal=1, src='Format set by DBS and Companies House')
D('psc-threshold', 'More than 25%', '%', ap=LOCK, legal=1, src='Law: Companies Act 2006 (people with significant control)')
D('ciw-start-date', 'At least 14 weeks ahead', 'weeks', ap=LOCK, legal=1, sc='ciw', src='CIW guidance (check)')
D('ciw-post-registration-duties', 'Responsible Individual visit every 3 months; quality of care review every 6 months; annual return', 'schedule', ap=LOCK, legal=1, sc='ciwafter', src='Law: Regulation and Inspection of Social Care (Wales) Act 2016 and its regulations')
D('rqia-post-registration-duties', 'Monthly monitoring', 'schedule', ap=LOCK, legal=1, sc='rqiaafter', src='RQIA Minimum Standards (check)')
D('regulator-fixed-facts', 'RQIA PIN 497850; CIW: 7 Regional Partnership Boards; RQIA: 5 HSC Trusts; managers registered with Social Care Wales or NISCC', 'list', ap=LOCK, legal=1, src='Set by CIW and RQIA')
# Tenders
D('tender-submit-margin', '2 working days before the buyer\'s deadline', 'working days', dec=1, old='1 working day before (a spare day)', ap=SA, csr='tender-submit-days-before', name='Tender: when we submit')
D('tender-timeline', 'Draft to the client 10 working days before the deadline, client approval 5 working days before, submit 2 working days before', 'working days', dec=1, old='Draft 7 working days before, approval 4 working days before', ap=SA, csr='tender-draft-days-before', name='Tender: back-scheduled timeline')
D('tender-tight-deadline-flag', '15 working days', 'working days', ap=SA)
D('tender-earlier-deadline-wins', 'The earlier time wins', 'rule', ap=LOCK)
D('bid-no-bid-approval', 'The client decides whether to bid; a director accepts the bid work when there is a capacity or same-lot question', 'route', dec=1, old='Collins approves bid or no bid', ap=SA)
D('case-owner-approval-before-outreach', 'The case owner agrees first', 'rule', ap=LOCK)
D('same-lot-conflict', 'The same lot is a conflict and is not offered', 'rule', ap=LOCK)
D('tps-ctps-screening', 'Numbers screened against TPS and CTPS within the last 28 days', 'days', ap=LOCK, legal=1, sc='prospect', src='Law: Privacy and Electronic Communications Regulations (TPS and CTPS)')
D('lot-decision-checks', '4 checks; 2 fails usually means no', 'count', ap=SA)
D('tender-eligibility', 'Set by each buyer', 'rule', ap=LOCK, src='Each buyer\'s tender pack')
D('lawful-wage-check', 'National Living Wage £12.71 an hour from 1 April 2026, aged 21 and over (check each April)', '£ an hour', ap=LOCK, legal=1, src='Law: National Minimum Wage rates (check each April)')
D('tender-insurance-minimums', '£5 million employer\'s liability by law; buyers may ask for more', '£', ap=LOCK, legal=1, src='Law: Employers\' Liability (Compulsory Insurance) Act 1969')
D('tender-document-expiry-warning', '6 weeks before expiry', 'weeks', dec=1, old='A month before', ap=SA, csr='expiry-warning-weeks', name='Document expiry warning')
D('contract-renewal-watch', 'About 6 months before the contract ends', 'months', ap=SA)
D('tender-profile-freshness', 'Sections older than 3 months are flagged; policies reviewed in the last 12 months', 'months', ap=SA, note='decisions.md is silent. Boards flag 5 months and not 2, so 3 months is set here, to confirm.')
D('tender-weekly-client-email', 'Monday mornings', 'day of the week', ap=SA)
D('tender-client-approval', '4 ticks before we submit', 'count', ap=LOCK)
D('tender-submission-evidence', 'Receipt saved the same day', 'rule', ap=LOCK)
D('tender-portal-access', 'Portal passwords are never asked for', 'rule', dec=1, old='Stored in the vault if unavoidable', ap=SA)
D('tender-outcome-follow-up', 'A reminder when the framework reopens', 'rule', ap=SA)
D('modern-slavery-threshold', '£36 million turnover', '£', ap=LOCK, legal=1, src='Law: Modern Slavery Act 2015, section 54')
# Money
P = dict(ap=OTHER, ef=NEW, sc='signed')
D('price-cqc-domiciliary', '£4,000 + VAT', '£', dec=1, csr='price-dom', name='Price: CQC registration, domiciliary care', **P)
D('price-cqc-supported-living', '£5,000 + VAT', '£', dec=1, csr='price-sl', name='Price: CQC registration, supported living', **P)
D('price-full-start-up', '£8,500 + VAT (still to check: £8,500 or £8,000)', '£', dec=1, old='No price set; each set-up quoted before work', csr='price-full', name='Price: Full start-up package',
  pending=dict(value='£8,500 + VAT', by='Collins', on='Mon 2 Nov', waiting='Rachel Turner', where='Price book (board 77)', file='PriceBook.dc.html'), **P)
D('price-ciw-rqia', '£4,500 + VAT', '£', dec=1, csr='price-ciw', name='Price: CIW and RQIA registration', **P)
D('price-sl-add-on', '£1,500 including VAT', '£', csr='price-sl-addon', name='Price: supported living add-on', **P)
D('price-interview-prep', '£750 including VAT', '£', csr='price-interview', name='Price: CQC interview preparation', **P)
D('price-pir', '£750 + VAT per PIR, one PIR per service type', '£', csr='price-pir', name='Price: PIR writing', pir=1, **P)
D('price-tender-writing', 'From £1,500 + VAT, quoted after review', '£', csr='price-tender-from', name='Price: tender writing', **P)
D('price-single-services', 'From £500 + VAT, 1 payment in full', '£', dec=1, name='Price: single services', **P)
D('price-bid-review', 'Around £500, VAT to confirm', '£', name='Price: bid review', **P)
D('pending-prices', '"Price to set": nobody quotes it', 'rule', dec=1, ap=OTHER, ef=NEW, sc='new')
D('price-change-approval', 'Anyone may suggest a price; a super admin enters it; the other super admin approves; new clients only', 'route', dec=1, old='The second super admin approves', ap=LOCK, sc='signed', src='Decided 4 November: dual control on prices')
D('discount-approval', 'A super admin who is not the requester, with a reason', 'route', dec=1, old='Collins approves', ap=LOCK, sc='new', src='Decided 4 November: dual control on discounts')
D('instalment-splits', 'Domiciliary care, supported living, CIW and RQIA: 2 x 50% (accept, sign and pay; submission). Full start-up: 3 x one third (accept, sign and pay; final pack sign-off; submission). Tender writing: 50% at signing, 50% before submission. Add-ons: 1 payment in full', 'split', dec=1, ap=OTHER, ef=NEW, sc='signed')
D('instalment-rounding', 'The last instalment takes the rounding', 'rule', ap=LOCK)
D('pay-after-sign', 'The client signs, then pays', 'rule', ap=LOCK)
D('payment-methods', 'Stripe (card and other Stripe methods); bank transfer only by agreement, marked paid by finance', 'list', dec=1, old='Stripe card; bank transfer marked paid by finance', ap=OTHER, csr='payment-provider')
D('payment-reminders', 'A week before; overdue bands 0 to 30, 31 to 60 and over 60 days; over 60 days: payment plan or pause work', 'schedule', ap=SA, sc='overdue')
D('refunds-credit-notes', 'A manager approves refunds and credit notes', 'route', ap=OTHER, sc='new')
D('extras-priced-first', 'Agreed and priced before any work', 'rule', ap=LOCK)
D('vat-treatment', '20%, stored as one setting; prices are + VAT unless the price book says including VAT', '%', dec=1, old='+ VAT, including VAT and "VAT to confirm" mixed', ap=OTHER, ef=DATE, csr='vat-rate', name='VAT rate')
D('accounting-sync', 'Xero, synced every hour', 'frequency', dec=1, ap=OTHER)
D('referral-thank-you', 'Value to set', '£', ap=OTHER, ef=NEW, sc='after')
D('out-of-package-promises', 'Flagged to a manager', 'rule', ap=LOCK)
# People and access
D('roles-and-permissions', 'Manager, consultant (case owner), onboarding lead, client care, coach, sales, finance, data protection lead (a manager). Super admin is a flag on top of a role', 'list', dec=1, old='10 roles, including weekly update owner and account owner as roles', ap=OTHER)
D('super-admin-holders', 'At least 2 named super admins: Collins (director) and Rachel Turner (operations manager)', 'people', dec=1, old='Collins and an unnamed manager', ap=LOCK, sc='staff', src='Protected rule: go-live needs two active, named super admins')
D('second-super-admin-approvals', 'Prices, discounts, permissions, super admin invites, form versions, template and email versions with legal wording, retention changes, early deletion, break-glass', 'list', dec=1, old='Prices, permissions, deletion, break-glass, form versions, super admin invites', ap=LOCK, sc='staff', src='Decided 4 November: dual control on from go-live')
D('cover-and-leave', 'Planned leave uses cover delegation: a manager approves cover for named clients and dates, including vault reveal for those clients, ending automatically', 'rule', dec=1, old='Cover sees pages, tasks and updates; vault needs break-glass', ap=OTHER)
D('leaver-offboarding', 'Access ends 17:30 on the last day; emails forwarded for 90 days; "Suspend now" when needed', 'rule', ap=OTHER)
D('staff-invites', 'An invite ends after 7 days', 'days', ap=OTHER)
D('client-account-people', 'Co-director: everything; manager: their own tasks; accountant: shared items only', 'rule', ap=LOCK, sc='all')
D('partner-access', 'Later phase', 'phase', ap=OTHER)
D('view-as', 'Read only, logged, and visible to the client', 'rule', ap=LOCK, sc='all')
D('workload-capacity', 'Shown as % of a normal week', 'rule', ap=SA)
# Security
D('staff-two-step-login', 'Compulsory for staff', 'rule', ap=LOCK, sc='staff')
D('client-two-step-login', 'Optional, recommended for directors', 'rule', ap=OTHER)
D('client-sign-in', 'Magic link, no password; a known device stays signed in 30 days. When Care Sync holds the login to the client\'s sign-in mailbox, a code to the client\'s mobile on new devices and before signing, approving, downloading everything or changing contact details', 'rule', dec=1, old='No password; phone signed in for 30 days', ap=OTHER, csr='client-device-days')
D('staff-session-timeout', '30 minutes idle', 'minutes', ap=OTHER, sc='staff', csr='staff-idle-timeout', note='The inventory found no value. 30 minutes is the registry.js default, to confirm on Security (board 84).')
D('break-glass', 'Emergencies only: approved by a super admin who is not the requester (or self-authorised with a written reason if none can be reached); 4 hours; both super admins and the client told the same day; reviewed within 1 working day', 'hours', dec=1, old='4 hours; client emailed the same day', ap=OTHER, csr='break-glass-hours')
D('vault-reveal', '30 seconds, with a reason for each reveal and copy', 'seconds', ap=OTHER)
D('logins-never-shared', 'Never shared', 'rule', ap=LOCK)
D('vault-hand-back', 'Handed back at the end of the engagement', 'rule', ap=LOCK)
D('client-mailbox-authority', 'Written authority; CQC, CIW, RQIA and tender portal emails only; never files Hub sign-in or e-signature emails', 'rule', dec=1, old='Written authority; CQC, CIW, RQIA and tender portal emails only', ap=LOCK)
D('audit-log', 'Every action, and it cannot be edited or deleted', 'rule', ap=LOCK, sc='staff')
D('unusual-activity-alerts', 'Usual is under 5 exports a day per person; more alerts both super admins', 'count', ap=OTHER, sc='staff')
D('super-admin-weekly-summary', 'Every Monday at 07:00', 'time', ap=SA, sc='staff')
D('link-expiry', 'One-task links last 14 days', 'days', ap=OTHER)
D('hosting-and-backups', 'UK only; nightly backup at 02:00; restore tested every 3 months', 'rule', ap=LOCK)
D('upload-limits', 'PDF, JPG or PNG, up to 20 MB', 'MB', ap=SA)
D('sensitive-fields-masked', 'Masked by default', 'rule', ap=LOCK)
# Data and privacy
D('id-dbs-retention', 'Identity and DBS images are deleted once the regulator has decided; the Hub keeps a record (seen by, date, document type, DBS number and issue date)', 'rule', dec=1, old='Kept until our work for the client ends (retention schedule v1)', ap=OTHER, sc='reg',
  pending=dict(value='Deleted once the regulator has decided', by='Collins (data protection lead)', on='Fri 30 Oct', waiting='Rachel Turner', where='Data and privacy (board 85)', file='DataPrivacy.dc.html'), name='Identity and DBS images: how long we keep them')
D('scheduled-deletion', 'Routine deletions inside the approved schedule run automatically after 7 days\' notice; a legal hold, open complaint, regulator query or payment dispute blocks them', 'days', dec=1, old='Deleted 7 days after one approval', ap=OTHER)
D('retention-per-document-type', 'Retention schedule v2: a period for each document type', 'schedule', dec=1, old='Retention schedule v1 (go-live)', ap=OTHER, sc='reg', name='Retention schedule',
  pending=dict(value='Retention schedule v2', by='Collins (data protection lead)', on='Fri 30 Oct', waiting='Rachel Turner', where='Data and privacy (board 85)', file='DataPrivacy.dc.html'))
D('voice-note-deletion', 'Deleted after transcription', 'rule', ap=LOCK)
D('data-protection-requests', 'One calendar month (can be extended in some cases)', 'months', ap=LOCK, legal=1, src='Law: UK GDPR, Article 12')
D('breach-reporting', '72 hours from awareness, if reportable', 'hours', ap=LOCK, legal=1, src='Law: UK GDPR, Article 33')
D('privacy-page-every-look', 'Every look by staff shows on the client\'s privacy page', 'rule', ap=LOCK)
D('consent-wordings', 'Approved wordings only; legal wording needs the other super admin', 'rule', ap=OTHER)
D('ico-registration', 'Number to add; the Security page claim stays hidden until it is entered', 'text', ap=OTHER, csr='ico-number', note='From ia.md go-live readiness: the ICO registration number is still open.')
D('marketing-consent-sole-traders', 'Consent required', 'rule', ap=LOCK, legal=1, sc='prospect', src='Law: Privacy and Electronic Communications Regulations')
# Messages and notifications
D('weekly-update-day', 'Friday, for every client', 'day of the week', dec=1, old='Friday on most boards; the owner\'s own day on some', ap=OTHER, sc='weekly', csr='weekly-update-day', name='Weekly update day')
D('weekly-update-rhythm', 'Monday review, Wednesday chase, Thursday second-person check, Friday send', 'schedule', dec=1, old='Monday review, Tuesday and Wednesday send, Thursday chase, Friday manager check', ap=MGR, sc='weekly', csr='weekly-rhythm')
D('weekly-update-opt-out', 'Always on; the client chooses the channel', 'rule', dec=1, old='The client could switch it off', ap=OTHER, sc='weekly')
D('weekly-update-send-time', 'By 16:00', 'time', dec=1, ap=OTHER, sc='weekly', csr='weekly-update-time')
D('weekly-update-template', '9 parts', 'count', ap=OTHER, sc='weekly')
D('notification-channels', 'Email, the Hub bell, and texts only for the introduction call and urgent legal deadlines. WhatsApp later (off)', 'list', dec=1, old='Text and WhatsApp by client choice', ap=OTHER)
D('quiet-hours', '8pm to 8am for automated emails and texts; legal deadline alerts and tender deadlines within 24 hours still go', 'time', dec=1, old='8pm to 8am, except CQC deadlines', ap=OTHER, csr='quiet-hours')
D('onboarding-form-reminders', 'After 2 days, again after 4; Grace calls on day 6; then weekly until done', 'days', dec=1, old='One reminder after 3 days, a call after 6 (some boards)', ap=SA, sc='onb', csr='form-reminders')
D('document-request-reminders', 'After 3 days, then weekly', 'days', dec=1, old='A gentle nudge after 5 days', ap=SA, sc='pre', csr='document-reminders')
D('draft-review-reminder', 'After 3 days', 'days', dec=1, ap=SA, sc='build')
D('signature-reminders', 'After 2 days, then the consultant calls', 'days', dec=1, old='After 2 days, until signed', ap=SA, sc='build', csr='signature-reminders')
D('third-party-reminders', 'After 3 working days, then weekly', 'working days', dec=1, old='About 3 working days', ap=SA, sc='onb', csr='third-party-reminders', name='Third party reminders (landlord, referee)')
D('pause-reminders', 'Reminders pause until a date', 'rule', ap=LOCK)
D('worried-client-no-nudges', 'No nudges and no sales or growth messages while a client is worried; the review invitation is not held back', 'rule', dec=1, old='No nudges; no growth messages', ap=LOCK, src=PROMISE_REVIEW)
D('staff-alert-principles', 'Never silent', 'rule', ap=LOCK, sc='staff')
D('bounced-email-handling', 'The owner is alerted at once; the message waits until the address is confirmed', 'rule', ap=SA)
D('marketing-frequency-caps', 'At most one marketing email a week; never more than one new idea a month', 'frequency', ap=SA, sc='after', note='decisions.md settles "one new idea a month" (growth-offer-rules) and is silent on the weekly email cap, which is the value the spec uses.')
D('win-back', 'After 6 months without activity (email 8.1)', 'months', ap=SA, sc='prospect')
D('tender-alert-opt-in', 'Opt-in only', 'rule', ap=LOCK, sc='tender')
D('notification-bell', '2 views', 'count', ap=SA)
# Forms and templates
D('template-versioning', 'A new version applies to new journeys only; clients halfway stay on their version unless moved', 'rule', ap=LOCK)
D('form-version-approval', 'The onboarding lead drafts; the other super admin approves', 'route', dec=1, old='Directors edit forms', ap=LOCK, src='Decided 4 November: dual control on form versions')
D('package-modules', '17 modules (A to Q)', 'count', ap=OTHER, ef=NEW)
D('max-tasks-shown', '3 tasks at a time', 'count', ap=LOCK, sc='all')
D('no-time-estimates', 'No promises about how long a regulator, buyer or decision takes, and no "most people finish in N days". Form pages may say how long the page takes to fill in', 'rule', dec=1, old='Time estimates on several boards and emails', ap=LOCK, sc='all', src=PROMISE_TIME, name='No time estimates')
D('save-and-resume', 'Every answer saves instantly', 'rule', ap=LOCK)
D('declaration-last', 'The declaration is always last', 'rule', ap=LOCK)
D('onboarding-complete-before-project', 'Required sections complete first', 'rule', ap=LOCK)
D('tender-form-sections', '15 sections', 'count', dec=1, old='21 sections', ap=OTHER, ef=NEW, sc='tender')
D('not-sure-button', 'On every question', 'rule', ap=LOCK)
D('question-routing', 'The onboarding lead before handover; the case owner after', 'route', ap=SA, sc='active')
D('email-library-versions', '65 messages, each versioned; legal wording needs the other super admin', 'count', ap=LOCK, sc='all', src='Decided 4 November: dual control on legal wording', name='Email versions and legal wording',
  pending=dict(value='5.2 Notice of Proposal v3', by='Daniel Mensah', on='Fri 30 Oct', waiting='Collins or Rachel Turner', where='Messages and automations (board 82)', file='Messages.dc.html'))
D('call-guide', '8 steps', 'count', ap=SA, sc='onb')
D('automation-rules', '46 rules on', 'count', ap=SA, sc='all')
D('relationship-check-moments', 'One tap, three faces, after onboarding, after submission and after the decision; then monthly in aftercare. Reported as % happy', 'schedule', dec=1, old='At the end of each stage, scored out of 5', ap=SA, sc='reg')
# Branding and wording
D('british-english-no-dashes', 'British English; no em or en dashes', 'rule', ap=LOCK)
D('email-style', 'About 120 words, no bold, no exclamation marks', 'rule', ap=SA)
D('banned-words', '"free" is not used in client messages (say "no charge to the client" or "included"); also "guaranteed", "patient", "cheap", "basic", "reach out"', 'list', dec=1, old='"free resubmission" used on staff screens', ap=SA)
D('email-signatures', 'Consultant, bid lead, account owner or director, by email type', 'list', ap=SA)
D('sending-addresses', 'Automated Hub messages from hello@caresyncexperts.co.uk (domain authenticated); personal messages from the staff member\'s Google Workspace mailbox', 'address', dec=1, old='A recognisable Care Sync address', ap=OTHER)
D('brand-assets', 'Care Sync Unified design tokens', 'rule', ap=SA)
D('accessibility-standard', 'WCAG 2.2 AA; touch targets 44 by 44', 'rule', ap=LOCK)
D('neutral-pronouns', 'they/them unless stated', 'rule', ap=LOCK)
D('growth-email-footer', 'A fixed footer on growth emails', 'rule', ap=SA, sc='after')
D('hub-language', 'English only', 'rule', ap=SA)
D('approved-claims', 'Approved claims list only', 'rule', ap=SA)
D('date-format', 'Mon 2 Nov, or dd/mm/yyyy', 'format', ap=LOCK)
# Integrations
D('connections-and-health', '15 connections, each showing what depends on it', 'count', dec=1, old='12 connections, including WhatsApp', ap=OTHER, note='ia.md: 13 of 15 healthy today.')
D('gohighlevel-won-deal', 'Automatic: a won deal starts the journey', 'rule', ap=SA, sc='prospect')
D('companies-house-checks', 'Continuous monitoring', 'frequency', ap=SA)
D('cqc-register-copy', 'Daily', 'frequency', ap=SA, sc='cqc')
D('tender-sources', 'Daily', 'frequency', ap=SA, sc='tender')
D('calls-through-gohighlevel', 'Through the GoHighLevel phone', 'rule', ap=SA)
# Aftercare and growth
D('aftercare-length', '12 months, included in the full start-up package only. Others can buy "Aftercare, 12 months" as an add-on (price to set)', 'months', dec=1, old='12 months for every registered client (boards)', ap=OTHER, ef=NEW, csr='aftercare-months', name='Aftercare: length and who gets it')
D('aftercare-check-in-rhythm', 'Monthly, led by the consultant', 'frequency', ap=SA)
D('aftercare-message-schedule', 'Day 7 launch checklist, day 30 check-in, month 4 inspection readiness, policy review 60 days before the anniversary, the anniversary', 'schedule', ap=SA)
D('inspection-readiness-timing', 'Month 4', 'month', dec=1, old='Month 4 to 6', ap=SA, csr='inspection-readiness-month')
D('policy-review-reminder', '60 days ahead', 'days', ap=SA)
D('aftercare-month-12-handover', 'Month 12', 'month', ap=SA)
D('growth-offer-rules', 'One growth idea shown at a time, no more than one new idea a month, never during a concern or refusal', 'rule', dec=1, old='Three growth options on the aftercare home', ap=LOCK, src=PROT)
D('worried-client-rules', 'The manager calls within 1 working day (a director if the manager is involved); no sales or growth messages until resolved; the review invitation is not held back', 'rule', dec=1, old='Director calls within 1 working day; no sales or review messages', ap=LOCK, sc='all', src=PROMISE_REVIEW)
D('retained-package', 'Offered once, to clients with 2 tenders in 12 months or more than one council area', 'rule', ap=SA, sc='tender')
D('referral-asks', 'At registration, an award letter, or a paid deposit', 'list', ap=SA)
D('anniversary-year-review', 'At the registration anniversary', 'rule', ap=SA)
# Reviews and feedback
D('review-invitation-moment', 'At registration, once, with one reminder after 7 days', 'rule', dec=1, old='2 weeks after registration in some places', ap=LOCK, src=PROMISE_REVIEW)
D('review-reminder', 'Once, 7 days later, only if neither link was opened', 'days', ap=LOCK, csr='review-reminder-days', src=PROMISE_REVIEW)
D('review-no-gating', 'Every registered client is invited, once, whatever their feedback. Nobody is held back or steered', 'rule', dec=1, old='Worried clients held back on 2 boards', ap=LOCK, legal=1,
  src='Law and platform rules: consumer law on fake and gated reviews (DMCC Act 2024) and Google and Trustpilot rules. ' + PROMISE_REVIEW)
D('review-platforms', 'Google and Trustpilot, both offered; the client chooses. Either can be switched off here', 'list', dec=1, old='The Google review link only at first', ap=SA, csr='review-platforms')
D('review-integrity', 'No incentives for reviews', 'rule', ap=LOCK, legal=1, src='Law: DMCC Act 2024 (fines up to 10% of turnover)')
D('review-reply-time', '2 working days', 'working days', ap=SA)
D('unhappy-feedback-routing', 'Goes to the manager, who calls within 1 working day (a director if the manager is involved) and shares it with the consultant with care', 'route', dec=1, old='Consultant and director straight away', ap=SA, sc='all')
D('complaints-handling', 'Acknowledge within 1 working day; full reply within 20 working days; monthly director review', 'working days', ap=LOCK, sc='all', src='Protected rule: the complaint acknowledgement is separate from the reply promise and does not change with it')

EXTRA_RULES = [{'id': 'target-weekend-rule', 'area': 'Promises and timings',
  'rule': 'When one of our internal target dates falls on a weekend or a bank holiday, it moves to the working day before. Legal deadlines never move: they are shown exactly as the law sets them.',
  'values_found': ['the working day before'], 'where': [], 'conflict': False, 'who_should_own': 'super admin', 'is_legal_fixed': False}]
D('target-weekend-rule', 'Internal targets on a weekend or bank holiday move to the working day before; legal deadlines never move', 'rule', ap=SA, sc='all', csr='target-weekend-rule', name='Targets that fall on a weekend',
  note='Added by the lead on 4 November (registry.js key target-weekend-rule); not in inventory.json, so it has no inventory history.')
AUTO_EXTRA = {'target-weekend-rule': ['Notice of Proposal target dates', 'Tender back-scheduling', 'Request for information target date']}

# Automations that read each rule
AUTO = {
 'client-question-reply-time': ['Question timer and overdue alert'], 'question-escalation-team-lead': ['Question escalation to the team lead'],
 'unanswered-message-red': ['Unanswered message colour on My day'], 'senior-question-reply-time': ['Senior question timer'],
 'introduction-call-target': ['Introduction call clock after payment', 'Introduction call texts'], 'working-hours': ['Every working-time clock'],
 'regulator-news-same-day': ['Regulator news to the client'], 'promise-at-risk-warning': ['Promise at risk warning'], 'target-dates-checked-weekly': ['Weekly target date check'],
 'submit-after-final-signature': ['Send after signing clock'], 'consultant-change-notice': ['New consultant email on reassignment'], 'morning-brief': ['Morning brief'],
 'onboarding-gates-list': ['Gate checks when the form arrives'], 'handover-approver': ['Handover approval request'], 'unowned-client-red': ['Unowned client alert'],
 'critical-risk-alerts': ['Critical risk alert'], 'gate-failure-alerts-once': ['Gate failure alert'], 'stage-waiting-colours': ['Waiting on colours'],
 'gone-quiet': ['Gone quiet alert to client care'], 'no-outbound-contact-red': ['No contact alert'], 'regulator-watch-cadence': ['CQC email watch', 'CIW Online check', 'RQIA Web Portal check'],
 'watch-gap-red': ['Watch gap alert'], 'session-reminders': ['Session reminders'], 'interview-reminders': ['Interview reminders'], 'interview-hub-account': ['Interview Preparation Hub account'],
 'nop-internal-targets': ['Notice of Proposal target dates'], 'nop-alert-schedule': ['Notice of Proposal alerts'], 'nop-representation-deadline': ['Legal deadline calculator', 'Legal deadline alerts'],
 'appeal-deadline': ['Legal deadline calculator', 'Legal deadline alerts'], 'legal-alerts-always-on': ['Legal deadline alerts'], 'refusal-same-day-actions': ['Refusal same-day tasks'],
 'refusal-kind-check-in': ['Kind check-in after a refusal'], 'rfi-reply-targets': ['Request for information target date'], 'dbs-age-rules': ['DBS age check'],
 'tender-submit-margin': ['Tender back-scheduling'], 'tender-timeline': ['Tender back-scheduling'], 'tender-tight-deadline-flag': ['Tight deadline flag'],
 'tender-document-expiry-warning': ['Document expiry warning'], 'contract-renewal-watch': ['Contract renewal watch'], 'tender-weekly-client-email': ['Monday tender email'],
 'tps-ctps-screening': ['TPS and CTPS screening'], 'tender-sources': ['Daily tender source check'], 'payment-reminders': ['Payment reminders'], 'accounting-sync': ['Xero sync'],
 'instalment-splits': ['Stripe instalments'], 'leaver-offboarding': ['Leaver access end'], 'staff-invites': ['Invite expiry'], 'break-glass': ['Break-glass timer and alerts'],
 'unusual-activity-alerts': ['Unusual activity alert'], 'super-admin-weekly-summary': ['Weekly super admin summary'], 'link-expiry': ['One-task link expiry'],
 'hosting-and-backups': ['Nightly backup'], 'id-dbs-retention': ['Scheduled deletion run'], 'scheduled-deletion': ['Scheduled deletion run'], 'retention-per-document-type': ['Scheduled deletion run'],
 'voice-note-deletion': ['Voice note deletion'], 'weekly-update-day': ['Weekly update due list', 'Chase reminder', 'Second-person check', 'Send-time check'],
 'weekly-update-rhythm': ['Weekly update due list', 'Chase reminder', 'Second-person check'], 'weekly-update-send-time': ['Send-time check'],
 'quiet-hours': ['Every automated email and text'], 'notification-channels': ['Every automated email and text'], 'onboarding-form-reminders': ['Form reminders', 'Call task for Grace on day 6'],
 'document-request-reminders': ['Document reminders'], 'draft-review-reminder': ['Draft review reminder'], 'signature-reminders': ['Signature reminders'],
 'third-party-reminders': ['Landlord and referee reminders'], 'bounced-email-handling': ['Bounce alert to the owner'], 'win-back': ['Win-back email'],
 'automation-rules': ['All 46 automation rules'], 'relationship-check-moments': ['Relationship check prompts'], 'aftercare-message-schedule': ['Aftercare emails'],
 'aftercare-check-in-rhythm': ['Monthly check-in task'], 'policy-review-reminder': ['Policy review reminder'], 'review-invitation-moment': ['Review invitation at registration'],
 'review-reminder': ['Review reminder'], 'review-platforms': ['Review invitation at registration'], 'review-no-gating': ['Review invitation at registration'],
 'gohighlevel-won-deal': ['Won deal starts a journey'], 'companies-house-checks': ['Companies House monitoring'], 'cqc-register-copy': ['CQC register copy'],
 'complaints-handling': ['Complaint acknowledgement'], 'growth-offer-rules': ['Growth idea picker'], 'marketing-frequency-caps': ['Marketing frequency cap'],
 'worried-client-no-nudges': ['Pause nudges for worried clients'], 'worried-client-rules': ['Pause nudges for worried clients'], 'pause-reminders': ['Reminder pause'],
 'gate-failure-alerts-once': ['Gate failure alert'], 'resubmission-gate': ['Resubmission gate check'], 'aftercare-length': ['Aftercare emails'], 'inspection-readiness-timing': ['Aftercare emails'],
}

# Extra places found by searching boards and the email library for the rule's own wording
ENRICH = {
 'weekly-update-day': (r"every Friday|Friday update|Friday's update|update every Friday|Friday: send|send all \d+ by 16:00|\d+ due Fri 6 Nov|updates? due Fri|updates? on Friday|[Ww]eekly updates? (?:on|every) Friday|Friday, by 16:00", r'Friday'),
 'client-question-reply-time': (r"repl\w*(?: here)? within 1 working day|1 working day promise|We reply within 1 working day", r'reply within 1 working day|replies within 1 working day|within 1 working day'),
 'quiet-hours': (r"8pm to 8am|quiet hours", r'8pm|quiet hours'),
 'sessions-included': (r"3 sessions|three sessions|of 3 sessions|[Ss]ession \d of 3", r'three sessions|3 sessions'),
 'aftercare-length': (r"12 months of aftercare|12 months aftercare|12-month aftercare|first-year support", r'12 months'),
 'review-platforms': (r"Trustpilot", r'Trustpilot'),
 'cv-gap-rules': (r"gaps? (?:longer than|over) 4 weeks", r'gap longer than 4 weeks|gaps? over 4 weeks'),
 'nop-representation-deadline': (r"28 days", None),
 'ico-registration': (r"ico-number|ICO registration number|ICO number", None),
}
def _plain(t):
    t = re.sub(r'<style.*?</style>|<helmet>.*?</helmet>', ' ', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r"[\[\]{}'`]|\\n", ' ', t)
    return re.sub(r'\s+', ' ', t)
OWN = {'Rules.dc.html', 'Packages.dc.html', 'FitsTogether.dc.html'}
ENRICH_EXCLUDE = {'ico-registration': {'CiwForm.dc.html', 'RqiaForm.dc.html'}}  # those forms ask for the client's own ICO number
BOARD_TEXT = {f: _plain(open(PROJ + f).read()) for f in BOARDS if os.path.exists(PROJ + f) and f not in OWN}
ETXT = {}
_t = open('/home/user/Assets/docs/superpowers/specs/2026-11-02-care-sync-hub-client-emails.md').read()
for m in re.finditer(r'^### (\d+\.\d+[a-z]?) .*?(?=^### |^## |\Z)', _t, re.M | re.S):
    ETXT[m.group(1)] = m.group(0)

def title_of(i):
    t = i.replace('-', ' ')
    rep = {'nop': 'Notice of Proposal', 'cv': 'CV', 'dbs': 'DBS', 'id': 'identity', 'rfi': 'request for information', 'ciw': 'CIW', 'rqia': 'RQIA', 'cqc': 'CQC',
           'psc': 'PSC', 'brp': 'BRP', 'tps': 'TPS', 'ctps': 'CTPS', 'sl': 'supported living', 'pir': 'PIR', 'ico': 'ICO', 'vat': 'VAT', 'gohighlevel': 'GoHighLevel', 'rqia': 'RQIA', '2': '2', '12': '12'}
    w = [rep.get(x, x) for x in t.split()]
    s = ' '.join(w)
    return s[0].upper() + s[1:]

def _norm(s):
    return re.sub(r'[^a-z0-9£%]+', ' ', s.lower().replace("\\'", "'")).strip()
NORM_TEXT = {f: _norm(x) for f, x in BOARD_TEXT.items()}
STOP = set('that this with from they them your have will when what into only than more each every also been were their there about which while after before then just like over under some such very much'.split())
CODE = re.compile(r'\)\s*\+|CSR|\bs\.\w+|GN\(|\bpb-|\bsb-|\bT\(|icoErr|=>|===|\bconst\b|\breturn\b|setState|\bcls\b|\bpick\b|\s\+\s|\+ G\(|\b[a-z]+[A-Z]\w*\b|\b[a-z]\.[a-z]\w*\b|\w:\s|\bG\(')
# Board quotes checked by hand: the board no longer has this rule at all, so it is not listed
DROP_REFS = {('cv-gap-rules', 'FormBuilder.dc.html'), ('no-time-estimates', 'Journey.dc.html')}
STALE = []
def current_quote(f, says, rid=''):
    # The inventory was taken from earlier versions of the boards. Keep a quote only if the board still says it;
    # otherwise use the closest sentence the board says now, or drop the board if nothing close is left.
    parts = [_norm(p) for p in re.split(r'\.\.\.|…', says) if _norm(p)]
    if parts and all(p in NORM_TEXT[f] for p in parts):
        return says
    words = [w for w in _norm(says).split() if (len(w) >= 4 or re.match(r'^[0-9£]', w)) and w not in STOP]
    if (rid, f) in DROP_REFS:
        STALE.append((f, says, None)); return None
    if not words:
        STALE.append((f, says, '')); return ''
    best, score = None, 0.0
    for seg in re.split(r'(?<=[.?!])\s+|\s,\s|\s:\s|"|\|', BOARD_TEXT[f]):
        seg = seg.strip(' ,')
        if len(seg) < 12 or len(seg) > 220 or CODE.search(seg): continue
        sw = set(_norm(seg).split())
        sc = sum(1 for w in words if w in sw) / len(words)
        if sc > score: best, score = seg, sc
    if best and re.search(r'[a-z0-9] (?:Open|Mark|Pick|Your|The|A|Every|Account|Save|Cancel|Nightly|Cover|Upload) |^\d', best):
        best = None  # run-together labels, not one sentence
    if best and score >= 0.75:
        best = re.sub(r'^[^A-Za-z0-9£"]*', '', best).strip(' ,')
        best = re.sub(r"\b(\w+) s\b", r"\1's", best)  # apostrophes are stripped from the board text
        if len(best) > 105: best = best[:105].rsplit(' ', 1)[0]
        STALE.append((f, says, best)); return best
    # Not said the same way any more: keep the board (it still uses the rule) but show no quote
    STALE.append((f, says, '')); return ''

def used_in(r):
    out, seen = [], set()
    def add(kind, ref, says=''):
        if ref in seen: return
        seen.add(ref); says = re.sub(r'\{\{(\w+)\}\}', lambda m: '[' + m.group(1).replace('_', ' ') + ']', says)
        out.append({'kind': kind, 'ref': ref, 'says': says[:110]})
    for w in r['where']:
        src = w['src']
        m = re.match(r'board (\S+\.dc\.html)', src)
        if m and m.group(1) in BOARDS:
            if m.group(1) in NORM_TEXT:
                q = current_quote(m.group(1), w['says'], r['id'])
                if q is None: continue
                add(BOARDS[m.group(1)][2], bref(m.group(1)), q); continue
            add(BOARDS[m.group(1)][2], bref(m.group(1)), w['says']); continue
        m = re.match(r'email (\d+\.\d+[a-z]?)', src)
        if m:
            add('email', eref(m.group(1)), w['says']); continue
    en = ENRICH.get(r['id'])
    if en:
        bp, ep = en
        for f, txt in sorted(BOARD_TEXT.items(), key=lambda x: BOARDS[x[0]][0]):
            if f in ENRICH_EXCLUDE.get(r['id'], ()): continue
            mm = re.search(bp, txt)
            if mm:
                win = txt[max(0, mm.start() - 70): mm.end() + 70]
                segs = [g.strip() for g in re.split(r' , |\s,\s|: \(|\? | : |\.map\(|=>|===', win)]
                s = next((g for g in segs if mm.group(0) in g), mm.group(0))
                s = re.sub(r'^[^A-Z0-9]*', '', s).strip(' ,')
                if len(s) > 105: s = s[:105].rsplit(' ', 1)[0]
                s = re.sub(r"\b(\w+) s\b", r"\1's", s)  # apostrophes are stripped from the board text
                if re.search(r'\)\s*\+|CSR|\bs\.\w+|GN\(|\bpb-|\bsb-|\bT\(|icoErr', s): s = ''
                add(BOARDS[f][2], bref(f), s)
        if ep:
            for n, et in ETXT.items():
                if re.search(ep, et):
                    add('email', eref(n), '')
    for a in AUTO.get(r['id'], []) + AUTO_EXTRA.get(r['id'], []):
        add('automation', 'automation: ' + a)
    order = {'client': 0, 'staff': 1, 'email': 2, 'automation': 3, 'report': 4}
    out.sort(key=lambda x: order[x['kind']])
    return out

def spec_refs(r):
    return [w['src'] for w in r['where'] if w['src'].startswith('spec')]

def default_value(r):
    vf = r['values_found']
    return vf[0][0].upper() + vf[0][1:] if vf else ''

entries = []
missing = []
for r in INV + EXTRA_RULES:
    i = r['id']
    o = R.get(i)
    if o is None:
        missing.append(i); o = dict(v=default_value(r), u='')
    legal = bool(o.get('legal') or r['is_legal_fixed'])
    ap = o.get('ap') or (LOCK if r['who_should_own'].startswith('nobody') else SA)
    locked = ap == LOCK
    src = o.get('src', '')
    if locked and not src:
        src = PROT
    note = o.get('note', '')
    if not o.get('dec') and not note:
        if len(r['values_found']) > 1 or r['conflict']:
            note = 'decisions.md is silent; this is the value most places use. Others found: ' + '; '.join(x for x in r['values_found'] if x.lower() != o['v'].lower())[:200]
        else:
            note = 'decisions.md is silent; every place found uses this value.'
    elif o.get('dec') and not note:
        note = 'Set by decisions.md (4 November 2026).'
    vers = []
    ef = o.get('ef') or DATE
    if o.get('old') and not o.get('pending'):
        vers.append({'v': 1, 'date': GOLIVE, 'value': o['old'], 'by': 'Collins, at go-live', 'status': 'replaced', 'effective': 'everyone'})
        vers.append({'v': 2, 'date': DEC_DATE, 'value': o['v'], 'by': 'Decided by Collins, approved by Rachel Turner on Mon 2 Nov', 'status': 'live', 'effective': ('new clients from ' if ef == NEW else 'everyone from ') + DEC_DATE})
    elif o.get('pending'):
        p = o['pending']
        vers.append({'v': 1, 'date': GOLIVE, 'value': o.get('old', o['v']), 'by': 'Collins, at go-live', 'status': 'live', 'effective': 'everyone'})
        vers.append({'v': 2, 'date': p['on'] + ' 2026', 'value': p['value'], 'by': 'Entered by ' + p['by'] + ', waiting for ' + p['waiting'], 'status': 'waiting', 'effective': 'new clients only' if ef == NEW else 'everyone from the approval date'})
    elif o.get('pir'):
        vers.append({'v': 1, 'date': GOLIVE, 'value': '£750 + VAT', 'by': 'Collins, at go-live', 'status': 'replaced', 'effective': 'everyone'})
        vers.append({'v': 2, 'date': 'Fri 30 Oct 2026', 'value': o['v'], 'by': 'Requested by Grace, approved by Collins', 'status': 'live', 'effective': 'new clients from Sun 1 Nov 2026'})
    else:
        vers.append({'v': 1, 'date': GOLIVE, 'value': o['v'], 'by': 'Collins, at go-live' if not locked else ('Fixed by law or a regulator' if legal else 'Locked at go-live'), 'status': 'live', 'effective': 'everyone'})
    sc = o.get('sc') or AREA_SCOPE[r['area']]
    cn, cl = SCOPES[sc]
    owner = OWNER[r['area']]
    if locked and legal: owner = 'Fixed by law or a regulator (kept up to date by Collins)'
    elif locked: owner = 'Locked by Care Sync (' + owner + ' keeps it in view)'
    if ap == MGR: owner = 'Managers (Rachel Turner)'
    e = {
        'id': i, 'area': r['area'], 'name': o.get('name') or title_of(i), 'rule': r['rule'], 'value': o['v'], 'unit': o['u'] or 'rule',
        'legal': legal, 'source': src, 'locked': locked, 'owner': owner, 'approval': ap, 'effective': ef,
        'used_in': used_in(r), 'versions': vers, 'clients_now': cn, 'clients_label': cl,
        'changed_this_month': any(('Nov' in v['date'] or 'Fri 30 Oct' in v['date']) and v['status'] == 'live' and v['v'] > 1 for v in vers),
        'waiting': o['pending'] if o.get('pending') else None,
        'registry_key': o.get('csr', ''), 'spec': spec_refs(r), 'had_conflict': r['conflict'], 'note': note,
    }
    entries.append(e)

if missing:
    print('NO OVERRIDE FOR', len(missing), missing)
extra = set(R) - {r['id'] for r in INV + EXTRA_RULES}
if extra: print('OVERRIDES WITH NO RULE', extra)
json.dump({'generated': 'Mon 2 Nov 2026', 'source': 'inventory.json + decisions.md (4 November 2026)', 'count': len(entries), 'rules': entries}, open(SP + '/superadmin/registry.json', 'w'), indent=1, ensure_ascii=False)
json.dump([{'board': f, 'inventory': s, 'now': q} for f, s, q in STALE], open(SP + '/superadmin/registry-stale-quotes.json', 'w'), indent=1, ensure_ascii=False)
print('stale board quotes', len(STALE), 'replaced', sum(1 for x in STALE if x[2]), 'kept without a quote', sum(1 for x in STALE if x[2] == ''), 'dropped', sum(1 for x in STALE if x[2] is None))
print('rules', len(entries), 'locked', sum(e['locked'] for e in entries), 'legal', sum(e['legal'] for e in entries),
      'changed', sum(e['changed_this_month'] for e in entries), 'waiting', sum(bool(e['waiting']) for e in entries),
      'used_in', sum(len(e['used_in']) for e in entries))
