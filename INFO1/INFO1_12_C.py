n, m, q = [int(d) for d in input().split()]
a = [[0]*m for _ in range(n)]

for _ in range(q):
    i, j = [int(d) for d in input().split()]
    a[i][j] = 1 & ~a[i][j]

for i in range(n):
    print(' '.join([str(v) for v in a[i]]))