import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Assets/6db558a7-551f-58f7-827c-5570646704f4/scratchpad/gen')
from staffboard import build
OUT = sys.argv[1]

TABS = '''      <div role="tablist" aria-label="__LABEL__" style="display: flex; gap: 6px; flex-wrap: wrap;">
        <sc-for list="{{__LIST__}}" as="tb" hint-placeholder-count="3">
          <sc-if value="{{tb.on}}" hint-placeholder-val="{{ false }}"><button class="sb-tab t-on" role="tab" aria-selected="true" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
          <sc-if value="{{tb.off}}" hint-placeholder-val="{{ true }}"><button class="sb-tab t-off" role="tab" aria-selected="false" onClick="{{tb.pick}}">{{tb.label}}</button></sc-if>
        </sc-for>
      </div>
'''
def tabs(lst, label):
    return TABS.replace('__LIST__', lst).replace('__LABEL__', label)

# A. Deadlines: regulator and tender deadline calendar
CSS_A = '''
.dl-date{width:64px;flex-shrink:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:6px 0;border-radius:10px;background:var(--cs-surface-page)}
.dl-d{font-size:22px;line-height:26px;font-weight:600}
.dl-grp{padding:12px 20px 6px;border-top:1px solid var(--cs-border-subtle);font-size:13px;line-height:18px;font-weight:600;color:var(--cs-text-secondary);display:flex;justify-content:space-between}
.dl-when{display:flex;flex-direction:column;gap:4px;width:250px;flex-shrink:0}
.dl-line{display:flex;justify-content:space-between;gap:8px;font-size:13px;line-height:18px}
.cal{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px;padding:0 20px 16px}
.cal-h{font-size:12px;line-height:16px;color:var(--cs-text-muted);font-weight:500;padding:4px 6px}
.cal-c{min-height:78px;border-radius:10px;padding:6px 8px;display:flex;flex-direction:column;gap:6px;align-items:flex-start;font:inherit;text-align:left;cursor:pointer;color:var(--cs-text-primary)}
.cc-off{border:1px solid var(--cs-border-subtle);background:var(--cs-surface-page)}
.cc-on{border:2px solid var(--cs-action-primary);background:var(--cs-surface-raised)}
.cc-blank{border:0;background:transparent;cursor:default}
.cal-c:focus-visible{outline:2px solid var(--cs-border-focus);outline-offset:2px}
.cal-n{font-size:14px;line-height:18px;font-weight:500}
.dots{display:flex;gap:4px;flex-wrap:wrap}
.dot{width:10px;height:10px;border-radius:999px;display:inline-block}
.d-legal{background:var(--cs-status-error-text)}
.d-reg{background:var(--cs-status-info-text)}
.d-tender{background:var(--cs-text-brand)}
.d-exp{background:var(--cs-status-warning-text)}
.d-after{background:var(--cs-text-muted)}
.lg{display:inline-flex;align-items:center;gap:6px;font-size:12px;line-height:16px;color:var(--cs-text-secondary)}
'''

BODY_A = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Deadlines</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">Every regulator and tender date across all clients. Days left are counted from today, Monday 2 November.</span>
        </div>
''' + tabs('views', 'View') + '''      </div>
      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px;">
