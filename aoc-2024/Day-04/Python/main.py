z=range;k=z(-1,2);r=len(m:=[*open(0)]);c=len(m[-1]);print('Part 1:',sum(''.join(m[i//c+t*p][i%c+t*q]for t in z(4))=='XMAS'for i in z(r*c)for p in k for q in k if r>i//c+3*p>-1<i%c+3*q<c),'\nPart 2:',sum(m[i+1][j+1]<'B'!={m[i][j],m[i+2][j+2]}&{m[i+2][j],m[i][j+2]}=={*'MS'}for i in z(r-2)for j in z(c-2)))