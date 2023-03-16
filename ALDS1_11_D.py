from collections import deque

n, m = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for _ in range(m):
    s, t = [int(x) for x in input().split()]
    g[s].append(t)
    g[t].append(s)

roots = [None]*n
for s in range(n):
    if roots[s] is not None:
        continue

    roots[s] = s
    que = deque([s])
    while que:
        v = que.popleft()
        for u in g[v]:
            if roots[u] is not None:
                continue
            roots[u] = s
            que.append(u)


q = int(input())
for _ in range(q):
    s, t = [int(x) for x in input().split()]
    print('yes' if roots[s] == roots[t] else 'no')
