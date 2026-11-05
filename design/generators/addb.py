import json,sys
p=sys.argv[1]; name,title,w,h,x,y,inter=sys.argv[2:9]
c=json.load(open(p))
b={"h":int(h),"title":title,"w":int(w),"x":int(x),"y":int(y)}
if int(w)>=1000: b["expand"]="fill"
if inter=='1': b["is_interactive"]=True
c['boards'][name]=b
if name not in c['order']: c['order'].append(name)
if len(sys.argv)>9:
    k,txt,ny,mw=sys.argv[9:13]
    c['notes'][k]={"kind":"title1","maxW":int(mw),"text":txt,"w":240,"x":0,"y":int(ny)}
    if k not in c['noteOrder']: c['noteOrder'].append(k)
json.dump(c,open(p,'w'),indent=2)
