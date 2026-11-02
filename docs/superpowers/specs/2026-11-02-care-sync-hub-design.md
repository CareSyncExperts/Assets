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
| **Client team member** | For example the proposed registered manager | Only what the owner shares, for example their own documents (CV, DBS, training) and interview dates |
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
| 6 | **Final pack sign-off** | Consistency check across the whole pack (section 10.3). Client gives a final approval of the complete pack with an e-signature (section 10.10). | Client |
| 7 | **Submitted** | Consultant submits by email outside the Hub, then logs the submission with the date and captured email (section 7.3). | Care Sync |
| 8 | **With CQC** | Tracks everything CQC sends: acknowledgement, requests for more information, DBS steps, returned applications. | Shared |
| 9 | **Interview** | Interview date logged; client is reminded and given a button to log in to the separate Interview Preparation Hub (section 8). | Client, with Care Sync support |
| 10 | **Outcome** | Registered, or Notice of Proposal (with deadline handling, section 6.3), or withdrawn. | Shared |
| 11 | **Aftercare** | Client receives their Registration File (section 10.14). Then 12 months of guidance: monthly check-ins, first inspection readiness, policy review reminders. | Care Sync |

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

**Core identity and suitability (per person, for example the registered manager and nominated individual).** These follow Care Sync's existing onboarding gates (section 18.2):
- Identity: enhanced DBS (number and issue date verified, certificate image received), **or** three valid IDs where there is no enhanced DBS
- Proof of address (for example a utility bill dated within the last 3 months)
- CV covering age 16 to the present, with every gap explained
- Professional registration details, checked against the public register
- References and GP details
- Training certificates

**Office evidence (branches on one question: "Where will your office be?"). The address evidence gate is a hard gate: no application work starts until it passes.**

| Answer | Required |
|---|---|
| Commercial office | The office lease or licence agreement |
| Home office, mortgaged | Lender's permission **and** the title deed |
| Home office, rented | Tenancy agreement **and** the landlord's written permission for administrative office use |
| Home office, owned outright | The title deed |
| Virtual office or PO box | Not accepted. The client is told why and shown the options |

The address on the evidence must match the address on the onboarding form. A mismatch fails the gate with the exact reason shown.

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
| Interview date set | Date, time, format, and a button to log in to the Interview Preparation Hub |
| Notice of Proposal to refuse | What it means, the date of service, a **28-day countdown** for written representations, and the plan (section 6.3) |
| Notice of Decision | What it means and the **28-day window** to appeal to the First-tier Tribunal |
| Registered | A celebration screen, the next steps for starting the service, and the move into Aftercare |

### 5.5 Interview preparation

A link only. See section 8.

### 5.6 Sessions and booking

- "You have **2 of 3** sessions left." The number comes from the package.
- Client picks a session type (for example Document review, Mock interview, General support) and a time from the assigned consultant's real calendar.
- Confirmation and reminder emails, with a video link added automatically.
- After the session, the consultant adds a short summary and actions, which appear in the client's timeline.
- Extra sessions can be offered for purchase when the included ones are used.

### 5.7 Messages

- Messages are attached to what they are about: a document, a draft, a stage. Nothing gets lost.
- A general "Ask us anything" thread for everything else (all the ways to ask are in section 5.9).
- Every message is also sent by email, and email replies come back into the Hub (section 7).

### 5.8 Document vault

Everything the client has given us and everything we have produced, organised by track, with final versions clearly marked. Available for the full aftercare period and beyond, subject to the retention policy (section 13).

### 5.9 Asking questions: clients

Clients should never feel stuck or unsure who to ask. There are four ways to ask, all ending up in the same place for staff.

1. **"Ask about this" on everything.** Every document, draft, stage and deadline has a small "Ask about this" button. The question is automatically linked to that item, so the consultant sees exactly what the client is looking at and never has to ask "which document do you mean?".
2. **Sync Assistant (instant answers, any time).** A help assistant inside the Hub that answers common questions straight away, day or night, for example "Where do I get an enhanced DBS?", "Why do you need a utility bill?", "What happens after you submit?", "When is my next session?".
   - It only answers from Care Sync's approved help content and the client's own journey status. It does not give advice on the client's specific application.
   - If it is not sure, or the question is about the client's case, it says so and passes the question to their consultant with one tap, including the conversation so far.
   - Every answer shows "Was this helpful?". Unhelpful answers are reviewed by staff and the help content is improved.
3. **Ask your consultant.** A direct question to the assigned consultant. The Hub shows the promised reply time (for example "We reply within 1 working day") and the question appears in "who has the ball" until it is answered.
4. **Request a call back.** For anything easier to talk through. The client picks a few suitable times; the consultant confirms one. Call backs do not use up the included sessions unless staff decide they should.

**Questions become help content.** When staff answer a question that other clients are likely to ask, they can tick "Add to help" and the answer (with client details removed) becomes part of the Sync Assistant's approved content after a director approves it. The Hub gets smarter every week.

**Short "what happens now" guides.** Each stage has a two-minute guide or video explaining what happens in that stage, what the client needs to do and how long it usually takes.

### 5.10 Making it easier for clients

