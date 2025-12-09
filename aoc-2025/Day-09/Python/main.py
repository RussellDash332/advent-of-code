def pip(p):
    z = False; n = len(P)
    for i in range(n):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%n][0]-p[0], P[(i+1)%n][1]-p[1])
        if a[1] > b[1]: a, b = b, a
        if a[1] <= 0 and b[1] > 0 and a[0]*b[1] < a[1]*b[0]: z = not z
        if a[0]*b[1] == a[1]*b[0] and a[0]*b[0]+a[1]*b[1] <= 0: return True
    return z

# ray tracing?
def pip2(p):
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-9: return True
    ray = (p, (p[0]+1e9, p[1]+1e9+7))
    return bool(sum(intersect_check(ray, (poly[i], poly[i+1])) for i in range(len(poly)-1))%2)

def its(s1, s2):
    (p1, p2), (p3, p4) = s1, s2; (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    c1 = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1); c2 = (x2-x1)*(y4-y1)-(y2-y1)*(x4-x1)
    if (c1 <= 0 and c2 <= 0) or (c1 >= 0 and c2 >= 0): return 0
    c1 = (x4-x3)*(y1-y3)-(y4-y3)*(x1-x3); c2 = (x4-x3)*(y2-y3)-(y4-y3)*(x2-x3)
    if (c1 <= 0 and c2 <= 0) or (c1 >= 0 and c2 >= 0): return 0
    return 1

P = [[*map(int, l.split(','))] for l in open(0)]
print('Part 1:', max(-~abs(c-a)*-~abs(d-b) for a,b in P for c,d in P))
Z = 0
for a,b in P:
    for c,d in P:
        if -~abs(c-a)*-~abs(d-b) <= Z: continue
        bad = 0
        for s in (((a, b), (a, d)), ((a, d), (c, d)), ((c, d), (c, b)), ((c, b), (a, b))):
            if not pip(s[0]) or not pip(s[1]): # check if the midpoint is also outside the polygon to be more accurate, but I think this will work for the input shape
                bad = 1; break
            for i in range(len(P)):
                if its(s, (P[i], P[i-1])):
                    bad = 1; break
            if bad: break
        if not bad:
            Z = -~abs(c-a)*-~abs(d-b)
print('Part 2:', Z)