import sys
t = u = 0
m = dict(zip(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', *map(str, range(1, 10))], [*range(1, 10)]*2))
for l in sys.stdin:
    s = [*map(int, filter(lambda x: x.isnumeric(), l))]
    f = []
    for i in [*m, *map(str, range(10))]:
        f.append((i, l.find(i)))
        if f[-1][1] == -1: f.pop()
        f.append((i, l.rfind(i)))
        if f[-1][1] == -1: f.pop()
    f = sorted({*f}, key=lambda x: x[1])
    t += 10*s[0] + s[-1]
    u += 10*m[f[0][0]] + m[f[-1][0]]
print('Part 1:', t)
print('Part 2:', u)