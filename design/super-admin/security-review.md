# Care Sync Hub: data protection and security review of the super admin design

**Scope.** I read sections 13, 14, 21, 41, 46, 49, 51, 55, 57, 60 and 61 of `/home/user/Assets/docs/superpowers/specs/2026-11-02-care-sync-hub-design.md`, plus the break-glass email in `2026-11-02-care-sync-hub-client-emails.md`. I read seven boards as text in `/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/hub-canvas/project/`: SuperAdmin, TeamCover, PortalWatch, Account, Security, PriceBook and FormBuilder. I also checked SignIn, ClientStates, EmailConnect, ClientsList and ManagerDash where they touch this topic. I did not edit any file.

**Biggest risks.**
1. Anyone at Care Sync who can open a client's email login can also sign in to the Hub as that client, and sign documents as them.
2. There is no screen for handling a personal data breach, even though the demo data already contains a likely one: a leaver exported 38 client documents on a Sunday night.
3. Break-glass is being used for routine leave cover, and the boards and spec give three different rules for who approves it.

---

## Legal time limits used in this review

| Duty | Time limit | Source |
|---|---|---|
| Report a personal data breach to the ICO | Without undue delay and, where feasible, within 72 hours of becoming aware. Not needed if the breach is unlikely to result in a risk to people. If late, give the reasons. The 72 hours are clock hours, so weekends count. | UK GDPR Art 33(1) |
| A processor tells its controller about a breach | Without undue delay | Art 33(2) |
| Record every breach, reported or not | Facts, effects and action taken | Art 33(5) |
| Tell the people affected | Without undue delay, where the breach is likely to be high risk. The exceptions are in Art 34(3). | Art 34(1) |
| Subject access, correction, erasure, restriction, portability, objection | Without undue delay and within one month of receipt. Can be extended by two further months for complex or numerous requests, if the person is told within the first month. Normally free. | Art 12(3) and 12(5); ICO right of access guidance |
| Pausing the clock while waiting for ID or clarification | ICO guidance allows it. The Data (Use and Access) Act 2025 puts it into law. **Check** that the commencement date has passed. | ICO guidance; Data (Use and Access) Act 2025 |
| Data protection complaints procedure (acknowledge within 30 days) | **Check** whether this part of the Data (Use and Access) Act 2025 has commenced | Data (Use and Access) Act 2025 |
| Record of processing activities | Required. The under-250-staff exemption does not apply, because the processing is not occasional and includes criminal offence data. | Art 30 and Art 30(5) |
| Data protection impact assessment | Required before high-risk processing. Consult the ICO if high risk remains after mitigation. | Art 35 and Art 36 |
| Written contract with every processor | Required | Art 28(3) |
| DBS certificates (criminal offence data) | Needs a Schedule 1 condition, and an appropriate policy document where Schedule 1 Part 4 requires one. **Check** which condition applies with the data protection lead. | Art 10; DPA 2018 s.10 and Schedule 1 |
| How long DBS certificate information is kept | DBS guidance for registered bodies says normally no longer than 6 months. **Check** whether it applies to Care Sync, which is not a registered body. Either way it is a useful benchmark. | DBS guidance |
| Finance records | 6 years for VAT and company tax records (HMRC); 3 years for a private company's accounting records. **Check**. | HMRC; Companies Act 2006 s.388 |
| Contract claims | 6 years. A sensible basis for keeping engagement letters and signature records. | Limitation Act 1980 s.5 |

---

## 1. What the current design already does well

