import sys
m = [*map(str.strip, sys.stdin)]; R = len(m); C = len(m[0]); n = R*C
K = ((0, -1, '<'), (0, 1, '>'), (1, 0, 'v'), (-1, 0, '^'))
F = [{} for _ in range(n)]
G = [{} for _ in range(n)]
for rr in range(R):
    for cc in range(C):
        if m[rr][cc] == '#': continue
        curr = rr*C+cc
        for dr, dc, z in K:
            if 0<=rr+dr<R and 0<=cc+dc<C and m[rr+dr][cc+dc] != '#':
                nxt = (rr+dr)*C+cc+dc
                if z == m[rr][cc] or m[rr][cc] == '.': F[curr][nxt] = 1
                G[curr][nxt] = 1
for u in (i for i in range(R*C) if len(G[i]) == 2):
    (a, b), (c, d) = G[u].items()
    G[u] = {}
    del G[a][u]; del G[c][u]
    G[a][c] = G[c][a] = b+d

# recursive
sys.setrecursionlimit(3000)
def bt(g, v, d, p):
    if v in p: return
    if v == n-2: ans[0] = max(ans[0], d); return
    p.add(v)
    for w in g[v]: bt(g, w, d+g[v][w], p)
    p.discard(v)

# iterative
def bt_iter(g, v, d, p):
    s = [(2*v, d)]; T = 2*n-4
    while s:
        v, d = s.pop()
        if v%2: p.discard(v-1)
        else:
            if v in p: continue
            if v == T: ans[0] = max(ans[0], d); continue
            p.add(v), s.append((v+1, d))
            for w in g[v//2]: s.append((2*w, d+g[v//2][w]))

ans = [0]; bt(F, 1, 0, set()), print('Part 1:', ans[0])
ans = [0]; bt(G, 1, 0, set()), print('Part 2:', ans[0])