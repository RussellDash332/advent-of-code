# Day 01: 148
a,b=map(sorted,zip(*(map(int,x.split())for x in open(0))));print('Part 1:',sum(abs(x-y)for x,y in zip(a,b)),'\nPart 2:',sum(x*b.count(x)for x in a))
# Day 02: 232
a=[[*map(int,r.split())]for r in open(0)];f=lambda t:sum(any((z:=[*zip(s:=r[:i]+r[i+1:],s[1:])])*(all(0<x-y<4for x,y in z)+all(0<y-x<4for x,y in z))for i in range(len(r)*t,len(r)+1))for r in a);print('Part 1:',f(1),'\nPart 2:',f(0))
# Day 03: 196
import re;t=('do()'+open(0).read()).split("don't()");f=lambda p:sum(int(a)*int(b)for r in t for a,b in re.findall('mul\((\d+),(\d+)\)',r[r.find('do()')*p:]));print('Part 1:',f(0),'\nPart 2:',f(1))
# Day 04: 304
z=range;k=z(-1,2);r=len(m:=[*open(0)]);c=len(m[-1]);print('Part 1:',sum(''.join(m[i//c+t*p][i%c+t*q]for t in z(4))=='XMAS'for i in z(r*c)for p in k for q in k if r>i//c+3*p>-1<i%c+3*q<c),'\nPart 2:',sum(m[i+1][j+1]<'B'!={m[i][j],m[i+2][j+2]}&{m[i+2][j],m[i][j+2]}=={*'MS'}for i in z(r-2)for j in z(c-2)))
# Day 05: 354
r=range;m=z=s=0;p={};u=p.get;d={0};[len(l)==1and[m:=1]or m and[k:=len(a:=[*map(int,l.split(','))])//2,e:=a[k],c:=1,[a[i]in u(a[j],d)or[c:=0,t:=a[i],f:=a.__setitem__,f(i,a[j]),f(j,t)]for i in r(len(a))for j in r(i)],z:=z+e*c,s:=s+a[k]]or[a:=[*map(int,l.split('|'))],p.__setitem__(a[0],u(a[0],d)|{a[1]})]for l in open(0)];print('Part 1:',z,'\nPart 2:',s-z)
# Day 06: 430
S=list.__setitem__;r=len(m:=[*map(list,open(0))]);c=len(m[-1]);X=max(R:=range(r*c),key=lambda x:m[x//c][x%c]);s=lambda p:[d:={(a:=X//c,b:=X%c)},v:=-1,w:=0,l:=0,[~-l*(r>a>-1<b<c)and[[[t:=v,v:=w,w:=-t]for _ in'.'*4if r>a+v>-1<b+w<c!='.'>m[a+v][b+w]],l:=l|((t:=(a,b,a:=a+v,b:=b+w))in d),d.add(t)]for _ in R],[d,l][p]][5];print('Part 1:',len(D:={u[:2]for u in s(0)}),'\nPart 2:',sum([S(m[a],b,'#'),s(1),S(m[a],b,'.')][1]for a,b in D))
# Day 07: 265
m=[*open(0)];f=lambda i,c,k,t,p:f(i+1,c+k[i],k,t,p)or f(i+1,c*k[i],k,t,p)or~-p*f(i+1,int(f'{c}{k[i]}'),k,t,p)if i-len(k)else c==t;z=lambda p:print(f'Part {p}:',sum([u:=l.split(':'),t:=int(u[0]),k:=[*map(int,u[1].split())],t*f(1,k[0],k,t,p)][3]for l in m));z(1);z(2)
# Day 08: 388
import math;Z=range;R=len(m:=[*open(0)]);C=len(m[-1]);N={};A=set();B=set();[[(x:=m[i][j])>'.'!=N.__setitem__(x,N.get(x,[])+[(i,j)])]for i in Z(R)for j in Z(C)];[[g:=math.gcd(x,y),x:=x//g,y:=y//g,e:=c,f:=d,[[B.add(t:=(e:=e+x,f:=f+y)),k==1!=A.add(t)]for k in Z(R+C)if R>e+x>-1<f+y<C]]for i in N for a,b in N[i]for c,d in N[i]if(x:=a-c)*C+(y:=b-d)];print('Part 1:',len(A),'\nPart 2:',len(B))