''' + tabs('filters', 'Show') + '''        <span class="sb-sub">{{summary}}</span>
      </div>

      <sc-if value="{{isList}}" hint-placeholder-val="{{ true }}">
        <section class="sb-card" aria-label="Deadlines by date">
          <sc-for list="{{groups}}" as="g" hint-placeholder-count="3">
            <div class="dl-grp"><span>{{g.label}}</span><span>{{g.count}}</span></div>
            <sc-for list="{{g.rows}}" as="r" hint-placeholder-count="3">
              <div class="sb-row" style="align-items: flex-start;">
                <span class="dl-date"><span class="sb-muted">{{r.dow}}</span><span class="dl-d">{{r.day}}</span><span class="sb-muted">{{r.mon}}</span></span>
                <span style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 3px;">
                  <span style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><span style="font-weight: 500;">{{r.title}}</span><span class="{{r.typeCls}}">{{r.type}}</span></span>
                  <span class="sb-sub"><span style="font-weight: 500; color: var(--cs-text-primary);">{{r.client}}</span>. Owner: {{r.owner}}</span>
                  <span class="sb-muted">{{r.note}}</span>
                </span>
                <span class="dl-when">
                  <sc-for list="{{r.dates}}" as="d" hint-placeholder-count="2">
                    <span class="dl-line"><span><span class="sb-muted">{{d.k}}</span><br><span style="font-weight: 500;">{{d.v}}</span></span><span class="{{d.cls}}">{{d.left}}</span></span>
                  </sc-for>
                </span>
                <button class="sb-btn b-gh" style="width: 128px; flex-shrink: 0;">{{r.cta}}</button>
              </div>
            </sc-for>
          </sc-for>
        </section>
      </sc-if>

      <sc-if value="{{isMonth}}" hint-placeholder-val="{{ false }}">
        <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
          <section class="sb-card" style="flex: 3 1 600px; min-width: 0;" aria-labelledby="m-h">
            <div class="sb-head"><h2 id="m-h" class="sb-h2">November 2026</h2>
              <span style="display: flex; gap: 12px; flex-wrap: wrap;"><span class="lg"><span class="dot d-legal"></span>Legal</span><span class="lg"><span class="dot d-reg"></span>Regulator</span><span class="lg"><span class="dot d-tender"></span>Tender</span><span class="lg"><span class="dot d-exp"></span>Expiry</span><span class="lg"><span class="dot d-after"></span>Aftercare</span></span>
            </div>
            <div class="cal">
              <sc-for list="{{dow}}" as="w" hint-placeholder-count="7"><span class="cal-h">{{w.k}}</span></sc-for>
              <sc-for list="{{cells}}" as="c" hint-placeholder-count="35">
                <sc-if value="{{c.real}}" hint-placeholder-val="{{ true }}">
                  <button class="{{c.cls}}" onClick="{{c.pick}}" aria-pressed="{{c.pressed}}" aria-label="{{c.aria}}">
                    <span class="cal-n">{{c.n}}</span>
                    <span class="dots"><sc-for list="{{c.dots}}" as="d" hint-placeholder-count="1"><span class="{{d.cls}}"></span></sc-for></span>
                    <span class="sb-muted">{{c.tag}}</span>
                  </button>
                </sc-if>
                <sc-if value="{{c.blank}}" hint-placeholder-val="{{ false }}"><span class="cal-c cc-blank"></span></sc-if>
              </sc-for>
            </div>
          </section>
          <section class="sb-card" style="flex: 2 1 340px; min-width: 0;" aria-labelledby="dd-h">
            <div class="sb-head"><h2 id="dd-h" class="sb-h2">{{dayTitle}}</h2><span class="sb-sub">{{dayCount}}</span></div>
            <sc-for list="{{dayRows}}" as="r" hint-placeholder-count="3">
              <div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 4px;">
                <span style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><span style="font-weight: 500;">{{r.title}}</span><span class="{{r.typeCls}}">{{r.type}}</span></span>
                <span class="sb-sub">{{r.client}}. {{r.which}}. {{r.left}}</span>
              </div>
            </sc-for>
            <sc-if value="{{dayEmpty}}" hint-placeholder-val="{{ false }}"><div class="sb-row"><span class="sb-sub">Nothing due on this day.</span></div></sc-if>
            <sc-if value="{{decShow}}" hint-placeholder-val="{{ true }}"><div class="sb-row" style="flex-direction: column; align-items: stretch; gap: 4px;"><span class="sb-th">Early December</span><sc-for list="{{dec}}" as="r" hint-placeholder-count="3"><span class="sb-sub">{{r.t}}</span></sc-for></div></sc-if>
          </section>
        </div>
      </sc-if>

      <div class="sb-card" style="padding: 12px 16px; display: flex; gap: 10px; align-items: flex-start;"><x-import component-from-global-scope="CareSync.Icon" name="shield-check" size="{{n18}}"></x-import><span class="sb-sub">{{footNote}}</span></div>
