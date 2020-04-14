from graph import Graph
from node  import Node
from edge import Edge
from ant import Ant


# Create graph
g = Graph()

# Add initial node
g.add_root(Node(1,g.get_id()))

current_ant = Ant(1,1,g.root,g)
ret_node = current_ant.expand_node()


# # # # # # # # # # # # # # # # # # # # # # # # # # current_ant.update_node(ret_node)
# # # # # # # # # # # # # # # # # # # # # # # # # # current_ant.expand_node()
# # # # # # # # # # # # # # # # # # # # # # # # # # print(str(g))
# Gerar ants

for i in range(0,1000):
    current_ant = Ant(1,1,g.root,g)
    while not current_ant.explore():
        if len(current_ant.current_node.get_nodes()) == 0:
            break
        else:
            current_ant.chooses_path()

        
    current_ant.deposit_pheromones()
    ret_node = current_ant.expand_node()

print(g)