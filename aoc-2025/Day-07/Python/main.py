M = [l.strip() for l in open(0)]
R, C = len(M), len(M[0])
S = set()
Q = [(1, i) for i in range(len(M[0])) if M[0][i] == 'S']
D = {}
for r, c in Q:
    if (r, c) in S or not R>r>-1<c<C: continue
    if M[r][c] == '^':
        D[(r, c)] = [(r, c-1), (r, c+1)]
        Q += D[(r, c)]
        S.add((r, c))
    else:
        D[(r, c)] = [(r+1, c)]
        Q += D[(r, c)]
I = {}
for i in D.values():
    for j in i: I[j] = I.get(j, 0)+1
Q = [Q[0]]
for u in Q:
    for v in D.get(u, []): I[v] -= 1; I[v] < 1 != Q.append(v)
Z = {x:1 for x in Q if x[0]==R}
while Q:
    u = Q.pop(); Z[u] = Z.get(u, 0)+sum(Z.get(v, 0) for v in D.get(u, []))
print('Part 1:', len(S))
print('Part 2:', Z[u])