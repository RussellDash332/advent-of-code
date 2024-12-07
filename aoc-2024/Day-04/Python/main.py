m = [*map(str.strip, open(0))]
r = len(m); c = len(m[0])
a = b = 0
for i in range(r):
    for j in range(c):
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if (dr or dc) and r>i+3*dr>-1<j+3*dc<c:
                    a += ''.join(m[i+k*dr][j+k*dc] for k in range(4)) == 'XMAS'
        if i < r-2 and j < c-2 and m[i+1][j+1] == 'A':
            b += {m[i][j], m[i+2][j+2]} == {m[i][j+2], m[i+2][j]} == {'M', 'S'}
print('Part 1:', a)
print('Part 2:', b)