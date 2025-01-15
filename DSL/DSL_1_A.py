n, q = [int(x) for x in input().split()]
set_of = {}
for i in range(n):
    set_of[i] = {i}

for i in range(q):
    cmd, x, y = [int(d) for d in input().split()]
    sx = set_of[x]; sy = set_of[y]
    if 0 == cmd:
        if sx == sy: continue
        xor = sx ^ sy
        union = sx | sy
        set_of[x] = union
        set_of[y] = union
        for e in xor: set_of[e] = union
        continue
    print(1 if sx == sy else 0)