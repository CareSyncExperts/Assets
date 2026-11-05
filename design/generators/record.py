import sys
def b(s,t,i=''):
    ic=f' icon="{i}"' if i else ''
    return f'<x-import component-from-global-scope="CareSync.StatusBadge" status="{s}"{ic}>{t}</x-import>'
stages=[("Found",'done'),("Bid decision",'done'),("Onboarding",'done'),("Writing",'now'),("Client review",'next'),("Submitted",'next'),("Result",'next')]
def st(n,s):
    if s=='done': dot='<span style="width: 24px; height: 24px; border-radius: 999px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"></path></svg></span>'; col='var(--cs-text-secondary)'
    elif s=='now': dot='<span style="width: 24px; height: 24px; border-radius: 999px; border: 2px solid var(--cs-action-primary); box-sizing: border-box; display: flex; align-items: center; justify-content: center;"><span style="width: 10px; height: 10px; border-radius: 999px; background: var(--cs-action-primary);"></span></span>'; col='var(--cs-text-primary)'
    else: dot='<span style="width: 24px; height: 24px; border-radius: 999px; border: 2px solid var(--cs-border-default); box-sizing: border-box;"></span>'; col='var(--cs-text-muted)'
    w='600' if s=='now' else '400'
    return f'<li style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center;">{dot}<span style="font-size: 13px; line-height: 18px; color: {col}; font-weight: {w};">{n}</span></li>'
