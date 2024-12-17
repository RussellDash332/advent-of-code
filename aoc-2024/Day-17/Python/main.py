'''
Assumptions:
- the input starts with (2,4), has (7,5) in between, and ends with (3,0), and there's exactly one of each of these pairs
- (0,3) and (5,5) appear somewhere between the (7,5) pair and (3,0) pair, in either order, and there's only one of each of these pairs
- literally any remaining pair must be either (1,x) or (4,y), which are XOR operations, and none of these are after the (5,5) pair
'''

import re
a,b,c,*p=map(int,re.findall('\d+',open(0).read()));q=0;z=[];m={0};u=[0]*4;t=0

while q<len(p):
    i=p[q];j=p[q+1];x=(0,1,2,3,a,b,c,0)[j] # index 7 might still come out as a literal
    if i==0:a>>=x
    if i==1:b^=j;u[t]^=j
    if i==2:b=x%8
    if i==3:q=(j-2,q)[a==0];t|=2*(q<0)
    if i==4:b^=c
    if i==5:z.append(str(x%8))
    if i==6:b=a>>x
    if i==7:c=a>>x;t|=j==5
    q+=2
print('Part 1:',','.join(z))
for n in p[::-1]:m={y for x in m for k in range(8)if[y:=8*x+k,p:=y%8^u[0],(p^(y>>p)^u[1])%8==n][2]}
print('Part 2:',min(m))