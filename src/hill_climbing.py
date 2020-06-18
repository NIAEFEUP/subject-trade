import math
import random
from time import perf_counter

from hour import Hour
from schedule import Schedule
from student import Student
from state import State
from generator import GenerateState
from data_bank import DataBank


Xi = 5000
steepest_ascent_number = 5
simulated_annealing_step = 0.0005
restart_number = 10

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

            if number_of_tries > Xi:
                break
        return state

    @staticmethod
    def random_restart_hill_climbing(state):
        best_state = HillClimbingVariants.hill_climbing(state)
        
        for _ in range(restart_number):
            s = state
            for _ in range(100):
                s = s.random_neighbour()
            if s.heuristic > best_state.heuristic:
                best_state = s

        return best_state

    @staticmethod
    def steepest_ascent_hill_climbing(state):
        number_of_tries = 0
        while number_of_tries < Xi:
            state.get_score()
            counter = 0
            q = []
            
            while counter < steepest_ascent_number:
                s = state.random_neighbour()
                s.get_score()
                q.append(s)
                counter += 1
            
            q.sort(reverse=True, key=lambda node: node.heuristic)
            best = q[0]

            if best.heuristic > state.heuristic:
                state = s
                number_of_tries = 0
            else:
                number_of_tries += 1
            
            if number_of_tries > Xi:
                break

        return state

    @staticmethod
    def simulated_annealing(state):
        temperature = 1
        iterations = 0
        number_of_tries = 0
        best_state = state
        while number_of_tries < Xi:
            temperature = 1 - iterations * simulated_annealing_step
            
            state.get_score()
            s = state.random_neighbour()
            s.get_score()

            if s.heuristic > state.heuristic:
                state = s

            if s.heuristic > best_state.heuristic:
                number_of_tries = 0
                best_state = s

            elif temperature > 0: 
                delta = (s.heuristic - state.heuristic) / (s.heuristic + state.heuristic) 
                probability = math.exp(delta / temperature)
                if random.random() <= probability: 
                    state = s
            iterations += 1

            if temperature <= 0:
                number_of_tries += 1

        return best_state
        
        

state = DataBank.get_state_2()
state.get_score()
print(state.heuristic, '\n')

print('Hill Climbing')

t1 = perf_counter()
ret = HillClimbingVariants.hill_climbing(state)
t2 = perf_counter()

print('Heuristic', ret.heuristic)
print('Time', round(t2-t1, 2), '\n')

print('Random Restart Hill Climbing')

t1 = perf_counter()
ret = HillClimbingVariants.random_restart_hill_climbing(state)
t2 = perf_counter()

print('Heuristic', ret.heuristic, '\n', 'Time', round(t2-t1, 2), '\n')

print('Steepest Ascent Hill Climbing')

t1 = perf_counter()
ret = HillClimbingVariants.steepest_ascent_hill_climbing(state)
t2 = perf_counter()

print('Heuristic', ret.heuristic, '\n', 'Time', round(t2-t1, 2), '\n')

print('Simulated Annealing')

t1 = perf_counter()
ret = HillClimbingVariants.simulated_annealing(state)
t2 = perf_counter()

print('Heuristic', ret.heuristic, '\n', 'Time', round(t2-t1, 2), '\n')