- **Tell us once.** Company name, addresses, people, service type and other details are entered once in a company profile and reused everywhere: forms, drafts, the submission bundle and the consistency check. Clients never type the same thing twice, and staff never copy and paste it into documents.
- **Reply to upload.** Clients can simply reply to a reminder email with the document attached. The Hub files it against the right item automatically, and staff confirm it.
- **Voice answers.** Busy clients can answer onboarding and questionnaire questions with a voice note on their phone. The Hub turns it into text for the consultant, and the client can check the text.
- **Save and come back.** Every form saves as the client goes, so they can stop and continue later on any device.
- **Easy to read.** Adjustable text size, read-aloud support and plain-English explanations on every screen.

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
| Your question has been answered | When a consultant replies |
| Document to sign | When an engagement letter or final sign-off is ready, with a reminder after 2 days |
| How did we do? | When a stage finishes |
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

## 8. Interview preparation (link to the separate Interview Preparation Hub)

Interview preparation content does **not** live in Care Sync Hub. Care Sync already has a separate Interview Preparation Hub with its own login, and that is where clients learn and practise. Care Sync Hub only points clients to it.

What Care Sync Hub does:

- Shows a clear **"Go to Interview Preparation Hub"** button that opens the Interview Preparation Hub's login page in a new tab.
- Shows the button only to clients whose package includes interview preparation.
- Sets up the client's Interview Preparation Hub account automatically when the interview stage starts, and emails their login details, so no one on the team has to do it by hand (section 10.13).
- Makes the button prominent when an interview date is logged, and includes it in the interview confirmation and reminder emails (7 days, 1 day and the morning of).
- Keeps the interview date, time and format on the client's tracker and in the CQC outcome centre.
- Lets the client book one of their included sessions with a consultant if they want help before the interview (section 5.6).

What Care Sync Hub does not do:

- No question banks, practice, quizzes or learning materials.
- No copy of the Interview Preparation Hub's content.

The link address is set once by a director in the Hub's settings, so it can be changed without developer work.

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
Every CQC request for more information, every returned application reason and every tender feedback note is recorded and tagged. Over time this becomes Care Sync's own knowledge base: a "common reasons for delays" checklist and better first drafts. This is something competitors cannot copy.

### 10.5 AI assistance for staff
Care Sync already has AI skills for CV gap analysis, policies, Statements of Purpose, business plans, training plans, CQC application checks and tender writing. In the Hub these become buttons inside the relevant stage ("Generate first draft from onboarding answers", "Run CV gap analysis", "Check pack before sign-off"). A person always reviews and owns the output; nothing AI-generated reaches a client without passing the quality check.

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
- Staff time and profitability per package (section 10.12)
- Client feedback scores by stage and consultant (section 10.11)

### 10.10 E-signatures for approvals and the engagement letter
- At the start, the client signs the engagement letter and terms inside the Hub before work begins.
- At final pack sign-off, the client signs to confirm they have reviewed and approved the content that will be submitted.
- Each signature records the name, date, time and the exact document version signed, stored with the journey. If anything is questioned later, there is a clear record of what the client approved and when.
- Recommended tool: DocuSeal (Care Sync already has guidance for using it), connected to the Hub so signing happens without leaving the page.

### 10.11 One-tap feedback at the end of each stage
- When a stage finishes, the client is asked one question: "How did we do on this stage?" with three faces (happy, neutral, unhappy) and an optional comment.
- An unhappy or neutral answer alerts the consultant and a director straight away, so problems are fixed weeks before they become complaints or poor reviews.
- Scores appear on the director dashboard by stage and consultant.

### 10.12 Light time tracking
- Staff can start a timer on any client task, or add time afterwards in a few seconds.
- Time is totalled per journey, track and package.
- Directors see which packages are profitable, which are underpriced, and how long each stage really takes. This guides pricing and hiring as Care Sync grows.
- Time is never shown to clients.

### 10.13 Automatic Interview Preparation Hub accounts
- When the interview stage starts (or when a director chooses), the Hub creates the client's account in the Interview Preparation Hub and emails the login details.
- If the Interview Preparation Hub cannot accept automatic account creation, the Hub creates a task for a staff member to set it up, with the client's details ready to copy.

### 10.14 The Registration File
- When a client is registered, the Hub produces a neatly organised, Care Sync branded file of every final document: application evidence, Statement of Purpose, policies, training plan, business plan, insurance, signed approvals and the CQC registration confirmation.
- Delivered as a single download (organised folders plus an index PDF) and kept in the document vault.
- A professional finish that clients value and keep, and a natural starting point for inspection readiness.

### 10.15 "Going quiet" alert
- If a client has not logged in, uploaded or replied for a set number of days (for example 10) while the ball is with them, the consultant gets a prompt to phone them.
- Catches clients who are stuck, overwhelmed or unhappy before the journey stalls.

### 10.16 Holiday and absence cover
- When a consultant is on leave, their clients and tasks are automatically routed to a named cover colleague, and clients see who is covering.
- When the consultant returns, they get a short summary of everything that happened while they were away.

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

### 11.5 Asking questions: staff

Staff should never be stuck, and the answer to a question should only ever need to be given once.

