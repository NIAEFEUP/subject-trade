from student import Student 
from hour import Hour 
from state import State 

import random 

# Func
def generator_students(n_students, subjects):
    generated_students = []
    for i in range(n_students+1):
        subject_classes ={}
        subject_target = {}
        subject_give_in = {}
        number_classes = random.randint(1,7)
        for _ in range(number_classes+1):                                    #generates the subject classes
            subject = random.choice(subjects)
            if subject not in subject_classes.keys(): 
                subject_classes[subject] = random.randint(1,13)
        print(subject_classes)       

            
        #comment
        #s = Student(20180000+i, subject_classes, subject_target, subject_give_in, {}) 
        #generated_students.append(s) 
    
    #return generated_students 


# Function that generates the schedule for classes givin the list of classes and the state
def time_generator(subjects, state): 
    for number, subject in enumerate(subjects):
        for j in range(14): 
            hour_2 = Hour(number, j*2)
            state.add_schedule(subject, j, hour_2, Hour(hour_2.hours, j*2+1))
    return state 

state = State()
time_generator(['TCOM', 'FIS', 'LCOM', 'MPCP', 'FIS2', 'CMAT', 'AMAT', 'BDAD'], state)
generator_students(4,['TCOM', 'FIS', 'LCOM', 'MPCP', 'FIS2', 'CMAT', 'AMAT', 'BDAD'])

