class Node:
    def __init__(self,id):
        self.node_id = id
        self.left  = None
        self.right = None

    def enum_id_postorder(self):
        l = []
        if self.left:
            l += self.left.enum_id_postorder()
        if self.right:
            l += self.right.enum_id_postorder()
        l += [self.node_id]
        return l

def make_tree_from(pl: list, il: list, n: int):
    if not pl: return None
    root_id = pl[0]
    root = Node(root_id)

    n_left = il.index(root_id)
    root.left = make_tree_from(pl[1:1+n_left], il[0:n_left], n_left)
    n_right = n - n_left - 1
    root.right = make_tree_from(pl[1+n_left:n], il[1+n_left:n], n_right)
    return root

n = int(input())
pl = [int(x) for x in input().split()]
il = [int(x) for x in input().split()]

root = make_tree_from(pl, il, n)
print(*root.enum_id_postorder())
