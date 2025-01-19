class UnionFindTreeWeighted:
    def __init__(self, n):
        self.parent_of = [0] * n
        for i in range(n): self.parent_of[i] = i
        self.diff_weight = [0] * n

    def root_of(self, x):
        px = self.parent_of[x]
        if x == px: return x
        rx = self.root_of(px)
        if px != rx:
            self.parent_of[x] = rx
            self.diff_weight[x] += self.diff_weight[px]
        return rx

    def weight_of(self, x):
        self.root_of(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        return self.weight_of(y) - self.weight_of(x)

    def is_same(self, x, y):
        return self.root_of(x) == self.root_of(y)

    def merge(self, x, y, z):
        w = z + self.weight_of(x) - self.weight_of(y)
        x = self.root_of(x); y = self.root_of(y)
        if x == y: return
        self.parent_of[y] = x
        self.diff_weight[y] = w

def main():
    n, q = [int(x) for x in input().split()]
    uft = UnionFindTreeWeighted(n)

    for i in range(q):
        v = [int(d) for d in input().split()]
        cmd, x, y, z = (v + ([0] * 4))[:4]
        if 0 == cmd:
            uft.merge(x, y, z)
            continue
        print(uft.diff(x, y) if uft.is_same(x, y) else '?')

main()