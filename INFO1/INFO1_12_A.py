from sys import stdin

n, m = [int(x) for x in input().split()]

a = [[0]*m for _ in range(n)]
for i in range(n):
    for j, vj in enumerate([int(x) for x in input().split()]):
        a[i][j] = vj

for line in stdin:
    i, j = [int(x) for x in line.split()]
    print(a[i][j])