import sys;t=u=0;r=range;m=dict(zip(['one','two','three','four','five','six','seven','eight','nine',*map(str,r(1,10))],[*r(1,10)]*2));exec("for l in sys.stdin:s=[*filter(lambda x:'0'<x<':',l)];t+=int(s[0]+s[-1]);f=[m[j]for i in r(len(l))for j in m if l[i:][:len(j)]==j];u+=10*f[0]+f[-1]");print('Part 1:',t,'\nPart 2:',u)
import sys;a=b=0;exec("for l in sys.stdin:g,c=l.split(':');h={};t=c.split();[h.update({(u:=t[2*i+1][0]):max(h.get(u,0),int(t[2*i]))}) for i in range(len(t)//2)];a+=int(g[4:])*(h['b']<15)*(h['g']<14)*(h['r']<13);b+=h['b']*h['g']*h['r']");print('Part 1:',a,'\nPart 2:',b)
import sys;r=range;m=[*map(str.strip,sys.stdin)];R=len(m);C=len(m[0]);q=0;x=r(-1,2);A=set();[[n:=set(),[[k:=v,[[k:=k-(k+1and'/'<m[u][k]<':'),v:=v+(v<C and'/'<m[u][v]<':')]for _ in r(C)],n.add((u,k+1,v))]for s in x for t in x if R>(u:=i+s)>=0and C>(v:=j+t)>=0and'/'<m[u][v]<':'],A:=A|n,0if len(n)!=2or'*'!=T else[y:=n.pop(),z:=n.pop(),q:=q+int(m[y[0]][y[1]:y[2]])*int(m[z[0]][z[1]:z[2]])]]for i in r(R)for j in r(C)if(T:=m[i][j])not in'0123456789.'];print('Part 1:',sum(int(m[i][j:k])for i,j,k in A),'\nPart 2:',q)
import sys;c=[];exec("for l in sys.stdin:a,b=l.split('|');c.append(len({*map(int,b.split())}&{*map(int,a.split(':')[1].split())}))");d=[1]*len(c);[exec("d[i+j+1] += d[i]")for i in range(len(c))for j in range(c[i])];print('Part 1:',sum(2**s*bool(s)//2for s in c),'\nPart 2:',sum(d))
import sys;I=sys.stdin.readline;convert=lambda s:[x:=[],[[u:=[],[[x.append((max(a+p-q,p),min(b+p-q,p+r-1))),u.append((max(a,q),min(b,q+r-1)))]for p,q,r in d if(a<q+r)*(b>=q)],0if u else[x.append((a,b)),u.append(x[-1])],x.append((a,u[0][0]-1)),u.insert(0,x[-1]),x.append((u[-1][1]+1,b)),u.append(x[-1]),[x.append((e[1]+1,f[0]-1))for e,f in zip(u,u[1:])]]for a,b in s],[(a,b)for a,b in x if a<=b]][2];s=[s:=[*map(lambda x:[int(x)]*2,I().split(':')[1].split())],[[t:=s[2*i][0],t+s[2*i+1][0]-1]for i in range(len(s)//2)]];I();[[I(),d:=[],exec("while(e:=[*map(int,I().split())]):d.append(e)"),d.sort(key=lambda x: x[1]),s:=[*map(convert,s)]]for _ in'.'*7];print('Part 1:',min(s[0])[0],'\nPart 2:',min(s[1])[0])
f=1;l=[input().split()[1:]for _ in'..'];g=lambda a,b:a-1-2*int((a-(a*a-4*b)**0.5)/2);exec('for i in zip(*l):f*=g(*map(int,i))');print('Part 1:',f,'\nPart 2:',g(*map(int,map(''.join,l))))
import sys;from collections import*;m=dict(zip('TJQKA',':;<=>'));r=lambda f:[max(f),-len(f)];d=[*map(str.split,sys.stdin)];s=lambda t:sum((i+1)*int(e[1])for i,e in enumerate(sorted(d,key=lambda c:max(r(Counter(c[0].replace(t,i)).values())for i in c[0])+[m.get(i,i)for i in c[0]])));print('Part 1:',s('@'));m['J']='1';print('Part 2:',s('J'))
import sys,re;from math import *;from functools import *;m=input().strip();input();g={};[[n:=re.findall('\w+',l),g.update({n[0]:n[1:]})]for l in sys.stdin];d=lambda p,q,s:[[p:=g[p][i>'L']for i in m],len(m)+(0if q==p[s:]else d(p,q,s))][1];print('Part 1:',d('AAA','ZZZ',0),'\nPart 2:',reduce(lambda x,y:x*y//gcd(x,y),[d(i,'Z',2)for i in g if'A'==i[2]]))