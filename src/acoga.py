from time import time

from genetic_algorithm import GeneticAlgorithm, GeneticState
from ant_colony import AntColony, GenerateState


class ACOGA:
    @staticmethod
    def acoga(root):
        print('Ant Colony')
        best_states = AntColony.ant_colony(root)
        best_states = [GeneticState(state.state) for state in best_states]
        print('Genetic Algorithm')
        return GeneticAlgorithm.genetic_algorithm(best_states)

subjects = ['BDAD', 'LPOO', 'LGP']
n_students = 50
root_state = GenerateState.get_random_state(subjects, n_students)

t1 = time()
print(ACOGA.acoga(root_state)[0].heuristic)
t2 = time()

print('Time elapsed:', t2-t1)