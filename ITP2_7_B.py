q = int(input())

a = set()
for _ in range(0,q):
    op,x = [int(x) for x in input().split()]
    if 0 == op:
        a.add(x)
        print(len(a))
    elif 1 == op:
        print(1 if x in a else 0)
    else:
        if x in a: a.remove(x)
