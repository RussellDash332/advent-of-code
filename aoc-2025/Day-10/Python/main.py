import z3
p1 = p2 = 0
for l in open(0):
    m, *p, c = l.split()
    n = len(m)-2
    q = [*map(lambda x: eval(x[:-1]+',)'), p)]
    c = [*map(int, c[1:-1].split(','))]

    B = [-1]*(1<<n); B[0] = 0    
    p = [*map(lambda x: sum(1<<i for i in x), q)]
    m = int(m[-2:0:-1].replace('#', '1').replace('.', '0'), 2)
    Q = [0]
    for u in Q:
        for v in p:
            if ~B[u^v]: continue
            B[u^v] = B[u]+1; Q.append(u^v)
    p1 += B[m]

    S = [z3.Int(f'x{i}') for i in range(len(p))]
    s = z3.Optimize()
    G = [[] for _ in range(n)]
    for i in range(len(q)):
        s.add(S[i] >= 0)
        for e in q[i]: G[e].append(i)
    for i in range(n):
        s.add(sum(S[k] for k in G[i]) == c[i])
    s.minimize(sum(S)); s.check()
    p2 += int(str(s.model().eval(sum(S))))
print('Part 1:', p1)
print('Part 2:', p2)