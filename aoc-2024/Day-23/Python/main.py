g = {}
for r in open(0):
    a,b=r.strip().split('-')
    g[a]=g.get(a,set())
    g[b]=g.get(b,set())
    g[a].add(b),g[b].add(a)
Z = set()
for i in g:
    for j in g[i]:
        for k in g[i]&g[j]:
            if len({i,j,k})==3 and 't' in i[0]+j[0]+k[0]:
                Z.add(tuple(sorted((i,j,k))))
print('Part 1:', len(Z))

def bk(r, p, x):
    if not p and not x: return ','.join(sorted(r))
    ans = ''
    for i in p: u = i; break
    for i in x: u = i; break
    for w in [*p]:
        if w in g[u]: continue
        r.add(w); ans = max(ans, bk(r, p&g[w], x&g[w]),key=lambda x:len(x.split(','))); r.discard(w), p.discard(w), x.add(w)
    return ans
print('Part 2:', bk(set(), {*g}, set()))