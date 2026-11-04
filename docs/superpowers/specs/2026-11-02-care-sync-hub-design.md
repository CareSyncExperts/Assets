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
2. The consultant sends the submission to CQC **from the client's own email account**, through the client mailbox connection (section 41). The email is composed and sent inside the Hub, with the bundle attached.
3. The Hub keeps a copy of the sent email as evidence, and the consultant confirms "Submitted" with one click (the date fills in from the email).
4. The client is told immediately, and the stage moves to "With CQC".

If the email was sent outside the Hub, the consultant logs the submission manually and attaches the sent email or a screenshot.

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
After registration, the Aftercare track runs for the 12 months included in the package: monthly check-ins, policy review reminders, first inspection readiness, and a clear offer of next services (tenders, inspection readiness, marketing). At registration the Hub invites **every** registered client to leave a review on Google and Trustpilot (section 37, never only the happy ones) and, separately, asks about referrals.

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
| **Client care** | Usually Divine, for introduction calls | The introduction call after payment, relationship check-ins and the client's contact preferences (section 52) |
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
- **Reusable tender profile:** captures company, regulator, services, key people, contract examples, workforce, partnerships and documents once, for every future bid. It is presented as small tasks (section 38), pre-filled from the client record and the CQC register, and much of it can be gathered during the onboarding meeting itself. Later tenders only ask what has changed.
- **Evidence library per client:** contract examples from the last 3 years (who, what, how many people, hours, value, dates, outcomes), anonymised case studies, referees with permission recorded, and standard documents (accounts, organisation chart, CVs, CQC certificate and latest report, Statement of Purpose, insurance with levels and expiry dates, council quality monitoring reports, ICO number, Data Security and Protection Toolkit status, Cyber Essentials, ISO certificates). Expiry dates feed the expiry watch.
- **Drafts as files:** the bid is written in Word by the bid team, outside the Hub, and submitted on the buyer's portal. Each draft version is uploaded to the tender record, shared with the client to comment on and approve, and a second consultant's check is recorded as a task.
- **Commitments noted:** any commitment the client agrees to in the bid (for example "every new carer shadows for three shifts") is noted on the tender record, so that if the bid wins it becomes part of the start-up checklist.
- **Clarifications noted:** questions sent to the buyer and any buyer answers that affect the bid are recorded as notes on the tender record, and the client is told.
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

A tender tracker with a countdown to the closing date and to **their** next deadline (form, documents, comments, sign-off), the lots they are bidding for, the documents still needed, drafts to review (Word documents shared from the tender record), and the outcome.

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
| Mock inspection and inspection readiness | Pending (included in first-year support of full start-up packages) | Month 4 to 6 after registration |
| Training matrix and compliance management | Pending | After registration, as staff are recruited |
| Policy rebrand, branding and business forms | From £500 + VAT (single service), confirm | Client rebrands or buys an existing service |
| Statement of Purpose updates | Pending | Change of manager, address, bands or services |
| Ofsted registration support | Pending | Children's services enquiries |
| Temporary staffing and combined care agency packages | Pending | Staffing agency enquiries |

Service names follow the staff induction catalogue (Get registered, Stay compliant, Win work and grow, Brand and market). See section 50 for one conflict to resolve before launch.

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
| **1. Foundations and migration** | Roles, client records, address lookup with UPRNs, Companies House checks, the address matching engine and consistency matrix, smart onboarding forms with automatic gate checks and downloads, onboarding gates, stages and evidence rules, pack components, deadline sequence, weekly update composer, document vault, secure vault, register import |
| **2. Client experience** | Client Hub (Today, journey, documents, Review Room, CQC centre, Ask), notifications, e-signatures |
| **3. Tenders** | Tender Radar, the tender record (CRM: tender details, dates, tasks, files, notes, result), evidence library, submission checklist |
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
- **Easy to finish.** Saves as you go on any device, shows progress as small tasks done (never a total time), voice answers for long text, and a reminder if unfinished (target 2 working days for tenders). Reminders stop the moment it is submitted. Section 38 replaces the single long form with a short start and small tasks.
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

## 27. Address intelligence and company verification

Applications fail on small inconsistencies: Flat 2 on the form, Flat 3 on the bill, "Road" in one document and "Rd" in another, a registered office that is not the office CQC will register. The Hub checks every address and every company fact automatically, everywhere it appears, and shows a person the exact difference.

### 27.1 Prevent errors at the source
- Every address is chosen from a **postcode lookup** (Ordnance Survey Places API), not typed. Each address gets its **UPRN** (the unique reference for that exact property), its standard form and its map position.
- Clients pick their flat or unit from the list for that building, so "Flat 2" cannot silently become "Flat 3".
- If an address is genuinely missing from the lookup (for example a new build), the client can type it, and it is flagged for a person to check.

### 27.2 Every address has a role
One client can have many addresses, each with a role:

| Role | Source |
|---|---|
| Registered office | Companies House |
| Office where the service is managed (CQC location) | Onboarding form, then CQC application |
| Correspondence address | Onboarding form |
| Registered manager, nominated individual and director addresses and 5-year history | Onboarding form |
| Supported living properties and service delivery addresses | Onboarding or tender form |
| Address on each evidence document | Read from the document: lease, tenancy, title, utility bill, bank statement |
| Address written in the Statement of Purpose, policies, business plan and insurance quote | Read from the drafts |
| Address on the CQC register (after registration) | CQC API |

### 27.3 The matching engine
Every pair of addresses that should agree is compared, strongest test first:
1. **Same UPRN:** exact match.
2. **Same standardised address:** case, punctuation and abbreviations normalised ("Rd" and "Road", "St" and "Street"), flat and unit parsed separately.
3. **Same building, different unit:** for example Flat 2 against Flat 3. Always a **mismatch**, shown clearly, because it is the most common real error.
4. **Same postcode only:** probable, needs a person.
5. **Different:** mismatch.

Results show the two addresses **side by side with the differing words highlighted**, the source of each, and a suggested fix.

### 27.4 Reading the documents
When a document is uploaded, the Hub reads it and extracts the facts that matter, then a person confirms them. Nothing is accepted on the machine's word alone.

| Document | Facts read | Checks |
|---|---|---|
| Utility bill or bank statement | Name, address, date, issuer | Address matches the person's current address; dated within 3 months; name matches the person |
| Tenancy agreement | Tenants, landlord, address, term dates, any clause on business use | Address matches the office; tenancy current; flags a ban on business use; flags when the tenancy is in a director's personal name, so the landlord's letter must cover the company |
| Landlord or lender permission letter | Who gave permission, to whom, for which address, for what use, date, signature | Covers administrative office use, names the company, matches the office address and the landlord or lender |
| Commercial lease or licence | Parties, premises address, term, permitted use | The company (not only a director) is a party or authorised; address matches; lease current |
| Title register (HM Land Registry official copy, small fee per title) | Registered owner, any registered charge such as a mortgage | Owner matches the director; **a registered charge means lender permission is required** |
| Virtual office agreement | Provider and address | Not accepted; the client is told why and shown the options |

### 27.5 Companies House checks (Companies House public data API)
Run when the company number is entered, again before submission, and continuously afterwards:
- Company status is active, with no strike-off proposal, liquidation or dissolution
- Registered office matches the form, and the role it plays is clear (registered office and the CQC office can differ, but the client must be clear which is which)
- Directors on the form match the officers on the register (names, and month and year of birth); persons with significant control match
- Accounts and confirmation statement are not overdue
- Nature of business (SIC codes) fits a care provider, with a prompt to review it if not (for example 88100, social work activities without accommodation for the elderly and disabled)
- Director identity verification: each director's 11-character Companies House personal code is recorded, as the current form already asks
- Disqualified directors search for every director
- Company name used **exactly** as registered everywhere (Ltd or Limited, spacing, ampersands), feeding the consistency check

**Continuous monitoring:** the Companies House streaming service watches every client company. A change of registered office, a new or departing director, overdue accounts or a strike-off notice alerts the case owner, updates the client record, and prompts a check of whether CQC needs to be told.

### 27.6 CQC register checks
- Before tenders and after registration, the CQC API confirms the provider and location addresses, the registered manager, regulated activities and service types, and alerts on any difference from the Hub.
- For tenders, the office's distance to each lot is worked out from the postcode, measured the way the pack defines it.

### 27.7 The Address and identity check screen (staff)
One view per client: a **consistency matrix**. Rows are the facts (company name, registered office, CQC office address, registered manager name and address, nominated individual, service types, service user bands). Columns are the sources (onboarding form, Companies House, evidence documents, Statement of Purpose, policies, insurance quote, CQC application sheet). Each cell shows a tick, a cross with the exact difference, or "needs a person". One click opens the side-by-side comparison and the fix.

### 27.8 What the client sees
A mismatch becomes one calm question, never an error message:
> "Your electricity bill says Flat 3, 14 Orchard Way. Your form says Flat 2. Which is right?"

Buttons: "Flat 3 is right, update my form" or "Flat 2 is right, I'll upload another bill". The fix updates every place that address is used, and the client sees the tick appear.

---

## 28. The consultant cockpit

How a consultant doing CQC applications and tenders would want the system to work:

