a = b = 0
for r in open(0):
    r = [*map(int, r.split())]; k = 0
    for i in range(len(r)+1):
        s = r[:i] + r[i+1:]
        z = [*zip(s, s[1:])]
        if all(0<x-y<4 for x,y in z) or all(0<y-x<4 for x,y in z): a += i==len(r); k = 1
    b += k
print('Part 1:', a)
print('Part 2:', b)