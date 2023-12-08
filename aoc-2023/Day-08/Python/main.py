import sys, re; from math import *
cmd = input().strip(); input(); g = {}
for l in sys.stdin:
    a, b, c = re.findall('\w+', l)
    g[a] = [b, c]

def dist(pos, dst, slc=0):
    t = 0
    while True:
        for i in cmd: t += 1; pos = g[pos][i>'L']
        if pos[slc:] == dst: return t

print('Part 1:', dist('AAA', 'ZZZ'))
t = [dist(i, 'Z', -1) for i in g if i[-1] == 'A']; u = 1
for i in t: u = (u*i)//gcd(u, i)
print('Part 2:', u)