**Vault**
- "Viewing a password requires a stated reason, and every view is logged" (s.21).
- "revealed only with a stated reason, hidden again after 30 seconds, and copyable without being shown. Every view is logged, and the client can see the log in their privacy dashboard" (s.41.3).
- The PortalWatch board puts this into practice: "Copy without showing", "Why do you need to see it? Reveal for 30 seconds", "Every view and copy is logged and visible to the client".
- "The preferred route is always to be added as a user ... rather than to hold a password" (s.21). PortalWatch shows it working: "Daniel is a user on Kemi's account ... No password held".
- "Logins never appear in notes, messages, emails, exports or AI tools" (s.41.3), and this is listed as a rule the super admin cannot switch off (s.51.4, rule 8).
- A "hand-back checklist at the end of every engagement: access removed, stored logins deleted, client told" (s.41.3).
- Email accounts Care Sync creates for a client are "created in the client's name and ownership from day one, with the client holding the recovery details and two-step verification" (s.41.4).

**Transparency to the client**
- "Every look is logged and shown to the client on their privacy page, including 'view as' and emergency (break-glass) access. Break-glass also sends the client an email the same day" (s.51.4, rule 3). Email 9.1 exists.
- The Account board shows entries in plain words, for example "opened your proof of address to check the date". The Security board explains UK storage, encryption, the vault, deletion and the ICO registration.

**Super admin safeguards**
- "Price changes, permission changes, data deletion and break-glass access need a second super admin to approve" (s.46.2).
- "Nobody approves their own request", and "break-glass access ends automatically after 4 hours" (s.60.3).
- SuperAdmin board: "Write a reason before you approve or decline", and "Every decision is written to the audit log with the reason."
- Permission changes show before and after. Invites expire after 7 days and need two-step login (TeamCover).
- A weekly super admin summary goes to both super admins.

**Deletion with legal hold**
- The SuperAdmin board lists every document to be deleted, with the client and the date retention ended.
- "Legal hold check: clear. None of the 3 clients has a legal hold, an open complaint, a regulator query or a payment dispute."
- "Deleted 7 days after approval, so it can still be stopped."
- "A record of the decision is kept, never the documents."

**Audit and alerts**
- "Entries cannot be edited or deleted."
- An unusual activity alert with a baseline: "exported 38 client documents (usual: under 5 a day)", plus a "paused Sam's downloads" action.
- "Failures are always shown here and to the owner. Nothing fails silently."

**Leavers**
- TeamCover checklist: "All of Sam's vault access ends Fri 6 Nov at 17:30, automatically"; "Sign-in stops Fri 6 Nov at 17:30"; every client reassigned with a handover note.

**Minimisation**
- "Redacted PDF: dates of birth, DBS numbers and ID numbers hidden" for partners (s.26.3).
- "Sensitive fields are masked by default for staff, revealing one is logged" (s.26.3, point 10).
- Voice notes "are deleted once transcribed and checked" (s.13).
- The mailbox connection files only CQC, CIW, RQIA and tender emails (s.41.1).
- Private client examples use "initials only" (FormBuilder).

**Baseline requirements**
- UK hosting, encryption in transit and at rest, staff MFA, a DPIA before launch (s.13).
- "daily backups with tested restores" (s.49.10).
- A data protection requests queue, a breach log "with the 72-hour reporting clock", the record of processing and the DPIA all named (s.49.6).

---

## 2. Gaps, ranked by risk

### Critical

**G1. Client account takeover through the vault-held mailbox.**
- Clients sign in with a magic link sent to their email. SignIn says: "We sent a link to amara@harbourlanecare.co.uk". That same mailbox's password is in Care Sync's vault: the Account board shows "amara@harbourlanecare.co.uk Connected" and "stored your business email login".
- So any staff member who can reveal or copy that login can sign in to the Hub as the client. They could then approve packs, use "Download everything", change contact details, or open DocuSeal signing links and sign as the client.
- This weakens the evidence value of every e-signature after the mailbox is connected. The client's two-step sign-in is "Off. Recommended for directors" (Security), and the phone stays signed in for 30 days (SignIn).
- **Control:** a client sign-in policy setting.
  - When the sign-in email is a vault-held mailbox, require a second factor on a device the client holds (SMS code to their mobile) for new devices.
  - Require the same factor again before signing, approving, "Download everything", or changing the email, phone or people on the account.
  - Turn on DocuSeal signer verification by SMS (**check** what DocuSeal supports).
  - The mailbox connection must never file or show Hub sign-in or DocuSeal emails.
  - Alert when a client session starts from a Care Sync network or a staff device.
