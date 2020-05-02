from queue import PriorityQueue

from graph import Graph
from node  import Node
from edge import Edge
from ant import Ant
from state import State

from generator import get_random_state


subjects = ['BDAD', 'LPOO', 'LGP']
n_students = 50

def calculate_if_rose(new, old):
    if new > 0 and old > 0 and new/old > 1.1:
        return True
    
    if new > 0 and old < 0 and abs(new/old) > 1.1:
        return True

    if new < 0 and old < 0 and new/old <= 0.5:
        return True
    
    return False

def ant_colony():
    iterations_total = 10
    iterator = iterations_total
    percentage = 0.1
    best_10 = []
    root_state = get_random_state(subjects, n_students)


    g = Graph()
    g.add_root(Node(root_state, g.get_id()))

    maximum = g.root
    best_10.append(g.root)
    best_10.sort(reverse=True, key=lambda node: node.heuristic)

    while iterator > 0:
        current_ant = Ant(1,1,g.root,g)

        while not current_ant.explore():
            if len(current_ant.get_curr_node_new_neighbours()) == 0:
                break
            else:
                current_ant.chooses_path()
            
        current_ant.deposit_pheromones()
        ret_node = current_ant.expand_node()

        best_10.append(ret_node)
        best_10.sort(reverse=True, key=lambda node: node.heuristic)

        if len(best_10) > 10:
            best_10.pop(10)
            
        if maximum.heuristic < ret_node.heuristic:
            maximum = ret_node

        if calculate_if_rose(ret_node.heuristic, maximum.heuristic):
            iterator = iterations_total
        else:
            iterator -= 1

    return best_10

    

g = ant_colony()
print(g)