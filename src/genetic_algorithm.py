from random import sample

from genetic_state import GeneticState

POPULATION_SIZE = 6
STATE_SIZE = 7

population = [GeneticState(GeneticState.gen_binary(STATE_SIZE)) for _ in range(POPULATION_SIZE)]


def genetic_algorithm(population):
    new_population = population

    while new_population[0].int() != 127:
        new_population = population

        i = 0
        while len(population) > 0:
            i+= 1
            #print(i)
            print(population)
            enum_pop = list(enumerate(population, start = 0))

            dad = sample(enum_pop, 1)[0]
            population.pop(int(dad[0]))

            mum = sample(enum_pop, 1)[0]
            population.pop(int(mum[0]))

            off_spring1, off_spring2 = dad[1].gen_off_spring(mum[1])

            off_spring1.mutate()
            off_spring2.mutate()

            new_population.append(off_spring1)
            new_population.append(off_spring2)
        print('left')

        new_population.sort(reverse=True, key=lambda node: node.heuristic)
        
    return new_population[0]
        
print(genetic_algorithm(population))

