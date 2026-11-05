# Data for Messages and automations (board 82): email library previews and the automation rules.
import re
from emailspec import parse

# Demo clients used for "Preview as a real client"
CL = {
 'sunrise': dict(label='Sunrise Homecare Ltd (Priya Shah)', first_name='Priya', company_name='Sunrise Homecare Ltd', consultant_name='Daniel Mensah', to='priya@sunrisehomecare.co.uk'),
 'harbour': dict(label='Harbour Lane Care Ltd (Amara Okafor)', first_name='Amara', company_name='Harbour Lane Care Ltd', consultant_name='Grace Whitfield', to='amara@harbourlanecare.co.uk'),
 'meadow': dict(label='Meadow View Care Ltd (Ade Ola)', first_name='Ade', company_name='Meadow View Care Ltd', consultant_name='Divine', to='ade@meadowviewcare.co.uk'),
 'bright': dict(label='Bright Path Care Ltd (Joy Adeyemi)', first_name='Joy', company_name='Bright Path Care Ltd', consultant_name='Daniel Mensah', to='joy@brightpathcare.co.uk'),
 'riverside': dict(label='Riverside Homecare Ltd (Mark Evans)', first_name='Mark', company_name='Riverside Homecare Ltd', consultant_name='Olu', to='mark@riversidehomecare.co.uk'),
 'elm': dict(label='Elm Tree Care Ltd (Femi Adebayo)', first_name='Femi', company_name='Elm Tree Care Ltd', consultant_name='Daniel Mensah', to='femi@elmtreecare.co.uk'),
 'westbrook': dict(label='Westbrook Care Ltd (Sade Johnson)', first_name='Sade', company_name='Westbrook Care Ltd', consultant_name='Daniel Mensah', to='sade@westbrookcare.co.uk'),
 'willow': dict(label='Willow Bank Supported Living Ltd (David Clarke)', first_name='David', company_name='Willow Bank Supported Living Ltd', consultant_name='Olu', to='david@willowbanksl.co.uk'),
 'brookside': dict(label='Brookside Homecare Ltd (Aisha)', first_name='Aisha', company_name='Brookside Homecare Ltd', consultant_name='Olu', to='aisha@brooksidehomecare.co.uk'),
 'maple': dict(label='Maple Court Care Ltd (Peter)', first_name='Peter', company_name='Maple Court Care Ltd', consultant_name='Daniel Mensah', to='peter@maplecourtcare.co.uk'),
 'ashby': dict(label='Ashby Care Ltd (Helen)', first_name='Helen', company_name='Ashby Care Ltd', consultant_name='Daniel Mensah', to='helen@ashbycare.co.uk'),
 'oakleaf': dict(label='Oakleaf Living Ltd (Kemi Adebola)', first_name='Kemi', company_name='Oakleaf Living Ltd', consultant_name='Daniel Mensah', to='kemi@oakleafliving.co.uk'),
 'fernhill': dict(label='Fernhill Homecare Ltd (Lucy)', first_name='Lucy', company_name='Fernhill Homecare Ltd', consultant_name='Daniel Mensah', to='lucy@fernhillhomecare.co.uk'),
 'kingsway': dict(label='Kingsway Care Ltd (Hassan)', first_name='Hassan', company_name='Kingsway Care Ltd', consultant_name='Olu', to='hassan@kingswaycare.co.uk'),
 'afon': dict(label='Afon Care Ltd (Rhian)', first_name='Rhian', company_name='Afon Care Ltd', consultant_name='Daniel Mensah', to='rhian@afoncare.co.uk'),
 'lagan': dict(label='Lagan View Care Ltd (Niamh)', first_name='Niamh', company_name='Lagan View Care Ltd', consultant_name='Olu', to='niamh@laganviewcare.co.uk'),
}

