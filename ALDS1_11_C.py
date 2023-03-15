from collections import deque

def bfs(n, adj):
    d = [-1]*n
    d[0] = 0
    que = deque([1])
    while que:
        v = que.popleft()
        dist = d[v-1]
        for u in adj[v-1]:
            if -1 < d[u-1]:
                continue
            d[u-1] = dist+1
            que.append(u)
    return d

n = int(input())

a = [None]*n
for _ in range(n):
    u,k,*v = [int(x) for x in input().split()]
    a[u-1] = v

d = bfs(n, a)
for i,di in enumerate(d):
    print(i+1, di)
