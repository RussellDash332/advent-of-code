# Day 01: 347
[r:=range,m:=dict(zip(['one','two','three','four','five','six','seven','eight','nine',*map(str,z:=r(1,10))],[*z]*2)),t:=sum([s:=[*filter(lambda x:'0'<x<':',l)],f:=[m[j]for i in r(len(l))for j in m if l[i:i+len(j)]==j],complex(int(s[0]+s[-1]),10*f[0]+f[-1])][2]for l in __import__('sys').stdin),print('Part 1:',int(t.real),'\nPart 2:',int(t.imag))]
# Day 02: 274
[z:=int,u:=sum([g:=l.split(':'),t:=g[1].split(),h:=dict(sorted((t[2*i+1][0],z(t[2*i]))for i in range(len(t)//2))),complex(z(g[0][4:])*(h['g']<14>=h['b'])*(h['r']<13),h['b']*h['g']*h['r'])][3]for l in __import__('sys').stdin),print('Part 1:',z(u.real),'\nPart 2:',z(u.imag))]
# Day 03: 525
[r:=range,m:=[*map(str.strip,__import__('sys').stdin)],R:=len(m),C:=len(m[0]),q:=0,x:=r(-1,2),A:=set(),[[n:=set(),[[k:=v,[[k:=k-(k+1and'/'<m[u][k]<':'),v:=v+(v<C and'/'<m[u][v]<':')]for _ in r(C)],n.add((u,k+1,v))]for s in x for t in x if R>(u:=i+s)>=0and C>(v:=j+t)>=0and'/'<m[u][v]<':'],A:=A|n,0if len(n)!=2or'*'!=T else[y:=n.pop(),z:=n.pop(),q:=q+int(m[y[0]][y[1]:y[2]])*int(m[z[0]][z[1]:z[2]])]]for i in r(R)for j in r(C)if(T:=m[i][j])not in'0123456789.'],print('Part 1:',sum(int(m[i][j:k])for i,j,k in A),'\nPart 2:',q)]
# Day 04: 285
[c:=[[x:=l.split('|'),len({*map(int,x[1].split())}&{*map(int,x[0].split(':')[1].split())})][1]for l in __import__('sys').stdin],d:=[1]*len(c),[d.__setitem__(u:=i+j+1,d[u]+d[i])for i in range(len(c))for j in range(c[i])],print('Part 1:',sum(2**s*(s>0)//2for s in c),'\nPart 2:',sum(d))]
# Day 05: 698
[S:=str.split,A:=list.append,I:=__import__('sys').stdin.readline,c:=lambda s:[x:=[],[[u:=[],[[A(x,(max(a+p-q,p),min(b+p-q,p+r-1))),A(u,(max(a,q),min(b,q+r-1)))]for p,q,r in d if(a<q+r)*(b>=q)],0if u else[A(x,(a,b)),A(u,x[-1])],A(x,(a,u[0][0]-1)),u.insert(0,x[-1]),A(x,(u[-1][1]+1,b)),A(u,x[-1]),[A(x,(e[1]+1,f[0]-1))for e,f in zip(u,u[1:])]]for a,b in s],[(a,b)for a,b in x if a<=b]][2],s:=[s:=[*map(lambda x:[int(x)]*2,S(S(I(),':')[1]))],[[t:=s[2*i][0],t+s[2*i+1][0]-1]for i in range(len(s)//2)]],I(),[[I(),d:=[1],[(A(d,[*map(int,S(I()))])if not d or d[-1]else 0)for i in d],d:=d[1:-1],d.sort(key=lambda x:x[1]),s:=[*map(c,s)]]for _ in'.'*7],print('Part 1:',min(s[0])[0],'\nPart 2:',min(s[1])[0])]
# Day 06: 185
[f:=1,l:=[input().split()[1:]for _ in'..'],g:=lambda a,b:a-1-2*int((a-(a*a-4*b)**.5)/2),[f:=f*g(*map(int,i))for i in zip(*l)],print('Part 1:',f,'\nPart 2:',g(*map(int,map(''.join,l))))]
# Day 07: 349
[m:=dict(zip('TJQKA',':;<=>')),d:=[*map(str.split,(I:=__import__)('sys').stdin)],s:=lambda t:sum((i+1)*int(e[1])for i,e in enumerate(sorted(d,key=lambda c:max((lambda f:[max(f),-len(f)])(I('collections').Counter(c[0].replace(t,i)).values())for i in c[0])+[m.get(i,i)for i in c[0]]))),print('Part 1:',s('@')),m:={**m,'J':'1'},print('Part 2:',s('J'))]
# Day 08: 328
[I:=__import__,m:=input().strip(),input(),g:=dict(((n:=I('re').findall('\w+',l))[0],n[1:])for l in I('sys').stdin),d:=lambda p,s:[[p:=g[p][i>'L']for i in m],len(m)+(0if'Z'*s==p[3-s:]else d(p,s))][1],print('Part 1:',d('AAA',3),'\nPart 2:',I('functools').reduce(lambda x,y:x*y//I('math').gcd(x,y),[d(i,1)for i in g if'A'==i[2]]))]
# Day 09: 197
print('Part 1:',sum((M:=map)(E:=lambda l:l[-1]+E([b-a for a,b in zip(l,l[1:])])if l else 0,L:=[*M(lambda x:[*M(int,x.split())],__import__('sys').stdin)])),'\nPart 2:',sum(M(lambda x:E(x[::-1]),L)))
# Day 10: 797
[x:=range,b:=[*map(str.strip,__import__('sys').stdin)],m:=[[A:='@']*(C:=2*len(b[0])+1)],[m.extend([[*(A+A.join(l)+A)],m[0]])for l in b],R:=len(m),Z:=x(X:=R*C),d:=[-2]*X,S:=d.__setitem__,g:=[[]for _ in Z],q:=[(u,0)for u in Z if'S'==m[u//C][u%C]],s:=[(0,0)],f:=lambda a,b:(g[a].append(b),g[b].append(a)),[[t:=m[u//C][u%C],f(u,u-C)if t in'S|LJ'else 0,f(u,u+C)if t in'S|7F'else 0,f(u,u+1)if t in'S-LF'else 0,f(u,u-1)if t in'S-J7'else 0]for u in Z],[[t:=q[0][1],u:=q.pop(0)[0],[S(u,t),q.extend((v,t+1)for v in g[u])]if d[u]<0else 0]for _ in x(X*4)if q],[[r:=s[-1][0],c:=s.pop()[1],[S(C*r+c,0),s.extend((r+p,c+z)for p,z in((0,-1),(0,1),(-1,0),(1,0))if R>r+p>-1and-1<c+z<C)]if 0>d[C*r+c]else 0]for _ in x(X*4)if s],print('Part 1:',max(d)//2,'\nPart 2:',sum(0>d[C*r+c]for r in x(1,R,2)for c in x(1,C,2)))]
# Day 11: 398
[A:=list.append,m:=[*map(str.strip,__import__('sys').stdin)],x:=range,f:=lambda e:[p:=[0],q:=[0],G:=[],r:={*x(R:=len(m))},c:={*x(C:=len(m[0]))},[[r:=r-{i},c:=c-{j},A(G,(i+1,j+1))]for i in x(R)for j in x(C)if'.'>m[i][j]],[A(l,l[i]+1+e*(i in h))for l,h,H in((p,r,R),(q,c,C))for i in x(H)],sum(abs(p[a]-p[c])+abs(q[b]-q[d])for a,b in G for c,d in G)//2][7],print('Part 1:',f(1),'\nPart 2:',f(999999))]
# Day 12: 467
[L:=len,g:=lambda l,p:[m:={},f:=lambda i,j,c:m[t]if(t:=(i,j,c))in m else(c==p[-1])*(L(p)-1==j)|(c<1)*(j==L(p))if i==L(l)else[r:=(f(i+1,j,c+1)if l[i]in'?#'else 0)+(f(i+1,j,0)if(k:=l[i]in'?.')*(c<1)else 0)+(f(i+1,j+1,0)if k*c*(j<L(p))and(p[j]==c)else 0),m.update({t:r}),r][2],f(0,0,0)][2],a:=sum(complex(g((d:=l.split())[0],p:=[*map(int,d[1].split(','))]),g('?'.join(5*[d[0]]),5*p))for l in __import__('sys').stdin),print('Part 1:',int(a.real),'\nPart 2:',int(a.imag))]
# Day 13: 313
print('Part 1:',int((u:=sum(complex((s:=lambda g,d=0:[0,*(i for i in range(len(g[0]))if sum(a!=b for r in g for a,b in zip(r[i-1::-1],r[i:]))==d)][-1])(g:=l.split('\n'))+100*s(h:=[*zip(*g)]),s(g,1)+100*s(h,1))for l in''.join(__import__('sys').stdin).replace('\r','').split('\n\n'))).real),'\nPart 2:',int(u.imag))