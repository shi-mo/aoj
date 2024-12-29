n = int(input())
a = []
for i in range(n):
    s,v = input().split()
    a.append([s, int(v), i])

def partition(a: list, p: int, r: int, cmp):
    x = a[r]
    i = p-1
    for j in range(p,r):
        if cmp(x, a[j]): continue
        i += 1
        a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    return i+1

def qsort(a: list, p: int, r: int, cmp):
    if r <= p: return
    q = partition(a, p, r, cmp)
    qsort(a, p, q-1, cmp)
    qsort(a, q+1, r, cmp)

def is_stable(a: list):
    for i in range(len(a)-1):
        if a[i][1] != a[i+1][1]: continue
        if a[i][2] > a[i+1][2]: return False
    return True

qsort(a, 0, n-1, lambda x,y: x[1] < y[1])

print('Stable' if is_stable(a) else 'Not stable')
for s,v,_ in a:
    print(f'{s:s} {v:d}')
