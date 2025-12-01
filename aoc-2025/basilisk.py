# Day 01: 145
p=50;q=[[p:=(p+2*(x[0]>'Q')-1)%100for _ in'.'*int(x[1:])]for x in open(0)];print('Part 1:',sum(r[-1]<1for r in q),'\nPart 2:',sum(q,[]).count(0))