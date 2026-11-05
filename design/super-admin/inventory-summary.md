# Care Sync Hub: inventory of configurable rules

Read only research, 4 November 2026. Sources: the design spec, the client email library, the demo world, and all 75 boards (text and JS data extracted). Full data: `inventory.json` in this folder (228 rules, 70 flagged as conflicts, 23 fixed by law or a regulator).

Source labels: "spec 6.2" is a spec section, "email 2.2" is an email in the library, "board Weekly.dc.html (9)" is a board file with its canvas number.

## Counts per area

| Area | Rules | With a conflict |
|---|---|---|
| Promises and timings | 15 | 3 |
| Journey and gates | 23 | 8 |
| Sessions and coaching | 11 | 2 |
| Regulators | 26 | 11 |
| Tenders | 21 | 6 |
| Money | 24 | 10 |
| People and access | 10 | 3 |
| Security | 16 | 1 |
| Data and privacy | 10 | 1 |
| Messages and notifications | 20 | 9 |
| Forms and templates | 15 | 5 |
| Branding and wording | 12 | 2 |
| Integrations | 6 | 1 |
| Aftercare and growth | 11 | 4 |
| Reviews and feedback | 8 | 4 |
| **Total** | **228** | **70** |

## Conflicts, most important first

### A. Legal, reputational or promise-breaking

1. **Reviews are gated for worried clients** (review-no-gating). Spec 37.1, 51.4 rule 5, 52.4 and the note under email 5.1 say every client is invited, whatever their feedback or mood. Board ManagerDash.dc.html (43) and board ClientCare.dc.html (70) say "no sales or review messages until it is resolved". Stopping review invitations for unhappy clients is the review gating that spec 37.1 says Google and Trustpilot forbid.
2. **"No time estimates" is broken everywhere** (no-time-estimates). Spec 51.4 rule 2 says the super admin cannot switch this off, and spec 38.4 agrees. But spec 35.1 ("how long it takes to read"), 57.2 ("with a time estimate") and 57.3 ("Every page shows a time estimate") contradict it. Emails that break it: 2.3 ("a minute or two"), 7.6 ("roughly how long"), 7.8 ("about 10 minutes") and 10.3 ("about 20 minutes"). Boards that break it: Journey (2) "Most people finish this stage in 5 days", Welcome (25) "about an hour" and "about 40 minutes", TenderClient (31), ClientDesktop (54) "about 15 minutes to read", TenderWork (57), TenderConfirm (58), TwoServices (59), and the "1 minute" page labels on TenderOnboard (38), ManagerFlow (47), CiwForm (55) and RqiaForm (56).
3. **When a bid is submitted** (tender-submit-margin). Spec 19.2 says 2 days before close and never on the last day. Spec 57.2 and email 7.7 say "two working days spare". The demo bid on every board submits Mon 30 Nov for a deadline of Tue 1 Dec 12:00, which is one working day. Board TenderWork.dc.html (57) even says "a spare day is kept". The same bid also breaks the spec 19.2 timeline (tender-timeline): spec 19.2 has drafts 10 days before close and price sign-off 5 days before, while the demo has drafts on Fri 20 Nov (7 working days) and approval on Wed 25 Nov (4 working days).
4. **How the 28 days are counted** (nop-representation-deadline, appeal-deadline). Board Cqc.dc.html (5) counts 28 days after service: served 2 Feb 2027, reply by 2 March. The demo world and boards 7, 43 and 75 count 28 days beginning with the day of service: served 21 Oct, deadline 17 Nov. Westbrook's appeal counts the other way: decision 26 Oct, window closes 23 Nov. The demo also treats "served (received)" as the same date. A legal counting rule must be one fixed rule.
5. **Our own Notice of Proposal targets** (nop-internal-targets). Spec 6.3 has draft by day 14, client review by day 21 and send by day 25. Board Cqc.dc.html (5) uses day 13, day 17 and day 21. The demo world and board ManagerDash.dc.html (43) send 7 days before the legal deadline (Tue 10 Nov against Tue 17 Nov).
6. **Who approves break-glass** (second-super-admin-approvals). Spec 46.2 says the second super admin, and spec 55.0 says a manager when the other super admin is away. Email 9.1 tells the client "A Care Sync director approved it". Spec 46.2 also leaves out form versions (spec 51.7, board 44) and super admin invites (board 78), which both need the second super admin.

### B. The same journey described two ways

