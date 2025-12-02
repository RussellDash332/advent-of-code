# Day 01: 145
p=50;q=[[p:=(p+2*(x[0]>'Q')-1)%100for _ in'.'*int(x[1:])]for x in open(0)];print('Part 1:',sum(r[-1]<1for r in q),'\nPart 2:',sum(q,[]).count(0))
# Day 02: 227
v=[*map(int,input().replace('-',',').split(','))];f=lambda t:sum([k:=len(s:=str(i)),i*any(s==l*s[:k//l]for l in range(2,[2,k][t]+1))][1]for a,b in zip(v[::2],v[1::2])for i in range(a,b+1));print('Part 1:',f(0),'\nPart 2:',f(1))