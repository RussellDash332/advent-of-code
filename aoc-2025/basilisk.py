# Day 01: 145
p=50;q=[[p:=(p+2*(x[0]>'Q')-1)%100for _ in'.'*int(x[1:])]for x in open(0)];print('Part 1:',sum(r[-1]<1for r in q),'\nPart 2:',sum(q,[]).count(0))
# Day 02: 196
import re;v=[[*map(int,l.split('-'))]for l in input().split(',')];f=lambda t:sum(i for a,b in v for i in range(a,b+1)if re.match(rf'^(\d+)\1{t}$',str(i)));print('Part 1:',f(''),'\nPart 2:',f('+'))
# Day 03: 187
from functools import*;f=cache(lambda x,n:max(f(y:=x//10,n),10*f(y,n-1)+x%10)if x*n else 0);v=[*map(int,open(0))];print('Part 1:',sum(f(x,2)for x in v),'\nPart 2:',sum(f(x,12)for x in v))