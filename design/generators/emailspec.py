# Parse the client emails spec into sections and emails (read only).
import re
SPEC = '/home/user/Assets/docs/superpowers/specs/2026-11-02-care-sync-hub-client-emails.md'
def parse():
    secs = []; cur = None; em = None
    for line in open(SPEC, encoding='utf-8').read().split('\n'):
        m = re.match(r'^## (\d+)\. (.+)$', line)
        if m:
            cur = {'n': m.group(1), 'name': m.group(2).strip(), 'emails': []}; secs.append(cur); em = None; continue
        if line.startswith('## '):
            cur = None; em = None; continue
        m = re.match(r'^### (\d+\.\d+[a-z]?) (.+)$', line)
        if m and cur is not None:
            em = {'num': m.group(1), 'name': m.group(2).strip(), 'trigger': '', 'subject': '', 'lines': [], 'button': ''}
            cur['emails'].append(em); continue
        if em is None: continue
        if line.strip() == '---': em = None; continue
        t = re.match(r'^\*\*Trigger:\*\* (.+)$', line)
        if t: em['trigger'] = t.group(1).strip(); continue
        s = re.match(r'^\*\*Subject:\*\* (.+)$', line)
        if s: em['subject'] = s.group(1).strip(); continue
        b = re.match(r'^Button: (.+)$', line)
        if b: em['button'] = b.group(1).strip(); continue
        em['lines'].append(line)
    secs = [s for s in secs if s['emails']]
    return secs
if __name__ == '__main__':
    S = parse(); n = 0
    for s in S:
        print(s['n'], s['name'], len(s['emails']))
        for e in s['emails']:
            n += 1
            body = '\n'.join(e['lines'])
            f = sorted(set(re.findall(r'\{\{([^}]+)\}\}', body + e['subject'])))
            print('  ', e['num'], e['name'], '|T:', e['trigger'][:50], '|', f)
    print('TOTAL', n)
