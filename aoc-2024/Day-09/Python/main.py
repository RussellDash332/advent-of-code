# 565 chars, longer golf but much faster (~40s) so I'll keep it here instead
s=[*map(int,input())];Z=range;A=list.__setitem__;S=sum;L=len;P=-1;E=[];G=enumerate;f=lambda t:[m:=(L(q:=[0,S([[S([[[i],E]for _ in Z(j)],E)[:P],[[P]*j]][i%2]for i,j in G(s)],E),[j*[[i,P][i%2]]for i,j in G(s)]][t])+1)//2,z:=[[i for i in Z(1,m)if e==L(q[2*i])]for e in Z(10)],i:=0,[[f:=(r:=q[2*i+1]).count(P),x:=max(S(z[:f+1],[P])),l:=L(u:=q[2*x]),x>P!=[z[l].pop(),[[A(r,f-l+y,u[y]),A(u,y,P)]for y in Z(l)]]or[i:=i+1,q[2*i][0]>P<z[L(q[2*i])].pop(0)]]for _ in Z(2*m)if~-m>i],print(f'Part {t}:',S(i*j*(j>P)//2for i,j in G(S((v[::1-k%2*2]for k,v in G(q)),E))))];f(1);f(2)