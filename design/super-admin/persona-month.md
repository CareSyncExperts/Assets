## Super admin usability test: Collins (super admin 1) and the manager (super admin 2)

This was a read-only review. I read spec sections 46, 49, 51, 55, 60 and 61, the demo world file and all 8 super admin boards (text and JS arrays). I also cross-checked 20 other boards. No files were changed.

The short version: the Hub is strong at approving things (a reason is required, nobody approves their own request, and the audit log cannot be edited). It is weak at configuring things. Most "settings" are text typed into each screen, with no control behind them. The staff menu has a "Templates" item, but no board exists for it. ClientMap's "Super admin controls" row (teal, "set once by the super admin") lists about 25 controls, and almost none of them has a screen.

### Scenario by scenario

**1. Launch day.** Verdict: Partly.
- **What exists:**
  - PriceBook: "Edit price" and "Set a price"; anything not decided shows "Price to set; nobody quotes it".
  - FormBuilder: 4 live forms and 5 draft add-on forms.
  - TeamCover: "Invite a person".
  - SuperAdmin: "Connections: 11 of 12 healthy", status only.
- **What is missing:**
  - Branding, the sending domain (authentication of the sending address), the email library, journey templates, reminder timings, a quiet hours default, working hours, bank holiday calendars, a retention schedule, the ICO number and the legal wordings (questions 21, 24, 25).
  - There is no way to connect an integration or enter its key, and no "ready to go live" checklist.
  - There is no import for clients who are already partway through. AddClient only handles a fresh won deal, so Westbrook at stage 10 could not be added.
  - **Bootstrap problem:**
    - TeamCover says "A super admin invite needs the other super admin's approval before it is sent", and every price or form needs the second super admin to approve it.
    - On day one only Collins exists, so he cannot invite the second super admin or set up the first price book.
    - The manager's row reads "Account set up at launch", with no name.

**2. Weekly update day from Friday to Thursday.** Verdict: No.
- There is no setting anywhere. "Friday" is typed into 32 boards, for example:
  - Weekly: "Friday: send all 10 by 16:00", "Wednesday: chase…", "Thursday: a second consultant reads every draft".
  - Welcome: "An update every Friday".
  - Cqc: "We update you every Friday until it comes".
  - Main: "Your Friday update".
  - Account: "Friday updates and anything important".
  - SuperAdmin automation: "Weekly updates on Friday".
  - Reports promise: "Weekly update every Friday".
  - AddClient: "Grace sends the Friday update".
  - Staff, ManagerDash and TeamCover: "10 due Fri 6 Nov".
- The internal rhythm (chase on Wednesday, second read on Thursday) would also need to move a day earlier.

**3. Reply promise from 1 working day to 4 working hours.** Verdict: No.
- ClientMap lists "reply-time promise" as a super admin control, but there is no screen for it.
- Hard-coded text: "Daniel usually replies within 1 working day" (Ask), "Grace replies here within 1 working day" (four forms), "Daniel replies within 1 working day" (Review), "timed against the 1 working day promise" (Questions), and Reports "Reply to client questions within 1 working day 97%".
- "Working hours" are not defined anywhere: no office hours, and no bank holiday calendars for England and Wales versus Northern Ireland, which matter for RQIA clients.
- The complaint acknowledgement ("1 working day") is a protected rule (51.4 rule 7) and must not change along with the reply promise.
- Reports would need to measure each reply against the promise that was in force at the time.

