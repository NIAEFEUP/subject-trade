from random import sample, choice, randint

from src.base.hour import Hour
from src.base.state import State
from src.base.student import Student

MAXIMUM_CLASSES = 6
NUMBER_OF_CLASSES = 12


class NewDict:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __repr__(self):
        return 'NewD' + self.dictionary.__repr__()

    def items(self):
        return self.dictionary.items()


class GenerateState:
    # Function that generates students objects
    @staticmethod
    def generator_students(n_students, subjects):
        generated_students = []
        for i in range(n_students):
            subject_classes = {}
            subject_target = {}
            subject_give_in = {}
            number_classes = randint(4, NUMBER_OF_CLASSES)

            # subject classes
            for j in range(0, number_classes):
                subject = choice(subjects)
                if subject not in subject_classes.keys():  # the subject can't be repeated
                    subject_classes[subject] = randint(1, NUMBER_OF_CLASSES)
                else:
                    j -= 1

            # target classes
            for _ in range(randint(1, len(subject_classes))):
                subject = choice(list(subject_classes.keys()))  # choose a class to change
                target = [randint(1, MAXIMUM_CLASSES) for _ in
                          range(randint(1, NUMBER_OF_CLASSES))]  # class target number
                target = list(set(
                    filter(lambda x: x != subject_classes[subject], target)))  # the target can't be in subject_classes
                subject_target[subject] = target

                # give_in classes
            for _ in range(randint(0, len(subject_classes) - len(subject_target))):  # the give_in can't be a target
                subject = choice(list(subject_classes.keys()))
                while (subject in list(subject_target.keys())):
                    subject = choice(list(subject_classes.keys()))

                give_in = []
                while (give_in == list()):  # if there's a give_in, the list can't be empty
                    give_in = [randint(1, MAXIMUM_CLASSES) for _ in
                               range(randint(1, NUMBER_OF_CLASSES))]  # give_in classes
                    give_in = list(set(filter(lambda x: x != subject_classes[subject],
                                              give_in)))  # the give_in can't be the actual class

                subject_give_in[subject] = give_in

            s = Student(i, subject_classes, subject_target, subject_give_in, {})

            for _ in range(randint(0, len(subject_classes))):  # number of subjects with buddies
                buddies = []
                for _ in range(1, 4):  # number of buddies in a subject
                    buddy = randint(0, (n_students - 1))
                    while (buddy == s.student_id):  # avoid the buddy being him self
                        buddy = randint(0, (n_students - 1))
                    buddies.append(buddy)

                subject = choice(list(subject_classes.keys()))
                while (subject in list(s.buddies.keys())):  # the subject cannot be already at s.buddies
                    subject = choice(list(subject_classes.keys()))

                s.add_buddies(subject, list(set(buddies)))

            generated_students.append(s)

        return generated_students

    @staticmethod
    def great_students(list_of_subjects, number_students):
        generated_students = []
        dict_of_targets = {}
        dict_of_student_info = {}

        for i in range(number_students):
            subject_target = {}
            subject_give_in = {}

            for el in sample(list_of_subjects, 1):
                number_of_targets = randint(1, 3)
                # number_of_targets random targets from 1 to NUMBER_OF_CLASSES
                subject_target[el] = sample([j for j in range(1, NUMBER_OF_CLASSES + 1)], number_of_targets)

            c = choice(list_of_subjects)
            while c in subject_target.keys():
                c = choice(list_of_subjects)

            number_of_give_ins = randint(1, 3)
            # number_of_give_ins random give ins from 1 to NUMBER_OF_CLASSES
            subject_give_in[el] = sample([j for j in range(1, NUMBER_OF_CLASSES + 1)], number_of_give_ins)

            # Fill dict of targets with a random target of this student
            for subject, target in subject_target.items():
                if subject not in dict_of_targets:
                    dictionary = {choice(list(subject_target)): 1}
                    dict_of_targets[subject] = NewDict(dictionary)
                else:
                    clas = choice(list(subject_target))
                    if clas not in dict_of_targets[subject].dictionary:
                        dict_of_targets[subject].dictionary[clas] = 1
                    else:
                        dict_of_targets[subject].dictionary[clas] += 1

            dict_of_student_info[i] = [subject_target, subject_give_in]

        for i in range(number_students):
            subjects_and_classes = {}

            for subject in list_of_subjects:
                for clas, counter in dict_of_targets[subject].dictionary.items():
                    if counter > 0:
                        counter -= 1
                        subjects_and_classes[subject] = clas
                        break
                subjects_and_classes[subject] = choice([j for j in range(1, NUMBER_OF_CLASSES + 1)])

            subject_targets = dict_of_student_info[i][0]
            subject_give_ins = dict_of_student_info[i][1]

            generated_students.append(Student(i, subjects_and_classes, subject_targets, subject_give_ins, {}))

        return generated_students

        # Function that generates the schedule for each classes given the list of classes

    @staticmethod
    def random_time_generator(subjects, state):
        days_of_the_week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
        for _, subject in enumerate(subjects, start=1):
            for j in range(NUMBER_OF_CLASSES):
                hour_1 = Hour(7, 0) + Hour(j * 2, 0)
                hour_2 = hour_1 + Hour(2, 0)
                state.add_schedule(subject, j, hour_1, hour_2, sample(days_of_the_week, 1)[0])
        return state

    @staticmethod
    def time_generator(subjects, state):
        days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for number, subject in enumerate(subjects, start=1):
            for j in range(NUMBER_OF_CLASSES):
                hour_1 = Hour(7, 0) + Hour(j * 2, 0)
                hour_2 = hour_1 + Hour(2, 0)
                state.add_schedule(subject, j, hour_1, hour_2, days_of_the_week[j % (len(days_of_the_week) - 1)])
        return state

    @staticmethod
    def get_random_state(list_of_subjects, number_students):
        state = State()
        GenerateState.random_time_generator(list_of_subjects, state)

        for student in GenerateState.generator_students(number_students, list_of_subjects):
            state.add_student(student)

        return state

    @staticmethod
    def get_great_state(list_of_subjects, number_students):
        state = State()
        GenerateState.time_generator(list_of_subjects, state)

        for student in GenerateState.great_students(list_of_subjects, number_students):
            state.add_student(student)

        return state


# state = State()
# GenerateState.random_time_generator(['TCOM', 'FIS', 'LCOM', 'MPCP', 'FIS2', 'CMAT', 'AMAT', 'BDAD'], state)
# GenerateState.generator_students(40,['TCOM', 'FIS', 'LCOM', 'MPCP', 'FIS2', 'CMAT', 'AMAT', 'BDAD'])
# GenerateState.get_great_state(['a', 'b', 'c'], 100)