'''

SCRIPT_A = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { v: 'list', f: 'mine', day: 30 }; }
  renderVals() {
    const s = this.state;
    const DAY = 86400000, TODAY = Date.UTC(2026, 10, 2);
    const W = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const ts = d => Date.UTC(2026, d[0] - 1, d[1]);
    const fmt = d => { const x = new Date(ts(d)); return W[x.getUTCDay()] + ' ' + d[1] + ' ' + M[d[0] - 1]; };
    const left = d => { const n = Math.round((ts(d) - TODAY) / DAY); return n === 0 ? 'Today' : n === 1 ? '1 day' : n + ' days'; };
    // type: legal, duty, reg, tender, exp, after. main: [month, day, label]. target: [month, day] or null
    const D = [
      { c: 'Elm Tree Care Ltd', t: 'Reply to CQC\'s request for more information', type: 'reg', main: [11, 12, 'CQC reply by'], target: [11, 6], owner: 'Daniel', mine: true, note: 'Received by email Thu 29 Oct. 3 questions. Femi approves the answers first', cta: 'Open answers' },
      { c: 'Sunrise Homecare Ltd', t: 'Written representations to the Notice of Proposal', type: 'legal', main: [11, 17, 'Legal deadline'], target: [11, 10], owner: 'Daniel', mine: true, note: 'Served Wed 21 Oct, day 1 of 28 (worked out the safe way; confirm with a legal adviser). Draft by day 14 (Tue 3 Nov), senior review by Collins and Priya\'s approval by day 20 (Mon 9 Nov), send by day 21 (Tue 10 Nov)', cta: 'Open reply' },
      { c: 'Oakleaf Living Ltd', t: 'Case study due from Kemi, Northshire bid', type: 'tender', main: [11, 11, 'Due from Kemi'], target: null, owner: 'Daniel', mine: true, note: 'From the bid plan agreed with Kemi', cta: 'Open bid' },
      { c: 'Westbrook Care Ltd', t: 'Leon\'s reference 1 passes 6 months old', type: 'exp', main: [11, 12, 'Passes 6 months'], target: null, owner: 'Daniel', mine: true, note: 'Dated 12 May. Our rule: references under 6 months old on the resubmit date, Mon 30 Nov. Referee asked 28 Oct', cta: 'Open project' },
      { c: 'Oakleaf Living Ltd', t: 'Northshire clarification questions close, 17:00', type: 'tender', main: [11, 13, 'Buyer\'s deadline'], target: null, owner: 'Daniel', mine: true, note: 'Northshire County Council home care framework, Lot 1 North', cta: 'Open bid' },
      { c: 'Westbrook Care Ltd', t: 'Sade\'s DBS passes 12 months old', type: 'exp', main: [11, 18, 'Passes 12 months'], target: null, owner: 'Daniel', mine: true, note: 'Issued 18 Nov 2025. Our rule: DBS under 12 months old on the resubmit date. New application started 29 Oct, so the pack has a current one on 30 Nov', cta: 'Open project' },
      { c: 'Ashby Care', t: 'Month 12 handover', type: 'after', main: [11, 18, 'Handover'], target: null, owner: 'Daniel', mine: true, note: 'Summary of everything done and what is due next', cta: 'Open' },
      { c: 'Westbrook Care Ltd', t: 'Tribunal appeal window closes', type: 'legal', main: [11, 22, 'Legal deadline'], target: null, owner: 'Daniel', mine: true, note: 'Notice of decision received Mon 26 Oct, day 1 of 28 (worked out the safe way; confirm with a legal adviser). Sade chose to resubmit (recorded 28 Oct), so no appeal is planned', cta: 'Open project' },
      { c: 'Elm Tree Care Ltd', t: 'CQC interview with Claire Hughes', type: 'reg', main: [11, 24, 'Interview'], target: null, owner: 'Daniel', mine: true, note: 'Interview portal 40% done. Practice with Millicent Thu 5 Nov', cta: 'Open portal' },
      { c: 'Afon Care Ltd', t: 'CIW suitability interview with Rhian', type: 'reg', main: [11, 26, 'Interview'], target: null, owner: 'Daniel', mine: true, note: 'Practice with Millicent Mon 9 Nov', cta: 'Open' },
      { c: 'Westbrook Care Ltd', t: 'Resubmit the new pack to CQC', type: 'reg', main: null, target: [11, 30], owner: 'Daniel', mine: true, note: 'Senior review first, on Thu 12 Nov. Every date checked as valid on 30 Nov', cta: 'Open project' },
      { c: 'Oakleaf Living Ltd', t: 'Public liability insurance renews', type: 'exp', main: [11, 30, 'Renews'], target: null, owner: 'Daniel', mine: true, note: 'Ask Kemi for the new certificate. The Northshire bid needs a current one', cta: 'Open' },
      { c: 'Bryn Glas Care', t: 'CIW regulation 73 visit and report', type: 'duty', main: [11, 30, 'Due'], target: null, owner: 'Aftercare team', mine: false, note: 'Responsible individual visit, every 3 months. Month 4 of aftercare', cta: 'Open' },
      { c: 'Foyle Home Care', t: 'RQIA monthly quality monitoring report', type: 'duty', main: [11, 30, 'Due'], target: null, owner: 'Aftercare team', mine: false, note: 'Written by the registered person each month. Month 8 of aftercare', cta: 'Open' },
      { c: 'Oakleaf Living Ltd', t: 'Care Sync draft to Kemi, Northshire bid', type: 'tender', main: null, target: [11, 17], owner: 'Daniel', mine: true, note: '10 working days before the buyer\'s deadline. Kemi approves the final bid Tue 24 Nov, 5 working days before', cta: 'Open bid' },
      { c: 'Oakleaf Living Ltd', t: 'Northshire bid deadline, 12:00', type: 'tender', main: [12, 1, 'Buyer\'s deadline'], target: [11, 27], owner: 'Daniel', mine: true, note: 'Kemi approves the final bid Tue 24 Nov. Care Sync submits Fri 27 Nov, 2 working days before the deadline', cta: 'Open bid' },
      { c: 'Oakleaf Living Ltd', t: 'Eastford supported living application deadline', type: 'tender', main: [12, 4, 'Buyer\'s deadline'], target: null, owner: 'Daniel', mine: true, note: 'Dynamic purchasing system. Deciding scope, profile check under way', cta: 'Open bid' },
      { c: 'Lagan View Care Ltd', t: 'RQIA interviews', type: 'reg', main: [12, 8, 'Interviews'], target: null, owner: 'Olu (Daniel covering this week)', mine: true, note: 'Submitted on the RQIA Web Portal Wed 30 Sep. Practice with Millicent Wed 11 Nov', cta: 'Open' }
    ];
    const TYPE = { legal: ['Legal deadline', 'c-bad', 'd-legal'], duty: ['Duty in the regulations', 'c-bad', 'd-legal'], reg: ['Regulator', 'c-info', 'd-reg'], tender: ['Tender', 'c-brand', 'd-tender'], exp: ['Expiry', 'c-warn', 'd-exp'], after: ['Aftercare', 'c-neutral', 'd-after'] };
    const isLegal = x => x.type === 'legal' || x.type === 'duty';
    const test = { mine: x => x.mine, all: () => true, legal: isLegal };
    const items = D.filter(test[s.f]).map(x => {
      const first = x.target && (!x.main || ts(x.target) < ts(x.main)) ? x.target : x.main;
      return Object.assign({}, x, { first, when: ts(first) });
    }).sort((a, b) => a.when - b.when);
    const datesOf = x => {
      const out = [];
      if (x.target) out.push({ k: 'Our target', v: fmt(x.target), left: left(x.target), cls: 'sb-chip c-neutral' });
      if (x.main) out.push({ k: x.main[2], v: fmt(x.main), left: left(x.main), cls: 'sb-chip ' + (isLegal(x) ? 'c-bad' : 'c-info') });
      return out;
    };
    const row = x => { const d = new Date(x.when); return {
      title: x.t, client: x.c, owner: x.owner, note: x.note, cta: x.cta, type: TYPE[x.type][0], typeCls: 'sb-chip ' + TYPE[x.type][1],
      dow: W[d.getUTCDay()], day: String(d.getUTCDate()), mon: M[d.getUTCMonth()], dates: datesOf(x)
    }; };
    const G = [['This week', Date.UTC(2026, 10, 9)], ['Next week', Date.UTC(2026, 10, 16)], ['Later', Infinity]];
    let from = 0;
    const groups = G.map(([label, to]) => { const rows = items.filter(x => x.when >= from && x.when < to).map(row); from = to; return { label, count: rows.length === 1 ? '1 date' : rows.length + ' dates', rows }; }).filter(g => g.rows.length);
    // month view
    const dots = {};
    items.forEach(x => [x.main, x.target].forEach(d => { if (d && d[0] === 11) { (dots[d[1]] = dots[d[1]] || []).push({ x, which: d === x.target ? 'Our target' : d[2] }); } }));
    const cells = [];
    for (let i = 0; i < 6; i++) cells.push({ real: false, blank: true });
    for (let n = 1; n <= 30; n++) {
      const list = dots[n] || [];
      cells.push({ real: true, blank: false, n: String(n), cls: 'cal-c ' + (s.day === n ? 'cc-on' : 'cc-off'), pressed: s.day === n ? 'true' : 'false',
        aria: n + ' November: ' + (list.length === 1 ? '1 date' : list.length + ' dates'), tag: n === 2 ? 'Today' : (list.length > 2 ? list.length + ' dates' : ''),
        dots: list.map(o => ({ cls: 'dot ' + TYPE[o.x.type][2] })), pick: () => this.setState({ day: n }) });
    }
    while (cells.length % 7) cells.push({ real: false, blank: true });
    const sel = dots[s.day] || [];
    const dayRows = sel.map(o => ({ title: o.x.t, client: o.x.c, which: o.which, left: left([11, s.day]) + ' left', type: TYPE[o.x.type][0], typeCls: 'sb-chip ' + TYPE[o.x.type][1] }));
    const dec = items.filter(x => (x.main && x.main[0] === 12)).map(x => ({ t: fmt(x.main) + ': ' + x.c + ', ' + x.t + ' (' + left(x.main) + ')' }));
    const V = [['list', 'List by date'], ['month', 'Month']];
    const F = [['mine', 'Mine'], ['all', 'All'], ['legal', 'Legal deadlines only']];
    const GD = (id, fb) => (window.CSR ? window.CSR.get(id, fb) : fb);
    const footNote = 'Every date is worked out from the date a notice was served or a message was received, and recorded with evidence: a copy of the letter or email, the date it arrived, and who logged it. Legal periods are worked out the safe way: the day of service counts as day 1, so 28 days ends 27 days after service. If unsure, we use the earliest possible date and confirm with a legal adviser. Our own targets come first: for a Notice of Proposal, draft by day ' + GD('nop-draft-day', 14) + ', senior review and client approval by day ' + GD('nop-review-day', 20) + ', send by day ' + GD('nop-send-day', 21) + '. For tenders, we submit ' + GD('tender-submit-days-before', 2) + ' working days before the buyer\'s deadline.';
    return {
      theme: this.props.theme ?? 'light', three: 3, n18: 18, user: { name: 'Daniel Mensah', initials: 'DM' }, nav: __NAV__, footNote,
      views: V.map(([k, label]) => ({ label, on: s.v === k, off: s.v !== k, pick: () => this.setState({ v: k }) })),
      filters: F.map(([k, label]) => ({ label: label + ' (' + D.filter(test[k]).length + ')', on: s.f === k, off: s.f !== k, pick: () => this.setState({ f: k }) })),
      summary: items.length + ' dates. ' + items.filter(isLegal).length + ' legal. Mine includes the clients you cover for Olu this week',
      isList: s.v === 'list', isMonth: s.v === 'month', groups,
      dow: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].map(k => ({ k })), cells,
      dayTitle: fmt([11, s.day]), dayCount: sel.length === 1 ? '1 date' : sel.length + ' dates', dayRows, dayEmpty: sel.length === 0, dec, decShow: dec.length > 0
    };
  }
}'''
build(OUT + '/Deadlines.dc.html', 'Deadlines', 'Deadlines', int(sys.argv[2]) if len(sys.argv) > 2 else 1800, BODY_A, SCRIPT_A, 'deadlines', CSS_A)

