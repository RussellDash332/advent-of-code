A, B = [], []
for x in open(0):
    a, b = map(int, x.split())
    A.append(a), B.append(b)
A.sort(), B.sort()
print('Part 1:', sum(abs(x-y) for x,y in zip(A, B)))
print('Part 2:', sum(x*B.count(x) for x in A))