- **Connects to:** SignIn (code step), Account and Security (two-step on and compulsory in this case), EmailConnect (state that sign-in and signing emails are never read), Sign (verification step), and the SuperAdmin alert list.

### High

**G2. No breach handling workflow, and the demo already contains a likely breach.**
- Sam Patel, who leaves on Friday, "exported 38 client documents on Sun 1 Nov at 21:40". The board offers only "Look into it" or "Mark as expected (handover copies)".
- Section 49.6 names a breach log, but no board has an incident record, the 72-hour clock, a decision record, a screen for telling the people affected, or incident contacts.
- Detection ran as a 06:00 batch the next day. Under Art 33(1) the clock starts when Care Sync becomes aware, so slow detection eats into the 72 hours.
- **Control:** an Incidents and breaches screen (screen H in section 3).
  - "Start breach assessment" appears on every unusual activity alert and every incident a member of staff reports.
  - The record captures the awareness time and runs a countdown to 72 hours. It holds a risk assessment, a "report to ICO: yes or no, with reasons" decision (Art 33(5) requires the record either way), the ICO reference, and a "tell the people affected: yes or no" decision under Art 34.
  - "Mark as expected" needs a reason, and a second super admin when the person involved is a leaver.
  - Bulk export alerts become real time.
- **Connects to:** a staff "Report a concern or incident" button on every staff screen, client email templates for telling affected people, the client's privacy page entry, and the staff Academy (s.48) for breach training.

**G3. Break-glass is used for routine cover, and approval rules conflict.**
- TeamCover: "Vault logins need break-glass (1 request is waiting in Super admin)" for planned leave.
- Section 46.1 says break-glass "alerts the other super admin". Section 46.2 says it needs "a second super admin to approve". On the board a consultant requests it and one super admin approves.
- Account tells the client "A director can step in only in an emergency", yet the person getting access is a consultant.
- Routine use makes the emergency alerts meaningless and trains staff to ask for them.
- **Control:**
  - Cover delegation on Team and cover includes vault reveal for the covered clients, limited to the leave dates and approved when the leave is set.
  - Break-glass is kept for genuine emergencies. The person can authorise it themselves with a reason when no approver can be reached. It has a 4 hour limit, an immediate alert to both super admins and the client, and a mandatory review within 1 working day.
  - Write one rule into s.46 and use it on every board.
- **Connects to:** the TeamCover cover card, the SuperAdmin approvals list, Account wording ("Who can see your information"), and email 9.1 wording ("A Care Sync director approved it").

**G4. Vault lifecycle is incomplete.**
1. "Copy without showing" needs no reason (PortalWatch logs "copied without showing" with no reason), but a copied password can be pasted anywhere. It should need the same reason as a reveal.
2. The weekly summary shows "41 logins revealed" in a week. That is high when the mailbox connection is meant to remove the need. Nothing alerts on reveals per person.
3. Section 41.1 lets the vault "hold the authenticator for that account". Holding a client's password and their two-step seed together gives full control of their account. This needs the strongest controls, or should be removed in favour of delegation.
4. Rotation is a reminder only. Nothing records whether the client actually changed the password at hand-back.
5. Staff type passwords in on PortalWatch, which implies the password reached them by phone or email. The client should enter it themselves (board 27), with staff entry as a logged fallback.
6. Old secrets live elsewhere. Past responses to the tender Google Form still hold portal passwords (s.55 only removes the question). There is also the logins spreadsheet and the interim 1Password vault.
- **Control:** a Vault control screen (screen C).
  - Reason required for both reveal and copy.
  - Reveal counts per person, with a threshold alert.
  - Entry fields: access method (user added, delegated, stored password, authenticator held), written authority with a link to the signed clause, review date and last rotation.
  - Hand-back states: requested, access removed, connection and tokens revoked, entry deleted, client confirmed the password changed (or declined, recorded).
  - A one-time "legacy secrets purge" task: Google Form responses, the spreadsheet, and moving 1Password into the Hub.
