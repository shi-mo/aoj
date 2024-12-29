class Dfs:
    def __init__(self, n, a):
        self.time = 1
        self.n = n
        self.adj = a
        self.d = [None]*n
        self.f = [None]*n

    def dfs(self):
        for i in range(self.n):
            self.dfs_for(i+1)
            if None not in self.d:
                break

    def dfs_for(self, u):
        if self.d[u-1] is not None:
            return

        self.d[u-1] = self.time
        self.time += 1
        for v in self.adj[u-1]:
            self.dfs_for(v)
        self.f[u-1] = self.time
        self.time += 1

n = int(input())

a = [None]*n
for _ in range(n):
    u,k,*v = [int(x) for x in input().split()]
    a[u-1] = v

dfs = Dfs(n, a)
dfs.dfs()

for i in range(n):
    u = i+1
    print(*[u,dfs.d[i],dfs.f[i]])
