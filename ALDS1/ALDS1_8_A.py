class BTree:
    def __init__(self):
        self.root = None

    def insert(self, k):
        nd = BTreeNode(k)
        p = None
        x = self.root
        while x is not None:
            p = x
            if nd.key < x.key: x = x.left
            else: x = x.right
        nd.p = p

        if p is None:
            self.root = nd
        elif nd.key < p.key:
            p.left = nd
        else:
            p.right = nd
        return self

    def keys_inorder(self):
        if self.root is None: return []
        return self.root.keys_inorder()

    def keys_preorder(self):
        if self.root is None: return []
        return self.root.keys_preorder()

class BTreeNode:
    def __init__(self, k):
        self.key = k
        self.p = None
        self.left = None
        self.right = None

    def keys_inorder(self):
        l = []
        if self.left:
            l += self.left.keys_inorder()
        l += [self.key]
        if self.right:
            l += self.right.keys_inorder()
        return l

    def keys_preorder(self):
        l = []
        l += [self.key]
        if self.left:
            l += self.left.keys_preorder()
        if self.right:
            l += self.right.keys_preorder()
        return l

m = int(input())
t = BTree()

for _ in range(m):
    op,*v = [x for x in input().split()]
    if 'insert' == op:
        t.insert(int(v[0]))
    else:
        ki = t.keys_inorder()
        if ki:
            print(' ', end='')
            print(*ki)
        else:
            print()

        kp = t.keys_preorder()
        if kp:
            print(' ', end='')
            print(*kp)
        else:
            print()
