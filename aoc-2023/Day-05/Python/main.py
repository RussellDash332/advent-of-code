def convert(s):
    s2 = []
    for a, b in s:
        u = []
        for p, q, r in d:
            if b < q or a > q+r-1: continue
            t = p-q; s2.append((max(a, q)+t, min(b, q+r-1)+t)), u.append((max(a, q), min(b, q+r-1)))
        if not u: s2.append((a, b)), u.append((a, b))
        s2.append((a, u[0][0]-1)), u.insert(0, (a, u[0][0]-1)), s2.append((u[-1][1]+1, b)), u.append((u[-1][1]+1, b))
        for i in range(len(u)-1): s2.append((u[i][1]+1, u[i+1][0]-1)), u.append((u[i][1]+1, u[i+1][0]-1))
    return [(a, b) for a, b in s2 if a <= b]

s = [*map(lambda x: [int(x)]*2, input().split(':')[1].split())]; input()
s2 = sorted([s[2*i][0], s[2*i][0]+s[2*i+1][0]-1] for i in range(len(s)//2))
while True:
    try: c = input().split()[0]; d = []
    except: break
    while True:
        try: e = [*map(int, input().split())]
        except: e = []
        if not e: break
        d.append(e)
    d.sort(key=lambda x: x[1]); s = convert(s); s2 = convert(s2)
print('Part 1:', min(s)[0])
print('Part 2:', min(s2)[0])