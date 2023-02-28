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

    def find(self, k):
        if self.root is None:
            return None

        nd = self.root
        while nd is not None:
            if k == nd.key:
                return nd 
            elif k < nd.key:
                nd = nd.left
            else:
                nd = nd.right
        return None

    def delete(self, k):
        x,lr = self._find_with_lr(k)
        if x is None:
            return False

        if not (x.left or x.right):
            self._splice_node(x, lr, None)
            return True
        if x.left and x.right:
            m,lr = self._find_min_lr(x.right)
            x.key = m.key
            self._splice_node(m, lr, m.right)
            return True
        self._splice_node(x, lr, x.left or x.right)
        return True

    def _find_with_lr(self, k):
        lr = None
        x = self.root
        while x is not None:
            if k == x.key:
                break
            elif k < x.key:
                lr = 'left'
                x = x.left
            else:
                lr = 'right'
                x = x.right
        return x,lr

    def _find_min_lr(self, x):
        lr = 'right'
        while x and x.left:
            x = x.left
            lr = 'left'
        return x,lr

    def _splice_node(self, x, lr, y):
        if x.p is None:
            self.root = y
        else:
            setattr(x.p, lr, y)
        if y is not None:
            y.p = x.p

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
    elif 'find' == op:
        print('yes' if t.find(int(v[0])) else 'no')
    elif 'delete' == op:
        t.delete(int(v[0]))
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
