import sys
c = []
for l in sys.stdin:
    a, b = l.split('|')
    c.append(len({*map(int, b.split())}&{*map(int, a.split(': ')[1].split())}))
d = [1]*len(c)
for i in range(len(c)):
    for j in range(c[i]): d[i+j+1] += d[i]
print('Part 1:', sum(2**(s-1) if s else 0 for s in c))
print('Part 2:', sum(d))