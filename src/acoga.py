from time import time

from genetic_algorithm import GeneticAlgorithm, GeneticState
from ant_colony import AntColony, GenerateState
from data_bank import DataBank


class ACOGA:
    @staticmethod
    def acoga(root):
        #print('Ant Colony')
        best_states = AntColony.ant_colony(root)
        best_states = [GeneticState(state.state) for state in best_states]
        #print('Genetic Algorithm')
        return GeneticAlgorithm.genetic_algorithm(best_states)


root_state = DataBank.get_state_2()

mean_heuristic_ant_colony = 0
mean_heuristic_genetic_algorithm = 0
mean_heuristic_acoga = 0

mean_time_ant_colony = 0
mean_time_genetic_algorithm = 0
mean_time_acoga = 0

for i in range(10):
    print('Ant Colony: ' + str(i))
    t1 = time()
    mean_heuristic_ant_colony += AntColony.ant_colony(root_state)[0].heuristic
    t2 = time()
    mean_time_ant_colony += t2 - t1
    
    print('Genetic Algorithm: ' + str(i))
    t1 = time()
    pop = GeneticAlgorithm.random_initial_population(root_state)
    mean_heuristic_genetic_algorithm += GeneticAlgorithm.genetic_algorithm(pop)[0].heuristic
    t2 = time()
    mean_time_genetic_algorithm += t2 - t1

    print('Acoga: ' + str(i))
    t1 = time()
    mean_heuristic_acoga = ACOGA.acoga(root_state)[0].heuristic
    t2 = time()
    mean_time_acoga += t2 - t1

mean_heuristic_ant_colony = mean_heuristic_ant_colony/10
mean_heuristic_genetic_algorithm = mean_heuristic_genetic_algorithm/10
mean_heuristic_acoga = mean_heuristic_acoga/10

mean_time_ant_colony = mean_time_ant_colony/10
mean_time_genetic_algorithm = mean_time_genetic_algorithm/10
mean_time_acoga = mean_time_acoga/10


print('\n\n\n')
print('Ant Colony mean time: ' + str(mean_time_ant_colony))
print('Ant Colony mean heuristic: ' + str(mean_heuristic_ant_colony))

print('\n')
print('Genetic Algorithm mean time: ' + str(mean_time_genetic_algorithm))
print('Genetic Algorithm mean heuristic: ' + str(mean_heuristic_genetic_algorithm))

print('\n')
print('Acoga mean time: ' + str(mean_time_acoga))
print('Acoga mean heuristic: ' + str(mean_heuristic_acoga))