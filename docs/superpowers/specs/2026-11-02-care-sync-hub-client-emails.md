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

Your first step is a short form tailored to your package. It takes about {{form_minutes}} minutes and saves as you go.

Button: Open my Hub

Speak soon,
{{consultant_name}}
Care Sync Experts

### 1.2 Meet your team
**Trigger:** handover approved
**Subject:** Your Care Sync team

Hi {{first_name}},

All your onboarding checks have passed, so your application work starts today.

Your team:
{{case_owner}} leads your application.
{{weekly_owner}} sends your update every {{update_day}}.
Millicent coaches you for your CQC interview when the time comes.

Your first update arrives on {{first_update_date}}. If you have a question before then, tap "Ask" in your Hub and it comes straight to us.

Button: See your journey

{{consultant_name}}

---

## 2. Onboarding

### 2.1 Your tailored form
**Trigger:** welcome plus 0 days
**Subject:** Your form has {{section_count}} sections, about {{form_minutes}} minutes

Hi {{first_name}},

Your form only asks what we need for {{package_name}}, and anything we already know is filled in for you.

If your registered manager or a director should answer their own part, you can invite them from the form, and they will only see their section.

Not sure of an answer? Tap "Not sure" and we will help.

Button: Start my form

{{consultant_name}}

### 2.2 Form reminder (day 2 and day 4, stops when submitted)
**Subject:** Your form is {{percent_complete}} per cent done

Hi {{first_name}},

You are {{percent_complete}} per cent of the way through your form. The next part is {{next_section}}, which takes about {{section_minutes}} minutes.

Everything you have entered is saved, on any device.

Button: Carry on

{{consultant_name}}

### 2.3 Form received
**Trigger:** form submitted
**Subject:** Thank you, we have your form

Hi {{first_name}},

Thank you for completing your form. We have already checked your company with Companies House and compared your details across your documents.

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

You can highlight any sentence to comment or ask a question, then approve it or ask for changes. Most people take about {{review_minutes}} minutes.

Button: Review now

{{consultant_name}}

### 3.3 Final pack ready to sign
**Subject:** Your application pack is ready for your signature

Hi {{first_name}},

Every document in your pack is approved and we have checked that names, addresses and services match everywhere.

Please review the final pack and sign to confirm it is ready to go to CQC. Once you sign, we send it within {{send_days}} working days and tell you the same day.

Button: Review and sign

{{consultant_name}}

---

## 4. With CQC

### 4.1 Submitted
**Subject:** Your application has gone to CQC

Hi {{first_name}},

We submitted your application to CQC today, {{submission_date}}.

What happens next: CQC confirms they have received it, then may ask for more information or invite your manager to an interview. CQC sets its own timetable, so we cannot give you a date, but we check every week and tell you the moment anything arrives.

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

Thank you for trusting us with this,
{{consultant_name}}

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

Thank you for working with us. If you have a moment, a short review helps other providers find the right support.

Button: See your year

{{consultant_name}}

---

## 7. Tenders

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

## Principles used (for review)

- **Audience:** B2B care provider owners and managers.
- **Reciprocity:** useful checklists and updates given before any offer.
- **Commitment and consistency:** small steps first (form sections, one quick question).
- **Social proof:** only real, permitted case studies and reviews, asked for at high points.
- **Peak-end rule:** every email ends on reassurance and a clear next step; registration and anniversary emails are designed as peaks.
- **Ethics and legal gates:** no fear, no fake urgency, no invented proof, prices only from the price book, opt-out on every growth email, consent rules for sole traders.
- **Claims still needing evidence before use:** any case study or review quoted must be confirmed and permitted by the client.
