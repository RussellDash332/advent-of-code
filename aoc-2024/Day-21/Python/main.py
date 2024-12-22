from functools import *; from itertools import *
N = '789456123X0A'; D = 'X^A<v>'; RN = {e:i for i,e in enumerate(N)}; RD = {e:i for i,e in enumerate(D)}
K = dict(zip('<v^>',((0,-1),(1,0),(-1,0),(0,1))))
A = {}; B = {}

for (E, F, R) in ((A, D, 2), (B, N, 4)):
    for ri in range(R):
        for ci in range(3):
            if F[3*ri+ci] == 'X': continue
            for rj in range(R):
                for cj in range(3):
                    if F[3*rj+cj] == 'X': continue
                    if cj>=ci: p = '>'*(cj-ci)
                    else: p = '<'*(ci-cj)
                    if rj>=ri: p += 'v'*(rj-ri)
                    else: p += '^'*(ri-rj)
                    E[F[3*ri+ci]+F[3*rj+cj]] = p

@lru_cache
def f(s, n, t=0):
    if n == 0: return len(s)
    s = 'A'+s; z = 0
    for i in range(len(s)-1):
        P = []; x = (B, A)[t][s[i]+s[i+1]]; r, c = divmod((RN, RD)[t][s[i]], 3)
        for p in {*permutations(x)}:
            rr, cc = r, c; ok = 1
            for q in p:
                dr, dc = K[q]; rr += dr; cc += dc
                if not 4-2*t>rr>-1<cc<3 or (N, D)[t][3*rr+cc] == 'X': ok = 0; break
            if ok: P.append(''.join(p))
        z += min(f(p+'A', n-1, 1) for p in P)
    return z

Z = [0, 0]
for s in open(0):
    s = s.strip(); k = int(''.join(x for x in s if '/'<x<':'))
    for p in range(2): Z[p] += k*f(s, 3+23*p)
print('Part 1:', Z[0], '\nPart 2:', Z[1])