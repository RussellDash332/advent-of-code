p1 = p2 = 0
for s in input().split(','):
    a, b = map(int, s.split('-'))
    for i in range(a, b+1):
        k = len(s:=str(i))
        for l in range(2, k+1):
            if s[:k//l]*l == s: p1 += i*(l==2); p2 += i; break
print('Part 1:', p1)
print('Part 2:', p2)