pipe=''.join(st(n,s) for n,s in stages)
tasks=[("Onboarding meeting","Daniel and Kemi","05/11",("success","Done")),("Tender profile updated","Kemi","06/11",("success","Done")),("Evidence and case studies","Kemi","11/11",("warning","Due Wednesday")),("Clarification questions to the buyer","Daniel","13/11",("success","Sent")),("First drafts to the client","Daniel, checked by Olu","20/11",("neutral","Not yet")),("Client comments back","Kemi","24/11",("neutral","Not yet")),("Final bid and prices signed off","Kemi, e-signature","27/11",("neutral","Not yet")),("Submit on the portal and save the receipt","Daniel","27/11",("neutral","Not yet"))]
trows=''.join(f'<div style="display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 1.3fr) 70px 130px; gap: 10px; align-items: center; padding: 9px 0; border-top: 1px solid var(--cs-border-subtle); font-size: 14px; line-height: 20px;"><span style="font-weight: 500;">{a}</span><span style="color: var(--cs-text-secondary);">{o}</span><span style="color: var(--cs-text-secondary);">{d}</span><span>{b(*s)}</span></div>' for a,o,d,s in tasks)
files=[("Tender pack from the portal","12 files, saved 02/11","archive"),("Technical answers, draft 1.docx","Written in Word. Not uploaded yet","file-text"),("Social value, draft 1.docx","Written in Word. Not uploaded yet","file-text"),("Pricing schedule.xlsx","From Kemi, 06/11","file-check"),("Final submitted copy","Saved on submission","file-clock"),("Portal receipt","Saved on submission","file-clock")]
frows=''.join(f'<div style="display: flex; gap: 10px; align-items: center; padding: 9px 0; border-top: 1px solid var(--cs-border-subtle);"><x-import component-from-global-scope="CareSync.Icon" name="{i}" size="{{{{n20}}}}"></x-import><span style="flex-grow: 1; display: flex; flex-direction: column;"><span style="font-size: 14px; line-height: 20px; font-weight: 500;">{a}</span><span style="font-size: 12px; line-height: 16px; color: var(--cs-text-secondary);">{m}</span></span></div>' for a,m,i in files)
log=[("Kemi uploaded the pricing schedule","06/11"),("Buyer clarification: social value goes inside the technical upload. Kemi told","06/11"),("Bid lead added as a portal user. Three accounts done","05/11"),("Onboarding meeting held. Lot 1 only, agreed with Kemi","05/11"),("Kemi chose to bid after the Tender Radar match","02/11")]
lrows=''.join(f'<div style="display: flex; justify-content: space-between; gap: 10px; padding: 8px 0; border-top: 1px solid var(--cs-border-subtle); font-size: 14px; line-height: 20px;"><span>{a}</span><span style="color: var(--cs-text-muted); flex-shrink: 0;">{d}</span></div>' for a,d in log)
facts=[("Buyer","Northshire Council"),("Reference","NS/2026/114"),("Lots","Lot 1 North (bidding). Lot 2 South (not this time)"),("Estimated value","£1.2m a year, 4 years"),("Clarification deadline","Friday 13 November, 17:00"),("Buyer's deadline","Tuesday 1 December, 12:00"),("Our submission date","Friday 27 November, 12:00"),("Result expected","February 2027")]
facts_html=''.join(f'<div style="display: flex; flex-direction: column; padding: 8px 0; border-top: 1px solid var(--cs-border-subtle);"><span style="font-size: 12px; line-height: 16px; color: var(--cs-text-muted);">{a}</span><span style="font-size: 14px; line-height: 20px; font-weight: 500;">{v}</span></div>' for a,v in facts)
page=f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>Tender record</title>
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
.tr-card{{background:var(--cs-surface-raised);border-radius:12px;box-shadow:var(--cs-elevation-1);padding:16px 20px;display:flex;flex-direction:column}}
.tr-h{{margin:0 0 6px;font-size:17px;line-height:26px;font-weight:500}}
</style>
</helmet>
<div data-cs-theme="{{{{theme}}}}" style="min-height: 1120px; background: var(--cs-surface-page); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; display: flex; flex-wrap: wrap; align-items: stretch;">
  <div style="flex: 0 0 270px; background: var(--cs-surface-raised); border-right: 1px solid var(--cs-border-subtle);">
    <x-import component-from-global-scope="CareSync.SideNav" product="Care Sync Hub" product-sub="Care Sync Experts" label="Staff navigation" sections="{{{{nav}}}}"></x-import>
  </div>
  <div style="flex: 999 1 560px; min-width: 0; display: flex; flex-direction: column;">
    <x-import component-from-global-scope="CareSync.TopBar" title="Tender record" notifications="{{{{three}}}}" user="{{{{user}}}}"></x-import>
    <main style="padding: 24px 28px; display: flex; flex-direction: column; gap: 16px; max-width: 1280px; width: 100%; box-sizing: border-box;">
      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 12px; flex-wrap: wrap;">
        <div style="display: flex; flex-direction: column; gap: 2px;">
          <span style="font-size: 13px; line-height: 18px; color: var(--cs-text-brand); font-weight: 500;">Oakleaf Living. Tender writing</span>
          <h1 style="margin: 0; font-size: 28px; line-height: 36px; font-weight: 600;">Northshire home support framework</h1>
          <span style="font-size: 14px; line-height: 20px; color: var(--cs-text-secondary);">Bid lead Daniel, second reviewer Olu. Client decision maker Kemi. Portal inbox read daily by Kemi.</span>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          {b("warning","20 working days to our date","clock")}
          <x-import component-from-global-scope="CareSync.Button" variant="secondary" icon-start="external-link">Open the portal</x-import>
          <x-import component-from-global-scope="CareSync.Button" variant="primary" icon-start="upload">Upload a file</x-import>
        </div>
      </div>
      <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px 16px; border-radius: 12px; background: var(--cs-surface-brand); color: var(--cs-action-on-secondary);">
        <x-import component-from-global-scope="CareSync.Icon" name="info" size="{{{{n20}}}}"></x-import>
        <span style="font-size: 14px; line-height: 20px;">The bid is written in Word by the bid team and submitted on the buyer's portal. The Hub keeps the record: which tender, the dates, who does what, every file and every message with the client.</span>
      </div>
      <section aria-label="Stage" class="tr-card"><ol style="margin: 0; padding: 4px 0; list-style: none; display: flex; gap: 6px;">{pipe}</ol></section>
      <div style="display: flex; gap: 16px; flex-wrap: wrap; align-items: flex-start;">
        <div style="flex: 3 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 16px;">
          <section aria-labelledby="tk-h" class="tr-card">
            <div style="display: flex; justify-content: space-between; align-items: baseline;"><h2 id="tk-h" class="tr-h">Tasks and deadlines</h2><span style="font-size: 13px; color: var(--cs-text-secondary);">Planned back from the buyer's deadline</span></div>
            {trows}
          </section>
          <section aria-labelledby="lg-h" class="tr-card">
            <h2 id="lg-h" class="tr-h">Notes and messages</h2>
            {lrows}
          </section>
        </div>
        <div style="flex: 2 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 16px;">
          <section aria-labelledby="fc-h" class="tr-card">
            <h2 id="fc-h" class="tr-h">The tender</h2>
            {facts_html}
          </section>
          <section aria-labelledby="fl-h" class="tr-card">
            <h2 id="fl-h" class="tr-h">Files</h2>
            {frows}
          </section>
          <section aria-labelledby="oc-h" class="tr-card">
            <h2 id="oc-h" class="tr-h">Result</h2>
            <span style="font-size: 14px; line-height: 20px; color: var(--cs-text-secondary);">Recorded when the buyer decides: won or not, the score, the feedback file, and when the framework reopens.</span>
          </section>
        </div>
      </div>
    </main>
  </div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"theme":{{"editor":"enum","options":["light","dark"],"default":"light"}},"$preview":{{"width":1440,"height":1120}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{
      theme: this.props.theme ?? 'light', three: 3, n20: 20,
      user: {{ name: 'Daniel Mensah', initials: 'DM' }},
      nav: [
        {{ items: [
          {{ label: 'My day', icon: 'layout-dashboard' }},
          {{ label: 'Clients', icon: 'users' }},
          {{ label: 'Tender Radar', icon: 'search' }},
          {{ label: 'Tenders', icon: 'clipboard-list', current: true }}
        ] }},
        {{ heading: 'Manage', items: [
          {{ label: 'Templates', icon: 'file-text' }},
          {{ label: 'Reports', icon: 'trending-up' }}
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
