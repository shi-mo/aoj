def main():
    t, nq, q = load_input()
    g = DAWG(t)
    for i in range(nq):
        if g.match(q[i]): print('1')
        else:             print('0')

def load_input():
    t = input()
    nq = int(input())
    q = [input() for _ in range(nq)]
    return t, nq, q

class DAWG:
    def __init__(self, text):
        cls = self.__class__
        self.text = text
        self.next_id = 0
        self.node_list = []

        root = self.create_node(0)
        self.root = root
        self.terminal = root
        self.bottom = cls.BottomNode(root)
        self.build()

    def create_node(self, length):
        cls = self.__class__
        node = cls.Node(self.next_id)
        self.next_id += 1
        node.length = length
        self.node_list.append(node)
        return node

    def copy_node(self, node, length):
        new_node = self.create_node(length)
        new_node.final = node.final
        for c, v in node.edge_to.items():
            new_node.edge_to[c] = v
        new_node.slink = node.slink
        return new_node

    def build(self):
        for i, c in enumerate(self.text):
            v = self.terminal
            self.terminal = self.create_node(i+1)
            while not v.has_transition_to(c):
                v.edge_to[c] = self.terminal
                v = v.slink
            u = v.next_state(c)
            if v.length + 1 == u.length:
                self.terminal.slink = u
                continue
            new_node = self.copy_node(u, v.length+1)
            v.edge_to[c] = new_node
            u.slink = new_node
            self.terminal.slink = new_node
            v = v.slink
            while v.length + 1 < v.next_state(c).length:
                v.edge_to[c] = new_node
                v = v.slink

    def match(self, pattern):
        node = self.root
        for c in pattern:
            if not node.has_transition_to(c):
                return False
            node = node.next_state(c)
        return True

    class Node:
        def __init__(self, id):
            self.id = id
            self.length = 0
            self.final = False
            self.edge_to = {}
            self.slink = None

        def has_transition_to(self, c):
            return c in self.edge_to
        
        def next_state(self, c):
            return self.edge_to[c]

    class BottomNode(Node):
        def __init__(self, root):
            super().__init__('Bottom')
            self.length = -1
            self.root = root
            root.slink = self

        def has_transition_to(self, c):
            return True
        
        def next_state(self, c):
            return self.root
main()