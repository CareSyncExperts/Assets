const { chromium } = require('playwright');
const boards = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  for (const name of boards) {
    const p = await b.newPage({ viewport: { width: 1440, height: 1000 } });
    const errs = [];
    p.on('pageerror', e => errs.push(e.message.slice(0, 120)));
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 120)); });
    await p.goto('http://localhost:8765/project/' + name, { waitUntil: 'load' });
    await p.waitForTimeout(1200);
    const n = await p.$$eval('[data-cs-theme] button', bs => bs.length);
    let changed = 0, same = 0;
    const dead = [];
    for (let i = 0; i < n; i++) {
      const before = await p.evaluate(() => document.querySelector('[data-cs-theme]').innerText);
      const bs = await p.$$('[data-cs-theme] button');
      if (!bs[i]) continue;
      const label = ((await bs[i].innerText()) || (await bs[i].getAttribute('aria-label')) || '').trim().slice(0, 40);
      try { await bs[i].click({ timeout: 2000 }); } catch (e) { continue; }
      await p.waitForTimeout(150);
      const after = await p.evaluate(() => document.querySelector('[data-cs-theme]').innerText);
      if (after !== before) changed++; else { same++; if (dead.length < 14) dead.push(label); }
    }
    console.log(name + ': ' + n + ' buttons, ' + changed + ' change the screen, ' + same + ' no change in the demo, errors ' + errs.length + ' ' + (errs[0] || ''));
    console.log('   no visible effect: ' + dead.join(' | '));
    await p.close();
  }
  await b.close();
})();
