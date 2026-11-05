# Shared shell for staff boards (1440 wide) with side navigation and top bar.
HEAD = '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>__TITLE__</title>
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
:root{--font-sans:Kanit, sans-serif}
body{margin:0}
.sb-card{background:var(--cs-surface-raised);border-radius:12px;box-shadow:var(--cs-elevation-1);overflow:hidden}
.sb-h2{margin:0;font-size:18px;line-height:26px;font-weight:500}
.sb-sub{font-size:13px;line-height:18px;color:var(--cs-text-secondary)}
.sb-muted{font-size:12px;line-height:16px;color:var(--cs-text-muted)}
.sb-row{padding:12px 20px;display:flex;gap:14px;align-items:center;border-top:1px solid var(--cs-border-subtle);font-size:14px;line-height:20px}
.sb-head{padding:18px 20px 10px;display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
.sb-chip{display:inline-flex;align-items:center;min-height:22px;padding:0 8px;border-radius:999px;font-size:12px;line-height:16px;font-weight:500;white-space:nowrap}
.c-ok{background:var(--cs-status-success-bg);color:var(--cs-status-success-text)}
.c-warn{background:var(--cs-status-warning-bg);color:var(--cs-status-warning-text)}
.c-bad{background:var(--cs-status-error-bg);color:var(--cs-status-error-text)}
.c-info{background:var(--cs-status-info-bg);color:var(--cs-status-info-text)}
.c-neutral{background:var(--cs-surface-subtle);color:var(--cs-text-secondary)}
.c-brand{background:var(--cs-surface-brand);color:var(--cs-text-brand)}
.sb-tab{min-height:36px;padding:0 14px;border-radius:999px;font:inherit;font-size:13px;cursor:pointer}
.t-on{border:2px solid var(--cs-action-primary);background:var(--cs-surface-raised);color:var(--cs-text-primary);font-weight:500}
.t-off{border:1px solid var(--cs-border-default);background:transparent;color:var(--cs-text-secondary)}
.sb-btn{min-height:36px;padding:0 12px;border-radius:10px;font:inherit;font-size:13px;font-weight:500;cursor:pointer;white-space:nowrap}
.b-pri{border:0;background:var(--cs-action-primary);color:var(--cs-action-on-primary)}
.b-sec{border:0;background:var(--cs-action-secondary);color:var(--cs-action-on-secondary)}
.b-gh{border:1px solid var(--cs-border-default);background:var(--cs-surface-raised);color:var(--cs-text-primary)}
.sb-tab:focus-visible,.sb-btn:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:2px}
.sb-th{font-size:12px;line-height:16px;color:var(--cs-text-muted);font-weight:500}
.sb-kpi{padding:16px 18px;display:flex;flex-direction:column;gap:2px}
.sb-kv{font-size:26px;line-height:34px;font-weight:600}
.bar{height:8px;border-radius:999px;background:var(--cs-surface-subtle);overflow:hidden}
.bar span{display:block;height:8px;border-radius:999px;background:var(--cs-action-primary)}
.w0{width:0}.w5{width:5%}.w10{width:10%}.w15{width:15%}.w20{width:20%}.w25{width:25%}.w30{width:30%}.w35{width:35%}.w40{width:40%}.w45{width:45%}.w50{width:50%}.w55{width:55%}.w60{width:60%}.w65{width:65%}.w70{width:70%}.w75{width:75%}.w80{width:80%}.w85{width:85%}.w90{width:90%}.w95{width:95%}.w100{width:100%}
__CSS__
</style>
</helmet>
<div data-cs-theme="{{theme}}" style="min-height: __H__px; background: var(--cs-surface-page); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; display: flex; flex-wrap: wrap; align-items: stretch;">
  <div style="flex: 0 0 270px; background: var(--cs-surface-raised); border-right: 1px solid var(--cs-border-subtle);">
    <x-import component-from-global-scope="CareSync.SideNav" product="Care Sync Hub" product-sub="Care Sync Experts" label="Staff navigation" sections="{{nav}}"></x-import>
  </div>
  <div style="flex: 999 1 560px; min-width: 0; display: flex; flex-direction: column;">
    <x-import component-from-global-scope="CareSync.TopBar" title="__TOP__" notifications="{{three}}" user="{{user}}"></x-import>
    <main style="padding: 28px 32px; display: flex; flex-direction: column; gap: 18px; max-width: 1280px; width: 100%; box-sizing: border-box;">
