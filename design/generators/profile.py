import sys
S=[("1. This tender","Portal link, reference and deadline read from the portal. Authority to submit. No passwords","done"),
   ("2. Company","Names, addresses, numbers, VAT, ICO, Central Digital Platform share code","done"),
   ("3. Regulator and registration","CQC provider and location IDs, rating, conditions, activities, service types","done"),
   ("4. Who you support","Bands, ages, criteria, specialisms","done"),
   ("5. Key people","Contact, registered manager, nominated individual, directors","done"),
   ("6. Money","Turnover for 2 years, accounts, insurance and expiry dates, accountant","done"),
   ("7. Contract examples","2 of 3 added. Both referees have agreed","part"),
   ("8. Private clients","Initials only, with the family contact's permission","done"),
   ("9. Your team","Numbers, turnover, vacancies, Oliver McGowan, visas, languages, lowest hourly rate","part"),
   ("10. Partners and community","Local partners, and what you could commit to every year","part"),
   ("11. Documents and policies","9 of 11 uploaded. Missing: training matrix, business continuity plan","part"),
   ("12. Proof and stories","Figures, accreditations, praise, 4 to 6 case studies, any concerns","part"),
   ("13. Lots and capacity","Which lots, hours if you won them all, who leads the start-up","todo"),
   ("14. How you deliver","Only the settings in your lots: home care here","done"),
   ("15. Declaration","Your name, role, date and consent","todo")]
def mark(s):
    if s=='done': return '<span aria-hidden="true" style="width: 24px; height: 24px; flex-shrink: 0; border-radius: 999px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"></path></svg></span>'
    if s=='part': return '<span aria-hidden="true" style="width: 24px; height: 24px; flex-shrink: 0; border-radius: 999px; border: 2px solid var(--cs-action-primary); box-sizing: border-box; display: flex; align-items: center; justify-content: center;"><span style="width: 10px; height: 10px; border-radius: 999px; background: var(--cs-action-primary);"></span></span>'
    return '<span aria-hidden="true" style="width: 24px; height: 24px; flex-shrink: 0; border-radius: 999px; border: 2px solid var(--cs-status-warning-border); box-sizing: border-box;"></span>'
lab={'done':'Done','part':'In progress','todo':'To do'}
rows=''.join(f'<div style="padding: 12px 16px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid var(--cs-border-subtle);">{mark(s)}<span style="flex-grow: 1; display: flex; flex-direction: column; min-width: 0;"><span style="font-size: 15px; line-height: 22px; font-weight: 500;">{a}</span><span style="font-size: 12px; line-height: 16px; color: var(--cs-text-secondary);">{b}</span></span><span class="sr">{lab[s]}</span></div>' for a,b,s in S)
page=f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>Your tender profile</title>
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
a{{color:#0E7876}}
.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
</style>
</helmet>
<div data-cs-theme="{{{{theme}}}}" style="width: 390px; height: 1620px; position: relative; overflow: hidden; background: var(--cs-surface-page); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; box-sizing: border-box;">
  <div style="padding: 24px 20px 120px; display: flex; flex-direction: column; gap: 16px;">
    <header style="display: flex; flex-direction: column; gap: 4px;">
      <span style="font-size: 14px; line-height: 20px; color: var(--cs-text-secondary);">Oakleaf Living</span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">Your tender profile</h1>
      <span style="font-size: 14px; line-height: 20px; color: var(--cs-text-secondary);">Every question from our tender form, filled in once and used for every bid. Stop any time; it saves as you go. Next time we only ask what has changed.</span>
    </header>
    <section aria-label="Profile progress" style="background: var(--cs-surface-inverse); color: #FFFFFF; border-radius: 16px; padding: 18px 20px; display: flex; flex-direction: column; gap: 10px;">
      <div style="display: flex; justify-content: space-between; align-items: baseline;"><span style="font-size: 15px; line-height: 22px; font-weight: 500;">Ready for most tenders</span><span style="font-size: 26px; line-height: 34px; font-weight: 600;">82%</span></div>
      <div aria-hidden="true" style="height: 8px; border-radius: 999px; background: rgba(255,255,255,0.22); overflow: hidden;"><div style="width: 82%; height: 8px; border-radius: 999px; background: #AEFFEF;"></div></div>
      <span style="font-size: 13px; line-height: 18px; color: #D0D5DD;">Last checked 2 November. Insurance expires 31 March, we will remind you.</span>
    </section>
    <a href="#" style="display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-radius: 12px; background: var(--cs-surface-raised); box-shadow: var(--cs-elevation-2); text-decoration: none; color: var(--cs-text-primary);"><x-import component-from-global-scope="CareSync.Icon" name="history" size="{{{{n20}}}}"></x-import><span style="flex-grow: 1; display: flex; flex-direction: column;"><span style="font-size: 15px; line-height: 22px; font-weight: 500;">Carry on where you left off</span><span style="font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">Contract examples, example 3 of 3</span></span><x-import component-from-global-scope="CareSync.Icon" name="chevron-right" size="{{{{n20}}}}"></x-import></a>
    <div style="background: var(--cs-surface-raised); border-radius: 12px; box-shadow: var(--cs-elevation-1); overflow: hidden;">{rows}</div>
    <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 14px; border-radius: 12px; background: var(--cs-surface-brand); color: var(--cs-action-on-secondary);">
      <x-import component-from-global-scope="CareSync.Icon" name="info" size="{{{{n20}}}}"></x-import>
      <span style="font-size: 13px; line-height: 18px;">Missing policies? We can write or update them for you. Ask Daniel for a quote.</span>
    </div>
  </div>
  <nav aria-label="Main" style="position: absolute; left: 0; right: 0; bottom: 0; height: 84px; padding: 8px 8px 20px; box-sizing: border-box; background: var(--cs-surface-raised); border-top: 1px solid var(--cs-border-subtle); display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));">
    <a href="Tenders.dc.html" style="display: flex; flex-direction: column; align-items: center; gap: 2px; text-decoration: none; color: var(--cs-text-secondary); font-size: 12px; line-height: 16px;"><x-import component-from-global-scope="CareSync.Icon" name="layout-dashboard" size="{{{{n24}}}}"></x-import>Today</a>
    <a href="TenderProfile.dc.html" aria-current="page" style="display: flex; flex-direction: column; align-items: center; gap: 2px; text-decoration: none; color: var(--cs-text-brand); font-size: 12px; line-height: 16px; font-weight: 500;"><x-import component-from-global-scope="CareSync.Icon" name="user" size="{{{{n24}}}}"></x-import>Profile</a>
    <a href="DocRoom.dc.html" style="display: flex; flex-direction: column; align-items: center; gap: 2px; text-decoration: none; color: var(--cs-text-secondary); font-size: 12px; line-height: 16px;"><x-import component-from-global-scope="CareSync.Icon" name="file-check" size="{{{{n24}}}}"></x-import>Documents</a>
    <a href="Ask.dc.html" style="display: flex; flex-direction: column; align-items: center; gap: 2px; text-decoration: none; color: var(--cs-text-secondary); font-size: 12px; line-height: 16px;"><x-import component-from-global-scope="CareSync.Icon" name="circle-help" size="{{{{n24}}}}"></x-import>Ask</a>
  </nav>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"theme":{{"editor":"enum","options":["light","dark"],"default":"light"}},"$preview":{{"width":390,"height":1620}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{ theme: this.props.theme ?? 'light', n20: 20, n24: 24 }}; }}
}}
</script>
</body>
</html>
'''
open(sys.argv[1],'w').write(page)
