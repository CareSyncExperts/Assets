# Shared facts for the super admin boards built by agent B (Rules 80, Packages 81, Fits together 89).
SP = '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad'

# board file -> (number, short name, kind)
BOARDS = {
 'Main.dc.html': (1, 'Today', 'client'), 'Journey.dc.html': (2, 'Your journey', 'client'), 'Documents.dc.html': (3, 'Your documents', 'client'),
 'Review.dc.html': (4, 'Review Room', 'client'), 'Cqc.dc.html': (5, 'CQC centre', 'client'), 'Ask.dc.html': (6, 'Ask Care Sync', 'client'),
 'Staff.dc.html': (7, 'My day', 'staff'), 'Onboarding.dc.html': (8, 'Onboarding gates', 'staff'), 'Weekly.dc.html': (9, 'Weekly update composer', 'staff'),
 'Radar.dc.html': (10, 'Tender Radar', 'staff'), 'Tender.dc.html': (11, 'Tender record', 'staff'), 'FormStaff.dc.html': (13, 'Form received and checks', 'staff'),
 'AddressCheck.dc.html': (14, 'Address and identity check', 'staff'), 'AddressClient.dc.html': (15, 'One quick question', 'client'),
 'EmailRegistered.dc.html': (17, 'Email: You are registered', 'email'), 'DocRoom.dc.html': (18, 'Documents room', 'client'), 'Sign.dc.html': (19, 'Sign your pack', 'client'),
 'Celebrate.dc.html': (20, 'Registered, share your experience', 'client'), 'DoneList.dc.html': (21, 'Done for you checklist', 'client'),
 'PortalWatch.dc.html': (22, 'Regulator and tender watch', 'staff'), 'CompanySearch.dc.html': (23, 'Find your company', 'client'),
 'SuperAdmin.dc.html': (24, 'Super admin home', 'staff'), 'Welcome.dc.html': (25, 'Welcome', 'client'), 'EmailConnect.dc.html': (27, 'Your business email', 'client'),
 'Sessions.dc.html': (28, 'Book your session', 'client'), 'Account.dc.html': (29, 'Your account and privacy', 'client'), 'Aftercare.dc.html': (30, 'Aftercare and growing', 'client'),
 'TenderClient.dc.html': (31, 'Your tender', 'client'), 'ClientMap.dc.html': (32, 'Client journey map', 'staff'), 'IntroCall.dc.html': (33, 'Introduction call', 'staff'),
 'SnapSend.dc.html': (34, 'Snap and send', 'client'), 'SupportWho.dc.html': (35, 'Who you will support', 'client'), 'Directors.dc.html': (36, 'Directors and owners', 'client'),
 'ThirdParty.dc.html': (37, 'One-task links', 'client'), 'TenderOnboard.dc.html': (38, 'Tender Preparation Questionnaire', 'client'), 'BrandWeb.dc.html': (39, 'Brand and website', 'client'),
 'SignIn.dc.html': (40, 'Sign in', 'client'), 'Notifications.dc.html': (41, 'Notifications', 'client'), 'ClientPage.dc.html': (42, 'Client page', 'staff'),
 'ManagerDash.dc.html': (43, 'Manager dashboard', 'staff'), 'FormBuilder.dc.html': (44, 'Forms', 'staff'), 'SmallTasks.dc.html': (45, 'Small tasks', 'client'),
 'RegDetails.dc.html': (46, 'Your onboarding form', 'client'), 'ManagerFlow.dc.html': (47, 'CQC Registration Information Form', 'client'), 'TenderProfile.dc.html': (48, 'Tender profile', 'client'),
 'Tenders.dc.html': (49, 'Your tenders', 'client'), 'BidDecision.dc.html': (50, 'Should we bid?', 'client'), 'AddClient.dc.html': (51, 'Add a client', 'staff'),
 'OnbCheck.dc.html': (52, 'After the form', 'client'), 'ClientStates.dc.html': (53, 'Every state and small moment', 'client'), 'ClientDesktop.dc.html': (54, 'Your Hub on a computer', 'client'),
 'CiwForm.dc.html': (55, 'CIW Registration Information Form', 'client'), 'RqiaForm.dc.html': (56, 'RQIA Registration Information Form', 'client'), 'TenderWork.dc.html': (57, 'Tender workspace', 'client'),
 'TenderConfirm.dc.html': (58, 'Each new tender', 'client'), 'TwoServices.dc.html': (59, 'Your plan', 'client'), 'PlanCosts.dc.html': (60, 'Plan and costs', 'client'),
 'AddressCards.dc.html': (61, 'Address history', 'client'), 'Security.dc.html': (62, 'How we keep your information safe', 'client'), 'RegCentre.dc.html': (63, 'Your regulator', 'client'),
 'TeamViews.dc.html': (64, 'Co-director and manager views', 'client'), 'Resubmit.dc.html': (65, 'Refused: we resubmit', 'client'), 'ResubmitStaff.dc.html': (66, 'Resubmission project', 'staff'),
 'Questions.dc.html': (67, 'Questions inbox', 'staff'), 'ClientsList.dc.html': (68, 'Clients', 'staff'), 'CoachSessions.dc.html': (69, 'Sessions and interview practice', 'staff'),
 'ClientCare.dc.html': (70, 'Client care', 'staff'), 'AftercareStaff.dc.html': (71, 'Aftercare (staff)', 'staff'), 'Reports.dc.html': (72, 'Reports', 'report'),
 'OnboardingQueue.dc.html': (73, 'Onboarding queue', 'staff'), 'Handover.dc.html': (74, 'Handover', 'staff'), 'Deadlines.dc.html': (75, 'Deadlines', 'staff'),
 'RegReply.dc.html': (76, 'Answer the regulator', 'staff'), 'PriceBook.dc.html': (77, 'Price book', 'staff'), 'TeamCover.dc.html': (78, 'Team and cover', 'staff'),
 'GoLive.dc.html': (79, 'Go-live readiness', 'staff'), 'Rules.dc.html': (80, 'Rules and promises', 'staff'), 'Packages.dc.html': (81, 'Packages and journeys', 'staff'),
 'Messages.dc.html': (82, 'Messages and automations', 'staff'), 'PeopleAccess.dc.html': (83, 'People and access', 'staff'), 'SecurityCentre.dc.html': (84, 'Security', 'staff'),
 'DataPrivacy.dc.html': (85, 'Data and privacy', 'staff'), 'Health.dc.html': (86, 'System health', 'staff'), 'MoneyExports.dc.html': (87, 'Money and exports', 'staff'),
 'ViewAs.dc.html': (88, 'View as and history', 'staff'), 'FitsTogether.dc.html': (89, 'How it fits together', 'staff'),
}

