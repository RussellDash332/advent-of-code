# partial golf, again
Z=range;M,E=open(0).read().split('\n\n');M=[*map(list,M.split('\n'))];N=[[*''.join(map({'#':'##','O':'[]','.':'..','@':'@.'}.get,r))]for r in M]
def do(M):
    R=len(M);C=len(M[0])
    for i in Z(R):
        for j in Z(C):
            if M[i][j]=='@':r,c=i,j;M[i][j]='.'
    for i in E:
        for x,y,z in((0,-1,'<'),(0,1,'>'),(1,0,'v'),(-1,0,'^')):
            if i!=z:continue
            Q=[(r+x,c+y)];V=set()
            for p,q in Q:
                if M[p][q]not in'[]O'or(p,q)in V:continue
                V.add((p,q))
                if M[p][q]=='[':Q.append((p,q+1))
                elif M[p][q]==']':Q.append((p,q-1))
                Q.append((p+x,q+y))
            if(M[r+x][c+y]>'#')*all(M[p+x][q+y]>'#'for p,q in V):
                r+=x;c+=y;O={(p,q):M[p][q]for p,q in V}
                for p,q in O:M[p][q]='.'
                for p,q in O:M[p+x][q+y]=O[(p,q)]
    return sum(100*i+j for i in Z(R)for j in Z(C)if M[i][j]in'[O')
print('Part 1:',do(M),'\nPart 2:',do(N))