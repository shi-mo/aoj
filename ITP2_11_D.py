n,k = [int(x) for x in input().split()]

for d in range(1<<n):
    s = [i for i in range(n) if 0 != (d & 1<<i)]
    if k != len(s): continue
    print(f'{d:d}:', *s)
