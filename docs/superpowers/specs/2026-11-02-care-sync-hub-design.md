# Care Sync Hub: Design Specification

**Date:** 2 November 2026
**Status:** Draft for review
**Working name:** Care Sync Hub (name can change)

---

## 1. Purpose

Care Sync Hub is one system that runs every client journey Care Sync Experts delivers, from the first CV review to registration and aftercare. It replaces scattered emails, folders and spreadsheets with a single place where:

- **Clients** always know which stage they are at, what we need from them, and what happens next.
- **Staff** know exactly what to do today, for which client, and nothing slips.
- **Directors** can see the whole business at a glance and grow it without losing quality.

### 1.1 What success looks like

1. A client never needs to email to ask "any update?" because the answer is always on their screen.
2. A new member of staff can pick up a client pack and know exactly where it stands within five minutes.
3. Every document, draft, comment, email and decision for a client is in one timeline.
4. No legal deadline (such as the 28 days to respond to a CQC Notice of Proposal) is ever missed.
5. Adding a new service or package means editing a template, not building new software.
6. Care Sync can take on many more clients with the same team, without quality dropping.

### 1.2 Decisions already made

| Decision | Choice |
|---|---|
| Build approach | Our own custom Care Sync platform, with connections to existing tools (email, calendar, and GoHighLevel if used) |
| Services covered | All of them: Domiciliary Care, Supported Living, full start up packages, single-element packages, tenders, aftercare, and later marketing |
| How applications are submitted | **Outside the Hub, by email.** The Hub prepares the submission, records that it was sent, captures the evidence and tracks everything that follows. It never submits to CQC itself. |
| Language | British English throughout, plain English for clients |

---

## 2. Who uses it

| Role | Who | What they can do |
|---|---|---|
| **Client owner** | The person who bought the package (usually the nominated individual or director) | See everything for their company, upload documents, review and approve drafts, book sessions, invite team members |
| **Client team member** | For example the proposed registered manager | Only what the owner shares, for example interview preparation and their own documents (CV, DBS, training) |
| **Consultant** | Care Sync staff member assigned to a client pack | Run the journey: request and check documents, write drafts, reply to feedback, log submissions and outcomes, send emails |
| **Quality reviewer** | Senior staff | Check drafts before they reach the client, sign off final packs |
| **Director / admin** | Care Sync leadership | All of the above plus assignment, templates, reporting, user management |

Clients and staff use different views of the same system. Clients never see internal notes, internal tasks or other clients.

---

## 3. The core idea: one engine, many journeys

Every service Care Sync sells becomes a **Journey template**. Every template is built from the same small set of parts, so the system stays simple even as the number of services grows.

### 3.1 Building blocks

| Part | Meaning | Example |
|---|---|---|
| **Journey** | One client's engagement on one service | "Bright Path Care Ltd: Domiciliary Care Full Package" |
| **Track** | A parallel line of work inside a journey | Registration, Business plan, Brand and website, Aftercare |
| **Stage** | A step on the client's tracker | Documents, Drafting, Your review, Submitted, Interview, Registered |
| **Requirement** | Something we need from the client, with rules | Enhanced DBS, 2 forms of ID, utility bill dated within the last 3 months |
| **Deliverable** | Something we produce for the client to review | Statement of Purpose, policy set, training plan, business plan, tender response |
| **Milestone** | Something that happened, with a date | Submitted to CQC, interview date set, Notice of Proposal received, Registered |
| **Deadline** | A date that matters, with a countdown | 28 days to make representations, tender closing date |
| **Session** | A booked meeting that counts against the package | Session 2 of 3: mock interview |
| **Task** | Internal work for staff | "Check DBS certificate", "Draft safeguarding policy" |

### 3.2 Templates are editable by Care Sync, not by developers

Directors can create or change a template inside the Hub: add a stage, add a required document, change the wording of a reminder, change the number of included sessions. Changes only apply to new journeys, so live clients are not disrupted. Each template has a version number.

### 3.3 Starting templates

