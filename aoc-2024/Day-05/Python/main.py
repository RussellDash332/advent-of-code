p = q = m = 0; g = {}
for i in open(0):
    if len(i) == 1: m = 1
    elif m:
        x = [*map(int, i.split(','))]; y = [*x]
        for i in range(len(x)):
            for j in range(i):
                if x[j] in g[x[i]]: x[i], x[j] = x[j], x[i]
        p += (x==y)*y[len(x)//2]; q += x[len(x)//2]
    else:
        a, b = map(int, i.split('|'))
        if a not in g: g[a] = set()
        if b not in g: g[b] = set()
        g[a].add(b)
print('Part 1:', p)
print('Part 2:', q-p)