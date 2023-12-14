import sys
m = [*map(list, map(str.strip, sys.stdin))]
def roll(m):
    for c in range(len(m[0])):
        for r in range(len(m)):
            if m[r][c] == 'O':
                while r and m[r-1][c] == '.': m[r-1][c], m[r][c], r = 'O', '.', r-1
    return m
def val(m): return sum((len(m)-i)*m[i].count('O') for i in range(len(m)))
def rot(m): return [[m[i][j] for i in range(len(m)-1, -1, -1)] for j in range(len(m[0]))]
def cyc(m): return [m:=rot(roll(m)) for _ in '.'*4][3]
def enc(m): return ''.join(map(''.join, m))
print('Part 1:', val(roll([i[:] for i in m])))
h, v = {enc(m): 0}, [val(m)]
while (e:=enc(m:=cyc(m))) not in h: h[e] = len(h); v.append(val(m))
print('Part 2:', v[(1000000000-(z:=h[e]))%(len(h)-z)+z])