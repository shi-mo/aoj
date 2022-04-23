while True:
    a = list(map(int, input().split()))
    a.sort()
    if (0 == a[0]) and (0 == a[1]):
        break
    print(f'{a[0]:d} {a[1]:d}')
