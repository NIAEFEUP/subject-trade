import random

class Ant:
    def __init__(self, alpha, beta, node, graph):
        self.alpha = alpha
        self.beta = beta
        self.node = node
        self.edges_path = []
        self.visited_nodes = []
        self.deposit_level = 2
        self.evaporation_level = 1
        self.graph = graph

    def chooses_path(self, current_node):
        s = current_node.get_sum(self.alpha, self.beta)
        rand_val = random.randint(1, s)
        
        edges = []
        for _, b in current_node.edges.items():
            edges.append(b)

        #probabilities range
        e = []
        for i, edge in enumerate(edges):

            other_node = None
            if edge.node_1.id != current_node.id:
                other_node = edge.node_1
            else: other_node = edge.node_2

            if i != 0:
                e.append((edge.pheromones ** self.alpha) * (other_node.heuristic ** self.beta) + e[len(e) - 1])
            else: 
                e.append((edge.pheromones ** self.alpha) * (other_node.heuristic ** self.beta))

        for i, element in enumerate(e):
            if rand_val <= element:

                other_node = None
                if edges[i].node_1.id != current_node.id:
                    other_node = edges[i].node_1
                else: other_node = edges[i].node_2
                
                return (other_node, edges[i])


    def update_node(self, node):
        self.node = node

    def deposit_pheromones(self):
        for _, node in self.graph.nodes.items():
            for _, edge in node.edges.items():
                edge.pheromones -= self.evaporation_level

            for e in self.edges_path:
                if str(e) in node.edges:
                    node.edges[str(e)].pheromones += self.deposit_level

    def explore(self):
        if self.graph.id == 1:
            p = 1
        else:
            a = self.graph.id / 200
            p = 1 / (1-a)
