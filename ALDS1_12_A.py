import math
from heapq import heapify, heappop

def mst(n, g):
    heap = [[math.inf, v] for v in range(n)]
    heap[0] = [0, 0]

    sum = 0
    while heap:
        heapify(heap)
        cv,v = heappop(heap)
        sum += cv

        for i,[cu,u] in enumerate(heap):
            gvu = g[v][u]
            if gvu < 0: continue
            heap[i][0] = min(cu, gvu)
    return sum

n = int(input())
g = [None for _ in range(n)]

for i in range(n):
    g[i] = [int(x) for x in input().split()]

print(mst(n, g))
