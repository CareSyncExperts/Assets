import html
P=[
 ("Paid and welcomed","25 Welcome, 33 Introduction call","Takes a friendly call. Nothing to type","Client added with their package (board 51); payment creates the introduction call (Divine by default, anyone can take it); sales notes carried over","1.1 Welcome, 1.2 Lovely to speak to you, 1.3 Call texts, 1.4 Meet your team","Who calls, how fast, retries, the call guide, welcome wording"),
 ("Onboarding form","46 Onboarding form, 47 Manager's part, 23 Find your company, 26 Your manager, 35 Who you support, 36 Directors","Answers their tailored form, at their own pace. Stops and resumes any time","Sent after the introduction call, tailored to the package chosen when the client was added (board 51). The project starts only when it is complete","2.1 Your onboarding form, 2.2 Gentle reminder, 2.5 Your manager's invite","Packages and their sections (form builder, board 44), reminder timings"),
 ("Documents and email","46 Registration details, 47 Manager's part, 3 From you, 15 One quick question, 27 Business email","Photos and one-tap answers","Photos read; address checked across documents; email login into the vault","2.2 Gentle reminder, 2.4 One quick question, 2.6 Email connected","Reminder timings, quiet hours, vault roles, retention"),
 ("Writing and review","1 Today, 2 Journey, 21 Done for you, 18 Written for you, 4 Review, 28 Sessions","Comments, approves, books session 2","Pack written; Pack Doctor checks; Friday update every week","3.1 Friday update, 3.2 Draft ready, 3.4 Session booked","Pack Doctor rules, update template, reply-time promise"),
 ("Sign","19 Sign your pack","Signs once","Second consultant checks; names and addresses match everywhere","3.3 Final pack ready to sign","E-signature settings, who can approve a pack"),
 ("Sent to CQC","5 CQC centre","Nothing","Sent from the client's own email; copy kept on the timeline","4.1 Submitted","Email connection health; CQC email rules"),
 ("With CQC","5 CQC centre, 6 Ask, Interview Preparation Hub link","Answers CQC's questions with us; interview practice","Replies drafted; interview prepared; nothing missed","4.2 More information, 4.3 Interview booked, 4.4 After the interview","Watch rules, reminder timings, Interview Hub link"),
 ("Decision","20 Registered, 17 Email, 5 Notice of Proposal","Celebrates, or reviews a calm plan","Registration File; or the written response within 28 days","5.1 Registered, 5.2 Notice of Proposal, 5.3 Returned, 5.4 Review reminder (once)","Google and Trustpilot links, reviews policy"),
 ("Aftercare, 12 months","30 Aftercare, 29 Account and privacy","Monthly check-in; ticks the readiness list","Check-ins, policy review reminders, inspection readiness","6.1 Launch checklist, 6.2 Day 30, 6.4 Readiness, 6.7 Policy review, 6.8 Your year","Aftercare length per package, check-in rhythm"),
 ("Grow, then hand back","30 Grow, 50 Should we bid, 48 Tender profile, 49 Your tenders, 31 Tender detail","Chooses what fits, if anything","Tender Radar matches; supported living; PIR; logins handed back at the end","6.3 Tender near you, 6.5 PIR, 6.6 Supported living, 7.1 and 7.2 Tender result, 8.1 Win-back","Price book, offer rules (no false urgency), hand-back checklist, deletion"),
]
ROWS=[("The client sees",1,"chips"),("The client does",2,"txt"),("We do for them",3,"txt"),("Emails sent",4,"mail"),("Super admin controls",5,"admin")]
def esc(s): return html.escape(s, quote=True)
cells=[]
grid='display: grid; grid-template-columns: 132px repeat(10, minmax(0, 1fr)); gap: 8px; align-items: stretch;'
# phase header row
hdr=f'<div style="{grid}"><span></span>'
for i,p in enumerate(P):
    hdr+=f'''<div style="display: flex; flex-direction: column; gap: 6px; padding: 12px; border-radius: 12px; background: var(--cs-surface-inverse); color: #FFFFFF;"><span style="width: 26px; height: 26px; border-radius: 999px; background: #AEFFEF; color: #004558; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600;">{i+1}</span><span style="font-size: 15px; line-height: 20px; font-weight: 500;">{esc(p[0])}</span></div>'''
