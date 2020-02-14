from queue import PriorityQueue


from hour import Hour
from schedule import Schedule
from student import Student
import state as S

tries_macro_shc = 100
tries_macro_sahc = 40
steepest_number = 40

def hill_climbing(students):
    state = S.State()
    for student in students:
        state.add_student(student)
    
    number_of_tries = 0
    while number_of_tries < tries_macro_shc:
        state.set_score()
        for s in state.generate_neighbour():
            if s.get_score() > state.score:
                state = s
                number_of_tries = 0
            else:
                number_of_tries += 1

            if number_of_tries > tries_macro_shc:
                break
    
    return state

def steepest_ascent_hill_climbing(students):
    state = S.State()
    for student in students:
        state.add_student(student)
    
    number_of_tries = 0
    while number_of_tries < tries_macro_sahc:
        state.set_score()
        counter = 0
        q = PriorityQueue()
        
        for s in state.generate_neighbour():
            if counter >= steepest_number: break
            q.put(s)
            counter += 1
        
        best = q.get()
        best.set_score()

        if best.score > state.score:
            state = s
            number_of_tries = 0
        else:
            number_of_tries += 1
        
        if number_of_tries > tries_macro_sahc:
            break