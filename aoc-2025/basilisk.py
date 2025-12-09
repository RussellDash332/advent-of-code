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
# Day 07: 183
L,*M=open(0);Q={L.index('S'):1};print('Part 1:',sum([[T:={},sum([x:=r[k]>'S',T:=T|{v:T.get(v,0)+Q[k]for v in(k-x,k+x)}][0]for k in Q),Q:=T][1]for r in M]),'\nPart 2:',sum(Q.values()))
# Day 08: 355
R=range(len(P:=[[*map(int,l.split(','))]for l in open(0)]));T=z=[1<<i for i in R];Q=[[U:=T[a]|T[b],[T.__setitem__(u,U)for u in R if(1<<u)&U],z:={*T},S:=P[a][0]*P[b][0]][2]for _,a,b in sorted((sum((a-b)**2for a,b in zip(P[i],P[j])),i,j)for i in R for j in range(i))if~-len(z)];*_,a,b,c=sorted(map(int.bit_count,Q[999]));print('Part 1:',a*b*c,'\nPart 2:',S)
# Day 09: 622
R=range(len(P:=[[*map(int,l.split(','))]for l in open(0)]));D=abs;J=complex;C=lambda p:sum(1-I(*p,p[0]+1e6,p[1]+6e7,*P[i],*P[i-1])for i in R)%2or next((1for i in R if D(J(*P[i])-J(*p))+D(J(*p)-J(*P[i-1]))==D(J(*P[i])-J(*P[i-1]))),0);I=lambda a,b,c,d,e,f,g,h:((c-a)*(f-b)-(d-b)*(e-a))*((c-a)*(h-b)-(d-b)*(g-a))<0>((g-e)*(b-f)-(h-f)*(a-e))*((g-e)*(d-f)-(h-f)*(c-e));Z=sorted((~D(c-a)*-~D(d-b),a,b,c,d)for a,b in P for c,d in P);print('Part 1:',-Z[0][0],'\nPart 2:',next(-w for w,a,b,c,d in Z if(K:=[(a,b),(a,d),(c,d),(c,b)])and[z:=all(map(C,K)),[z:=z*~-I(*K[k],*K[k-1],*P[i],*P[i-1])for i in R for k in(0,1,2,3)if z],z][2]))