- **Connects to:** PortalWatch, EmailConnect, the client's privacy page (reveal and copy entries, plus "We handed back your logins on [date]; please change your password"), and the closing checklist (s.49.8).

**G5. The audit log is not complete or tamper resistant, and some access sits outside it.**
- The SuperAdmin log types are Vault, Unusual, Data, Prices, Automation, People, Forms and Approval. There are no sign-ins, document views or downloads, sensitive field reveals, exports, view-as, AI assistant use, or emails sent as the client. Section 13 requires "every view, download".
- Account shows view events, and s.51 says it is "the same audit log the super admin sees", so the two must match.
- "Entries cannot be edited or deleted" is a screen promise, not storage design.
- Developer and hosting access to the production database, plus tools such as n8n, Langfuse (AI prompt logs), Stirling PDF and RAGFlow (s.30), bypass the Hub's log.
- **Control:**
  - Event types: sign-in success and failure, two-step failure, session revoked, document viewed, downloaded or uploaded, field revealed, vault added, revealed, copied, edited or deleted, export, view-as start and stop, break-glass start and stop, sent as the client, AI request, role or permission change, retention change, legal hold, deletion run, rights request step, incident step, integration key change.
  - Storage: append-only with a hash chain, a daily copy to write-once storage outside the app's admin rights, and the log's own retention period.
  - A production access register for developers and suppliers, using just-in-time access that is itself logged.
- **Connects to:** Account "Every time we looked" (add "sent on your behalf" and "signed in to your email"), and the staff privacy notice, because the log monitors staff too (**check** ICO employment monitoring guidance).

**G6. Leavers, joiners and exports.**
- The leaver checklist covers only the Hub. Section 61 says "Google Workspace runs ... staff sign-in", so the Google account, Gmail delegation and Drive ownership must be handled there.
- Also missing: GoHighLevel, Xero, Stripe, DocuSeal, the Interview Preparation Hub, 1Password, the WhatsApp business device, revoking open sessions and tokens, returning devices, and wiping company data from phones.
- Access ends on the last day even while an export by that leaver is under investigation. There is no "suspend now".
- No permission grid column covers export or download. ClientsList has an "Export" button, and the "Everything pack (ZIP)" and spreadsheet export exist (s.26.3).
- Joiners: nothing checks a signed confidentiality agreement or completed data protection training before access to client data.
- **Control:**
  - A leaver checklist per system with owner and state, and a "Suspend now" button.
  - Export permission per role. Consultants get no bulk export. Bulk export needs approval and goes in an export register.
  - Joiner gates: confidentiality agreement signed, Academy data protection module passed, device check done. Vault access opens only after these.
- **Connects to:** TeamCover, ClientsList export, SuperAdmin alerts, and Academy (s.48).

**G7. Retention covers only ID and DBS, and deletion stops at the Hub.**
- The schedule exists only for ID and DBS. Section 46.1 promises "Retention periods per document type", but no board shows a schedule.
- Deletion in the Hub does not reach copies in Gmail and Drive (staff draft in Word or Google Docs), DocuSeal, GoHighLevel notes and call recordings, WhatsApp on staff phones, the Interview Preparation Hub, Langfuse prompt logs, or backups.
- DBS certificate images are kept until 12 months of aftercare end (s.55, question 5). CQC needs the number and issue date, not the image kept for a year or more after submission. Compare the DBS 6 month benchmark (**check**).
- GP medical reference forms (CIW and RQIA, Appendices E and F) are health data under Art 9, with no retention rule or Art 9 condition recorded (**check** with the data protection lead).
- Section 13 says "deleted or archived". Archiving is not deletion, so pick one.
- Routine deletions need a super admin approval each time. With only one super admin set up, this risks a backlog.
- **Control:** a Retention and deletion screen (screen F).
  - A versioned schedule per document type, with trigger, period, basis and what happens.
  - Deletion runs that list the other systems to clear, each with a tick.
  - Backup expiry stated.
  - Routine deletions inside the approved schedule run automatically with a 7 day notice. Dual approval is needed only for schedule changes or early or unscheduled deletion.
  - Proposed default: delete ID images and the DBS image once the regulator has finished its checks, keeping "seen by, on, type, DBS number and issue date". This is for the data protection lead to decide.