def bref(f):
    n, name, kind = BOARDS[f]
    return 'board %d %s' % (n, name)

# Email titles from the client email library (docs/superpowers/specs/2026-11-02-care-sync-hub-client-emails.md)
def load_emails():
    import re
    t = open('/home/user/Assets/docs/superpowers/specs/2026-11-02-care-sync-hub-client-emails.md').read()
    out = {}
    for m in re.finditer(r'^### (\d+\.\d+[a-z]?) (.+)$', t, re.M):
        title = re.sub(r'\s*\(.*?\)\s*$', '', m.group(2)).strip()
        out[m.group(1)] = title
    return out
EMAILS = load_emails()
def eref(n):
    return 'email %s %s' % (n, EMAILS.get(n, ''))

# The demo world client mix (52 active clients; matches Manager dashboard board 43 stage counts)
SCOPES = {
 'all': (52, 'every active client'),
 'reg': (48, 'registration clients, stages 1 to 11'),
 'active': (38, 'clients in stages 1 to 10'),
 'weekly': (42, '38 clients in stages 1 to 10 and 4 tender only clients'),
 'onb': (6, 'clients in onboarding, stage 1'),
 'build': (20, 'clients in stages 2 to 6'),
 'pre': (26, 'clients in stages 1 to 6'),
 'reglr': (12, 'clients with the regulator, stages 7 to 10'),
 'sess': (30, 'clients with sessions still to come'),
 'interview': (2, 'clients at interview, stage 9'),
 'after': (10, 'clients in aftercare'),
 'tender': (5, 'clients with a live bid'),
 'cqc': (38, 'CQC clients'), 'ciw': (5, 'CIW clients'), 'rqia': (5, 'RQIA clients'),
 'full': (11, 'full start-up clients'),
 'nop': (1, 'Sunrise Homecare, Notice of Proposal'),
 'refused': (1, 'Westbrook Care, refused and resubmitting'),
 'legal': (2, 'Sunrise Homecare and Westbrook Care'),
 'ciwafter': (1, 'Bryn Glas Care, CIW aftercare'), 'rqiaafter': (1, 'Foyle Home Care, RQIA aftercare'),
 'sam': (6, 'Sam Patel\'s 6 clients, being reassigned'),
 'signed': (0, 'nobody now: signed clients keep the price in their agreement'),
 'new': (0, 'nobody now: new clients only'),
 'staff': (0, 'no clients directly: the 10 people with access'),
 'prospect': (0, 'enquiries, before they are clients'),
}