7. **Onboarding form reminders, five different patterns** (onboarding-form-reminders):
   - email 2.2: after 2 days, then 4;
   - spec 32.2: day 2 and 4;
   - spec 54.2 and boards 47, 55, 56 and 38: one gentle reminder outside quiet hours;
   - board OnboardingQueue.dc.html (73): one reminder after 3 days, then a call after 6;
   - spec 38.5: suggest a call after 3 days;
   - spec 26.2: a 2 working day target for tenders.

   **Document reminders also disagree** (document-request-reminders). Spec 6.2 says after 3 days, then weekly. The live automation on board SuperAdmin.dc.html (24) is "Document waiting 5 days, gentle nudge". Spec 45.3 adds named schedules (gentle, standard, urgent) with no timings.
8. **Weekly update day** (weekly-update-day). Spec 18.1 and 18.5 send on the owner's set weekday (Tuesday or Wednesday), and email 1.4 uses a per-client {{update_day}}. Spec 6.2, 59.1, emails 4.1, 5.3b, 10.4 and 11.2, and every board say Friday.
9. **Weekly rhythm** (weekly-update-rhythm). Spec 17 and 18.5: Mon review, Tue and Wed send, Thu chase, Fri manager QA. Spec 59.1 and board Weekly.dc.html (9): Mon review, Wed chase, Thu QA by a second consultant, Fri send by 16:00.
10. **Can a client switch off the weekly update?** (weekly-update-opt-out). Spec 6.2 says clients can choose. Spec 42 says every client hears from us at least weekly, and board ClientMap.dc.html (32) lists it under "Always on".
11. **Kick-off session before handover** (no-work-before-handover). Spec 4 (stage 1, "session 1 of 3"), spec 51.3 and board Welcome.dc.html (25) ("Book your kick-off with Millicent") book the kick-off at welcome. Spec 54.0, the demo world and boards 33, 51, 73 and 74 lock all sessions until a manager approves the handover.
12. **The 8 onboarding gates are two different lists** (onboarding-gates-list). Spec 18.2: Form, Company, CVs, People, Professional registration, Identity (DBS or three IDs), References and GP, Address evidence. Demo world and boards 8 and 13: Company and directors, Identity, Office address evidence, Registered manager, Employment history, References, DBS, Professional registers.
13. **Who approves handover** (handover-approver). Spec 18.2 and board TeamCover.dc.html (78) say a manager. Boards 8, 73 and 74 and the demo world name Collins, the director and super admin 1. Related (super-admin-holders): spec 46 says managers hold the super admin accounts, yet super admin 1 is Collins everywhere.
14. **Who gets aftercare** (aftercare-length). Spec 3.3 gives 12 months of aftercare only to the full packages; "CQC Registration only" has no aftercare track. Emails 10.7 and 11.5 and boards RegCentre (63) and AftercareStaff (71) give it to every registered client. This date also drives ID deletion (item 15).
15. **ID and DBS retention** (id-dbs-retention). Spec 13 says the period is to be agreed. Spec 55.0 suggests until the 12 months of aftercare end. Board Security.dc.html (62) says the same, "unless the law says". Board Account.dc.html (29) says "after our work ends". Clients with no aftercare (tender only, single services) have no period at all.
16. **Resubmission gate** (resubmission-gate). Spec 58.2 says six items. Board ResubmitStaff.dc.html (66) has seven (it adds "copy of the pack and date sent kept as evidence"), and board ManagerDash.dc.html (43) shows "1 of 7". **Reference age** (resubmission-refresh-ages): boards 66 and 75 use "references under 6 months old", a rule the spec never sets (spec 58.2 only says "confirmed again").
17. **RQIA identity documents** (identity-documents). Spec Appendix F.1 says "two ID documents and the RQIA PIN". Spec 55.0 q48 and q55 and board RqiaForm.dc.html (56) say three. **BRP allowance** (brp-expiry-allowance): 18 months in spec 55.0 and board 55; board 56 says only "may still be accepted".
18. **How many growth offers at once** (growth-offer-rules). Spec 33.1 says one suggestion, and spec 51.4 rule 6 says no more than one new suggestion a month. Spec 51.3 and board Aftercare.dc.html (30) show three growth options in month 1. **Frequency caps** (marketing-frequency-caps): spec 32.1 sets one marketing email a week and spec 51.4 one new suggestion a month, with no rule for how they combine.
19. **Can the second-person quality check be relaxed?** (quality-gate-second-person). Spec 10.6 lets directors relax it per staff member. Spec 28 and 30 make it absolute for anything going to a client, regulator or buyer.
20. **Who decides bid or no bid** (bid-no-bid-approval). Spec 53.3 says the client decides, lot by lot. Spec 60.2, the demo world and boards 10, 11 and 43 add an approval by Collins with a reason. The demo world limits that approval to "another client on Lot 2", while boards 10 and 11 apply it to every bid.
21. **Texts and WhatsApp** (notification-channels). Spec 6.1 says later phase and urgent items only, and spec 55.0 puts WhatsApp in later phases. Spec 34.2, the introduction call texts (email 1.3) and boards Account (29), Notifications (41) and SuperAdmin (24) use them now for reminders and nudges. **Quiet hours exceptions** (quiet-hours): spec 51.4 lets a CQC or tender deadline through; board Account (29) says "except CQC deadlines" only. No source says whether quiet hours cover email, or covers CIW and RQIA deadlines.
22. **When the review invitation goes out** (review-invitation-moment). Spec 37.2 says at the registration moment. Board ClientCare.dc.html (70) says "Registered 2 weeks ago and happy. The review invitation goes out automatically tomorrow". **Platforms** (review-platforms): spec 55.0 says the Google link only at first, while spec 37.2, email 5.1 and board 20 show Google and Trustpilot as equal buttons.
23. **Worried and unhappy client handling** (worried-client-rules, unhappy-feedback-routing):
    - Who is told: spec 52.4 says the manager, the same day. Board IntroCall.dc.html (33) says Collins and Grace.
    - Director call: boards 43 and 70 add "a director call within 1 working day".
    - "Unsure" clients: spec 52.4 prompts the consultant; board 33 nudges Grace.
    - Unhappy stage feedback: spec 10.11 alerts the consultant. Board ClientStates.dc.html (53) hides the comment from the consultant unless the client wants it shown.
