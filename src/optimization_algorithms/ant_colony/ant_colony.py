from src.optimization_algorithms.ant_colony.ant import Ant
from src.optimization_algorithms.ant_colony.graph import Graph
from src.optimization_algorithms.ant_colony.node import Node

It_Without_G_Better = 5000

class AntColony:
    @staticmethod
    def ant_colony(root_state, IT_WITHOUT_G_BETTER=It_Without_G_Better):
        iterator = IT_WITHOUT_G_BETTER
        best_10 = []

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

            if ret_node not in best_10:
                flag = False
                for element in best_10:
                    if ret_node.heuristic == element.heuristic:
                        flag = True
                if not flag:
                    best_10.append(ret_node)
            
            best_10.sort(reverse=True, key=lambda node: node.heuristic)

            if len(best_10) > 10:
                best_10.pop(10)

            if ret_node.heuristic > maximum.heuristic:
                iterator = IT_WITHOUT_G_BETTER
                maximum = ret_node
            else:
                iterator -= 1

        return best_10

# subjects = ['BDAD', 'LPOO', 'LGP', 'DWQ', 'AWS', 'BBPA', 'POWQ']
# n_students = 10   
# root_state = GenerateState.get_random_state(subjects, n_students)

# best = AntColony.ant_colony(root_state)
# for b in best:
#     #print(b, "student_num", b.state.student_num, "conflicts", b.state.conflicts, "didn't get", b.state.didnt_get)
#     print(b.heuristic)
#     # for student in b.state.students.values():
#     #     print(student.student.subject_)
