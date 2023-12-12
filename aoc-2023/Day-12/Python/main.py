import sys

def solve(l, p):
    m = {}
    def f(i, j, c):
        k = (i, j, c)
        if k in m: return m[k]
        if i==len(l): return (c==p[-1] and j==len(p)-1)|(c==0 and j==len(p))
        r = 0
        if l[i] in '?#': r += f(i+1, j, c+1)
        if l[i] in '?.':
            if c == 0: r += f(i+1, j, 0)
            elif c > 0 and j < len(p) and p[j] == c: r += f(i+1, j+1, 0)
        m[k] = r; return r
    return f(0, 0, 0)

a = b = 0
for l in sys.stdin:
    l, p = l.split(); p = [*map(int, p.split(','))]
    a += solve(l, p); b += solve('?'.join(5*[l]), 5*p)
print('Part 1:', a)
print('Part 2:', b)