const fs=require('fs');
const [,,file,...scen]=process.argv;
const h=fs.readFileSync(file,'utf8');
let js=h.split('data-dc-script')[1]; js=js.slice(js.indexOf('>')+1, js.indexOf('</script>'));
const C=new Function('DCLogic', js+'\nreturn Component;')(class{constructor(p){this.props=p||{};this.state={}}setState(o){Object.assign(this.state,o)}});
for (const s of scen){
  const c=new C({}); Object.assign(c.state.a, JSON.parse(s)); c.state.i=0;
  let v=c.renderVals(); const n=+v.secTotal; const titles=[]; let fieldCount=0;
  for(let i=0;i<n;i++){c.state.i=i; v=c.renderVals(); titles.push(v.secTitle+' ('+v.fields.length+')'); fieldCount+=v.fields.length;}
  console.log(s,'\n  pages',n,'fields',fieldCount,v.skipNote,'\n  '+titles.join(' | '));
}