1. **Client at a glance.** One page answers everything in 10 seconds: stage, who has the ball, risk, pack components, next deadline, last update, open questions, expiring documents, Companies House status, the consistency matrix result and each person's readiness.
2. **People profiles.** Each registered manager, nominated individual and director has one profile: identity route, DBS, Companies House personal code, professional registration, address timeline, CV timeline with gaps, training. If the same person is involved in two client companies, the Hub links them and flags it.
3. **Pack Doctor before submission.** A pre-submission check (built on Care Sync's existing pack alignment and pre-submission checking skills) runs everything: the consistency matrix, exact company name, service types and service user bands identical across the Statement of Purpose, forms and policies, registered manager details the same everywhere, signatures present, documents in date. It gives a list of **blockers** and **warnings**. Submission stays locked while any blocker remains.
4. **Copy-to-application.** The CQC application sheet with Copy buttons (section 26.3).
5. **CQC correspondence assistant.** When a CQC email is captured, the Hub extracts the request and the deadline, finds the relevant documents and drafts a reply for the consultant to edit and send.
6. **Command bar.** Press one shortcut and type to jump to any client, document or action ("Bright Path SoP", "send update", "new tender").
7. **Generated documents.** Statement of Purpose, policy headers, business plan and tender facts generated from the single client record, so a change made once updates everywhere at the next version.
8. **Everything for tenders in one place.** Tender Radar, the tender record, the evidence library and the submission checklist (section 19).
9. **Four-eyes quality.** Second-person sign-off on packs, bids and anything sent to CQC.
10. **Playbook at hand.** The "how we do this" guide beside every step, and the Staff Assistant for quick answers.

---

## 29. Client experience principles (how the best companies would approach it)

| Company habit | What it means for Care Sync Hub |
|---|---|
| **Apple: prevent the problem, keep it calm** | Postcode lookup and pre-fill stop errors before they happen. One clear next step per screen. Bad news explained calmly with a plan. Privacy treated as a feature |
| **Amazon: tell people before they ask** | Order-tracking style updates. If Care Sync is going to miss a promised date, the client is told **before** the date, with the new date and the reason. The Hub detects the risk from overdue tasks automatically |
| **Google: measure what matters** | The HEART measures (happiness, engagement, adoption, retention, task success) tracked per stage. Reminder wording and timing tested and improved using real results |
| **Meta: meet people where they already are** | Updates by WhatsApp or text where the client agrees, as well as email and in the Hub, with quiet hours respected |
| **Uber and delivery apps: show progress and timing** | A live tracker with expected dates for the stages Care Sync controls, based on how long those stages really take. **No dates are ever promised for CQC's own decisions**; instead the client sees how long it has been since submission and what normally happens next |

Features that follow from these principles:
- **Proactive updates.** Every milestone triggers an update, plus the weekly nine-part update (section 18.5). A short update is sent even when there is no news ("CQC has not replied yet. Nothing is needed from you. We check every week.").
- **Personal video updates.** For big moments (submitted, interview booked, registered) the consultant can record a 60-second video message that appears in the client's Hub.
- **Plain-English glossary.** Tap any term such as "nominated individual", "service user band" or "framework" for a one-line explanation.
- **Privacy dashboard for clients.** Clients can see who at Care Sync opened their documents and when, as a Google account activity page does.
- **No surprises on money.** The payment schedule and what is paid are always visible.
- **Feedback that is acted on.** One-tap stage feedback (section 10.11), reviewed weekly, with changes recorded so clients see their feedback made a difference.

---

## 30. Care Sync's skills as engines inside the Hub

Care Sync already has a large library of specialist AI skills. In the Hub they become buttons and automatic checks inside the right stage. Staff stay in charge: every skill output is a draft or a suggestion that a person reviews, and nothing reaches a client or a regulator without passing the quality gate.

| Hub moment | Skills that power it |
|---|---|
| Enquiry reply and quote | sales-strategy (price book, call cards, live coaching, debriefs), caresync-client-enquiry-engine (written replies, always using the sales-strategy prices) |
| Onboarding checks | cv-gap-analysis (CV from age 16, gaps), cqc-registration-expert (specialist questions such as one person in two roles), provider-location-trading-name-rules (company, location and trading name consistency), marker-care-sync-document-intelligence (reading bills, tenancies, leases and title registers) |
| Drafting the pack | cqc-sop-creation, cqc-business-plan, cqc-domiciliary-care-policies, cqc-supported-living-policies, caresync-pro-policy-writer, caresync-pro-sl-policy-writer, caresync-legislation-policy-writer, cqc-staff-training-plan, care-training-matrix, cqc-supported-living-service-user-contract, cqc-supported-living-org-structure-chart, cqc-forms-creator, cqc-application |
| Rebranding existing policies | supported-living-policy-rebrand, dom-care-policy-rebrand |
| Writing standard | cqc-writing-standard, cqc-writing-library, cqc-regulations-master, cqc-rule-register |
| Pack Doctor before submission | cqc-pre-submission-checker, cqc-pack-alignment-checker, cqc-pack-scanner, dom-cqc-pack-auditor, sl-cqc-pack-auditor, cqc-application-rejection-prevention-engine |
| Wales and Northern Ireland | ciw-domiciliary-registration, ciw-registration-form-filler, ciw-domiciliary-policy-writer, rqia-interview (and the interview prep managers for the separate Interview Preparation Hub) |
| After registration | cqc-registration-variations (supported living add-on, locations, bands), cqc-pir-completion (PIR writing), cqc-inspection-readiness (first inspection readiness) |
| Tenders | tender-opportunity-analyser (reading packs, triage), uk-care-tender-score-engineer (where the marks are), uk-care-tender-questionnaire (PSQ and Central Digital Platform), uk-care-tender-writer (drafting), uk-care-tender-evaluator and uk-care-tender-readiness-auditor (second review and final check) |
| Brand, website and marketing services | caresync-website-builder, caresync-branding, care-sync-worldclass-marketing, care-sync-seo-2, care-sync-content-engine, social-media-manager, care-sync-meta-ads |
| Client communications | care-sync-marketing-psychology (ethical persuasion rules), stop-slop and humanizer (natural writing) |
| Quality and safety of every AI output | no-fabrication, fact-check, care-sync-quality-gate, care-sync-strict-council (high-stakes decisions) |
| Platform building blocks | docuseal-care-sync-signature-governance (e-signatures), stirling-pdf-care-sync-pdf-governance (PDF packs and redaction), n8n-care-sync-automation-governance (automations), ragflow-care-sync-knowledge-governance (knowledge for the Sync Assistant and Staff Assistant), langfuse-care-sync-observability and promptfoo-care-sync-quality-gate (monitoring and testing AI quality), opa-care-sync-policy-engine-governance (permission rules), gohighlevel (sales record sync) |

Rules for every skill in the Hub:
- The output is labelled as a draft, shows which skill produced it, and records who reviewed and approved it.
- Facts come only from the client record and approved sources; anything unverified is marked for checking, never invented.
- A second person signs off anything going to a client, CQC or a buyer.
- AI quality is measured continuously, and a skill whose drafts are often heavily edited is reviewed.

---

## 31. Onboarding that changes with the package

The client only ever sees questions for what they bought. A CQC registration client never sees website questions; a full package client gets their brand and business plan sections too; a supported living add-on client sees only what the add-on needs.

### 31.1 Form modules by package

| Module | DOM reg | SL reg | CIW | RQIA | Full start-up | SL add-on | Interview only | PIR | Tender | Variation | Website or marketing | Single service |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A. Company and contacts | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| B. Company formation (only if not yet incorporated) | | | | | ✓ | | | | | | | |
| C. Regulator, service type and regulated activity | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | ✓ | | |
| D. Registered manager | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | | | |
| E. Nominated individual (England) or Responsible Individual (Wales, Northern Ireland) | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | | | |
| F. Directors and persons with significant control | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | | | |
| G. Office and premises evidence | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | ✓ | | |
| H. Service users, bands and specialisms | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | | ✓ | | |
| I. Supported living (housing arrangements, separation of housing and care, client groups, specialist services) | | ✓ | | | if SL | ✓ | | | | | | |
| J. Business plan, cash flow, financial viability | | ✓ | ✓ | ✓ | ✓ | | | | | | | if a business plan |
| K. Insurance quote details | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | | | |
| L. Interview details (date, role, service type) | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ | | | | | |
| M. PIR (deadline, location, data checklist) | | | | | | | | ✓ | | | | |
| N. Tender (the full tender questionnaire with its lot branching) | | | | | | | | | ✓ | | | |
| O. Brand, website and marketing (logo, colours, domain, tone, photos, service pages) | | | | | ✓ | | | | | | ✓ | |
| P. Welsh language Active Offer | | | ✓ | | if CIW | | | | | | | |
| Q. Declarations and e-signature | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### 31.2 Rules
- A client with two packages gets each module **once**. Answers are shared, never asked twice.
- When a client buys something new later (for example the supported living add-on or a tender), only the **new** modules are sent, pre-filled from what is already known.
- The client never sees a long form or a total time. They start with 3 questions, and the modules for their package arrive as small tasks over the following days (section 38). A full start-up client simply has more small tasks than a CQC registration client; a supported living add-on client has only a few, with company details already filled in.
- Each module has an owner role, so the right person gets the right section (for example section D goes to the registered manager).
- Staff can add or remove a module for an individual client, with a reason recorded.
- Packages and their modules are set in the form builder by directors, so new packages need no developer work.

---

## 32. Stage-by-stage client communications

The full wording of every email is in `docs/superpowers/specs/2026-11-02-care-sync-hub-client-emails.md`.

### 32.1 Principles
- **Every stage change tells the client**, in the Hub and by email (and by text or WhatsApp where they agreed): what happened, what it means, what happens next, and whether anything is needed from them.
- **One email, one job, one button.** Short, calm, specific, ending on reassurance and the next step.
- **Help first, sell second.** Delivery emails never contain sales offers. Offers appear only in aftercare and growth emails, only when relevant to the client's own situation, and never when the client is unhappy, has a Critical risk, or is dealing with a refusal.
- **True and lawful.** British English, no dashes, no bold in email bodies, no "free", no guarantees, real proof only, and an opt-out on every marketing email. Sole traders get marketing only with consent.
- **Signed by a real person**, the client's consultant, with a reply going straight to them and into the Hub.
- **Frequency cap.** At most one marketing email a week per client; service emails are not capped but are combined where several happen on one day.

### 32.2 The email map

| Stage | Emails |
|---|---|
| Before signing | Enquiry reply within 15 minutes in staffed hours; quote; agreement reminder |
| Welcome | Welcome and 3 quick questions; meet your team |
| Onboarding | Your next few things; gentle reminders that open the exact task (day 2 and 4); everything received with what we checked; one quick question or fix list; all checks passed and your named team |
| Delivery | Weekly update (nine-part); document accepted or needs re-upload; draft ready to review; review reminder; final pack ready to sign |
| CQC | Submitted; CQC acknowledged; CQC asked for more information; interview booked (with the Interview Preparation Hub link); interview reminders; after the interview |
| Outcome | You are registered (celebration, Registration File, next steps); Notice of Proposal (calm plan); application returned (recovery plan) |
| Aftercare and growth | Day 7 launch checklist; day 30 check-in; tender in your area; month 4 first inspection readiness; policy review 60 days before the anniversary; PIR received; registration anniversary with "your year with Care Sync" |
| Tenders | Tender onboarding; deadlines; submitted; won (mobilisation, case study request); not successful (feedback review, next window) |
| Win-back | No activity for 6 months: one useful update relevant to their service, and a way to say "not now" |

---

## 33. Relationship and growth programme (learning from the best)

| What the best companies do | How Care Sync applies it |
|---|---|
| **Amazon: order tracking that tells you before you ask** | Every stage email, a live tracker, and a "we're running late" message before any promised date is missed |
| **Amazon: "frequently bought together", at the right moment** | A next-best-offer map (below) that suggests one relevant service at the moment it is genuinely useful, never a catalogue |
| **Amazon Subscribe and Save, Prime** | A retained option for clients who need ongoing work: retained tender package, annual policy review, priority tender alerts. Pricing set by Collins before launch |
| **Alibaba: trust between buyer and seller** | The Care Sync promise written into every client's Hub: fixed fees agreed before work starts, response times, who handles CQC correspondence, and what happens if something goes wrong |
| **Alibaba: matching buyers to opportunities** | Tender Radar matching clients to tenders in their area, with a readiness score that shows what to fix first |
| **Spotify "Wrapped", year in review** | "Your year with Care Sync" on the registration anniversary: registered date, policies updated, tenders bid and won, milestones. Easy to share if the client wants to |
| **Starbucks and Uber: rewards and referrals** | A refer-a-provider programme with a thank-you agreed by Collins, asked for at natural high points (registration, award letter, paid deposit) |
| **Apple: signature moments** | A personal video from the consultant on big days, a registration celebration screen and email, and optionally a posted card on registration day |
| **Big platforms: partner networks** | A directory of trusted partners clients often need (insurers, accountants, recruitment, care monitoring systems for clients to buy directly), with any referral arrangement disclosed |

### 33.1 Next-best-offer map
One relevant suggestion, at the right moment, only if the client is happy and has no open problem:

| Moment | Suggestion (prices from the price book) |
|---|---|
| Registered, home care client | Tender alerts for their area; marketing or website if they have few enquiries |
| Registered, client mentions learning disability or autism work | Supported living add-on, £1,500 including VAT (policies quoted separately) |
| Tender matched in their area | Tender planning call (no charge), then tender writing from £1,500 + VAT |
| PIR received | PIR writing, £750 + VAT |
| Month 4 to 6 after registration | First inspection readiness (price Pending) |
| 60 days before the policy anniversary | Policy review and update (price Pending) |
| Opening a new office or area | Variation support (price Pending) |
| Second tender in 12 months | Retained tender package (rate Pending) |

### 33.2 Measures
Client satisfaction per stage, Net Promoter Score at registration and anniversary, response times, time from payment to submission, services per client, repeat purchase rate, referral rate, and unsubscribe rate (a rise means the emails are not helping).

---

## 34. Calm, person-centred client experience

The Hub does a lot, but the client should only ever feel three things: "I know where I am", "I know what to do next", and "someone is looking after me".

### 34.1 Never overwhelming
- **Three things on the home screen, no more:** where you are, what you need to do (at most three items, most important first), and what we are doing for you. Everything else is one tap away.
- **One task at a time.** "Next up" opens a focused screen for a single small task (one to three questions or one photo). When it is done, the next one appears. Long time estimates are never shown; small tasks may say "Quick" or "One photo".
- **We batch our asks.** Staff requests are grouped so the client gets one tidy list, not a stream of separate messages.
- **Plain English everywhere**, with the glossary one tap away (section 29).
- **Quiet by default.** Updates arrive when something matters, at times the client chose.

### 34.2 Person-centred
Asked once, during welcome, and changeable at any time:
- The name they like to be called
- How they want updates: email, text, WhatsApp, or in the Hub only
- When to contact them (for example "not before 10am, I work nights") and when not to
- How much detail they like: "just the headlines" or "tell me everything"
- Accessibility needs: larger text, read aloud, simpler language, a language other than English
- A "pause reminders until" option for holidays or difficult times, with the consultant told so deadlines are still protected

The consultant sees these preferences on the client page and in every message they write, and the Hub follows them automatically.

### 34.3 Everything in one place
The client Hub holds everything they need: progress, tasks, documents to review and sign, messages, sessions, their team with photos and names, the CQC tracker, the Interview Preparation Hub link, their Registration File and, after registration, their aftercare plan.

---

## 35. Documents room: view, review, compare and approve

Clients can see everything Care Sync has produced for them, as proper documents, and review them without downloading anything.

### 35.1 What the client can do
- **Open any document in the browser**, laid out as the real Word document with its pages and formatting. On a phone, a "reading view" reflows the text so it is comfortable to read.
- **Read a one-line summary first:** what the document is for, how long it takes to read, and **what to check** in it ("Check your office address and the people you will support").
- **Comment or ask a question** on any sentence (the Review Room, section 5.3).
- **Suggest a change** directly in the text. It appears to staff as a tracked change they can accept or reject, like Word's track changes or Google Docs' suggesting mode.
- **See what changed** between versions, with additions and deletions highlighted.
- **Approve** each document, or approve a whole pack after each part has been reviewed.
- **Download** as Word or PDF at any time.

### 35.2 What staff can do
- Upload a Word document or generate one from the client record; the Hub makes it viewable automatically.
- Publish a new version with a short note ("Added learning disabilities to service user groups as you asked"). The client is told, and sees exactly what changed.
- See every client comment and suggestion beside the text, accept or reject suggestions, and resolve comments.
- Optionally open a document in Microsoft Word or Google Docs to edit, then bring it back as the next version. The Hub always holds the official version and its history.

### 35.3 Document statuses
Drafting, In our quality check, Ready for you, Changes in progress, Approved, Signed and locked. The client only sees a document once it has passed the quality check.

---

## 36. E-signatures

### 36.1 What gets signed
- Engagement letter and terms
- Onboarding form declarations
- Final pack approval before submission
- Tender promises and price sign-off
- Quotes and agreements for new services

The client signs to confirm approval. CQC's own application declarations are still made by the applicant in CQC's process; the Hub records the client's approval of the content.

### 36.2 How signing works
- Built with DocuSeal (Care Sync's signature governance skill), embedded in the Hub so the client never leaves it.
- Works on a phone: draw, type or adopt a signature.
- The client reads the exact document they are signing, page by page, before the Sign button activates.
- Identity is confirmed by the logged-in account and, for key documents such as the final pack, a one-time code sent by text.
- Signing order where more than one person signs (for example a director, then the registered manager).
- Reminders until signed, following the client's contact preferences.

### 36.3 The record
Each signature produces a signed PDF and an audit certificate: who signed, when, the verified email or phone, and a fingerprint of the exact document version. The signed document is locked; any change needs a new version and a new signature. Electronic signatures of this kind are widely used and accepted in England and Wales for business agreements of this type.

---

## 37. Reviews on Google and Trustpilot

### 37.1 Yes, and the rules
Clients can be invited to review Care Sync on **Google** (using the Google Business Profile review link) and **Trustpilot** (using Trustpilot's review invitations; the free plan allows 50 invitations a month, and higher volumes or API access need a paid plan). Three rules apply, and the Hub enforces them:
1. **Invite everyone at the same moment, never only the happy ones.** Google and Trustpilot both prohibit selective inviting and steering unhappy clients away from public reviews.
2. **No incentives of any kind for a review.** The referral thank-you (section 33) is never linked to reviews.
3. **No fake or edited reviews.** Staff never write, suggest wording for, or post reviews for clients. Since 6 April 2025 UK law bans fake reviews and concealed incentivised reviews, with fines of up to 10% of turnover, and the CMA expects businesses to have a clear policy. Care Sync adopts a written reviews policy.

### 37.2 When and how
- **Moments:** registration issued; tender award letter received; a non-CQC service delivered and accepted (for example a website or a PIR).
- **Where:** a "Share your experience" card on the celebration screen and in the celebration email, with two equal buttons, **Review us on Google** and **Review us on Trustpilot**. A separate "Tell us privately" option is also there for anyone who prefers it, but it never replaces or hides the public options.
- **One reminder after 7 days, then stop.** No further chasing.
- **Every client at that moment is invited**, whatever their stage feedback score. Stage feedback (section 10.11) is for fixing problems, never for deciding who is asked.
- **Every review gets a reply** from Care Sync within 2 working days, thanking the client, or responding calmly and helpfully to criticism. A reply task appears in "My day".
- **Reviews are displayed honestly** on the website through the platforms' own widgets, never edited or selected misleadingly.

---

## 38. Effortless onboarding: no long forms

Clients are busy and a long form gets abandoned. So the Hub never presents one. Instead it combines three things: **ask very little at the start, fill in everything it can find itself, and collect the rest in small pieces when each piece is actually needed.**

### 38.1 The start: 3 questions
These three questions are the opening of the onboarding form (section 54), done together on the introduction call where possible. The rest of the form follows in the same place, tailored to the package.

At welcome the client answers only:
1. **Find your company:** type the company name or number and pick it from the Companies House results (or choose "not formed yet"). The Hub fills in the company name, registered office, directors and owners, and the client confirms with one tap (section 44).
2. **Who will be your registered manager?** A name and email or mobile, and one tap for whether they will also be the nominated individual. The Hub invites that person to do their own part.
3. **How would you like to do the rest?**
   - **Snap and send:** take photos of your documents and we read them for you.
   - **Do it on a call:** book a call and your onboarding lead fills everything in with you while you talk. You just check and sign.
   - **Bit by bit myself:** small tasks arrive a few at a time.

That is the whole first step. The client sees "Done. We'll take it from here." and a short list of what comes next.

### 38.2 Photos instead of typing
Most of the information Care Sync needs is already printed on documents the client has. The Hub reads it (section 27.4) and the client only confirms:

| The client sends a photo or file of | The Hub fills in |
|---|---|
| Driving licence or passport | Full name, date of birth, address |
| DBS certificate | Certificate number, issue date, name |
| Utility bill or bank statement | Name, address, date |
| Tenancy, lease or title register | Office address, parties, permitted use, whether a mortgage is registered |
| CV (any format) | Employment history from age 16, with gaps highlighted to explain |
| Insurance certificate | Insurer, cover levels, expiry date |
| Professional registration card or letter | Body and registration number, ready to verify on the public register |

Everything read from a document is shown back for a one-tap "That's right" or a quick correction. Staff confirm before anything is used.

### 38.3 Small tasks, at the right time
The package modules (section 31) are broken into small tasks of one to three questions or one photo. They arrive **when they are needed**, not all at once:
- Week 1: identity, address and office evidence (photos), and the manager's CV (upload)
- Week 2: the people you will support (tap to choose, no typing)
- When the insurance quote is being prepared: a few insurance questions
- When the business plan is being written: a few questions on finances, or "ask my accountant"
- When an interview is booked: interview details

At most three tasks are shown at a time. Each can be answered from a phone in the time it takes to make a cup of tea.

### 38.4 Designed for busy people
- **One question per screen**, with big tap answers instead of typing wherever possible.
- **"Skip for now"** on anything that is not urgent. It moves to later and never blocks progress.
- **"I don't know"** sends the question to the onboarding lead to help.
- **"Same as before"** wherever an answer repeats (for example the manager's address when it matches the director's).
- **Hand it to someone else:** any task can be passed to the manager, a director or the accountant with one tap.
- **Voice answers** for anything long.
- **Reminders that open the exact task.** A text, WhatsApp message or email contains a secure link that goes straight to that one question or camera upload. Documents are never sent inside a chat message.
- **Progress shown as wins, not time:** "6 of 9 things done", with a tick and a short "Nice, that's your ID sorted" after each task.

### 38.5 Done for you on a call
For clients who prefer it, or who stall, the onboarding lead books a call and completes the information live in **assisted mode** (section 26.3), sharing their screen if helpful. The client receives a summary to check and e-sign. Staff can offer this at any time from the client page, and the Hub suggests it automatically if a client has not started their tasks after 3 days.

### 38.6 What staff see
- A **missing information list** per client, ordered by what blocks work soonest, with one-tap "remind", "book a call" or "fill in from my notes".
- Everything read from documents is shown with its source, for quick confirmation.
- The same onboarding gates (section 18.2) update automatically as each small task arrives.
- A dashboard of where clients stall, so the questions or reminders causing it can be improved.

---

## 39. Simple for staff: big-company standards

Staff should be able to use the Hub on day one without training.

1. **One home screen per role.** "My day" shows only that person's work, in priority order. Nobody hunts through menus.
2. **Every task has one obvious button** that does the next thing ("Send update", "Check documents", "Reply").
3. **Search and jump anywhere** with the command bar: type a client, document or action.
4. **Consistent everywhere.** The same layout, words and status badges on every screen, from the Care Sync Unified design system.
5. **Help in place.** The Playbook guide sits beside each step; hovering any status explains it.
6. **Safe to click.** Undo for most actions, a confirmation only for things that cannot be undone, and drafts saved automatically.
7. **The Hub does the boring work:** filing, naming files, chasing, deadline maths, checks, update drafts, syncing to GoHighLevel.
8. **Clear empty states.** When there is nothing to do, the screen says so ("All caught up. Next update due Tuesday.").
9. **First-day tour.** A short guided tour for new staff, plus the practice client (section 11.6).
10. **Measured and improved.** Time taken for common tasks is tracked, and the slowest are simplified first.

---

## 40. "Done for you": showing clients everything we have done

Clients should be able to see, at any moment, everything Care Sync has done for them, crossed off like a finished list in Apple Reminders or Google Tasks, with proof.

### 40.1 The checklist (client view)
One list for the whole package, in three groups:
- **Done:** ticked and crossed out, with the date, who did it, and a link to the document or evidence. Collapsed by default ("Done: 24"), so it never overwhelms.
- **In progress:** what Care Sync is working on now, with the expected date.
- **Coming up:** what happens next, greyed out.

Client tasks and Care Sync tasks sit side by side, so the client sees that the work is shared and moving.

### 40.2 The package deliverables list
Each package comes with its own checklist of everything it includes, taken from the price book, so the client can watch every promise being crossed off. For example:

| Package | Items on the checklist |
|---|---|
| Domiciliary care registration | Every policy and document CQC asks for; help with the provider and registered manager forms; insurance quote obtained; consistency check across the pack; Interview Preparation Hub access; three coaching sessions with Millicent; all CQC correspondence handled; launch support |
| Supported living registration | As above, plus the easy read service user guide; financial viability statement signed by the in-house accountant; financial forecast; organisation structure chart; service user contract; CQC's additional form for services for autistic people and people with a learning disability, where it applies; pre-application engagement form, where it applies |
| Supported living add-on | Route check; new Statement of Purpose with changes highlighted; service user bands; CQC notification; the dom care to supported living transition guide; Interview Preparation Hub access; CQC correspondence |
| CIW registration | The ten CIW policies; Statement of Purpose; two-year business plan; cash flow; organisation structural plan; Responsible Individual questionnaire answers; Welsh language Active Offer in every document; insurance quote; coaching; correspondence |
| RQIA registration | The ten core policies; Statement of Purpose; Service User Guide; business plan; cash flow; financial viability statement; Responsible Individual and manager application guidance; insurance quote; coaching; correspondence |
| Full start-up | Company formation where needed; branding; website; business plan; registration items; first-year support including a mock inspection, help with council approved provider lists, and policy updates |
| Tender | Pack breakdown and rules; timeline and document checklist; each quality answer drafted and reviewed; questionnaire completed; compliance check; submission evidence |

Directors maintain these lists in the template builder, so they always match what is sold.

### 40.3 The work log ("what we have done for you")
A running record, like an order history, of every meaningful thing done for the client, written in plain English:
- "Wrote your 30 policies" (with the documents)
- "Checked your company with Companies House"
- "Compared your address across 6 documents"
- "Answered CQC's request for your recruitment policy, 12 November"
- "Checked for news from CQC, Thursday 14:10. Nothing new yet."

Most entries are created automatically from what staff already do, so communicating costs staff no extra effort.

### 40.4 Stage receipts
When a stage finishes, the client gets a short receipt: "Stage 4 done. Here is everything we did", as a crossed-off list with links. The weekly update's "Done this week" uses the same ticked list.

---

## 41. CQC and tender news: client email access and the secure vault

Staff need to know the moment CQC or a buyer replies, without logging in to dozens of client accounts by hand.

### 41.1 The client's email account is the CQC channel
CQC registration applications are sent to CQC by email, and CQC replies to the applicant's email address. So for every registration client, Care Sync holds the **client's email address and password** in the secure vault, with the client's written authority in their e-signed engagement letter. Often this is an account Care Sync created for the client (section 41.4).

With the login stored, the Hub does more than let staff log in by hand:
- **Mailbox connection.** The Hub connects to the client's mailbox (Google, Microsoft or standard email settings) and **pulls in every email from CQC automatically**, filed on the client's timeline with an alert to the case owner and a suggested milestone to confirm (section 7.2). Staff do not need to log in to check for news.
- **Send as the client.** Submissions and replies to CQC are written and sent from the client's own address inside the Hub, so CQC always hears from the applicant's email, and a copy is kept on the timeline.
- **Only what is needed.** The Hub files CQC, CIW, RQIA and tender portal emails. Other personal or business emails in the client's inbox are not copied into the Hub.
- **Manual login when needed.** Staff can still open the mailbox directly, using the vault's copy button, for anything the connection cannot do.
- **Two-step verification.** Where the email service asks for a code, the vault can hold the authenticator for that account with the client's consent, or the Hub sends the client a one-tap request for the code (section 41.3).

### 41.2 Other accounts
- **Tender portals:** Care Sync's bid lead is added as a user wherever the portal allows it; otherwise the portal login is stored in the vault. Portal notification emails also arrive through the client's mailbox connection.
- **Website, domain, Google Business Profile and social media:** manager or user access where offered, otherwise a stored login.
- **CQC provider portal after registration:** CQC asks each portal user to have their own email address, so the client's registered manager or nominated individual keeps their own portal account. The client's email connection still brings in CQC's emails.

### 41.2a Watch schedule
- The mailbox connection runs continuously; a CQC or portal email creates an alert and a suggested milestone for a person to confirm (section 7.2).
- If a mailbox connection breaks (for example after a password change), the case owner is alerted the same day and asked to update the login.
- For any client in "With CQC" or with a live tender where the connection is not working, the Hub schedules a **manual check task** (for example Monday and Thursday). The staff member ticks "Checked, nothing new" or logs what they found.
- Every check appears on the client's work log ("We checked for news from CQC on Thursday"), so clients know someone is watching even when there is no news.
- A client in "With CQC" with no check or watch for 7 days turns red on the manager's dashboard.

### 41.3 The secure vault (extends section 21)
- One place per client for every account Care Sync needs: **the client's email account (the CQC channel)**, tender portals, Find a Tender, website hosting, domain, Google Business Profile, social media, insurance portals.
- Each entry records the system, the account owner (always the client), how access was given (stored login, mailbox connection, or user added), the client's written authority and date, and the review date.
- Staff can update a login in seconds when a client changes a password, and the mailbox connection reconnects automatically.
- Stored logins are encrypted, visible only to named roles, revealed only with a stated reason, hidden again after 30 seconds, and copyable without being shown. Every view is logged, and the client can see the log in their privacy dashboard.
- **Two-step codes:** where a system sends a code to the client's phone, the Hub sends the client a one-tap request ("Care Sync needs your code to check CQC news. Tap to send it"), so nobody waits on calls or texts.
- Reminders to change passwords after a contract is awarded or the work ends, and a **hand-back checklist** at the end of every engagement: access removed, stored logins deleted, client told.
- Logins never appear in notes, messages, emails, exports or AI tools.

**Do now:** move the existing logins spreadsheet into a business password manager with a shared vault per client and restricted access, until the Hub is live.

### 41.4 Email accounts Care Sync creates for clients
Where Care Sync sets up a business email account for a client, the account is created in the client's name and ownership from day one, with the client holding the recovery details and two-step verification. Care Sync's access is given by delegation where the email service supports it, and handed back at the end of the work.

---

## 42. Always communicating

Good service is mostly communication. The Hub makes it automatic and makes silence impossible to miss.

1. **No silent client.** Every client hears from Care Sync at least weekly (section 18.5). A client with no outbound contact for 7 days, or a client message unanswered for 1 working day, turns red on the owner's "My day" and the manager's dashboard.
2. **Work becomes updates by itself.** Staff actions feed the work log and stage receipts (section 40), so clients see progress without staff writing extra messages.
3. **Promise tracking.** Every date promised to a client is recorded as a promise. If it is at risk, the owner is prompted to tell the client before it is missed, with a new date and the reason.
4. **One timeline per client.** Emails, calls, WhatsApp messages, meetings, documents and decisions in one place. Logging a call takes one tap and a line of notes; meeting notes (with consent) can be summarised and shared with the client.
5. **Communication health.** Each client shows a simple health signal (on track, needs attention, at risk) based on contact frequency, response times, open questions and promises, so managers see problems early.
6. **Their way.** Every message follows the client's preferences for channel, timing and detail (section 34.2).
7. **Cover without gaps.** Leave and absence routing (section 10.16) means no client goes quiet because someone is away.

---

## 43. The staff toolkit (everything in one place)

| Job | Tools in the Hub |
|---|---|
| Starting a client | 3-question start, photo capture, Companies House and address checks, onboarding gates, assisted mode, missing information list (sections 26, 27, 38) |
| Doing the work | Templates and skills, document generation, Review Room with tracked suggestions, quality gate, Pack Doctor, consistency matrix (sections 5.3, 28, 30, 35) |
| Keeping clients informed | Weekly update composer, work log, stage receipts, email library, promise tracking, communication health (sections 18.5, 32, 40, 42) |
| CQC | Submission bundle sent from the client's email, automatic CQC email capture, outcome centre, deadline countdowns, correspondence assistant (sections 7, 27, 28, 41) |
| Tenders | Tender Radar, call cards, tender record, evidence library, submission checklist (sections 19, 24, 53) |
| Selling and growth | Opportunity Engine, price book, quotes and e-signed agreements, GoHighLevel sync, next-best-offer map (sections 24, 33) |
| Signing and approvals | E-signatures, sign-offs, version locking (sections 20, 36) |
| Security | Secure vault with client email logins, hand-back checklist, audit log (sections 13, 21, 41) |
| Help and quality | Playbook, Staff Assistant, "Ask a senior", practice client, keyboard shortcuts and command bar (sections 11.5, 11.6, 28, 39) |

---

## Appendix A. Coverage audit: Drive and forms against this specification

Checked on 3 November 2026 against the Companies folder, the onboarding forms and the tender folders. Items marked "Added" were found in this audit and added to the sections shown.

| Source | Item | Where it is covered |
|---|---|---|
| Client Control Register: Dashboard | Totals, owners, overdue updates, missing CQC references | Director dashboard (10.9), manager views (18.5), migration (22) |
| Client Control Register: Client Register | Stage, owners, update day, pack components, deadlines, CQC submission date and reference, risk | 18.1 to 18.3 |
| Client Control Register: Weekly Updates | Nine-part update, evidence, QA status, next promised date | 18.5 |
| Client Control Register: Onboarding Queue and Form QA | Gates, recheck dates, one alert per change, handover approval | 18.2, 26.3, 38.6 |
| Client Control Register: Interviews and Closure | Interview status, preparation, outcome, closure approval, archive | 18.3, 8 |
| Client Control Register: Operating Guide | Weekly rhythm, rejection and resubmission, submitted control, deadline sequence, ownership model | 18 |
| Client Control Register: Drive Audit | Folder classification and colours | Replaced by structured stages (17, 22) |
| Client Folder Standard Template | Folders 00 to 10 | Vault structure (18.6) |
| Templates: CQC application forms | CQC provider forms and the add a regulated activity form | CQC application sheet (26.3), variations (24.2) |
| Templates: Supported living | Additional form for services for autistic people and people with a learning disability; pre-application engagement form; financial forecast; business plan prompts; transition guide; organisation chart; service user contract | **Added:** package checklist (40.2); module I (31.1) |
| Templates: Care Sync Pro prompts | Mock inspection and audit modules | Inspection readiness (24.2, 33.1) |
| Training folder and provider training guides | Domiciliary care and supported living provider guides | **Added:** aftercare resources on the launch checklist (40.2, email 6.1); Care Sync does not deliver staff training |
| Filing review | Service agreements, office licence agreements, invoices | Engagement letter e-signature (36); office evidence rules (5.2, 27.4) |
| Logins spreadsheet | Client logins and email accounts created by Care Sync | Secure vault holding client email logins (21, 41); client email accounts (**Added:** 41.4) |
| CQC Registration Information Form | Company details, trading name, correspondence address, partners who are not directors, legal entity | Modules A and F (31.1) |
| | Company formation: name choices, shares, persons with significant control, Companies House identity verification code, authorisation to incorporate | Module B (31.1), Companies House checks (27.5) |
| | Regulated activities and service user bands | Modules C and H |
| | Registered manager and nominated individual details, address history, professional registration | Modules D and E, address timeline (26.2) |
| | GP and referee, with permission for CQC to contact them | Gate "References and GP" (18.2); permissions recorded in module D |
| | Enhanced DBS or three IDs | Identity gate (18.2), photo capture (38.2) |
| | Directors 1 to 4 | Repeating groups (26.1) |
| | Signatory and declaration | E-signature (36) |
| Tender Preparation Questionnaire | Tender, portal, authority to submit, what has changed | Tender workspace (19.3); passwords removed (26.1) |
| | Company, Central Digital Platform, regulator, ratings | Tender profile (19.3), CQC checks (27.6) |
| | People, finance, insurance, accountant | Tender profile, evidence library (19.3) |
| | Contract examples and private clients | Evidence library (19.3) |
| | Workforce: numbers, turnover, vacancies, mandatory training completion, languages, drivers, pay, HR and care systems | Tender profile (19.3); price lawful-wage check |
| | Partnerships and social value | Tender profile (19.3) |
| | Documents and policies, quote for missing policies | Evidence library; policies for tenders (24.2) |
| | Standout evidence and concerns | Evidence library; onboarding meeting (19.3) |
| | Lots, and home care, supported living (including property details), care home and community sections | Lots decision and module N branching (19.3, 31.1) |
| | Declaration and consent | E-signature (36) |
| CIW and RQIA Registration Information Forms | Responsible Individual, Welsh language Active Offer, regions or HSC Trust areas | Modules E and P (31.1), CIW and RQIA checklists (40.2) |
| Tender outreach folder | Approved tenders queue, daily provider lists, research results, ready for GoHighLevel, archive | Tender Radar (19.1) |
| Tender writing folder | Questionnaires, clarification log, sales playbook, client tender onboarding deck | Tender workspace (19.2, 19.3), sales (24) |
| Company induction folder | Staff induction deck, facilitator guide, quiz answer sheet, CQC and policies training | **Added:** Care Sync Academy (48); brand voice guard (49.9); catalogue (24.2) |
| CQC registration training deck | Eight-step journey, document pack per service type, terminology, real refusal grounds and the checks that catch them | **Added:** master record and Pack Doctor rules (47) |
| CIW and RQIA Registration Information Forms | Question detail | **Not reviewed:** the forms cannot be read directly and no response sheets were found; covered at module level (31.1) until the questions are shared |

Apart from the CIW and RQIA question detail noted above, no item in the reviewed sources was left without a home in this specification.

---

## Appendix B. Google Forms compared with the Hub flow

The questions stay the same; the flow changes. Every question in the current forms is kept (Appendix A). What changes is how and when it is asked, so clients do far less typing.

### B.1 CQC Registration Information Form

| Google Form section | In the Hub | How it is collected | When |
|---|---|---|---|
| Is your company registered with Companies House? | Start question 1: "Find your company" | Search by name or number (section 44) | Start |
| Business name, number, registered office, legal entity | Filled from Companies House | Client confirms with one tap | Start |
| Trading name, correspondence address, phone, company email, website | Company details task | Pre-filled where known, quick confirm | Week 1 |
| Company formation: name choices, company type, shares, persons with significant control, identity verification code, authorisation to incorporate | Module B, only if not yet formed | Name ideas with an indicative check (section 44.2), taps for shares | Start, if not formed |
| Regulated activities and service type | Known from the package | Client confirms | Start |
| Service user bands | "Who you will support" task | Tap to choose | Week 2 |
| Registered manager details | Start question 2 invites the manager | The manager completes their own section | Week 1 (manager) |
| Registered manager address history (five free-text boxes) | Address timeline | Postcode lookup, month pickers, gap detection; current address read from an ID or bill photo | Week 1 (manager) |
| Professional body and registration number | Professional registration task | Photo of the card or letter, or typed; public register link for staff | Week 1 (manager) |
| GP and referee, with permission for CQC to contact them | References task | Short form for the manager | Week 1 to 2 |
| Same person as manager and nominated individual? | Asked with start question 2 | One tap | Start |
| Nominated individual details and address history | Nominated individual section, only if a different person | Same as the manager's section | Week 1 |
| Enhanced DBS, or three forms of ID | Identity task | Photo of the DBS certificate or ID documents, read automatically | Week 1 |
| Directors 1 to 4 | Filled from Companies House, unlimited | Only missing contact details are asked | Start to week 1 |
| Signatory, position, signature, date | E-signature | One signature when everything is in | At the end |

### B.2 Tender Preparation Questionnaire

| Google Form section | In the Hub | How it is collected | When |
|---|---|---|---|
| 1. Tender details, portal link, closing date | Filled from Tender Radar and the agreement | Client confirms | Tender start |
| 1. Portal username and password | **Removed from the form** | Bid lead added as a portal user, or login stored in the vault | Tender start |
| 1. Authority to submit | E-signed authority | One signature | Tender start |
| R. What has changed since last time | Only on repeat tenders | Previous answers shown with "still correct?" | Repeat tenders |
| 2 to 6. Company, regulator, ratings, services, service user bands | Filled from the client record, Companies House and the CQC register | Client confirms | Tender start |
| 7. Key people | Filled from people profiles | Client confirms or updates | Tender start |
| F. Finance, insurance, accountant | Finance task | "Ask my accountant" hands it over with one tap; insurance read from the certificate photo | Week 1 |
| 8. Contract examples and private clients | Evidence library | Gathered in the onboarding meeting, voice notes welcome, reused for future bids | Onboarding meeting |
| 9. Workforce | Workforce task | Number taps and short answers | Week 1 |
| 13. Partnerships and social value | Evidence library | Onboarding meeting | Onboarding meeting |
| 14. Documents and policies | Evidence library check | The Hub shows what is already held and asks only for what is missing | Week 1 |
| E. Standout evidence and concerns | Evidence library | Onboarding meeting, voice notes | Onboarding meeting |
| L. Lots | Lots decision | Tap per lot, with the four checks | Onboarding meeting |
| 11, 10, 12, C. Home care, supported living (including property), care home, community support | Only for the lot types being bid for | Short tasks; property details from photos and taps | Week 1 |
| 16. Declaration and consent | E-signature | One signature | Before drafting starts |

---

## 44. Company search and smart lookups

Google Forms can only offer empty boxes. The Hub searches official records as the client types.

### 44.1 Find your company by name
- The client (or a staff member starting a new client) types **a few letters of the company name or the company number**. Results from the Companies House register appear as they type.
- Each result shows the company name, number, status (active or dissolved), date incorporated and the registered office town, so the right one is obvious. Dissolved companies are hidden unless asked for.
- Choosing a company shows a confirmation card ("Is this your company?") with the directors listed. One tap fills in the company details, registered office, directors and persons with significant control, and starts the Companies House checks (section 27.5).

### 44.2 Not formed yet
- The client types name ideas. The Hub shows existing companies with the same or very similar names, as an **indicative check only**; Companies House makes the final decision on any name.
- The three name choices, company type and shares are collected as small tasks (module B).

### 44.3 Already registered with CQC
- For supported living add-on, variation, PIR and tender clients, the client can search for their service by name on the **CQC register**. The Hub keeps a daily copy of CQC's published register data so the search is instant.
- Choosing their service fills in the provider and location IDs, rating and date, regulated activities, service types and registered manager.

### 44.4 Find a person's other companies
- Typing a director's name searches Companies House officer records. Staff see that person's other appointments, which helps spot other care companies, dissolved companies, or the same person already linked to another Care Sync client.
- The disqualified directors search runs for every director.

### 44.5 No duplicates
As soon as a company is chosen, the Hub checks existing Care Sync clients and GoHighLevel contacts and says, for example, "This company is already a client (tender journey, Daniel)", so records are never duplicated.

### 44.6 Search everything (staff)
The command bar searches every client, person, company number, CQC reference, document and email, and copes with spelling slips ("brite path" finds Bright Path Care Ltd).

### 44.7 Other lookups
- Postcode lookup for every address, with the local authority area worked out from it (useful for matching tenders).
- Professional registration numbers checked for the right format for each body, with a direct link to that body's public register for staff to verify.

---

## 45. Lessons from leading tools

Researched on 3 November 2026: Teamwork.com, Rocketlane, GuideCX, monday.com, TaxDome, Karbon, Canopy, Clio, SuiteDash, Assembly (formerly Copilot), Moxo, Content Snare and HoneyBook. Findings come from search summaries of official help centres, release notes and reviews (the vendor sites themselves could not be opened from this session), so details should be confirmed before building. Only ideas that are new to this specification, or clearly better than it, are listed.

### 45.1 Money and starting work
| Idea | Learned from | What it does for Care Sync |
|---|---|---|
| **Accept, sign and pay in one step** | HoneyBook, Canopy, TaxDome, SuiteDash | The client opens one proposal page, chooses a package, e-signs the engagement letter and pays the deposit. Payment is only possible after signing. The journey, welcome email, first tasks and invoice then start automatically, with no staff action |
| **Good, better, best packages** | Canopy | One proposal shows, for example, registration only, registration plus tenders, and the full package, with prices from the price book. The client chooses which, not whether |
| **Instalments with automatic payment and reminders** | HoneyBook, TaxDome | Fees split by stage are charged on the due date if the client opts in, with polite reminders before and after. Pricing and schedules follow the price book (the standard instalment schedule is still Pending) |
| **Buy add-ons in the portal** | Assembly | Clients can buy an extra coaching session, a policy refresh or PIR help from a short list of services, without a call |

### 45.2 Workflows that run themselves
| Idea | Learned from | What it does for Care Sync |
|---|---|---|
| **Stages that move on by themselves** | TaxDome | When the client finishes every item, signs or pays, the journey moves to the next stage automatically. Milestones that need evidence from CQC still need a person (section 18.3) |
| **Client wording separate from staff stages** | TaxDome | Staff can use detailed internal stages while the client sees calm, plain wording such as "With CQC" |
| **One template that branches** | TaxDome, Moxo | Tags such as domiciliary care, supported living, variation or Wales switch steps on or off, so one template covers many cases and steps only appear when relevant |
| **Roles in templates, names later** | Teamwork | Templates assign "Tender writer" or "Case owner"; the manager picks a person later from a list showing who has capacity |
| **Steps that wait for each other, with a predicted date** | GuideCX, Moxo | If an earlier step slips, later dates move too, and the Hub shows an honest expected submission date for the stages Care Sync controls |
| **Simple automation rules** | Karbon, SuiteDash, HoneyBook | Directors set "when this happens, do that" rules (for example "when all tasks are done, mark the stage complete"), and can describe a rule in plain English for the Hub to set up |

### 45.3 Less chasing, more doing
| Idea | Learned from | What it does for Care Sync |
|---|---|---|
| **Do it from the email or text** | GuideCX, Assembly, Teamwork | Clients reply, approve or upload straight from the message without logging in. Replies land on the right task |
| **One-task links for other people** | Moxo, Teamwork Proofs | With the client's agreement, the Hub sends a secure link to a **landlord or mortgage lender** to upload the permission letter, a **referee** to confirm details, or an **accountant** to send figures. No account needed; the link expires |
| **Reviewers and approvers** | Teamwork Proofs | A co-director can be invited to comment only, or to approve, on a document without a full login |
| **Named reminder schedules** | Content Snare, Karbon | Staff pick a schedule when sending a request (gentle, standard, urgent), can preview every reminder, and reminders show the client's progress. After the last reminder, the task changes to "needs a call" and the owner is alerted |
| **Not started by alerts** | GuideCX | Warns staff when an important task has not been started by a set date, before it becomes overdue |
| **Bulk and repeating requests** | Content Snare, SuiteDash | One request sent to many clients at once (for example every supported living client after a law change), or repeated yearly for aftercare evidence. Client groups make this easy |
| **Read receipts** | Clio | Staff see when a client opened a message or document, which ends "we never got it" confusion |

### 45.4 One team inbox
| Idea | Learned from | What it does for Care Sync |
|---|---|---|
| **Shared inbox with labels** | Karbon, Teamwork Desk | All client and CQC email in one team inbox, synced with Gmail or Outlook, labelled automatically (CQC request, client question, document, urgent). One click turns an email into a task or attaches it to a journey |
| **Collision warning** | Teamwork Desk | Warns when two staff start replying to the same email |
| **Aftercare support requests** | Teamwork Desk | Aftercare questions become support requests with a reply target and a one-tap "How did we do?" |

### 45.5 AI that saves staff time
Every AI output is a draft for a person to check (section 30).
| Idea | Learned from | What it does for Care Sync |
|---|---|---|
| **Call notes to actions** | Rocketlane, Care Sync's own Google Meet practice | With consent, an onboarding or planning call becomes a summary, a draft follow-up email and a list of actions, risks and promised dates on the client's record |
| **Morning brief** | HoneyBook | At 8am each person gets a short summary of today's priorities, clients going quiet and promises due |
| **Meeting brief** | Assembly | Before any call, a one-page summary of the client's stage, recent messages, open questions and documents |
| **Uploads checked and filed automatically** | Canopy, TaxDome, Moxo | Each upload is matched to the request it answers, renamed, filed and checked for completeness before staff look at it |
| **Pre-filled repeat requests** | TaxDome, Canopy | Variation, PIR and aftercare requests are pre-filled from the original application |

### 45.6 Insight and improvement
| Idea | Learned from | What it does for Care Sync |
|---|---|---|
| **Health colour and "request an update"** | Teamwork | Each journey shows green, amber or red, and a manager can ask the owner for an update with one click |
| **Warnings with suggested actions** | GuideCX | Low engagement, late tasks, missing owners or no recent activity raise a warning with a suggested next step |
| **Which steps run late** | GuideCX | A report shows which template steps are usually late, so the slowest stages get fixed first |

### 45.7 A Care Sync app
A branded app (starting as an installable web app) with push notifications, a document scanner, Face ID or fingerprint login, and **switching between companies** for owners who run more than one provider (TaxDome, Moxo, SuiteDash). Staff get the same app filtered by "Due today", "In progress" and "Overdue".

### 45.8 Where these fit in the phases
- **Phase 1:** stages that move on by themselves, client wording, branching templates, roles in templates, reminder schedules, read receipts.
- **Phase 2:** do it from the email, one-task links for landlords, referees and accountants, reviewers and approvers, accept sign and pay, instalments.
- **Phase 4:** add-ons in the portal, bulk and repeating requests.
- **Phase 5:** shared inbox with labels, AI call notes, morning and meeting briefs, upload matching, warnings, lateness report, automation rules in plain English.
- **Phase 6:** the Care Sync app.

---

## 46. Super admin and system settings

Care Sync needs two **super admins** (for example Collins and one other senior person) who control the whole system, separate from everyday staff roles. Every super admin action is logged, and the most sensitive ones need a second super admin to approve.

### 46.1 What the super admin controls
| Area | What they can do |
|---|---|
| **People and access** | Invite and remove staff; assign roles (client care, onboarding lead, case owner, weekly update owner, manager, interview coach, tender writer, sales rep, account owner, finance); set which clients each person can see; enforce two-step login for all staff; set session time-outs |
| **Permissions** | A clear grid of what each role can view, edit, approve, send and export, including who can reveal vault logins and who can approve discounts |
| **Staff leaving** | One-click offboarding: access removed everywhere, clients and tasks reassigned with handover notes, vault access revoked, their mailbox connections handed to the new owner |
| **Packages and price book** | Packages, deliverable checklists, prices, VAT treatment and instalment schedules; only the super admin changes a price, and every change is dated |
| **Journey templates and forms** | Stages, small tasks, branching, reminder schedules, client wording and the form builder, with versions |
| **Emails and messages** | The email library, saved replies, signatures, sending domains and quiet hours |
| **Automation rules** | Every "when this happens, do that" rule, with an on and off switch and a log of every run; **failed automations are shown, never silent** |
| **Integrations and keys** | Companies House, Ordnance Survey, CQC data, HM Land Registry, DocuSeal, GoHighLevel, Google or Microsoft, payment provider, Xero, text and WhatsApp, BidSuite and the Interview Preparation Hub, each with a health status |
| **Branding** | Logo, colours and wording from the Care Sync Unified design system, for the Hub, emails and documents |
| **Data and retention** | Retention periods per document type, scheduled deletion, legal holds, data export, and the data protection requests queue (section 49.6) |
| **Security** | The full audit log (who saw, changed, downloaded, sent or revealed what, and when), unusual activity alerts, and **break-glass access** to a client's vault in an emergency, which needs a reason and alerts the other super admin |
| **View as** | See the Hub exactly as a given client or staff member sees it, to check or support them. Read-only, logged, and the client can see it in their privacy page |
| **System health** | Uptime, email delivery, failed syncs, broken mailbox connections and backup status in one place |
| **Business dashboards** | All director dashboards (section 10.9), proof bank (section 49.5), and exports for the accountant |

### 46.2 Safeguards on the super admin role
- At least two super admins, so the business is never locked out, and no more than needed.
- Two-step login is compulsory, with a hardware key or authenticator app recommended.
- Price changes, permission changes, data deletion and break-glass access need a second super admin to approve.
- A weekly summary of all super admin actions goes to both super admins.

---

## 47. The master record and Pack Doctor rules from real refusals

Care Sync's own CQC training deck makes the point clearly: "every refusal we looked at came from documents telling different stories". The Hub turns Care Sync's training into automatic checks.

### 47.1 One master record (the scope)
Each client has one master record, fixed early and changed only on purpose:
- Legal name exactly as at Companies House, company number, directors
- Registered manager and nominated individual
- Office location, with proof of the right to use it
- Regulated activity (usually personal care)
- Service type (domiciliary care, supported living or both)
- Service user bands
- Locations, and the registered manager's share of time at each

Every document, form answer and application sheet is checked against it.

### 47.2 Changing the scope shows its knock-on effects
Changing the master record shows exactly what must change across the pack before anyone can save it. For example:
- **Adding the learning disability or autism band:** CQC's additional form; positive behaviour support and restraint policies; a separate Mental Capacity and Best Interests policy; accessible (easy read) documents; specialist training in the training plan.
- **Removing that band:** remove STOMP and any claim to support those groups.
- **Adding supported living:** support-session wording, a supported living service user guide, housing separation evidence, and session monitoring instead of call monitoring.

### 47.3 Pack Doctor rules (from real refusal grounds)
| Check | What it catches |
|---|---|
| **Required document set** | The nine documents every service sends, the three home care and supported living add, and the two specialist services add; one policy per topic, with duplicates flagged |
| **Wrong-setting words** | Care home words in home care or supported living packs (resident, admission, placement, patient, ward, home manager, clinical governance), and "visit" or "call" in supported living packs, each with a suggested replacement |
| **Scope drift** | Activities, bands or claims in documents that were not applied for (for example STOMP without the learning disability band, or extra bands in the Statement of Purpose) |
| **Clinical task exclusions** | Nursing tasks such as syringe drivers in a personal care only service, which would need a different regulated activity |
| **Named people and numbers** | A real safeguarding lead with an out of hours contact; the local authority safeguarding team where the service is delivered, with its out of hours number; the complaints contact; the registered manager's contact details and address for notices in the Statement of Purpose |
| **Roles written in full** | No "depending on the role" in recruitment: each role, its regulator and the check named |
| **Overseas workers** | A written position on sponsoring and on employing overseas workers |
| **Structure matches reality** | No "the board will review" for a sole director; the real independent challenge arrangement described instead |
| **Complaints route** | Escalation to the Local Government and Social Care Ombudsman, not to CQC |
| **Business plan detail** | A 12-month, month-by-month forecast with costs broken down every month, not a single total |
| **Training plan detail** | Provider per topic, refresher dates, training by job role including managers, specialist training per band, the Care Certificate, support for overseas staff |
| **Service user guide contents** | What the service does not provide, how needs are assessed, charges, how visits or sessions are monitored, complaints, safeguarding, contract terms, contacts |
| **Supported living separation** | No house rules, curfews, signing-in books, staff master keys or tied housing; Deprivation of Liberty Safeguards never described as applying in someone's own home (the Court of Protection route instead); a landlord and provider with a shared director declared and managed as a conflict of interest |
| **Links and references** | Every link in the final Word file opened on submission day (Care Sync's link-checking skill), and every law referenced as the current Act, not a Bill or an out-of-date version |

Every rule shows the exact sentence, the reason and a suggested fix. Blockers stop submission; warnings need a person to confirm. New refusal grounds that CQC raises are added to the rules through the learning loop (section 10.4), so the Pack Doctor gets stronger with every case.

---

## 48. Care Sync Academy (staff learning)

Care Sync already trains staff well: a first-day induction, team training sessions with presenters, judges and quizzes, a facilitator guide and an answer sheet. The Hub gives this a home:
- **Learning paths by role.** Enquiry and sales; project delivery; tenders. Each has its first-week checklist ("what good looks like").
- **Session library.** Recorded or live sessions (for example the CQC registration training), with slides, facilitator notes and the questions used.
- **Quizzes with scores.** Questions from the induction and training sessions, the sales new starter sign-off (24 questions) and the call review rubric. Answers stay hidden until the person has answered.
- **Sign-off before working alone.** A new starter works on the practice client (section 11.6) and must pass their path before taking a live client. A manager signs off.
- **Refreshers.** Short quizzes repeat on a schedule and whenever a rule changes (for example a new CQC refusal ground).
- **Feedback.** Each session ends with the three questions from the training deck (one thing you will check differently, one open question, a score), which shape the next session.

---

## 49. Closing the remaining gaps

### 49.1 Invoicing, payments and accounts
Invoices, deposits, instalments and receipts live on each client's record and sync with **Xero** (or the accounting software Care Sync uses), so nothing is typed twice. Credit control reminders follow the client's preferences, and refunds and credit notes need manager approval. The client sees what is paid and what is due, with no surprises (section 29).

### 49.2 Complaints about Care Sync
A simple, visible way for a client to raise a complaint about Care Sync's own service, with an acknowledgement within 1 working day, a named handler who is not the person complained about, a response target, and a record of lessons learned. Complaints are reviewed monthly by the directors.

### 49.3 Partner access (for example AssuredBid)
On joint packages, a partner organisation gets a limited partner login: only the clients and items they work on, only with the client's agreement, all activity logged, and access removed automatically when the work ends.

### 49.4 Regulatory watch
A staff feed of changes from CQC, CIW, RQIA, Ofsted, the Procurement Act guidance and relevant law. Each change is tagged with the templates, policies and clients it affects, so the Hub can flag "12 supported living clients need their safeguarding policy updated" and create the tasks.

### 49.5 Proof bank
Marketing and sales claims are worked out from the Hub's own records and kept in one approved list with their evidence: first-time registration approval rate, providers supported, tender outcomes, client reviews. Sales, the website and documents use only the approved wording, so every claim is substantiated (as advertising rules require) and the same everywhere.

### 49.6 Data protection operations
A queue for subject access requests, correction and deletion requests, with legal deadlines tracked; a breach log with the 72-hour reporting clock; the record of processing activities; and a data protection impact assessment kept up to date.

### 49.7 Providers with several locations
One client can have several locations, each with its own address, registered manager, service types and CQC location ID, and each checked against the master record.

### 49.8 Closing a client
When work ends, a closure checklist runs: final update and Registration File sent, invoices settled, vault logins handed back or deleted, access removed, closure approved by a manager, and records kept or deleted on the retention schedule. The client keeps their documents.

### 49.9 Brand voice guard
Client-facing messages and documents are checked against Care Sync's voice rules from the staff induction: words never used (patient, guaranteed, cheap or basic, reach out), care home words in the wrong setting, British English, and no dashes. Staff see a gentle suggestion before sending.

### 49.10 Reliability
UK hosting, daily backups with tested restores, an uptime target, a status page for staff, and alerts when email delivery or an integration fails.

---

## 50. Inconsistencies found in Care Sync's own materials

These should be resolved before launch, because the Hub, the website and sales will all use one approved version (section 49.5):
1. **Founding year:** the staff induction says Care Sync was founded in 2023; the sales playbook says Care Sync Experts Ltd was established in 2024.
2. **Staff training:** the induction lists "Comprehensive Training" and "Training Matrix" as services; the sales playbook says Care Sync does not deliver staff training. Decide whether training is offered, and if so, what exactly.
3. **"Former CQC senior inspector managers":** the induction calls this the biggest trust signal, but it is not in the sales playbook's confirmed proof list. It needs evidence on file before it is used in marketing.
4. **CIW and RQIA forms:** these could not be reviewed in detail. Please share their question lists or response sheets.

---

## 51. Client side, start to finish (audit and super admin alignment)

Every client screen was checked one by one, against each other, against the email library and against the super admin (section 46). This section records what was fixed, what was added, the full journey, and the rules that keep the client experience calm whatever is changed in settings.

### 51.1 What the audit found and fixed
| Found | Fixed |
|---|---|
| Two different client companies across the screens (one company on some, another on the rest) | One client story everywhere: Harbour Lane Care Ltd, director Amara Okafor, registered manager Ruth Bennett, consultant Daniel, coach Millicent, onboarding lead Grace |
| Today said policies were still being drafted, while other screens showed them approved | Today now shows the business plan in final checks, matching the checklist and the documents room |
| The 3 sessions were credited to Daniel on some screens and Millicent on others | All 3 sessions are with Millicent (kick-off, document review, interview practice), as the Drive offer says |
| Wrong weekdays (a Thursday that was a Friday, a Friday that was a Saturday) and a Notice of Proposal served on the day of submission | Every date checked; the CQC screen follows one believable timeline |
| "About 10 minutes" and "About 2 minutes" on documents and signing | Removed. No time estimates anywhere (section 38) |
| Two separate "Your documents" screens that did not link | One Documents tab with two parts: **From you** (evidence) and **Written for you** (the pack) |
| The invited manager's form read like a long form ("Section 4 of 9") | It is now the manager's own short task: "Hi Ruth, 3 of 5 done, 2 quick questions left" |
| The registered office did not match the flat in the address question | Companies House, tenancy and question now tell one story (Flat 3 is right, the form said Flat 2) |
| No way to see what Care Sync had done from Today or Journey | Both now link to the done-for-you checklist |
| Gendered pronouns for people in mockups | Neutral wording throughout |

### 51.2 The ten steps
| Step | The client sees (board) | The client does | We do | Emails | Super admin controls |
|---|---|---|---|---|---|
| 1. Paid and welcomed | 25 Welcome, 33 Introduction call | Takes a friendly call; nothing to type | Introduction call task created at payment (Divine by default); sales notes carried over; team assigned | 1.1, 1.2, 1.3, 1.4 | Who calls, how fast, retries, call guide, welcome wording |
| 2. Three questions | 23, 26, 16 | Three taps and one name | Companies House fill-in; manager invited | 2.1, 2.5 | Question sets per package; Companies House key |
| 3. Documents and email | 3, 12, 15, 27 | Photos and one-tap answers | Photos read; address checked; email login into the vault | 2.2, 2.4, 2.6 | Reminder timings, quiet hours, vault roles, retention |
| 4. Writing and review | 1, 2, 21, 18, 4, 28 | Comments, approves, books session 2 | Pack written; Pack Doctor checks; Friday update | 3.1, 3.2, 3.4 | Pack Doctor rules, update template, reply-time promise |
| 5. Sign | 19 | Signs once | Second consultant check; consistency check | 3.3 | E-signature settings; who can approve a pack |
| 6. Sent to CQC | 5 (Before we send) | Nothing | Sent from the client's own email | 4.1 | Email connection health; CQC email rules |
| 7. With CQC | 5, 6, Interview Preparation Hub link | Answers with us; interview practice | Replies drafted; interview prepared | 4.2, 4.3, 4.4 | Watch rules, reminder timings, Interview Hub link |
| 8. Decision | 20, 17, 5 (Notice of Proposal) | Celebrates, or reviews a calm plan | Registration File; or written response within 28 days | 5.1 to 5.4 | Review links and reviews policy |
| 9. Aftercare | 30, 29 | Monthly check-in; readiness list | Check-ins, policy review reminders, inspection readiness | 6.1, 6.2, 6.4, 6.7, 6.8 | Aftercare length per package; check-in rhythm |
| 10. Grow, then hand back | 30, 31 | Chooses what fits, if anything | Tender matches, supported living, PIR; logins handed back | 6.3, 6.5, 6.6, 7.0 to 7.2, 8.1 | Price book, offer rules, hand-back checklist, deletion |

Always on at every step: Ask Care Sync (6), Account and privacy (29), the Friday update, the CQC watch and the done-for-you checklist (21). Board 32 shows this map on the canvas.

### 51.3 Client screens added
- **25 Welcome:** the first moment after the deal is won. Agreement and deposit already ticked, the team introduced with what each person does, a hello video from the consultant, "how it works" in three lines, one button to start question 1, and the kick-off booking. Magic-link sign-in, no password.
- **26 Question 2, your manager:** "It will be me" or "Someone else" (name and mobile or email), then the nominated individual in one tap, using the directors found at Companies House. The manager gets their own invite, so the client never chases.
- **27 Your business email:** the CQC channel. Either the email Care Sync set up (in the client's name) or the client's own email and password, straight into the vault. Four plain promises (only regulator and tender emails filed; sent from your address; every sign-in visible; withdraw any time) and a link to the signed authority.
- **28 Sessions:** the 3 sessions with Millicent. Session 1 done with notes, session 2 booked by tapping a day and time (only free times shown), session 3 unlocks when CQC sets the interview date. Extra sessions through Ask, never pushed.
- **29 Account and privacy:** who can see the client's information and why, every time anyone looked (the same audit log the super admin sees, in plain words), the business email connection, contact preferences and quiet hours, download everything, correct something, how long things are kept, and "Raise a concern" that goes to a director.
- **30 Aftercare:** the post-registration home. Aftercare month counter, the next monthly check-in, a "ready for your first inspection" checklist, three growth options picked for this client with confirmed prices and a gentle "Tell me more", and the Registration File.
- **31 Your tender:** for tender clients. Internal submission date ahead of the buyer's deadline, at most 3 things waiting on the client (a voice note story, approving prices), each answer with its share of the score and status, and buyer clarifications already read for them.
- **5 CQC centre** gains a third state, **Before we send**, so the CQC tab is useful from day one: pack readiness, the business email connection, and what happens after submission, with no promises about CQC's timescales.

### 51.4 Client rules the super admin cannot switch off
These protect the calm, person-centred experience (section 34) and Care Sync's reputation. Settings can change wording and timings, but not these:
1. At most **3 tasks** shown to a client at once, each one photo, one tap or a few words.
2. **No time estimates** on forms, tasks or documents.
3. **Every look is logged and shown** to the client on their privacy page, including "view as" and emergency (break-glass) access. Break-glass also sends the client an email the same day.
4. **Quiet hours** apply to texts and messages, except for a CQC or tender deadline.
5. **Reviews:** every registered client is invited, once, with one reminder; no incentives; no filtering of unhappy clients.
6. **Growth offers:** only confirmed prices from the price book, no false urgency, no "free", no guarantees, never more than one new suggestion a month, and none before registration except the services the client already chose.
7. **Complaints** always go to a director, never to the person complained about, with acknowledgement within 1 working day (section 49.2).
8. **Logins** never appear in messages, emails, exports or AI tools, and are handed back when the work ends.

### 51.5 Super admin settings that shape the client experience
| Super admin area (section 46.1) | What the client notices |
|---|---|
| Packages and price book | Which tracks appear in Journey, the done-for-you list, and the prices shown in Aftercare |
| Journey templates and forms | The 3 questions, small tasks and their wording, and when each task arrives |
| Emails and messages | Every email in the library, signatures, quiet hours |
| Automation rules | Reminders, the Friday update, CQC email alerts; failures go to staff, never to the client as an error |
| Integrations | Company search, address checks, the business email connection, signing and the interview link |
| Branding | Logo, colours and wording in the Hub, emails and documents |
| Data and retention | "How long we keep things" and "Download everything" on the privacy page |
| Security and audit | The "Every time we looked" list on the privacy page |
| View as | Staff can see exactly what the client sees; the client sees that it happened |

### 51.6 Emails added to the library
1.2 Lovely to speak to you (after the introduction call), 1.3 the introduction call texts (sorry we missed you, call back confirmed), 2.5 Your manager's invite (sent to the manager), 2.6 Business email connected, 3.4 Session booked and reminders, 7.0 Tender submitted (with the portal receipt), 9.1 Emergency access to your account, 9.2 We have received your concern, and 9.3 Your new consultant.

### 51.7 Screens added for forms, outside links and staff tools
| Board | Screen | What it shows |
|---|---|---|
| 34 | Snap and send | Camera with edge detection, then "Is this right?" with the details read from the photo, then done. Address cross-checked against the company record and tenancy. Nothing is used until staff confirm |
| 35 | Who you will support | Tap-to-choose groups with a live preview of the Statement of Purpose sentence and the documents that update with it (scope knock-on, section 47.2). Choosing children triggers a call with the consultant |
| 36 | Directors and owners | Directors from Companies House with their identity verification status, the 25% ownership question, and a text link for any director still to verify |
| 37 | One-task links | What a landlord, referee or accountant sees: no account, one ready-made letter or three questions, sign or answer, done. Link expires in 14 days |
| 38 | Tender in small pieces | Choose lots (with the consultant's suggestion), tell a story by voice note, and add our bid lead to the portal with no password shared |
| 39 | Brand and website | Logo, colours and tone as three choices, with a live preview of the home page |
| 40 | Sign in | Magic link by email or a code by text. No password |
| 41 | Notifications | "Needs you" and "Everything", matching the client's real tasks and news |
| 42 | Client page (staff) | One client in one place: waiting on client, waiting on us, Pack Doctor, timeline, how the client likes to work, people, access and money, sales notes, and "View as" |
| 43 | Manager dashboard | What needs a manager today, payment-to-first-call time, submissions and registrations, how clients feel, clients by stage, team load and money |
| 44 | Form builder (super admin) | Packages and the sections each one gets, who answers, when each arrives, the questions, and the guardrails. Drafts need the other super admin to publish |
| 45 | Small tasks | Insurance, business plan money (or send to the accountant), interview details read from CQC's email, "not formed yet", and the declaration |

---

## 52. Payment, the introduction call and the relationship signal

The first human moment matters most. As soon as a client pays, someone from Care Sync rings to say hello. It is an introduction, not a sales call. Today that is usually Divine, but it is built as a **task** so anyone can take it.

### 52.1 The moment payment lands
In this order, automatically:
1. **Payment confirmed.** Card or Direct Debit payments confirm themselves. A bank transfer is marked paid by finance with one click, which counts as the same event.
2. **Client set up.** The client record, Hub account and journey are created from the won deal (section 51.2, step 1), and the welcome email (1.1) goes with a magic link.
3. **Introduction call task created**, assigned to the default caller (Divine), due within the target time set by the super admin (suggested: within 2 working hours; if payment lands out of hours, by 10:00 the next working morning).
4. **Sales notes attached** to the task from GoHighLevel (section 52.5).
5. **Counted** on the manager's dashboard: calls due, calls overdue, and the time from payment to first conversation.

### 52.2 The introduction call task (board 33)
- **Owner:** Divine by default. Anyone can take it with one tap ("Who is calling"), and the previous owner is told. If the default caller is away, it goes to the backup callers set by the super admin, in turn.
- **On the task:** the client's name, role, number, best time to call, package, whether they have opened the welcome email and signed in, and the sales notes.
- **Call guide (8 steps, ticked as you go):** welcome by name and say thank you; introduce the team and what each person does; confirm what is included; do question 1 together in the Hub; ask about the office (the usual hold-up); explain that CQC works by email and the business email step; set honest expectations (CQC sets its own timescales, an update every Friday, the same day when CQC writes); book the kick-off with Millicent and ask how they like to be contacted. The guide never includes selling, and never promises a date or an outcome.
- **What the caller captures:** preferred contact method and times, anything about access needs (for example voice notes instead of reading), and a short note. These fill the client record, so the client is never asked twice.
- **Outcomes:**
  - **Spoke to the client:** a "lovely to speak to you" email (1.2) with the next 3 things, which the caller can edit before it goes; the caller records how the client sounded (happy, unsure or worried).
  - **No answer:** a friendly text goes straight away with a link to pick a time, and the next try becomes a task (suggested: later the same day, then the next working morning). **Never more than 3 calls.** After the third, an email is sent instead and the manager is told.
  - **Call back later:** the client picks or agrees a time, gets a text confirming it, and the task moves to that time with the notes kept.
  - **Something is wrong** (for example the client is unhappy or wants to change the package): the manager is told the same day and takes it from there.
- **Recording:** calls are only recorded or summarised with the client's consent (open question 25).

### 52.3 What the client sees
On the Welcome screen (board 25): "Divine will call you this morning. Just to say hello, answer any questions and help with question 1 if you like", the number we will ring, and "Pick a better time". Out of hours it says when the call will happen ("Divine will call you on Monday morning"). Divine also appears in "Your team" and on the privacy page, so the client knows who is calling and why.

### 52.4 The relationship signal
Care Sync should always know how each client feels, not just where their work is.
- **Where it comes from:** the introduction call (happy, unsure or worried), later calls and sessions, and a one-tap "How are we doing?" at three moments: after the kick-off, after submission and after the decision.
- **What it does:** unsure prompts the consultant to check in; **worried** tells the manager the same day, offers a call with a director, and **switches off all growth messages** for that client until it is resolved.
- **What it never does:** it is never used to decide who gets a review invitation. Every registered client is invited, exactly as section 37 says, so there is no review gating.

### 52.5 Sales to delivery handover
When a deal is won in GoHighLevel, the sales notes come with it: what the client wants and by when, any worries, deadlines (for example a lease date or a commissioner's timetable) and exactly what was promised. These appear on the introduction call and on the consultant's client page. Anything promised that is outside the package is flagged to the manager before work starts, so the client's expectations and the work always match.

### 52.6 Other client gaps closed
- **Payments visible to the client** (board 29): deposit paid with receipt, the next payment and when it is due, a reminder a week before, and every invoice and receipt to download (section 49.1).
- **People on the account** (board 29): the owner sees who else has access and what they can see, and can add a director or the accountant, who only see what is shared.
- **Consultant changes:** if the consultant changes, the client is told the same day by the new consultant (email 9.3), with the handover notes (section 11) so nothing has to be repeated.
- **How the client likes to work:** a short profile on every client record (contact method, best times, access needs, language preferences), filled from the introduction call and shown to everyone who works with them.

### 52.7 Super admin settings for the introduction call
Default caller (Divine) and backup callers, the target time after payment, working hours, the retry pattern (never more than 3 calls), the call guide and its versions, the summary email wording, and the recording consent wording. A new staff role, **Client care**, covers introduction calls and relationship check-ins.

---

## 53. Tenders as a service of their own (what real bids taught us)

Tender writing is a separate service. Many tender clients are established providers who never buy a registration, and some buy both. This section was written after reviewing the Tender and Tender Writing folders in Drive (a live Procurement Act 2023 framework bid with its technical and social value drafts, the buyer's published clarification log, selection and method statement questionnaires, evidence packs, the Client Tender Onboarding deck, the tender sales playbook and the staff tender writing course) and every question header of the Tender Preparation Questionnaire. No client details were copied.

### 53.1 Three kinds of tender client, one Hub
| Client | What they see | How it starts |
|---|---|---|
| **Tender only** (established provider) | A tender home (board 49): live bids, tenders matched for them, results, and their tender profile. Navigation is Today, Profile, Documents, Ask | Payment and the introduction call (section 52), then the tender profile pre-filled from Companies House and the CQC register |
| **Registration plus tender** | One Hub with two tracks. Journey shows Registration and Tender side by side, and every answer is shared, never asked twice | The tender profile is pre-filled from the registration record |
| **Retained** (several bids a year) | The same tender home, with bids used this year and the matches from the Tender Radar | Each new bid only asks what has changed |

### 53.2 Eligibility comes first
Real buyers set conditions that reject a bid before any answer is read. The Hub checks them at the bid decision and again after every clarification, per lot:
- **CQC registration** covering the regulated activity and client groups for that lot. A provider that is not yet registered can still bid for lots that are **not regulated** (for example community support), and join regulated lots later where the market stays open.
- **Operational presence**, for example an office in the county when the bid is submitted. Buyers have said in writing that a promise to open one after the award does not count.
- **Delivery history**, for example 3 years, judged at service level, not on one person's past jobs. New providers are steered to markets that accept new suppliers, and to **private client examples** as evidence.
- **Financial standing**, insurance levels, Central Digital Platform registration and share code, and any partners or subcontractors declared.

### 53.3 Should we bid? (board 50)
The client decides, lot by lot, with Care Sync's view beside each lot: which conditions are met, which are not, and why. For a registration plus tender client the Hub shows plainly which lots must wait for registration, and sets the reminder to join when they are registered. Declined matches are remembered, so they are not shown again.

### 53.4 The tender profile (board 48)
The Tender Preparation Questionnaire has 21 sections. The Hub keeps them as one reusable profile, filled once in small tasks and checked before every bid:
1. Tender details: portal link, reference and deadline read from the portal; authority to submit. **Portal usernames and passwords are never asked for**; Care Sync's bid lead is added as a portal user.
2. Company: legal and trading names, addresses, numbers, VAT, ICO, Central Digital Platform share code, trading status.
3. Regulator and registration: CQC, CIW or RQIA details, rating, inspection date, conditions, regulated activities and service types.
4. Who you support: bands, ages, criteria and specialisms.
5. Key people: contact, registered manager, nominated individual, directors or trustees.
6. Money: turnover for 2 years, accounts filed, what a new company can offer instead, insurance with expiry dates, the accountant.
7. Contract examples, with referee consent recorded.
8. **Private client examples** (initials only, with the family contact's permission), which matter most for new providers.
9. Your team: numbers, turnover, vacancies, Oliver McGowan training, **visa sponsorship**, drivers, languages, the lowest hourly rate (checked against the lawful wage), training, wellbeing, HR and care planning systems.
10. Partners and community, and what the client could commit to every year (social value).
11. Documents and policies held, who writes them, and a one-tap request for a policy quote.
12. Proof and stories: what makes the service different, outcomes, figures for the last 12 months, accreditations, praise, 4 to 6 case studies (by voice note), and any concerns about the tender.
13. Lots and capacity: which lots, hours they could take if they won everything, staff, and who leads the start-up.
14. How you deliver, shown only for the settings in the lots: home care (areas, travel time, shortest visit, double-handed visits, nights, scheduling); supported living (model, nights, and the property, who provides it and its features); care home (beds, rooms, specialisms); community support (types, personal care, areas, hours).
15. Declaration and consent.

### 53.5 The Hub is the CRM, not the writing tool
Bids are written in Word by the bid team and submitted on the buyer's portal. The Hub keeps the **tender record** (board 11) so everyone knows exactly what is happening:
- **Which tender:** buyer, reference, portal link, lots (bidding or not, and why), estimated value, clarification deadline, buyer's deadline, Care Sync's own submission date and when the result is expected.
- **Stage:** found, bid decision, onboarding, writing, client review, submitted, result.
- **Tasks and deadlines** with an owner each, planned back from the buyer's deadline (section 19.2), including the client's own tasks.
- **Files:** the tender pack from the portal, each draft version (Word), the client's documents, the final submitted copy and the portal receipt.
- **Notes and messages:** every client conversation, eligibility decisions, and buyer clarifications that affect the bid.
- **People:** bid lead, second reviewer, the client's decision maker and who reads the portal inbox.
- **Result:** won or not, the score, the feedback file, and when the framework or market reopens.

### 53.6 What the client sees
The client's tender home (board 49) and tender detail (board 31) show the deadline countdown, what is waiting on them, drafts to review as Word documents, the files they have sent, and the result. Comments on drafts can be left in the Hub or on a call.

### 53.7 After submission
Questions during evaluation (answered within the buyer's deadline), presentations or interviews (with a practice session first), the intention to award and the standstill period, and the **assessment summary** with scores for each question, which is stored on the tender record. A win turns the commitments noted on the tender record into the start-up checklist. A loss gives three improved answers and a reminder when the framework or market reopens.

### 53.8 Staff tender writing course
The Week 1 and Week 2 course in Drive (what a tender is, questionnaire and method statement masterclasses, practice questions with marked feedback rounds) becomes a track in the Care Sync Academy (section 48). A new writer drafts practice answers against real scoring bands, gets marked feedback in rounds, and is signed off before writing for a client.

### 53.9 Emails added
7.3 Should we bid (your decision needed), 7.4 The buyer changed something that affects your bid, and 7.5 A framework or market you can join is open again.

---

## 54. Complete onboarding: every question, stop and come back

The Hub asks **every** question on Care Sync's CQC and tender forms, nothing less (Appendix C and Appendix D), but never as one long form. Clients can do it all in one sitting, a little at a time, or with us on a call, and always pick up exactly where they stopped.

### 54.0 When it is sent, and why it matters
The onboarding form is what the whole project runs on. **No CQC writing, and no project work, starts until it is complete** and the onboarding gate is passed (section 18).
1. **The client is added with their package.** Most clients arrive from a won deal in GoHighLevel with the details filled in; a super admin (or staff with permission) can also add one by hand (board 51). The package or packages chosen decide exactly which sections the onboarding form contains (section 31.1). Shared sections appear once even across two packages, and "setting up your company" appears only if the company is not formed yet.
2. **Payment lands** and the introduction call task is created (section 52).
3. **On the introduction call** the caller starts the onboarding form with the client and does section 1 together.
4. **Straight after the call**, the tailored onboarding form is sent (email 2.1). If the call cannot happen, it is sent the next working morning so nothing waits.
5. **The client completes it**, just like the Google Form they fill in today: the same sections, the same questions, the same wording and the same branching (board 47). They can stop and come back any time, with gentle reminders. If they prefer, they can send a section to someone else to fill in (for example their manager), but by default the client fills in everything.
6. **The onboarding lead checks it.** When every required section is complete and the gate checks pass, the project starts and the client sees "We have started your CQC pack". Sections that only make sense later (for example interview details, or business plan money questions) are marked "opens later" and never hold up the start.

If the package changes later (for example a supported living add-on or a tender), only the new sections are added to the same form, pre-filled from what is already known.

### 54.1 One home for the whole form (board 46)
"Your onboarding form" lists the sections of the client's form. For CQC registrations these are the sections of the CQC Registration Information Form: 1 your company; 2 company details (or setting up your company, if not formed); 3 directors; 4 your service; 5 Registered Manager; 6 Registered Manager addresses; 7 Registered Manager GP; 8 Registered Manager referee; 9 Registered Manager ID and DBS; 10 Nominated Individual; 11 Nominated Individual addresses, ID and DBS (only if a different person); 12 declaration and signature. A tender client gets the Tender Preparation Questionnaire. CIW and RQIA clients get their own forms once their questions are mapped. Anything a package needs that is not on the current forms (for example brand and website for the full start-up package) is shown as an extra, to confirm. Each section shows its status in plain words:
- **Done**, with what was filled in for the client ("Filled in from Companies House");
- **In progress**, with the exact step ("Ruth: 5 of 8 steps. Stopped at 'Your GP'");
- **Waiting for** a named person ("Waiting for Peter");
- **Not needed**, with the reason ("Your company is already formed");
- **Opens later** ("Last of all. Opens when the rest is done").

Tapping a section shows every question in it, ticked or not, so nothing is hidden. The tender profile (board 48) works the same way for the 15 sections of the tender form.

### 54.2 Save and resume rules
1. **Every answer saves the moment it is given**, on the server, not in the browser. There is no "save" button to forget and nothing is lost if the phone dies.
2. **Resume point:** the first unanswered question in the section the person last used. It appears as "Carry on where you left off" on Today, on the section list and in the reminder email.
3. **Welcome back:** returning to a section shows what is already saved and how many steps are left, with "Carry on" and "Look over my answers first" (board 47).
4. **Save and finish later** is always one tap away. The Hub confirms it is saved, says where they will pick up, and sends one gentle reminder outside quiet hours.
5. **Any device:** the same magic link works on a phone, tablet or computer.
6. **The client fills in the whole form**, as on the Google Form. If they choose to send a section to someone else (for example their manager or landlord), that person gets their own link and their own resume point.
7. **Never asked twice:** answers already known (Companies House, the sale, the introduction call, photos read, earlier sections, earlier tenders) are filled in for the person to check.
8. **Branching:** company already formed hides the formation section; the same person as manager and nominated individual completes the nominated individual section in one tap; "DBS not done yet" hands the task to Care Sync; "no professional registration" skips that step; tender settings appear only for the lots chosen.
8a. **Smart rules taken from the forms themselves:** the same person as Registered Manager and Nominated Individual means the Nominated Individual pages are skipped; a DBS already done means only the certificate number, issue date and upload are asked, with no ID documents and no address history (those are only for a new DBS application); a DBS older than 12 months is flagged and switches to the application details; no professional registration skips that page; a company that is not yet formed gets the set-up pages with SIC codes worked out from the ticks; a returning tender client answers only "what has changed" and this tender's pages.
9. **Checks as you go:** UK date format, no impossible dates (such as a DBS issue date in the future), 12-digit DBS numbers, postcode lookup with UPRNs, a 5-year address timeline with gap detection, three accepted ID types, documents dated within 3 months where required, unlimited directors and examples.
10. **Do it on a call:** a staff member can complete any section with the client on the phone, in the same fields, and the client just checks and signs.
11. **Staff see exactly where everyone stopped,** and the onboarding gate (board 8) shows what is still missing.
12. **The declaration opens last,** only when every other section is complete, and is signed electronically.
13. **Download:** a PDF of all answers can be produced at any time (section 26.4), for the client and for the file.

---

## 55. Open questions for Care Sync

1. **Email system:** Does the team use Google Workspace or Microsoft 365 for Care Sync mailboxes?
2. **Submission by email:** Is it correct that the consultant sends the application by email and the Hub only records it? Are there any other parts of the process that must stay on email?
3. **Other regulators (partly answered):** CIW and RQIA are now covered (Appendices E and F). Do you also deliver Ofsted work?
4. **Team size and volume:** Roughly how many staff, and how many active clients at once now and in 12 months?
5. **Retention period:** How long should identity documents and DBS certificates be kept after a journey ends?
6. **Payments:** Should clients pay (for example for extra sessions) inside the Hub, or does payment stay in your current system?
7. **GoHighLevel:** Answered: it is the sales CRM. Confirm that a won deal (signed agreement and paid deposit) should start a Hub journey automatically.
8. **Interview Preparation Hub:** What system does it run on, and can new client accounts be created automatically (for example through an API or an invite link)?
9. **Reply times:** What reply time should the Hub promise clients for questions (for example 1 working day), and for staff "Ask a senior" questions?
10. **Price book items marked Pending:** retained tender rate, policy fees, variation prices, bid review VAT, and mock inspection and marketing prices for registration-only clients.
11. **Logins spreadsheet:** agree to move it into a password manager now, before the Hub is live.
12. **Tender form passwords:** agree to remove the portal username and password questions from the Google Form now.
13. **Interim PDF script:** would you like the Google Forms Apps Script (section 26.4) built now, so every submission produces a downloadable PDF before the Hub exists?
14. **Data services:** confirm Care Sync is happy to register for a Companies House API key (no charge), an Ordnance Survey Places API account (usage-based pricing, to be confirmed with Ordnance Survey) and to pay HM Land Registry's per-title fee when a title register check is needed.
15. **WhatsApp updates:** confirm whether client updates by WhatsApp are wanted, using the Care Sync business number.
16. **Growth programme:** prices for the retained options, the referral thank-you, and whether to post a card on registration day.
17. **Partner directory:** which partners to list, and any referral arrangements to disclose.
18. **Reviews:** confirm the Google Business Profile review link and the Trustpilot plan (free, 50 invitations a month, or paid), and agree the written reviews policy.
19. **Document editing:** do staff edit in Microsoft Word or Google Docs today, so the Hub can connect to the right one?
20. **Email accounts:** which email services do clients' accounts use (Gmail, Google Workspace, Microsoft 365, other)? This decides how the mailbox connection is built.
21. **Written authority:** agree the engagement letter wording that authorises Care Sync to hold the client's email login and to send and receive CQC emails on their behalf.
22. **Password manager now:** choose a business password manager for the interim vault.
23. **Payments:** which payment provider (for example Stripe or GoCardless) and the standard instalment schedule, so "accept, sign and pay" can be built.
24. **Third-party links:** agree the wording clients approve before the Hub contacts their landlord, lender, referee or accountant.
25. **Call recording:** agree the consent wording for recording and summarising calls.
26. **Super admins:** confirm who holds the two super admin accounts (section 46), and who approves a break-glass request when one of them is away.
27. **Accounting software:** do you invoice in Xero, QuickBooks or another system, so invoices, deposits and instalments can sync (section 49.1)?
28. **Partner access:** confirm that AssuredBid and any other partners should get limited partner logins, and what each partner may see (section 49.3).
29. **Inconsistencies:** agree the correct founding year, whether "Comprehensive Training" stays on the website, and the evidence behind the "former CQC senior inspector" wording (section 50), so the Hub, emails and sales scripts all say the same thing.
30. **Answered: CIW and RQIA onboarding forms.** Both were exported from Drive and rebuilt (Appendices E and F).
31. **Refusal library:** confirm we may turn the anonymised reasons from past CQC refusals into Pack Doctor rules (section 47), with no client names kept.
32. **Sessions:** confirm Millicent runs all 3 sessions, including the kick-off, and whether extra sessions can be bought (and the price).
33. **Aftercare rhythm:** confirm a monthly check-in for the 12 months of aftercare, and who leads it.
34. **Complaints:** agree the full response target after the 1 working day acknowledgement, and which director handles complaints.
35. **Default quiet hours:** confirm 8pm to 8am as the default for texts and messages.
36. **Introduction calls:** confirm Divine as the default caller, who the backup callers are, and the target time after payment (suggested: within 2 working hours, or by 10:00 the next working morning).
37. **Phone system:** should introduction calls be made through GoHighLevel's phone system (so they are logged automatically) or from staff mobiles?
38. **Deposits:** which payment methods are accepted for the deposit, and who marks bank transfers as paid.
39. **Tender prices:** confirm the retained tender package price, whether bid review is plus VAT, and the price for joining a dynamic market or framework application (often shorter than a full tender).
40. **Visa sponsorship questions:** confirm the tender profile should ask how many staff are sponsored and the licence status, since buyers increasingly ask about workforce stability.
41. **Tender writing course:** confirm the Week 1 and Week 2 course should become the Academy track, and who marks practice answers.
42. **Questions beyond the form:** CQC's own registered manager application also covers employment history, qualifications and other roles held. Should the Hub collect these too (for example from the CV photo), or does Care Sync gather them separately today?
43. **More than one referee:** the form asks for one referee for the manager. Confirm whether a second referee should be asked for.
44. **CIW and RQIA forms (done, Appendices E and F):** confirm the changes: the full 12-digit DBS number, CIW Online's hours bands, the Wales client groups, and the questions marked "Added by the Hub".
45. **Decided: the Hub stays in English for CIW clients.** The CIW form still asks the client's preferred language for CIW's own calls and letters.
46. **Testing with clients:** which three clients (one CQC, one tender, one with both) could try the boards before building starts?
47. **Address history length:** both forms ask for 5 years. Care Sync's CIW guidance mentions 10 years for some people. Which should the Hub ask for?
48. **Answered: ID documents.** Three for all three regulators, including at least one photo ID and one proof of current address (see question 55).
49. **RQIA PIN:** is 497850 still the PIN to give for new AccessNI checks?
50. **RQIA price:** the RQIA package document says £3,500, while the Hub's price book shows £4,500 + VAT. Which is current?
51. **Answered: other officers in Wales.** CIW Online keeps a full People record for every officer, with the same nine sections as the RI (personal information, qualifications, employment history, registration history, references, DBS, declarations, suitability questions, submission declarations). The officer list asks the applicant to confirm all officers are fit and proper under section 9. The form now has two pages for each officer who is not the RI. Source: Care Sync's CIW form-filler skill, references 06f and 06h (walked on the live portal).
52. **Answered, to confirm once with RQIA: AccessNI.** RQIA checks the owners and senior managers it registers through its own AccessNI application, hence the PIN. AccessNI has no update service, so a certificate does not move with the person. The form now always collects three ID documents, and certificate details are optional. RQIA's own guidance could not be opened from here, so ask the registration team to confirm once (registration@rqia.org.uk, 028 9051 7500).
53. **Answered: RQIA referee rule.** Schedule 2 of the Domiciliary Care Agencies Regulations (Northern Ireland) 2007 asks for "two written references relating to the person, including a reference from the person's present or most recent employer, if any". The form uses this wording and offers "there is no previous employer". The "last period of employment of not less than three months" wording is from the Nursing Agencies Regulations (Northern Ireland) 2005, not the domiciliary care rules.
54. **Answered: sole traders and partnerships.**
    - **Wales:** where the provider is an individual, they are the RI (CIW guidance on section 21). In a partnership, the RI must be one of the partners. For a company, the RI is normally a director or similar officer. CIW Online also allows a non-officer RI to be added to the officers list.
    - **Northern Ireland (regulation 8):** a sole trader carries on the agency and must be fit themselves. An organisation's RI must be a director, manager, secretary or other officer, which is wider than the old form's "director, partner, or trustee". In a partnership, the partners carry on the agency and one partner takes the lead, for example on training.
    - The forms now say this for each type.
55. **Answered: ID documents.** The DBS rules changed on 22 April 2025, and the transition ended on 1 November 2025.
    - eVisas are accepted, checked online with a share code.
    - An expired biometric residence permit showing indefinite leave can still be used for ID for up to 18 months after its expiry.
    - DBS and AccessNI both need three documents, including at least one photo ID and at least one showing the current address.
    - The CIW and RQIA lists now say this, and RQIA's "two" is now three. This also answers question 48 for RQIA.
    - The CQC form's list now uses the same wording.

---

## 56. Client design audit: is everything there before we build?

Done on 4 November 2026, board by board, against the client's whole life with Care Sync. The question each time: could a developer build this screen from the board and this spec without guessing?

### 56.1 Every client moment and the board that shows it

| When | What the client does or sees | Board |
| --- | --- | --- |
| Before payment | Nothing in the Hub. Sales stays in GoHighLevel | None needed |
| Payment made | Welcome email, then sign in with a link (no password) | Email 1.1, 40 |
| First sign-in | Privacy consent, then the welcome moment and the team | 53, 25 |
| Introduction call | Staff task (Divine by default, anyone can take it); client gets the confirmation text | 33, email 1.3 |
| Onboarding form sent | Form home tailored to the package, with the sections listed | 46 |
| Filling in the form | The real CQC, CIW or RQIA form, or the tender questionnaire: every question and rule, save and come back, check your answers | 47, 55, 56, 38, 54 (computer) |
| Form helpers | Company search, snap and send, who you will support, directors | 23, 34, 35, 36 (inside the form) |
| Form sent | Being checked, something to fix, project started | 52 |
| Every day | Today, with what is waiting on you and what we did | 1, 54 (computer) |
| Two services | Project switcher for a registration plus tenders | 1, 54 |
| The journey | All 11 stages and where they are | 2 |
| Evidence | Documents, the documents room, one quick question about an address | 3, 18, 15 |
| Other people | One-task links for landlord, referee and accountant; invited manager | 37 |
| Business email | Connect the CQC channel | 27 |
| Drafts | Review Room, then sign once | 4, 19 |
| Sessions | Book and move sessions with Millicent | 28 |
| Questions | Ask Care Sync; the bell | 6, 41 |
| CQC | Before, question asked, returned, interview, registered | 5 |
| Registered | Celebration, the email, share your experience | 20, 17 |
| After | Aftercare and growing; done for you checklist | 30, 21 |
| Tenders | Tender home, tender profile, should we bid, a tender's page | 49, 48, 50, 31 |
| Money, insurance, interview | Small tasks | 45 |
| Brand and website | Three choices (full package only) | 39 |
| Account | Account, privacy, the audit log in plain words | 29 |
| Anything going wrong | Link expired, empty, no news from CQC, upload problems, offline, error | 53 |
| Payments and feedback | Second payment, payment received, how are we doing, raise a concern, pause reminders, help, refer someone | 53 |

### 56.2 Boards kept only as history

Board titles on the canvas now say this too.

- 12 (manager's own part), 16 (easy start) and 26 (manager question) were early ideas. They split the form per person and changed the questions. The real form (47) replaces them, because everyone is onboarded with the same form.
- 23, 34, 35 and 36 are helpers inside a form question, not extra steps.
- 45 keeps insurance, money and interview. "Not formed yet" and the declaration are now pages of 47.

### 56.3 Devices

- Phone first (390 wide) for every client screen.
- Computer (1440 wide): the side menu, a two-column Today, and the form with the page list on the left and "why we ask" on the right (board 54). Every other screen uses the same parts at the wider width. No extra boards are needed.
- One web app that works on both, added to the home screen. No app store app in Phase 1.

### 56.4 Handoff checklist for every client screen

A screen is ready to build only when it passes all of these:

1. **Words.** British English, no dashes, plain words a carer would use, they/them for anyone whose pronouns we do not know, and no promise we cannot keep (times, prices, outcomes).
2. **States.** Loading, empty, error, offline and "done" are shown on the board or in 53.
3. **Touch.** Every button and link is at least 44 by 44, with a visible focus ring.
4. **Accessibility.** WCAG 2.2 AA: contrast, labels on every field, errors said in words and not only colour, works with a screen reader and a keyboard, nothing moves on its own.
5. **Dark mode.** Uses only the Care Sync tokens, so the theme switch works. Check each board with the theme property set to dark.
6. **Super admin.** Anything the client sees has a matching control or record on the staff side (51, 42, 24).
7. **Data.** Mockups use made-up people only. No real client details anywhere.
8. **Save.** Anything the client types is saved as they go and is still there when they come back.

### 56.5 Still open before the client side is truly finished

- The CIW and RQIA forms are now done (boards 55 and 56, Appendices E and F). Confirm the changes (questions 44 and 47 to 50).
- Test the boards with three real clients before building: one CQC, one tender and one with both (question 46).

## 57. Client tests, 4 November 2026

Three example clients were walked through the screens by independent reviewers, each playing one person honestly:
- **Amara:** a first-time CQC applicant, using only her phone, with English as her second language.
- **Kemi:** an established provider who buys tenders only.
- **David:** a co-director with both a CQC registration and tenders, on a computer.

This is not a replacement for real clients (question 46), but it found real problems.

### 57.1 Fixed straight away

- **Staff notes hidden from clients:**
  - "our Google Form" and "(not on the current form, to confirm)"
  - "creates a quote task for sales"
  - CQC form reference numbers
  - "Added by the Hub"
- **Welcome depends on the package:** registration, tenders only, or both. A tender-only client no longer sees CQC wording, coaching sessions or the registration team, and meets their bid lead instead. The "never more than 3 at a time" promise now says the form comes first.
- **CQC form:**
  - The Companies House identity code no longer blocks the form. It explains how to get the code and that it is needed before the company is registered, not before the form is finished.
  - Second and third company names are optional.
  - A reassurance box for anyone worried about asking their current employer for a reference.
  - A plain-words DBS check ("had a DBS for a care job in the last 12 months? Send a photo").
  - Plain explanations of Registered Manager and Nominated Individual, and "(who you will support)" on the service user bands.
- **All forms:**
  - The last button says "Send to Care Sync".
  - The thank-you screen no longer sounds like the regulator has it.
  - "1 page" in the singular.
  - Returning tender clients see "kept from last time" instead of "did not apply".
- **Tender form:**
  - "Have you done this before?" is answered for signed-in clients.
  - New companies can say they are not trading yet.
- **Form home:** clean tender section names (no "6. 6D."), a description for each, the right resume point, and a banner that matches the package.
- **Today:**
  - One measure, not four: "3 small things need you" and the stage.
  - Tenders show "Opens after registration" for a client who has both.
- **Consistency across screens:**
  - Policies are "written, ready for your review" everywhere, not "approved" in one place and "being written" in another.
  - Session 2 shows the same date everywhere.
  - The onboarding form shows the same completion date everywhere.
  - The team lists match.
  - The computer view's tender card counts the tender tasks.
  - "We send your application to CQC", not "email".
- **Money:** the account shows the package total, what is paid, what is left and when, and that extras are always priced first. The amounts are examples until the price book and the instalment schedule are confirmed (questions 10 and 23).
- **People:** a co-director gets their own sign-in, sees everything and has their own tasks.
- **Help:** a phone number at the top of Ask.
- **Documents:** "Proof this is your home" replaces "Proof you can live there legally".

### 57.2 Still to design (in priority order)

1. **Tender-only screens:**
   - A tender document store, with expiry dates and where each document was used.
   - A tender draft review and a single "approve for submission" step, instead of the CQC Review and Sign screens.
   - One list of "what we need from you this week" across all bids, with dates.
2. **One tender profile.** The form home, the questionnaire and the tender profile should be one source of truth. Each new tender asks only for what is missing. Show held answers to confirm, not an empty "what has changed" box.
3. **A joined-up timeline for clients with both services.** Which tenders open up after registration, with target dates. The bid decision screen already explains this well.
4. **Timelines and money in one place:**
   - a target submission date and a typical range for the regulator's decision
   - the earliest realistic date for a first tender
   - what happens and what it costs if CQC refuses (notice of decision, appeal)
5. **Address history as cards** with postcode lookup, month and year pickers, "add another address" and gap warnings. This is a build requirement for every form.
6. **An "I am not sure, ask us" link on every form question**, and a time estimate for each section.
7. **Security page:** where data is stored, Care Sync's ICO registration, two-step sign-in for directors, and when ID copies are deleted. On the email connection screen, lead with "we set one up for you".
8. **Supported living:**
   - the CQC supported living package needs questions about the properties, the landlord and how housing and care are kept separate
   - the tender form needs a short start-up route that reuses onboarding answers
9. **Past bids:** scores, feedback and reusable answers, win rate and contract renewal dates, so a client is warned before a re-tender.
10. **Language help** (read aloud, translation) and WhatsApp updates, once question 15 is decided.

## Appendix C. CQC Registration Information Form: every page, question and rule

Source: the live Google Form "CQC Registration Information Form, for Domiciliary Care / Supported Living CQC Applications" (hello@caresyncexperts.co.uk), exported from Google Drive on 4 November 2026. The Hub form (board 47) uses the same pages, questions, wording, options and rules, and the client fills it in just like the Google Form. No answers were copied. Required questions are marked *.

| # | Page | Show this page | Questions (wording as on the form) | Options | Hub additions |
|---|---|---|---|---|---|
| 1 | Company Registration Status | Always | Is your limited company already registered with Companies House? | Yes, my company is already registered with Companies House / No, please register the company for me as part of my CQC package | Company search fills page 2 |
| 2 | Company Information | Company registered = Yes | Registered Business Name; Trading Name (if different); Company Registration Number (if applicable); Registered Office Address; Correspondence Address (if different); Business Telephone Number *; Company Email Address; Website (if applicable); Type of Legal Entity; Partners or owners who are not directors (if any) | | Filled in from Companies House for the client to check |
| 2a | Care Sync to Set Up Your Limited Company: Service Type and SIC Codes, Company Name Choices | Company registered = No | What care service type are you registering for? *; 1st choice company name *; 2nd choice company name *; 3rd choice company name *; Trading name preference | Service type: Domiciliary care / Supported living / Care home with nursing / Children services or any service for under-18s / Specialist Learning Disability, Autism or Mental Health service | SIC codes worked out from the ticks and shown (88100, 87900, 88910, 87200, 87100), exactly as the form explains |
| 2b | Company Basics, Director 1 (Lead Director), Additional Directors | Company registered = No | Type of company *; Registered office address *; Director 1: Full legal name *, Date of birth *, Nationality *, Country of residence *, Service address *, Occupation *, Companies House Identity Verification Code *; Additional director details | Type: Private limited company by shares (Ltd) / by guarantee / Limited Liability Partnership (LLP) / Other | Identity code checked for 11 characters; link to the verification guide |
| 2c | Persons with Significant Control, Share Structure, Communications, Authorisation | Company registered = No | Are the directors also the PSCs? *; PSC details (only if different); Number of shares *; Value per share *; Will a single owner hold 100% of shares? *; Share split (only if multiple owners); Email address for Companies House notices *; Mobile number for the lead director *; Authorisation to incorporate *; Confirmation of accuracy * | PSC: Yes, the directors are the PSCs / No, the PSCs are different people. Shares: Yes, single owner with 100% / No, multiple owners | PSC details and share split appear only when needed |
| 3 | Directors 1 to 4 | Always; each next director when "Is there another director?" = Yes | Director N: Full name *, Date of birth *, Mobile number *, Email address *; Is there another director? *; More than four directors? | Yes / No | Director 1 filled in from Companies House or the lead director; never typed twice |
| 4 | Primary Service Type and CQC Service User Bands | Always | Which CQC-regulated activities will you provide?; CQC Service User Bands | Activities: Personal Care (Domiciliary Care) / Personal Care (Supported Living) / Personal Care and Nursing (Supported Living) / Accommodation for persons who require nursing or personal care / Other. Bands: Adults aged 18 to 65 / Adults aged 65+ / Physical disability / Dementia / Mental health / Sensory impairment / People detained under the Mental Health Act / People who misuse drugs or alcohol / People with an eating disorder / Learning disabilities and or autistic people / Children and young people aged 0 to 18 / The whole population / Other | Bands feed the Statement of Purpose and training plan |
| 5 | Registered Manager Details | Always | What is your title? *; Full Name *; Date of Birth *; Email Address *; Mobile Number *; Current Address *; Is the Registered Manager currently registered with a health or social care professional body? * | Title: Mr / Mrs / Miss / Ms / Mx / Dr. Professional body: Yes / No | CV uploaded here (the form asks for it to be submitted separately) |
| 6 | Registered Manager Professional Registration | Professional body = Yes | Professional body *; Professional registration number * | NMC / Social Work England / HCPC / GMC / GPhC / GDC / GOC / GOsC / GCC / PSNI / Other UK or overseas body | Number checked on the public register |
| 7 | GP Details (Registered Manager only, CQC section 1.12) | Always | GP's name *; Surgery (Practice name) *; Surgery address line 1 *; Surgery address line 2 *; GP Surgery Town/city *; County; Postcode *; Do you give permission for CQC to contact your doctor or their surgery? * | Yes / No | Searching the surgery can fill the address |
| 8 | Reference Details (Registered Manager only, CQC section 1.16) | Always | Referee's title *, first name *, last name *, address line 1 *, address line 2 *, Town/city *, Postcode *, email address *, telephone number *; Do you give permission for CQC to contact your referee? * | Yes / No | The form's "must be the last employer" rules shown on the page |
| 9 | Registered Manager and Nominated Individual Confirmation | Always | Will the same person serve as both your Registered Manager AND Nominated Individual? * | Yes, the same person serves as both / No, different people | Yes: pages 10 to 14 are skipped and nothing is entered twice |
| 10 | Nominated Individual Details | Same person = No | Full Name *; Date of Birth *; Email Address *; Mobile Number *; Current Address *; Is the Nominated Individual currently registered with a health or social care professional body? * | Yes / No | Filled in from the directors where possible; CV uploaded here |
| 11 | Nominated Individual Professional Registration | Same person = No and professional body = Yes | Professional body *; Professional registration number * | Same 11 bodies | Checked on the public register |
| 12 | DBS Check for Nominated Individual | Same person = No | Have you already completed an Enhanced DBS check for the Nominated Individual with the Adult Workforce barred list and a countersignature? * | Yes, the DBS check has already been completed / No, the DBS check has not yet been done (Care Sync will help with the application) | |
| 13 | Nominated Individual DBS Certificate Details | Same person = No and DBS done | DBS Certificate Number *; DBS Issue Date *; DBS Certificate Upload * | | 12 digits; issue date within the last 12 months. **No ID or address history asked** |
| 14 | Nominated Individual: DBS application details and 5-year address history | Same person = No and DBS not done | Select the three forms of identification you can provide *; Address 1 (current) *; Addresses 2 to 5 | Current valid passport / Driving licence photocard / Biometric residence permit (if applicable) / Utility Bill / Bank Statement / Council Tax | Exactly three IDs; more than five addresses can be added in the Hub instead of emailed |
| 15 | DBS Check for Registered Manager | Always (covers the one person if the same) | Have you already completed an Enhanced DBS check for the Registered Manager with the Adult Workforce barred list and a countersignature? | Yes / No (Care Sync will help) | |
| 16 | Registered Manager DBS Certificate Details | DBS done | DBS Certificate Number *; DBS Issue Date *; DBS Certificate Upload * | | 12 digits; an issue date older than 12 months is flagged and the application details are asked instead. **No ID or address history asked** |
| 17 | Registered Manager: DBS application details and 5-year address history | DBS not done | Select the three forms of identification you can provide *; Address 1 (current) *; Addresses 2 to 5; attach a sheet if more than 5 addresses | Same 6 ID options | Gaps in the 5 years spotted for you |
| 18 | Declaration | Always, last | Declaration statement; Signatory: Full Name; Position in Organisation; Signature; Date | | Electronic signature |

Examples of the smart path: a sole director who is also the manager, with a DBS already done, sees 12 pages. They never enter the nominated individual's details, never give ID documents, and never give an address history. A company that is not yet formed, with different people and no DBS yet, sees up to 18 pages.

## Appendix D. Tender Preparation Questionnaire: every page, question and rule

Source: the live Google Form "Care Sync Experts, Tender Preparation Questionnaire" (hello@caresyncexperts.co.uk), exported from Google Drive on 4 November 2026. The Hub form (board 38) uses the same pages, questions, wording, options and rules.

| Page | Show this page | Questions | Notes and options |
|---|---|---|---|
| This tender | Always | 1.1 Link to the tender portal; 1.2 Tender name or reference number *; 1.3 Closing date and time *; 1.4 Portal username; 1.5 Portal password; 1.6 Registered on the portal already? *; 1.7 Saved PDF copies of the tender documents?; 1.8 Authority to submit *; 1.9 Completed this form before? * | 1.5 goes straight into the encrypted vault, and adding the bid lead as a portal user is offered first. 1.6: Yes, fully registered / Started but not finished / Not yet registered / Not sure |
| What has changed | 1.9 = "Yes, for an earlier tender" | R.1 What has changed since you last filled in this form? *; new or renewed documents | All profile pages below are skipped: last time's answers are kept |
| About your company | First time | 3.1 to 3.16 (legal name *, trading name, registered office *, service delivery address, phone *, email *, website, date registered, company number, charity number, VAT number, ICO number, Central Digital Platform registration, share code, DUNS, trading status *) | 3.14 share code only when 3.13 = "Yes, and I have our share code". Filled in from Companies House |
| Your regulator | First time | 2.1 Which regulator? *; 2.2 More than one regulator? | CQC / CIW / RQIA / Ofsted / Care Inspectorate (Scotland) / Not yet registered, applying now / Not regulated |
| 4A, 5A, 6A CQC | 2.1 = CQC | 4A.1 to 4A.7; 5A.1 regulated activities (15 options); 5A.2 service types (15 options); 6A.1 service user bands (12 options) | 4A.7 only when conditions = Yes. Filled in from the CQC register |
| 4B, 5B, 6B CIW | 2.1 = CIW | 4B.1 to 4B.5 (including the 7 Regional Partnership Boards and the Welsh Active Offer); 5B.1 (11 service types); 6B.1 (11 needs) | |
| 4C, 5C, 6C RQIA | 2.1 = RQIA | 4C.1 to 4C.4 (5 HSC Trusts); 5C.1 (12 service types); 6C.1 (10 groups) | |
| 5D | 2.1 = Ofsted, Scotland, applying now or not regulated | 5D.1 Your services and registration position | Care Sync calls the client |
| 6D Ages and specialisms | First time | 6D.1 youngest age; 6D.2 oldest age; 6D.3 criteria; 6D.4 specialisms (28 options) | Numbers checked |
| 7 Key people | First time | 7.1 to 7.4 owner (7.1 *); 7.5 to 7.8 Nominated or Responsible Individual; 7.9 to 7.12 Registered Manager; 7.13 other senior staff | CVs uploaded here rather than emailed |
| Finance and insurance | First time | F.1 turnover *; F.2; F.3 accounts filed? *; F.4 alternatives; F.5 insurance cover and expiry *; F.6 accountant | F.4 only for a new company. Accounts status checked at Companies House |
| 8 Track record | First time | 8.1 experience *; contract example 1 (8.2 to 8.12); "another example?" * | Examples 2 (8.13 to 8.23) and 3 (8.24 to 8.34) each on their own page when "another?" = Yes. No examples page when 8.1 = Private clients only or None yet |
| Private client experience | First time | 8.A share private clients? *; PRIV1.1 to PRIV1.11; "another?" | Examples 2 and 3 on their own pages. Initials only |
| 9 Workforce | First time | 9.1 to 9.18 (9.1 *, 9.3 *, 9.13 *) | Visa sponsorship (9.10); lowest hourly rate checked against the lawful wage |
| 13 Partnerships and social value | First time | 13.1 (12 options) to 13.4 | |
| 14 Documents and policies | First time | 14.1 documents (22 options); 14.2 policies (13 options); 14.3; 14.4 policy quote? *; 14.5 | A "Yes" to 14.4 creates a quote task for sales. Documents uploaded here rather than emailed |
| Your evidence | First time | E.1 to E.7 (E.6 *) | |
| Lots | Always | L.1 *; L.2 *; L.3; L.4 | |
| Your services for this tender | Always | Home care? *; Supported living? *; Care home? *; Community support? * | Only the matching pages follow |
| Home care | Home care = Yes | 11.1 to 11.8 (11.2 *) | |
| Supported living | Supported living = Yes | 10.1 *; 10.2 *; 10.3; 10.4 * | |
| Supported living property | 10.4 = "We do, or our landlord partner does" | 10.5 to 10.19 (10.6 *) | Extra properties can be added in the Hub instead of a template |
| Care home | Care home = Yes | 12.1 * to 12.9 | 12.4 only for specialist provision |
| Community support | Community support = Yes | C.1 *; C.2 *; C.3 *; C.4 | |
| Sign-off | Always, last | 16.1 to 16.5, all * | |

A returning client sees 6 pages: this tender, what has changed, lots, services, the pages for their settings, and sign-off. A first-time client sees between 17 and 21 pages, depending on their regulator, examples and lots.

## Appendix E. CIW Registration Information Form: every page, question and rule

Rebuilt on 4 November 2026 from the live Google Form ("CIW Registration Information Form, Domiciliary Support Service, Wales"), then checked against what CIW Online actually asks for, using Care Sync's CIW form-filler skill (portal sections 1 to 9, the new client intake list and the rejection patterns). Board 55 shows it working. Every question on the live form is kept; a coverage check found all 108 questions and options in the board. The Hub, like CIW, is in English only.

### E.1 Problems found in the live form

| Problem | Fix in the Hub |
| --- | --- |
| DBS asks for the last 4 digits only. CIW checks the DBS online through the Update Service, so it needs the full 12-digit number | Full number, checked for 12 digits |
| "Update Service ID (if yes)" is a Yes or No question, so nobody can type the ID | A text box, shown only when the person is on the Update Service |
| Every DBS question is required even when the answer is "No DBS" | Certificate details only when Yes; three ID documents only when No |
| Regional Partnership Board "Area(s)" lets you pick only one | Tick boxes. The Hub explains each area is its own service with its own Statement of Purpose |
| Service Details says "the person who will be in day-to-day charge" (copied from the manager section) | Correct description |
| Trading name and company number are required although marked "if different" and "if applicable" | Optional |
| Dates use the American order (MM/DD/YYYY) | dd/mm/yyyy throughout |
| RI full name is not required while the date of birth is | Both required, and copied from the officers page |
| The RI is retyped although they must be one of the officers | Pick the officer; their details are copied |
| "If Yes, complete qualifications only" is an instruction, not logic | The manager's personal details appear only when the manager is a different person |
| Address history is one box with no dates check | Address rows with a gap check over 5 years |
| A Yes in registration history asks for nothing more | A short "tell us more" box appears |
| Weekly hours bands differ from CIW Online (for example 501 to 1000) | CIW Online's 8 bands |
| Client groups are not the Wales groups (no adults under 65, no criminal justice) | The 12 groups used in Wales |
| One upload box for every person's CV, and the signature is a file upload | One upload per person; sign on screen; the three declaration statements become ticks |
| "Organization" in US spelling | British English |

### E.2 Gaps against CIW Online, now asked (each marked "Added by the Hub" on the board)

- Who is filling it in, whether they are authorised, and whether the client has a CIW Online account.
- An office in Wales if the registered office is elsewhere (CIW asks for the principal office).
- Organisation history with any regulator, and whether a parent company owns 50% or more.
- Each officer's home address (CIW wants it, not the company address).
- Range of needs, using CIW Online's names; start date (at least 14 weeks ahead); office ownership.
- How you will work: personal care, help with medicines, help with money, Welsh speakers on the team (the Active Offer). Learning disability or autism experience appears only when those groups are ticked, because CIW checks it.
- RI: National Insurance number, qualifications, professional body, any investigation by a professional regulator, and why they are the right person (CIW asks how the RI is eligible).
- Registration history: other business interests in the UK or overseas.
- Referees: did they employ you for at least 3 months, and is either a relative or a director. Warnings appear before CIW would reject.
- GP: the Hub sends CIW's medical reference form early, because CIW needs all 3 pages signed and stamped and GPs can be slow.
- Manager: chosen yet (CIW allows applying without one, but will not register until a Social Care Wales registered manager is named), Social Care Wales status and number, Level 5.
- Documents: which ones the client already has, so the documents list is right first time. This includes the bank reference on CIW's own form and an insurance certificate (not a quote or schedule), which are common reasons for return.

### E.3 Pages and rules

1. Before You Start. 2. Organisation Information (filled from Companies House for a company or LLP). 3. Organisation History and Group. 4. Organisation Officers (another officer adds the next, up to three, then "more than three"). 5. Service Details. 6. How You Will Work. 7. RI Details (copied from the chosen officer). 8. DBS Information. 9. RI Qualifications and Experience. 10. Registration History. 11. RI References. 12. RI GP Details. 13. Registered Manager Details. 14. Required Documents. 15. Check your answers. 16. Declaration.

Smart rules:

- DBS done and on the Update Service: no ID documents.
- DBS done but not on the Update Service: a prompt to join, as there is a time limit after issue.
- DBS not done: three ID documents.
- DBS issue date: warning as it nears 3 months old, because CIW Online warns that older certificates may be rejected.
- RI is also the manager: only qualifications and Social Care Wales details are asked.
- CV checks: gaps of 4 weeks or more, and "present" as an end date, are flagged.

The address history stays on the RI page whatever the DBS answer, because it belongs to the RI's fitness checks and not only to the DBS. This is a difference from the CQC form.

Tested: 16 to 21 pages depending on the answers (sole trader, an RI who is not an officer, a manager who is a different person, and more).

### E.4 Second review, the same day

The form was printed page by page as a client sees it and checked again, then reviewed independently against the CIW skill. Changes:

- **Dates of birth:** Companies House shows only the month and year, so the form asks the client to add the day instead of claiming the full date came from Companies House.
- **Officers:** position is now a choice, and the form explains what a sole trader enters.
- **Choosing the RI:** the picker lists only officers who exist, plus "someone else, who is not an officer" (CIW Online allows this). Each person is told CIW will email them an invitation to complete their own part.
- **New page, Other Officers: Checks:** for every officer who is not the RI (place of birth, previous surnames, DBS, history), because CIW Online keeps a record for every officer.
- **Registered Manager, when a different person:** their own DBS, two references, GP medical reference, registration history, professional body, place of birth, previous surnames, NI number and interview language. These are three extra pages, skipped when the RI is the manager.
- **New page, Your CIW Choices:** decisions CIW Online asks the client to make, not Care Sync:
  - legal notices by email
  - sharing their email with Social Care Wales and Data Cymru (Dewis Cymru)
  - the areas and the RI becoming conditions of registration, with a warning that saying No delays the application
  - a note that each person ticks their own declarations at submission
- **Languages:** the language the service is provided in, the inspection language and each person's interview language, as CIW Online asks. The Welsh speakers question now suits a start-up with no team yet.
- **Prices and funding:** a rough hourly rate and who will pay, because CIW asks for a scale of charges.
- **More CIW Online questions:**
  - a branch office
  - the service telephone and email (the organisation's can be reused)
  - taking over a service
  - shared premises
  - the councils within the chosen areas
- **Checks that catch contradictions:** children ticked with an adult age range; 65+ with adults under 65; a children-only DBS for an adult service.
- **Referees:** a relative is a CIW rule; a company director is Care Sync advice. These are now separate questions. The "unless not possible" route for the 3-month employer rule is explained.
- **Wording:**
  - Internal notes such as "Added by the Hub" are no longer shown to clients; they are kept here for Care Sync.
  - "Checked" messages now say what will be checked, not that a check has happened.
  - The DBS age is counted to the day of submission.
  - The Update Service ID is optional.
  - Biometric residence permits now read "or eVisa".
  - No personal care is flagged for the consultant to check.
- **Declaration:** a fourth statement lets Care Sync act as the client's agent.

## Appendix F. RQIA Registration Information Form: every page, question and rule

Rebuilt on 4 November 2026 from the live Google Form ("RQIA Registration Information Form, Northern Ireland"). RQIA's own website is blocked in this session, so it was checked against Care Sync's RQIA guide and package in Drive, and public summaries of RQIA guidance. Board 56 shows it working. All 95 questions and options from the live form are in the board.

### F.1 Problems found in the live form

| Problem | Fix in the Hub |
| --- | --- |
| HSC Trust "Area(s)" lets you pick only one | Tick boxes |
| Service Details says "the person who will be in day-to-day charge" | Correct description |
| AccessNI questions are not required and have no logic | Certificate details when Yes; two ID documents and the RQIA PIN when No |
| "If applying new, note RQIA PIN: 497850" is a question box | A note, shown only when a new AccessNI check is needed |
| The documents ask for AccessNI ID for the manager, but there are no manager AccessNI questions | Manager AccessNI asked when the manager is a different person |
| Referee 2 has no "Relationship to you" | Added |
| Manager address history "if different from RI" is an instruction | Shown only when the manager is a different person |
| Dates in MM/DD/YYYY; signature as a file upload; one CV box for everyone | dd/mm/yyyy; sign on screen; one CV upload per person |

### F.2 Gaps, now asked (each marked "Added by the Hub")

- ICO registration and an RQIA Web Portal login (RQIA issues logins after checking identity, so this starts early).
- Start date. A short "tell us more" box after any Yes in registration history.
- Whether either referee is a relative (Care Sync's own guide lists weak or family references as a top reason for delay).
- Level 5 qualification status; NISCC registration (the manager must be NISCC registered).
- Which documents the client already has: Statement of Purpose, Service User Guide, policies, staffing and training plan, business plan, bank letter, insurance, office. These come from Care Sync's RQIA guide.

### F.3 Pages and rules

1. Organisation Information (filled from Companies House for a company or LLP). 2. Organisation Officers. 3. Service Details. 4. RI Details (copied from the chosen officer). 5. AccessNI Information. 6. Registration History. 7. RI References. 8. RI GP Details. 9. Registered Manager Details. 10. Required Documents. 11. Check your answers. 12. Declaration.

Smart rules:

- AccessNI done: no ID documents.
- RI is also the manager: only the registration number, Level 5 and qualifications are asked.
- Manager is a different person: their details, address history and AccessNI are asked, and the same "done already, no ID" rule applies to them.

Tested: 14 to 17 pages depending on the answers.

### F.4 Second review, the same day

- **Dates of birth:** the same Companies House fix as Appendix E.
- **RI picker:** lists only existing officers. There are notes for sole traders and partnerships, where the partners are the registered provider.
- **Agency type:** conventional or supported living, as RQIA registers them separately.
- **New pages:**
  - How You Will Work: personal care, medicines, money, starting staff numbers, hourly rate and who pays (for the Service User Guide and staffing plan)
  - RI Qualifications and Experience
- **AccessNI:**
  - An existing certificate is no longer treated as enough. RQIA may run its own check using its PIN, so ID documents are still collected, as optional, in case a new check is needed.
  - The RI's NI number is asked.
- **Registered Manager, when a different person:** their own AccessNI, two references (one from the current or most recent job), GP, registration history, place of birth, previous surnames and NI number. These are three extra pages, skipped when the RI is the manager. The manager is told they also apply to RQIA to be registered as manager.
- **Registration history:** prompts the client to include other regulators.
- **Wording:** the same fixes as Appendix E, including the eVisa wording, hidden internal notes and the agent consent in the declaration.
