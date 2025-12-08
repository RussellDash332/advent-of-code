class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N; self.size = [1]*N; self.n = N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            self.n -= 1
            if self.rank[x] > self.rank[y]: self.p[y] = x; self.size[x] += self.size[y]
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]; self.size[y] += self.size[x]
from math import *
P = [[*map(int, l.split(','))] for l in open(0)]
U = UFDS(N:=len(P))
E = sorted((hypot(*(a-b for a,b in zip(P[i], P[j]))), i, j) for i in range(N) for j in range(i))
for k, (_, a, b) in enumerate(E):
    U.union(a, b)
    if k == 999:
        print('Part 1:', prod(sorted(U.size[i] for i in {U.find(i) for i in range(N)})[-3:]))
    if U.n == 1:
        print('Part 2:', P[a][0]*P[b][0])
        break