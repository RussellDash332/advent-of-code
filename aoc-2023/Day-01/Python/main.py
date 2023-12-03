import sys
t = u = 0
m = dict(zip(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', *map(str, range(1, 10))], [*range(1, 10)]*2))
n = [*m, *map(str, range(10))]
for l in sys.stdin:
    s = [*map(int, filter(lambda x: x.isnumeric(), l))]
    t += 10*s[0] + s[-1]
    f = sorted(filter(lambda x: x[1]+1, {*((i, t(i)) for i in n for t in (l.find, l.rfind))}), key=lambda x: x[1])
    u += 10*m[f[0][0]] + m[f[-1][0]]
print('Part 1:', t)
print('Part 2:', u)