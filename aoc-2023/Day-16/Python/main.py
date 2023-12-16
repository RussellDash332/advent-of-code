import sys
m = [*map(str.strip, sys.stdin)]; b = []
for i in range(R:=len(m)): b.extend(((i, 0, 0), (i, (C:=len(m[0]))-1, 2)))
for i in range(C): b.extend(((0, i, 3), (R-1, i, 1)))
K = ((0, 1), (-1, 0), (0, -1), (1, 0)); m = ''.join(map(''.join, m))

def simulate(t):
    s = [t]; e = [0]*R*C; v = [0]*4*R*C
    while s:
        r, c, z = s.pop()
        if 0<=r<R and 0<=c<C and v[(k:=4*r*C+4*c+z)]==0:
            v[k] = e[k//4] = 1; x = m[k//4]
            if x == '|' and z%2==0: s.extend(((r-1, c, 1), (r+1, c, 3)))
            elif x == '-' and z%2: s.extend(((r, c-1, 2), (r, c+1, 0)))
            elif x == '\\': dr, dc = K[z^3]; s.append((r+dr, c+dc, z^3))
            elif x == '/': dr, dc = K[z^1]; s.append((r+dr, c+dc, z^1))
            else: dr, dc = K[z]; s.append((r+dr, c+dc, z))
    return sum(e)
print('Part 1:', simulate((0, 0, 0)))
print('Part 2:', max(map(simulate, b)))