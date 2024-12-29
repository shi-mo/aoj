class Node:
    def __init__(self, k, priority):
        self.key = k
        self.priority = priority
        self.left = None
        self.right = None

def insert(t: Node, k: int, priority: int):
    if t is None:
        return Node(k, priority)
    if k == t.key:
        return t

    if k < t.key:
        t.left = insert(t.left, k, priority)
        if t.priority < t.left.priority:
            t = right_rotate(t)
    else:
        t.right = insert(t.right, k, priority)
        if t.priority < t.right.priority:
            t = left_rotate(t)
    return t

def find(t: Node, k: int):
    if t is None:
        return None

    while t is not None:
        if k == t.key:
            return t 
        elif k < t.key:
            t = t.left
        else:
            t = t.right
    return None

def delete(t: Node, k: int):
    if t is None:
        return None

    if k < t.key:
        t.left = delete(t.left, k)
    elif t.key < k:
        t.right = delete(t.right, k)
    else:
        return _delete(t, k)
    return t

def _delete(t: Node, k: int):
    if not(t.left or t.right):
        return None

    if t.left is None:
        t = left_rotate(t)
    elif t.right is None:
        t = right_rotate(t)
    else:
        if t.left.priority > t.right.priority:
            t = right_rotate(t)
        else:
            t = left_rotate(t)
    return delete(t, k)

def right_rotate(t: Node):
    s = t.left
    t.left = s.right
    s.right = t
    return s

def left_rotate(t: Node):
    s = t.right
    t.right = s.left
    s.left = t
    return s

def keys_inorder(t: Node):
    if t is None:
        return []

    l = []
    if t.left:
        l += keys_inorder(t.left)
    l += [t.key]
    if t.right:
        l += keys_inorder(t.right)
    return l

def keys_preorder(t: Node):
    if t is None:
        return []

    l = []
    l += [t.key]
    if t.left:
        l += keys_preorder(t.left)
    if t.right:
        l += keys_preorder(t.right)
    return l

m = int(input())
t = None

for _ in range(m):
    op,*v = [x for x in input().split()]
    if 'insert' == op:
        t = insert(t, int(v[0]), int(v[1]))
    elif 'find' == op:
        print('yes' if find(t, int(v[0])) else 'no')
    elif 'delete' == op:
        t = delete(t, int(v[0]))
    else:
        ki = keys_inorder(t)
        if ki:
            print(' ', end='')
            print(*ki)
        else:
            print()

        kp = keys_preorder(t)
        if kp:
            print(' ', end='')
            print(*kp)
        else:
            print()
