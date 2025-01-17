from sys import stdin

n, m = [int(x) for x in input().split()]

a = [[0]*m for _ in range(n)]
for i in range(n):
    for j, vj in enumerate([int(x) for x in input().split()]):
        a[i][j] = vj

i1, j1 = [int(x) for x in input().split()]
i2, j2 = [int(x) for x in input().split()]
r1 = min(i1, i2); r2 = max(i1, i2)
c1 = min(j1, j2); c2 = max(j1, j2)
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        if c1 < j: print(' ', end='')
        print(a[i][j], end='')
    print('')