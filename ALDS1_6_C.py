from collections import deque

n = int(input())
a,b = [],[]
for i in range(n):
    s,v = input().split()
    a.append([s, int(v)])
    b.append([s, int(v), i])

def qsort(a: list, p: int, r: int, cmp):
    stack = deque()
    stack.append([p,r])
    while stack:
        b,e = stack.pop()
        if e <= b: continue
        x = a[e]
        i = b-1
        for j in range(b,e):
            if cmp(x, a[j]): continue
            i += 1
            a[i],a[j] = a[j],a[i]
        a[i+1],a[e] = a[e],a[i+1]
        stack.append([i+2,e])
        stack.append([b,i])

qsort(a, 0, n-1, lambda x,y: x[1] < y[1])
qsort(b, 0, n-1, lambda x,y: (x[1]*n + x[2]) < (y[1]*n + y[2]))
ast = [x[0:2] for x in b]

print('Stable' if a == ast else 'Not stable')
for s,v in a:
    print(f'{s:s} {v:d}')
