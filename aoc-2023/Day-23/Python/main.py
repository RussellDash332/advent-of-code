import sys
m = [*map(str.strip, sys.stdin)]; R = len(m); C = len(m[0]); n = R*C
K = ((0, -1, '<'), (0, 1, '>'), (1, 0, 'v'), (-1, 0, '^'))
F = [{} for _ in range(n)]; G = [{} for _ in range(n)]
for rr in range(R):
    for cc in range(C):
        if m[rr][cc] == '#': continue
        curr = rr*C+cc
        for dr, dc, z in K:
            if 0<=rr+dr<R and 0<=cc+dc<C and m[rr+dr][cc+dc] != '#':
                nxt = (rr+dr)*C+cc+dc
                if z == m[rr][cc] or m[rr][cc] == '.': F[curr][nxt] = 1
                G[curr][nxt] = 1
for u in range(n):
    if len(G[u]) == 2: (a, b), (c, d) = G[u].items(); G[u] = {}; del G[a][u]; del G[c][u]; G[a][c] = G[c][a] = b+d

# iterative
def bt_iter():
    s = [(2, 0)]; T = 2*n-4; ans = 0; p = set()
    while s:
        v, d = s.pop()
        if v%2: p.discard(v-1)
        else:
            if v in p: continue
            if v == T: ans = max(ans, d); continue
            p.add(v), s.append((v+1, d))
            for w in F[v//2]: s.append((2*w, d+F[v//2][w]))
    return ans

# recursive
def bt():
    for i in range(n): G[i] = tuple(G[i].items())
    ans = [0]; p = [0]*n
    def f(v, d):
        if p[v]: return
        if v == t:
            if ans[0] < d: ans[0] = d
            return
        p[v] = 1
        for w, x in G[v]: f(w, d+x)
        p[v] = 0
    s, y = [*G[1]][0]; t, z = [*G[n-2]][0] # the input is nice :)
    f(s, y+z); return ans[0]

print('Part 1:', bt_iter())
print('Part 2:', bt())