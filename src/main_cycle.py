import math
from queue import PriorityQueue
import random

from hour import Hour
from schedule import Schedule
from student import Student
import state as S
import macros
import generator as Gen

def hill_climbing(students):
    state = S.State()
    for student in students:
        state.add_student(student)
    
    number_of_tries = 0
    state.set_score()
    while number_of_tries < macros.hill_climbing_tries:
        for s in state.generate_neighbour():
            s.set_score()
            if s.score > state.score:
                state = s
                number_of_tries = 0
            else:
                number_of_tries += 1

            if number_of_tries > macros.hill_climbing_tries:
                break
    
    return state

def steepest_ascent_hill_climbing(students):
    state = S.State()
    for student in students:
        state.add_student(student)
    
    number_of_tries = 0
    while number_of_tries < macros.steepest_ascent_tries:
        state.set_score()
        counter = 0
        q = PriorityQueue()
        
        for s in state.generate_neighbour():
            s.set_score()
            if counter >= macros.steepest_number: break
            q.put(s)
            counter += 1
        
        best = q.get()

        if best.score > state.score:
            state = s
            number_of_tries = 0
        else:
            number_of_tries += 1
        
        if number_of_tries > macros.steepest_ascent_tries:
            break

    return state

def simulated_annealing(students):
    state = S.State()
    for student in students:
        state.add_student(student)
    
    temperature = 1
    number_of_tries = 0
    while True:
        temperature = 1 - number_of_tries * macros.simulated_annealing_step
        if temperature == 0: return state
        
        state.set_score()
        s = state.generate_neighbour()
        s.set_score()

        if s.score > state.score:
            state = s
        else: 
            delta = (s.score - state.score) / (s.score + state.score) 
            probability = math.exp(delta / temperature)
            if random.random() <= probability: 
                state = s
        number_of_tries += 1

    return state
        
        
#print("olhaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\n\olhaaaaaaaaaaaaaaaaaaaaaaaaaaaaolhaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\nolhaaaaaaaaaaaaaaaaaaaaaaaaaaaaolhaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
state = S.State()
Gen.time_generator(['TCOM', 'FIS', 'LCOM', 'MPCP'], state)
students = Gen.generator_students(5,['TCOM', 'FIS', 'LCOM', 'MPCP'])

for i in state.get_schedule(): 
    print(i)
#state = hill_climbing(students)

#print(state)