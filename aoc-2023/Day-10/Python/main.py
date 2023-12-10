import sys; from collections import deque
b = [*map(str.strip, sys.stdin)]; m = [['@']*(2*len(b[0])+1)]; inf = float('inf')
for l in b: m.append([*('@'+'@'.join(l)+'@')]), m.append(['@']*(2*len(b[0])+1))
R, C = len(m), len(m[0])
d = [inf]*R*C
g = [[] for _ in range(R*C)]
q = deque((C*i+j, 0) for i in range(R) for j in range(C) if m[i][j] == 'S')
for r in range(R):
    for c in range(C):
        if m[r][c] in 'S|LJ': g[C*(r-1)+c].append(C*r+c), g[C*r+c].append(C*(r-1)+c)
        if m[r][c] in 'S|7F': g[C*(r+1)+c].append(C*r+c), g[C*r+c].append(C*(r+1)+c)
        if m[r][c] in 'S-LF': g[C*r+c+1].append(C*r+c), g[C*r+c].append(C*r+c+1)
        if m[r][c] in 'S-J7': g[C*r+c-1].append(C*r+c), g[C*r+c].append(C*r+c-1)
while q:
    u, t = q.popleft()
    if d[u] > t:
        d[u] = t; m[u//C][u%C] = '█'
        for v in g[u]: q.append((v, t+1))

print('Part 1:', max(map(lambda x: x if x != inf else -1, d))//2)
k = ((0, -1), (0, 1), (-1, 0), (1, 0)); s = [(0, 0)]
while s:
    r, c = s.pop()
    if d[C*r+c] == inf:
        d[C*r+c] = -1; m[r][c] = ' '
        for dr, dc in k:
            if 0<=r+dr<R and 0<=c+dc<C: s.append((r+dr, c+dc))
print('Part 2:', sum(d[C*r+c]==inf for r in range(1, R, 2) for c in range(1, C, 2)))

# visualize
#for i in m: print(''.join(i))