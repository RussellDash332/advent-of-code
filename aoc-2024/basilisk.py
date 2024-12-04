# Day 01: 148
a,b=map(sorted,zip(*(map(int,x.split())for x in open(0))));print('Part 1:',sum(abs(x-y)for x,y in zip(a,b)),'\nPart 2:',sum(x*b.count(x)for x in a))
# Day 02: 232
a=[[*map(int,r.split())]for r in open(0)];f=lambda t:sum(any((z:=[*zip(s:=r[:i]+r[i+1:],s[1:])])*(all(0<x-y<4for x,y in z)+all(0<y-x<4for x,y in z))for i in range(len(r)*t,len(r)+1))for r in a);print('Part 1:',f(1),'\nPart 2:',f(0))
# Day 03: 196
import re;t=('do()'+open(0).read()).split("don't()");f=lambda p:sum(int(a)*int(b)for r in t for a,b in re.findall('mul\((\d+),(\d+)\)',r[r.find('do()')*p:]));print('Part 1:',f(0),'\nPart 2:',f(1))
# Day 04: 304
z=range;k=z(-1,2);r=len(m:=[*open(0)]);c=len(m[-1]);print('Part 1:',sum(''.join(m[i//c+t*p][i%c+t*q]for t in z(4))=='XMAS'for i in z(r*c)for p in k for q in k if r>i//c+3*p>-1<i%c+3*q<c),'\nPart 2:',sum(m[i+1][j+1]<'B'!={m[i][j],m[i+2][j+2]}&{m[i+2][j],m[i][j+2]}=={*'MS'}for i in z(r-2)for j in z(c-2)))
# Day 05: