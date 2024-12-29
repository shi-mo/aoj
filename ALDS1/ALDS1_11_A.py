n = int(input())
a = [[0]*n for _ in range(n)]

for _ in range(n):
    u,k,*v = [int(x) for x in input().split()]
    for vi in v:
        a[u-1][vi-1] = 1

for ai in a:
    print(*ai)
