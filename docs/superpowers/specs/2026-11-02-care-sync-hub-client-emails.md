# Care Sync Hub: Client Email Library

**Date:** 2 November 2026
**Status:** Draft for review
**Goes with:** `2026-11-02-care-sync-hub-design.md`, section 32

## How these emails are written

- British English. No dashes. No bold in the body. No exclamation marks.
- One job and one button per email. Under about 120 words.
- Calm, warm and specific. End on reassurance and the next step.
- Never "free", never a guarantee, never invented proof or urgency.
- Signed by the client's consultant. Replies go to the consultant and into the Hub.
- Delivery emails carry no sales offers. Offers appear only in aftercare and growth emails (marked "Growth"), only when relevant, and never to an unhappy client or during a refusal.
- Growth emails end with: "You are receiving this because you are a Care Sync client. You can choose which updates you get in your Hub, or reply 'stop'."
- Words in double braces are filled in by the Hub, for example {{first_name}}.

Audience for every email: B2B, the care provider owner or manager.

---

## 1. Welcome

### 1.1 Welcome to Care Sync
**Trigger:** agreement signed and deposit paid
**Subject:** Welcome to Care Sync, {{first_name}}

Hi {{first_name}},

Welcome to Care Sync. We are glad to be working with you on {{package_name}} for {{company_name}}.

Everything now lives in your Care Sync Hub: where you are, what we need from you, and what we are doing for you. You never need to email us to ask for an update.

Your first step is just 3 quick questions. After that, we fill in what we can ourselves and ask for the rest a little at a time, mostly as photos of documents you already have.

Button: Answer 3 quick questions

Speak soon,
{{consultant_name}}
Care Sync Experts

### 1.2 Lovely to speak to you
**Trigger:** the introduction call is saved as "Spoke to the client" (the caller can edit it before it goes)
**Subject:** Lovely to speak to you today

Hi {{first_name}},

Thank you for your time today. It was lovely to speak to you.

As we said on the call, here are your next three things:
{{next_three_things}}

None of them take long, and you can do them on your phone. If anything comes to mind later, tap "Ask" in your Hub and it comes straight to us.

Button: Open my Hub

{{caller_name}}
Care Sync Experts

### 1.3 Introduction call texts
**Sorry we missed you (sent straight after an unanswered call):** Hi {{first_name}}, it is {{caller_first_name}} from Care Sync. Sorry we missed you. We will try again at {{next_try}}, or pick a time that suits you: {{link}}

**Call back confirmed:** Hi {{first_name}}, it is {{caller_first_name}} from Care Sync. Thank you, we will call you on {{call_time}}. Need a different time? {{link}}

At most 3 calls and 2 texts are ever sent for an introduction call. Texts follow quiet hours.

### 1.4 Meet your team
**Trigger:** handover approved
**Subject:** Your Care Sync team

Hi {{first_name}},

All your onboarding checks have passed, so your application work starts today.

Your team:
{{case_owner}} leads your application.
{{weekly_owner}} sends your update every {{update_day}}.
Millicent, your coach, runs your 3 sessions, including interview practice.

Your first update arrives on {{first_update_date}}. If you have a question before then, tap "Ask" in your Hub and it comes straight to us.

Button: See your journey

{{consultant_name}}

---

## 2. Onboarding

### 2.1 Your onboarding form
**Trigger:** straight after the introduction call (or the next morning if the call could not happen), tailored to the package chosen when the client was added
**Subject:** Your onboarding form, made for {{package_name}}

Hi {{first_name}},

Thank you for your time today. As we said on the call, your onboarding form is ready. It has only the sections for {{package_name}}, and we have already filled in what we know, such as your company details from Companies House.

It has the same questions as the form you may have seen from us before, and we start your project as soon as it is complete. It saves as you go, so you can stop and come back any time, on any device.

Prefer to do it together? Reply and we will go through it with you on a call.

Button: Open my onboarding form

{{consultant_name}}

### 2.2 Gentle reminder (after 2 days, then 4, stops when done)
**Subject:** One quick thing: {{next_task}}

