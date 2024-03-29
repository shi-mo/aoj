class Node:
    def __init__(self,id):
        self.node_id = id
        self.parent = None
        self.left  = None
        self.right = None
        self.sibling = None
        self._height = None

    def parent_id(self):
        return self.parent.node_id if self.parent else -1

    def left_id(self):
        return self.left.node_id if self.left else -1

    def right_id(self):
        return self.right.node_id if self.right else -1

    def sibling_id(self):
        return self.sibling.node_id if self.sibling else -1

    def type(self):
        if not self.parent: return 'root'
        if not (self.left or self.right): return 'leaf'
        return 'internal node'

    def degree(self):
        deg = 0
        if self.left:  deg += 1
        if self.right: deg += 1
        return deg

    def depth(self):
        d = 0
        nd = self
        while nd.parent:
            d += 1
            nd = nd.parent
        return d

    def height(self):
        if self._height: return self._height
        if not (self.left or self.right):
            self._height = 0
            return 0

        lh = self.left.height() if self.left else 0
        rh = self.right.height() if self.right else 0
        self._height = 1 + max(lh, rh)
        return self._height

n = int(input())
nodes = [Node(i) for i in range(n)]

for _ in range(n):
    id,l,r = [int(x) for x in input().split()]
    nd = nodes[id]
    left = nodes[l] if 0 <= l else None
    right = nodes[r] if 0 <= r else None
    nd.left = left
    nd.right = right
    if left: left.parent = nd
    if left: left.sibling = right
    if right: right.parent = nd
    if right: right.sibling = left

for nd in nodes:
    print(f'node {nd.node_id:d}: ' +
            f'parent = {nd.parent_id():d}, ' +
            f'sibling = {nd.sibling_id():d}, ' +
            f'degree = {nd.degree():d}, ' +
            f'depth = {nd.depth():d}, ' +
            f'height = {nd.height():d}, ' +
            f'{nd.type():s}')
