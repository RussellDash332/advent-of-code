m = [*open(0)]

def run(p):
    z = 0
    for l in m:
        t, r = l.split(': '); t = int(t)
        a = [*map(int, r.split())]
        q = [(a[0], 1)]; ok = 0
        while q:
            u, d = q.pop()
            if d == len(a) or u > t:
                if u == t: ok = 1; break
                continue
            q.append((u*a[d], d+1)); q.append((u+a[d], d+1)) or p and q.append((int(f'{u}{a[d]}'), d+1))
        z += ok*t
    return z

print('Part 1:', run(0))
print('Part 2:', run(1))