__BODY__
    </main>
  </div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"theme":{"editor":"enum","options":["light","dark"],"default":"light"},"$preview":{"width":1440,"height":__H__}}'>
__SCRIPT__
</script>
</body>
</html>
'''
NAV = """[{ items: [
  { label: 'My day', icon: 'layout-dashboard'__C_day__ },
  { label: 'Clients', icon: 'users'__C_clients__ },
  { label: 'Onboarding', icon: 'list-checks'__C_onboarding__ },
  { label: 'Questions', icon: 'inbox', badge: { text: '5', status: 'warning' }__C_questions__ },
  { label: 'Deadlines', icon: 'clock'__C_deadlines__ },
  { label: 'Sessions', icon: 'calendar'__C_sessions__ },
  { label: 'Client care', icon: 'user'__C_care__ },
  { label: 'Aftercare', icon: 'shield-check'__C_after__ },
  { label: 'Regulator and tender watch', icon: 'eye'__C_watch__ },
  { label: 'Tenders', icon: 'clipboard-list'__C_tenders__ }
] }, { heading: 'Manage', items: [
  { label: 'Manager dashboard', icon: 'building-2'__C_manager__ },
  { label: 'Team and cover', icon: 'users'__C_team__ },
  { label: 'Reports', icon: 'trending-up'__C_reports__ },
  { label: 'Super admin', icon: 'settings'__C_admin__ }
] }]"""
def nav(current):
    n = NAV
    for k in ['day', 'clients', 'onboarding', 'questions', 'deadlines', 'sessions', 'care', 'after', 'watch', 'tenders', 'manager', 'team', 'reports', 'admin']:
        n = n.replace('__C_' + k + '__', ', current: true' if k == current else '')
    return n
def build(path, title, top, h, body, script, current, css=''):
    script = script.replace('__NAV__', nav(current))
    out = HEAD.replace('__TITLE__', title).replace('__TOP__', top).replace('__H__', str(h)).replace('__BODY__', body).replace('__SCRIPT__', script).replace('__CSS__', css)
    open(path, 'w').write(out)

# Super admin console: its own menu, with a way back to the Hub.
SANAV = """[{ items: [
  { label: 'Back to the Hub', icon: 'chevron-left' }
] }, { heading: 'Super admin', items: [
  { label: 'Home', icon: 'layout-dashboard'__S_home__, badge: { text: '7', status: 'warning' } },
  { label: 'Go-live readiness', icon: 'list-checks'__S_golive__ },
  { label: 'Rules and promises', icon: 'clock'__S_rules__ },
  { label: 'Packages and journeys', icon: 'clipboard-list'__S_packages__ },
  { label: 'Price book', icon: 'file-check'__S_prices__ },
  { label: 'Forms', icon: 'pencil-line'__S_forms__ },
  { label: 'Messages and automations', icon: 'inbox'__S_messages__ },
  { label: 'People and access', icon: 'users'__S_people__ },
  { label: 'Security', icon: 'shield-alert'__S_security__ },
  { label: 'Data and privacy', icon: 'lock'__S_privacy__ },
  { label: 'System health', icon: 'refresh-cw'__S_health__ },
  { label: 'Money and exports', icon: 'download'__S_money__ },
  { label: 'View as', icon: 'eye'__S_viewas__ },
  { label: 'How it fits together', icon: 'git-compare'__S_map__ }
] }]"""
SAKEYS = ['home', 'golive', 'rules', 'packages', 'prices', 'forms', 'messages', 'people', 'security', 'privacy', 'health', 'money', 'viewas', 'map']
def sanav(current):
    n = SANAV
    for k in SAKEYS:
        n = n.replace('__S_' + k + '__', ', current: true' if k == current else '')
    return n
def build_sa(path, title, top, h, body, script, current, css=''):
    """Same shell as build(), with the super admin menu. Put nav: __NAV__ in renderVals."""
    script = script.replace('__NAV__', sanav(current))
    out = HEAD.replace('product="Care Sync Hub" product-sub="Care Sync Experts"', 'product="Care Sync Hub" product-sub="Super admin"').replace('__TITLE__', title).replace('__TOP__', top).replace('__H__', str(h)).replace('__BODY__', body).replace('__SCRIPT__', script).replace('__CSS__', css)
    open(path, 'w').write(out)
