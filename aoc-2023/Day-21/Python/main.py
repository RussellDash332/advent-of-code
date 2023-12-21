import sys
m = [*map(str.strip, sys.stdin)]
K = ((0, -1), (0, 1), (-1, 0), (1, 0))
R = len(m); H = [1]; T = [0, 1]
q = {(R//2, R//2)}; q2 = set(); s = set()
for t in range(3*R):
    for r, c in q:
        s.add((r, c))
        for dr, dc in K:
            x, y = r+dr, c+dc
            if m[x%R][y%R] != '#' and (x, y) not in s: q2.add((x, y))
    q = q2; q2 = set(); T[t%2] += len(q); H.append(T[t%2])
def f(n):
    a, b, c = H[n%R::R]; n //= R; return a+n*(b-a)+n*(n-1)//2*(c-2*b+a)
print('Part 1:', f(64))
print('Part 2:', f(26501365))