const { chromium } = require('playwright');
const fs = require('fs');
const canvas = JSON.parse(fs.readFileSync('render/project/canvas.json'));
(async () => {
  const b = await chromium.launch(); let bad = 0;
  for (const [name, bd] of Object.entries(canvas.boards)) {
    const p = await b.newPage({ viewport: { width: bd.w || 390, height: 900 } });
    await p.goto('http://localhost:8765/project/' + name, { waitUntil: 'load' }); await p.waitForTimeout(1200);
    const r = await p.evaluate(() => {
      const root = document.querySelector('[data-cs-theme]'); if (!root) return ['no root'];
      const text = root.innerText + ' ' + [...root.querySelectorAll('input,textarea')].map(e => e.value + ' ' + (e.placeholder || '')).join(' ') + ' ' + [...root.querySelectorAll('[aria-label]')].map(e => e.getAttribute('aria-label')).join(' ');
      const hits = []; for (const pat of ['[object Object]', 'undefined', 'NaN', '{{', '}}', 'null']) { const i = text.indexOf(pat); if (i >= 0) hits.push(pat + ': ...' + text.slice(Math.max(0, i - 40), i + 30).replace(/\s+/g, ' ')); }
      return hits;
    });
    if (r.length) { bad++; console.log(name, r.join(' | ')); }
    await p.close();
  }
  console.log('screens with leftovers:', bad, 'of', Object.keys(canvas.boards).length);
  await b.close();
})();
