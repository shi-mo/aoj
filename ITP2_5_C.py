n = int(input())
a = [int(x) for x in input().split()]

def next_of(a: list, desc: bool):
    p = a.copy()
    if desc: p = [-x for x in p]
    n = len(a)

    l = -1
    for i in reversed(range(1,n)):
        if p[i-1] > p[i]: continue
        l = i-1
        break

    if l < 0:
        if desc: p = [-x for x in p]
        return p

    r = l+1
    for j in range(l+2,n):
        if p[l] > p[j]: continue
        if p[r] < p[j]: continue
        r = j

    p[l],p[r] = p[r],p[l]
    p[l+1:] = sorted(p[l+1:])

    if desc: p = [-x for x in p]
    return p

p = next_of(a, desc=True)
if p != a: print(*p)

print(*a)

b = next_of(a, desc=False)
if b != a: print(*b)