1. **Internal comments with @mentions.** On any client, document, draft or task, staff can leave an internal comment and @mention a colleague. Internal comments are clearly marked and never visible to clients.
2. **"Ask a senior".** A staff member can raise a question to the senior team (for example "Client has a council tenancy for a home office: what evidence do we accept?"). Questions go into a shared queue with a reply time target, linked to the client item, so seniors see the full context.
3. **The Care Sync Playbook.** Each stage in every template has a built-in "how we do this" guide for staff: the steps, the standards, examples of good work, and common mistakes. It appears right next to the work, not in a separate folder.
4. **Answers become the Playbook.** When a senior answers a question that others will face, they tick "Add to Playbook". Over time the Playbook captures how Care Sync works, which makes new starters productive quickly and keeps quality consistent.
5. **Staff Assistant.** An AI assistant for staff that answers from the Playbook, the templates and past answers ("How do we word a reminder for a missing lease?", "What does our training plan usually include for supported living?"). It shows where each answer came from and suggests "Ask a senior" when unsure.
6. **"I'm stuck" flag.** One click on any journey tells a director that the consultant needs help, with a short note. Stuck journeys appear at the top of the director dashboard.

### 11.6 Making it easier for staff

- **Saved replies.** Approved replies for common client questions and situations, inserted with a couple of clicks and personalised automatically.
- **Bulk actions.** For example, send the same reminder to every client waiting on a DBS, or move several journeys at once.
- **Handover notes.** When a journey is reassigned, the Hub writes a summary of where it stands, what is outstanding and any client preferences, for the new consultant.
- **Practice client.** A sandbox client where new starters can safely try every part of the journey before working with real clients.
- **Works on mobile.** Staff can check documents, answer questions and approve drafts from their phone.
- **Keyboard shortcuts** for staff who work in the Hub all day.

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
- **AI assistants:** the Sync Assistant only uses approved help content and the asking client's own journey status; it can never see other clients' data. The Staff Assistant only sees what that staff member is allowed to see. Conversations are logged.
- **Voice notes** are deleted once transcribed and checked, unless the client asks to keep them.
- **E-signature records** are kept for as long as the related journey records.
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
| AI | Claude, used through the existing Care Sync skills, for staff-side drafting and checks, the Sync Assistant (approved help content only) and the Staff Assistant (Playbook only) |
| E-signatures | DocuSeal, connected to the Hub |
| Voice notes | Speech-to-text transcription, with the client able to check the text |
| Integrations | GoHighLevel (optional): new paid clients create a journey automatically |

### 14.1 Main records

Organisation (client company) with its company profile, Person, Journey, Track, Stage, Requirement, Document (with versions and expiry), Deliverable (with versions, comments and decisions), Milestone, Deadline, Session, Task, Email and message threads, Question (client or staff, with status and linked item), Help article and Playbook entry, Signature, Stage feedback, Time entry, Template (journey, email, notification, saved reply), Audit event.

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

## 16. Phases (first draft, replaced by section 25)

Each phase gets its own implementation plan and delivers something usable. Section 25 replaces this table now that the current operation has been reviewed.

| Phase | Delivers |
|---|---|
| **1. Foundations** | Logins and roles, client records and company profile ("tell us once"), journey templates (Dom Care and Supported Living), tracker, smart document checklist with checking, staff assignment, "My day", email notifications, client timeline, "Ask about this" and "Ask your consultant", internal comments with @mentions, save and come back |
| **2. Review and email** | Review Room (comments, questions, approve, versions), quality gate, e-signatures (engagement letter and final sign-off), staff email sending with templates and saved replies, inbound email capture and "reply to upload", submission logging, CQC outcome centre with deadline handling |
| **3. Sessions and interviews** | Booking with session counts, call back requests, calendar and video links, interview date tracking and reminders, link to the Interview Preparation Hub with automatic account setup, stage feedback |
| **4. Tenders and full packages** | Tender template with back-scheduling, brand and website and business plan tracks, aftercare track, single-element templates, Registration File |
| **5. Intelligence** | AI drafting buttons, Sync Assistant, Staff Assistant, Playbook and "Ask a senior", pack consistency check, expiry watch, learning loop, readiness score, time tracking, going quiet alerts, director dashboard, weekly summaries |
| **6. Extras** | SMS and WhatsApp alerts, voice answers, holiday cover routing, practice client, GoHighLevel connection, payments for extra sessions, CIW / RQIA / Ofsted templates |

---

## 17. What we learnt from Care Sync's current operation

Reviewed on 2 November 2026 from the Companies folder in Google Drive: the Client Control Register, the Client Folder Standard Template, the tender outreach folder and the Client Tender Onboarding deck. No client names or personal details are copied into this specification.

**What already works and must be kept:**
- Hard onboarding gates: nothing starts until form, address, identity or DBS, CV and professional registration checks pass.
- A clear weekly rhythm: Monday review, Tuesday and Wednesday client updates by named owners, Thursday chasing, Friday manager QA.
- Evidence rules: "Do not mark Sent without evidence", CQC dates and references only from the acknowledgement, never guessed.
- Lifecycle rules: an interview pass is not completion; rejected applications stay active with a recovery plan; archiving needs manager approval; history is never deleted.
- "No silent or unowned client": every client always has a named owner.
- A strong tender delivery method: a structured onboarding meeting, a timeline planned back from the closing date, lot-by-lot decisions, an evidence-led approach and client sign-off of every promise.

