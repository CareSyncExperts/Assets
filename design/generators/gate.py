import sys
def badge(s,t,icon=''):
    ic=f' icon="{icon}"' if icon else ''
    return f'<x-import component-from-global-scope="CareSync.StatusBadge" status="{s}"{ic}>{t}</x-import>'
cop=[("CQC registration covers the regulated activity","Personal care registered",("success","Pass"),("neutral","Not needed")),
     ("An office in the county when we submit","Office in Northshire since 2023",("success","Pass"),("success","Pass")),
     ("3 years of delivery history, as a service","2 contract examples and 1 private client",("success","Pass"),("success","Pass")),
     ("Financial standing","Accounts filed, turnover above the threshold",("success","Pass"),("success","Pass")),
     ("Insurance at the levels asked","Employer's liability £5m, asked £10m",("warning","Raise by 27/11"),("warning","Raise by 27/11")),
     ("Central Digital Platform registration and share code","Share code received 05/11",("success","Pass"),("success","Pass")),
     ("Partners or subcontractors declared","None used",("neutral","Not needed"),("neutral","Not needed"))]
rows=''.join(f'<div style="display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 1.6fr) 130px 130px; gap: 10px; align-items: center; padding: 10px 0; border-top: 1px solid var(--cs-border-subtle); font-size: 14px; line-height: 20px;"><span style="font-weight: 500;">{a}</span><span style="color: var(--cs-text-secondary);">{b}</span><span>{badge(*c)}</span><span>{badge(*d)}</span></div>' for a,b,c,d in cop)
clar=[("Social value has no separate upload slot. It goes inside the technical section","Q5 moved into the technical upload","info"),
      ("The office must exist when we submit, not after the award","Eligibility checked again: pass","success"),
      ("Complete both the online questionnaire and the Word version","Added to the return checklist","info"),
      ("Fixed hourly rates are pass or fail, not scored","Client accepted the rates on 06/11","success")]
