# Day 01: 148
a,b=map(sorted,zip(*(map(int,x.split())for x in open(0))));print('Part 1:',sum(abs(x-y)for x,y in zip(a,b)),'\nPart 2:',sum(x*b.count(x)for x in a))
# Day 02: 232
a=[[*map(int,r.split())]for r in open(0)];f=lambda t:sum(any((z:=[*zip(s:=r[:i]+r[i+1:],s[1:])])*(all(0<x-y<4for x,y in z)+all(0<y-x<4for x,y in z))for i in range(len(r)*t,len(r)+1))for r in a);print('Part 1:',f(1),'\nPart 2:',f(0))
# Day 03: 196
import re;t=('do()'+open(0).read()).split("don't()");f=lambda p:sum(int(a)*int(b)for r in t for a,b in re.findall('mul\((\d+),(\d+)\)',r[r.find('do()')*p:]));print('Part 1:',f(0),'\nPart 2:',f(1))
# Day 04: 304
z=range;k=z(-1,2);r=len(m:=[*open(0)]);c=len(m[-1]);print('Part 1:',sum(''.join(m[i//c+t*p][i%c+t*q]for t in z(4))=='XMAS'for i in z(r*c)for p in k for q in k if r>i//c+3*p>-1<i%c+3*q<c),'\nPart 2:',sum(m[i+1][j+1]<'B'!={m[i][j],m[i+2][j+2]}&{m[i+2][j],m[i][j+2]}=={*'MS'}for i in z(r-2)for j in z(c-2)))
# Day 05: 351
r=range;m=z=s=0;p={};u=p.get;d={0};[len(l)==1and[m:=1]or m and[k:=len(a:=[*map(int,l.split(','))])//2,e:=a[k],c:=1,[a[i]in u(a[j],d)or[c:=0,t:=a[i],f:=a.__setitem__,f(i,a[j]),f(j,t)]for i in r(len(a))for j in r(i)],z:=z+e*c,s:=s+a[k]]or[a:=[*map(int,l.split('|'))],p.update({a[0]:u(a[0],d)|{a[1]}})]for l in open(0)];print('Part 1:',z,'\nPart 2:',s-z)
# Day 06: 430
S=list.__setitem__;r=len(m:=[*map(list,open(0))]);c=len(m[-1]);X=max(R:=range(r*c),key=lambda x:m[x//c][x%c]);s=lambda p:[d:={(a:=X//c,b:=X%c)},v:=-1,w:=0,l:=0,[~-l*(r>a>-1<b<c)and[[[t:=v,v:=w,w:=-t]for _ in'.'*4if r>a+v>-1<b+w<c!='.'>m[a+v][b+w]],l:=l|((t:=(a,b,a:=a+v,b:=b+w))in d),d.add(t)]for _ in R],[d,l][p]][5];print('Part 1:',len(D:={u[:2]for u in s(0)}),'\nPart 2:',sum([S(m[a],b,'#'),s(1),S(m[a],b,'.')][1]for a,b in D))
# Day 07: 265
m=[*open(0)];f=lambda i,c,k,t,p:f(i+1,c+k[i],k,t,p)or f(i+1,c*k[i],k,t,p)or~-p*f(i+1,int(f'{c}{k[i]}'),k,t,p)if i-len(k)else c==t;z=lambda p:print(f'Part {p}:',sum([u:=l.split(':'),t:=int(u[0]),k:=[*map(int,u[1].split())],t*f(1,k[0],k,t,p)][3]for l in m));z(1);z(2)
# Day 08: 385
import math;Z=range;R=len(m:=[*open(0)]);C=len(m[-1]);N={};A=set();B=set();[[(x:=m[i][j])>'.'!=N.update({x:N.get(x,[])+[(i,j)]})]for i in Z(R)for j in Z(C)];[[g:=math.gcd(x,y),x:=x//g,y:=y//g,e:=c,f:=d,[[B.add(t:=(e:=e+x,f:=f+y)),k==1!=A.add(t)]for k in Z(R+C)if R>e+x>-1<f+y<C]]for i in N for a,b in N[i]for c,d in N[i]if(x:=a-c)*C+(y:=b-d)];print('Part 1:',len(A),'\nPart 2:',len(B))
# Day 09: 439
P=-1;s=[*map(int,input())];Z=range;G=enumerate;f=lambda t:[d:=0,q:=sum((j*[[i//2,P][i%2]]for i,j in G(s)),[]),r:={j:i for i,j in G(q)},a:=q.__setitem__,[[m:=t or s[2*i]]+[[q[P]<0>q.pop()for _ in Z(9)]+[k:=r[i],l:=0,[[[[a(k-m+1+j,P),a(p+j,i),r.update({i:r[i]-1}),d:=p]for j in Z(m)],l:=P]for p in Z(d*t,r[i])if[P]*m==q[p:p+m]and~l]]for _ in Z(s[2*i]//m)]for i in Z(max(q),P,P)],print(f'Part {2-t}:',sum(i*j*(j>P)for i,j in G(q)))];f(1);f(0)
# Day 10: 557
E=list.append;S=list.__setitem__;R=len(m:=[*open(0)]);C=len(m[-1]);Z=range(N:=R*C);G=[[]for _ in Z];I=[0]*N;T=[];[[r:=i//C,c:=i%C,R>r+p>-1<c+q<C and 1+int(m[r][c])==int(m[r+p][c+q])!=[E(G[i],j:=(r+p)*C+c+q),S(I,j,I[j]+1)]]for i in Z for p,q in((-1,0),(0,-1),(0,1),(1,0))];Q=[i for i in Z if I[i]<1];[E(T,u)or[[S(I,v,I[v]-1),I[v]<1!=E(Q,v)]for v in G[u]]for u in Q];[print(f'Part {p+1}:',sum([D:=[0]*N,S(D,x,1),[S(D,u,D[u]+D[v])for u in T[::-1]for v in G[u]],sum([D[i]>0,D[i]][p]for i in Z if'1'>m[i//C][i%C])][3]for x in Z if'8'<m[x//C][x%C]))for p in(0,1)]
# Day 11: 240
m=input().split();h={};f=lambda x,d:d<1or h.get(t:=(x,d))or[v:=~-d,p:=10**((k:=len(str(x)))//2),h.update({t:[k&1and f(2024*x,v)or f(x//p,v)+f(x%p,v),f(1,v)][x<1]}),h[t]][3];[print(f'Part {p}:',sum(f(int(i),50*p-25)for i in m))for p in(1,2)]