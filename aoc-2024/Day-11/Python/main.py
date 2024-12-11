m=[*map(int,input().split())];h={}
def f(x,d):
 if d==0:return 1
 if(x,d)in h:return h[(x,d)]
 if x==0:h[(x,d)]=f(1,d-1);return h[(x,d)]
 y=str(x)
 if len(y)%2==0:h[(x,d)]=f(int(y[:len(y)//2]),d-1)+f(int(y[len(y)//2:]),d-1)
 else:h[(x,d)]=f(2024*x,d-1)
 return h[(x,d)]
print('Part 1:',sum(f(i,25)for i in m))
print('Part 2:',sum(f(i,75)for i in m))