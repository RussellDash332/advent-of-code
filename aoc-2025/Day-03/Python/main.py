import sys; from functools import *
@cache
def dp(l, i, n):
    return 0 if i<0 or n<1 else max(10*dp(l, i-1, n-1)+int(l[i]), dp(l, i-1, n))
p1 = p2 = 0
for l in sys.stdin:
    k = len(l:=l.strip())
    p1 += dp(l, k-1, 2)
    p2 += dp(l, k-1, 12)
print('Part 1:', p1)
print('Part 2:', p2)