import sys
p1 = p2 = 0
for l in sys.stdin:
    gid, c = l.strip().split(': ')
    gid = int(gid.split()[1])
    h = {}
    for i in c.split('; '):
        for j in i.split(', '):
            q, n = j.split()
            if n not in h: h[n] = 0
            h[n] = max(h[n], int(q))
    p1 += gid * (h['blue'] <= 14) * (h['green'] <= 13) * (h['red'] <= 12)
    p2 += h['blue'] * h['green'] * h['red']
print('Part 1:', p1)
print('Part 2:', p2)