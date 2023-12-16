import sys; from collections import deque
m = [*map(str.strip, sys.stdin)]; b = []
for i in range(len(m)): b.extend(((i, 0, 0, 1), (i, len(m[0])-1, 0, -1)))
for i in range(len(m[0])): b.extend(((0, i, 1, 0), (len(m)-1, i, -1, 0)))

def simulate(t):
    q = deque([t])
    e = [[0]*len(i) for i in m]
    seen = set()
    while q:
        r, c, dr, dc = q.popleft()
        if not (0<=r<len(m) and 0<=c<len(m[0])): continue
        if (tup:=(r, c, dr, dc)) in seen: continue
        seen.add(tup)
        e[r][c] += 1
        if m[r][c] == '.': q.append((r+dr, c+dc, dr, dc))
        elif m[r][c] == '|':
            if dr == 0: q.append((r-1, c, -1, 0)), q.append((r+1, c, 1, 0))
            else: q.append((r+dr, c+dc, dr, dc))
        elif m[r][c] == '/':
            if dr == 0: q.append((r-dc, c, -dc, 0))
            else: q.append((r, c-dr, 0, -dr))
        elif m[r][c] == '-':
            if dc == 0: q.append((r, c-1, 0, -1)), q.append((r, c+1, 0, 1))
            else: q.append((r+dr, c+dc, dr, dc))
        else: # \
            if dr == 0: q.append((r+dc, c, dc, 0))
            else: q.append((r, c+dr, 0, dr))
    return sum(map(lambda x: sum(map(bool, x)), e))
print('Part 1:', simulate((0, 0, 0, 1)))
print('Part 2:', max(map(simulate, b)))