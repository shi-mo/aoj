n = int(input())

masks = [0] * n
for i in range(n):
    _,*v = [int(x) for x in input().split()]
    for b in v: masks[i] |= 1<<b

q = int(input())

st = 0
for _ in range(q):
    v = [int(x) for x in input().split()]
    op = v[0]
    if 0 < op: m  = masks[v[1]]

    if 0 == op:
        print(1 if 0 != (st & (1<<v[1])) else 0)
    elif 1 == op:
        st |= m
    elif 2 == op:
        st &= ~m
    elif 3 == op:
        st = st^m | st&(~m)
    elif 4 == op:
        print(1 if (st & m) == m else 0)
    elif 5 == op:
        print(1 if 0 != (st & m) else 0)
    elif 6 == op:
        print(1 if 0 == (st & m) else 0)
    elif 7 == op:
        print(bin(st & m).count('1'))
    elif 8 == op:
        print(st & m)
