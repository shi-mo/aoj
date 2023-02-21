n = int(input())
a = [int(x) for x in input().split()]

def next_of(a: list, desc: bool):
    p = a.copy()
    if desc: p = [-x for x in p]

    escape = False
    for j in reversed(range(1,n)):
        if escape: break
        for i in reversed(range(0,j)):
            v = max(p[i+1:])
            if p[i] > v: continue

            b = list(sorted(p[i:].copy()))
            idx = b.index(p[i])
            if (len(b)-1) <= idx: continue

            p[i] = b[idx+1]
            b.remove(b[idx+1])
            p[i+1:] = sorted(b)
            escape = True
            break

    if desc: p = [-x for x in p]
    return p

p = next_of(a, desc=True)
if p != a:
    print(*p)

print(*a)

b = next_of(a, desc=False)
if b != a:
    print(*b)
