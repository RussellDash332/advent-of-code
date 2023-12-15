def hash(x):
    h = 0
    for i in x: h = (h+ord(i))*17%256
    return h
s = input().split(','); b = [[] for _ in range(256)]; m = {}
for t in s:
    if '=' in t:
        x, f = t.split('='); v, f = hash(x), int(f)
        if x not in m: b[v].append(x)
        m[x] = f
    else:
        x = t[:-1]; v = hash(x)
        if x in m: del m[x]; b[v].remove(x)
print('Part 1:', sum(map(hash, s)))
print('Part 2:', sum((i+1)*(j+1)*m[b[i][j]] for i in range(len(b)) for j in range(len(b[i]))))