Hi {{first_name}},

Just one thing to keep your application moving: {{next_task}}.

Tap the button and it opens straight to it.

Button: Do it now

Or reply "call me" and we will sort it out together.

{{consultant_name}}

### 2.3 Form received
**Trigger:** form submitted
**Subject:** Thank you, we have your form

Hi {{first_name}},

Thank you, that is everything we need for now. We have already checked your company with Companies House and compared your details across your documents.

{{if no issues}}Everything matches. There is nothing more you need to do right now.
{{if issues}}We need {{issue_count}} small things from you. Each one is explained in your Hub and takes a minute or two.

Button: See what we checked

{{consultant_name}}

### 2.4 One quick question
**Trigger:** a mismatch found (for example a different flat number)
**Subject:** One quick question about your office address

Hi {{first_name}},

Your {{document_name}} says {{value_on_document}}. Your form says {{value_on_form}}. CQC needs these to match, so we want to check which is right.

It takes one tap in your Hub, and we will update every document for you.

Button: Answer the question

{{consultant_name}}

### 2.5 Your manager's invite (sent to the manager)
**Trigger:** the client names someone else as registered manager (question 2)
**Subject:** {{client_first_name}} has asked you to do your part

Hi {{manager_first_name}},

{{client_first_name}} has named you as registered manager for {{company_name}}, and Care Sync Experts is helping with the CQC registration.

Your part is a few short questions and a couple of photos. You can do it on your phone, a little at a time, and only you and Care Sync can see your answers.

Button: Start my part

{{consultant_name}}

### 2.6 Business email connected
**Trigger:** the client's business email is connected and its login stored in the vault
**Subject:** We are now watching for CQC emails for you

Hi {{first_name}},

Your business email, {{business_email}}, is now connected. We file only emails from CQC, CIW, RQIA and tender portals, and your other emails are never copied.

You can see every time we sign in, and why, on your privacy page. You can withdraw this at any time.

Button: See your privacy page

{{consultant_name}}

---

## 3. Delivery

### 3.1 Weekly update
**Trigger:** the client's update day (written by the weekly update owner from the nine-part draft)
**Subject:** Your weekly update: {{stage_name}}

Hi {{first_name}},

Where you are: {{stage_plain_english}}.
Done this week: {{done_this_week}}.
Policies: {{policies_status}}.
Application forms: {{forms_status}}.
Statement of Purpose: {{sop_status}}.
Interview portal: {{portal_status}}.
What we need from you: {{client_actions}} by {{client_action_date}}.
What we will do next: {{our_next_action}} by {{our_next_date}}.
Next update: {{next_update_date}}.

Button: Open my Hub

{{weekly_owner}}

### 3.2 Draft ready to review
**Subject:** Your {{document_name}} is ready to review

Hi {{first_name}},

Version {{version}} of your {{document_name}} is ready. It has been checked by a second consultant.

We have marked the few things to check first. You can tap any sentence to comment or ask a question, then approve it or ask for changes.

Button: Review now

{{consultant_name}}

### 3.3 Final pack ready to sign
**Subject:** Your application pack is ready for your signature

Hi {{first_name}},

Every document in your pack is approved and we have checked that names, addresses and services match everywhere.

Please review the final pack and sign to confirm it is ready to go to CQC. Once you sign, we send it within {{send_days}} working days and tell you the same day.

Button: Review and sign

{{consultant_name}}

### 3.4 Session booked
**Trigger:** the client books one of their 3 sessions (reminders follow the day before and an hour before)
**Subject:** Your session with {{coach_name}} is booked

Hi {{first_name}},

Your session {{session_number}} of 3 with {{coach_name}} is booked for {{session_date}} at {{session_time}}, by video.

The link is below and on your Today page. If anything comes up, you can change the time in your Hub.

Button: Add to my calendar

{{consultant_name}}

---

## 4. With CQC

### 4.1 Submitted
**Subject:** Your application has gone to CQC

Hi {{first_name}},

