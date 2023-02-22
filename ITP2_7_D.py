from bisect import bisect_left,bisect_right
q = int(input())

a = []
for _ in range(0,q):
    op,*v = [int(x) for x in input().split()]
    x = v[0]

    idx = bisect_left(a, x)
    if 0 == op:
        a.insert(idx, x)
        print(len(a))
    elif 1 == op:
        print(bisect_right(a,x) - idx)
    elif 2 == op:
        del a[idx:bisect_right(a,x)]
    else:
        y = v[1]
        idxR = bisect_right(a, y)
        for ai in a[idx:idxR]:
            print(ai)
