import sys
def icon(n,s=24): return f'<x-import component-from-global-scope="CareSync.Icon" name="{n}" size="{{{{n{s}}}}}"></x-import>'
def btn(t,primary=True):
    if primary: return f'<span style="min-height: 48px; border-radius: 12px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 500;">{t}</span>'
    return f'<span style="min-height: 44px; border-radius: 12px; border: 1px solid var(--cs-border-control); display: flex; align-items: center; justify-content: center; font-size: 15px;">{t}</span>'
def link(t): return f'<span style="min-height: 40px; display: flex; align-items: center; justify-content: center; color: var(--cs-text-brand); font-size: 14px; font-weight: 500;">{t}</span>'
def chip(t,on=False):
    st='border: 2px solid var(--cs-action-primary); background: var(--cs-selection-bg); color: var(--cs-selection-text); font-weight: 500;' if on else 'border: 1px solid var(--cs-border-default); background: var(--cs-surface-raised);'
    return f'<span style="display: inline-flex; align-items: center; min-height: 40px; padding: 0 14px; border-radius: 999px; font-size: 14px; margin: 0 6px 6px 0; {st}">{t}</span>'
def badge(ic,tone):
    bg={'brand':'var(--cs-surface-brand)','warn':'var(--cs-status-warning-bg)','ok':'var(--cs-status-success-bg)','err':'var(--cs-status-error-bg)','info':'var(--cs-status-info-bg)'}[tone]
    return f'<span aria-hidden="true" style="width: 52px; height: 52px; border-radius: 999px; background: {bg}; display: flex; align-items: center; justify-content: center;">{icon(ic)}</span>'