24. **Feedback moments and scale** (relationship-check-moments). Spec 10.11 asks at the end of every stage, with three faces. Spec 52.4 asks at three moments. Board Reports.dc.html (72) scores out of 5.

### C. Money

25. **Full start-up price** (price-full-start-up): still £8,500 or £8,000, yet client boards 29 and 60 show £8,500 + VAT and £2,833.33 instalments as if confirmed. **RQIA and CIW VAT** (price-ciw-rqia): spec 55.0 says "£4,500 (shown with VAT added)", while spec 24.2, spec 61, board 77 and the demo world say £4,500 + VAT. **Single services** (price-single-services): spec 24.2 says from £500 + VAT; board 77 says "To set".
26. **Instalments** (instalment-splits): spec 45.1 still says the instalment schedule is Pending, while spec 61 and the boards set it. CIW and RQIA splits are "default, to confirm". **Payment methods** (payment-methods): spec 52.1 and 55.0 allow bank transfer; spec 61 and the boards mention only Stripe methods.
27. **Who approves discounts and pending prices** (discount-approval, pending-prices). Spec 24.2 says Collins. Board PriceBook.dc.html (77) says any super admin, with the other approving. No discount limit is defined. **Who can change a price** (price-change-approval): board 24 shows Grace, who is not a super admin, requesting a price change, while spec 46.1 says only a super admin changes a price.
28. **VAT** (vat-treatment): no VAT rate is stored anywhere. **Accounting** (accounting-sync): spec 55.0 q27 still lists the accounting software as unknown, while the boards and demo world show Xero connected and synced hourly.
29. **Extra sessions** (extra-sessions): clients can buy them in the portal (spec 45.1), but no price exists in spec 24.2 or board 77. **Sessions per package** (sessions-included): only registration has a stated 3. Board 77 gives the £750 interview preparation add-on "3 sessions with Millicent", which the spec never says.

### D. Smaller wording and value mismatches

