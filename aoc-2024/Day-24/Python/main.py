s,t=open(0).read().split('\n\n');Z=t.count(' z')
T={}
for x in t.split('\n'):a,b,c,_,d=x.split();T[(a,c,b)]=d
F=lambda k,a,b,c:k==(a,b,c)or(b,a,c)==k
M={}
for i in s.split('\n'):M[i[:3]]=int(i[4:])
S=[];C=''
def W(a,b):T[a],T[b]=T[b],T[a];S.extend((T[a],T[b]))
for _ in T:
    for (a,c,b),d in T.items():
        if a in M and c in M:
            if b=='XOR':M[d]=M[a]^M[c]
            if b=='OR':M[d]=M[a]|M[c]
            if b=='AND':M[d]=M[a]&M[c]
print('Part 1:',sum(M[f'z{i:02}']<<i for i in range(Z)))
for i in range(Z-1):
    m=n=r=z=c=''
    for k in T:
        if F(k,f'x{i:02}',f'y{i:02}','XOR'):m=k
        if F(k,f'x{i:02}',f'y{i:02}','AND'):n=k
    if C:
        for k in T:
            if F(k,T[C],T[m],'AND'):r=k
        if not r:
            W(m,n)
            for k in T:
                if F(k,T[C],T[m],'AND'):r=k
        for k in T:
            if F(k,T[C],T[m],'XOR'):z=k
        if m and T[m][0]=='z':W(m,z)
        if n and T[n][0]=='z':W(n,z)
        if r and T[r][0]=='z':W(r,z)
        for k in T:
            if F(k,T[r],T[n],'OR'):c=k
    if c and T[c][0]=='z' and T[c]!=f'z{Z-1}':W(c,z)
    C=c if C else n
print('Part 2:',','.join(sorted(S)))

'''
Note to self:
For n-th least significant bit,
Xn ^ Yn -> Mn
Xn & Yn -> Nn
C(n-1) & Mn -> Rn
C(n-1) ^ Mn -> Zn # output
Rn | Nn -> Cn     # carry
'''