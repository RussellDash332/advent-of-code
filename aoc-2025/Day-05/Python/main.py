def merge(intervals):
    r = []
    for j in intervals:
        if r and r[-1][1] >= j[0] and j[1] >= r[-1][0]: r[-1] = (min(r[-1][0], j[0]), max(r[-1][1], j[1]))
        else: r.append(j)
    return r
m = [*open(0)]; I = []; J = []
for i in m:
    if '-' in i: I += [[*map(int, i.split('-'))]]
    elif i.strip(): J += [int(i)]
print('Part 1:', sum(any(x in range(a,b+1) for a,b in I)for x in J))
print('Part 2:', sum(b-a+1 for a,b in merge(I)))