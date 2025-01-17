class UnionFindTree:
    def __init__(self, N):
        self.parent_of = [0] * N
        for i in range(N):
            self.parent_of[i] = i

    def root_of(self, x):
        px = self.parent_of[x]
        if x == px: return x
        rx = self.root_of(px)
        if px != rx:
            self.parent_of[x] = rx
        return rx

    def unite(self, x, y):
        rx = self.root_of(x)
        ry = self.root_of(y)
        if rx == ry: return
        self.parent_of[ry] = rx

    def is_same(self, x, y):
        rx = self.root_of(x)
        ry = self.root_of(y)
        return rx == ry

def main():
    n, q = [int(x) for x in input().split()]
    uft = UnionFindTree(n)

    for i in range(q):
        cmd, x, y = [int(d) for d in input().split()]
        if 0 == cmd:
            if uft.is_same(x, y): continue
            uft.unite(x, y)
            continue
        print(1 if uft.is_same(x, y) else 0)

main()