| Template | Tracks |
|---|---|
| **Domiciliary Care: Full Package** | Registration, Business plan, Policies, Brand and website, Interview, Aftercare (12 months) |
| **Supported Living: Start Up Package** | Registration, Business plan, Policies, Brand and website, Interview, Aftercare (12 months) |
| **CQC Registration only** (Dom Care or Supported Living) | Registration, Policies, Interview |
| **Single element** | One track only, for example Policies only, Interview coaching only, Business plan only, CV review only |
| **Tender** | Tender (see section 9) |
| **Aftercare / ongoing support** | Monthly check-ins, inspection readiness |
| **Later:** CIW, RQIA, Ofsted, marketing retainer | Built from the same parts once the core is proven |

Supported Living and Domiciliary Care share most of their structure. The differences (for example supported living housing and tenancy arrangements) are extra requirements and deliverables set in each template, so the team controls them.

---

## 4. The client journey, stage by stage (CQC registration)

This is the default Registration track. Each stage shows on the client tracker with a plain-English explanation of what it means and what happens next.

| # | Stage | What happens | Who has the ball |
|---|---|---|---|
| 1 | **Welcome** | Client gets a magic-link login, a welcome video or message, and a short onboarding form (company details, service type, office type, proposed registered manager). Kick-off session booked (session 1 of 3). | Client |
| 2 | **CV review** | Client uploads the proposed registered manager's CV. Consultant reviews it, records gaps (experience, qualifications, training) and shares a short CV review with actions. | Care Sync, then client |
| 3 | **Your documents** | Smart checklist (section 5.2). Each item is uploaded, checked, and accepted or returned with a reason. | Client |
| 4 | **Drafting** | Consultant prepares the deliverables: Statement of Purpose, policies, training plan, business plan and any others in the package. Each passes the quality check before the client sees it. | Care Sync |
| 5 | **Your review** | Client reviews each draft in the Review Room, leaves comments and questions, and approves or asks for changes. | Client, then Care Sync |
| 6 | **Final pack sign-off** | Consistency check across the whole pack (section 10.3). Client gives a final approval of the complete pack. | Client |
| 7 | **Submitted** | Consultant submits by email outside the Hub, then logs the submission with the date and captured email (section 7.3). | Care Sync |
| 8 | **With CQC** | Tracks everything CQC sends: acknowledgement, requests for more information, DBS steps, returned applications. | Shared |
| 9 | **Interview** | Interview date logged; Interview Hub opens a countdown preparation plan (section 8). | Client, with Care Sync support |
| 10 | **Outcome** | Registered, or Notice of Proposal (with deadline handling, section 6.3), or withdrawn. | Shared |
| 11 | **Aftercare** | 12 months of guidance: monthly check-ins, first inspection readiness, policy review reminders. | Care Sync |

Stages can move backwards (for example CQC returns the application), and the tracker shows that honestly, with what is needed to move forward again.

---

## 5. What the client sees

### 5.1 Home screen: "Today"

The first screen a client sees answers four questions, in this order:

1. **Where am I?** A tracker showing all stages, with the current one highlighted.
2. **What do you need from me?** A short list of actions, each with one button ("Upload your utility bill", "Review your Statement of Purpose").
3. **What are you doing for me?** "Care Sync is drafting your policies. Expected by Friday 14 November."
4. **What is coming up?** Next session, next deadline, interview date.

If nothing is needed from the client, it says so clearly: **"Nothing needed from you right now. We will let you know as soon as there is."** That sentence alone removes most chasing emails.

A **readiness score** (for example "Registration pack: 78% ready") shows overall progress.

### 5.2 Smart document checklist

The checklist adapts to the client's answers instead of showing every possible document to everyone.

**Core identity and suitability (per person, for example the registered manager and nominated individual):**
- Enhanced DBS certificate
- 2 forms of photo or official ID
- 1 proof of address (for example a utility bill dated within the last 3 months)
- CV
- Training certificates

**Office evidence (branches on one question: "Where will your office be?"):**

| Answer | Required |
|---|---|
| Commercial office | Lease or licence agreement for the premises |
| Home office | Proof of legal occupancy (for example tenancy agreement, mortgage statement or title) **and** a letter of permission from the mortgage lender or landlord |

**Business and compliance:**
- Insurance quote
- Any other items set in the template (for example supported living housing arrangements)

**How each item works:**
- Each item shows *why* we need it and an example of a good one.
- Upload from phone (photo) or computer. Photos are straightened and converted to PDF automatically.
- Status: **Needed**, **Uploaded, being checked**, **Accepted**, **Please re-upload** (with the reason, for example "This bill is older than 3 months"), **Expiring soon**, **Not needed** (waived by staff with a note).
- The client only ever re-does the items that failed.

