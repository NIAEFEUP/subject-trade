import graph
import node


g = graph.Graph()

n1 = node.Node(1, g.get_id())
n2 = node.Node(2, g.get_id())


g.add_root(n1)
g.add_node(n1, n2)