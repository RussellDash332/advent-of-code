import sys
from collections import deque
from functools import reduce
from math import gcd

G = {}; GT = {}; T = {}; S = {}
for l in sys.stdin:
    a, b = l.strip().split(' -> ')
    if a == 'broadcaster': T[a] = -1
    elif a[0] == '%': a = a[1:]; T[a] = S[a] = 0
    else: a = a[1:]; T[a] = 1
    b = b.split(', '); G[a] = b
    for c in b:
        if c not in GT: GT[c] = {}
        GT[c][a] = 0
z, tc = [0], [0]; src = [*GT['rx']]; H = {i:0 for i in sum([[*GT[i]] for i in src], [])}
def push():
    tc[0] += 1; q = deque([('broadcaster', 0, -1)])
    while q:
        u, p, par = q.popleft() # u receives pulse p from par
        z[0] += complex(1-p, p)
        if u not in T: continue
        if T[u] == 0:
            if not p: S[u] ^= 1; q.extend((v, S[u], u) for v in G[u])
        elif T[u] == 1:
            GT[u][par] = p; n = 1-int(all(GT[u].values())); q.extend((v, n, u) for v in G[u])
            if u in src:
                for k, v in GT[u].items():
                    if v and H[k] == 0: H[k] = tc[0]
        else:
            q.extend((v, p, u) for v in G[u])
for _ in range(1000): push()
print('Part 1:', int(z[0].real*z[0].imag))
while not all(H.values()): push()
print('Part 2:', reduce(lambda x,y: x*y//gcd(x, y), H.values()))