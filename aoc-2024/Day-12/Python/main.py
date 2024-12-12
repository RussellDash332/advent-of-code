m = ['@'+l.strip()+'@' for l in open(0)]; C = len(m[0]); m = ['@'*C]+m+['@'*C]; R = len(m); V = [0]*R*C; Z = Z2 = 0
for i in range(1, R-1):
    for j in range(1, C-1):
        Q = [(i, j)]; A = P = 0; S = set(); E = 0
        for r, c in Q:
            if V[r*C+c]: continue
            V[r*C+c] = 1; A += 1
            for k, (dr, dc, t) in enumerate(((-1, 0, r), (0, -1, c), (0, 1, c), (1, 0, r))):
                if m[r][c]==m[r+dr][c+dc]: Q.append((r+dr, c+dc))
                else: P += 1; S.add((k, t, r, c))
        p = [-1]*3
        for t in sorted(S):
            E += t[:2] != p[:2] or abs(t[2]-p[2])+abs(t[3]-p[3]) != 1
            p = t
        Z += A*P; Z2 += A*E
print('Part 1:', Z, '\nPart 2:', Z2)