from random import randint

class Node:
    def __init__(self, state, id):
        self.state = state
        self.edges = {}
        self.id = id
        self.heuristic = self.get_heuristic()
    
    def add_edge(self, edge):
        if str(edge) not in self.edges:
            self.edges[str(edge)] = edge

    def get_nodes(self):
        l = []
        for edge in self.edges.values():
            l.append(edge.get_other(self))
        return l
        
    def get_heuristic(self): # To be replaced by state.get_score
        # return self.state
        return self.state.get_score()

    def get_sum(self, alpha, beta):
        s = 0
        for edge in self.edges.values():
            other_node = None
            if edge.node_1.id != self.id:
                other_node = edge.node_1
            else: other_node = edge.node_2

            s += (edge.pheromones ** alpha) * (other_node.heuristic ** beta)
        return s

    def return_new_state(self): # To be replaced by random_neighbour
        # return randint(0, 100)
        return self.state.random_neighbour()

    def __str__(self):
        return 'Node: ' + str(self.state)

    def __repr__(self):
        return 'Node: ' + str(self.state)

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False

    def __lt__(self, other):
        if self.heuristic < other.heuristic:
            return self
        else:
            return other