P = 'Preview only. Nothing is sent from here.'
# num: (client, overrides, conditions, note)
PV = {
 '1.1': ('meadow', dict(package_name='the Full start-up package'), [], 'Sent to Ade today at 10:02, when Meadow View paid.'),
 '1.2': ('meadow', dict(caller_name='Divine', next_three_things='1. Answer 3 quick questions in your Hub.\n2. Look out for your onboarding form.\n3. Save our number for your updates.'), [], 'Not sent yet: Divine\'s introduction call with Ade is due by 12:02.'),
 '1.3': ('meadow', dict(caller_first_name='Divine', next_try='2pm today', link='caresynchub.co.uk/call', call_time='Tuesday at 10am'), [], 'Texts only for the introduction call and urgent legal deadlines.'),
 '1.4': ('harbour', dict(case_owner='Daniel Mensah', weekly_owner='Daniel Mensah', update_day='%%update_day%%', first_update_date='%%next_update%%', consultant_name='Daniel Mensah'), [], 'Not sent yet: goes when a manager approves the handover (3 gates still open).'),
 '2.1': ('harbour', dict(package_name='the Full start-up package'), [], 'Sent to Amara on Mon 19 Oct at 11:16, straight after the introduction call.'),
 '2.2': ('harbour', dict(next_task='finish your onboarding form'), [], 'Sent to Amara on Wed 21 Oct and Fri 23 Oct. Grace called on Mon 26 Oct.'),
 '2.3': ('harbour', dict(issue_count='3'), ['issues'], 'Sent to Amara on Fri 30 Oct at 08:00 (the form came in Thu 29 Oct 21:46, inside quiet hours). Complaint C-001 is about this email: see View as (board 88).'),
 '2.4': ('willow', dict(document_name='tenancy agreement', value_on_document='Unit 4, 22 Mill Lane', value_on_form='Unit 3, 22 Mill Lane'), [], P),
 '2.5': ('harbour', dict(client_first_name='Amara', manager_first_name='Ruth'), [], 'Sent to Ruth Bennett on Tue 20 Oct.'),
 '2.6': ('harbour', dict(business_email='amara@harbourlanecare.co.uk', consultant_name='Daniel Mensah'), [], 'Sent to Amara on Wed 28 Oct at 16:03.'),
 '3.1': ('bright', dict(weekly_owner='Daniel Mensah', stage_name='Stage 4 of 11: drafting', stage_plain_english='we are writing your application pack', done_this_week='your Statement of Purpose version 2 passed the second consultant check, and session 2 with Millicent is booked', policies_status='written and checked, ready for your review', forms_status='the provider form check is due on Wed 11 November', sop_status='version 2 is ready for your comments', portal_status='opens once we submit', client_actions='your comments on the Statement of Purpose', client_action_date='Thu 5 November', our_next_action='finish the provider form check', our_next_date='Wed 11 November', next_update_date='%%next_update2%%'), [], 'Next one due %%next_update%% by %%update_time%%. Daniel writes it from the nine-part draft.'),
 '3.2': ('bright', dict(document_name='Statement of Purpose', version='2'), [], 'Sent to Joy on Fri 30 Oct.'),
 '3.3': ('bright', dict(send_days='%%send_days%%'), [], P),
 '3.4': ('bright', dict(coach_name='Millicent', session_number='2', session_date='Monday 2 November', session_time='10:00'), [], 'Sent when Joy booked session 2. Reminders went the day before and go an hour before.'),
 '4.1': ('riverside', dict(submission_date='Friday 23 October'), [], 'Sent to Mark on Fri 23 Oct.'),
 '4.2': ('elm', dict(request_summary='more detail on how you will cover weekend visits', client_action='a sample weekend rota from Claire', client_action_date='Wed 4 November', cqc_deadline='Thu 12 November'), ['client action'], 'Our reply target is Fri 6 Nov, %%rfi%% working days before CQC\'s date.'),
 '4.3': ('elm', dict(interviewee_name='Claire Hughes', interview_date='Tuesday 24 November', interview_time='10:30', interview_method='video call', sessions_left='1'), [], 'Sent to Femi when CQC booked the interview.'),
 '4.4': ('elm', {}, [], P),
 '5.1': ('brookside', dict(aftercare_line='%%aftercare_yes%%'), [], 'Sent to Aisha on Mon 19 Oct, the day Brookside was registered. Review invitation: Google and Trustpilot, the client chooses.'),
 '5.2': ('sunrise', dict(deadline='%%deadline%%'), [], 'Sent to Priya on Wed 21 Oct (version 2).'),
 '5.3': ('riverside', {}, [], P),
 '5.3a': ('westbrook', dict(target_date='Monday 30 November'), [], 'Sent to Sade on Mon 26 Oct. The appeal window closes Sun 22 Nov, worked out the safe way.'),
 '5.3b': ('westbrook', dict(date='Monday 30 November'), [], 'Not sent yet: Westbrook\'s resubmit target is Mon 30 Nov.'),
 '5.4': ('brookside', {}, [], 'Sent to Aisha on Mon 26 Oct. Aisha chose Google on Tue 27 Oct. No more reminders.'),
 '6.1': ('brookside', {}, [], 'Sent to Aisha on Mon 26 Oct.'),
 '6.2': ('brookside', dict(support_months_left='%%months_left%%'), [], 'Due Wed 18 Nov.'),
 '6.3': ('maple', dict(account_owner='Jo Martin', council='Northshire County Council', service='home care framework', lots_and_areas='Lot 1 North and Lot 2 South', closing_date='Tue 1 December', fit_reason='you are registered for domiciliary care and you already work in the Lot 2 South area', readiness_percent='68'), [], 'Held: Oakleaf Living already bids on Lot 1 North, so "Accept the bid work" waits on the Manager dashboard (board 43).'),
 '6.4': ('maple', {}, [], P),
 '6.5': ('ashby', dict(pir_deadline='Fri 4 December'), [], 'Prices come from the price book. A discount for Ashby (2 service types) waits for a super admin: decision 3 on Home.'),
 '6.6': ('maple', {}, [], P),
 '6.7': ('ashby', dict(policy_date='7 January 2026', review_due_date='7 January 2027', changes_summary='two pieces of guidance your policies refer to have been updated'), [], 'Due Mon 9 Nov, 60 days before the anniversary.'),
 '6.8': ('ashby', dict(milestones='registered with CQC, your first inspection readiness check, and your policies kept up to date'), [], 'Due on the registration anniversary.'),
 '7.0': ('oakleaf', dict(tender_name='Northshire County Council home care framework 2027, Lot 1 North', award_date='late January 2027, from the tender pack'), [], 'Not sent yet: Care Sync submits %%t_submit%%.'),
 '7.1': ('oakleaf', dict(tender_name='the Northshire home care framework', award_summary='a place on Lot 1 North', bid_lead='Daniel Mensah'), [], P),
 '7.2': ('oakleaf', dict(tender_name='Eastford Borough Council supported living', bid_lead='Daniel Mensah'), ['dynamic market'], P),
 '7.3': ('oakleaf', dict(tender_name='Eastford Borough Council supported living'), [], 'Sent to Kemi when Eastford matched.'),
 '7.4': ('oakleaf', dict(tender_name='the Northshire home care framework', clarification_summary='the buyer now asks for 2 case studies instead of 1', our_action='we have added a second case study to your task list', client_action_sentence='We need a short story from you by Wed 11 November, as planned.'), [], P),
 '7.5': ('willow', dict(market_name='Eastford Borough Council supported living', after_registration_clause=', now that you are registered with CQC', profile_percent='70'), [], 'Preview only: as it would read once Willow Bank is registered.'),
 '7.6': ('oakleaf', dict(count='2', this_week_list='1. Case study for Northshire Lot 1 North, by Wed 11 November.\n2. Staff numbers and turnover, by Mon 16 November.', first_due_date='Wed 11 November', bid_lead_name='Daniel Mensah'), [], 'Goes on Mon 9 Nov, because both are due the week after.'),
 '7.7': ('oakleaf', dict(tender_name='the Northshire home care framework', approval_date='%%t_approve%%', our_submit_date='%%t_submit%%', buyer_deadline='Tuesday 1 December at 12:00', bid_lead_name='Daniel Mensah'), [], 'Dates worked out from the buyer\'s deadline: draft %%t_draft%%, approval %%t_approve%%, submit %%t_submit%%.'),
 '7.8': ('oakleaf', dict(tender_name='Eastford Borough Council supported living', new_question_count='6', bid_lead_name='Daniel Mensah'), [], 'Sent to Kemi when work on Eastford started.'),
 '7.9': ('oakleaf', dict(document_name='employer\'s liability insurance certificate', expiry_date='Fri 11 December', needed_by='Tue 24 November', tender_name='Northshire', bid_lead_name='Daniel Mensah'), ['bid'], 'Sent to Kemi on Fri 30 Oct, %%expiry_weeks%% weeks before it runs out.'),
 '7.10': ('oakleaf', dict(contract_name='Northshire home care', months='6', end_date='Fri 30 April 2027', bid_lead_name='Daniel Mensah'), [], P),
 '8.1': ('fernhill', dict(service_type='domiciliary care', relevant_update='our checklist for your yearly policy review is ready in your Hub'), [], P),
 '9.1': ('riverside', dict(time='14:20', staff_name='Daniel Mensah', account_name='CQC business email', reason='CQC sent an urgent request and the login was needed to read it', hours='%%bg_hours%%', approver_name='Rachel Turner', approver_role='Operations manager'), [], 'Sample values: no emergency access in the last 30 days, so this has not been sent to anyone.'),
 '9.2': ('harbour', dict(director_name='Collins', director_first_name='Collins', response_date='Monday 2 November'), [], 'Sent to Amara on Sat 31 Oct at 10:03, one minute after she raised her concern.'),
 '9.3': ('kingsway', dict(previous_consultant='Sam Patel', next_update_date='%%next_update2%%'), [], 'Sent by the reassignment, never typed by hand. Waiting: goes to Kingsway and Cedar Lodge on Mon 9 Nov if decision 5 on Home is approved (Sam Patel\'s clients, Team and cover, board 78, and People and access, board 83). Sam\'s other 4 clients get it when their new owner is approved.'),
 '9.4': ('kingsway', dict(what_happened='on Sunday 1 November, between 21:40 and 22:05, a colleague who is leaving Care Sync downloaded copies of documents from the Hub files of 6 clients, including yours, onto a Care Sync laptop at home, outside our usual way of working',
        data_involved='documents in your company\'s Hub file, such as CVs, references and identity documents. Your Hub lists exactly which ones',
        likely_effect='the laptop is encrypted and managed by Care Sync, and so far nothing shows the files were shared. If they had been, someone could try to use the identity details',
        actions_taken='we stopped the downloads and the colleague\'s access on the morning of Monday 2 November, and we are checking the laptop and our systems',
        what_to_do='look out for post, calls or emails that use your details unexpectedly, and tell us straight away if anything looks wrong',
        contact_name='Collins', contact_phone='0333 577 0877'), [],
        'Never sent automatically. Collins signs it as data protection lead and Rachel Turner, the other super admin, approves it. Draft with sample values from incident 2026-01 (Security, board 84): not sent, because the decision on telling the people affected is still open.'),
 '10.1': ('afon', {}, [], 'Sent to Rhian before CIW Online invitations went out.'),
 '10.2': ('afon', {}, [], 'Sent to Rhian. CIW is still waiting for Sarah Jones\'s reference.'),
 '10.3': ('afon', dict(call_date='Wednesday 14 October', call_time='10:00'), [], 'Sent to Rhian before submission on Wed 14 Oct.'),
 '10.4': ('afon', dict(submission_date='Wednesday 14 October'), [], 'Sent to Rhian on Wed 14 Oct.'),
 '10.5': ('afon', dict(request_summary='more detail on your out of hours cover', client_action='your on-call rota', client_action_date='Thu 5 November', ciw_deadline='Fri 13 November'), ['client action'], P),
 '10.6': ('afon', dict(interviewee_name='Rhian', interview_date='Thursday 26 November', interview_time='10:00', interview_method='video call', interview_language='English'), [], 'Sent to Rhian when CIW booked the interview.'),
 '10.7': ('afon', dict(aftercare_line='%%aftercare_no%%'), [], 'Preview only. Afon has registration only, so the aftercare line offers aftercare instead.'),
 '10.8': ('afon', dict(deadline='Monday 14 December'), [], 'Preview only, with sample dates.'),
 '10.9': ('afon', dict(target_date='Monday 1 February'), [], 'Preview only, with sample dates.'),
 '11.1': ('lagan', {}, [], 'Sent before the Hub went live on Thu 1 Oct.'),
 '11.2': ('lagan', dict(submission_date='Wednesday 30 September'), [], 'Sent before the Hub went live on Thu 1 Oct.'),
 '11.3': ('lagan', dict(request_summary='your manager\'s AccessNI certificate number', client_action='the certificate number', client_action_date='Thu 5 November', rqia_deadline='Fri 13 November'), ['client action'], P),
 '11.4': ('lagan', dict(interviewee_names='Niamh and your manager', interview_date='Tuesday 8 December', interview_times='10:00 and 11:30'), [], 'Sent to Niamh when RQIA booked the interviews.'),
 '11.5': ('lagan', dict(aftercare_line='%%aftercare_no%%'), [], 'Preview only. Lagan View has registration only.'),
 '11.6': ('lagan', dict(deadline='Monday 14 December'), [], 'Preview only, with sample dates.'),
 '11.7': ('lagan', dict(target_date='Monday 1 February'), [], 'Preview only, with sample dates.'),
 '11.8': ('lagan', dict(date='Monday 1 February'), [], 'Uses 5.3b, with RQIA in place of CQC. Preview only.'),
}

