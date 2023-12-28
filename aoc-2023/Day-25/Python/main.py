import sys, re
from collections import *

g = {}; r = {}
for l in sys.stdin:
    a, *b = re.findall('\w+', l)
    if a not in r: r[a] = len(r)
    for v in b:
        if v not in r: r[v] = len(r)
    g[a] = b
INF = float('inf'); V = len(r)

def BFS(s, t):
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for idx in AL[u]:
            v, cap, flow = EL[idx]
            if cap > flow and d[v] == -1:
                d[v] = d[u]+1
                q.append(v)
    return d[t] != -1

def DFS(u, t, f=INF):
    if u == t or f == 0: return f
    for i in range(last[u], len(AL[u])):
        last[u] = i
        v, cap, flow = EL[AL[u][i]]
        if d[v] != d[u]+1: continue
        pushed = DFS(v, t, min(f, cap - flow))
        if pushed:
            EL[AL[u][i]][2] += pushed
            EL[AL[u][i]^1][2] -= pushed
            return pushed
    return 0

EL, AL = [], [[] for _ in range(V)]
for i in g:
    for j in g[i]: EL.append([r[j], 1, 0]), AL[r[i]].append(len(EL)-1), EL.append([r[i], 1, 0]), AL[r[j]].append(len(EL)-1)
for source in range(V):
    for sink in range(source+1, V):
        mf = 0; d = [-1]*V
        for e in EL: e[2] = 0
        while BFS(source, sink):
            last = [0]*V; f = DFS(source, sink)
            while f: mf += f; f = DFS(source, sink)
            d = [-1]*V
        if mf == 3:
            c = sum(i!=-1 for i in d)
            print('Part 1:', c*(V-c))
            print('Part 2: THE END!'), exit(0)