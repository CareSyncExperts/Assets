const fs=require('fs');
const [,,file,scen]=process.argv;
const h=fs.readFileSync(file,'utf8');
let js=h.split('data-dc-script')[1]; js=js.slice(js.indexOf('>')+1, js.indexOf('</script>'));
const C=new Function('DCLogic', js+'\nreturn Component;')(class{constructor(p){this.props=p||{};this.state={}}setState(o){Object.assign(this.state,o)}});
const c=new C({}); Object.assign(c.state.a, JSON.parse(scen||'{}')); c.state.i=0;
let v=c.renderVals(); const n=+v.secTotal;
for(let i=0;i<n;i++){c.state.i=i; v=c.renderVals();
  console.log(`\n=== ${v.secNo}/${v.secTotal} ${v.secTitle}\n    ${v.secIntro}`);
  for(const f of v.fields){
    if(f.isInfo) console.log('  [i] '+f.label.replace(/\n/g,' / '));
    else if(f.isJump) console.log('  > '+f.label);
    else { const t=f.isText?'text':f.isPara?'para':f.isChoice?'choice':f.isMulti?'multi':f.isFile?'file':'sign';
      console.log(`  - ${f.label}${f.req?' *':''} [${t}]${f.value?' = '+f.value:''}${f.opts.length?' {'+f.opts.map(o=>(o.on?'(x)':'')+o.label).join(' | ')+'}':''}${f.tip?'\n      tip: '+f.tip:''}${f.ok?'\n      ok: '+f.ok:''}`);}
  }
}