We submitted your application to CQC today, {{submission_date}}.

What happens next: CQC confirms they have received it, then may ask for more information or invite your manager to an interview. CQC sets its own timetable, so we cannot give you a date. We watch your business email for CQC and tell you the same day anything arrives, and you still get your update every Friday.

Nothing is needed from you right now.

Button: See your CQC tracker

{{consultant_name}}

### 4.2 CQC asked for more information
**Subject:** CQC has asked for some extra information

Hi {{first_name}},

CQC has asked for {{request_summary}}. This is a normal part of the process.

We are handling it. {{if client action}}We need {{client_action}} from you by {{client_action_date}} so we can reply well before CQC's deadline of {{cqc_deadline}}.

Button: See the request

{{consultant_name}}

### 4.3 Interview booked
**Subject:** Your CQC interview is booked for {{interview_date}}

Hi {{first_name}},

CQC has booked {{interviewee_name}}'s interview for {{interview_date}} at {{interview_time}}, by {{interview_method}}.

Your Interview Preparation Hub is ready. You can also book a session with Millicent; you have {{sessions_left}} included sessions left.

We will remind you 7 days, 1 day and the morning before.

Button: Go to Interview Preparation Hub

{{consultant_name}}

### 4.4 After the interview
**Subject:** Well done for getting through your interview

Hi {{first_name}},

Thank you for letting us know how the interview went. We have recorded the questions you were asked and any follow-up CQC mentioned.

Next, CQC makes its formal decision. We will tell you as soon as it arrives.

Button: See what happens next

{{consultant_name}}

---

## 5. Outcome

### 5.1 You are registered
**Subject:** You are registered with CQC

Hi {{first_name}},

{{company_name}} is now registered with CQC. This is a big moment, and it is yours.

Your Registration File is ready: every final document in one place, neatly organised for your first inspection.

Your next steps for the first 30 days are in your Hub, and {{consultant_name}} would like to book a short call to plan your launch and goals.

Button: Open my Registration File

If you would like to share your experience, it helps other care providers find the right support: Review us on Google, or Review us on Trustpilot. You can also tell us privately in your Hub.

Thank you for trusting us with this,
{{consultant_name}}

Note: every registered client receives this invitation, whatever their feedback score. No incentive is ever offered for a review.

### 5.2 Notice of Proposal (calm plan)
**Subject:** CQC has written to you, and we have a plan

Hi {{first_name}},

CQC has sent a Notice of Proposal. It is not a final decision, and you have time to respond.

You have until {{deadline}} to send written representations, which is 28 days from the date on the notice. We have already started drafting your response, and the plan with dates is in your Hub.

{{consultant_name}} will call you today to talk it through.

Button: See the plan

{{consultant_name}}

### 5.3 Application returned
**Subject:** CQC has returned your application, here is what happens now

Hi {{first_name}},

CQC has returned your application and explained what it needs. We have read their letter and set out a recovery plan, with what we will fix, anything we need from you, and a target date to resubmit.

You will get an update every week until it is back with CQC.

Button: See the recovery plan

{{consultant_name}}

### 5.4 Review reminder (once, 7 days later, then stop)
**Trigger:** 7 days after 5.1, only if neither review link has been opened
**Subject:** Would you share your experience?

Hi {{first_name}},

If you have a couple of minutes, a short review of your experience with Care Sync helps other providers decide who to trust with their registration.

Review us on Google, or Review us on Trustpilot. Whatever you write, thank you.

This is the only reminder we will send.

{{consultant_name}}

---

## 6. Aftercare and growth

### 6.1 Day 7: your launch checklist
**Subject:** Your first week as a registered provider

Hi {{first_name}},

A week in, here is a short checklist to make your first month smooth: display your registration correctly, set up your notifications process, and keep your policies to hand for staff.

It is all in your Hub, with a tick box for each item.

Button: Open my checklist

{{consultant_name}}

### 6.2 Day 30: check-in
**Subject:** How is your first month going?

Hi {{first_name}},

