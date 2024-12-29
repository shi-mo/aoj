class Node:
    def __init__(self,id):
        self.node_id = id
        self.parent = None
        self.left  = None
        self.right = None

    def enum_id_preorder(self):
        l = []
        l += [self.node_id]
        if self.left:
            l += self.left.enum_id_preorder()
        if self.right:
            l += self.right.enum_id_preorder()
        return l

    def enum_id_inorder(self):
        l = []
        if self.left:
            l += self.left.enum_id_inorder()
        l += [self.node_id]
        if self.right:
            l += self.right.enum_id_inorder()
        return l

    def enum_id_postorder(self):
        l = []
        if self.left:
            l += self.left.enum_id_postorder()
        if self.right:
            l += self.right.enum_id_postorder()
        l += [self.node_id]
        return l

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
    if right: right.parent = nd

root = None
for nd in nodes:
    if not nd.parent:
        root = nd
        break

print('Preorder\n ', end='')
print(*root.enum_id_preorder())
print('Inorder\n ', end='')
print(*root.enum_id_inorder())
print('Postorder\n ', end='')
print(*root.enum_id_postorder())
