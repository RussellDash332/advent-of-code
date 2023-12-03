import sys
m = [*map(lambda x: x.strip(), sys.stdin)]
p1 = p2 = 0
all_nums = set()
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] not in '0123456789.':
            nums = set()
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if 0<=i+di<len(m) and 0<=j+dj<len(m[0]) and '0'<=m[i+di][j+dj]<='9':
                        k = l = j+dj
                        while k >= 0 and '0'<=m[i+di][k]<='9': k -= 1
                        while l < len(m[0]) and '0'<=m[i+di][l]<='9': l += 1
                        nums.add((i+di, k+1, l))
            all_nums |= nums
            if m[i][j] == '*' and len(nums) == 2:
                (a, b, c), (d, e, f) = nums
                p2 += int(m[a][b:c])*int(m[d][e:f])
for i, j, k in all_nums: p1 += int(m[i][j:k])
print('Part 1:', p1)
print('Part 2:', p2)