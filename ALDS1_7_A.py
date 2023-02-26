class Node:
    def __init__(self,id):
        self.node_id = id
        self.parent = None
        self.lchild = None
        self.rsibling = None

    def parent_id(self):
        return self.parent.node_id if self.parent else -1

    def type(self):
        if not self.parent: return 'root'
        if not self.lchild: return 'leaf'
        return 'internal node'

    def depth(self):
        d = 0
        nd = self
        while nd.parent:
            d += 1
            nd = nd.parent
        return d

    def children(self):
        l = []
        nd = self.lchild
        while nd:
            l.append(nd.node_id)
            nd = nd.rsibling
        return l

n = int(input())
nodes = [Node(i) for i in range(n)]

for _ in range(n):
    id,k,*c = [int(x) for x in input().split()]
    nd = nodes[id]
    if c: nd.lchild = nodes[c[0]]
    for i in range(k):
        child = nodes[c[i]]
        child.parent = nd
        if i < k-1: child.rsibling = nodes[c[i+1]]

for nd in nodes:
    cl = ', '.join([str(id) for id in nd.children()])
    print(f'node {nd.node_id:d}: parent = {nd.parent_id():d}, ' +
        f'depth = {nd.depth():d}, {nd.type():s}, [{cl:s}]')
