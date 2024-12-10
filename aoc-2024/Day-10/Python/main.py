R = len(m:=[*open(0)])
C = len(m[-1])
N = R*C
G = [[] for _ in range(N)]
I = [0]*R*C
T = []
for i in range(N):
    r = i//C; c = i%C
    for dr, dc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        if R>r+dr>-1<c+dc<C and int(m[r+dr][c+dc]) == int(m[r][c])+1: G[i].append(j:=(r+dr)*C+c+dc); I[j] += 1
Q = [i for i in range(N) if I[i] == 0]
for u in Q:
    T.append(u)
    for v in G[u]:
        I[v] -= 1
        if I[v] == 0: Q.append(v)
X = {i for i in range(N) if m[i//C][i%C]>'8'}; A = B = 0
for x in X:
    D = [0]*N; D[x] = 1
    for u in T[::-1]:
        for v in G[u]: D[u] += D[v]
    A += sum((D[i]>0)*(m[i//C][i%C]=='0')for i in range(N))
    B += sum(D[i]*(m[i//C][i%C]=='0')for i in range(N))
print('Part 1:', A, '\nPart 2:', B)