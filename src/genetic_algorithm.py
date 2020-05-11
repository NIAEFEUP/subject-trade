from random import sample
from copy import deepcopy
from time import sleep

from genetic_state import GeneticState

INITIAL_POPULATION_SIZE = 4
STATE_SIZE = 10
MAX_ELEMENTS = 50

population = [GeneticState(GeneticState.gen_binary(STATE_SIZE)) for _ in range(INITIAL_POPULATION_SIZE)]


def genetic_algorithm(population):
    new_population = population
    
    while new_population[0].int() != ((2 ** STATE_SIZE) - 1):
        new_population = deepcopy(population)
        
        i = 0
        while len(population) > 0:
            i+= 1

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
        print(new_population[0].int())
        
    return new_population[0]
        
print(genetic_algorithm(population))