# B. RegReply: answering a regulator
CSS_B = '''
.rr-ta{min-height:84px;padding:10px 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;line-height:20px;resize:vertical;box-sizing:border-box;width:100%}
.rr-inp{min-height:40px;padding:0 12px;border-radius:10px;border:1px solid var(--cs-border-control);background:var(--cs-surface-raised);color:var(--cs-text-primary);font:inherit;font-size:14px;box-sizing:border-box}
.rr-q{padding:16px 20px;border-top:1px solid var(--cs-border-subtle);display:flex;flex-direction:column;gap:8px}
.rr-quote{padding:10px 12px;border-left:3px solid var(--cs-border-default);background:var(--cs-surface-page);border-radius:0 8px 8px 0;font-size:14px;line-height:20px}
.rr-step{display:flex;gap:12px;align-items:flex-start;padding:12px 20px;border-top:1px solid var(--cs-border-subtle);font-size:14px;line-height:20px}
.rr-num{width:26px;height:26px;border-radius:999px;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;flex-shrink:0}
.n-done{background:var(--cs-action-primary);color:var(--cs-action-on-primary)}
.n-todo{border:2px solid var(--cs-border-control);color:var(--cs-text-secondary);box-sizing:border-box}
.rr-msg{padding:10px 12px;border-radius:10px;font-size:14px;line-height:20px}
.m-warn{background:var(--cs-status-warning-bg);color:var(--cs-text-primary)}
.m-ok{background:var(--cs-status-success-bg);color:var(--cs-text-primary)}
'''

