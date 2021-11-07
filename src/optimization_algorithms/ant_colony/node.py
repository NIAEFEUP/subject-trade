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
        
    def get_heuristic(self):
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

    def return_new_state(self): 
        return self.state.random_neighbour()

    def __str__(self):
        return 'Node: ' + str(self.state)

    def __repr__(self):
        return 'Node: ' + str(self.state)

    def __eq__(self, other):
        try:
            if len(self.state.students) == len(other.state.students):
                for student, student_class in self.state.students.items():
                    if student in other.state.students.keys():   
                        for subject, clas in student_class.subjects_and_classes.items():
                            if other.state.students[student].subjects_and_classes[subject] == clas:
                                pass
                            else: 
                                return False
                    else: 
                        return False
            else: 
                return False
            return True

        except:
           return False

    def __lt__(self, other):
        if self.heuristic < other.heuristic:
            return self
        else:
            return other