- **Connects to:** the client's privacy page "How long we keep things", which must read from the schedule rather than fixed text (Account and Security disagree today), the privacy notice version, and the closing checklist.

**G8. Rights requests have no screen and only cover the account holder.**
- "Download everything" serves the client company's account holder.
- There is nothing for other people, each with their own rights: the registered manager (Ruth), co-directors, referees, landlords (Tom Reid), GPs named on forms, prospects in GoHighLevel and the Tender Radar, and staff.
- "Download everything" by a director may include the registered manager's DBS, GP details and address history. Decide what each role's download contains (**check** with the data protection lead).
- **Control:** a Rights requests screen (screen G).
  - Fields: received date and channel, the person and their relationship to Care Sync, request type, identity checked, clock (one month, extension decision recorded within the first month), systems searched checklist, third-party redaction done, response sent and how.
  - A "Correct something we hold" request from the client page lands here.
- **Connects to:** the client page "Correct something we hold" and "Raise a concern", the public privacy notice contact route, and the staff "Log a request" button (requests arrive by phone, WhatsApp and email too).

**G9. Suppliers, processor contracts and data location.**
- The Security board says "Your files are kept on servers in the UK". Section 55 says "Client data is stored in the UK".
- Several suppliers are, or may be, outside the UK: GoHighLevel, Stripe, Xero, Google Workspace, WhatsApp (Meta), the AI provider (Claude, which s.14 uses for staff drafting with client data), Langfuse, the transactional email, SMS and speech-to-text providers, and DocuSeal cloud. **Check** each supplier's location and transfer mechanism, for example the UK Extension to the EU-US Data Privacy Framework for certified US companies, or the IDTA or UK Addendum.
- No register, no processor contract (DPA) tracking, and the SuperAdmin connections list covers only 12 systems.
- Partner access (AssuredBid, s.49.3) needs a data sharing or processor agreement.
- **Control:** a Suppliers screen (screen J).
- **Connects to:** Security wording ("Your Hub's database and files are in the UK; some of our trusted suppliers process data elsewhere under UK safeguards"), a public sub-processor list linked from the privacy notice, and the SuperAdmin connections list (one record per supplier, so health and compliance sit together).

### Medium

**G10. Records of processing, lawful bases, DPIA and consent wording.**
- There is no record of processing (Art 30). Nothing records whether Care Sync is controller or processor for each activity (**check**; likely controller for its consultancy, sales and billing).
- No Schedule 1 condition or appropriate policy document for DBS data, and no Art 9 condition for GP medical references.
- The DPIA is one line in the spec. High-risk items it must cover: mailbox monitoring and sending as the client, the vault and stored authenticators, AI drafting on client documents, criminal offence data.
- ClientStates asks the client to tick "I agree, continue" to the privacy notice and terms together. A privacy notice is information, not consent. Consent should be asked separately and only where it is the lawful basis, for example WhatsApp updates, call recording, marketing to sole traders, or holding an authenticator.
- **Control:** a Records screen (screen I) holding the record of processing, lawful basis per activity, DPIA register with review dates, and the appropriate policy document.
- **Connects to:** ClientStates first sign-in (split notice from consent), Account contact preferences (each consent with date and withdraw), and FormBuilder (see G14).

