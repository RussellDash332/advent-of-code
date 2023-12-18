import sys

def area(ins):
    sr = sc = pp = 0; m = []
    for d, s in ins: m.append((sr, sc)); dr, dc = k[d]; pp += s; sr += s*dr; sc += s*dc
    return (abs(sum(m[i][0]*m[(i+1)%len(m)][1]-m[i][1]*m[(i+1)%len(m)][0] for i in range(len(m))))+pp+2)//2

k = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}; p = [*k]; a, b = [], []
for l in sys.stdin: d, s, c = l.split(); a.append((d, int(s))), b.append((p[int(c[7])], int(c[2:7], 16)))
print('Part 1:', area(a))
print('Part 2:', area(b))