# trigger, timing (tokens filled from Rules and promises)
TT = {
 '1.1': ('Agreement signed and first instalment paid through Stripe', 'Straight away'),
 '1.2': ('Introduction call saved as "Spoke to the client"; the caller edits it first', 'When the caller sends it'),
 '1.3': ('Introduction call not answered, or a call back booked', 'Straight after the call. At most 3 calls and 2 texts'),
 '1.4': ('A manager approves the handover', 'Same day'),
 '2.1': ('Introduction call done, or the next morning if it could not happen', 'Straight after the call'),
 '2.2': ('Onboarding form not finished', '%%form_rem%%'),
 '2.3': ('Onboarding form submitted', 'Straight away, held in quiet hours'),
 '2.4': ('A document and the form disagree', 'When a person confirms it'),
 '2.5': ('The client names someone else as registered manager', 'Straight away'),
 '2.6': ('Business email login saved in the vault', 'Straight away'),
 '3.1': ('The weekly update day', 'Every %%update_day%% by %%update_time%%'),
 '3.2': ('A draft passes the second consultant check', 'Same day. Reminder %%draft_rem%%'),
 '3.3': ('Every document approved and consistent', 'Same day. Reminder %%sig_rem%%'),
 '3.4': ('The client books one of their %%sessions%% sessions', 'Then the day before and an hour before'),
 '4.1': ('Application submitted to CQC', 'Same day, within %%send_after%% of signing'),
 '4.2': ('CQC asks for more information', 'Same day. We reply %%rfi%% working days early'),
 '4.3': ('CQC books an interview', 'Reminders 7 days, 1 day, the morning'),
 '4.4': ('The client tells us how the interview went', 'Same day'),
 '5.1': ('Registration confirmed', 'Same day. Review invitation once'),
 '5.2': ('Staff log a Notice of Proposal and its service date', 'Same day, after the consultant\'s call'),
 '5.3': ('CQC returns the application', 'Same day'),
 '5.3a': ('CQC refuses the application', 'Same day, after the consultant\'s call'),
 '5.3b': ('The new application goes back to CQC', 'Same day'),
 '5.4': ('Neither review link opened', '%%review_days%% days after 5.1, once, then stop'),
 '6.1': ('Day 7 after registration', 'Day 7'),
 '6.2': ('Day 30 after registration', 'Day 30, then monthly check-ins'),
 '6.3': ('Tender Radar match, conflict check passed, client opted in', 'When matched. One new idea a month at most'),
 '6.4': ('Month %%insp_month%% after registration', 'Once, in month %%insp_month%%'),
 '6.5': ('A PIR is logged or a PIR email is captured', 'Same day'),
 '6.6': ('A home care client mentions learning disability or autism work', 'When it comes up. One new idea a month at most'),
 '6.7': ('60 days before the policy anniversary', '60 days before'),
 '6.8': ('Registration anniversary', 'On the day'),
 '7.0': ('Bid submitted on the buyer\'s portal', '%%tender_submit%% working days before the deadline'),
 '7.1': ('The buyer awards a place', 'Same day'),
 '7.2': ('The buyer says the bid was not successful', 'Same day'),
 '7.3': ('A tender matches, or a lot needs a decision', 'When matched'),
 '7.4': ('A clarification is marked "affects us"', 'Same day'),
 '7.5': ('A framework reopens, or a market opens to the client', 'When it opens'),
 '7.6': ('Something needs the client that week', 'Monday mornings'),
 '7.7': ('The bid is ready for the client', '%%tender_approve%% working days before the deadline'),
 '7.8': ('Work starts on a new tender', 'Same day'),
 '7.9': ('A document the buyer checks runs out', '%%expiry_weeks%% weeks before it runs out'),
 '7.10': ('A contract has 6 months left', 'Once'),
 '8.1': ('No activity for 6 months', 'Once, then silence unless asked'),
 '9.1': ('Emergency (break-glass) access is used', 'Same day. Access ends after %%bg_hours%% hours'),
 '9.2': ('The client raises a concern in their Hub', 'Straight away. Acknowledged within 1 working day'),
 '9.3': ('Reassignment: a journey moves to a new consultant, once a super admin approves it', 'On the day it moves'),
 '9.4': ('The data protection lead (Collins) decides on the incident record that the people affected must be told', 'Never automatic. Rachel Turner, the other super admin, approves each one'),
 '10.1': ('Application set up in CIW Online', 'Same day'),
 '10.2': ('CIW starts asking referees', 'Same day'),
 '10.3': ('Every part of the CIW application is complete', 'Same day, with the call booked'),
 '10.4': ('Submitted in CIW Online', 'Same day'),
 '10.5': ('CIW asks for more information', 'Same day. We reply %%rfi%% working days early'),
 '10.6': ('CIW books a suitability interview', 'Reminders 7 days, 1 day, the morning'),
 '10.7': ('Registered with CIW', 'Same day'),
 '10.8': ('Staff log a CIW notice of proposal', 'Same day, after the consultant\'s call'),
 '10.9': ('CIW refuses the application', 'Same day, after the consultant\'s call'),
 '11.1': ('We ask RQIA for the Web Portal login', 'Same day'),
 '11.2': ('Submitted on the RQIA Web Portal', 'Same day'),
 '11.3': ('RQIA asks for more information', 'Same day. We reply %%rfi%% working days early'),
 '11.4': ('RQIA books fit person interviews', 'Reminders 7 days, 1 day, the morning'),
 '11.5': ('Registered with RQIA', 'Same day'),
 '11.6': ('Staff log an RQIA notice of proposal', 'Same day, after the consultant\'s call'),
 '11.7': ('RQIA refuses the application', 'Same day, after the consultant\'s call'),
 '11.8': ('The new application goes back to CIW or RQIA', 'Same day. Uses 5.3b'),
}
VER = {'1.2': ('v2', 'Divine, Mon 12 Oct'), '2.2': ('v2', 'Grace, Wed 14 Oct'), '3.1': ('v2', 'Rachel Turner, Fri 16 Oct'),
       '5.1': ('v3', 'Rachel Turner, Thu 29 Oct'), '5.2': ('v2', 'Daniel Mensah, Wed 7 Oct'), '5.3a': ('v2', 'Daniel Mensah, Wed 28 Oct'),
       '9.1': ('v2', 'Rachel Turner, Fri 30 Oct'), '10.7': ('v2', 'Collins, Thu 29 Oct'), '11.5': ('v2', 'Collins, Thu 29 Oct')}
