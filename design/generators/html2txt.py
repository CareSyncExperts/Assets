import sys,re
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0; s.buf=''
    def handle_starttag(s,t,a):
        if t in('script','style','head'): s.skip+=1
        if t in('div','p','br','li','h1','h2','h3','span','label','tr'): s.flush()
    def handle_endtag(s,t):
        if t in('script','style','head'): s.skip-=1
        s.flush()
    def handle_data(s,d):
        if not s.skip: s.buf+=d
    def flush(s):
        x=re.sub(r'\s+',' ',s.buf).strip()
        if x and (not s.out or s.out[-1]!=x): s.out.append(x)
        s.buf=''
p=P(); p.feed(open(sys.argv[1],encoding='utf-8').read()); p.flush()
open(sys.argv[2],'w').write('\n'.join(p.out))
print(len(p.out))
