import math
from heapq import heapify, heappop

n = int(input())
g = [None] * n

for _ in range(n):
    u,k,*vc = [int(x) for x in input().split()]
    g[u] = {vc[2*i]:vc[(2*i)+1] for i in range(k)}

d = [None] * n
heap = [[math.inf, v] for v in range(n)]
heap[0] = [0, 0]

while heap:
    heapify(heap)
    du, u = heappop(heap)
    d[u] = du
    for i, [dv,v] in enumerate(heap):
        if not v in g[u]:
            continue
        d_new = du + g[u][v]
        if d_new < dv:
            heap[i] = [d_new, v]

for v in range(n):
    print(v, d[v])