LEGAL = {'5.2', '5.3a', '10.8', '10.9', '11.6', '11.7'}
LOCKED = {'5.1': 'Review invitation: locked', '5.4': 'One reminder: locked', '9.1': 'Same day email: locked', '9.2': 'Acknowledge in 1 working day: locked'}
# Emails no automation sends: who sends them and where they are linked from
MANUAL = {'9.4': ['Never sent automatically. The data protection lead (Collins) fills it from the incident record and signs it. Because Collins is also a super admin, Rachel Turner approves it before it goes.', 'Linked from: Security (board 84), incident 2026-01, "Tell the people affected".', 'The incident record keeps a copy and the time each one was sent.']}
MANUAL_NOTE = {'9.4': 'Never sent automatically: Rachel Turner approves'}
GROWTH = {'6.3', '6.4', '6.6', '8.1'}

def sign_of(num, v):
    if num == '1.4': return v['consultant_name']
    for k in ['weekly_owner', 'bid_lead_name', 'bid_lead', 'account_owner', 'director_name', 'approver_name', 'caller_name', 'contact_name', 'consultant_name']:
        if k in v: return v[k]
    return 'Care Sync'

def mailbox(name):
    return name.lower().replace(' ', '.') + '@caresyncexperts.co.uk'

def segs(text, v):
    """Split filled text into segments [text, kind, key]: kind 0 plain, 1 merge field, 2 registry token."""
    out = []
    pos = 0
    for m in re.finditer(r'\{\{([^}]+)\}\}|%%([a-z_0-9]+)%%', text):
        if m.start() > pos: out.append([text[pos:m.start()], 0, ''])
        if m.group(1):
            f = m.group(1)
            if f not in v: raise KeyError('missing merge value %s' % f)
            val = v[f]
            tm = re.fullmatch(r'%%([a-z_0-9]+)%%', val)
            if tm: out.append(['', 2, tm.group(1)])
            else: out.append([val, 1, f])
        else:
            out.append(['', 2, m.group(2)])
        pos = m.end()
    if pos < len(text): out.append([text[pos:], 0, ''])
    return out

def prep_lines(num, lines, conds):
    t = '\n'.join(lines).strip('\n')
    t = t.replace('every Friday', 'every %%update_day%%')
    if num == '6.5': t = t.replace('£750', '%%price_pir%%')
    if num == '6.6': t = t.replace('£1,500', '%%price_sl_addon%%')
    if num == '7.7': t = t.replace('two working days', '%%tender_submit_words%% working days')
    if num == '3.4': t = t.replace(' of 3 with', ' of %%sessions%% with')
    if num == '1.4': t = t.replace('runs your 3 sessions', 'runs your %%sessions%% sessions')
    # inline conditionals
    t = re.sub(r'\{\{if ([^}]+)\}\}(.*?)\{\{end\}\}', lambda m: m.group(2) if m.group(1)[3:] in conds or m.group(1) in conds else '', t)
    t = re.sub(r'\{\{if (bid)\}\}(.*?)\{\{end\}\}', lambda m: m.group(2) if 'bid' in conds else '', t)
    out = []
    for ln in t.split('\n'):
        m = re.search(r'\{\{if ([^}]+)\}\}', ln)
        if m:
            c = m.group(1)
            if c in conds: ln = ln.replace(m.group(0), '')
            else:
                ln = ln[:m.start()].rstrip()
                if not ln: continue
        if ln.startswith('Note:'): continue
        if ln.startswith('- '): ln = '• ' + ln[2:]
        out.append(ln)
    t = '\n'.join(out)
    t = re.sub(r'\n{3,}', '\n\n', t).strip()
    return [p for p in t.split('\n\n') if p.strip()]

