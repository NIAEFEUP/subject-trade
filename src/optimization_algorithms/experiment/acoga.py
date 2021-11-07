from time import time

from src.optimization_algorithms.ant_colony.ant_colony import AntColony
from src.optimization_algorithms.genetic_algorithm.genetic_algorithm import \
    GeneticAlgorithm
from src.optimization_algorithms.genetic_algorithm.genetic_state import \
    GeneticState


class ACOGA:
    IT_WITHOUT_G_BETTER= 5000

    @staticmethod
    def acoga(root):
        t1 = time()
        best_states = AntColony.ant_colony(root)
        t2 = time()
        print('Ant Colony time:', t2 - t1)
        print('Current best:', best_states[0].heuristic)

        best_states = [GeneticState(state.state) for state in best_states]

        t1 = time()
        ret = GeneticAlgorithm.genetic_algorithm(best_states)
        t2 = time()
        print('Genetic Algorithm time:', t2 - t1)
        return ret
