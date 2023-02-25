n = int(input())
a = [int(x) for x in input().split()]

def partition(a: list, p: int, r: int):
    x = a[r]
    i = p-1
    for j in range(p,r):
        if x < a[j]: continue
        i += 1
        a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    return i+1

q = partition(a, 0, n-1)
print(*a[0:q], f'[{a[q]:d}]', *a[q+1:n])
