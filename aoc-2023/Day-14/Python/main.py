import sys; from copy import deepcopy
m = [*map(list, map(str.strip, sys.stdin))]
def val(m):
    return sum((len(m)-i)*m[i].count('O') for i in range(len(m)))
def rot(m):
    return [[m[i][j] for i in range(len(m)-1, -1, -1)] for j in range(len(m[0]))]
def roll(m):
    for c in range(len(m[0])):
        for r in range(len(m)):
            if m[r][c] == 'O':
                while r and m[r-1][c] == '.': m[r-1][c], m[r][c] = 'O.'; r -= 1
    return m
def cyc(m):
    return [m:=rot(roll(m)) for _ in range(4)][3]
print('Part 1:', val(roll(deepcopy(m))))
h = [deepcopy(m)]
while (m:=cyc(m)) not in h: h.append(deepcopy(m))
print('Part 2:', val(h[(1000000000-(z:=h.index(m)))%(len(h)-z)+z]))