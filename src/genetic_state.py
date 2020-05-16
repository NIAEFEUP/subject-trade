import random
from copy import deepcopy

class NewDict:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __repr__(self):
        return self.dictionary.__repr__()

class GeneticState:
    def __init__(self, state):
        self.state = state
        self.heuristic = self.heuristic()
        self.genetic_state = set()

    def heuristic(self):
        return self.state.heuristic

    def convert_to_genetic_state(self):   # TODO test this
        for student_id, student in self.state.students.items():
            for subject, class_ in student.items():
                if not subject in self.genetic_state:
                    self.genetic_state[subject] = NewDict({})

                if not class_ in self.genetic_state[subject].dictionary:
                    self.genetic_state[subject].dictionary[class_] = []

                self.genetic_state[subject].dictionary[class_].append(student_id)

    @staticmethod
    def convert_to_normal_state(received_state, received_genetic_state): # TODO test this
        state = deepcopy(received_state)

        for subject in received_genetic_state:
            for class_, students in subject.items():
                for student in students:
                    state.students[student].subjects_and_classes[subject] = class_
        
        return GeneticState(state)

    def gen_off_spring(self, other): # TODO think about how to do this with our actual state.
        separation_point = random.randint(1, len(self.state) - 2)
        off_spring_1_state = []
        off_spring_2_state = []

        for i in range(0, len(self.state)):
            if i < separation_point:
                off_spring_1_state.append(self.state[i])
                off_spring_2_state.append(other.state[i])
            else:
                off_spring_1_state.append(other.state[i])
                off_spring_2_state.append(self.state[i])

        return (GeneticState(off_spring_1_state), GeneticState(off_spring_2_state))
    
    def mutate(self): # TODO replace with something else
        if random.randint(1,50) == 1:
            mutation = True
        else:
            mutation = False

        if mutation:
            self.state = self.state.random_neighbour()
            self.heuristic = self.heuristic()


