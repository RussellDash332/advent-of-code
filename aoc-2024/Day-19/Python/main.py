p,_,*m=map(str.strip,open(0));p=p.split(', ')

import functools
@functools.lru_cache
def f(s, idx=0):
    if idx == len(s): return 1
    ans = 0
    for i in range(len(p)):
        if len(p[i])+idx <= len(s):
            ok = 1
            for j in range(len(p[i])):
                if p[i][j] != s[idx+j]: ok = 0; break
            if ok: ans += f(s, idx+len(p[i]))
    return ans

v = [x for i in m if (x:=f(i))]
print('Part 1:', len(v))
print('Part 2:', sum(v))