q = int(input())

h = {}
for _ in range(q):
    op,*v = [x for x in input().split()]
    k = v[0]
    if '0' == op:
        h[k] = v[1]
    else:
        print(h[k])
