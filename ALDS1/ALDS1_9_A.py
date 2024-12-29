h = int(input())
a = [int(x) for x in input().split()]

for idx, k in enumerate(a):
    i = idx + 1
    print(f'node {i:d}: key = {k:d}, ', end='')
    if 1 < i:
        print(f'parent key = {a[int(i/2)-1]:d}, ', end='')
    if 2*i <= h:
        print(f'left key = {a[2*i - 1]:d}, ', end='')
    if (2*i + 1) <= h:
        print(f'right key = {a[2*i]:d}, ', end='')
    print()
