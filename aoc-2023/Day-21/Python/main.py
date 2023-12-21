import sys
m = [*map(str.strip, sys.stdin)]
K = ((0, -1), (0, 1), (-1, 0), (1, 0))
R = len(m); H = [1]; q = {(R//2, R//2)}; q2 = set()

# LOL
assert R == len(m[0]) and m[R//2][R//2] == 'S'

for _ in range(3*R):
    for r, c in q:
        for dr, dc in K:
            x, y = r+dr, c+dc
            if m[x%R][y%R] != '#': q2.add((x, y))
    q = q2; q2 = set(); H.append(len(q))
def f(n):
    a, b, c = H[n%R::R]; n //= R; return a+n*(b-a)+n*(n-1)//2*(c-2*b+a)
print('Part 1:', H[64])
print('Part 2:', f(26501365))