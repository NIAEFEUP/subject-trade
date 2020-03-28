class Node:
    def __init__(self, state, id):
        self.state = state
        self.edges = {}
        self.id = id
    
    def add_edge(self, edge):
        if str(edge) not in self.edges:
            self.edges[str(edge)] = edge

    def __str__(self):
        return str(self.state)

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False