**G11. Sign-in, sessions and devices.**
- Section 46.1 lists "set session time-outs", but no screen shows them. There are no device or sign-in records for staff or clients.
- Staff sign in through Google Workspace, so the Hub's "enforce two-step login" depends on Google admin settings. The super admin screen should read Google's enforcement status, not assume it. The KPI says "All use two-step login".
- **Control:** a Sign-in and devices screen (screen B).
  - Suggested staff defaults: 30 minutes idle, 10 hours absolute, re-confirm before vault, export and approvals.
  - Suggested client defaults: 30 days on a known device, a fresh code for sensitive actions.
  - Device list with revoke. "Sign out everywhere" for clients.
- **Connects to:** Account ("Sign out of this phone" becomes a device list) and TeamCover (per person devices).

**G12. Access reviews.**
- None are designed.
- Managers see "All" clients in the grid, against s.13 "staff see only clients they are assigned to unless they are directors".
- Partner access, cover access and integration keys need periodic checks.
- **Control:** a quarterly access review (screen A).
- **Connects to:** TeamCover grid and the client's "Who can see your information" list.

**G13. Backups, restore tests and keys.**
- The board shows "Nightly backup done 02:00" only. There is no restore test record, recovery targets, backup location or retention, or encryption key management. The vault and sensitive fields need separate keys that a super admin cannot export.
- **Control:** a Resilience screen (screen K).
- **Connects to:** System health and the Security page ("encrypted").

**G14. Form builder has no data protection gate.**
- Questions are not tagged with a data category (personal, special category, criminal offence, credential). Adding a question that collects such data does not trigger a check, a retention tag or a privacy notice update.
- **Control:** a data category tag per question. Adding a special category, criminal offence or credential question needs data protection lead sign-off and updates the record of processing and the retention schedule.
- **Connects to:** FormBuilder version approval and the client's form help text ("why we ask").

**G15. Dual control cannot work today, and approval identity.**
- TeamCover shows super admin 2 as "Account set up at launch". PriceBook shows "2 Nov 2026: £8,500 + VAT, entered by Collins" with no second approval.
- The boards use an "acting as" switch for the second approver. In the product each approval needs its own signed-in account and a fresh two-step check.
- **Control:** a launch gate: two named super admins active, plus a sealed recovery account.

**G16. ICO registration claim is unconfirmed.**
- Security says "Care Sync Experts is registered with the ICO", but the number is still open (question 58).
- **Control:** a setting for the ICO registration number and renewal date. The Security page shows nothing until it is filled.

---

## 3. Proposed super admin section: "Security and data protection"

Top tiles, each one a link: next access review due; open rights requests (fewest days left); open incidents (hours left); last restore test; suppliers missing a processor contract; deletions due; super admins active (target 2).

**A. People, roles and access review** (extends TeamCover)
- Fields: person; role(s); client scope (assigned, covered with dates, all); vault rights; export rights; joiner gates (confidentiality agreement, training, device); start and end dates.
- Access review: reviewer, date, each grant marked keep or remove with a reason, sign-off.
- States: Invited, Active, Covering, Suspended, Leaving, Left.
- Review states: Due, In progress, Signed off, Overdue.

**B. Sign-in and devices**
- Policies: staff idle and absolute time-outs; client device period; actions that need re-confirmation; two-step status read from Google Workspace.
- Per person: devices (name, first and last seen, location, company or personal), recent sign-ins, failed attempts, "Revoke", "Sign out everywhere".
- Device states: Trusted, New, Revoked.

**C. Vault control**
- Per entry: client; system; access method; account owner; written authority (link, date); named roles; last reveal or copy (who, reason); review date; last rotation.
- Entry states: Active, Review due, Hand-back requested, Access removed, Deleted, Client confirmed change.
- Also on this screen: reveals per person this week with a threshold, authenticators held (target 0), and the legacy secrets purge task.

**D. Elevated access: break-glass and view-as**
- Fields: requester; client; scope; reason; start; auto end (4 hours); approver or "emergency, self-authorised"; client emailed (time); review by (1 working day); review outcome.
- States: Requested, Active, Ended, Reviewed, Misuse found (which opens screen H).
- View-as is read-only with a banner and only for clients the person may already see. The client sees an entry only for pages that showed their data.

