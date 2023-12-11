import sys

m = [*map(str.strip, sys.stdin)]
def solve(e):
    R, C, G = len(m), len(m[0]), []
    r, c = {*range(R)}, {*range(C)}
    for i in range(R):
        for j in range(C):
            if m[i][j] == '#': r.discard(i), c.discard(j), G.append((i, j))
    p, q = {}, {}; t = u = 0
    for i in range(R):
        if i in r: t += e
        p[i] = i+t
    for i in range(C):
        if i in c: u += e
        q[i] = i+u
    return sum(abs(p[a]-p[c])+abs(q[b]-q[d]) for a,b in G for c,d in G)//2

print('Part 1:', solve(1))
print('Part 2:', solve(10**6-1))