from heapq import *; INF = 1e18
K=((0,-1),(-1,0),(1,0),(0,1));R=len(M:=[*open(0)]);C=len(M[-1])
for i in range(R):
    for j in range(C):
        if M[i][j]=='S': si, sj = i, j
        if M[i][j]=='E': ei, ej = i, j
def dijkstra(Q, z):
    D = {x:0 for _,x in Q}
    while Q:
        t, (u, v, du, dv) = heappop(Q)
        if (u, v) == z: continue
        for di, dj in K:
            if (di, dj) != (du, dv) and M[u][v] > '#' and D.get(n:=(u, v, di, dj), INF) >= t+1000: D[n] = t+1000; heappush(Q, (D[n], n))
        if M[u+du][v+dv] > '#' and D.get(n:=(u+du, v+dv, du, dv), INF) >= t+1: D[n] = t+1; heappush(Q, (D[n], n))
    return D
V = dijkstra([(0, (si, sj, 0, 1))], (ei, ej))
W = dijkstra([(0, (ei, ej, di, dj)) for di, dj in K], (si, sj))
Z = set()
print('Part 1:', X:=min(V.get((ei, ej, di, dj), INF) for di, dj in K))
for i, j, di, dj in V:
    if V[(i, j, di, dj)]+W.get((i, j, -di, -dj), INF)==X: Z.add((i, j))
print('Part 2:', len(Z))