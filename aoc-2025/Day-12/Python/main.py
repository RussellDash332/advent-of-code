*p, v = open(0).read().split('\n\n')
Q = []
for i in range(len(p)):
    _, *m = p[i].split()
    Q.append(sum(r.count('#') for r in m))
Z = 0
for k in v.split('\n'):
    R, C, *q = [*map(int, k[:(t:=k.find(':'))].split('x')+k[t+1:].split())]
    Z += R*C >= sum(Q[i]*v for i,v in enumerate(q))
print('Part 1:', Z)
print('Part 2: THE END!')