import sys,html
stages=[("Onboarding",6),("Documents",9),("Writing and review",11),("Signing",3),("With CQC",7),("Interview",2),("Aftercare",14)]
mx=max(v for _,v in stages)
bars=''
for name,v in stages:
    pct=round(v/mx*100)
    bars+=f'''<div style="display: grid; grid-template-columns: 150px minmax(0, 1fr) 32px; gap: 10px; align-items: center;" title="{name}: {v} clients"><span style="font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">{name}</span><span style="height: 14px; border-radius: 0 4px 4px 0; background: var(--cs-surface-subtle); position: relative; overflow: hidden;"><span style="position: absolute; left: 0; top: 0; bottom: 0; width: {pct}%; border-radius: 0 4px 4px 0; background: var(--cs-action-primary);"></span></span><span style="font-size: 13px; line-height: 18px; font-weight: 500; text-align: right;">{v}</span></div>\n'''
table=''.join(f'<tr><td>{n}</td><td>{v}</td></tr>' for n,v in stages)
team=[("Daniel Mensah","12 clients","1 overdue","warning"),("Olu","9 clients","On track","success"),("Grace Whitfield","7 onboarding","On track","success"),("Divine","2 calls today","1 due soon","warning")]
trows=''.join(f'<div class="md-row"><span style="font-weight: 500;">{a}</span><span style="color: var(--cs-text-secondary);">{b}</span><x-import component-from-global-scope="CareSync.StatusBadge" status="{d}">{c}</x-import></div>' for a,b,c,d in team)
needs=[("triangle-alert","Notice of Proposal response for Sunrise Homecare","19 days left. Draft due Monday","error"),("users","Introduction call overdue: Meadow View Care","Paid 2 hours 40 minutes ago. Divine is on another call","warning"),("circle-alert","A worried client: Riverside Homecare","Felt rushed on Friday's call. A director call is suggested","warning"),("clock","3 clients gone quiet","No reply for 10 days or more","info")]
nrows=''.join(f'<div class="md-row" style="align-items: flex-start;"><x-import component-from-global-scope="CareSync.Icon" name="{i}" size="{{{{n20}}}}"></x-import><span style="flex-grow: 1; display: flex; flex-direction: column;"><span style="font-weight: 500;">{a}</span><span style="font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">{b}</span></span><x-import component-from-global-scope="CareSync.Button" variant="secondary" size="small">Open</x-import></div>' for i,a,b,s in needs)
page=f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>Manager dashboard</title>
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
.md-card{{background:var(--cs-surface-raised);border-radius:12px;box-shadow:var(--cs-elevation-1);padding:18px 20px;display:flex;flex-direction:column;gap:12px}}
.md-h{{margin:0;font-size:18px;line-height:28px;font-weight:500}}
.md-row{{display:flex;justify-content:space-between;align-items:center;gap:12px;font-size:14px;line-height:20px;padding:8px 0;border-top:1px solid var(--cs-border-subtle)}}
.sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
</style>
</helmet>
<div data-cs-theme="{{{{theme}}}}" style="min-height: 1100px; background: var(--cs-surface-page); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; display: flex; flex-wrap: wrap; align-items: stretch;">
  <div style="flex: 0 0 270px; background: var(--cs-surface-raised); border-right: 1px solid var(--cs-border-subtle);">
    <x-import component-from-global-scope="CareSync.SideNav" product="Care Sync Hub" product-sub="Directors" label="Manager navigation" sections="{{{{nav}}}}"></x-import>
  </div>
  <div style="flex: 999 1 560px; min-width: 0; display: flex; flex-direction: column;">
    <x-import component-from-global-scope="CareSync.TopBar" title="Manager dashboard" notifications="{{{{four}}}}" user="{{{{user}}}}"></x-import>
    <main style="padding: 28px 32px; display: flex; flex-direction: column; gap: 20px; max-width: 1280px; width: 100%; box-sizing: border-box;">
      <div style="display: flex; flex-direction: column; gap: 4px;">
        <h1 style="margin: 0; font-size: 30px; line-height: 38px; font-weight: 600;">Monday 2 November</h1>
        <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">52 active clients. Four things need a manager today; everything else is on track.</span>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 16px;">
        <x-import component-from-global-scope="CareSync.KpiCard" icon="users" label="Payment to first call" value="1h 12m" status="{{{{k1}}}}"></x-import>
        <x-import component-from-global-scope="CareSync.KpiCard" icon="shield-check" label="Submitted this month" value="4" status="{{{{k2}}}}"></x-import>
        <x-import component-from-global-scope="CareSync.KpiCard" icon="circle-check" label="Registered this month" value="2" status="{{{{k3}}}}"></x-import>
        <x-import component-from-global-scope="CareSync.KpiCard" icon="trending-up" label="Clients feeling happy" value="46 of 52" status="{{{{k4}}}}"></x-import>
      </div>
      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <div style="flex: 3 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 20px;">
          <section aria-labelledby="nd-h" class="md-card">
            <h2 id="nd-h" class="md-h">Needs a manager today</h2>
            {nrows}
          </section>
          <section aria-labelledby="st-h" class="md-card">
            <div style="display: flex; justify-content: space-between; align-items: baseline;"><h2 id="st-h" class="md-h">Active clients by stage</h2><span style="font-size: 13px; color: var(--cs-text-secondary);">52 clients</span></div>
            <div role="img" aria-label="Active clients by stage. Largest: Aftercare 14, Writing and review 11." style="display: flex; flex-direction: column; gap: 8px;">
{bars}            </div>
            <table class="sr-only"><caption>Active clients by stage</caption><tr><th>Stage</th><th>Clients</th></tr>{table}</table>
          </section>
        </div>
        <div style="flex: 2 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 20px;">
          <section aria-labelledby="fl-h" class="md-card">
            <h2 id="fl-h" class="md-h">How clients feel</h2>
            <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px;">
              <div style="padding: 12px; border-radius: 10px; background: var(--cs-status-success-bg); display: flex; flex-direction: column; gap: 2px;"><span style="display: flex; align-items: center; gap: 6px; font-size: 13px; line-height: 18px;"><x-import component-from-global-scope="CareSync.Icon" name="circle-check" size="{{{{n16}}}}"></x-import>Happy</span><span style="font-size: 24px; line-height: 32px; font-weight: 600;">46</span></div>
              <div style="padding: 12px; border-radius: 10px; background: var(--cs-status-info-bg); display: flex; flex-direction: column; gap: 2px;"><span style="display: flex; align-items: center; gap: 6px; font-size: 13px; line-height: 18px;"><x-import component-from-global-scope="CareSync.Icon" name="circle-help" size="{{{{n16}}}}"></x-import>Unsure</span><span style="font-size: 24px; line-height: 32px; font-weight: 600;">5</span></div>
              <div style="padding: 12px; border-radius: 10px; background: var(--cs-status-warning-bg); display: flex; flex-direction: column; gap: 2px;"><span style="display: flex; align-items: center; gap: 6px; font-size: 13px; line-height: 18px;"><x-import component-from-global-scope="CareSync.Icon" name="circle-alert" size="{{{{n16}}}}"></x-import>Worried</span><span style="font-size: 24px; line-height: 32px; font-weight: 600;">1</span></div>
            </div>
            <span style="font-size: 12px; line-height: 16px; color: var(--cs-text-muted);">From calls, sessions and one-tap check-ins. Worried clients get no sales messages until resolved.</span>
          </section>
          <section aria-labelledby="tm-h" class="md-card">
            <h2 id="tm-h" class="md-h">Team</h2>
            {trows}
          </section>
          <section aria-labelledby="mn-h" class="md-card">
            <h2 id="mn-h" class="md-h">Money this month</h2>
            <div class="md-row"><span>Invoices sent</span><span style="font-weight: 500;">11</span></div>
            <div class="md-row"><span>Paid on time</span><span style="font-weight: 500;">9</span></div>
            <div class="md-row"><span>Overdue, reminders running</span><span style="font-weight: 500;">2</span></div>
            <span style="font-size: 12px; line-height: 16px; color: var(--cs-text-muted);">Synced with the accounting software every hour.</span>
          </section>
        </div>
      </div>
    </main>
  </div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"theme":{{"editor":"enum","options":["light","dark"],"default":"light"}},"$preview":{{"width":1440,"height":1100}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{
      theme: this.props.theme ?? 'light', four: 4, n16: 16, n20: 20,
      user: {{ name: 'Collins', initials: 'C' }},
      k1: {{ tone: 'success', text: 'Average this month' }},
      k2: {{ tone: 'info', text: 'From the client email' }},
      k3: {{ tone: 'success', text: 'Reviews invited' }},
      k4: {{ tone: 'success', text: '1 worried, 5 unsure' }},
      nav: [
        {{ items: [
          {{ label: 'Dashboard', icon: 'layout-dashboard', current: true }},
          {{ label: 'Clients', icon: 'users' }},
          {{ label: 'Approvals', icon: 'shield-check', badge: {{ text: '2', status: 'warning' }} }},
          {{ label: 'Complaints', icon: 'circle-alert' }}
        ] }},
        {{ heading: 'Reports', items: [
          {{ label: 'Delivery', icon: 'list-checks' }},
          {{ label: 'Sales and growth', icon: 'trending-up' }},
          {{ label: 'Proof bank', icon: 'archive' }}
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
