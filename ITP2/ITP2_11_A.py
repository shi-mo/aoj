n = int(input())

for d in range(1<<n):
    s = [i for i in range(n) if 0 != (d & 1<<i)]
    print(f'{d:d}:', *s)