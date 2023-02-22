from bisect import bisect_left,bisect_right

n = int(input())
a = [int(x) for x in input().split()]
q = int(input())

for _ in range(0,q):
    k = int(input())
    print(bisect_left(a, k), bisect_right(a, k))
