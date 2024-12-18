S=[*open(0)];L=71;m=L*L*[1]
for k in range(len(S)):
 d=L*L*[-1];a,b=map(int,S[k].split(','));m[b*L+a]=0;q=[(0,0)];d[0]=0
 for r,c in q:
  for x,y in((0,-1),(-1,0),(0,1),(1,0)):
   p=(r+x)*L+c+y
   if L>r+x>-1<c+y<L>m[p]>0>d[p]:d[p]=d[r*L+c]+1;q.append((r+x,c+y))
 if k==1023:print('Part 1:',d[-1])
 if d[-1]==-1:print('Part 2:',S[k].strip());break