hdr+='</div>'
body=''
for label,idx,kind in ROWS:
    admin = kind=='admin'
    lab_style='font-size: 13px; line-height: 18px; font-weight: 600; color: var(--cs-text-brand);' if admin else 'font-size: 13px; line-height: 18px; font-weight: 500; color: var(--cs-text-secondary);'
    row=f'<div style="{grid}"><span style="padding: 12px 4px; display: flex; align-items: flex-start; gap: 6px; {lab_style}">'
    if admin: row+='<x-import component-from-global-scope="CareSync.Icon" name="settings" size="{{n16}}"></x-import>'
    row+=f'{esc(label)}</span>'
    for p in P:
        v=p[idx]
        cs='padding: 10px 12px; border-radius: 10px; font-size: 13px; line-height: 18px; '
        if admin: cs+='background: var(--cs-selection-bg); color: var(--cs-selection-text); font-weight: 500;'
        else: cs+='background: var(--cs-surface-raised); box-shadow: var(--cs-elevation-1);'
        if kind=='chips':
            inner=''.join(f'<span style="display: inline-block; margin: 0 4px 4px 0; padding: 2px 8px; border-radius: 999px; background: var(--cs-surface-brand); color: var(--cs-text-brand); font-size: 12px; line-height: 18px; font-weight: 500;">{esc(x.strip())}</span>' for x in v.split(','))
        elif kind=='mail':
            inner=''.join(f'<span style="display: block; margin-bottom: 3px;">{esc(x.strip())}</span>' for x in v.split(','))
        else: inner=esc(v)
        row+=f'<div style="{cs}">{inner}</div>'
    row+='</div>'
    body+=row
always=[("6 Ask Care Sync","Questions any time. A real person when it matters"),("29 Account and privacy","Every look at their documents or email, listed"),("Friday update","Every week, even when there is no news"),("CQC watch","Their email checked every few minutes"),("Done for you","Each finished task ticked off as it happens"),("How they feel","From calls and quick check-ins. A worried client gets a director, not an offer")]
alw=''.join(f'<div style="flex: 1 1 200px; padding: 12px 14px; border-radius: 10px; background: var(--cs-surface-raised); box-shadow: var(--cs-elevation-1); display: flex; flex-direction: column; gap: 2px;"><span style="font-size: 14px; line-height: 20px; font-weight: 500;">{esc(a)}</span><span style="font-size: 12px; line-height: 16px; color: var(--cs-text-secondary);">{esc(b)}</span></div>' for a,b in always)
page=f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>Client journey map</title>
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
<div data-cs-theme="{{{{theme}}}}" style="width: 1920px; min-height: 1180px; background: var(--cs-surface-page); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; padding: 32px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px;">
  <header style="display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; margin-bottom: 10px;">
    <div style="display: flex; flex-direction: column; gap: 4px;">
      <span style="font-size: 14px; line-height: 20px; color: var(--cs-text-brand); font-weight: 500;">Care Sync Hub, client side</span>
      <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">From the first hello to the last handover</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Ten steps for a registration client. Tender-only clients start at step 1, then go straight to their tender home (boards 48 to 50, 31 and the tender record 11). Numbers are boards on this canvas; teal rows are set once by the super admin.</span>
    </div>
    <div style="display: flex; gap: 16px; font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">
      <span style="display: flex; align-items: center; gap: 6px;"><span style="width: 14px; height: 14px; border-radius: 4px; background: var(--cs-surface-raised); box-shadow: var(--cs-elevation-1);"></span>What happens</span>
      <span style="display: flex; align-items: center; gap: 6px;"><span style="width: 14px; height: 14px; border-radius: 4px; background: var(--cs-selection-bg);"></span>Set by the super admin</span>
    </div>
  </header>
  {hdr}
  {body}
  <section aria-labelledby="alw-h" style="margin-top: 14px; display: flex; flex-direction: column; gap: 10px;">
    <h2 id="alw-h" style="margin: 0; font-size: 18px; line-height: 28px; font-weight: 500;">Always on, at every step</h2>
    <div style="display: flex; gap: 8px; flex-wrap: wrap;">{alw}</div>
  </section>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"theme":{{"editor":"enum","options":["light","dark"],"default":"light"}},"$preview":{{"width":1920,"height":1180}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{ theme: this.props.theme ?? 'light', n16: 16 }};
  }}
}}
</script>
</body>
</html>
'''
import sys
open(sys.argv[1],'w').write(page)