def build_library():
    secs = parse()
    bynum = {}
    for s in secs:
        for e in s['emails']: bynum[e['num']] = e
    data = []
    for s in secs:
        rows = []
        for e in s['emails']:
            num = e['num']
            ck, ov, conds, note = PV[num]
            v = dict(CL[ck]); v.update(ov)
            src = e
            subj = e['subject']; btn = e['button']
            lines = e['lines']
            kind = 'email'
            if num == '11.8':
                b = bynum['5.3b']; lines = [l.replace('CQC', 'RQIA') for l in b['lines']]; subj = b['subject'].replace('CQC', 'RQIA'); btn = b['button']
            paras = prep_lines(num, lines, conds)
            texts = []
            if num == '1.3':
                kind = 'texts'
                for p in paras:
                    m = re.match(r'\*\*(.+?):\*\* (.+)$', p, re.S)
                    if m: texts.append({'label': m.group(1), 'segs': segs(m.group(2), v)})
                paras = [p for p in paras if not p.startswith('**')]
            signer = sign_of(num, v)
            ver, changed = VER.get(num, ('v1', 'Collins, Thu 1 Oct'))
            tags = []
            if num == '5.2': tags.append(['v3 waiting', 'warn'])
            if num == '11.8': tags.append(['Uses 5.3b', 'neutral'])
            else: tags.append(['Live', 'ok'])
            if kind == 'texts': tags.append(['Texts', 'info'])
            if num in GROWTH: tags.append(['Growth', 'info'])
            if num in LEGAL: tags.append(['Legal wording', 'brand'])
            if num in LOCKED: tags.append(['Locked rule', 'brand'])
            if num in MANUAL: tags = [['Live', 'ok'], ['Never automatic', 'warn'], ['Super admin approves', 'brand']]
            trig, timing = TT[num]
            rows.append({
                'num': num, 'name': e['name'], 'trig': trig, 'timing': timing, 'ver': ver, 'changed': changed, 'tags': tags,
                'subject': segs(subj, v), 'button': btn, 'paras': [segs(p, v) for p in paras], 'texts': texts, 'kind': kind,
                'client': ck, 'clientLabel': CL[ck]['label'], 'to': CL[ck]['to'], 'signer': signer, 'reply': mailbox(signer),
                'note': note, 'growth': num in GROWTH, 'legal': num in LEGAL, 'lockNote': LOCKED.get(num, '') or MANUAL_NOTE.get(num, ''), 'manual': MANUAL.get(num, []),
                'fields': [[k, v[k]] for k in sorted(set(re.findall(r'\{\{([a-z_]+)\}\}', '\n'.join(lines) + subj))) if k in v],
            })
        data.append({'n': s['n'], 'name': s['name'], 'rows': rows})
    return data

# 5.2 versions in [field] notation (the editor never shows double braces)
NOP_V2 = '''Hi [first_name],

CQC has sent a Notice of Proposal. It is not a final decision, and you have time to respond.

You have until [deadline] to send written representations, which is 28 days from the date on the notice. We have already started drafting your response, and the plan with dates is in your Hub.

If CQC still refuses after reading your response, we resubmit your application for you, as part of your package. You are not on your own with this.

[consultant_name] will call you today to talk it through.

[consultant_name]'''
NOP_V3 = '''Hi [first_name],

CQC has sent a Notice of Proposal. It is not a final decision, and you have time to respond.

You have until [deadline] to send written representations. The 28 days start on the day the notice was served, [date_served]. We count that day as day 1, which gives the earliest possible date.

We have started your response and aim to send it by [our_target], a week early. The plan with dates is in your Hub.

If CQC still refuses after reading your response, we resubmit your application for you, as part of your package. You are not on your own with this.

[consultant_name] will call you today to talk it through.

[consultant_name]'''

# Automation rules. g: group key. lock: reason. aff: clients affected today if switched off.
G = [('onb', 'Welcome and onboarding'), ('rem', 'Reminders'), ('del', 'Delivery and weekly updates'), ('reg', 'Regulators and legal deadlines'),
     ('rev', 'Reviews and feedback'), ('care', 'Care, privacy and complaints'), ('grow', 'Aftercare and growth'), ('ten', 'Tenders'), ('later', 'Later phase')]
