import math
import random
from time import perf_counter
from src.utils.data_bank import DataBank


class HillClimbingVariants:
    XI = 5000
    STEEPEST_ASCENT_NUMBER = 5
    SIMULATED_ANNEALING_STEP = 0.0005
    RESTART_NUMBER = 10

    @staticmethod
    def hill_climbing(state):
        number_of_tries = 0
        state.get_score()
        while number_of_tries < HillClimbingVariants.XI:
            s = state.random_neighbour()
            s.get_score()
            if s.heuristic > state.heuristic:
                state = s
                number_of_tries = 0
            else:
                number_of_tries += 1

            if number_of_tries > HillClimbingVariants.XI:
                break
        return state

    @staticmethod
    def random_restart_hill_climbing(state):
        best_state = HillClimbingVariants.hill_climbing(state)

        for _ in range(HillClimbingVariants.RESTART_NUMBER):
            s = state
            for _ in range(100):
                s = s.random_neighbour()

            best_state = HillClimbingVariants.hill_climbing(s)
            if s.heuristic > best_state.heuristic:
                best_state = s

        return best_state

    @staticmethod
    def steepest_ascent_hill_climbing(state):
        number_of_tries = 0
        while number_of_tries < HillClimbingVariants.XI:
            state.get_score()
            counter = 0
            q = []

            s = None
            while counter < HillClimbingVariants.STEEPEST_ASCENT_NUMBER:
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

            if number_of_tries > HillClimbingVariants.XI:
                break

        return state

    @staticmethod
    def simulated_annealing(state):
        temperature = 1
        iterations = 0
        number_of_tries = 0
        best_state = state
        while number_of_tries < HillClimbingVariants.XI:
            temperature = 1 - iterations * HillClimbingVariants.SIMULATED_ANNEALING_STEP

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
