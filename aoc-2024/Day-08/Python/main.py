# Partly golfed
import math;R=len(m:=[*open(0)]);C=len(m[-1]);N={};A=set();B=set()
for i in range(R):
    for j in range(C):N[m[i][j]]=N.get(m[i][j],[])+[(i,j)]
for i in N:
 if i>'.':
  for a,b in N[i]:
   for c,d in N[i]:
    x=a-c;y=b-d;e=c;f=d
    if x or y:
     g=math.gcd(x,y);x//=g;y//=g
     if R>c+2*x>-1<d+2*y<C:A.add((c+2*x,d+2*y))
     while R>e+x>-1<f+y<C:e+=x;f+=y;B.add((e,f))
print('Part 1:',len(A),'\nPart 2:',len(B))