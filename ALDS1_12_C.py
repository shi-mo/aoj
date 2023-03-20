import math
from heapq import heapify, heappop, heappush

n = int(input())
g = [None] * n

for _ in range(n):
    u,k,*vc = [int(x) for x in input().split()]
    g[u] = {vc[2*i]:vc[(2*i)+1] for i in range(k)}

d = [0] + [math.inf] * (n-1)
heap = [[0, 0]]

while heap:
    du, u = heappop(heap)
    for v in g[u]:
        dv = du + g[u][v]
        if dv < d[v]:
            d[v] = dv
            heappush(heap, [dv, v])

for v in range(n):
    print(v, d[v])