BODY_B = '''      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px;">
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <h1 style="margin: 0; font-size: 32px; line-height: 40px; font-weight: 600;">Answering a regulator</h1>
          <span style="font-size: 15px; line-height: 22px; color: var(--cs-text-secondary);">One place to answer what a regulator has asked: each point, our answer, the evidence, a senior check, the client's approval, and a record of what was sent.</span>
        </div>
''' + tabs('tabs', 'Which reply') + '''      </div>

      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">
        <sc-for list="{{facts}}" as="k" hint-placeholder-count="4">
          <div class="sb-card sb-kpi"><span class="sb-muted">{{k.k}}</span><span style="font-size: 18px; line-height: 26px; font-weight: 600;">{{k.v}}</span><span class="{{k.cls}}" style="align-self: flex-start;">{{k.note}}</span></div>
        </sc-for>
      </div>

      <div style="display: flex; gap: 20px; flex-wrap: wrap; align-items: flex-start;">
        <section class="sb-card" style="flex: 3 1 600px; min-width: 0;" aria-labelledby="pt-h">
          <div class="sb-head" style="flex-direction: column; align-items: flex-start; gap: 2px;"><h2 id="pt-h" class="sb-h2">{{pointsTitle}}</h2><span class="sb-sub">{{pointsSub}}</span></div>
          <sc-for list="{{points}}" as="p" hint-placeholder-count="3">
            <div class="rr-q">
              <div style="display: flex; justify-content: space-between; gap: 10px; align-items: center; flex-wrap: wrap;"><span style="font-weight: 600;">{{p.n}}</span><span class="{{p.cls}}">{{p.state}}</span></div>
              <div class="rr-quote"><span class="sb-muted">{{p.qLabel}}</span><br>{{p.q}}</div>
              <label style="display: flex; flex-direction: column; gap: 4px; font-size: 13px; color: var(--cs-text-secondary);">{{p.aLabel}}<textarea class="rr-ta" value="{{p.a}}" onChange="{{p.onA}}"></textarea></label>
              <div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;"><span class="sb-muted">Evidence:</span><sc-for list="{{p.ev}}" as="e" hint-placeholder-count="2"><span class="{{e.cls}}">{{e.t}}</span></sc-for></div>
              <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><button class="sb-btn b-gh" onClick="{{p.flip}}">{{p.flipLabel}}</button><span class="sb-muted">{{p.hint}}</span></div>
            </div>
          </sc-for>
        </section>

        <div style="flex: 2 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 16px;">
          <section class="sb-card" aria-labelledby="st-h" style="padding-bottom: 8px;">
            <div class="sb-head"><h2 id="st-h" class="sb-h2">Before it goes</h2><span class="sb-sub">{{stepsSub}}</span></div>
            <sc-for list="{{steps}}" as="s" hint-placeholder-count="4">
              <div class="rr-step"><span class="{{s.cls}}">{{s.mark}}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="font-weight: 500;">{{s.t}}</span><span class="sb-sub">{{s.note}}</span></span></div>
            </sc-for>
            <div class="rr-step" style="flex-direction: column; align-items: stretch; gap: 8px;">
              <label style="display: flex; gap: 10px; align-items: center; min-height: 36px; cursor: pointer;"><input type="checkbox" checked="{{reviewed}}" onChange="{{onReview}}" style="width: 20px; height: 20px; accent-color: var(--cs-action-primary);">{{reviewLabel}}</label>
              <button class="sb-btn b-pri" style="align-self: flex-start;" onClick="{{toClient}}">{{toClientLabel}}</button>
              <sc-if value="{{blockShow}}" hint-placeholder-val="{{ false }}"><div class="rr-msg m-warn">{{blockText}}</div></sc-if>
            </div>
          </section>

          <section class="sb-card" aria-labelledby="rs-h" style="padding: 16px 20px; display: flex; flex-direction: column; gap: 10px;">
            <h2 id="rs-h" class="sb-h2">Record sent</h2>
            <span class="sb-sub">{{recordIntro}}</span>
            <sc-if value="{{canRecord}}" hint-placeholder-val="{{ false }}">
              <div style="display: flex; flex-direction: column; gap: 10px;">
                <label style="display: flex; flex-direction: column; gap: 4px; font-size: 13px;">Date sent<input class="rr-inp" placeholder="dd/mm/yyyy" value="{{sentDate}}" onChange="{{onDate}}"></label>
                <label style="display: flex; flex-direction: column; gap: 4px; font-size: 13px;">How it was sent<select class="rr-inp" value="{{method}}" onChange="{{onMethod}}"><option>By email, to the address the regulator gave</option><option>By post, recorded delivery</option><option>Through the regulator's online portal</option></select></label>
                <span class="sb-muted">A PDF copy of exactly what was sent is kept in the evidence log, with who sent it.</span>
                <button class="sb-btn b-pri" style="align-self: flex-start;" onClick="{{record}}">Record sent</button>
              </div>
            </sc-if>
            <sc-if value="{{recorded}}" hint-placeholder-val="{{ false }}"><div class="rr-msg m-ok">{{recordedText}}</div></sc-if>
          </section>

          <section class="sb-card" style="padding: 16px 20px; display: flex; flex-direction: column; gap: 6px;" aria-labelledby="pl-h">
            <h2 id="pl-h" class="sb-h2">{{plainTitle}}</h2>
            <span class="sb-sub">{{plain}}</span>
          </section>
        </div>
      </div>
'''

