import random

class GeneticState:
    def __init__(self, state):
        self.state = state
        self.heuristic = self.heuristic()

    def heuristic(self): # TODO replace with get_score
        val = 0
        for el in self.state:
            if el == 1:
                val += 1

        return val

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
        if random.randint(1,100) == 1:
            mutation = True
        else:
            mutation = False

        if mutation:
            index = random.sample(range(0, len(self.state)), 1)[0]
            if self.state[index] == 1:
                self.state[index] = 0
            else:
                self.state[index] = 1

    def int(self):
        val = 0
        for index, element in enumerate(self.state[::-1]):
            if element == 1:
                val += 2 ** (index)
        
        return val

    @staticmethod
    def gen_binary(number):
        options = [0,1]
        return [random.sample(options, 1)[0] for i in range(number)]

    def __repr__(self):
        return str(self.state)
