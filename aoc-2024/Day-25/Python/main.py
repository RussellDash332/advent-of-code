m = open(0).read().split('\n\n')
U = []; L = []; M = len(m[0].split())-1
for g in m:
    g = g.split()
    v = []
    if g[0][0] == '#':
        for i in range(len(g[0])):
            h = 0
            for j in range(1, len(g)):
                if g[j][i] == '#': h += 1
                else: break
            v.append(h)
        L.append(v)
    else:
        for i in range(len(g[0])):
            h = 0
            for j in range(1, len(g)):
                if g[~j][i] == '#': h += 1
                else: break
            v.append(h)
        U.append(v)
Z = 0
for u in U:
    for l in L:
        Z += all(x+y<M for x, y in zip(u, l))
print('Part 1:', Z)
print('Part 2: THE END!')