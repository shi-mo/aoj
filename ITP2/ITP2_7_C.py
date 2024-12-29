from bisect import bisect_left,bisect_right
q = int(input())

a = []
for _ in range(0,q):
    op,*v = [int(x) for x in input().split()]
    x = v[0]

    idx = bisect_left(a, x)
    xina = (0 <= idx and idx < len(a) and x == a[idx])
    if 0 == op:
        if not xina:
            a.insert(idx, x)
        print(len(a))
    elif 1 == op:
        print(1 if xina else 0)
    elif 2 == op:
        if xina:
            del a[idx:idx+1]
    else:
        y = v[1]
        idxR = bisect_right(a, y)
        for ai in a[idx:idxR]:
            print(ai)
