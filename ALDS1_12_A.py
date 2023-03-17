import math

def mst_prim(n, g):
    mincost_to = [math.inf] * n
    rest_nodes = list(range(n))

    sum = 0
    mincost_to[0] = 0
    while rest_nodes:
        v = rest_nodes[0]
        for u in rest_nodes[1:]:
            if mincost_to[u] < mincost_to[v]:
                v = u

        rest_nodes.remove(v)
        sum += mincost_to[v]

        for u in range(n):
            cost2v = g[v][u]
            if -1 < cost2v:
                mincost_to[u] = min(cost2v, mincost_to[u])
    return sum

n = int(input())
g = [None for _ in range(n)]

for i in range(n):
    g[i] = [int(x) for x in input().split()]

print(mst_prim(n, g))