**What the current tools make hard:**
- Status lives in several places: spreadsheet tabs, Drive folder colours ("not visually verified" appears often) and inboxes.
- On the register snapshot of 19 July 2026: 17 client updates overdue, 26 submitted cases missing a submission date and CQC reference, 49 overdue next deadlines.
- Free text drifts into status columns, so counts and dashboards become unreliable.
- Tender provider research depends on a browser automation that often stops ("not run"), and results move to GoHighLevel by hand.
- Client logins created by Care Sync are kept in a spreadsheet. This is a security risk that the Hub's secure vault replaces (section 21).

The Hub keeps every good rule above and enforces it automatically, with structured fields instead of colours and free text.

---

## 18. Delivery operating model (built from Care Sync's rules)

### 18.1 Roles in the Hub

| Role | Current equivalent | Accountable for |
|---|---|---|
| **Onboarding lead** | Owns the Onboarding Queue and Form QA | Onboarding form, gate checks, chasing missing information, readiness for handover |
| **Case owner** | Owns CQC delivery | Milestones, risk decisions, rejection and resubmission, interview readiness, closure evidence |
| **Weekly update owner** | Updates assigned clients on a set weekday | The weekly client update and its evidence |
| **Manager** | Friday review and approvals | Handover approval, QA before resubmission, overdue work, closure approval |
| **Interview coach** | Interview coaching sessions | Mock interviews and preparation status |
| **Tender writer and second reviewer** | Tender team | Drafting and the second consultant review |
| **Sales rep and account owner** | Sales team | Outbound tender sales, inbound enquiries, growth (section 24) |

One person can hold several roles. Every client always shows its case owner and weekly update owner; a client with either missing appears in red on the manager's dashboard.

### 18.2 Onboarding gates (hard gates)

Payment is complete before a client enters onboarding. The Hub creates the client record, client ID and onboarding checklist automatically.

| Gate | What must be true |
|---|---|
| Form | Onboarding form received for the correct company branch and service type |
| Company | Companies House record verified; every director listed |
| CVs | CVs for every director, the registered manager and the nominated individual (if different), each covering age 16 to the present with gaps explained |
| People | Registered manager and nominated individual confirmed, and whether they are the same person (flagged for a specialist check) |
| Professional registration | Status, body and number recorded and verified on the public register |
| Identity | Enhanced DBS verified, or three valid IDs |
| References and GP | Complete |
| Address evidence | Section 5.2 office rules pass and the address matches the form |

How it behaves:
- Each gate shows **Pass**, **Fail** with the exact issue, or **Not checked**.
- A failure sets "Resubmission requested" with a recheck date. The client sees exactly what to fix, in plain English, on their checklist.
- The onboarding lead is alerted **once** per new or materially changed failure, never repeatedly for an unchanged one.
- When every gate passes, the onboarding lead marks it ready. Only a **manager** can approve handover, and handover requires a named case owner and weekly update owner.

### 18.3 Application stages and rules

| Stage | Moves on when (evidence required) |
|---|---|
| Onboarding and information collection | Manager approves handover |
| In progress | Pack components reach client review |
| Waiting for client information | Shown whenever the client holds the ball; the stage itself does not change |
| Client review or approval | Client e-signs the final pack |
| Submitted to CQC | Submission date and CQC reference entered **from the acknowledgement** (captured email or upload) |
| Interview scheduled | Invitation saved with date, time and method |
| Interview completed | Outcome, discussion and actions recorded the same day |
| CQC registration decision pending | Formal decision received |
| Registration issued | Final update sent, handover, finance and admin checks done |
| Closure approved, then archived | Manager approval; history kept for ever |
| Rejected or returned, resubmission required | Risk set to Critical automatically; recovery plan due within 2 working days |
| Resubmission in progress | Corrections done; manager QA approval required before resubmitting |
| Resubmitted to CQC | New submission date and evidence; original rejection history kept |

Rules enforced by the Hub:
- No stage moves on without its evidence. The button stays disabled and says what is missing.
- An interview pass never completes a project.
- A rejected client is never archived or left without an owner.
- **Pack components** are tracked separately, each with its own status (Not started, Drafting, Ready for QA, With client, Complete): Policies, Provider form, Registered manager form, Statement of Purpose, CQC interview portal access.
- **Deadline sequence:** every client has a current internal action and the following action, each with a due date. Ticking the current one done promotes the next automatically.
- **Risk level:** Low, Medium, High or Critical, set by rules (for example rejection makes it Critical) and adjustable by the case owner with a reason.

### 18.4 Service types (from the register)

DOM, SL, DOM and SL, SL add-on to DOM, Interview preparation, Tender writing, Website, Website and DOM, Website and SL, Other. Each maps to a journey template (section 3.3). "To confirm" is allowed only during onboarding and blocks handover.

### 18.5 The weekly update, built in

The Hub runs Care Sync's weekly rhythm for staff:

| Day | Who | What the Hub does |
|---|---|---|
| Monday | Weekly update owners | "Review" list of assigned clients with everything that changed since last week |
| Tuesday and Wednesday | The owner for that day | "Updates to send today", each already drafted |
| Thursday | Weekly update owners | Chase list: every client holding the ball, with promised dates |
| Friday | Manager | QA list: overdue updates, high-risk clients, weak evidence, next week's queue |

