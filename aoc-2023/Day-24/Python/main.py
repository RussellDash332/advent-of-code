import sys, re
from fractions import Fraction
data = [[*map(int, re.findall('[-\d]+', l))] for l in sys.stdin]; N = len(data)
lb, ub, ans = 2e14, 4e14, 0; A = []; b = []
for i in range(N):
    px1, py1, pz1, vx1, vy1, vz1 = data[i]
    for j in range(i+1, N):
        px2, py2, pz2, vx2, vy2, vz2 = data[j]; a, b, c, d, e, f = vx1, -vx2, px2-px1, vy1, -vy2, py2-py1
        if a*e-b*d: t = (c*e-b*f)/(a*e-b*d); t2 = (c-a*t)/b; ans += t > 0 and t2 > 0 and lb <= px1+vx1*t <= ub and lb <= py1+vy1*t <= ub
        '''
        To solve for (PX, PY, PZ, VX, VY, VZ), we have the following system of equations (uppercase variables are unknown)
        (PX + VX * Ti, PY + VY * Ti, PZ + VZ * Ti) = (pxi + vxi * Ti, pyi + vyi * Ti, pzi + vzi * Ti)
        -> PX + VX * Ti = pxi + vxi * Ti -> PX - pxi = (vxi - VX) * Ti -> (1)
                                         -> PY - pyi = (vyi - VY) * Ti -> (2)
        (1) * (vyi - VY) - (2) * (vxi - VX)
        -> (PX - pxi) * (vyi - VY) - (PY - pyi) * (vxi - VX) = 0
        -> PY * VX - PX * VY + vyi * PX + pxi * VY - pyi * VX - vxi * PY + (pyi * vxi - pxi * vyi) = 0 (3)
        -> PY * VX - PX * VY + vyj * PX + pxj * VY - pyj * VX - vxj * PY + (pyj * vxj - pxj * vyj) = 0 (4, i => j)
        (3) - (4)
        -> (vyi - vyj) * PX + (pxi - pxj) * VY - (pyi - pyj) * VX - (vxi - vxj) * PY + (pyi * vxi - pxi * vyi - pyj * vxj + pxj * vyj) = 0
        -> (vzi - vzj) * PX + (pxi - pxj) * VZ - (pzi - pzj) * VX - (vxi - vxj) * PZ + (pzi * vxi - pxi * vzi - pzj * vxj + pxj * vzj) = 0
        '''
        if len(A) != 6:
            A.append([vy1-vy2, vx2-vx1, 0, py2-py1, px1-px2, 0, px1*vy1+py2*vx2-py1*vx1-px2*vy2])
            A.append([vz1-vz2, 0, vx2-vx1, pz2-pz1, 0, px1-px2, px1*vz1+pz2*vx2-pz1*vx1-px2*vz2])

# https://github.com/RussellDash332/pytils/blob/main/rref.py
for i in range(len(A)):
    for j in range(len(A[0])): A[i][j] = Fraction(A[i][j])
def equal(a, b):
    return a == b
def leading_entry_col(A, r):
    row = A[r]; i = 0
    while i < len(A[0]) and equal(row[i], 0): i += 1
    return i
def list_pivots(A):
    res = []
    for r in range(len(A)):
        k = leading_entry_col(A, r)
        if k != len(A[0]): res.append((r, k))
    return sorted(res, reverse=True)
def col(A, i):
    return list(map(lambda x: x[i], A))
def ero1(A, i, c):
    for j in range(len(A[0])): A[i][j] *= c
def ero2(A, i, j, c):
    for k in range(len(A[0])): A[i][k] += c*A[j][k]
def ero3(A, i, j): A[i], A[j] = A[j], A[i]
curr_col = 0
curr_row = 0
while curr_col < len(A[0]) and curr_row < len(A):
    if equal(A[curr_row][curr_col], 0):
        check_col = col(A, curr_col)[curr_row+1:]
        for i in range(len(check_col)):
            if not equal(check_col[i], 0): break
            elif i == len(check_col)-1: i += 1
        if i < len(check_col): ero3(A, curr_row, curr_row+i+1)
        else: curr_col += 1
    else:
        if not equal(A[curr_row][curr_col], 1): ero1(A, curr_row, 1/A[curr_row][curr_col])
        for i in range(curr_row+1, len(A)):
            if not equal(A[i][curr_col], 0): ero2(A, i, curr_row, -A[i][curr_col])
        curr_col += 1
        curr_row += 1
pivots = list_pivots(A)
for i in range(len(pivots)-1):
    for j in range(pivots[i][0]-1, -1, -1): ero2(A, j, pivots[i][0], -A[j][pivots[i][1]])

print('Part 1:', ans)
print('Part 2:', A[0][6]+A[1][6]+A[2][6])