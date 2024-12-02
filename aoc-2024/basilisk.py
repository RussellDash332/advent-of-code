# Day 01: 148
a,b=map(sorted,zip(*(map(int,x.split())for x in open(0))));print('Part 1:',sum(abs(x-y)for x,y in zip(a,b)),'\nPart 2:',sum(x*b.count(x)for x in a))
# Day 02: 232
a=[[*map(int,r.split())]for r in open(0)];f=lambda t:sum(any((z:=[*zip(s:=r[:i]+r[i+1:],s[1:])])*(all(0<x-y<4for x,y in z)+all(0<y-x<4for x,y in z))for i in range(len(r)*t,len(r)+1))for r in a);print('Part 1:',f(1),'\nPart 2:',f(0))
# Day 03: 