**E. Audit log and alerts**
- Full event types (G5); filters by person, client, type and date; integrity check result ("chain verified 06:00"); exports of the log are logged.
- Alert rules, each with a threshold, on or off, and recipients: bulk export or download; out of hours; leaver in notice period; reveals per person; new country or device; repeated two-step failures; access to an unassigned client; client sign-in from a Care Sync device.
- Alert states: New, Looking into it, Expected (reason, second admin if a leaver is involved), Escalated to incident.

**F. Retention and deletion**
- Schedule table: document or data type, trigger, period, basis, action (delete or anonymise), systems to clear, version, approved by.
- Legal holds: scope, reason, placed by, review date, released by.
- Deletion runs: list of items, hold check, notice period, systems ticked off, backup expiry date, certificate of deletion.
- Schedule states: Draft, Awaiting second approval, Live.
- Run states: Scheduled, Stopped, Done, Partly done (a system not cleared).

**G. Rights requests**
- Fields: received (date, channel); person and relationship; type (access, correction, erasure, restriction, objection, portability, complaint); identity checked; due date (auto, one month); extension decided and told; clarification paused (**check** the Data (Use and Access) Act commencement); systems searched checklist (Hub, Gmail, Drive, GoHighLevel, Xero, DocuSeal, WhatsApp, Interview Preparation Hub, AI logs); redaction; response sent.
- States: Received, Verifying, In progress, Extended, Sent, Refused (with reason and right to complain to the ICO), Closed.

**H. Incidents and breaches**
- Fields: reported by and time; awareness time; 72 hour countdown; what happened; data types; approximate number of people and records; containment; risk assessment (likelihood, severity); report to ICO yes or no with reason; ICO reference and time; tell people yes or no with reason; message sent and when; clients told (where Care Sync acts as processor); supplier involved; lessons and actions; closed by.
- States: Reported, Assessing, Reported to ICO, Not reportable (reason kept), People told, Closed.

**I. Records**
- Record of processing per activity (purpose, people, data, lawful basis, Art 9 or Art 10 condition, controller or processor, suppliers, retention link, location).
- DPIA register (title, risk, measures, residual risk, owner, review date, status).
- Appropriate policy document (version, date).
- Privacy notice versions, published to the client page.

**J. Suppliers**
- Fields: supplier; purpose; data categories; special or criminal data (yes or no); people affected; where stored and processed; transfer mechanism; processor contract (date, link); security evidence; retention at supplier; deletion method; breach notice term; owner; review date; on public list (yes or no).
- States: Proposed, Approved, Review due, Blocked.
- Linked to the connection health list.

**K. Resilience**
- Backups: last run, location, encryption, retention, separate account.
- Restore tests: date, what was restored, time taken, against recovery targets, result, who.
- Keys: key set, purpose, last rotation, who can manage.
- States: OK, Overdue (no restore test in 90 days), Failed.

**L. Exports register**
- Fields: who; what; row or file count; purpose; approval; link expiry; downloaded (yes or no).
- States: Requested, Approved, Ready, Expired.

**M. Contacts and runbook**
- Data protection lead and deputy; both super admins; Google Workspace admin; hosting and developer on-call; cyber insurer; bank and Stripe; ICO helpline 0303 123 1113 and the online breach report form; Action Fraud 0300 123 2040 (**check** both numbers before go-live).
- A one-page runbook: first hour, first 24 hours, by 72 hours.
- A "last tested" date for a yearly tabletop exercise.

For about 8 staff, one data protection lead (for example a manager) owns screens F to M. The two super admins share the approvals.

---

## 4. Contradictions between the boards and the spec

