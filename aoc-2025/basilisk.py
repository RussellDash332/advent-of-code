# Day 01: 142
p=50;q=[[p:=(p+2*(x>'Q')-1)%100for _ in'.'*int(x[1:])]for x in open(0)];print('Part 1:',sum(r[-1]<1for r in q),'\nPart 2:',sum(q,[]).count(0))
# Day 02: 196
import re;v=[[*map(int,l.split('-'))]for l in input().split(',')];f=lambda t:sum(i for a,b in v for i in range(a,b+1)if re.match(rf'^(\d+)\1{t}$',str(i)));print('Part 1:',f(''),'\nPart 2:',f('+'))
# Day 03: 187
from functools import*;f=cache(lambda x,n:max(f(y:=x//10,n),10*f(y,n-1)+x%10)if x*n else 0);v=[*map(int,open(0))];print('Part 1:',sum(f(x,2)for x in v),'\nPart 2:',sum(f(x,12)for x in v))
# Day 04: 299
R=range;r=len(m:=[*map(list,open(0))]);c=len(m[0])-1;P=[0];[[q:=len(M:=[(i,j)for i in R(r)for j in R(c)if'.'<m[i][j]!=sum(r>i+x>-1<j+y<c!=m[i+x][j+y]>'.'for x in R(-1,2)for y in R(-1,2))<5]),[m[i].__setitem__(j,'.')for i,j in M],q and P.append(q)]for p in P];print('Part 1:',P[1],'\nPart 2:',sum(P))
# Day 05: 295
S,M=str.split,[];A,B=S(open(0).read(),'\n\n');[M.append(M and(a:=M[-1])[1]>=j[0]<=j[1]>=a[0]and[M.pop(),min(a[0],j[0]),max(a[1],j[1])][1:]or j)for j in sorted([*map(int,S(i,'-'))]for i in S(A))];print('Part 1:',sum(any(a<=int(q)<b+1for a,b in M)for q in S(B)),'\nPart 2:',sum(b-a+1for a,b in M))
# Day 06: 226
*X,P=open(0);P=P.split();A=[*zip(*map(str.split,X))];B=[''.join(x).strip()for x in zip(*X)];print('Part 1:',sum(eval(p.join(x))for x,p in zip(A,P)),'\nPart 2:',sum([eval(p.join(B[:(x:=B.index(''))])),B:=B[x+1:]][0]for p in P))
# Day 07: 205
L,*M=open(0);Q={L.index('S'):1};print('Part 1:',sum([[T:={},sum([x:=r[k]>'S',T:=T|{k-x:T.get(k-x,0)+Q[k],k+x:T.get(k+x,0)+Q[k]}][0]for k in Q),Q:=T][1]for i,r in enumerate(M)]),'\nPart 2:',sum(Q.values()))