import sys
m = [[*l.strip()] for l in sys.stdin]
r = len(m); c = len(m[0])
p1 = p2 = 0
while 1:
    bef = p2; M = []
    for i in range(r):
        for j in range(c):
            z = 0
            if m[i][j] == '.': continue
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if r>i+di>-1<j+dj<c: z += m[i+di][j+dj] == '@'
            if z<5: M += [(i, j)]; p2 += 1
    for i, j in M: m[i][j] = '.'
    p1 = p1 or len(M)
    if p2 == bef: break
print('Part 1:', p1)
print('Part 2:', p2)