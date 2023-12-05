s = [*map(int, input().split(':')[1].split())]; input()
s2 = sorted((s[2*i], s[2*i]+s[2*i+1]-1) for i in range(len(s)//2))
s = [(i, i) for i in s]

def merge(intervals):
    h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else(min(a[0],b[0]),max(a[1],b[1]))
    return [r:=[],[[r.pop(),r.append(k)]if r and(k:=h(r[-1],j))else r.append(j)for j in sorted(intervals)]][0]

def convert(s):
    s2 = []
    for a, b in s:
        u = []
        for p, q, r in d:
            if b < q or a > q+r-1: continue
            t = p-q; s2.append((max(a, q)+t, min(b, q+r-1)+t)), u.append((max(a, q), min(b+1, q+r)))
        if not u: s2.append((a, b)), u.append((a, b+1))
        s2.append((a, u[0][0]-1)), u.insert(0, (a, u[0][0]))
        s2.append((u[-1][1], b)), u.append((u[-1][1], b+1))
        for i in range(len(u)-1): s2.append((u[i][1], u[i+1][0]-1)), u.append((u[i][1], u[i+1][0]))
        assert merge(u) == [(a, b+1)]
    return [(a, b-1) for a, b in merge((a, b+1) for a, b in s2 if a <= b)]

while True:
    try: c = input().split()[0]; d = []
    except: break
    while True:
        try: e = [*map(int, input().split())]
        except: e = []
        if not e: break
        d.append(e)
    d.sort(key=lambda x: x[1]); s = convert(s); s2 = convert(s2)
print('Part 1:', s[0][0])
print('Part 2:', s2[0][0])