**The update composer** drafts each client's update from live Hub data, in Care Sync's nine-part standard:
1. Current stage, in plain English
2. Completed this week
3. Policies progress
4. Application forms progress (provider and registered manager)
5. Statement of Purpose status
6. CQC interview portal status
7. What the client needs to do, and by when
8. What Care Sync will do next, and the target date
9. Date of the next update

The owner checks and edits it, then sends it. It goes to the client by email and appears in their Hub timeline. The sent date, method and evidence are recorded automatically. An update can never be marked sent without that evidence. The manager's QA status (Approved or Needs changes) is recorded on Friday. Overdue updates turn red on the owner's "My day" and the manager's dashboard.

### 18.6 Client document structure

Each client's vault follows the existing Client Folder Standard Template, so staff find everything where they expect it:

00 Client and agreement · 01 Onboarding information · 02 CQC application forms · 03 Statement of Purpose · 04 Policies and procedures · 05 Business plan and financials · 06 Premises and supporting evidence · 07 CQC interview preparation · 08 Quality assurance and final pack · 09 Submission evidence and CQC correspondence · 10 Weekly client updates

During migration the Hub can mirror files into each client's existing Drive folder, so nothing changes for staff until they are ready.

---

## 19. Tenders: the complete system

Tenders have two sides: **finding and selling** (sales, section 24) and **writing and winning** (delivery, this section). Both use one shared Tender Radar.

### 19.1 Tender Radar (replaces the outreach spreadsheets)

1. **Ingest:** new tenders arrive daily from BidSuite, Find a Tender and the council portals Care Sync uses (ProContract, In-Tend, Atamis, Adam, Delta eSourcing), plus Sell2Wales and eTendersNI.
2. **Approve:** a staff member approves a tender for outreach with one click. The fields match the current Approved Tenders Queue: title, buyer and local authority, region, regulator, care setting, lots, closing date, clarification deadline, estimated value, link, eligibility notes.
3. **Research providers, server side and reliable:** the Hub finds providers in and around each lot area using the official CQC register (CQC location ID, rating and date, services, service user bands, registered manager, listed phone number), then adds contact details from approved directories. No browser automation, so no "not run" days. Each provider gets a confidence level and a recorded data source.
4. **Screen and check:** TPS and CTPS screening, the do-not-contact list, the conflict check (other clients on the same tender or lot, and whether Living Plus Care Services is bidding) and the green, amber and red triage.
5. **Hand to sales automatically:** contacts and call tasks are created in the Hub and synced to GoHighLevel. Nothing is moved by hand. Existing clients in the area are shown first.

### 19.2 The tender delivery journey

Built from the Client Tender Onboarding deck. All timings are working days, planned back from the closing date taken from the portal itself (if two documents disagree, the earlier time is used).

| When | Milestone | Who |
|---|---|---|
| Day 0 | Agreement signed and deposit paid; tender journey opens | Sales |
| Day 0 to 1 | Onboarding meeting (about 75 minutes), using the six-part agenda | Bid lead, note taker, client decision maker, registered manager, finance |
| Day 2 | Tender onboarding form complete | Client |
| Day 5 | Documents, evidence and case studies with Care Sync | Client |
| 10 days before close | First drafts to the client | Writer, after second review |
| 8 days before close | Client comments back | Client |
| 5 days before close | **Promises and price signed off** by the client | Client |
| 2 days before close | Submitted. Never on the last day | Bid lead |

If the deadline is tighter, the Hub compresses the plan but keeps the order, and flags anything under 15 working days for Collins.

### 19.3 What the tender workspace holds

