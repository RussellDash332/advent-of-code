import sys, re, itertools
B = {}; S = sorted([[*map(int, re.findall('[-\d]+', l))] for l in sys.stdin], key=lambda x: min(x[2],x[5]))
G = [set() for _ in S]; M = len(S); I = [0]*M

# list cubes
def lc(x1, y1, z1, x2, y2, z2):
    return itertools.product(range(min(x1,x2), max(x1,x2)+1), range(min(y1,y2), max(y1,y2)+1), range(min(z1,z2), max(z1,z2)+1))

# count falls
def cf(i):
    J = I.copy(); s = [i]; d = {i}
    while s:
        d.add(u:=s.pop())
        for v in G[u]:
            J[v] -= 1
            if J[v] == 0: s.append(v)
    return len(d)-1

# simulate dropping
for i, j in enumerate(S):
    while j[2]*j[5]:
        j[2] -= 1; j[5] -= 1
        if any(B.get(t,i)-i for t in lc(*j)): j[2] += 1; j[5] += 1; break
    for t in lc(*j): B[t] = i

# connect supports
for i in range(M):
    for x,y,z in lc(*S[i]):
        if B.get(j:=(x,y,z+1),i)-i: G[i].add(B[j])
    for j in G[i]: I[j] += 1

print('Part 1:', sum(all(I[j]-1 for j in v) for v in G))
print('Part 2:', sum(map(cf, range(M))))