### 5.3 Review Room (feedback and questions on drafts)

Inspired by Teamwork's Proofs feature, built for documents.

- Client opens a draft in the browser; no downloads needed.
- They highlight any sentence and add a **comment** or a **question**. Questions are flagged so staff answer them first.
- When finished they press **Approve** or **Needs changes**, with an optional overall note.
- Every version is kept. The client can compare version 2 with version 3 and see exactly what changed.
- Staff reply in the same thread, mark comments as resolved, and publish the next version.
- A clear status per deliverable: **Drafting**, **Ready for your review**, **Changes in progress**, **Approved**.
- Final approved versions are locked and downloadable as Word and PDF.

This works the same for CQC packs, business plans, website copy and tender responses.

### 5.4 CQC tracker and outcome centre

A dedicated screen for everything to do with the regulator, written in calm, plain English:

| Event | What the client sees |
|---|---|
| Submitted | "Your application was submitted to CQC on 3 November 2026." |
| Acknowledged / reference received | Reference number stored and shown |
| More information requested | What CQC asked for, who is handling it, and the response deadline |
| Returned as incomplete | What was missing, what we are doing, and when it will be resubmitted |
| Interview date set | Date, time, format, and a link straight into the Interview Hub |
| Notice of Proposal to refuse | What it means, the date of service, a **28-day countdown** for written representations, and the plan (section 6.3) |
| Notice of Decision | What it means and the **28-day window** to appeal to the First-tier Tribunal |
| Registered | A celebration screen, the next steps for starting the service, and the move into Aftercare |

### 5.5 Interview Hub

See section 8.

### 5.6 Sessions and booking

- "You have **2 of 3** sessions left." The number comes from the package.
- Client picks a session type (for example Document review, Mock interview, General support) and a time from the assigned consultant's real calendar.
- Confirmation and reminder emails, with a video link added automatically.
- After the session, the consultant adds a short summary and actions, which appear in the client's timeline.
- Extra sessions can be offered for purchase when the included ones are used.

### 5.7 Messages

- Messages are attached to what they are about: a document, a draft, a stage. Nothing gets lost.
- A general "Ask us anything" thread for everything else.
- Every message is also sent by email, and email replies come back into the Hub (section 7).

### 5.8 Document vault

Everything the client has given us and everything we have produced, organised by track, with final versions clearly marked. Available for the full aftercare period and beyond, subject to the retention policy (section 13).

---

## 6. Notifications and deadlines

### 6.1 Channels

- **In the Hub** (always)
- **Email** (always, from a recognisable Care Sync address)
- **SMS or WhatsApp** (later phase, for urgent items only: deadlines, interview reminders, CQC decisions)

### 6.2 Events that notify the client

| Event | Timing |
|---|---|
| Welcome and login link | On journey start |
| Document requested | When added |
| Document reminder | After 3 days, then weekly (configurable), stops as soon as uploaded |
| Document accepted / please re-upload | When checked |
| Draft ready for review | When published |
| Review reminder | After 3 days without a response |
| Stage changed | When moved |
| Ready for final sign-off | When pack passes consistency check |
| Submitted to CQC | When logged |
| Any CQC event in section 5.4 | When logged |
| Interview reminders | 7 days, 1 day and morning of |
| Session booked / reminder | On booking, 1 day before, 1 hour before |
| Deadline reminders | See 6.3 |
| Weekly progress summary | Every Friday: what we did this week, what is next, what we need |

Clients can choose quiet hours and whether they want the weekly summary. They cannot switch off legal deadline alerts.

### 6.3 Legal deadline handling

When staff log a **Notice of Proposal** or **Notice of Decision**, they enter the **date of service** shown on the notice. The Hub then:

1. Calculates the 28-day deadline from that date and shows it to client and staff.
2. Creates internal tasks back-scheduled from the deadline (for example draft representations by day 14, client review by day 21, send by day 25).
3. Alerts the assigned consultant and a director at day 7, 14, 21 and 25, and every day in the final 3 days.
4. Escalates to a director if any internal task is overdue.

The countdown is a guide based on the date entered; staff are reminded to check the date of service on each notice.

---

## 7. Email: the backbone

Applications and most regulator contact happen by email, so the Hub is built around email rather than replacing it.

