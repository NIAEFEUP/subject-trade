from time import time

from genetic_algorithm import GeneticAlgorithm, GeneticState
from ant_colony import AntColony, GenerateState
from data_bank import DataBank

It_Without_G_Better= 5000

class ACOGA:
    @staticmethod
    def acoga(root, IT_WITHOUT_G_BETTER=It_Without_G_Better):
        t1 = time()
        best_states = AntColony.ant_colony(root, IT_WITHOUT_G_BETTER)
        t2 = time()
        print('Ant Colony time:', t2 - t1)
        print('Current best:', best_states[0].heuristic)

        best_states = [GeneticState(state.state) for state in best_states]

        t1 = time()
        ret = GeneticAlgorithm.genetic_algorithm(best_states, IT_WITHOUT_G_BETTER)
        t2 = time()
        print('Genetic Algorithm time:', t2 - t1)
        return ret

# # # # # Test what happens with diff number of students

# list_of_states = DataBank.get_states_with_different_number()

# time_ant_colony = 0
# time_genetic_algorithm = 0
# time_acoga = 0

# for i, s in enumerate(list_of_states):
#     print('Initial state heuristic:', s.get_score(), '\n')

#     print('Ant colony with', str((i+1) * 2), 'students')
#     t1 = time()
#     print('Heuristic of:', AntColony.ant_colony(s)[0].heuristic)
#     t2 = time()
#     time_acoga += t2 - t1
#     print('Took', t2 - t1, 'seconds\n\n')

# # # # # Test what happens with more iterations

# root_state = DataBank.get_state_2()

# list_of_iterations = [500, 1000, 2000, 5000, 10000, 20000]

# for iterations in list_of_iterations:
#     t1 = time()
#     print('Heuristic value', ACOGA.acoga(root_state, iterations)[0].heuristic)
#     t2 = time()
#     print('Total time:', t2 - t1, '\n\n')


# # # # # Test how different number of students affects.

# list_of_states = DataBank.get_states_with_different_number()

# time_ant_colony = 0
# time_genetic_algorithm = 0
# time_acoga = 0

# for i, s in enumerate(list_of_states):
#     print('Initial state heuristic:', s.get_score(), '\n')

#     print('Acoga: ' + str(i))
#     t1 = time()
#     print('Heuristic of:', ACOGA.acoga(s)[0].heuristic)
#     t2 = time()
#     time_acoga += t2 - t1
#     print('Took', t2 - t1, 'seconds\n\n')

# # # # Test mean time and heuristic values

root_state = GenerateState.get_great_state(['A','B','C'], 200)
root_state.get_score()

print('Initial state score', root_state.heuristic)


mean_heuristic_ant_colony = 0
mean_heuristic_genetic_algorithm = 0
mean_heuristic_acoga = 0

mean_time_ant_colony = 0
mean_time_genetic_algorithm = 0
mean_time_acoga = 0

N_ITERATIONS = 1

for i in range(N_ITERATIONS):
    print('Acoga: ' + str(i))
    t1 = time()
    mean_heuristic_acoga += ACOGA.acoga(root_state)[0].heuristic
    t2 = time()
    mean_time_acoga += t2 - t1
    
    print('Genetic Algorithm: ' + str(i))
    t1 = time()
    pop = GeneticAlgorithm.random_initial_population(root_state)
    mean_heuristic_genetic_algorithm += GeneticAlgorithm.genetic_algorithm(pop)[0].heuristic
    t2 = time()
    mean_time_genetic_algorithm += t2 - t1

mean_heuristic_ant_colony = mean_heuristic_ant_colony/N_ITERATIONS
mean_heuristic_genetic_algorithm = mean_heuristic_genetic_algorithm/N_ITERATIONS
mean_heuristic_acoga = mean_heuristic_acoga/N_ITERATIONS

mean_time_ant_colony = mean_time_ant_colony/N_ITERATIONS
mean_time_genetic_algorithm = mean_time_genetic_algorithm/N_ITERATIONS
mean_time_acoga = mean_time_acoga/N_ITERATIONS


print('\n\n\n')
print('Ant Colony mean time: ' + str(mean_time_ant_colony))
print('Ant Colony mean heuristic: ' + str(mean_heuristic_ant_colony))

print('\n')
print('Genetic Algorithm mean time: ' + str(mean_time_genetic_algorithm))
print('Genetic Algorithm mean heuristic: ' + str(mean_heuristic_genetic_algorithm))

print('\n')
print('Acoga mean time: ' + str(mean_time_acoga))
print('Acoga mean heuristic: ' + str(mean_heuristic_acoga))