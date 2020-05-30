from random import sample
from copy import deepcopy
from time import sleep
from random import randint

from genetic_state import GeneticState
from data_bank import DataBank

INITIAL_POPULATION_SIZE = 2
MAX_ELEMENTS = 100
IT_WITHOUT_G_BETTER = 2000

class GeneticAlgorithm:
    @staticmethod
    def random_initial_population(first_state):
        '''
        Receives a state and generates several random other.
        '''
        population = [GeneticState(first_state)]

        while len(population) < INITIAL_POPULATION_SIZE:
            state = population[0].state
            number_of_students = len(state.students)

            number_of_changes = randint(number_of_students * 2, number_of_students * 5)

            for _ in range(number_of_changes):
                state = state.random_neighbour()

            population.append(GeneticState(state))

        return population

    @staticmethod
    def genetic_algorithm(population):
        '''
        Receives initial population and performs a genetic algorithm
        '''
        new_population = population

        highest_value = max(population, key = lambda s: s.heuristic)
        highest_value = highest_value.heuristic
        counter = IT_WITHOUT_G_BETTER

        while counter > 0:
            new_population = deepcopy(population)
            
            i = 0
            while len(population) > 1:
                i += 1

                enum_pop = list(enumerate(population, start = 0))
                dad = sample(enum_pop, 1)[0]
                population.pop(int(dad[0]))
                
                enum_pop = list(enumerate(population, start = 0))
                mum = sample(enum_pop, 1)[0]
                population.pop(int(mum[0]))

                off_spring1, off_spring2 = dad[1].gen_off_spring(mum[1])

                off_spring1.mutate()
                off_spring2.mutate()

                new_population.append(off_spring1)
                new_population.append(off_spring2)

            new_population.sort(reverse=True, key=lambda node: node.heuristic)
            population = deepcopy(new_population[:MAX_ELEMENTS])

            if population[0].heuristic > highest_value:
                print('new best value', population[0].heuristic)
                highest_value = population[0].heuristic
                counter = IT_WITHOUT_G_BETTER
            else:
                counter -= 1
            
        return new_population



# first_state = DataBank.get_state_0()
# population = GeneticAlgorithm.random_initial_population(first_state)
# results = GeneticAlgorithm.genetic_algorithm(population)

# print('Final result', results[0].heuristic)