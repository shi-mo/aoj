_ = input()
k,*b = [int(x) for x in input().split()]

for d in range(1<<k):
    s = [b[i] for i in range(k) if 0 != (d & 1<<i)]
    m = 0
    for j in s: m |= 1<<j
    print(f'{m:d}:', *s)
