from copy import deepcopy
from math import ceil
from random import sample


from generator import GenerateState
from data_bank import DataBank

class NewDict:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __repr__(self):
        return 'NewD' + self.dictionary.__repr__()
        
    def items(self):
        return self.dictionary.items()

class GeneticState:
    def __init__(self, state):
        self.state = state
        self.heuristic = self.heuristic()
        self.genetic_state = {}

    def heuristic(self):
        return self.state.heuristic

    def convert_to_genetic_state(self):
        for student_id, student in self.state.students.items():
            for subject, class_ in student.subjects_and_classes.items():
                if not subject in self.genetic_state:
                    self.genetic_state[subject] = NewDict({})

                if not class_ in self.genetic_state[subject].dictionary:
                    self.genetic_state[subject].dictionary[class_] = []

                self.genetic_state[subject].dictionary[class_].append(student_id)

    @staticmethod
    def convert_to_normal_state(received_state, genetic_state_to_be_converted):
        state = deepcopy(received_state)

        for subject, value in genetic_state_to_be_converted.items():
            for class_, students in value.items():
                for student in students:
                    state.students[student].subjects_and_classes[subject] = class_
        
        return GeneticState(state)

    def gen_off_spring(self, other):
        '''
        Consider self mum and other dad

        :param other: Other state to generate offspring
        :return: Tuple with offspring
        '''

        daughter = deepcopy(self)
        son = deepcopy(other)

        # Cycle to create daughter
        for subject, new_d in daughter.genetic_state.items():
            for class_, students in new_d.dictionary.items():
                student = sample(students, 1)[0] # A student from this class.

                # Chooses random student from that same class but in the dad state
                other_student = sample(other.genetic_state[subject].dictionary[class_], 1)[0]

                # Removes student and puts the other student there
                new_d.dictionary[class_].remove(student)
                new_d.dictionary[class_].append(other_student)

                # Finds other student and puts the first student there
                for class_2, students_2 in new_d.dictionary.items():
                    if class_ != class_2:
                        if other_student in students_2:
                            new_d.dictionary[class_2].remove(other_student)
                            new_d.dictionary[class_2].append(student)

        # Cycle to create son
        for subject, new_d in son.genetic_state.items():
            for class_, students in new_d.dictionary.items():
                student = sample(students, 1)[0] # A student from this class.

                # Chooses random student from that same class but in the dad state
                other_student = sample(self.genetic_state[subject].dictionary[class_], 1)[0]

                # Removes student and puts the other student there
                new_d.dictionary[class_].remove(student)
                new_d.dictionary[class_].append(other_student)

                # Finds other student and puts the first student there
                for class_2, students_2 in new_d.dictionary.items():
                    if class_ != class_2:
                        if other_student in students_2:
                            new_d.dictionary[class_2].remove(other_student)
                            new_d.dictionary[class_2].append(student)

        return (GeneticState.convert_to_normal_state(daughter.state, daughter.genetic_state),
                GeneticState.convert_to_normal_state(son.state, son.genetic_state))

            
    def mutate(self):
        self.state = self.state.random_neighbour()


#random_state = GenerateState.get_random_state(['Science', 'Bitch'], 5)
#random_state.get_score()
#genetic_state = GeneticState(random_state)

#print(random_state)
#print(genetic_state.genetic_state)

s0 = DataBank.get_state_0()
s1 = DataBank.get_state_1()

s0.get_score()
s1.get_score()

g_s0 = GeneticState(s0)
g_s1 = GeneticState(s1)

g_s0.convert_to_genetic_state()
g_s1.convert_to_genetic_state()

print('BEFORE OFFSPRING')
print('S0\n\n')
print(s0)
print('S1\n\n')
print(s1)

# print('AFTER OFFSPRING')
# print('S0\n\n')
# print(s0)
# print('S1\n\n')
# print(s1)

daughter, son = g_s0.gen_off_spring(g_s1)

print('OFFSPRING')
print('Daughter')
print(daughter.state)
print('Son')
print(son.state)

