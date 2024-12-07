import re
t = ('do()'+open(0).read()).split("don't()")
f = lambda p: sum(int(a)*int(b) for r in t for a,b in re.findall('mul\((\d+),(\d+)\)', r[r.find('do()')*p:]))
print('Part 1:', f(0))
print('Part 2:', f(1))