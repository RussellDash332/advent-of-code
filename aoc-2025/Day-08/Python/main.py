from heapq import *
from math import *
import sys

P = [[*map(int, l.split(','))] for l in sys.stdin]
N = len(P)

Up = [*range(N)]; Urank = [0]*N; Usize = [1]*N; Un = [N]
def find(i):
    if Up[i] == i: return i
    Up[i] = find(Up[i])
    return Up[i]
def union(i, j):
    if (x:=find(i)) != (y:=find(j)):
        Un[0] -= 1
        if Urank[x] > Urank[y]: Up[y] = x; Usize[x] += Usize[y]
        else: Up[x] = y; Urank[y] += Urank[x] == Urank[y]; Usize[y] += Usize[x]

E = [(hypot(P[i][0]-P[j][0], P[i][1]-P[j][1], P[i][2]-P[j][2]), i, j) for i in range(N) for j in range(i)]
heapify(E)
k = 0
while Un[0] > 1:
    _, a, b = heappop(E); union(a, b)
    if k == 999:
        *_, p, q, r = sorted(Usize[i] for i in {*map(find, range(N))})
        print('Part 1:', p*q*r)
    k += 1
print('Part 2:', P[a][0]*P[b][0])