G = {}
for l in open(0):
    x, *v = l.strip().split(); x = x[:-1]
    if x not in G: G[x] = []
    for i in v:
        G[i] = G.get(i, [])
    G[x] = v
I = {}
for i in G:
    for j in G[i]: I[j] = I.get(j, 0)+1
Q = [i for i in G if i not in I]
for u in Q:
    for v in G[u]: I[v] -= 1; I[v] < 1 != Q.append(v)
Z = {x:[1,0,0,0] for x in Q if not G[x]}
while Q:
    u = Q.pop()
    Z[u] = Z.get(u, [0]*4)
    for v in G[u]:
        for i in range(4): Z[u][i|(u=='dac')|2*(u=='fft')] += Z[v][i]
print('Part 1:', sum(Z.get('you', [0]*4)))
print('Part 2:', Z.get('svr', [0]*4)[3])