crow=''.join(f'<div style="display: flex; gap: 10px; align-items: flex-start; padding: 10px 0; border-top: 1px solid var(--cs-border-subtle);"><x-import component-from-global-scope="CareSync.Icon" name="inbox" size="{{{{n20}}}}"></x-import><span style="flex-grow: 1; display: flex; flex-direction: column;"><span style="font-size: 14px; line-height: 20px; font-weight: 500;">{a}</span><span style="font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">What we did: {b}</span></span>{badge(s,"Handled","check")}</div>' for a,b,s in clar)
ret=[("Online selection questionnaire (PSQ) on the portal",True),("Questionnaire 1, Word version",True),("Technical questionnaire, 5 answers",False),("Social value, inside the technical upload",False),("Training matrix attachment",False),("Fixed price acceptance",True),("TUPE: buyer confirmed none applies",True),("Declarations signed by Amara",False)]
rrow=''.join(f'<div style="display: flex; gap: 10px; align-items: center; padding: 8px 0; border-top: 1px solid var(--cs-border-subtle); font-size: 14px; line-height: 20px;">'+('<span style="width: 22px; height: 22px; flex-shrink: 0; border-radius: 6px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"></path></svg></span>' if d else '<span style="width: 22px; height: 22px; flex-shrink: 0; border-radius: 6px; border: 2px solid var(--cs-border-control); box-sizing: border-box;"></span>')+f'<span>{a}</span></div>' for a,d in ret)
after=[("Submitted","Portal receipt saved and sent to the client the same day"),("Questions during evaluation","Answered within the buyer's deadline, client told each time"),("Presentation or interview","If invited: a practice session with the client first"),("Intention to award and standstill","8 working days before the contract can be signed"),("Assessment summary","Scores for every question stored and fed into the answer bank"),("Win or learn","Win: the promise register becomes the start-up checklist. Not this time: lessons, and a reminder when the framework reopens")]
arow=''.join(f'<li style="display: flex; gap: 12px; padding: 8px 0;"><span style="width: 26px; height: 26px; flex-shrink: 0; border-radius: 999px; background: var(--cs-surface-brand); color: var(--cs-text-brand); display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600;">{i+1}</span><span style="display: flex; flex-direction: column;"><span style="font-size: 14px; line-height: 20px; font-weight: 500;">{a}</span><span style="font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">{b}</span></span></li>' for i,(a,b) in enumerate(after))
page=f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>Eligibility and return</title>
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
.bg-card{{background:var(--cs-surface-raised);border-radius:12px;box-shadow:var(--cs-elevation-1);padding:16px 20px;display:flex;flex-direction:column;gap:4px}}
.bg-h{{margin:0 0 6px;font-size:17px;line-height:26px;font-weight:500}}
</style>
</helmet>
<div data-cs-theme="{{{{theme}}}}" style="min-height: 1160px; background: var(--cs-surface-page); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; display: flex; flex-wrap: wrap; align-items: stretch;">
  <div style="flex: 0 0 270px; background: var(--cs-surface-raised); border-right: 1px solid var(--cs-border-subtle);">
    <x-import component-from-global-scope="CareSync.SideNav" product="Care Sync Hub" product-sub="Care Sync Experts" label="Staff navigation" sections="{{{{nav}}}}"></x-import>
  </div>
  <div style="flex: 999 1 560px; min-width: 0; display: flex; flex-direction: column;">
    <x-import component-from-global-scope="CareSync.TopBar" title="Eligibility, clarifications and return" notifications="{{{{two}}}}" user="{{{{user}}}}"></x-import>
    <main style="padding: 24px 28px; display: flex; flex-direction: column; gap: 16px; max-width: 1280px; width: 100%; box-sizing: border-box;">
      <div style="display: flex; flex-direction: column; gap: 2px;">
        <span style="font-size: 13px; line-height: 18px; color: var(--cs-text-brand); font-weight: 500;">Oakleaf Living. Northshire home support framework</span>
        <h1 style="margin: 0; font-size: 28px; line-height: 36px; font-weight: 600;">Can we bid, has anything changed, is everything in?</h1>
      </div>
      <section aria-labelledby="cp-h" class="bg-card">
        <div style="display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 1.6fr) 130px 130px; gap: 10px; align-items: end;"><h2 id="cp-h" class="bg-h">Conditions to take part</h2><span style="font-size: 12px; color: var(--cs-text-muted); padding-bottom: 8px;">Evidence</span><span style="font-size: 12px; color: var(--cs-text-muted); padding-bottom: 8px;">Lot 1 Home care</span><span style="font-size: 12px; color: var(--cs-text-muted); padding-bottom: 8px;">Lot 2 Community support</span></div>
        {rows}
        <span style="font-size: 12px; line-height: 16px; color: var(--cs-text-muted); padding-top: 6px;">Checked at the bid decision and again after every buyer clarification. A fail stops the bid for that lot unless it can be fixed before the deadline.</span>
      </section>
      <div style="display: flex; gap: 16px; flex-wrap: wrap; align-items: flex-start;">
        <section aria-labelledby="cl-h" class="bg-card" style="flex: 3 1 480px; min-width: 0;">
          <div style="display: flex; justify-content: space-between; align-items: baseline;"><h2 id="cl-h" class="bg-h">Buyer clarifications</h2><span style="font-size: 13px; color: var(--cs-text-secondary);">19 published. 4 affect this bid. Our 2 questions answered</span></div>
          {crow}
          <span style="font-size: 12px; line-height: 16px; color: var(--cs-text-muted); padding-top: 6px;">The Hub reads every new clarification from the portal. The bid lead marks each one "affects us" or "no change", so nothing is missed.</span>
        </section>
        <section aria-labelledby="rt-h" class="bg-card" style="flex: 2 1 340px; min-width: 0;">
          <div style="display: flex; justify-content: space-between; align-items: baseline;"><h2 id="rt-h" class="bg-h">The buyer's return checklist</h2><span style="font-size: 13px; color: var(--cs-text-secondary);">4 of 8</span></div>
          {rrow}
          <span style="font-size: 12px; line-height: 16px; color: var(--cs-text-muted); padding-top: 6px;">Built from the buyer's own tender documents, plus our 8 standard checks.</span>
        </section>
      </div>
      <section aria-labelledby="af-h" class="bg-card">
        <h2 id="af-h" class="bg-h">After we submit</h2>
        <ol style="margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); column-gap: 20px;">{arow}</ol>
      </section>
    </main>
  </div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"theme":{{"editor":"enum","options":["light","dark"],"default":"light"}},"$preview":{{"width":1440,"height":1160}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{
      theme: this.props.theme ?? 'light', two: 2, n20: 20,
      user: {{ name: 'Daniel Mensah', initials: 'DM' }},
      nav: [
        {{ items: [
          {{ label: 'My day', icon: 'layout-dashboard' }},
          {{ label: 'Clients', icon: 'users' }},
          {{ label: 'Tender Radar', icon: 'search' }},
          {{ label: 'Tenders', icon: 'clipboard-list', current: true }}
        ] }},
        {{ heading: 'Manage', items: [
          {{ label: 'Evidence libraries', icon: 'archive' }},
          {{ label: 'Answer bank', icon: 'file-text' }}
        ] }}
      ]
    }};
  }}
}}
</script>
</body>
</html>
'''
open(sys.argv[1],'w').write(page)
