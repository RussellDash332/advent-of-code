import sys

def solve(l, p):
    q = len(p); L = len(l); m = {}
    def f(i, j, c):
        if i==L: return (c==0 and j==q)or(c==p[-1] and j==q-1)
        k = (i, j, c)
        if k in m: return m[k]
        r = 0
        if l[i] > '#':
            if c == 0: r += f(i+1, j, 0)
            elif j < q and p[j] == c: r += f(i+1, j+1, 0)
        if l[i] != '.': r += f(i+1, j, c+1)
        m[k] = r; return r
    return complex(f(0, 0, 0), m[(4*L//5+1, 4*q//5, 0)])

a = 0
for l in sys.stdin:
    l, p = l.split()
    a += solve('?'.join(5*[l]), 5*[*map(int, p.split(','))])
print('Part 1:', int(a.imag))
print('Part 2:', int(a.real))