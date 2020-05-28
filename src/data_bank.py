from state import State
from student import Student
from schedule import Schedule
from hour import Hour


class DataBank:
    @staticmethod
    def get_state_0():
        state = State()

        # Generate schedule
        list_of_subjects = ['MPE', 'SSASC', 'ARSI']
        class_numbers = [1, 2, 3]

        hour_1 = Hour(14, 30)
        hour_2 = Hour(16, 30)

        hour_3 = Hour(15, 30)
        hour_4 = Hour(17, 30)

        hour_5 = Hour(11, 30)
        hour_6 = Hour(13, 30)
        
        state.add_schedule(list_of_subjects[0], 1, hour_1, hour_2, 'Monday')
        state.add_schedule(list_of_subjects[1], 1, hour_3, hour_4, 'Monday')
        state.add_schedule(list_of_subjects[2], 1, hour_5, hour_6, 'Monday')

        state.add_schedule(list_of_subjects[0], 2, hour_1, hour_2, 'Wednesday')
        state.add_schedule(list_of_subjects[1], 2, hour_3, hour_4, 'Wednesday')
        state.add_schedule(list_of_subjects[2], 2, hour_5, hour_6, 'Wednesday')

        state.add_schedule(list_of_subjects[0], 3, hour_1, hour_2, 'Friday')
        state.add_schedule(list_of_subjects[1], 3, hour_3, hour_4, 'Friday')
        state.add_schedule(list_of_subjects[2], 3, hour_6, hour_6, 'Friday')

        # Gerar estudantes.
        subect_and_class_1 = {'MPE': 1, 'SSASC': 3, 'ARSI': 1}
        target_1 = {'MPE': [2, 3], 'SSASC': [1,2]}
        give_ins_1 = {'ARSI':[2,3]}

        subect_and_class_2 = {'MPE': 2, 'SSASC': 2, 'ARSI': 3}
        target_2 = {'MPE': [1, 3], 'ARSI': [1,2]}
        give_ins_2 = {'SSASC':[2,3]}

        subect_and_class_3 = {'MPE': 3, 'SSASC': 1, 'ARSI': 2}
        target_3 = {'SSASC': [1, 3], 'ARSI': [2,3]}
        give_ins_3 = {'MPE':[1,2]}

        student_1 = Student(1, subect_and_class_1, target_1, give_ins_1, {})
        student_2 = Student(2, subect_and_class_2, target_2, give_ins_2, {})
        student_3 = Student(3, subect_and_class_3, target_3, give_ins_3, {})

        list_of_students = [student_1, student_2, student_3]

        for student in list_of_students: state.add_student(student)

        return state

    @staticmethod
    def get_state_1():
        state = State()
        
        # Generate schedule
        list_of_subjects = ['MPE', 'SSASC', 'ARSI']
        class_numbers = [1, 2, 3]

        hour_1 = Hour(14, 30)
        hour_2 = Hour(16, 30)

        hour_3 = Hour(15, 30)
        hour_4 = Hour(17, 30)

        hour_5 = Hour(11, 30)
        hour_6 = Hour(13, 30)
        
        state.add_schedule(list_of_subjects[0], 1, hour_1, hour_2, 'Monday')
        state.add_schedule(list_of_subjects[1], 1, hour_3, hour_4, 'Monday')
        state.add_schedule(list_of_subjects[2], 1, hour_5, hour_6, 'Monday')

        state.add_schedule(list_of_subjects[0], 2, hour_1, hour_2, 'Wednesday')
        state.add_schedule(list_of_subjects[1], 2, hour_3, hour_4, 'Wednesday')
        state.add_schedule(list_of_subjects[2], 2, hour_5, hour_6, 'Wednesday')

        state.add_schedule(list_of_subjects[0], 3, hour_1, hour_2, 'Friday')
        state.add_schedule(list_of_subjects[1], 3, hour_3, hour_4, 'Friday')
        state.add_schedule(list_of_subjects[2], 3, hour_6, hour_6, 'Friday')

        # Gerar estudantes.
        subect_and_class_1 = {'MPE': 2, 'SSASC': 3, 'ARSI': 3}
        target_1 = {'MPE': [2, 3], 'SSASC': [1,2]}
        give_ins_1 = {'ARSI':[2,3]}

        subect_and_class_2 = {'MPE': 1, 'SSASC': 1, 'ARSI': 2}
        target_2 = {'MPE': [1, 3], 'ARSI': [1,2]}
        give_ins_2 = {'SSASC':[2,3]}

        subect_and_class_3 = {'MPE': 3, 'SSASC': 2, 'ARSI': 1}
        target_3 = {'SSASC': [1, 3], 'ARSI': [2,3]}
        give_ins_3 = {'MPE':[1,2]}

        student_1 = Student(1, subect_and_class_1, target_1, give_ins_1, {})
        student_2 = Student(2, subect_and_class_2, target_2, give_ins_2, {})
        student_3 = Student(3, subect_and_class_3, target_3, give_ins_3, {})

        list_of_students = [student_1, student_2, student_3]

        for student in list_of_students: state.add_student(student)

        return state


    # @staticmethod
    # def get_state_2():
    #     state = State()
    #     # Gerar horário.
    #         # Uma lista de cadeiras.

    #     list_of_subjects = ['MPE', 'SSASC', 'ARSI']
    #     class_numbers = [1, 2, 3]

    #     hour_1 = Hour(14, 30)
    #     hour_2 = Hour(16, 30)

    #     hour_3 = Hour(15, 30)
    #     hour_4 = Hour(17, 30)

    #     hour_5 = Hour(11, 30)
    #     hour_6 = Hour(13, 30)
        
    #     state.add_schedule(list_of_subjects[0], 1, hour_1, hour_2, 'Monday')
    #     state.add_schedule(list_of_subjects[1], 1, hour_3, hour_4, 'Monday')
    #     state.add_schedule(list_of_subjects[2], 1, hour_5, hour_6, 'Monday')

    #     state.add_schedule(list_of_subjects[0], 2, hour_1, hour_2, 'Wednesday')
    #     state.add_schedule(list_of_subjects[1], 2, hour_3, hour_4, 'Wednesday')
    #     state.add_schedule(list_of_subjects[2], 2, hour_5, hour_6, 'Wednesday')

    #     state.add_schedule(list_of_subjects[0], 3, hour_1, hour_2, 'Friday')
    #     state.add_schedule(list_of_subjects[1], 3, hour_3, hour_4, 'Friday')
    #     state.add_schedule(list_of_subjects[2], 3, hour_6, hour_6, 'Friday')

    #     # Gerar estudantes.

    #     # def __init__(self, student_id, subjects_and_classes, subject_targets, subject_give_ins, buddies):

    #     subect_and_class_1 = {'MPE': 1, 'SSASC': 3, 'ARSI': 1}
    #     target_1 = {'MPE': [2, 3], 'SSASC': [1,2]}
    #     give_ins = {'ARSI':[2,3]}

    #     subect_and_class_2 = {'MPE': 2, 'SSASC': 2, 'ARSI': 1}
    #     target_2 = {'MPE': [1, 3], 'ARSI': [1,2]}
    #     give_ins = {'SSASC':[2,3]}

    #     subect_and_class_3 = {'MPE': 3, 'SSASC': 1, 'ARSI': 1}
    #     target_2 = {'SSASC': [1, 3], 'ARSI': [1,2]}
    #     give_ins = {'MPE':[1,2]}

    #     subect_and_class_4 = {'MPE': 1, 'SSASC': 3, 'ARSI': 2}
    #     target_2 = {'SSASC': [1, 3], 'ARSI': [1,2]}
    #     give_ins = {'MPE':[1,2]}

    #     subect_and_class_5 = {'MPE': 2, 'SSASC': 2, 'ARSI': 2}
    #     subect_and_class_6 = {'MPE': 3, 'SSASC': 1, 'ARSI': 2}
    #     subect_and_class_7 = {'MPE': 1, 'SSASC': 3, 'ARSI': 3}
    #     subect_and_class_8 = {'MPE': 2, 'SSASC': 2, 'ARSI': 3}
    #     subect_and_class_9 = {'MPE': 3, 'SSASC': 1, 'ARSI': 3}

        

    #     student_1 = Student(1, )