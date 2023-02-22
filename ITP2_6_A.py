from bisect import bisect_left

n = int(input())
a = [int(x) for x in input().split()]
q = int(input())

l = len(a)
for _ in range(0,q):
    k = int(input())
    i = bisect_left(a, k)
    print(1 if i < l and a[i] == k else 0)
