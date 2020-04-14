class Edge:
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2
        self.pheromones = 1

    def __str__(self):
        if self.node_1.id < self.node_2.id:
            return 'Edge: ' + str(self.node_1) + ' ' + str(self.node_2)
        else:
            return 'Edge: ' + str(self.node_2) + ' ' + str(self.node_1)

    def __eq__(self, other):
        if (self.node_1 == other.node_1 and self.node_2 == other.node_2) or (self.node_1 == other.node_2 and self.node_2 == other.node_1):
            return True
        else: return False