LK_REV = 'Every registered client is invited once, at registration, whatever their feedback: Google and Trustpilot, and the client chooses. Holding back unhappy or worried clients would be review gating, which the review platforms and consumer law do not allow. Spec 51.4, rule 5.'
LK_LEGAL = 'Legal deadlines (Notice of Proposal representations, appeal windows) must never be missed. Worked out the safe way: the day of service counts as day 1. Alerts break through quiet hours. Spec 6.3 and 51.4, rule 4.'
LK_COMP = 'Complaints go to a manager or director who is not the person complained about, with an acknowledgement within 1 working day and a full reply within 20 working days. Spec 49.2 and 51.4, rule 7.'
LK_WORRY = 'A worried client gets no sales or growth messages until a manager has resolved it. The review invitation is never held back. Spec 52.4 and decisions of 4 November.'
LK_QG = 'Every pack, reply and weekly update is checked by a second person before it goes. Decided 4 November: absolute, it cannot be relaxed.'
LK_LOOK = 'Every look at a client\'s information is shown on their privacy page, including view as and emergency access. Emergency access also emails the client the same day. Spec 51.4, rule 3.'
R = [
 # id, g, name, trigger, action, owner, timing, last, runs7, fails, retry, emails, screens, lock, aff
 ('A01', 'onb', 'Paid: welcome and the introduction call', 'First instalment paid through Stripe', 'Send 1.1, create the introduction call task for Divine and start the %%intro_call%% clock', 'Divine', 'Straight away', 'Today 10:02, Meadow View Care', 2, 0, '', ['1.1'], ['IntroCall.dc.html', 'Staff.dc.html', 'Welcome.dc.html'], '', 1),
 ('A02', 'onb', 'Introduction call texts', 'Call not answered, or a call back booked', 'Text "Sorry we missed you" or "Call back confirmed". At most 3 calls and 2 texts', 'Divine', 'Straight after the call, outside quiet hours', 'Mon 26 Oct 15:10, Lindenfield Care', 1, 0, '', ['1.3'], ['IntroCall.dc.html'], '', 1),
 ('A03', 'onb', 'Call done: thank you and the onboarding form', 'Introduction call saved as "Spoke to the client"', 'Draft 1.2 for the caller to edit, then send 2.1 with the form for the package', 'Divine, then Grace', 'Straight after the call', 'Fri 30 Oct 11:30, Lindenfield Care', 1, 0, '', ['1.2', '2.1'], ['IntroCall.dc.html', 'RegDetails.dc.html', 'AddClient.dc.html'], '', 1),
 ('A04', 'onb', 'Registered manager invited', 'The client names someone else as registered manager', 'Send 2.5 to the manager with their own short task', 'Grace', 'Straight away', 'Tue 20 Oct, Harbour Lane Care', 0, 0, '', ['2.5'], ['TeamViews.dc.html', 'ManagerFlow.dc.html'], '', 2),
 ('A05', 'onb', 'Form received: checks and thank you', 'Onboarding form submitted', 'Run Companies House and document checks, then send 2.3. Held in quiet hours', 'Grace', 'Straight away, held in quiet hours', 'Thu 29 Oct 21:46, Harbour Lane Care (sent Fri 30 Oct 08:00)', 1, 0, '', ['2.3'], ['FormStaff.dc.html', 'Onboarding.dc.html', 'OnbCheck.dc.html'], '', 6),
 ('A06', 'onb', 'Mismatch: one quick question', 'A document and the form disagree, confirmed by a person', 'Send 2.4 with one tap to answer', 'Grace', 'When confirmed', 'Wed 28 Oct, Willow Bank', 1, 0, '', ['2.4'], ['AddressCheck.dc.html', 'AddressClient.dc.html'], '', 6),
 ('A07', 'onb', 'Business email connected', 'Login saved in the vault', 'Send 2.6 and start the regulator email watch', 'Case owner', 'Straight away', 'Wed 28 Oct 16:03, Harbour Lane Care', 1, 0, '', ['2.6'], ['EmailConnect.dc.html', 'PortalWatch.dc.html', 'Account.dc.html'], '', 0),
 ('A08', 'onb', 'Gates passed: handover', 'All 8 onboarding gates pass', 'Ask a manager to approve the handover; on approval send 1.4, unlock sessions and set the weekly update owner. Never at welcome', 'Grace, then a manager', 'When the last gate passes', 'Thu 29 Oct, Binnian Care', 1, 0, '', ['1.4'], ['Onboarding.dc.html', 'Handover.dc.html', 'ManagerDash.dc.html', 'Sessions.dc.html'], '', 6),
 ('A09', 'rem', 'Onboarding form reminders', 'Onboarding form not finished', 'Send 2.2, which opens the exact task; Grace calls; stops when done', 'Grace', '%%form_rem%%', 'Today 09:00, 1 reminder', 4, 0, 'Retries 3 times in 1 hour, then tells Grace', ['2.2'], ['OnboardingQueue.dc.html', 'RegDetails.dc.html'], '', 3),
 ('A10', 'rem', 'Document reminders', 'A requested document is not uploaded', 'Send a reminder that opens the upload; then "needs a call"', 'Case owner', '%%doc_rem%%', 'Fri 30 Oct, 3 reminders', 7, 0, 'Retries 3 times in 1 hour, then tells the owner', ['2.2'], ['Documents.dc.html', 'Staff.dc.html'], '', 9),
 ('A11', 'rem', 'Landlord, referee and accountant reminders', 'A one-task link is not used', 'Send the third party a reminder of their one task', 'Grace', '%%third_rem%%', 'Fri 30 Oct, 2 reminders', 2, 0, 'Retries 3 times in 1 hour, then tells Grace', [], ['ThirdParty.dc.html', 'Onboarding.dc.html'], '', 4),
 ('A12', 'rem', 'Review and signature reminders', 'A draft waits for review, or the pack waits for a signature', 'Remind the client; for signatures the consultant then calls', 'Case owner', 'Review %%draft_rem%%. Signature %%sig_rem%%', 'Thu 29 Oct, Bright Path Care', 2, 0, 'Retries 3 times in 1 hour, then tells the owner', ['3.2', '3.3'], ['Review.dc.html', 'Sign.dc.html'], '', 5),
 ('A13', 'rem', 'Session reminders', 'A session is booked', 'Send 3.4, then reminders the day before and an hour before', 'Millicent', 'Day before, hour before', 'Today 09:00, Bright Path Care', 5, 0, 'Retries 3 times in 15 minutes', ['3.4'], ['Sessions.dc.html', 'CoachSessions.dc.html'], '', 30),
 ('A14', 'rem', 'Interview reminders', 'The regulator books an interview', 'Remind 7 days, 1 day and the morning before, with the Interview Preparation Hub link', 'Case owner', '7 days, 1 day, the morning', 'Tue 27 Oct, Elm Tree Care', 1, 0, 'Retries 3 times in 15 minutes', ['4.3', '10.6', '11.4'], ['Cqc.dc.html', 'RegCentre.dc.html'], '', 3),
 ('A15', 'rem', 'Document expiry warning', 'A document runs out', 'Send 7.9 and add a task for the owner', 'Case owner', '%%expiry_weeks%% weeks before', 'Fri 30 Oct, Oakleaf Living', 1, 0, 'Retries 3 times in 1 hour', ['7.9'], ['TenderWork.dc.html', 'Deadlines.dc.html'], '', 5),
 ('A16', 'del', 'Weekly update', 'The weekly update day', 'Open the nine-part draft for each owner on Monday, chase on Wednesday, second-person check on Thursday, send 3.1', 'Weekly update owners', 'Every %%update_day%% by %%update_time%%', 'Fri 30 Oct, 41 sent, 1 bounced', 42, 1, 'Retry blocked until the address is fixed', ['3.1'], ['Weekly.dc.html', 'Staff.dc.html', 'Main.dc.html', 'Reports.dc.html'], '', 42),
 ('A17', 'del', 'Bounced email', 'A client email bounces', 'Alert the owner, mark the update overdue, hold the resend until the address is confirmed', 'Case owner', 'Straight away', 'Fri 30 Oct 17:02, Greenway Support', 1, 0, '', [], ['Health.dc.html', 'Weekly.dc.html', 'ClientsList.dc.html'], '', 0),
 ('A18', 'del', 'Pack moves forward', 'A draft passes the second check, or every document is approved and consistent', 'Send 3.2 to review, or 3.3 to sign', 'Case owner', 'Same day', 'Fri 30 Oct, Bright Path Care', 3, 0, 'Retries 3 times in 1 hour', ['3.2', '3.3'], ['DocRoom.dc.html', 'Sign.dc.html'], '', 20),
 ('A19', 'del', 'Signed: submit and tell the client', 'The client signs the final pack', 'Submit within %%send_after%% from the client\'s own email, then send 4.1, 10.4 or 11.2 the same day', 'Case owner', 'Within %%send_after%%', 'Fri 23 Oct, Riverside Homecare', 0, 0, 'Retries 3 times, then tells the owner and a manager', ['4.1', '10.4', '11.2'], ['Cqc.dc.html', 'RegCentre.dc.html', 'Deadlines.dc.html'], '', 20),
 ('A20', 'del', 'Unanswered message', 'A client question waits', 'Alert the team lead after 6 working hours; red on My day and the manager dashboard after %%unanswered%%', 'Team lead', 'Working hours only', 'Today 08:30, 0 late', 6, 0, '', [], ['Questions.dc.html', 'Staff.dc.html', 'ManagerDash.dc.html'], '', 52),
 ('A21', 'reg', 'Regulator watch', 'New email from CQC, or a change on CIW Online or the RQIA Web Portal', 'File it, tell the case owner, tell the client the same day', 'Case owner', 'CQC email every few minutes; CIW and RQIA every working day', 'Today 09:35', 980, 0, 'Retries every 5 minutes. A gap over 7 days turns red', [], ['PortalWatch.dc.html', 'Cqc.dc.html', 'Health.dc.html'], '', 12),
 ('A22', 'reg', 'Notice of Proposal logged', 'Staff enter the service date from the notice', 'Work out the legal deadline the safe way, create tasks (draft day %%nop_draft%%, review day %%nop_review%%, send day %%nop_send%%), send 5.2 after the call', 'Case owner and a director', 'Same day', 'Wed 21 Oct, Sunrise Homecare', 0, 0, 'Retries every 5 minutes and alerts a director', ['5.2', '10.8', '11.6'], ['RegReply.dc.html', 'Deadlines.dc.html', 'Cqc.dc.html'], LK_LEGAL, 1),
 ('A23', 'reg', 'Legal deadline alerts', 'A legal deadline is open', 'Alert the consultant and a director on days 7, 14, 21 and 25, then every day in the last 3 days. Goes through quiet hours, and by text', 'Case owner and a director', 'Days 7, 14, 21, 25, then daily', 'Today 07:00, Sunrise and Westbrook', 2, 0, 'Retries every 5 minutes and alerts both super admins', [], ['Deadlines.dc.html', 'Staff.dc.html', 'ManagerDash.dc.html'], LK_LEGAL, 2),
 ('A24', 'reg', 'Refusal logged', 'Staff enter the notice of decision date', 'Work out the appeal window the safe way, send 5.3a (10.9, 11.7) after the call, open the resubmission plan', 'Case owner and a director', 'Same day', 'Mon 26 Oct, Westbrook Care', 0, 0, 'Retries every 5 minutes and alerts a director', ['5.3a', '10.9', '11.7'], ['ResubmitStaff.dc.html', 'Resubmit.dc.html', 'Deadlines.dc.html'], LK_LEGAL, 1),
 ('A25', 'reg', 'The regulator asks or books', 'More information requested, or an interview booked', 'Send 4.2 or 4.3 (CIW 10.5, 10.6; RQIA 11.3, 11.4); our reply target %%rfi%% working days before the regulator\'s date', 'Case owner', 'Same day', 'Tue 27 Oct, Elm Tree Care', 1, 0, 'Retries 3 times in 15 minutes', ['4.2', '4.3', '10.5', '10.6', '11.3', '11.4'], ['RegReply.dc.html', 'Cqc.dc.html', 'RegCentre.dc.html'], '', 12),
 ('A26', 'reg', 'Registered', 'Registration confirmed', 'Send 5.1 (10.7, 11.5) with the Registration File; start aftercare for full start-up clients and those who bought it', 'Case owner', 'Same day', 'Mon 19 Oct, Brookside Homecare', 0, 0, 'Retries 3 times, then tells the owner', ['5.1', '10.7', '11.5'], ['Celebrate.dc.html', 'EmailRegistered.dc.html', 'Aftercare.dc.html'], '', 12),
 ('A27', 'rev', 'Review invitation', 'Registration confirmed', 'Invite once, inside 5.1: Review us on Google, or on Trustpilot, the client chooses, or tell us privately', 'Divine', 'At registration, once', 'Mon 19 Oct, Brookside Homecare', 0, 0, 'Retries 3 times, then tells Divine', ['5.1'], ['Celebrate.dc.html', 'EmailRegistered.dc.html', 'Reports.dc.html'], LK_REV, 12),
 ('A28', 'rev', 'Review reminder', 'Neither review link opened', 'Send 5.4 once, then stop', 'Divine', '%%review_days%% days after 5.1', 'Mon 26 Oct, Brookside Homecare', 1, 0, 'Retries 3 times', ['5.4'], ['Reports.dc.html'], LK_REV, 12),
 ('A29', 'rev', 'How do you feel? check', 'After onboarding, after submission, after the decision, then monthly in aftercare', 'One tap, three faces, in the Hub', 'Divine', 'Three moments, then monthly', 'Fri 30 Oct, 4 answers', 4, 0, '', [], ['ClientStates.dc.html', 'ClientCare.dc.html', 'Reports.dc.html'], '', 52),
 ('A30', 'rev', 'Unhappy answer', 'An unhappy or neutral face', 'Alert the manager, who calls within 1 working day (a director if the manager is involved), and marks the client worried', 'Manager', 'Straight away', 'Fri 30 Oct, Riverside Homecare', 1, 0, '', [], ['ClientCare.dc.html', 'ManagerDash.dc.html'], '', 52),
 ('A31', 'rev', 'Worried client: no sales or growth messages', 'A client is marked worried', 'Stop every sales and growth message until resolved. Delivery emails and the review invitation still go', 'Manager', 'Until resolved', 'Fri 30 Oct, Riverside Homecare (1 held)', 1, 0, '', ['6.3', '6.4', '6.6', '8.1'], ['ClientsList.dc.html', 'ManagerDash.dc.html', 'Radar.dc.html'], LK_WORRY, 1),
 ('A32', 'rev', 'Public review reply', 'A review appears on Google or Trustpilot', 'Create a reply task in My day', 'Divine', 'Reply within 2 working days', 'Tue 27 Oct, 1 review', 1, 0, '', [], ['Staff.dc.html', 'ClientCare.dc.html'], '', 0),
 ('A33', 'care', 'Concern raised', 'The client raises a concern in their Hub', 'Send 9.2, route it to a manager or director not involved, open it in the complaints register', 'Collins and Rachel Turner', 'Acknowledge within 1 working day; full reply within 20 working days', 'Sat 31 Oct 10:03, Harbour Lane Care', 1, 0, 'Retries every 5 minutes and alerts both super admins', ['9.2'], ['ViewAs.dc.html', 'Account.dc.html', 'Reports.dc.html'], LK_COMP, 52),
 ('A34', 'care', 'Every look shown to the client', 'Anyone opens a client\'s information, uses view as, or uses emergency access', 'Add it to the client\'s privacy page; emergency access also sends 9.1 the same day and alerts both super admins', 'Collins (data protection lead)', 'Straight away', 'Today 08:50, Harbour Lane Care (view as)', 214, 0, 'Retries every minute and alerts both super admins', ['9.1'], ['Account.dc.html', 'SecurityCentre.dc.html', 'ViewAs.dc.html'], LK_LOOK, 52),
 ('A35', 'care', 'New consultant', 'Reassignment approved: a journey moves to a new consultant', 'Send 9.3, hand over mailbox connections and tasks', 'Manager', 'On the day it moves', 'Next: Mon 9 Nov, Kingsway and Cedar Lodge (decision 5)', 0, 0, 'Retries 3 times', ['9.3'], ['TeamCover.dc.html', 'PeopleAccess.dc.html', 'Account.dc.html'], '', 6),
 ('A36', 'grow', 'Aftercare check-ins', 'Day 7 and day 30 after registration, then monthly', 'Send 6.1 and 6.2, then a monthly check-in for aftercare clients', 'Case owner', 'Day 7, day 30, then monthly', 'Mon 26 Oct, Brookside Homecare', 1, 0, 'Retries 3 times', ['6.1', '6.2'], ['Aftercare.dc.html', 'AftercareStaff.dc.html'], '', 10),
 ('A37', 'grow', 'First inspection readiness', 'Month %%insp_month%% after registration (full start-up aftercare)', 'Send 6.4. Never to a worried client or during a refusal; one new idea a month at most', 'Case owner', 'Month %%insp_month%%', 'Thu 22 Oct, Bryn Glas Care', 0, 0, 'Retries 3 times', ['6.4'], ['Aftercare.dc.html', 'AftercareStaff.dc.html'], '', 10),
 ('A38', 'grow', 'PIR received', 'A PIR is logged or a PIR email is captured', 'Send 6.5 with the price book price', 'Case owner', 'Same day', 'Wed 28 Oct, Ashby Care', 1, 0, 'Retries 3 times', ['6.5'], ['PriceBook.dc.html', 'AftercareStaff.dc.html'], '', 10),
 ('A39', 'grow', 'Policy review and anniversary', '60 days before the policy anniversary; the registration anniversary', 'Send 6.7, and 6.8 on the day', 'Case owner', '60 days before; on the day', 'Mon 12 Oct, Foyle Home Care', 0, 0, 'Retries 3 times', ['6.7', '6.8'], ['Aftercare.dc.html'], '', 10),
 ('A40', 'grow', 'Tender in your area', 'Tender Radar match, conflict check passed, client opted in', 'The case owner approves first, then 6.3 goes. One new idea a month at most', 'Jo Martin', 'When matched', 'Held: Maple Court (waiting for "Accept the bid work")', 0, 0, '', ['6.3'], ['Radar.dc.html', 'ManagerDash.dc.html'], '', 10),
 ('A41', 'grow', 'Win-back', 'No activity for 6 months', 'Send 8.1 once, then silence unless the client asks', 'Collins', 'Once', 'Wed 7 Oct, 1 sent', 0, 0, 'Retries 3 times', ['8.1'], ['Reports.dc.html'], '', 0),
 ('A42', 'ten', 'Tender timeline', 'A bid deadline is set', 'Draft %%tender_draft%%, client approval %%tender_approve%% (7.7) and submit %%tender_submit%% working days before the deadline (7.0); Monday list (7.6)', 'Bid lead', 'Worked back from the buyer\'s deadline', 'Today 07:00, Oakleaf Living', 2, 0, 'Retries every 15 minutes and alerts the bid lead', ['7.7', '7.0', '7.6'], ['Tender.dc.html', 'TenderWork.dc.html', 'TenderClient.dc.html'], '', 5),
 ('A43', 'ten', 'New tender or match', 'A tender matches a client, or work starts on one', 'Send 7.3 (the client decides), then 7.8 to check what we hold', 'Bid lead', 'When matched', 'Thu 29 Oct, Oakleaf Living (Eastford)', 1, 0, 'Retries 3 times', ['7.3', '7.8'], ['BidDecision.dc.html', 'TenderConfirm.dc.html'], '', 5),
 ('A44', 'ten', 'The buyer changed something', 'A clarification is marked "affects us"', 'Send 7.4 with what we did and anything needed', 'Bid lead', 'Same day', 'None yet', 0, 0, 'Retries 3 times', ['7.4'], ['Tender.dc.html', 'TenderClient.dc.html'], '', 5),
 ('A45', 'ten', 'Results, renewals and reopened markets', 'An award result, a contract with 6 months left, or a framework reopening', 'Send 7.1 or 7.2, 7.10, or 7.5', 'Bid lead', 'Same day', 'Mon 5 Oct, 1 renewal', 0, 0, 'Retries 3 times', ['7.1', '7.2', '7.10', '7.5'], ['Tenders.dc.html', 'Radar.dc.html'], '', 5),
 ('A46', 'reg', 'Second-person check before a pack goes', 'A pack or reply is ready to send', 'Block sending until a second consultant has checked it. Cannot be relaxed', 'Manager', 'Every pack and reply', 'Fri 30 Oct, Sunrise Homecare draft', 3, 0, '', [], ['RegReply.dc.html', 'Weekly.dc.html'], LK_QG, 26),
 ('L01', 'later', 'WhatsApp copy of the weekly update', 'Weekly update sent, client chose WhatsApp', 'Send a short WhatsApp with a link to the update', 'Weekly update owners', 'Later phase', 'Never run', 0, 0, '', [], ['Account.dc.html'], '', 0),
 ('L02', 'later', 'WhatsApp reminders', 'Interview or legal deadline reminder due', 'Send the reminder by WhatsApp as well', 'Case owner', 'Later phase', 'Never run', 0, 0, '', [], ['Account.dc.html'], '', 0),
]
RULES = []
for r in R:
    (i, g, name, trig, act, owner, timing, last, runs, fails, retry, emails, screens, lock, aff) = r
    RULES.append(dict(id=i, g=g, name=name, trig=trig, act=act, owner=owner, timing=timing, last=last, runs=runs, fails=fails,
                      retry=retry or 'Retries 3 times in 1 hour, then tells the owner', emails=emails, screens=screens, lock=lock, aff=aff, later=(g == 'later')))
assert sum(1 for r in RULES if not r['later']) == 46, sum(1 for r in RULES if not r['later'])
