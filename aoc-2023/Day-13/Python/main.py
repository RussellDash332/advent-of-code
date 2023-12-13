def solve(g, d):
    for i in range(1, len(g[0])):
        if sum(sum(a!=b for a,b in zip(r[i-1::-1], r[i:])) for r in g) == d: return i
    return 0

import sys
a = b = 0
for l in ''.join(sys.stdin).replace('\r', '').split('\n\n'):
    g = l.split('\n'); h = [*zip(*g)]
    a += solve(g, 0) + 100*solve(h, 0)
    b += solve(g, 1) + 100*solve(h, 1)
print('Part 1:', a)
print('Part 2:', b)