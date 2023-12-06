f=1;l=[input().split()[1:]for _ in'..'];g=lambda a,b:a-1-2*int((a-(a*a-4*b)**0.5)/2)
for i in zip(*l):f*=g(*map(int,i))
print('Part 1:',f,'\nPart 2:',g(*map(int,map(''.join,l))))