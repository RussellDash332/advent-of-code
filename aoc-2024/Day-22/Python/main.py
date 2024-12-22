Z=0;M=1<<24;X=[0]*M
for x in map(int,open(0)):
    p = x%10; P = []; R = {}
    for _ in range(2000):
        x=(x<<6^x)%M; x=(x>>5^x)%M; x=(x<<11^x)%M
        P.append(x%10-p); p=x%10
        len(P) > 3 and R.setdefault(8000*P[-4]+400*P[-3]+20*P[-2]+P[-1], p)
    Z += x
    for i in R: X[i] += R[i]
print('Part 1:',Z,'\nPart 2:',max(X))