30. **Senior question reply** (senior-question-reply-time): spec 55.0 says "within 2 hours"; board Questions.dc.html (67) says "2 working hours".
31. **Watch cadence** (regulator-watch-cadence): spec 59.2 says CIW Online is checked "every working day"; email 10.4 and board 63 say "every day".
32. **CV gaps** (cv-gap-rules): the spec says every gap is explained; the CIW form flags gaps of 4 weeks or more; board FormBuilder.dc.html (44) asks about gaps of "more than 3 months". **Address history** (address-history-length): 5 years everywhere, but open question 47 says CIW may need 10 years for some people.
33. **Expiry warning** (tender-document-expiry-warning): a month in spec 57.2 and board 57; 6 weeks for insurance on board 67; no value in spec 10.2. **Tender profile freshness** (tender-profile-freshness): spec 57.2 says "older than a few months" with no value; board 58 implies somewhere between 2 and 5 months.
34. **Inspection readiness** (inspection-readiness-timing): month 4 in email 6.4, month 4 to 6 in spec 24.2 and 33.1, and month 3 on board 71.
35. **Form builder ownership** (form-version-approval): spec 26.3 and 31.2 give it to directors. Boards 44 and 78 let the onboarding lead draft and the second super admin approve.
36. **Two stage models** (stage-model): the 11 stages of spec 4 against the 13 staff stages of spec 18.3. **Escalation role** (critical-risk-alerts): spec 23 says the manager; spec 6.3 and 14.2 say a director.
37. **Stage colours** (stage-waiting-colours): spec 11.2 uses per-stage targets with no values. Board ClientsList.dc.html (68) uses one rule: amber after 5 days, red after 10.
38. **Signature reminders** (signature-reminders): spec 6.2 says one after 2 days; spec 36.2 says until signed; board 64 shows a manual button.
39. **The word "free"** (banned-words): spec 32.1 and 51.4 ban "free", but staff boards 43, 66, 69, 72 and 76 and the demo world say "free resubmission". Board RegReply (76) even says "we resubmit for free" in an explainer.
40. **Client sign-in** (client-sign-in): spec 12 offers an optional password or passkey; board 40 says no password. Board 40 has a 30-day device session that the spec does not set. **Saving** (save-and-resume): spec 54.2 says answers save on the server, not in the browser; board 53 (offline) keeps answers on the phone.
41. **Tender questionnaire size** (tender-form-sections): 21 sections in spec 53.4; 15 sections in spec 54.1 and board 48. **Portal passwords** (tender-portal-access): spec 53.4 says they are never asked; Appendix D keeps questions 1.4 and 1.5 on the form, routed to the vault.
42. **Connections** (connections-and-health): board 24's 12 connections leave out Ordnance Survey, CQC data, HM Land Registry and BidSuite from spec 46.1, and add the three watches and file storage instead.
43. **Roles grid** (roles-and-permissions): spec 13 says directors see every client; board 78 says managers do. The finance role in spec 46.1 has no row on board 78.
44. **Referees** (referee-rules): the demo world expects a second CQC referee "later", but spec 55.0 q43 keeps one referee for CQC.
45. **Sending addresses** (sending-addresses): spec 6.1 says notifications come from a "recognisable Care Sync address"; spec 7.1 says the staff member's own mailbox. No transactional sending domain is set.
46. **Undefined values behind live promises:**
    - working hours and bank holidays per nation (working-hours);
    - the {{send_days}} value in email 3.3 (board 19 says 2 working days) (submit-after-final-signature);
    - how far ahead our request-for-information targets sit (rfi-reply-targets).

## Rules stated in the spec that no board shows

These have no screen, value or control on any board, so the super admin design must add them:

- **Working hours:**
  - the definition of working hours and days (spec 52.7);
  - the enquiry reply within 15 minutes in staffed hours (32.2).
- **Red and alert thresholds:**
  - red at 1 working day for an unanswered client message, and at 7 days for no outbound contact (42);
  - Notice of Proposal alerts at day 7, 14, 21 and 25, then daily for the final 3 days (6.3);
  - overdue deadline task escalates to a director (6.3, 14.2);
  - the 8am morning brief (45.5);
  - stage target times for amber and red (11.2);
  - tender deadlines under 15 working days flagged to Collins (19.2); board 10 shows 13 working days with no flag.
- **Promises:**
  - growth plan call within 5 working days (24.1);
  - tender match call within 2 working days (24.3);
  - reply to every public review within 2 working days (37.2);
  - complaint full reply within 20 working days (55.0);
  - new consultant tells the client the same day (52.6);
  - recovery plan within 2 working days of a returned application (18.3).
- **Reminders:**
  - draft review reminder after 3 days (6.2);
  - signature reminder after 2 days (6.2);
  - win-back after 6 months (32.2);
  - marketing caps of one email a week and one new suggestion a month (32.1, 51.4);
  - Monday tender email only when needed (email 7.6).
- **Data and security:**
  - staff session time-outs (46.1), with no value set;
  - breach 72-hour clock and subject access deadlines (49.6);
  - voice notes deleted after transcription (13);
  - retention periods per document type other than ID and DBS (46.1);
  - sensitive fields masked by default (26.3);
  - download link expiry (13).
- **Money:**
  - refunds and credit notes need manager approval (49.1);
  - pending prices answered with "I'll confirm that for you today" (24.2);
  - the lawful wage figure of £12.71 from 1 April 2026 (19.3), which needs an annual update.
- **Tenders:**
  - the earlier closing time wins when two documents disagree (19.2);
  - the Living Plus Care Services conflict check (19.1);
  - a lot failing two of the four checks is "usually a no" (19.3).
