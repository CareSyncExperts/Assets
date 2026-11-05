import sys
def chip(t,on=False):
    if on: return f'<span style="display: inline-flex; align-items: center; min-height: 40px; padding: 0 14px; border-radius: 999px; border: 2px solid var(--cs-action-primary); background: var(--cs-selection-bg); color: var(--cs-selection-text); font-size: 14px; font-weight: 500;">{t}</span>'
    return f'<span style="display: inline-flex; align-items: center; min-height: 40px; padding: 0 14px; border-radius: 999px; border: 1px solid var(--cs-border-default); background: var(--cs-surface-raised); font-size: 14px;">{t}</span>'
def field(label,val):
    return f'<div style="display: flex; flex-direction: column; gap: 4px;"><span style="font-size: 13px; line-height: 18px; font-weight: 500;">{label}</span><span style="min-height: 46px; padding: 0 12px; border-radius: 10px; border: 1px solid var(--cs-border-control); display: flex; align-items: center; font-size: 15px; background: var(--cs-surface-raised);">{val}</span></div>'
def btn(t,primary=True):
    if primary: return f'<span style="min-height: 48px; border-radius: 12px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 500;">{t}</span>'
    return f'<span style="min-height: 44px; border-radius: 12px; border: 1px solid var(--cs-border-control); display: flex; align-items: center; justify-content: center; font-size: 15px;">{t}</span>'
def card(tag,title,why,body,foot):
    return f'''<article style="flex: 0 0 340px; background: var(--cs-surface-page); border-radius: 24px; box-shadow: var(--cs-elevation-2); padding: 22px 18px; display: flex; flex-direction: column; gap: 14px; box-sizing: border-box;">
<span style="font-size: 12px; line-height: 16px; color: var(--cs-text-brand); font-weight: 500;">{tag}</span>
<h2 style="margin: 0; font-size: 20px; line-height: 28px; font-weight: 600;">{title}</h2>
<span style="font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">{why}</span>
{body}
<div style="margin-top: auto; display: flex; flex-direction: column; gap: 8px;">{foot}</div>
</article>'''
cards=[
 card('K. Insurance, when the quote starts','A few questions for your insurance quote','So Daniel can get a quote that fits. We send it to you to choose.',
  '<span style="font-size: 14px; font-weight: 500;">Staff in your first year</span><div style="display: flex; flex-wrap: wrap; gap: 6px;">'+chip('1 to 5')+chip('6 to 15',True)+chip('16 or more')+'</div><span style="font-size: 14px; font-weight: 500;">Any insurance claims before?</span><div style="display: flex; gap: 6px;">'+chip('No',True)+chip('Yes')+'</div>',
  btn('Save')),
 card('J. Business plan money','Money questions, or ask your accountant','CQC wants to see the service can pay its way. Rough figures are fine.',
  field('Money available to start','£25,000')+field('Monthly costs, first year','About £9,000'),
  btn('Save')+btn('Send these to my accountant',False)),
 card('L. Interview details','CQC has set your interview','We read the date from CQC\'s email. Just check it.',
  '<div style="padding: 14px; border-radius: 12px; background: var(--cs-surface-raised); box-shadow: var(--cs-elevation-1); display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 18px; line-height: 26px; font-weight: 600;">Tuesday 26 January, 10:30</span><span style="font-size: 13px; color: var(--cs-text-secondary);">Video call. Ruth, registered manager</span></div><span style="font-size: 14px; font-weight: 500;">Is Amara joining too?</span><div style="display: flex; gap: 6px;">'+chip('Yes',True)+chip('No')+chip('Not sure')+'</div>',
  btn('That\'s right')),
 card('B. Not formed yet','Let us set up your company','You chose "my company is not formed yet". Three things and we do the rest.',
  field('Name you would like','Willow Bank Care Ltd')+'<span style="display: flex; gap: 6px; align-items: center; font-size: 13px; color: var(--cs-status-success-text);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"></path></svg>No other company has this name</span>'+field('Directors','You, and anyone else you add'),
  btn('Continue')),
 card('Q. Declarations','One last confirmation','Read in plain English. You sign once, at the end, with your pack.',
  '<div style="padding: 14px; border-radius: 12px; background: var(--cs-surface-raised); box-shadow: var(--cs-elevation-1); display: flex; flex-direction: column; gap: 10px; font-size: 14px; line-height: 20px;"><span>The information I have given is true to the best of my knowledge.</span><span>I will tell Care Sync if anything changes, like the office or the manager.</span><span>Care Sync may send my application to CQC by email for me.</span></div>',
  btn('Agree and sign with my pack')),
]
page=f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>Small tasks</title>
<script src="./support.js"></script>
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
<div data-cs-theme="{{{{theme}}}}" style="width: 1880px; min-height: 900px; background: var(--cs-surface-subtle); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; padding: 32px; box-sizing: border-box; display: flex; flex-direction: column; gap: 20px;">
  <header style="display: flex; flex-direction: column; gap: 4px;">
    <h1 style="margin: 0; font-size: 28px; line-height: 36px; font-weight: 600;">Small tasks, each arriving when it is needed</h1>
    <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">The smaller form sections, each a single phone screen. Letters match the sections in the form builder (board 44). Never more than 3 waiting at once.</span>
  </header>
  <div style="display: flex; gap: 24px; align-items: stretch;">
    {''.join(cards)}
  </div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"theme":{{"editor":"enum","options":["light","dark"],"default":"light"}},"$preview":{{"width":1880,"height":900}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{ theme: this.props.theme ?? 'light' }}; }}
}}
</script>
</body>
</html>
'''
open(sys.argv[1],'w').write(page)
