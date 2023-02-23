from bisect import bisect_left,bisect_right
q = int(input())

h = {}
keys = []
for _ in range(q):
    op,*v = [x for x in input().split()]
    k = v[0]

    idx = bisect_left(keys, k)
    if '0' == op:
        if not k in h: keys.insert(idx, k)
        h[k] = v[1]
    elif '1' == op:
        print(h[k] if k in h else 0)
    elif '2' == op:
        if k in h:
            del h[k]
            del keys[idx:idx+1]
    else:
        r = v[1]
        idxR = bisect_right(keys, r)
        for key in keys[idx:idxR]:
            print(key, h[key])
