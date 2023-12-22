import sys, re, itertools

# [-\d+] -> \d+ because there doesn't seem to be any negative number
# min(x[2],x[5]) -> x[2] because L < R
# range(min(a,b), max(a,b)+1) -> range(a,b+1) because of the above assumption

B = {}; S = sorted(([*map(int, re.findall('\d+',l))] for l in sys.stdin), key=lambda x: x[2])
M = len(S); I = [0]*M

# list cubes
def lc(x1, y1, z1, x2, y2, z2):
    return itertools.product(range(x1, x2+1), range(y1, y2+1), range(z1, z2+1))

# count falls
def cf(i):
    J = [*I]; s = [i]; d = -1
    for u in s:
        d += 1
        for v in G[u]:
            J[v] -= 1
            if J[v] == 0: s.append(v)
    return d

# simulate dropping
for i, j in enumerate(S):
    while j[2]:
        j[2] -= 1; j[5] -= 1
        if any(t in B and B[t] != i for t in lc(*j)): j[2] += 1; j[5] += 1; break
    for t in lc(*j): B[t] = i

# connect supports
G = []
for i in range(M):
    G.append({B[j] for *xy,z in lc(*S[i]) if (j:=(*xy,z+1)) in B and B[j] != i})
    for j in G[i]: I[j] += 1

print('Part 1:', sum(all(I[j]-1 for j in v) for v in G))
print('Part 2:', sum(map(cf, range(M))))