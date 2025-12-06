l = [*open(0)]
op = l[-1].split()
p = [*zip(*([*map(int, s.split())] for s in l[:-1]))]
q = ' '.join(map(''.join, zip(*l[:-1]))).split()
print('Part 1:', sum(eval(y.join(map(str, x))) for x, y in zip(p, op)))
x = [i for i in range(len(l[-1])) if l[-1][i] != ' '] + [len(l[-1])*2]
print('Part 2:', sum(eval(op[i].join(q[x[i]-i:x[i+1]-1-i])) for i in range(len(op))))