SCRIPT_B = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = {
      tab: 0,
      ready: [[true, false, true], [true, false, true]],
      ans: [[
        'We have recruited 6 care workers, with signed offers, and set out a rota for the first 3 months. A senior carer covers sickness and leave, and the manager is on call outside office hours. We will start with up to 8 people and grow only as staff join.',
        'Since the interview, the proposed manager has completed safeguarding adults training and two practice sessions with our coach. The local authority referral route, with phone numbers, is now written into the safeguarding policy and the staff handbook.',
        'The Statement of Purpose has been corrected. It now describes personal care only and lists no nursing or clinical tasks. The changes are marked so they are easy to check.'
      ], [
        'Our staffing plan now shows weekend cover: 2 care workers each Saturday and Sunday, with a senior carer on call. Sickness is covered by a bank of 2 relief workers who have finished induction.',
        'Claire was caring full time for a close family member from June 2021 to January 2022. She has written and signed a short statement to explain this.',
        'The office lease started on 1 October 2026. A copy of the signed lease is attached.'
      ]],
      reviewed: [false, false], stage: ['draft', 'draft'], block: [false, false], sentDate: ['', ''], method: ['By email, to the address the regulator gave', 'By email, to the address the regulator gave'], rec: ['', '']
    };
  }
  renderVals() {
    const st = this.state, t = st.tab;
    const set = (key, val) => { const a = st[key].slice(); a[t] = val; const o = {}; o[key] = a; this.setState(o); };
    const C = [{
      who: 'Priya', approver: 'Priya Shah', reviewer: 'Collins', reviewWhen: 'Mon 9 Nov',
      facts: [['Served (received)', 'Wed 21 Oct', 'Day 1. Notice saved', 'neutral'], ['Our target to send', 'Tue 10 Nov', 'Day 21: 8 days', 'warn'], ['Legal deadline', 'Tue 17 Nov', 'Day 28: 15 days', 'bad'], ['Senior review and approval', 'Mon 9 Nov', 'Day 20: Collins, then Priya', 'info']],
      targets: ['by day 14, Tue 3 Nov', 'by day 20, Mon 9 Nov', 'by day 20, Mon 9 Nov', 'by day 21, Tue 10 Nov'],
      pointsTitle: 'Sunrise Homecare Ltd: each ground in the Notice of Proposal',
      qLabel: 'What the notice says',
      aLabel: 'Our response',
      points: [
        ['Ground 1: staffing', 'The provider has not shown that there will be enough suitably trained staff to deliver the care described.', [['Staffing plan v3', 1], ['6 signed offers of employment', 1], ['Rota for the first 3 months', 1]]],
        ['Ground 2: safeguarding', 'At interview, the proposed manager could not explain how a safeguarding concern would be reported to the local authority.', [['Training certificate', 0], ['Safeguarding policy v2', 1], ['Coaching session notes', 1]]],
        ['Ground 3: Statement of Purpose', 'The Statement of Purpose describes clinical tasks that do not match the personal care service applied for.', [['Statement of Purpose v4, changes marked', 1]]]
      ],
      plainTitle: 'In plain English',
      plain: 'A Notice of Proposal tells the provider what CQC plans to decide and why. It is not the final decision. Written representations are the provider\'s chance to show CQC why it should decide differently, with evidence. We write them with Priya, who approves every word before anything is sent. If CQC still refuses, we resubmit, at no charge to the client. The 28 days are worked out the safe way: the day of service counts as day 1, so Priya\'s legal deadline is Tue 17 Nov. Confirm with a legal adviser if unsure. Our own targets: draft by day 14, senior review and Priya\'s approval by day 20, send by day 21, a week before the legal deadline.'
    }, {
      who: 'Femi', approver: 'Femi Adebayo', reviewer: 'Collins', reviewWhen: 'Thu 5 Nov',
      targets: ['', '', '', 'Fri 6 Nov, 4 working days before CQC\'s date'],
      facts: [['Received', 'Thu 29 Oct', 'By email, saved', 'neutral'], ['Our target to send', 'Fri 6 Nov', '4 days', 'warn'], ['CQC reply by', 'Thu 12 Nov', '10 days', 'info'], ['Senior review', 'Thu 5 Nov', 'Collins', 'info']],
      pointsTitle: 'Elm Tree Care Ltd: CQC request for more information',
      qLabel: 'CQC asked',
      aLabel: 'Our drafted answer',
      points: [
        ['Question 1: weekend and sickness cover', 'Please send an updated staffing plan showing how calls will be covered at weekends and during sickness.', [['Staffing plan v3', 1], ['Weekend rota', 1]]],
        ['Question 2: employment history', 'Please explain the gap in Claire Hughes\'s employment history between June 2021 and January 2022.', [['Claire\'s signed statement', 0]]],
        ['Question 3: office lease', 'Please confirm the office lease has started and send a copy.', [['Signed lease', 1]]]
      ],
      plainTitle: 'Why CQC asks',
      plain: 'Questions like these are a normal part of most applications and are not a sign of trouble. Clear, complete answers by the date CQC gives help the application keep moving towards Claire\'s interview on Tue 24 Nov.'
    }][t];
    const ready = st.ready[t];
    const points = C.points.map(([n, q, ev], i) => {
      const missing = ev.filter(e => !e[1]).length;
      const ok = ready[i];
      return {
        n, q, qLabel: C.qLabel, aLabel: C.aLabel, a: st.ans[t][i],
        onA: (e) => { const all = st.ans.map(x => x.slice()); all[t][i] = e.target.value; this.setState({ ans: all }); },
        ev: ev.map(([txt, have]) => ({ t: (have || ok ? txt : txt + ': waiting'), cls: 'sb-chip ' + (have || ok ? 'c-ok' : 'c-warn') })),
        state: ok ? 'Ready' : (missing ? 'Waiting for evidence' : 'Drafted'), cls: 'sb-chip ' + (ok ? 'c-ok' : 'c-warn'),
        flipLabel: ok ? 'Mark as not ready' : 'Mark ready',
        hint: ok ? 'Answer written and evidence attached.' : (missing ? 'Asked ' + C.who + ' for it. Mark ready once it is attached.' : 'Check the wording, then mark ready.'),
        flip: () => { const all = st.ready.map(x => x.slice()); all[t][i] = !ok; const stage = st.stage.slice(); if (stage[t] !== 'sent') stage[t] = 'draft'; this.setState({ ready: all, stage }); }
      };
    });
    const nReady = ready.filter(Boolean).length, allReady = nReady === ready.length;
    const stage = st.stage[t], reviewed = st.reviewed[t];
    const tg = i => C.targets[i] ? '. Target ' + C.targets[i] : '';
    const steps = [
      ['Draft every point', 'Daniel. ' + nReady + ' of ' + ready.length + ' ready' + tg(0), allReady],
      ['Senior review', C.reviewer + ', booked ' + C.reviewWhen + tg(1), reviewed],
      ['Client approves', C.approver + ' reads and approves the final wording' + tg(2), stage === 'approved' || stage === 'sent'],
      ['Send and record', 'Date, method and a copy kept as evidence' + tg(3), stage === 'sent']
    ].map(([tt, note, done], i) => ({ t: tt, note, cls: 'rr-num ' + (done ? 'n-done' : 'n-todo'), mark: done ? '✓' : String(i + 1) }));
    const left = [];
    if (!allReady) left.push((ready.length - nReady) + (ready.length - nReady === 1 ? ' point is' : ' points are') + ' not ready yet');
    if (!reviewed) left.push('the senior review by ' + C.reviewer + ' is booked for ' + C.reviewWhen);
    return {
      theme: this.props.theme ?? 'light', three: 3, user: { name: 'Daniel Mensah', initials: 'DM' }, nav: __NAV__,
      tabs: ['Sunrise: Notice of Proposal', 'Elm Tree: CQC questions'].map((label, i) => ({ label, on: t === i, off: t !== i, pick: () => this.setState({ tab: i }) })),
      facts: C.facts.map(([k, v, note, c]) => ({ k, v, note, cls: 'sb-chip c-' + c })),
      pointsTitle: C.pointsTitle, pointsSub: nReady + ' of ' + ready.length + ' ready. Edit any answer here; every change is saved with who made it.', points,
      stepsSub: stage === 'sent' ? 'Sent and recorded' : stage === 'approved' ? 'Approved, ready to send' : stage === 'client' ? 'With ' + C.who + ' for approval' : 'In progress',
      steps, reviewed, reviewLabel: C.reviewer + ' has reviewed it (booked ' + C.reviewWhen + ')',
      onReview: () => set('reviewed', !reviewed),
      toClientLabel: stage === 'draft' ? 'Send to client for approval' : stage === 'client' ? 'Record ' + C.who + '\'s approval' : stage === 'approved' ? 'Approved by ' + C.who : 'Sent',
      toClient: () => { if (stage === 'client') { const s3 = st.stage.slice(); s3[t] = 'approved'; this.setState({ stage: s3 }); return; } if (stage !== 'draft') return; if (allReady && reviewed) { const s2 = st.stage.slice(); s2[t] = 'client'; const b = st.block.slice(); b[t] = false; this.setState({ stage: s2, block: b }); } else set('block', true); },
      blockShow: st.block[t] && stage === 'draft', blockText: 'Not yet: ' + left.join(', and ') + '. We only send to ' + C.who + ' once every point is ready and checked.',
      canRecord: stage === 'approved', recorded: stage === 'sent',
      recordIntro: stage === 'draft' || stage === 'client' ? 'Opens once ' + C.who + ' has approved the final wording.' : stage === 'approved' ? C.who + ' has approved. Once it is sent, record it here.' : 'Done. This is the record the team and the client can see.',
      sentDate: st.sentDate[t], onDate: (e) => set('sentDate', e.target.value),
      method: st.method[t], onMethod: (e) => set('method', e.target.value),
      record: () => { if (!st.sentDate[t].trim()) return; const s2 = st.stage.slice(); s2[t] = 'sent'; this.setState({ stage: s2 }); },
      recordedText: 'Recorded: sent ' + st.sentDate[t] + ', ' + st.method[t].charAt(0).toLowerCase() + st.method[t].slice(1) + '. A copy is kept as evidence, and ' + C.who + ' can see it in the Hub.',
      plainTitle: C.plainTitle, plain: C.plain
    };
  }
}'''
build(OUT + '/RegReply.dc.html', 'Answering a regulator', 'Deadlines: answering a regulator', int(sys.argv[3]) if len(sys.argv) > 3 else 1600, BODY_B, SCRIPT_B, 'deadlines', CSS_B)