- **Meeting record:** whether note-taking consent was given, attendees, the single named decision maker, and the agreed draft turnaround time.
- **Three accounts checklist:** Central Digital Platform registration and share code received; tender portal registered and opted in to this tender; Care Sync's bid lead added as a portal user (the preferred route); the named person who reads the portal inbox every working day.
- **Lots decision:** for each lot, four checks (fit, area, evidence, capacity) and a recorded yes or no with the reason. A lot failing two checks is flagged "usually a no for now".
- **Reusable tender profile:** the onboarding form (about 45 minutes the first time, 10 for later tenders) captures company, regulator, services, key people, contract examples, workforce, partnerships and documents once, for every future bid.
- **Evidence library per client:** contract examples from the last 3 years (who, what, how many people, hours, value, dates, outcomes), anonymised case studies, referees with permission recorded, and standard documents (accounts, organisation chart, CVs, CQC certificate and latest report, Statement of Purpose, insurance with levels and expiry dates, council quality monitoring reports, ICO number, Data Security and Protection Toolkit status, Cyber Essentials, ISO certificates). Expiry dates feed the expiry watch.
- **Question-by-question drafting** in the Review Room, showing each question's word limit, weighting and the buyer's scoring bands, with a live word count. Every answer gets a second consultant review sign-off before the client sees it.
- **Promise register:** every commitment written into the bid ("every new carer shadows for three shifts") is listed separately, and the client approves each one. If the bid wins, the promise register becomes the contract mobilisation and compliance checklist.
- **Clarification log:** questions drafted with the client, submitted through the portal before the clarification deadline, and the buyer's answers recorded.
- **Price support:** the price is always the client's decision. The Hub shows a lawful-wage check (National Living Wage £12.71 an hour from 1 April 2026 for workers aged 21 and over, including travel time, plus holiday pay, pension and National Insurance) and warns if a rate looks too low to deliver lawfully.
- **Pre-submission compliance checklist** (every item must be ticked, with evidence where relevant), covering the eight ways to fail at the first gate:
  1. Submitted before the deadline, with margin
  2. Every mandatory document uploaded and every declaration signed by the client
  3. Insurance at or above the required levels (employer's liability at least £5 million by law)
  4. Financial check met, or the accepted alternative supplied
  5. CQC registration covers the right regulated activity and service type
  6. Word limits kept and the buyer's templates unchanged
  7. No contact with buyer staff outside the portal
  8. Every statement true and evidenced
- **Submission evidence:** the portal confirmation is captured and the client is notified the same day.
- **Outcome and learning:** the assessment summary or feedback, with scores per question, is stored. Wins trigger congratulations, mobilisation support, a case study permission request and a referral ask. Losses trigger a feedback review and a reminder for the next window (dynamic markets can be joined at any time; open frameworks reopen). Scores feed the learning loop.

### 19.4 What the client sees for a tender

A tender tracker with a countdown to the closing date and to **their** next deadline (form, documents, comments, sign-off), the lots they are bidding for, the documents still needed, drafts to review in the Review Room, the promise register to approve, and the outcome.

---

## 20. Ticks, sign-offs and signatures everywhere

| Level | Used for | Recorded |
|---|---|---|
| **Tick** | Tasks and checklist items, by staff or client | Who, when, and evidence where required ("Do not mark sent without evidence") |
| **Staff sign-off** | Gates, stages, pack components, drafts | The person signing; a second person verifies where required (QA, second review, manager approval) |
| **Client e-signature** | Engagement letter, final pack approval, tender promises and price, quotes and agreements | Name, time and the exact version signed |

Signed items are locked ("Signed and locked. This record is read-only."). Any change creates a new version. Every tick, sign-off and signature appears in the audit trail and, where relevant, on the client's tracker as a visible tick.

---

## 21. Secure vault for client logins

Care Sync sometimes creates or holds accounts for clients (email accounts, the CQC provider portal, tender portals). These move out of spreadsheets into an encrypted vault:
- Each login is stored against the client, visible only to named roles.
- Viewing a password requires a stated reason, and every view is logged.
- The preferred route is always to be added as a user (for example the bid lead on a tender portal) rather than to hold a password.
- Reminders prompt the client to change passwords after a contract is awarded or the work ends.
- Logins are never shown in notes, messages, emails or exports.

**Recommended now:** move the existing logins spreadsheet into a password manager with restricted access until the Hub is live.

---

## 22. Moving from the current tools

1. Import all clients from the Client Control Register, mapping each column to its Hub field (stage, owners, pack components, deadlines, CQC submission details, risk).
2. Every free-text value that does not fit a field becomes a note for review, so nothing is lost.
3. Clients with a missing CQC date or reference appear in a "fix the record" list, filled only from acknowledgement evidence.
4. Drive folders are linked, and optionally mirrored, so files stay where staff know them.
5. Run the Hub and the register side by side for 2 weeks, then switch.

---

## 23. Notification principles (from current practice)

- Staff alerts fire once per new or materially changed issue, never repeatedly for an unchanged one.
- No automatic client contact for internal issues. Clients are only contacted through approved templates or by a person.
- A legal deadline or a Critical risk always alerts the case owner and the manager.

---

## 24. Growth and sales

### 24.1 After registration
At registration the client receives the Registration File, the journey moves to Aftercare, and an account owner joins the consultant. A growth plan call within 5 working days, part of launch support, agrees goals such as council work, supported living or new areas, and completes the growth profile (section 24.4).

### 24.2 What can be offered (from the Care Sync price book)

| Offer | Price | Trigger |
|---|---|---|
| Tender writing | From £1,500 + VAT, full quotation after review | Tender Radar match in their area and service |
| Bid review | Around £500 (VAT to confirm) | Client writing their own bid |
| Retained tender package | Pending | 2 tenders in 12 months, or more than one council area |
| Policies for a tender | Extra fee, Pending | Gaps in tender readiness |
| Supported living add-on | £1,500 including VAT; policies quoted separately | Home care client moving into supported living |
| PIR writing | £750 + VAT per PIR | PIR received (logged by the client or captured from email) |
| Variations (location, service, band) | Pending | New office or area |
| CQC interview preparation | £750 including VAT | Interview booked |
| Single services (policy refresh, business plan) | From £500 + VAT | Annual review due or a law change |
| CIW or RQIA registration | £4,500 + VAT | Expansion into Wales or Northern Ireland |
| Marketing (website, SEO, Google profile) | Quote | Registered but few referrals |

Never offered: staff training or care monitoring systems (the Hub may recommend monitoring systems for clients to buy directly). Prices marked Pending cannot be quoted; the Hub shows "I'll confirm that for you today" and sends an approval request to Collins. Discounts require Collins's approval.

### 24.3 Opportunity Engine
Signals create tasks with an owner and a deadline: tender match (call within 2 working days), PIR received (urgent), registration (growth plan call, tender alert opt-in, review and referral asks), policy review due (60 days ahead), new office or area (variation), tender won (mobilisation, case study, referral), tender lost (feedback review, next window), unhappy stage feedback (**selling paused** and a save call to the consultant).

### 24.4 Growth and tender readiness profile
Rating and date per location, registration date, office location, insurance levels and expiry, policy currency, Central Digital Platform status, case studies, social value, and monthly spare capacity (one tap by the client). A readiness score shows gaps, and each gap links to the relevant service.

### 24.5 Sales workspace
- Sales tasks in "My day", ordered by urgency.
- One-click call cards in the Care Sync format, filled from Hub data, including the conflict check, deadline maths, the opener variant, the likely blocker and the cold call questions.
- A Sales Coach button for live "Say, Ask, Aim for" help.
- The 60-second debrief after each call.
- Follow-up sequences planned back from the deadline, stopping instantly on a no or an opt-out.
- Quote, e-signed agreement and deposit invoice in one flow; a paid deposit opens the delivery journey automatically.
- Compliance guardrails: TPS and CTPS screening within 28 days, do-not-contact on every channel, data source recorded, privacy footer added, conflict check before any contact.
- GoHighLevel stages with entry evidence (Matched, Contacted, Conversation, Planning call booked, Planning call held, Agreement sent, Won, Onboarded, Closed). Won requires a signed agreement and a paid deposit.
- Account plans, a weekly scorecard per rep, the call review rubric and the new starter sign-off.

### 24.6 GoHighLevel
Staff work in the Hub; calls, notes, stages, tasks and opt-outs sync to GoHighLevel automatically, which remains the official sales record.

---

## 25. Revised phases

| Phase | Delivers |
|---|---|
| **1. Foundations and migration** | Roles, client records, smart onboarding forms with automatic gate checks and downloads, onboarding gates, stages and evidence rules, pack components, deadline sequence, weekly update composer, document vault, secure vault, register import |
| **2. Client experience** | Client Hub (Today, journey, documents, Review Room, CQC centre, Ask), notifications, e-signatures |
| **3. Tenders** | Tender Radar, tender delivery journey and workspace, evidence library, promise register, compliance checklist |
| **4. Sales and growth** | Opportunity Engine, sales workspace, call cards, GoHighLevel sync, price book controls |
| **5. Intelligence** | AI drafting, Sync Assistant and Staff Assistant, consistency check, learning loop, dashboards |

---

## 26. Smart onboarding forms

Replaces the Google Forms (CQC Registration Information Form, Tender Preparation Questionnaire, and the CIW and RQIA versions) with forms built into the Hub. Reviewed on 2 November 2026 from the form response sheets; only the question structure was used.

### 26.1 What the current forms teach us

| Observation | Design response |
|---|---|
| The CQC form has about 120 questions and the tender form about 236, many hidden by branching | Keep the branching, and pre-fill everything the Hub already knows so clients answer far fewer |
| Directors, contract examples and private clients are fixed blocks ("Director 1" to "Director 4") | Repeating groups: "Add another director", unlimited |
| Address history boxes are filled with dates instead of addresses | A structured address timeline with postcode lookup, from and to months, and automatic gap detection |
| A DBS issue date was entered as year 3026; dates arrive in US format | Validation: real date pickers, UK format, no future dates where impossible, DBS certificate numbers checked for 12 digits |
| **Portal usernames and passwords are collected in plain text and stored in a spreadsheet** | Never collected in a form. The client adds Care Sync's bid lead as a portal user; if a password is unavoidable it goes straight into the secure vault (section 21) |
| Signatures are typed names | E-signature with name, time and the exact version signed |
| The tender form already asks "What has changed since you last completed this?" | Previous answers are shown pre-filled with a "still correct?" check, so a repeat form takes about 10 minutes |
| The tender deck tells clients to write "not sure" when unsure | A "Not sure" button on every question that creates a question for staff instead of a blank |

### 26.2 What the client experiences

- **Tailored from the first screen.** The form knows the client's package and only shows what applies: company formation (only if not yet incorporated), regulator (CQC, CIW or RQIA), service type, registered manager and nominated individual the same person or not, DBS done or three IDs, office type, and for tenders the lot types (home care, supported living, care home, community support).
- **Pre-filled, not re-typed.**
  - Company number → name, registered office, incorporation date, directors and persons with significant control filled from Companies House; the client confirms.
  - CQC provider ID → rating and date, locations, regulated activities and service types filled from the CQC register.
  - Postcode lookup for every address.
  - Everything already in the company profile ("tell us once", section 5.10).
- **Shared out to the right people.** The owner invites the registered manager, nominated individual, each director or the accountant to complete **only their own section** by secure link. Each section shows who owns it and its progress.
- **Helpful while answering.**
  - Every question says why we ask it and where it is used ("This goes in your provider application"), following the tender deck's "where each part of the form ends up" table.
  - Gap detection on address history (5 years) and CV history (age 16 to present) with a prompt to explain each gap.
  - Uploads inline beside the question, with date checks (for example a bill within 3 months).
  - Format checks for phone numbers, emails, postcodes and professional registration numbers, with a gentle "Is this right?" rather than a hard block where a format can vary.
- **Easy to finish.** Saves as you go on any device, shows time remaining, voice answers for long text, and a reminder if unfinished (target 2 working days for tenders). Reminders stop the moment it is submitted.
- **Signed properly.** The declaration and consent are e-signed, and the client gets a copy of their answers as a PDF.

### 26.3 What staff get (the main benefit)

1. **Nothing to re-type.** Answers land directly in the client record and company profile. Uploads are filed automatically into the right vault folder (01 Onboarding information, 06 Premises and supporting evidence, and so on) with consistent names.
2. **Instant automatic checks.** The moment the form is submitted, the onboarding gates (section 18.2) run:
   - directors on the form match Companies House;
   - address and CV gaps;
   - DBS details complete and valid in format;
   - a professional register link opened ready to verify;
   - registered manager and nominated individual the same person, flagged for a specialist check;
   - the office address on the form matches the address evidence.

   Staff see Pass, Fail with the exact issue, or Needs a person, and confirm. They no longer check 38 columns by hand.
3. **One-click fix list.** Failed checks become a plain-English list the client can act on, sent only when staff press Send.
4. **Changes highlighted.** If the client edits after submitting, staff see exactly what changed (old and new value) and the affected gates are rechecked. The onboarding lead is alerted once.
5. **Assisted mode.** A staff member can fill in the form with the client during a call, recorded as "completed with [staff name] on [date]".
6. **Downloads, in every useful shape:**

   | Download | What it is | Used for |
   |---|---|---|
   | **Client Information Pack (PDF)** | Branded, sectioned and readable, with a contents page, signature record, timestamp and a list of uploaded documents | The record, sharing internally, printing |
   | **Editable Word version** | The same content as a Word document | Editing and reusing text |
   | **CQC application sheet** | Answers arranged in the order the CQC provider and registered manager applications ask for them, each with a Copy button | Filling in the CQC application quickly and accurately |
   | **Tender data sheet** | Answers arranged by the Procurement Specific Questionnaire and Central Digital Platform sections, plus the evidence library | Supplier information and quality answers |
   | **Everything pack (ZIP)** | The PDF plus every upload, consistently named (for example CSE-071_RM_DBS.pdf) | Handover, archiving |
   | **Spreadsheet export** | One or many responses as Excel or CSV | Reporting |
   | **Redacted PDF** | Dates of birth, DBS numbers and ID numbers hidden | Sharing safely with partners such as AssuredBid, with the client's agreement |

   Every download is logged. A copy of the PDF is saved automatically to the client's Drive folder during migration.
7. **Answers feed the work.** Company name, addresses, people, service types and service user bands flow straight into the Statement of Purpose, policy headers, business plan, training plan and tender answers, and power the consistency check (section 10.3).
8. **Form builder for directors.** Questions, help text, branching and validation can be edited without developers. Each question records where it maps to in the Hub and in CQC or tender forms. Versions are kept, and live clients stay on the version they started.
9. **Insight.** The form reports where clients drop off, which questions get "Not sure" most often and how long each section takes, so the form keeps getting better.
10. **Privacy built in.** Sensitive fields are masked by default for staff, revealing one is logged, and retention follows section 13.

### 26.4 Until the Hub is live: quick wins in Google Forms

1. **Remove the portal password questions now.** Ask the client to add the bid lead as a portal user instead.
2. Add response validation: DBS number 12 digits, UK date format, email and phone patterns.
3. Replace the five free-text address boxes with a clearer format hint and an example.
4. Add an Apps Script that, on every submission, creates a branded PDF of the response in the client's Drive folder and emails the onboarding lead. This gives a downloadable copy straight away.

---

## 27. Open questions for Care Sync

1. **Email system:** Does the team use Google Workspace or Microsoft 365 for Care Sync mailboxes?
2. **Submission by email:** Is it correct that the consultant sends the application by email and the Hub only records it? Are there any other parts of the process that must stay on email?
3. **Other regulators:** Do you currently deliver CIW, RQIA or Ofsted work that should be included in the first phases?
4. **Team size and volume:** Roughly how many staff, and how many active clients at once now and in 12 months?
5. **Retention period:** How long should identity documents and DBS certificates be kept after a journey ends?
6. **Payments:** Should clients pay (for example for extra sessions) inside the Hub, or does payment stay in your current system?
7. **GoHighLevel:** Answered: it is the sales CRM. Confirm that a won deal (signed agreement and paid deposit) should start a Hub journey automatically.
10. **Price book items marked Pending:** retained tender rate, policy fees, variation prices, bid review VAT, and mock inspection and marketing prices for registration-only clients.
11. **Logins spreadsheet:** agree to move it into a password manager now, before the Hub is live.
12. **Tender form passwords:** agree to remove the portal username and password questions from the Google Form now.
13. **Interim PDF script:** would you like the Google Forms Apps Script (section 26.4) built now, so every submission produces a downloadable PDF before the Hub exists?
8. **Interview Preparation Hub:** What system does it run on, and can new client accounts be created automatically (for example through an API or an invite link)?
9. **Reply times:** What reply time should the Hub promise clients for questions (for example 1 working day), and for staff "Ask a senior" questions?
