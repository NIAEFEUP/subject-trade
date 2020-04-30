from queue import PriorityQueue

from graph import Graph
from node  import Node
from edge import Edge
from ant import Ant


# Create graph
# g = Graph()

# # Add initial node
# g.add_root(Node(1,g.get_id()))

# current_ant = Ant(1,1,g.root,g)
# ret_node = current_ant.expand_node()


# # # # # # # # # # # # # # # # # # # # # # # # # # current_ant.update_node(ret_node)
# # # # # # # # # # # # # # # # # # # # # # # # # # current_ant.expand_node()
# # # # # # # # # # # # # # # # # # # # # # # # # # print(str(g))
# Gerar ants


def calculate_if_rose(new, old):
    if new/old > 1.1:
        return True
    return False

def ant_colony():
    iterations_total = 50
    iterator = iterations_total
    percentage = 0.1
    best_10 = PriorityQueue()


    g = Graph()
    g.add_root(Node(1,g.get_id()))

    maximum = g.root
    best_10.put(g.root)

    while iterator > 0:
        current_ant = Ant(1,1,g.root,g)

        while not current_ant.explore():
            if len(current_ant.get_curr_node_new_neighbours()) == 0:
                break
            else:
                current_ant.chooses_path()
            
        current_ant.deposit_pheromones()
        ret_node = current_ant.expand_node()

        # if len(best_10) < 10:
        #     best_10.append(ret_node)
        # else:
            

        if maximum.heuristic < ret_node.heuristic:
            maximum = ret_node

        if calculate_if_rose(ret_node.heuristic, maximum.heuristic):
            iterator = iterations_total
        else:
            iterator -= 1

    return g

    

g = ant_colony()
print(g)