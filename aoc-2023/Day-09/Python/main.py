import sys
s = t = 0
def extrapolate(l):
    l = [l]
    for _ in l[0]: l.append([b-a for a,b in zip(l[-1], l[-1][1:])])
    l[-1].append(0)
    for i in range(1, len(l)): l[-1-i].append(l[-1-i][-1]+l[-i][-1])
    return l[0][-1]
for l in sys.stdin:
    l = [*map(int, l.split())]
    s += extrapolate(l)
    t += extrapolate(l[::-1])
print('Part 1:', s)
print('Part 2:', t)