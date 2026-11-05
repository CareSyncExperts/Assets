# Generic smart form board generator. Usage: build(path, title, formName, who, h, sectionsJs, initAnswers, resumeId, sentText)
HTML = r'''<!doctype html>
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
.of-in{min-height:44px;padding:0 12px;border-radius:10px;border:1px solid var(--cs-border-control);font:inherit;font-size:15px;background:var(--cs-surface-raised);color:var(--cs-text-primary);box-sizing:border-box;width:100%}
.of-ta{min-height:76px;padding:10px 12px;border-radius:10px;border:1px solid var(--cs-border-control);font:inherit;font-size:15px;background:var(--cs-surface-raised);color:var(--cs-text-primary);box-sizing:border-box;width:100%;resize:vertical}
.of-l{font-size:14px;line-height:20px;font-weight:500}
.of-f{display:flex;flex-direction:column;gap:6px;padding:12px 14px;border-radius:12px;background:var(--cs-surface-raised);box-shadow:var(--cs-elevation-1)}
.of-opt{display:flex;align-items:center;gap:10px;min-height:40px;padding:6px 12px;border-radius:10px;font:inherit;font-size:14px;line-height:19px;text-align:left;cursor:pointer;width:100%;box-sizing:border-box}
.of-opt:focus-visible,.of-btn:focus-visible,.of-link:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:2px}
.of-on{border:2px solid var(--cs-action-primary);background:var(--cs-selection-bg);color:var(--cs-text-primary);font-weight:500}
.of-off{border:1px solid var(--cs-border-default);background:var(--cs-surface-raised);color:var(--cs-text-primary)}
.of-btn{min-height:50px;border-radius:12px;font:inherit;font-size:16px;font-weight:500;cursor:pointer}
.of-link{min-height:40px;border:0;background:transparent;color:var(--cs-text-brand);font:inherit;font-size:14px;font-weight:500;cursor:pointer}
.of-hint{font-size:12px;line-height:16px;color:var(--cs-text-secondary)}
.of-ok{font-size:12px;line-height:16px;color:var(--cs-status-success-text)}
.of-req{color:var(--cs-status-error-text)}
.of-box{min-height:64px;border-radius:10px;border:1px dashed var(--cs-border-control);display:flex;align-items:center;justify-content:center;font-size:14px;color:var(--cs-text-secondary)}
.of-info{padding:12px 14px;border-radius:12px;font-size:13px;line-height:19px;white-space:pre-line}
.tone-info{background:var(--cs-status-info-bg)}
.tone-ok{background:var(--cs-status-success-bg)}
.tone-warn{background:var(--cs-status-warning-bg)}
.w0{width:0}.w10{width:10%}.w20{width:20%}.w30{width:30%}.w40{width:40%}.w50{width:50%}.w60{width:60%}.w70{width:70%}.w80{width:80%}.w90{width:90%}.w100{width:100%}
</style>
</helmet>
<div data-cs-theme="{{theme}}" style="width: 390px; height: __H__px; position: relative; overflow: hidden; background: var(--cs-surface-page); color: var(--cs-text-primary); font-family: Kanit, sans-serif; letter-spacing: -0.408px; box-sizing: border-box;">

  <sc-if value="{{isWelcome}}" hint-placeholder-val="{{ false }}">
    <div style="padding: 48px 24px 40px; display: flex; flex-direction: column; gap: 16px;">
      <span aria-hidden="true" style="width: 56px; height: 56px; border-radius: 999px; background: var(--cs-surface-brand); color: var(--cs-text-brand); display: flex; align-items: center; justify-content: center;"><x-import component-from-global-scope="CareSync.Icon" name="history" size="{{n24}}"></x-import></span>
      <span style="font-size: 13px; line-height: 18px; color: var(--cs-text-brand); font-weight: 500;">__FORM__</span>
      <h1 style="margin: 0; font-size: 26px; line-height: 34px; font-weight: 600;">Welcome back, __WHO__</h1>
      <span style="font-size: 16px; line-height: 24px; color: var(--cs-text-secondary);">You stopped at "{{resumeTitle}}". Everything before it is saved, and pages that do not apply to you are skipped.</span>
      <div style="display: flex; flex-direction: column; gap: 8px; padding: 14px 16px; border-radius: 12px; background: var(--cs-surface-raised); box-shadow: var(--cs-elevation-1);">
        <sc-for list="{{doneTitles}}" as="d" hint-placeholder-count="6">
          <span style="display: flex; gap: 10px; align-items: center; font-size: 14px; line-height: 20px; color: var(--cs-text-secondary);"><x-import component-from-global-scope="CareSync.Icon" name="circle-check" size="{{n16}}"></x-import>{{d}}</span>
        </sc-for>
      </div>
      <button class="of-btn" onClick="{{resume}}" style="border: 0; background: var(--cs-action-primary); color: var(--cs-action-on-primary);">Carry on where I stopped</button>
      <button class="of-link" onClick="{{fromStart}}">Go to the first page and check my answers</button>
    </div>
  </sc-if>

  <sc-if value="{{isPaused}}" hint-placeholder-val="{{ false }}">
    <div style="padding: 64px 24px 40px; display: flex; flex-direction: column; gap: 16px; align-items: center; text-align: center;">
      <span aria-hidden="true" style="width: 64px; height: 64px; border-radius: 999px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center;"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"></path></svg></span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">Saved. Come back any time</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">You will pick up at "{{secTitle}}" on any phone or computer. If it is still waiting, we send a gentle reminder after 2 days and again after 4, outside quiet hours, and Grace calls you on day 6.</span>
      <button class="of-link" onClick="{{unpause}}">Carry on now instead</button>
    </div>
  </sc-if>

  <sc-if value="{{isSent}}" hint-placeholder-val="{{ false }}">
    <div style="padding: 64px 24px 40px; display: flex; flex-direction: column; gap: 16px; align-items: center; text-align: center;">
      <span aria-hidden="true" style="width: 64px; height: 64px; border-radius: 999px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center;"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"></path></svg></span>
      <h1 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600;">Thank you. We have your answers</h1>
      <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">__SENT__</span>
      <button class="of-link" onClick="{{restart}}">See it again (demo)</button>
    </div>
  </sc-if>

  <sc-if value="{{inForm}}" hint-placeholder-val="{{ true }}">
    <header style="background: var(--cs-surface-raised); border-bottom: 1px solid var(--cs-border-subtle); padding: 14px 20px 12px; display: flex; flex-direction: column; gap: 8px;">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="font-size: 13px; line-height: 18px; color: var(--cs-text-secondary);">__FORM__</span>
        <span role="status" style="display: flex; align-items: center; gap: 4px; font-size: 12px; line-height: 16px; color: var(--cs-status-success-text);"><x-import component-from-global-scope="CareSync.Icon" name="check" size="{{n16}}"></x-import>Saved</span>
      </div>
      <div aria-hidden="true" style="height: 6px; border-radius: 999px; background: var(--cs-surface-subtle); overflow: hidden;"><div class="{{barCls}}" style="height: 6px; border-radius: 999px; background: var(--cs-action-primary);"></div></div>
      <span style="font-size: 12px; line-height: 16px; color: var(--cs-text-brand); font-weight: 500;">Page {{secNo}} of {{secTotal}}. About {{mins}}{{skipNote}}</span>
      <h1 style="margin: 0; font-size: 21px; line-height: 28px; font-weight: 600;">{{secTitle}}</h1>
      <span class="of-hint">{{secIntro}}</span>
    </header>

    <main style="padding: 16px 16px 170px; display: flex; flex-direction: column; gap: 10px;">
      <sc-for list="{{fields}}" as="f" hint-placeholder-count="6">
        <div>
          <sc-if value="{{f.isInfo}}" hint-placeholder-val="{{ false }}"><div class="{{f.tone}}">{{f.label}}</div></sc-if>
          <sc-if value="{{f.isJump}}" hint-placeholder-val="{{ false }}"><button class="of-opt of-off" onClick="{{f.go}}" style="justify-content: space-between;"><span style="display: flex; align-items: center; gap: 10px;"><span aria-hidden="true" style="color: var(--cs-status-success-text);">✓</span>{{f.label}}</span><span style="color: var(--cs-text-brand); font-weight: 500;">Change</span></button></sc-if>
          <sc-if value="{{f.isField}}" hint-placeholder-val="{{ true }}">
            <div class="of-f">
              <span class="of-l">{{f.label}}<sc-if value="{{f.req}}" hint-placeholder-val="{{ false }}"><span class="of-req"> *</span></sc-if></span>
              <sc-if value="{{f.hasTip}}" hint-placeholder-val="{{ false }}"><span class="of-hint">{{f.tip}}</span></sc-if>
              <sc-if value="{{f.isText}}" hint-placeholder-val="{{ true }}"><input class="of-in" aria-label="{{f.label}}" value="{{f.value}}" placeholder="{{f.ph}}"></sc-if>
              <sc-if value="{{f.isPara}}" hint-placeholder-val="{{ false }}"><textarea class="of-ta" aria-label="{{f.label}}" placeholder="{{f.ph}}" value="{{f.value}}"></textarea></sc-if>
              <sc-if value="{{f.isChoice}}" hint-placeholder-val="{{ false }}">
                <div role="radiogroup" aria-label="{{f.label}}" style="display: flex; flex-direction: column; gap: 6px;">
                  <sc-for list="{{f.opts}}" as="o" hint-placeholder-count="2">
                    <sc-if value="{{o.on}}" hint-placeholder-val="{{ false }}"><button class="of-opt of-on" role="radio" aria-checked="true" onClick="{{o.pick}}"><span aria-hidden="true" style="width: 18px; height: 18px; flex-shrink: 0; border-radius: 999px; border: 5px solid var(--cs-action-primary); box-sizing: border-box;"></span>{{o.label}}</button></sc-if>
                    <sc-if value="{{o.off}}" hint-placeholder-val="{{ true }}"><button class="of-opt of-off" role="radio" aria-checked="false" onClick="{{o.pick}}"><span aria-hidden="true" style="width: 18px; height: 18px; flex-shrink: 0; border-radius: 999px; border: 2px solid var(--cs-border-control); box-sizing: border-box;"></span>{{o.label}}</button></sc-if>
                  </sc-for>
                </div>
              </sc-if>
              <sc-if value="{{f.isMulti}}" hint-placeholder-val="{{ false }}">
                <div role="group" aria-label="{{f.label}}" style="display: flex; flex-direction: column; gap: 6px;">
                  <sc-for list="{{f.opts}}" as="o" hint-placeholder-count="3">
                    <sc-if value="{{o.on}}" hint-placeholder-val="{{ false }}"><button class="of-opt of-on" role="checkbox" aria-checked="true" onClick="{{o.pick}}"><span aria-hidden="true" style="width: 18px; height: 18px; flex-shrink: 0; border-radius: 4px; background: var(--cs-action-primary); color: var(--cs-action-on-primary); display: flex; align-items: center; justify-content: center; font-size: 12px;">✓</span>{{o.label}}</button></sc-if>
                    <sc-if value="{{o.off}}" hint-placeholder-val="{{ true }}"><button class="of-opt of-off" role="checkbox" aria-checked="false" onClick="{{o.pick}}"><span aria-hidden="true" style="width: 18px; height: 18px; flex-shrink: 0; border-radius: 4px; border: 2px solid var(--cs-border-control); box-sizing: border-box;"></span>{{o.label}}</button></sc-if>
                  </sc-for>
                </div>
              </sc-if>
              <sc-if value="{{f.isFile}}" hint-placeholder-val="{{ false }}"><span class="of-box">{{f.value}}</span></sc-if>
              <sc-if value="{{f.isSign}}" hint-placeholder-val="{{ false }}"><span class="of-box" style="font-family: cursive; font-size: 22px; color: var(--cs-text-primary);">{{f.value}}</span></sc-if>
              <sc-if value="{{f.hasOk}}" hint-placeholder-val="{{ false }}"><span class="of-ok">{{f.ok}}</span></sc-if>
              <button class="of-link" onClick="{{f.ask}}" style="min-height: 32px; font-size: 13px; align-self: flex-start; padding: 0;">{{f.askLabel}}</button>
            </div>
          </sc-if>
        </div>
      </sc-for>
    </main>

    <footer style="position: absolute; left: 0; right: 0; bottom: 0; padding: 12px 20px 20px; background: var(--cs-surface-raised); border-top: 1px solid var(--cs-border-subtle); display: flex; flex-direction: column; gap: 4px;">
      <div style="display: flex; gap: 10px;">
        <button class="of-btn" onClick="{{prev}}" style="flex: 0 0 96px; border: 1px solid var(--cs-border-control); background: var(--cs-surface-raised); color: var(--cs-text-primary); font-size: 15px;">Back</button>
        <button class="of-btn" onClick="{{next}}" style="flex: 1 1 auto; border: 0; background: var(--cs-action-primary); color: var(--cs-action-on-primary);">{{nextLabel}}</button>
      </div>
      <button class="of-link" onClick="{{pause}}">Save and finish later</button>
    </footer>
  </sc-if>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"theme":{"editor":"enum","options":["light","dark"],"default":"light"},"$preview":{"width":390,"height":__H__}}'>
class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { i: -1, paused: false, sent: false, a: __INIT__ };
  }
  renderVals() {
    const st = this.state, A = st.a;
    const set = (k, v) => this.setState({ a: Object.assign({}, A, { [k]: v }) });
    const tog = (k, j) => { const cur = (A[k] || []).slice(); const p = cur.indexOf(j); if (p >= 0) cur.splice(p, 1); else cur.push(j); set(k, cur); };
    const T = (label, value, o) => Object.assign({ kind: 'text', label, value: value || '', req: false }, o || {});
    const P = (label, value, o) => Object.assign({ kind: 'para', label, value: value || '', req: false }, o || {});
    const C = (label, key, opts, o) => Object.assign({ kind: 'choice', label, key, opts, req: true }, o || {});
    const M = (label, key, opts, o) => Object.assign({ kind: 'multi', label, key, opts, req: false }, o || {});
    const F = (label, value, o) => Object.assign({ kind: 'file', label, value: value || 'Add file', req: false }, o || {});
    const SG = (label, value, o) => Object.assign({ kind: 'sign', label, value: value || '', req: false }, o || {});
    const I = (text, tone) => ({ kind: 'info', label: text, tone: 'of-info tone-' + (tone || 'info') });
    const S = [];
    const skipped = [];
    let skipWord = 'not needed for you';
__SECTIONS__
    const lastPage = S.pop();
    S.push({ id: 'review', title: 'Check your answers', intro: 'Every page you have filled in. Tap any page to change it, then go on to the last page.', fields: [I((skipped.length ? skipped.length + (skipped.length === 1 ? ' page is ' : ' pages are ') + skipWord + ', so they are not shown. ' : '') + 'Nothing is sent until you press Send on the last page.', 'ok')].concat(S.map((x, k) => ({ kind: 'jump', label: x.title, to: k }))) });
    S.push(lastPage);
    const n = S.length;
    const i = Math.min(Math.max(st.i, 0), n - 1);
    const cur = S[i];
    const clean = t => (t || '').replace(/^Added by the Hub[.:]?\s*/, '');
    const fields = cur.fields.map(f => {
      const tip = clean(f.tip);
      const b = { label: f.label, req: !!f.req, value: f.value || '', ph: f.ph || '', tip, hasTip: !!tip, ok: f.ok || '', hasOk: !!f.ok,
        tone: f.tone || '', isInfo: f.kind === 'info', isField: f.kind !== 'info' && f.kind !== 'jump',
        isJump: f.kind === 'jump', go: () => this.setState({ i: f.to || 0 }),
        askLabel: st.asked === f.label ? 'Sent. Grace replies here within ' + ((window.CSR && CSR.get('reply-client', '1 working day')) || '1 working day') : 'Not sure? Ask us', ask: () => this.setState({ asked: f.label }), isText: f.kind === 'text', isPara: f.kind === 'para', isChoice: f.kind === 'choice', isMulti: f.kind === 'multi', isFile: f.kind === 'file', isSign: f.kind === 'sign', opts: [] };
      if (f.kind === 'choice') { const v = A[f.key] !== undefined ? A[f.key] : null; b.opts = f.opts.map(([k, label]) => ({ label, on: v === k, off: v !== k, pick: () => set(f.key, k) })); }
      if (f.kind === 'multi') { const v = A[f.key] || []; b.opts = f.opts.map((label, j) => ({ label, on: v.includes(j), off: !v.includes(j), pick: () => tog(f.key, j) })); }
      return b;
    });
    const ri = Math.max(0, S.findIndex(x => x.id === '__RESUME__'));
    const pct = Math.round(((i + 1) / n) * 10) * 10;
    const nf = cur.fields.filter(f => f.kind !== 'info' && f.kind !== 'jump').length;
    const mm = Math.max(1, Math.round(nf * 0.4));
    return {
      theme: this.props.theme ?? 'light', n16: 16, n24: 24,
      isWelcome: st.i === -1 && !st.paused && !st.sent, isPaused: st.paused, isSent: st.sent, inForm: st.i >= 0 && !st.paused && !st.sent,
      resumeTitle: S[ri].title, doneTitles: S.slice(0, ri).map(x => x.title),
      secNo: String(i + 1), secTotal: String(n), skipNote: skipped.length ? '. ' + skipped.length + (skipped.length === 1 ? ' page ' : ' pages ') + skipWord : '',
      mins: mm === 1 ? '1 minute' : mm + ' minutes', secTitle: cur.title, secIntro: clean(cur.intro), barCls: 'w' + pct, fields,
      nextLabel: i === n - 1 ? 'Send to Care Sync' : 'Next',
      resume: () => this.setState({ i: ri }), fromStart: () => this.setState({ i: 0 }),
      next: () => (i === n - 1 ? this.setState({ sent: true }) : this.setState({ i: i + 1 })),
      prev: () => this.setState({ i: i === 0 ? -1 : i - 1 }),
      pause: () => this.setState({ paused: true }), unpause: () => this.setState({ paused: false }),
      restart: () => this.setState({ i: -1, sent: false, paused: false })
    };
  }
}
</script>
</body>
</html>
'''
def build(path, title, form, who, h, sections_js, init, resume, sent):
    t = HTML.replace('__TITLE__', title).replace('__FORM__', form).replace('__WHO__', who).replace('__H__', str(h)) \
        .replace('__SECTIONS__', sections_js).replace('__INIT__', init).replace('__RESUME__', resume).replace('__SENT__', sent)
    open(path, 'w').write(t)
