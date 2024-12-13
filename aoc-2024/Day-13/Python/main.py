import re; R = re.findall('Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)', open(0).read())
for p in (0, 1):
    Z = 0
    for r in R:
        a, d, b, e, c, f = map(int, r); c += p*10**13; f += p*10**13; x = c*d-a*f; y = b*d-a*e
        if x%y==0: Z += 3*(c-x//y*b)//a+x//y
    print(f'Part {p+1}:', Z)