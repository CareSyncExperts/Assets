const { chromium } = require('playwright');
(async () => {
  const [,, name, theme, out, w, h] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w || 390, height: +h || 900 }, deviceScaleFactor: 1 });
  const errs = [];
  p.on('pageerror', e => errs.push(e.message.slice(0, 160)));
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 160)); });
  await p.goto('http://localhost:8765/project/' + name + (theme === 'dark' ? '?theme=dark' : ''), { waitUntil: 'load' });
  await p.waitForTimeout(2500);
  if (theme === 'dark') await p.evaluate(() => document.querySelectorAll('[data-cs-theme]').forEach(e => e.setAttribute('data-cs-theme', 'dark')));
  await p.waitForTimeout(300);
  await p.screenshot({ path: out, fullPage: true });
  console.log(name, theme, 'errors:', errs.length, errs.slice(0, 3).join(' | '));
  await b.close();
})();
