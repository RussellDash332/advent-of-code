import sys, math, re
r = {}
for l in sys.stdin:
    l = l.strip()
    if not l: break
    n, u = l.split('{'); u = u[:-1].split(','); h = []
    for v in u[:-1]: c, e = v.split(':'); h.append((c[0], c[1], int(c[2:]), e))
    h.append(u[-1]); r[n] = h

def solve(h, c='in'):
    if c == 'A': return math.prod(b-a+1 for a,b in h.values())
    elif c == 'R': return 0
    u = r[c]; f = 0
    for v, s, z, w in u[:-1]:
        k = h.copy(); a, b = k[v]
        if s == '<' and z > a: k[v] = (a, min(z-1, b)); h[v] = (min(z, b+1), b); f += solve(k, w)
        if s == '>' and z < b: k[v] = (max(a, z+1), b); h[v] = (a, max(a-1, z)); f += solve(k, w)
    return f + solve(h, u[-1])

print('Part 1:', sum(map(lambda x: [t:=dict(zip('xmas', map(lambda x: [int(x)]*2, re.findall('\d+', x)))), sum(i[1] for i in t.values())*solve(t)][1], sys.stdin)))
print('Part 2:', solve({i:(1,4000) for i in 'xmas'}))