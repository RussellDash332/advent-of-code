import sys; from heapq import *; from array import *

def dijkstra(lb, ub):
    R = len(m)
    C = len(m[0])
    D = array('i', [10**6]*4*R*C)
    K = ((0, 1), (-1, 0), (0, -1), (1, 0))
    Z = ((1, 3), (0, 2))*2
    X = range(1, ub+1)
    pq = []
    for s in range(4): D[s] = 0; heappush(pq, (0, s))
    while pq:
        dd, tt = heappop(pq)
        r, c, z = tt//(4*C), tt//4%C, tt%4
        if dd != D[tt]: continue
        for i in Z[z]:
            rr, cc = r, c; dr, dc = K[i]; inc = 0
            for k in X:
                rr += dr; cc += dc
                if 0<=rr<R and 0<=cc<C:
                    inc += m[rr][cc]
                    if lb <= k and D[(t:=4*C*rr+4*cc+i)] > (nn:=dd+inc): D[t] = nn; heappush(pq, (nn, t))
                else:
                    break
    return min(D[4*R*C-i-1] for i in range(4))

m = [[*map(int, l.strip())] for l in sys.stdin]
print('Part 1:', dijkstra(1, 3))
print('Part 2:', dijkstra(4, 10))