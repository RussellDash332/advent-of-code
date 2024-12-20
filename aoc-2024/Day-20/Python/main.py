m = [[*x.strip()] for x in open(0)]; R = len(m); C = len(m[0])
K = ((0, 1), (0, -1), (-1, 0), (1, 0)); G = set()
for i in range(R):
    for j in range(C):
        if m[i][j] == 'S': S = i*C+j; m[i][j] = '.'
        if m[i][j] == 'E': E = i*C+j; m[i][j] = '.'
        if m[i][j] == '.': G.add(i*C+j)

def bfs(v):
    D = [-1]*R*C; D[v] = 0; Q = [v]
    for u in Q:
        r, c = divmod(u, C)
        for dr, dc in K:
            p = (r+dr)*C+c+dc
            if D[p] < 0 and m[r+dr][c+dc] == '.': D[p] = D[u]+1; Q.append(p)
    return D

A = bfs(S); B = bfs(E); X = A[E]
for p in range(2):
    Z = 0; Y = 2+18*p
    for i in G:
        ri, ci = divmod(i, C)
        for rj in range(max(ri-Y, 1), min(ri+Y+1, R)):
            d = Y-abs(ri-rj)
            for cj in range(max(ci-d, 1), min(ci+d+1, C)):
                if rj*C+cj in G:
                    v = A[i]+B[rj*C+cj]+abs(ri-rj)+abs(ci-cj)
                    if X-v >= 100: Z += 1
    print(f'Part {p+1}:', Z)