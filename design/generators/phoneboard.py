# Shared shell for phone-sized client boards (390 wide).
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
a{color:#0E7876}
.pb-tab{min-height:36px;padding:0 12px;border-radius:999px;font:inherit;font-size:13px;cursor:pointer}
.pb-on{border:2px solid var(--cs-action-primary);background:var(--cs-surface-raised);color:var(--cs-text-primary);font-weight:500}
.pb-off{border:1px solid var(--cs-border-default);background:transparent;color:var(--cs-text-secondary)}
.pb-tab:focus-visible,.pb-btn:focus-visible,.pb-link:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:2px}
.pb-card{background:var(--cs-surface-raised);border-radius:12px;box-shadow:var(--cs-elevation-1);overflow:hidden}
.pb-row{padding:12px 16px;display:flex;gap:12px;align-items:flex-start;border-top:1px solid var(--cs-border-subtle);font-size:14px;line-height:20px}
.pb-row:first-child{border-top:0}
.pb-h2{margin:0;font-size:18px;line-height:26px;font-weight:500}
.pb-sub{font-size:13px;line-height:18px;color:var(--cs-text-secondary)}
.pb-muted{font-size:12px;line-height:16px;color:var(--cs-text-muted)}
.pb-btn{min-height:40px;padding:0 14px;border-radius:10px;font:inherit;font-size:14px;font-weight:500;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;gap:6px;text-decoration:none;white-space:nowrap}
.pb-pri{border:0;background:var(--cs-action-primary);color:var(--cs-action-on-primary)}
.pb-sec{border:0;background:var(--cs-action-secondary);color:var(--cs-action-on-secondary)}
.pb-ghost{border:1px solid var(--cs-border-default);background:var(--cs-surface-raised);color:var(--cs-text-primary)}
.pb-dis{border:0;background:var(--cs-surface-subtle);color:var(--cs-text-muted);cursor:not-allowed}
.pb-link{border:0;background:transparent;color:var(--cs-text-brand);font:inherit;font-size:14px;font-weight:500;cursor:pointer;min-height:40px;padding:0}
.pb-chip{display:inline-flex;align-items:center;min-height:22px;padding:0 8px;border-radius:999px;font-size:12px;line-height:16px;font-weight:500;white-space:nowrap}
.c-ok{background:var(--cs-status-success-bg);color:var(--cs-status-success-text)}
.c-warn{background:var(--cs-status-warning-bg);color:var(--cs-status-warning-text)}
.c-bad{background:var(--cs-status-error-bg);color:var(--cs-status-error-text)}
.c-info{background:var(--cs-status-info-bg);color:var(--cs-status-info-text)}
.c-brand{background:var(--cs-surface-brand);color:var(--cs-text-brand)}
.c-neutral{background:var(--cs-surface-subtle);color:var(--cs-text-secondary)}
.pb-note{padding:12px 14px;border-radius:12px;font-size:13px;line-height:19px}
.n-info{background:var(--cs-status-info-bg)}
.n-ok{background:var(--cs-status-success-bg)}
.n-warn{background:var(--cs-status-warning-bg)}
.dot{width:14px;height:14px;border-radius:999px;flex-shrink:0;margin-top:3px;box-sizing:border-box}
.d-done{background:var(--cs-action-primary)}
.d-now{border:3px solid var(--cs-action-primary);background:var(--cs-surface-raised)}
.d-next{border:2px solid var(--cs-border-default);background:var(--cs-surface-raised)}
.d-ten{border:3px solid var(--cs-status-info-text);background:var(--cs-surface-raised)}
.w0{width:0}.w10{width:10%}.w20{width:20%}.w30{width:30%}.w40{width:40%}.w50{width:50%}.w60{width:60%}.w70{width:70%}.w80{width:80%}.w90{width:90%}.w100{width:100%}
__CSS__
</style>
</helmet>
<div data-cs-theme="{{theme}}" style="width: 390px; height: __H__px; position: relative; overflow: hidden; background: var(--cs-surface-page); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; box-sizing: border-box;">
__BODY__
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"theme":{"editor":"enum","options":["light","dark"],"default":"light"},"$preview":{"width":390,"height":__H__}}'>
__SCRIPT__
</script>
</body>
</html>
'''
TABS = '''  <div style="padding: 10px 12px; background: var(--cs-surface-subtle);">
    <span style="display: block; font-size: 11px; line-height: 14px; color: var(--cs-text-muted); margin-bottom: 6px;">__LABEL__</span>
    <div role="tablist" aria-label="__ARIA__" style="display: flex; flex-wrap: wrap; gap: 6px;">
      <sc-for list="{{tabs}}" as="tb" hint-placeholder-count="3">
        <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="pb-tab pb-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
        <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="pb-tab pb-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
      </sc-for>
    </div>
  </div>
'''
def tabs(label, aria):
    return TABS.replace('__LABEL__', label).replace('__ARIA__', aria)
def build(path, title, h, body, script, css=''):
    out = HEAD.replace('__TITLE__', title).replace('__H__', str(h)).replace('__BODY__', body).replace('__SCRIPT__', script).replace('__CSS__', css)
    open(path, 'w').write(out)