How is everything going? If anything has come up, from a CQC question to a staffing worry, reply to this email and it comes straight to me.

You also have {{support_months_left}} months of support included in your package.

Button: Book a check-in call

{{consultant_name}}

### 6.3 Growth: a tender in your area
**Trigger:** Tender Radar match, conflict check passed, client opted in to tender alerts
**Subject:** {{council}} {{service}} tender, closes {{closing_date}}

Hi {{first_name}},

{{council}} has published a {{service}} contract covering {{lots_and_areas}}. It closes on {{closing_date}}.

From what we know about {{company_name}}, it looks like a good fit: {{fit_reason}}. Your tender readiness is {{readiness_percent}} per cent.

If it is worth a look, we can go through the pack together on a 30-minute tender planning call. There is no charge for the call.

Button: Book a tender planning call

{{account_owner}}

### 6.4 Growth: first inspection readiness
**Trigger:** month 4 after registration
**Subject:** Getting ready for your first CQC inspection

Hi {{first_name}},

Many new providers are inspected in their first year, so now is a good time to check that your records, policies and day-to-day practice line up.

Your Hub has a short readiness checklist you can work through. If you would like us to help, we offer first inspection readiness support.

Button: Open the checklist

{{consultant_name}}

### 6.5 PIR received
**Trigger:** client logs a PIR or a PIR email is captured
**Subject:** Your PIR is due on {{pir_deadline}}

Hi {{first_name}},

CQC has asked for your Provider Information Return, due on {{pir_deadline}}.

If you would like us to help, our PIR service is £750 plus VAT: a briefing with your manager, every answer drafted within the word limits, a second consultant review, and support while you submit it.

Button: Get help with my PIR

{{consultant_name}}

### 6.6 Growth: supported living add-on
**Trigger:** home care client indicates interest in supporting people with a learning disability or autistic people
**Subject:** Adding supported living to your registration

Hi {{first_name}},

You mentioned you might support people in their own tenancies. Adding supported living to your registration is something we do often.

Our supported living add-on is £1,500 including VAT. It covers a route check, a new Statement of Purpose, the CQC notification, Interview Preparation Hub access and all CQC correspondence. Supported living policies are quoted separately.

Button: Talk to us about it

{{consultant_name}}

### 6.7 Policy review due
**Trigger:** 60 days before the policy anniversary
**Subject:** Your policies are due their yearly review

Hi {{first_name}},

Your policies were written on {{policy_date}}, so their yearly review is due by {{review_due_date}}. Since then, {{changes_summary}}.

You can review them yourself using the list in your Hub, or we can update them for you.

Button: See what has changed

{{consultant_name}}

### 6.8 Your year with Care Sync
**Trigger:** registration anniversary
**Subject:** Your first year with Care Sync

Hi {{first_name}},

One year ago today, {{company_name}} was registered with CQC.

Your year: {{milestones}}.

Thank you for working with us. Here is to your second year.

Button: See your year

{{consultant_name}}

---

## 7. Tenders

### 7.0 Tender submitted
**Trigger:** the bid is submitted on the buyer's portal
**Subject:** Your {{tender_name}} bid has been submitted

Hi {{first_name}},

We submitted your bid for {{tender_name}} today, ahead of the buyer's deadline. The portal receipt is attached and saved in your Hub.

The buyer expects to announce results around {{award_date}}. We will tell you as soon as we hear.

Button: See your tender

{{consultant_name}}

### 7.1 Tender won
**Subject:** You have won a place on {{tender_name}}

Hi {{first_name}},

{{company_name}} has won {{award_summary}}. Congratulations to you and your team.

Your Hub now has a mobilisation checklist built from the promises in your bid, so you can deliver exactly what you committed to.

When you are ready, we would love to share your success as a case study, only with your permission.

Button: Open my mobilisation checklist

{{bid_lead}}

### 7.2 Tender not successful
**Subject:** The result for {{tender_name}}

Hi {{first_name}},

I am sorry, {{tender_name}} was not successful this time. We know how much work went into it.

