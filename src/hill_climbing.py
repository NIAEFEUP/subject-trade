import math
from queue import PriorityQueue
import random
from time import perf_counter

from hour import Hour
from schedule import Schedule
from student import Student
from state import State
from generator import GenerateState
from data_bank import DataBank


Xi = 2500
steepest_ascent_number = 5
simulated_annealing_step = 0.00005

class HillClimbingVariants:
    @staticmethod
    def hill_climbing(state): 
        number_of_tries = 0
        state.get_score()
        while number_of_tries < Xi:
            s = state.random_neighbour()
            s.get_score()
            if s.heuristic > state.heuristic:
                state = s
                number_of_tries = 0
            else:
                number_of_tries += 1
                if number_of_tries % 1000 == 0:
                    print(number_of_tries, state.heuristic)

            if number_of_tries > Xi:
                break
        return state

    @staticmethod
    def steepest_ascent_hill_climbing(state):
        number_of_tries = 0
        while number_of_tries < Xi:
            state.get_score()
            counter = 0
            q = PriorityQueue()
            
            while counter < steepest_ascent_number:
                s = state.random_neighbour()
                s.get_score()
                q.put(s)
                counter += 1
            
            best = q.get()

            if best.heuristic > state.heuristic:
                state = s
                number_of_tries = 0
            else:
                number_of_tries += 1
                if number_of_tries % 1000 == 0:
                    print(number_of_tries, state.heuristic)
            
            if number_of_tries > Xi:
                break

        return state

    @staticmethod
    def simulated_annealing(state):
        temperature = 1
        number_of_tries = 0
        best_state = state
        while True:
            temperature = 1 - number_of_tries * simulated_annealing_step
            if temperature <= 0: return best_state
            
            state.get_score()
            s = state.random_neighbour()
            s.get_score()

            if s.heuristic > state.heuristic:
                state = s

            if s.heuristic > best_state.heuristic:
                best_state = s

            else: 
                delta = (s.heuristic - state.heuristic) / (s.heuristic + state.heuristic) 
                probability = math.exp(delta / temperature)
                if random.random() <= probability: 
                    state = s
            number_of_tries += 1

        return state
        
        

state = GenerateState.get_great_state(['a', 'c', 'd', 'f', 'z'], 20)
state.get_score()
print(state.heuristic)
print('Conflicts', state.conflicts)

t1 = perf_counter()
ret = HillClimbingVariants.hill_climbing(state)
ret2 = HillClimbingVariants.hill_climbing(state)
ret3 = HillClimbingVariants.hill_climbing(state)
t2 = perf_counter()

print(max(ret.heuristic, ret2.heuristic, ret3.heuristic))
#print(ret.heuristic, round(t2-t1, 2))
#print('Conflicts', ret.conflicts)