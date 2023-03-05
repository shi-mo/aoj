def unshift(a, i):
    while 1 < i:
        tmp = a[i]
        a[i] = a[i//2]
        a[i//2] = tmp
        i = i//2

def reverse_heap_sort(a):
    n = len(a)
    a = [None] + a
    hsize = 1
    while hsize < n:
        unshift(a, hsize)
        hsize += 1
        tmp = a[1]
        a[1] = a[hsize]
        a[hsize] = tmp
    return a[1:]

_ = input()
a = [int(x) for x in input().split()]
print(*reverse_heap_sort(sorted(a)))
