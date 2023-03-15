class Bfs:
    def __init__(self, n, a):
        self.n = n
        self.adj = a
        self.d = [-1]*n

    def bfs(self):
        self.d[0] = 0
        for d in range(n):
            for i,di in enumerate(self.d):
                if di != d:
                    continue

                for v in self.adj[i]:
                    if 0 <= self.d[v-1]:
                        continue
                    self.d[v-1] = d+1

n = int(input())

a = [None]*n
for _ in range(n):
    u,k,*v = [int(x) for x in input().split()]
    a[u-1] = v

bfs = Bfs(n, a)
bfs.bfs()

for i in range(n):
    u = i+1
    print(*[u,bfs.d[i]])
