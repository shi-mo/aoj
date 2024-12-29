n = int(input())
k,*b = [int(x) for x in input().split()]

m = 0
for i in range(k): m |= 1<<b[i]

for d in range(1<<n):
    if (d & m) != m: continue
    s = [i for i in range(n) if 0 != (d & 1<<i)]
    print(f'{d:d}:', *s)
