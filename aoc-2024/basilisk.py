# Day 01: 148
a,b=map(sorted,zip(*(map(int,x.split())for x in open(0))));print('Part 1:',sum(abs(x-y)for x,y in zip(a,b)),'\nPart 2:',sum(x*b.count(x)for x in a))
# Day 02: 232
a=[[*map(int,r.split())]for r in open(0)];f=lambda t:sum(any((z:=[*zip(s:=r[:i]+r[i+1:],s[1:])])*(all(0<x-y<4for x,y in z)+all(0<y-x<4for x,y in z))for i in range(len(r)*t,len(r)+1))for r in a);print('Part 1:',f(1),'\nPart 2:',f(0))
# Day 03: 196
import re;t=('do()'+open(0).read()).split("don't()");f=lambda p:sum(int(a)*int(b)for r in t for a,b in re.findall('mul\((\d+),(\d+)\)',r[r.find('do()')*p:]));print('Part 1:',f(0),'\nPart 2:',f(1))
# Day 04: 304
z=range;k=z(-1,2);r=len(m:=[*open(0)]);c=len(m[-1]);print('Part 1:',sum(''.join(m[i//c+t*p][i%c+t*q]for t in z(4))=='XMAS'for i in z(r*c)for p in k for q in k if r>i//c+3*p>-1<i%c+3*q<c),'\nPart 2:',sum(m[i+1][j+1]<'B'!={m[i][j],m[i+2][j+2]}&{m[i+2][j],m[i][j+2]}=={*'MS'}for i in z(r-2)for j in z(c-2)))
# Day 05: 358
r=range;m=z=s=0;p={};u=p.get;d={0};[len(l)==1and[m:=1]or m and[k:=len(a:=[*map(int,l.split(','))])//2,e:=a[k],c:=1,[a[i]in u(a[j],d)or[c:=0,t:=a[i],f:=a.__setitem__,f(i,a[j]),f(j,t)]for i in r(len(a))for j in r(i)],z:=z+e*c,s:=s+(1-c)*a[k]]or[a:=[*map(int,l.split('|'))],p.__setitem__(a[0],u(a[0],d)|{a[1]})]for l in open(0)];print('Part 1:',z,'\nPart 2:',s)
# Day 06: 452
S=list.__setitem__;r=len(m:=[*map(list,open(X:=0))]);c=len(m[-1]);R=range;[[z:=0,[(T:=m[a])[b]=='^.'[p]and[f:=[*(X:=X or(a,b))],i:=f[0],j:=f[1],S(T,b,'^#'[p]),d:={0},x:=-1,y:=0,l:=0,[(r>i>-1<j<c)*(2-p-l)and[w:=(i,j),[[u:=y,y:=-x,x:=u]for _ in'.'*4if r>i+x>-1<j+y<c!=m[i+x][j+y]<'.'],i:=i+x,j:=j+y,t:=w+(i,j)*p,l:=l|(t in d),d.add(t)]for _ in'.'*r*c],S(T,b,'^.'[p]),z:=z+[len(d)-1,l][p]]for a in R(r)for b in R(c)],print(f'Part {p+1}:',z)]for p in(0,1)]
# Day 07: 