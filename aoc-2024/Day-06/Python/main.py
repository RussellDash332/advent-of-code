m = [[*i] for i in open(0)]; r = len(m); c = len(m[-1])

for i in range(r):
    for j in range(c):
        if m[i][j] == '^': sr, sc = X = i, j

d = []; e = []; dr, dc = -1, 0
while r>sr>-1<sc<c:
    while r>sr+dr>-1<sc+dc<c and m[sr+dr][sc+dc] == '#': dr, dc = dc, -dr
    d.append((sr, sc, sr:=sr+dr, sc:=sc+dc))
print('Part 1:', len({*(s[:2]for s in d)}))

def simulate(sr, sc):
    d = set(); dr, dc = -1, 0
    while r>sr>-1<sc<c:
        while r>sr+dr>-1<sc+dc<c and m[sr+dr][sc+dc] == '#': dr, dc = dc, -dr
        t = (sr, sc, sr:=sr+dr, sc:=sc+dc)
        if t in d: return 1
        d.add(t)

z = set()
for *_, k, l in d[:-1]:
    m[k][l] = '#'
    simulate(*X) and z.add((k, l))
    m[k][l] = '.'
print('Part 2:', len(z))