### 7.1 Sending emails to clients

- Staff send emails from inside the Hub using templates ("Documents received", "Draft ready", "Interview confirmed").
- Emails are sent from the staff member's own Care Sync mailbox (connected Google Workspace or Microsoft 365 account), so replies thread normally and look personal.
- Templates fill in the client's name, stage, outstanding items and dates automatically. Staff can edit before sending.
- Every email sent or received is saved on the client timeline.

### 7.2 Capturing incoming emails

Each journey has its own private Hub email address (for example `brightpath-dom-2611@in.caresynchub.co.uk`).

- Staff **CC or forward** any relevant email to it: CQC correspondence, client emails, insurer quotes.
- The Hub files the email and its attachments against the right client automatically.
- The Hub reads the email and **suggests** what it is: "This looks like an interview invitation for 18 November. Log it?" A person always confirms before any status changes or the client is notified. This prevents mistakes from wrongly read emails.

### 7.3 Submitting by email

Because the Hub never submits to CQC itself:

1. When the pack is signed off, the Hub builds a **submission bundle**: the final approved documents named and ordered consistently, plus a checklist of what must be included.
2. The consultant sends the submission from their own mailbox, CC'ing the journey's Hub address.
3. The Hub captures the sent email as evidence, and the consultant confirms "Submitted" with one click (the date fills in from the email).
4. The client is told immediately, and the stage moves to "With CQC".

If the Hub address was not CC'd, the consultant can log the submission manually and attach the sent email or a screenshot.

The same approach works for tenders submitted through council portals: the consultant or client uploads the portal confirmation as evidence.

---

## 8. Interview Hub

Opens as soon as an interview date is logged (and is available earlier for clients who want to start).

- **Countdown plan:** a day-by-day preparation plan from today to the interview date.
- **Question bank:** questions matched to the service type (Domiciliary Care or Supported Living) and the role being interviewed (registered manager, nominated individual), grouped by theme, with guidance on what a strong answer covers.
- **"Know your pack":** quick quizzes drawn from the client's own Statement of Purpose and policies, because interviewers ask about what the client has submitted.
- **Practice mode:** the client answers questions in writing or by voice; the Hub gives feedback on structure and coverage, which the consultant can review.
- **Mock interview booking:** one click to book a mock interview session (counts against the package).
- **Day-before checklist:** documents to have to hand, technology check for video interviews, what to expect.
- **After the interview:** client logs how it went and the questions they were asked. These feed the learning loop (section 10.4).
- Client owners can give the registered manager their own login with access only to the Interview Hub and their own documents.

---

## 9. Tenders

Tenders follow the same engine with their own template.

| # | Stage | What happens |
|---|---|---|
| 1 | **Opportunity** | Tender added (from the live tenders page, a client request, or found by staff): buyer, value, lots, closing date, portal link |
| 2 | **Go / no-go** | Quick readiness check against the tender's requirements; client confirms they want to bid |
| 3 | **Kick-off** | Client completes a tender questionnaire (service details, case studies, staffing, social value, policies) and uploads evidence |
| 4 | **Drafting** | Responses drafted question by question, each within its word limit, each with its scoring weight shown |
| 5 | **Client review** | Review Room: comments, questions, approve or needs changes per question |
| 6 | **Final sign-off** | Compliance check (all questions answered, word limits, attachments, declarations) |
| 7 | **Submitted** | Submitted through the buyer's portal; confirmation captured as evidence |
| 8 | **Clarifications** | Buyer questions logged with their deadlines |
| 9 | **Outcome** | Won / lost, scores and buyer feedback recorded |

**Back-scheduling:** when the closing date is entered, the Hub works backwards and sets internal deadlines (questionnaire due, first drafts due, client review due, final sign-off due), with a safety margin before the portal closes.

Won bids can trigger mobilisation support as a follow-on service.

---

## 10. Ideas that make the Hub stand out

### 10.1 "Who has the ball"
Every journey, stage, document and draft always shows whose turn it is: the client, Care Sync, or CQC / the buyer. Staff dashboards can filter "waiting on us" versus "waiting on client", so time is never lost on things nobody is actively working on.