def p(t,muted=True): return f'<span style="font-size: 14px; line-height: 20px; color: var({"--cs-text-secondary" if muted else "--cs-text-primary"});">{t}</span>'
def box(inner): return f'<div style="padding: 12px 14px; border-radius: 12px; background: var(--cs-surface-raised); box-shadow: var(--cs-elevation-1); display: flex; flex-direction: column; gap: 6px; font-size: 14px; line-height: 20px;">{inner}</div>'
def card(tag,ic,tone,title,body,foot):
    return f'''<article style="flex: 0 0 340px; min-height: 760px; background: var(--cs-surface-page); border-radius: 24px; box-shadow: var(--cs-elevation-2); padding: 24px 18px; display: flex; flex-direction: column; gap: 14px; box-sizing: border-box;">
<span style="font-size: 12px; line-height: 16px; color: var(--cs-text-brand); font-weight: 500;">{tag}</span>
{badge(ic,tone)}
<h2 style="margin: 0; font-size: 21px; line-height: 28px; font-weight: 600;">{title}</h2>
{body}
<div style="margin-top: auto; display: flex; flex-direction: column; gap: 8px;">{foot}</div>
</article>'''
row1=[
 card('First sign-in','shield-check','brand','Before you start: how we look after your information',
  box('<span>We only use your information to deliver your package.</span><span>Every time someone at Care Sync looks at your documents or email, you can see it.</span><span>You can download or correct your information at any time.</span>')+p('<span style="color: var(--cs-text-brand); font-weight: 500;">Read our privacy notice</span>. It explains this in full. It is information for you, not something to agree to.')+'<span style="display: flex; align-items: center; gap: 10px; min-height: 40px; font-size: 14px;"><span aria-hidden="true" style="width: 22px; height: 22px; border-radius: 6px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center; font-size: 13px;">&#10003;</span>I have read it</span>'+box('<span style="font-weight: 500;">Separately, only if you want</span><span>May we text you about your introduction call and urgent legal deadlines? You can change this any time.</span><div>'+chip('Yes, text me',True)+chip('No, thanks')+'</div>'),
  btn('Continue')),
 card('Sign-in link expired','clock','warn','This link has expired',
  p('For your security, sign-in links only work for a short time and only once. We can send you a fresh one straight away.'),
  btn('Send me a new link')+link('Ask us for help')),
 card('Nothing to do today','circle-check','ok','Nothing needs you today',
  p('Daniel is writing your business plan. Your next update is on <span>{{updDay}}</span>.')+box('<span style="font-weight: 500;">Coming up</span><span>Session 2 with Millicent, Thursday 10:00</span>'),
  link('See what we have done for you')),
 card('No news yet','inbox','info','No news from CQC yet',
  p('This is normal at this stage. We check your business email for CQC every few minutes, so you will hear the same day anything arrives.')+box('<span>Last checked: today, 10:42</span><span>Sent to CQC: 1 December</span>'),
  link('What usually happens next')),
 card('Upload problems','upload','warn','This photo is a little blurry',
  p('We could not read the dates. Lay it flat in good light and try again.')+box('<span style="font-weight: 500;">Also checked</span><span>This is a council tax bill. It counts as one of your three ID documents, so we have added it there for you.</span>'),
  btn('Take it again')+link('Upload a file instead (PDF, JPG or PNG, up to 20 MB)')),
 card('No internet','refresh-cw','info','You are offline',
  p('Keep going. Your answers are saved on this phone and will send automatically as soon as you are back online.')+box('<span>3 answers waiting to send</span>'),
  btn('Carry on',False)),
 card('Something went wrong','triangle-alert','err','Sorry, that did not work',
  p('Nothing you entered is lost, and our team has already been told. Please try again in a moment.'),
  btn('Try again')+link('Ask us for help')),
]
row2=[
 card('Paying','file-check','brand','Your second instalment',
  box('<span style="display: flex; justify-content: space-between; gap: 8px;"><span>Second instalment of 3, as in your agreement</span><span style="font-weight: 600; white-space: nowrap;">£2,833.33 + VAT</span></span><span style="font-size: 12px; color: var(--cs-text-muted);">Full start-up package. Due when you sign off your final pack</span>')+'<div>'+chip('Card',True)+chip('Other ways Stripe offers')+'</div>',
  btn('Pay securely with Stripe')+link('Talk to us about payment')),
 card('Payment received','circle-check','ok','Thank you, that is paid',
  box('<span>Second instalment: £2,833.33 + VAT</span><span>Paid by card through Stripe, 27 November</span><span>Receipt saved in your account</span>'),
  btn('Download receipt',False)),
 card('How are we doing?','users','brand','How are we doing so far?',
  p('One tap. It helps us look after you.')+'<div>'+chip('Happy')+chip('Okay')+chip('Not happy')+'</div>'+box('<span style="color: var(--cs-text-muted);">Anything you would like to tell us? (optional)</span>'),
  btn('Send')+p('If you are not happy, a manager calls you within 1 working day, and shares what you said with Daniel with care.')),
 card('Raise a concern','circle-alert','warn','Tell us what is not right',
  box('<span style="color: var(--cs-text-muted);">What happened, and what would put it right?</span><span style="min-height: 80px;"></span>'),
  btn('Send to a manager')+p('A manager, not your consultant, handles it, or a director if the manager is involved. We confirm we have it within 1 working day.')),
 card('Pause reminders','calendar','info','Pause reminders',
  p('Need a break, for a holiday or a difficult time? We will stop reminders until you are back.')+'<div>'+chip('1 week')+chip('2 weeks',True)+chip('Pick a date')+'</div>',
  btn('Pause until 18 November')+p('Daniel is told, and legal deadline alerts still come through, so any CQC deadlines are still looked after.')),
 card('Help','circle-help','brand','How can we help?',
  box('<span style="color: var(--cs-text-muted);">Search help</span>')+box('<span>What is a registered manager?</span><span>What is a DBS check, and do I need one?</span><span>What does CQC do with my application?</span><span>Can I change my answers later?</span>'),
  link('Ask a person instead')),
 card('Refer someone','link','brand','Know someone starting a care business?',
  p('If someone you know could use our help, share your link. We will look after them as we looked after you.'),
  btn('Share my link')+p('No pressure, and we never contact anyone without their permission.')),
]
def row(cards): return '<div style="display: flex; gap: 24px; align-items: stretch;">'+''.join(cards)+'</div>'
page=f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>Client states and moments</title>
<script src="./support.js"></script>
<script src="./registry.js"></script>
<link rel="stylesheet" href="ds/caresync/assets/Reference/care-sync-tokens-final.css">
<link rel="stylesheet" href="ds/caresync/components/bundle.css">
<script src="ds/caresync/components/bundle.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kanit:wght@400;500;600;700&display=swap">
<style>
:root{{--font-sans:Kanit, sans-serif}}
body{{margin:0}}
</style>
</helmet>
<div data-cs-theme="{{{{theme}}}}" style="width: 2588px; min-height: 1760px; background: var(--cs-surface-subtle); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; padding: 32px; box-sizing: border-box; display: flex; flex-direction: column; gap: 24px;">
  <header style="display: flex; flex-direction: column; gap: 4px;">
    <h1 style="margin: 0; font-size: 28px; line-height: 36px; font-weight: 600;">Every state and small moment, designed</h1>
    <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Top row: what the client sees when things are new, empty, slow or go wrong. Bottom row: the smaller moments around paying, feedback, concerns, breaks, help and referrals. Each card is one phone screen.</span>
  </header>
  {row(row1)}
  {row(row2)}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"theme":{{"editor":"enum","options":["light","dark"],"default":"light"}},"$preview":{{"width":2588,"height":1760}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{ theme: this.props.theme ?? 'light', n24: 24, updDay: (window.CSR && CSR.get('weekly-update-day', 'Friday')) || 'Friday' }}; }}
}}
</script>
</body>
</html>
'''
open(sys.argv[1],'w').write(page)
