import re; L = len(M:=[*map(int, re.findall('[-\d]+', open(0).read()))])

R, C = 103, 101; B = (1, -1)
for T in range(R*C):
    G = [['.']*C for _ in range(R)]
    Z = [0]*4
    for i in range(0, L, 4):
        py, px, vy, vx = M[i:i+4]
        x = (px+vx*T)%R; y = (py+vy*T)%C
        G[x][y] = '#'
        if x == R//2 or y == C//2: continue
        Z[(x<R//2)+2*(y<C//2)] += 1
    S = '\n'.join(''.join(r) for r in G)
    t = B[0]
    while '#'*t in S: t += 1
    if t > B[0]: B = (t, T)
    if T == 100: print('Part 1:', Z[0]*Z[1]*Z[2]*Z[3])
print('Part 2:', B[1])