### 10.2 Expiry watch
Each document can have an expiry or freshness rule (for example a utility bill within 3 months, an insurance quote's validity date). The Hub warns before something goes out of date, especially if it will expire before CQC is likely to look at it.

### 10.3 Pack consistency check
Before final sign-off, the Hub checks the whole pack for mismatches that commonly cause problems: the company name, registered office address, service type, registered manager name and service user groups should match across the Statement of Purpose, policies, business plan, application details and supporting documents. Mismatches are listed for the consultant to fix. (This uses Care Sync's existing pack alignment knowledge.)

### 10.4 The learning loop
Every real interview question, every CQC request for more information, every returned application reason and every tender feedback note is recorded and tagged. Over time this becomes Care Sync's own knowledge base: better question banks, a "common reasons for delays" checklist, and better first drafts. This is something competitors cannot copy.

### 10.5 AI assistance for staff
Care Sync already has AI skills for CV gap analysis, policies, Statements of Purpose, business plans, training plans, CQC application checks, interview preparation and tender writing. In the Hub these become buttons inside the relevant stage ("Generate first draft from onboarding answers", "Run CV gap analysis", "Check pack before sign-off"). A person always reviews and owns the output; nothing AI-generated reaches a client without passing the quality check.

### 10.6 Quality gate
A deliverable cannot be published to the client until a second person (quality reviewer) approves it. Directors can relax this per staff member once they are trusted. This protects Care Sync's reputation as the team grows.

### 10.7 Automatic chasing
The Hub chases missing documents and overdue reviews politely and automatically, then escalates to the consultant if there is still no response. Staff stop writing chaser emails by hand.

### 10.8 Aftercare that keeps clients
After registration, the Aftercare track runs for the 12 months included in the package: monthly check-ins, policy review reminders, first inspection readiness, and a clear offer of next services (tenders, inspection readiness, marketing). At registration the Hub also asks happy clients for a Trustpilot review and a referral.

### 10.9 Director dashboard
- Clients by stage and by consultant
- Average days spent in each stage (where things get stuck)
- Workload per consultant
- Upcoming legal deadlines across all clients
- Outcomes: registrations, refusals, tender wins and losses
- Revenue by package and stage (if payments are linked)

---

## 11. What staff see

### 11.1 "My day"
A single list for each consultant, ordered by urgency:
1. Legal deadlines
2. Client questions waiting for an answer
3. Documents to check
4. Feedback to action
5. Drafts due
6. Sessions today

### 11.2 Pipeline board
All journeys as cards in columns by stage, filterable by service, consultant and "who has the ball". Cards turn amber or red when a stage has run longer than its target time.

### 11.3 Client pack assignment
- A director assigns a journey (or one track, for example the policies) to a consultant.
- The workload view shows how many active journeys and tasks each person has before assigning.
- Reassigning moves all open tasks and keeps the full history, so handovers take minutes.

### 11.4 Client record
One page per client: company details, people, all journeys, the full timeline (emails, uploads, comments, milestones, sessions, notes), documents, and internal notes clients cannot see.

---

## 12. Easy to use: design principles

1. **One clear next action per screen.** Clients should never wonder what to do.
2. **Mobile first.** Many clients will upload documents and review drafts on their phone.
3. **No passwords for clients by default.** Magic-link login by email, with an optional password or passkey.
4. **Plain English.** No internal jargon; every stage and status explained in one sentence.
5. **Always show progress.** Tracker, readiness score and "who has the ball" on every relevant screen.
6. **Calm about bad news.** Refusals and returned applications are explained with what happens next, never just a status change.
7. **Accessible.** Meets WCAG 2.2 AA (contrast, keyboard use, screen readers, readable text sizes).
8. **Care Sync branding.** Uses the existing Care Sync logo, colours and assets.

---

## 13. Data protection and security

The Hub holds sensitive personal data, including identity documents and DBS certificates (criminal offence data under UK GDPR). Requirements:

- **UK hosting** for the database and file storage.
- **Encryption** in transit and at rest.
- **Role-based access:** clients see only their own company; client team members see only what is shared with them; staff see only clients they are assigned to unless they are directors.
- **Multi-factor authentication** for all staff accounts.
- **Audit log:** every view, download, upload, approval and status change is recorded with who and when.
- **Retention policy:** identity documents and DBS certificates are deleted or archived after a set period once the journey ends (period to be agreed with Care Sync's data protection lead). Clients are told what is kept and for how long.
- **Secure sharing:** download links expire; no documents sent as email attachments from the Hub unless staff choose to.
- A data protection impact assessment is completed before launch.

---

## 14. How it fits together (technical outline)

This is a recommended outline; it will be confirmed in the implementation plan.

| Part | Recommendation |
|---|---|
| Application | A single web application (TypeScript, Next.js) serving both the client and staff views, responsive for mobile |
| Database | PostgreSQL, hosted in a UK (London) region |
| File storage | Object storage in a UK region, with virus scanning on upload |
| Email out (notifications) | A transactional email service with good deliverability |
| Email out (staff emails) | Gmail or Microsoft 365 connection so emails send from staff mailboxes |
| Email in | Inbound email processing for each journey's Hub address |
| Calendar and video | Google Calendar or Microsoft 365 calendar connection, with automatic video links |
| Background jobs | Scheduler for reminders, chasers, deadline alerts and weekly summaries |
| AI | Claude, used through the existing Care Sync skills, for staff-side drafting and checks only |
| Integrations | GoHighLevel (optional): new paid clients create a journey automatically |

### 14.1 Main records

Organisation (client company), Person, Journey, Track, Stage, Requirement, Document (with versions and expiry), Deliverable (with versions, comments and decisions), Milestone, Deadline, Session, Task, Email and message threads, Template (journey, email, notification), Audit event.

### 14.2 When things go wrong

| Situation | Behaviour |
|---|---|
| Client email bounces | Consultant alerted; reminder shown in the Hub to update contact details |
| Inbound email cannot be matched to a client | Placed in a shared "unmatched" inbox for staff to file |
| Hub's reading of an email is wrong | No harm done: suggestions always need a person to confirm |
| Wrong milestone logged | Staff can correct it; the correction and reason are recorded in the audit log and the client is notified of the correction |
| Upload fails or file is unreadable | Client told immediately and asked to try again or use another format |
| Deadline task overdue | Escalated to a director automatically |
| Template changed mid-journey | Live journeys keep their template version; directors can choose to move a journey to the new version |

---

## 15. Testing approach

- Automated tests for every rule that matters: checklist branching, deadline calculation, permissions, reminders stopping when items are uploaded, quality gate enforcement.
- End-to-end tests of the full client journey in a browser (onboarding through registration) on desktop and mobile sizes.
- Permission tests proving clients can never see another client's data or internal notes.
- A pilot with 3 to 5 real clients and the full team before wider rollout, with feedback collected in the Hub itself.

---

## 16. Phases

Each phase gets its own implementation plan and delivers something usable.

| Phase | Delivers |
|---|---|
| **1. Foundations** | Logins and roles, client records, journey templates (Dom Care and Supported Living), tracker, smart document checklist with checking, staff assignment, "My day", email notifications, client timeline |
| **2. Review and email** | Review Room (comments, questions, approve, versions), quality gate, staff email sending with templates, inbound email capture, submission logging, CQC outcome centre with deadline handling |
| **3. Sessions and interviews** | Booking with session counts, calendar and video links, Interview Hub (countdown, question bank, practice, mock booking) |
| **4. Tenders and full packages** | Tender template with back-scheduling, brand and website and business plan tracks, aftercare track, single-element templates |
| **5. Intelligence** | AI drafting buttons, pack consistency check, expiry watch, learning loop, readiness score, director dashboard, weekly summaries |
| **6. Extras** | SMS and WhatsApp alerts, GoHighLevel connection, payments for extra sessions, CIW / RQIA / Ofsted templates |

---

## 17. Open questions for Care Sync

1. **Email system:** Does the team use Google Workspace or Microsoft 365 for Care Sync mailboxes?
2. **Submission by email:** Is it correct that the consultant sends the application by email and the Hub only records it? Are there any other parts of the process that must stay on email?
3. **Other regulators:** Do you currently deliver CIW, RQIA or Ofsted work that should be included in the first phases?
4. **Team size and volume:** Roughly how many staff, and how many active clients at once now and in 12 months?
5. **Retention period:** How long should identity documents and DBS certificates be kept after a journey ends?
6. **Payments:** Should clients pay (for example for extra sessions) inside the Hub, or does payment stay in your current system?
7. **GoHighLevel:** Is it your current CRM for leads and sales, and should a paid client in GoHighLevel automatically start a journey in the Hub?
