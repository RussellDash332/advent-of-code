import sys
x = 50; p1 = p2 = 0
for i in sys.stdin:
    d, v = -1 if i[0] == 'L' else 1, int(i[1:])
    p2 += v//100; v %= 100
    for _ in '.'*v: x = (x+d)%100; p2 += x == 0
    p1 += x == 0
print('Part 1:', p1)
print('Part 2:', p2)