import random
from copy import deepcopy

from src.state.schedule import Schedule


class State:
    PENALTY = 10000

    def __init__(self, state=None):
        if state is None:
            self.students = {}
            self.class_schedules = {}
            self.conflicts = 0
            self.didnt_get = 0
            self.student_num = 0
        else:
            self.students = state.students
            self.class_schedules = state.class_schedules
            self.conflicts = 0
            self.didnt_get = 0
            self.student_num = 0
            self.heuristic = self.get_score()

    # This comparison says a smaller object is bigger.
    # This may seem weird, but the comparison is used in a priority queue, which gives more priority to smaller objects
    # Since we want the bigger objects first in the PQ, I created the operator this way
    def __lt__(self, other):
        return self.heuristic > other.heuristic

    def __str__(self):
        st = ""
        for student in self.students.values():
            st += 'Student {0} has:'.format(student.student_id)
            for subject, clas in student.subjects_and_classes.items():
                st += ' Class {0} in the subject {1}/'.format(str(clas), subject)
            st += '\n'
        return st

    def add_student(self, student):
        self.students[student.student_id] = student
        self.student_num += 1

    def get_score(self):
        self.conflicts = 0
        self.didnt_get = 0
        MAX_SCORE = 100

        score = 0

        for student in self.students.values():

            alone = True
            gave_in = False
            got_target = False

            # checking buddies
            score_buddies = 0.5 * MAX_SCORE  # Gives 50% of importance to the buddies

            for subject in student.buddies:
                n = len(student.buddies[subject])
                score_each_buddy = (2 * score_buddies) / (n * (n + 1))
                increment_buddies = n
                for numbers in student.buddies[subject]:
                    if subject in self.students[numbers].subjects_and_classes:
                        if student.subjects_and_classes[subject] == \
                                self.students[numbers].subjects_and_classes[subject]:
                            score += score_each_buddy * increment_buddies  # Adds points when buddy is in the same class
                            increment_buddies -= 1  # Removes some points depending on the priority
                            alone = False

            # checking if student got a target class
            score_target_class = 0.5 * MAX_SCORE  # Gives 50% of importance to the Target Classes
            score_each_target = (2 * score_target_class) // (
                    (len(student.subjects_and_classes) + 1) * len(student.subjects_and_classes))
            increment_targets = len(student.subjects_and_classes)

            for position, subject_1 in enumerate(student.subjects_and_classes):

                if subject_1 in student.subject_targets.keys():
                    if student.subjects_and_classes[subject_1] in student.subject_targets[subject_1]:
                        score += score_each_target * increment_targets  # Adds points each time it is in a target class
                        increment_targets -= 1  # Removes some points depending on the priority
                        got_target = True

                        # checking if a student gave in any classes
                if subject_1 in student.subject_give_ins.keys():
                    if student.original_sac[subject_1] != student.subjects_and_classes[subject_1]:
                        if student.subjects_and_classes[subject_1] in student.subject_give_ins[subject_1]:
                            gave_in = True

                # checking for schedule conflicts.
                for p in range(position + 1, len(list(student.subjects_and_classes.keys()))):
                    key = list(student.subjects_and_classes.keys())[p]
                    if State.translate_subjects_and_classes(subject_1, student.subjects_and_classes[subject_1]) in \
                            self.class_schedules:
                        if State.translate_subjects_and_classes(key, student.subjects_and_classes[key]) in \
                                self.class_schedules:
                            sched_1 = self.class_schedules[
                                State.translate_subjects_and_classes(
                                    subject_1,
                                    student.subjects_and_classes[subject_1]
                                )
                            ]
                            sched_2 = self.class_schedules[
                                State.translate_subjects_and_classes(
                                    key,
                                    student.subjects_and_classes[key]
                                )
                            ]
                            if sched_1.conflicts(sched_2):
                                score -= State.PENALTY
                                self.conflicts += 1

            # If he gives up a class but didn't get the target nor he is with any of his buddies
            if gave_in and not got_target and alone:
                score -= State.PENALTY
                self.didnt_get += 1

        self.heuristic = score
        return score

    def add_schedule(self, subject, class_number, start_hour, end_hour, day):
        self.class_schedules[State.translate_subjects_and_classes(subject, class_number)] = Schedule(start_hour,
                                                                                                     end_hour, day)

    def trade_classes(self, student1_id, student2_id, subject_name):
        students = self.students
        student1_class = students[student1_id].get_class_for_subject(subject_name)
        student2_class = students[student2_id].get_class_for_subject(subject_name)
        students[student1_id].set_class_for_subject(subject_name, student2_class)
        students[student2_id].set_class_for_subject(subject_name, student1_class)

    def random_neighbour(self):
        list_students = []
        for elem in self.students.values():
            list_students.append(elem)
        master_students = deepcopy(list_students)
        used_master = []
        while len(used_master) != len(master_students):
            student_i = random.randrange(0, len(master_students))
            if student_i in used_master:
                continue
            student = master_students[student_i]
            student_classes = list(student.subjects_and_classes)
            temp_students = deepcopy(list_students)
            used_master.append(student_i)
            used_child = [student_i, ]
            while len(used_child) != len(temp_students):
                success = False
                trader_i = random.randrange(0, len(temp_students))
                if trader_i in used_child:
                    continue
                used_child.append(trader_i)
                trader = temp_students[trader_i]
                trader_classes = list(trader.subjects_and_classes)

                deploy_state = deepcopy(self)
                deploy_students = deepcopy(list_students)

                for trade_class in student_classes:
                    if trade_class in trader_classes:
                        success = True

                        deploy_students[student_i].subjects_and_classes[trade_class], \
                            deploy_students[trader_i].subjects_and_classes[trade_class] = \
                            deploy_students[trader_i].subjects_and_classes[trade_class], \
                            deploy_students[student_i].subjects_and_classes[trade_class]

                        deploy_dict = {}
                        for elem in deploy_students:
                            deploy_dict[elem.student_id] = elem

                        deploy_state.students = deploy_dict

                        return deploy_state
                if success:
                    break

    @staticmethod
    def translate_subjects_and_classes(subject, class_number):
        return subject + str(class_number)