Your scores and the buyer's feedback are in your Hub. I would like to go through them with you so the next bid is stronger. {{if dynamic market}}This is a dynamic market, so you can apply to join again while it runs.

Button: Book a feedback review

{{bid_lead}}

### 7.3 Should we bid?
**Trigger:** a tender is matched to the client, or a new tender needs a lot-by-lot decision
**Subject:** A tender that could suit {{company_name}}

Hi {{first_name}},

{{tender_name}} has opened, and it looks like a fit for {{company_name}}. We have checked each lot against what the buyer asks for, so you can see straight away where you can bid and where you would need to wait.

The decision is yours. It takes a minute in your Hub, and we are happy to talk it through.

Button: See the lots

{{consultant_name}}

### 7.4 The buyer changed something
**Trigger:** a published clarification is marked "affects us"
**Subject:** An update from the buyer on {{tender_name}}

Hi {{first_name}},

The buyer has answered a question from bidders, and it affects your bid: {{clarification_summary}}.

What we have done: {{our_action}}. {{client_action_sentence}}

Button: See your tender

{{consultant_name}}

### 7.5 A framework you can join is open again
**Trigger:** a framework reopens or a dynamic market you were waiting for becomes available to you (for example after registration)
**Subject:** You can now join {{market_name}}

Hi {{first_name}},

{{market_name}} is open to new providers again{{after_registration_clause}}. Last time we agreed to come back to it when this happened.

Your tender profile is already {{profile_percent}}% ready, so only a few new questions would come to you.

Button: Decide in your Hub

{{consultant_name}}

---

## 8. Win-back

### 8.1 Six months without activity
**Subject:** A quick update for {{service_type}} providers

Hi {{first_name}},

It has been a while, so here is one thing that may be useful for {{company_name}}: {{relevant_update}}.

If there is anything we can help with, reply to this email. If now is not the right time, just let us know and we will not get in touch again unless you ask.

Button: Open my Hub

{{consultant_name}}

---

## 9. Account and care

### 9.1 Emergency access to your account
**Trigger:** a super admin approves break-glass access to the client's vault (section 46.2)
**Subject:** We used emergency access to your account today

Hi {{first_name}},

Today at {{time}}, {{staff_name}} used emergency access to your {{account_name}}, because {{reason}}. A Care Sync director approved it, and access ended automatically after {{hours}} hours.

You can see exactly what happened on your privacy page. If you have any questions, reply to this email.

Button: See your privacy page

{{director_name}}, Director

### 9.2 We have received your concern
**Trigger:** the client raises a concern in their Hub
**Subject:** We have received your concern

Hi {{first_name}},

Thank you for telling us. Your concern has gone to {{director_name}}, a director who is not involved in your day-to-day work.

{{director_first_name}} will be in touch by {{response_date}}. Your work carries on as normal in the meantime.

Button: See your concern

{{director_name}}, Director

### 9.3 Your new consultant
**Trigger:** a journey is reassigned to a new consultant
**Subject:** Your new Care Sync consultant

Hi {{first_name}},

From today, I am your consultant, taking over from {{previous_consultant}}. I have read everything so far, including your notes and how you like to be kept in touch, so you will not need to repeat anything.

Your work carries on exactly where it was, and your next update is on {{next_update_date}}. I would love to say hello properly, so I will give you a quick call this week.

Button: See where things stand

{{consultant_name}}

---

## Principles used (for review)

- **Audience:** B2B care provider owners and managers.
- **Reciprocity:** useful checklists and updates given before any offer.
- **Commitment and consistency:** small steps first (form sections, one quick question).
- **Social proof:** only real, permitted case studies and reviews, asked for at high points.
- **Peak-end rule:** every email ends on reassurance and a clear next step; registration and anniversary emails are designed as peaks.
- **Ethics and legal gates:** no fear, no fake urgency, no invented proof, prices only from the price book, opt-out on every growth email, consent rules for sole traders.
- **Claims still needing evidence before use:** any case study or review quoted must be confirmed and permitted by the client.