**4. A new package (children's services, or a variation).** Verdict: No.
- PriceBook has no "Add a package" button.
- FormBuilder has no "New form" button; it only has "Start a draft" on existing forms.
- AddClient's package list and section letters are fixed in code.
- There is no stage, documents, sessions or aftercare editor, although spec 3.2 promises "add a stage… change the number of included sessions".
- Children's services exist only as "Choosing children triggers a call" (SupportWho).
- A variation price and its draft form exist, but AddClient will sell the variation while its form says "Draft, not live yet".

**5. A price change and a discount request.** Verdict: Partly.
- **Price change:** the edit flow works: price, VAT, "Effective from (new clients only)", a reason, then "You cannot approve your own change". But:
  - Instalments cannot be edited, although the board says "Instalment splits marked 'default' can be changed here". The edit form has only price, VAT and date.
  - There is no "where this price appears" list. Aftercare (30), PlanCosts (60), Account, AddClient (its own price array), GoHighLevel quotes and sales scripts all hold their own copy.
- **Discount:** the decision works. "Approve the discount" needs a reason, but then: "The price book itself does not change".
  - Nothing shows how the discount reaches the agreement, the Stripe instalments, the Xero invoice or the client's PlanCosts and Account screens.
  - AddClient has no "ask for a discount" control at all.

**6. Change one question on the CQC form with 3 clients halfway through.** Verdict: Partly (the best-designed flow).
- **What works:** FormBuilder's "Draft v8" with an Added, Removed and Reworded change view showing "Was: …", "Send to the second super admin", "Clients halfway through the form stay on v7: 3", and "Move to v8: answers kept, 2 new questions added".
- **What is missing:**
  - The pencil icon is decorative; there is no editor for wording, help text or validation.
  - There is no preview as the client.
  - There is no impact view on the FormStaff checks, the 8 onboarding gates, the CQC application sheet or the Questions inbox suggested replies ("Suggested replies follow the form's own help text").
  - Clients who are moved get no message.
  - AddClient's form preview does not change.

**7. Change the Notice of Proposal email and preview it as a client.** Verdict: No.
- There is no email library board. The "Templates" menu item goes nowhere.
- Email "5.2 Notice of Proposal" appears only as a label on ClientMap.
- There is no merge field preview (date served, legal deadline, our target), no version or approval, and no brand voice check (49.9).
- The only "Preview as the client" in the boards is for the fix list on Onboarding.

**8. A new consultant joins; Sam leaves on Friday.** Verdict: Partly.
- **Leaver (strong):** the TeamCover checklist, "Reassign" with a required handover note, "Vault access ends Fri 6 Nov at 17:30", and "Sam's emails forward to Collins for 90 days". But:
  - New owners can only be "Olu, from Mon 9 Nov" or "Collins". Neither the manager nor a new starter can be chosen.
  - The checklist has no client step: email 9.3 "Your new consultant" is missing, and the client's screens still show the old name ("Daniel, your consultant", the Account team list).
  - It does not cover Sam's 6 Friday updates due on his last day, his client mailbox connections (46.1 says they are handed to the new owner), Questions inbox items, Interview Preparation Hub access, GoHighLevel or Google Drive.
  - Sam's suspicious export does not trigger an immediate suspension; his access still ends on Friday.
- **Starter (thin):** the invite has only name, email and one of 7 roles. It does not provision Google Workspace, set client scope or a start date, or start Academy induction.
  - The new person never appears in AddClient's "Proposed consultant" list (fixed as Daniel, Olu, Sam) or in the reassignment options.

**9. Subject access request, and retention ending for a closed client.** Verdict: Partly.
- **Subject access request: No.** The client has "Download everything" and "Correct something we hold" (Account), but there is no staff queue for the 49.6 request queue: no one-month clock, identity check, redaction of referee or landlord data, or extension.
- **Retention: Yes for ID documents.** "Scheduled deletion: 14 identity documents" lists each document, "Legal hold check: clear", and "Deleted 7 days after approval". But:
  - There is no retention schedule screen and no control to place a legal hold.
  - Deletion is approved by one person (prepared by the Hub, approved by Collins). Spec 46.2 asks for a second super admin.

**10. A staff laptop is lost.** Verdict: No.
- There is no breach log, no 72-hour clock, no device or session list, no "sign out everywhere" or "suspend now", and no Google device wipe.
- The only help is searching the audit log by name, the "Export" button, and the unusual activity panel's "paused Sam's downloads".

**11. Break-glass access while the case owner is away.** Verdict: Yes.
- SuperAdmin has a reason box, "Approve for 4 hours", "Ends automatically after 4 hours", and "The client is emailed today and sees it on their privacy page". Gaps:
  - No alert to the other super admin (46.1).
  - No list of what was revealed during the window, and no way to revoke early or extend.
  - Olu is not told.
  - Break-glass is being used for planned leave cover ("Vault logins need break-glass", TeamCover). Planned leave should come with approved vault access set up when the leave is booked.

**12. Stripe stops syncing; one client's CQC email watch fails; an automation fails overnight.** Verdict: Partly.
- **Stripe:** a status chip only. No reconnect button, last successful sync, failed items queue, list of unmatched payments, or effect on payment-triggered stages and the client's payment screens.
- **CQC watch:** a single row ("Riverside Homecare: login not in the vault, 10 days") plus ManagerDash "Watch gaps". There is no list per client mailbox, no "ask the client to reconnect" (EmailConnect 27), and no fallback to the forwarding address (7.2).
- **Automation:** the Greenway failure flow is good ("Fix email address", "See run log", "resend waits until Daniel confirms"). But only 4 of the "46 rules on" are listed, there is no retry, and there is no out-of-hours alert.

**13. A regulator changes a rule.** Verdict: No.
- There is no regulatory watch (49.4) and no rule register linking a requirement to forms, gates, checks, Pack Doctor rules, checklists and emails. "Pack Doctor rules" appears only on ClientMap.
- FormBuilder can draft a CIW form change, and that is all.

**14. A complaint: "you told me two different things".** Verdict: Partly.
- ClientPage has "View as Joy", but it is a consultant tool with no reason box, no handler and no logging shown. There is no view as the client saw it on a past date, and no view as a staff member.
- The client's privacy log shows "Daniel Mensah saw your Hub as you see it".
- There is no complaints register (49.2: a named handler, a 20 working day reply, lessons learned).

**15. Month end.** Verdict: Partly.
- **What exists:** ManagerDash Money (invoiced, collected, overdue by age, instalments, revenue by package) and Reports (promises, days per stage, outcomes, tenders, feedback).
- **What is missing:**
  - Reports' period tabs do not change any figures.
  - The only export in the whole design is "audit-log.csv". There is no export for the accountant: no VAT split (some items are "incl. VAT" while ManagerDash says "Amounts exclude VAT"), no Stripe payouts and fees, no refunds or credit notes (49.1), no discounts given and no proof bank (49.5).

**16. Turn off review invitations.** Verdict: No.
- There are no on/off switches and no dependency view.
- **Spec conflict:** 51.4 rule 5 says "every registered client is invited, once" and that settings "cannot switch off" these rules. So the screen either needs a locked rule with an explanation, or the spec needs changing.
- Screens that depend on it: Celebrate "Review on Trustpilot", EmailRegistered "Review us on Trustpilot", email 5.4, Reports "Reviews 7 from 11 invitations", and ManagerDash's "no sales or review messages" rule for worried clients.

### (a) Summary table

| # | Scenario | Verdict | Board(s) | What is missing |
|---|---|---|---|---|
| 1 | Launch day | Partly | 77, 44, 78, 24 | Branding, sending domain, templates, emails, calendars, retention, integration setup, readiness check, bootstrapping the second super admin, import of existing clients |
| 2 | Weekly update day | No | none | One setting; Friday is hard-coded on 32 boards |
| 3 | Reply promise | No | none (ClientMap claims it) | Setting, working hours, bank holidays by nation, reporting against the promise of the day |
| 4 | New package | No | 77, 44 (edit only) | Package builder: price, instalments, form, stages, documents, sessions, aftercare, AddClient |
| 5 | Price and discount | Partly | 77 | Instalment editing, where-used list, discount flowing into agreement, Stripe and Xero, a discount request in AddClient |
| 6 | Form question change | Partly | 44 | Question editor, client preview, impact on gates, checks and application sheet, message to moved clients |
| 7 | Notice of Proposal email | No | none ("Templates" item is empty) | Email library, merge preview, versions, approval |
| 8 | Starter and leaver | Partly | 78, 24 | Starter provisioning, picker lists, client notice 9.3, mailbox handover, immediate suspension |
| 9 | Subject access and retention | Partly | 24 (deletion) | Request queue with legal clock, retention schedule, legal hold control, second approver |
| 10 | Lost laptop | No | 24 (log search only) | Breach log, 72-hour clock, sessions and devices, suspend, revoke |
| 11 | Break-glass | Yes | 24 | Alert to other super admin, early revoke, reveal list, planned-cover delegation |
| 12 | Failures | Partly | 24, 43 | Reconnect, retry, failed queue, per-client watch list, overnight alerts |
| 13 | Regulator rule change | No | none | Regulatory watch and rule register linked to forms, gates, checks, emails |
| 14 | View as and history | Partly | 42 ("View as Joy"), 29 | Super admin view as, past-date view, complaints register |
| 15 | Month end | Partly | 43, 72 | Accountant exports, VAT split, refunds and credit notes, working period filters |
| 16 | Turn off an automation | No | 24 (4 of 46 rules) | Rule list, switches, dependencies, locked protected rules |

### (b) Top 12 missing super admin capabilities, ranked by impact
1. **A settings and templates centre (the missing "Templates" board).** Service rules (weekly update day and time, reply promises, quiet hours, working hours, bank holiday calendars for each nation), journey templates and the email library, each with versions, approval and "preview as a real client". Every screen should read from these rather than holding its own text.
2. **A package builder.** One record per package linking price, editable instalments, form, stages, documents, sessions, aftercare length and whether AddClient offers it.
3. **The full automation list.** All 46 rules, each with an on/off switch, an owner, a run log, retry, "what depends on this", protected rules shown as locked, and out-of-hours failure alerts.
4. **Data protection operations.** The subject access, correction and deletion queue with legal clocks, a breach log with the 72-hour clock, a retention schedule for each document type, and legal holds.
5. **A staff incident panel.** Suspend now, sign out everywhere, revoke vault and Google sessions, "what did this person access in the last N days", linked to the breach log.
6. **Impact analysis and a regulatory rule register.** For any change to a price, question, rule or email: which clients, screens, gates, checks, emails and Pack Doctor rules are affected.
7. **One approvals inbox** with a true count. Today approvals are spread over SuperAdmin, PriceBook, FormBuilder, ManagerDash (bid or no bid) and Handover.
8. **Integration management.** Connect and reconnect, keys, last successful sync, a failed items queue, a per-client mailbox watch list, and a client reconnect message.
9. **A go-live readiness wizard.** Bootstrapping the second super admin, branding, sending domain authentication, ICO number, legal wordings, importing existing clients mid-journey, and the 3-client test.
10. **Super admin "View as"** for any client or staff member, now or at a past date, with a reason and logging, plus one combined communication history and a complaints register.
11. **Finance controls and exports.** An accountant export (VAT split, Stripe payouts and fees, refunds, credit notes, discounts), month close, refund approval, and discounts flowing through to the agreement, Stripe and Xero.
12. **The full staff lifecycle.** Starter provisioning (Google Workspace, Interview Preparation Hub, GoHighLevel, Academy, client scope, start date), an editable permissions grid, a leave and cover set-up control, the client notice of a new consultant, and new people appearing in every picker.

### (c) Places where a super admin setting does not flow through
1. **Weekly update day:** fixed text on 32 boards (client: Welcome, Main, Cqc, Account, Notifications; staff: Weekly, Staff, ManagerDash, Reports, TeamCover, AddClient).
2. **Reply promise:** fixed text in Ask, Review, the CiwForm, RqiaForm, ManagerFlow and TenderOnboard forms, the Questions SLA ("Reply by 16:00 tomorrow"), and Reports.
3. **Prices:**
   - AddClient has its own price and instalment arrays.
   - Aftercare (30) and PlanCosts (60) show prices as text.
   - AddClient's "Default, can be changed in the price book" points to an instalment control that does not exist.
4. **Discounts:** "The price book itself does not change". Nothing reaches AddClient's total, Sign, Stripe, Xero, PlanCosts or Account.
5. **Form versions:**
   - AddClient's "The onboarding form this client gets" uses its own 13 CQC sections (including Type of Legal Entity), not FormBuilder's 19 pages.
   - v8's "Removed: Type of Legal Entity" is not reflected anywhere else.
   - The FormStaff checks and Onboarding gates are not linked to form versions.
6. **New staff:** an invite does not add the person to AddClient's "Proposed consultant" list or to TeamCover's reassignment options.
7. **Reassignment:** the client-facing consultant name (Main, Account "Who can see your information", Ask) and email 9.3 are not part of offboarding.
8. **Retention:** SuperAdmin deletes for closed clients, but Account says "Your ID and DBS copies are deleted after our work ends" and Security says "deleted when your 12 months of aftercare end".
9. **Roles:** the permissions grid is read-only and not tied to the menu ("Items a role cannot use are hidden" is only a note).
10. **Quiet hours:** Account shows "8pm to 8am", Weekly says "outside their quiet hours", and there is no super admin default.
11. **WhatsApp:** this is a later-phase decision, yet Account offers a WhatsApp channel and SuperAdmin shows "SMS and WhatsApp: Healthy".
12. **Reviews:** the default is "the Google review link only at first", but Celebrate and EmailRegistered show Trustpilot buttons.
13. **Approval badge:** "3" is fixed everywhere while other decisions wait (see contradiction 1).
14. **Reports period tabs** change nothing.
15. **ClientMap's "Super admin controls" row** names controls that drive no screen: call guide, retries, reminder timings, update template, e-signature settings, who can approve a pack, watch rules, review links, aftercare length, check-in rhythm, offer rules, hand-back checklist.

### (d) Contradictions between super admin boards and other boards
1. **Approval count:** the badge reads "3 approvals waiting", but PriceBook shows "Discount requests 2", ManagerDash's Maple Court bid is "Waiting on you", OnboardingQueue has Binnian "Grace asked Collins to approve the handover", and FormBuilder v8 is "ready for review". Collins really has at least 7 decisions waiting.
2. **People count:** SuperAdmin and TeamCover both say "Staff with access 8" and "People with access 8", but TeamCover lists 9 people.
3. **The manager's row in TeamCover** shows "0% of a normal week" (the code checks for the name "Second super admin" but the row is named "A manager") and "Account set up at launch". Meanwhile PriceBook and FormBuilder already have that person approving things.
4. **The Manager role** has "Prices: View" and "Forms: View" in the grid, while the same board says the manager "Approves price, form and permission changes".
5. **The PIR price change** was "Requested by Grace, approved by Collins" (PriceBook history and the SuperAdmin log). This breaks "Only a super admin changes a price, and the other super admin approves it" and the grid's "Onboarding lead: Prices View".
6. **FormBuilder's halfway clients** (Primrose Care Services, Kingfisher Home Care, Elmwood Supported Living, "page 6 of 19") do not exist in OnboardingQueue. There, Oak Hollow "Stopped at section 8 of 13" and Kingfisher Support Ltd is a tender client.
7. **FormBuilder's CQC form has no "Your office" step**, although spec 60.2 added it because the address gate needs it.
8. **AddClient and PriceBook differ:**
   - Package names: "Interview preparation only" against "CQC interview preparation"; "PIR completion" against "PIR writing".
   - Seven price book items are missing from AddClient.
   - AddClient says "Collins sets it before the invoice goes out", while the price book rule is a second super admin approval.
9. **Discount source:** the PriceBook section is "Discount requests from Add a client", but AddClient has no such control, and the Ashby request came from Daniel, not from Add a client.
10. **Price statuses:** "Policy rebrand… still to confirm with Collins" shows as "Live"; "Single services" shows as Live with payment stages "To set".
11. **Break-glass:** Account says "A director can step in only in an emergency", but SuperAdmin grants Daniel, a consultant, and TeamCover uses break-glass for planned leave.
12. **View as:** a super admin capability in spec 46.1, but it appears only as a consultant's button on ClientPage.
13. **Free resubmissions:** ManagerDash says "45 hours… this year", including a July client. Reports, under "This quarter", says "Staff hours in total 45 hours" and "Registered after resubmitting 1, after 31 hours".
14. **Overdue invoices:** ManagerDash says "Overdue £5,300, 4 invoices"; Reports says "Paid on time 82%, 2 overdue".
15. **Connections:** SuperAdmin's 12 include WhatsApp (a later phase) and leave out Ordnance Survey, HM Land Registry, CQC data and BidSuite, which spec 46.1 lists.
16. **GoHighLevel:** "Won deals start journeys" (SuperAdmin, spec default 7), yet AddClient needs a person to press "Add client and book the introduction call" while the 2-hour call clock is already running.
17. **Single approver:** deletion and the PIR price change were each approved by one super admin, against spec 46.2.

### (e) Three things that are excellent and must be kept
1. **The approval pattern.**
   - "Write a reason before you approve or decline", "Nobody can approve their own request", and PriceBook's "You cannot approve your own change. Switch to 'Second super admin'…".
   - An audit log with "Entries cannot be edited or deleted", search, filters and export.
2. **FormBuilder versioning.** The Added, Removed and Reworded change view with "Was: …", "Clients halfway through the form stay on v7", "Move to v8: answers kept, 2 new questions added", and a draft whose stated purpose is to catch this month's real fix-list failures.
3. **Leaver handling with unusual activity detection.**
   - "Reassign" needs "a handover note"; "None go to Daniel, who is at capacity"; vault access and sign-in end automatically.
   - SuperAdmin catches "Sam Patel exported 38 client documents… Usual: under 5 a day", with "Look into it" (which pauses downloads) or "Mark as expected".

Also worth keeping: "Price to set; nobody quotes it" with exact penny rounding, the deletion list with its legal hold check, and the automation failure card ("resend waits until Daniel confirms the address with Tunde by phone").
