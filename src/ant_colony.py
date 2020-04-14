import graph
import node
import edge
import ant


def f(g):
    for _, n in g.nodes.items():
        for _, edge in n.edges.items():
            print(edge)
            print(edge.pheromones)
            print()

g = graph.Graph()

n1 = node.Node(1, g.get_id())
n2 = node.Node(2, g.get_id())
n3 = node.Node(5, g.get_id())
n4 = node.Node(10, g.get_id())
n5 = node.Node(1, g.get_id())

g.add_root(n1)
g.add_node(n1, n2)
g.add_node(n1, n3)
g.add_node(n1, n4)
g.add_node(n1, n5)

a1 = ant.Ant(1, 1, n1, g)
n2, edge = a1.chooses_path(a1.node)

a2 = ant.Ant(1, 1, n2, g)

a2.edges_path.append(edge)
a2.deposit_pheromones()

_, edge = a2.chooses_path(a1.node)
a2.edges_path.append(edge)
a2.deposit_pheromones()

f(g)