- **Wording and branding controls (no board shows them):**
  - British English, no dashes, no bold, no exclamation marks, about 120 words;
  - banned words, the brand voice guard, email signatures, the growth footer and the proof bank (32.1, 49.5, 49.9);
  - sending domains (46.1).
- **Templates:**
  - the email library and its versions (46.1, 57.4). The staff menu has a "Templates" item but there is no Templates board;
  - automation rules exist only as a short list on board 24.
- **Other:**
  - call backs do not use included sessions (5.9);
  - partner logins (49.3);
  - consent wordings for third-party contact and call recording (55.0);
  - the aftercare email schedule (day 7, day 30, month 4, 60 days before the policy anniversary, the anniversary) as a setting; board 71 shows duties but not this schedule.

## Rules shown on boards that the spec never defines

- **Promises and timings:**
  - "We submit within 2 working days" after signing (Sign, 19);
  - Friday updates sent by 16:00 (Weekly, 9);
  - a kind check-in a week after a refusal (ClientCare 70, ResubmitStaff 66);
  - a resubmission target of about 5 weeks (Resubmit, 65);
  - director call within 1 working day for worried clients (43, 70);
  - RFI internal targets: 2 days after receipt on board 5, 6 working days before CQC's date on board 7.
- **Thresholds:**
  - "waiting on" amber after 5 days and red after 10 (ClientsList, 68);
  - document nudge after 5 days (SuperAdmin, 24);
  - one onboarding reminder after 3 days, then a call after 6 (OnboardingQueue, 73);
  - landlord reminder after about 3 working days (Onboarding 8, AddressClient 15);
  - unusual activity when exports go above "under 5 a day" (24);
  - references must be under 6 months old (66, 75).
- **Access and security:**
  - cover staff cannot reveal vault logins, and cover is for urgent work only (78, 24);
  - staff invites expire after 7 days (78);
  - leaver sign-in stops at 17:30 on the last day, and their email is forwarded for 90 days (78);
  - the client's phone stays signed in for 30 days (SignIn, 40);
  - uploads up to 20 MB, PDF, JPG or PNG only (53).
- **Data:**
  - scheduled deletion runs 7 days after approval;
  - deletion is blocked by a legal hold, an open complaint, a regulator query or a payment dispute (24);
  - the super admin summary is sent Monday at 07:00 (24);
  - Xero syncs every hour (24, 43).
- **Money:**
  - overdue invoices aged 0 to 30, 31 to 60 and over 60 days, with "payment plan or pause work" after 60 days (43);
  - instalment reminder a week before is also in spec 52.6;
  - PIR priced "one PIR per service type" (24, 77);
  - "Sales never offers a discount. Trade scope first" (77);
  - "Never promise a lower rate" for the retained package (77);
  - the interview preparation add-on includes 3 sessions (77).
- **Sessions:**
  - sessions last one hour (Sessions, 28);
  - the case owner joins session 2 (7, demo world).
- **Aftercare and growth:**
  - readiness check at month 3 (71);
  - consultant handover summary at month 12 (71, 75);
  - retained support "offered once" (71);
  - the Radar asks the case owner again at month 3 after a no (10);
  - worried clients get no onboarding nudges (73);
  - worried clients get no review messages (43, 70). This one breaks the spec, see conflict 1.
- **Tenders:**
  - contracts re-tendered about 6 months before they end (57, email 7.10);
  - modern slavery statement only above £36 million turnover (38);
  - policies reviewed in the last 12 months (57, 38);
  - a one working day submission margin (57, 11). This one breaks the spec, see conflict 3.
- **Feedback:**
  - consultant scores out of 5 (Reports, 72);
  - a director handles unhappy feedback and the consultant does not see the comment (53).

## Notes for the super admin design

- Many conflicts come from one value typed in several places. Each item above should become one setting, with emails and boards reading it. The cases that matter most:
  - reply times;
  - reminder schedules;
  - tender margin;
  - Notice of Proposal targets and day counting;
  - weekly update day;
  - quiet hours;
  - aftercare length;
  - retention.
- Values fixed by law or a regulator (23 rules flagged `is_legal_fixed`) should be shown read-only with their source. Examples: 28 days, the 25% PSC threshold, the 12-digit DBS number, CIW regulations 73 and 80, RQIA monthly monitoring, the 72-hour breach clock, TPS screening within 28 days, the minimum wage and £5 million employer's liability.
- The super admin also needs a basic calendar setting: working hours, working days and bank holidays for England, Wales and Northern Ireland. Every "working day" promise depends on it.
