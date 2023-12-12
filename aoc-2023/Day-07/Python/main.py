import sys; from collections import *
m = dict(zip('TJQKA', ':;<=>'))
r = lambda f: [max(f), -len(f)]
d = [*map(str.split, sys.stdin)]
def solve(t):
    sd = sorted(d, key=lambda c: max(r(Counter(c[0].replace(t, i)).values()) for i in c[0])+[m.get(i, i) for i in c[0]])
    return sum((i+1)*int(e[1]) for i,e in enumerate(sd))
print('Part 1:', solve('@'))
m['J'] = '1'; print('Part 2:', solve('J'))