const { chromium } = require('playwright');
const fs = require('fs');
const canvas = JSON.parse(fs.readFileSync('render/project/canvas.json'));
(async () => {
  const b = await chromium.launch();
  const out = [];
  for (const [name, bd] of Object.entries(canvas.boards)) {
    for (const theme of ['light', 'dark']) {
      const p = await b.newPage({ viewport: { width: bd.w || 390, height: 900 } });
      const errs = [];
      p.on('pageerror', e => errs.push(e.message.slice(0, 120)));
      p.on('console', m => { if (m.type() === 'error' && !/favicon|woff/.test(m.text())) errs.push(m.text().slice(0, 120)); });
      try {
        await p.goto('http://localhost:8765/project/' + name, { waitUntil: 'load', timeout: 30000 });
        await p.waitForTimeout(1500);
        if (theme === 'dark') { await p.evaluate(() => document.querySelectorAll('[data-cs-theme]').forEach(e => e.setAttribute('data-cs-theme', 'dark'))); await p.waitForTimeout(200); }
        const m = await p.evaluate(() => {
          const r = document.querySelector('[data-cs-theme]');
          if (!r) return { noRoot: true };
          const rr = r.getBoundingClientRect();
          let hidden = 0, wide = 0, darkText = 0, samples = [];
          // content clipped at the bottom: deepest element bottom vs root height
          let maxBottom = 0;
          r.querySelectorAll('*').forEach(el => { const b = el.getBoundingClientRect(); if (b.width && b.height) { maxBottom = Math.max(maxBottom, b.bottom - rr.top); if (b.right - rr.left > rr.width + 2 && getComputedStyle(el).position !== 'fixed') { wide++; if (samples.length < 2) samples.push((el.textContent || el.tagName).trim().slice(0, 40)); } } });
          return { h: Math.round(rr.height), content: Math.round(maxBottom), wide, samples };
        });
        let dark = 0;
        if (theme === 'dark') dark = await p.evaluate(() => {
          // text that stays dark on a dark background
          let n = 0; const lum = c => { const v = (c.match(/\d+(\.\d+)?/g) || []).slice(0, 3).map(Number); return v.length < 3 ? 1 : (0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]) / 255; };
          document.querySelectorAll('[data-cs-theme] *').forEach(el => { if (el.children.length === 0 && (el.textContent || '').trim()) { const s = getComputedStyle(el); let bg = el, bgc = 'rgba(0, 0, 0, 0)'; while (bg && (bgc = getComputedStyle(bg).backgroundColor) === 'rgba(0, 0, 0, 0)') bg = bg.parentElement; if (lum(s.color) < 0.35 && lum(bgc) < 0.35) n++; } });
          return n;
        });
        out.push({ name, theme, errs: errs.length, err1: errs[0] || '', ...m, dark });
        if (theme === 'light' || dark > 0) await p.screenshot({ path: 'shots/' + name.replace('.dc.html', '') + '-' + theme + '.png', fullPage: false, clip: { x: 0, y: 0, width: bd.w || 390, height: Math.min(m.content || 900, 4000) } }).catch(() => {});
      } catch (e) { out.push({ name, theme, fail: e.message.slice(0, 100) }); }
      await p.close();
    }
  }
  fs.writeFileSync('audit.json', JSON.stringify(out, null, 1));
  await b.close();
})();