1. **Break-glass approval.**
   - s.46.1: the request "alerts the other super admin".
   - s.46.2: "need a second super admin to approve".
   - SuperAdmin board: a consultant requests it and one super admin approves.
   - TeamCover: it is used for routine leave cover.
   - Account: "A director can step in only in an emergency".
   - Email 9.1: "A Care Sync director approved it".
2. **Who can see client data.**
   - s.13: assigned staff only, unless directors.
   - TeamCover grid: Manager "All", Client care "Contact and feelings", Sales clients "once the owner agrees", cover access.
   - Account: "Nobody else at Care Sync can open your documents or logins".
   - Security: "Your consultant, Grace and your coach. Anyone else needs a reason".
3. **Coach access.** Account says "Session notes only" and the TeamCover grid says "Sessions only". Security says the coach can see the client's files. Security also leaves out Divine (client care), whom Account lists.
4. **Retention.**
   - s.13: "deleted or archived after a set period".
   - s.55: kept "until the 12 months of aftercare end".
   - Security: deleted "when your 12 months of aftercare end, unless the law says".
   - Account: "deleted after our work ends".
5. **Connections.** s.46.1 lists Ordnance Survey, CQC data, HM Land Registry, BidSuite and Microsoft. The SuperAdmin board's "All 12 connections" (s.60.2) leaves these out. Neither list includes the AI provider, transactional email, speech-to-text, virus scanning, n8n, Langfuse or RAGFlow (s.14 and s.30).
6. **Audit log coverage.** s.13 requires "every view, download, upload". The SuperAdmin board has no view, download or sign-in types. Account shows view events, and s.51 claims it is "the same audit log the super admin sees".
7. **Super admins.**
   - s.46 and s.60.5: "managers hold the super admin accounts".
   - TeamCover: "Collins, Director, super admin 1", and super admin 2 "Account set up at launch".
   - The second approval promised in s.46.2, PriceBook and FormBuilder cannot happen yet. PriceBook shows the £8,500 price entered by Collins alone.
8. **Who changes prices.** PriceBook and s.46.1 say "Only a super admin changes a price". The SuperAdmin log and PriceBook history show the PIR change "Requested by Grace", and the TeamCover grid gives the onboarding lead Prices "View" only.
9. **Cover and the vault.** TeamCover says cover excludes vault logins. On PortalWatch, Daniel, covering Olu's client Riverside, writes Riverside's password into the vault.
10. **Written authority date.**
    - s.41.1: authority comes from the e-signed engagement letter at the start.
    - EmailConnect: "Agreed in the agreement you signed on 19 October".
    - PortalWatch: "Mark gave written authority on Fri 23 Oct, when the application went in". That is also the date the application was submitted, while the login was not in the vault, even though s.41.1 says submissions are sent from the client's mailbox inside the Hub.
11. **Roles.** s.46.1 and s.18.1 list finance, weekly update owner, tender writer and account owner. The TeamCover roles and grid have none of these, so finance's access to money and Xero is undefined.
12. **Data location.** Security says "Your files are kept on servers in the UK" and s.55 says "Client data is stored in the UK". Client data also goes to suppliers that may process outside the UK (s.14 AI, s.24.6 GoHighLevel, s.61 Stripe, Xero and Google). **Check** each supplier.
13. **Two-step for clients.** s.57.2 and Security make two-step sign-in optional ("recommended for directors"). That conflicts with the vault holding the same mailbox that receives sign-in links (G1).
14. **Leaver access.** s.46.1 promises "access removed everywhere" and "mailbox connections handed to the new owner". The TeamCover checklist covers only the Hub, and does not show mailbox connections being handed over.
15. **Unrelated to data protection, but found:** s.51.4 rule 2 says "No time estimates", while s.57.3 says "Every page shows a time estimate".
16. **Harbour Lane's stage.** Account shows Daniel using Harbour Lane's email login on 22/10 while, on demo day (s.60.1), Harbour Lane is still in onboarding with Grace before handover. This may only be because client screens show different stages (s.60.1). If not, it breaks "work stays locked until a manager approves".
