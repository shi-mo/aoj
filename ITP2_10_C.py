q = int(input())

b64 = 0xffffffff_ffffffff
st = 0
for _ in range(q):
    v = [int(x) for x in input().split()]
    op = v[0]
    i  = v[1] if op <= 3 else None

    if 0 == op:
        print(1 if 0 != (st & (1<<i)) else 0)
    elif 1 == op:
        st |= 1<<i
    elif 2 == op:
        st &= ~(1<<i)
    elif 3 == op:
        st ^= (1<<i)
    elif 4 == op:
        print(1 if st == b64 else 0)
    elif 5 == op:
        print(1 if 0 != st else 0)
    elif 6 == op:
        print(1 if 0 == st else 0)
    elif 7 == op:
        print(bin(st).count('1'))
    elif 8 == op:
        print(st)
