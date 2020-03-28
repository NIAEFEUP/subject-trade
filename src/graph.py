import edge

class Graph:
    def __init__(self):
        self.nodes = {}
        self.id = 0

    def add_root(self, root):
        self.nodes[str(root.state)] = root

    def add_node(self, incoming, node):
        e = edge.Edge(incoming, node)
        incoming.add_edge(e)
        node.add_edge(e)
        self.nodes[str(node.state)] = node

    def get_id(self):
        a = self.id
        self.id += 1
        return a
