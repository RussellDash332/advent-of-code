import math
l = [input().split()[1:] for _ in '..']
g = lambda a,b: a-1-2*int((a-(a*a-4*b)**0.5)/2)
print('Part 1:', math.prod(g(*map(int,i)) for i in zip(*l)))
print('Part 2:', g(*map(int,map(''.join, l))))