from copy import deepcopy

from src.base.hour import Hour
from src.base.state import State
from src.base.student import Student


class DataBank:
    @staticmethod
    def get_state_0():
        state = State()

        # Generate schedule
        list_of_subjects = ['MPE', 'SSASC', 'ARSI']

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


    @staticmethod
    def get_state_2():
        state = State()
        # Gerar horário.
        list_of_subjects = ['MPE', 'SSASC', 'ARSI', 'DSG', "MRKT"]

        hour_1 = Hour(14, 30)
        hour_2 = Hour(16, 30)

        hour_3 = Hour(15, 30)
        hour_4 = Hour(17, 30)

        hour_5 = Hour(11, 30)
        hour_6 = Hour(13, 30)

        hour_7 = Hour(8, 0)
        hour_8 = Hour(10, 0)

        hour_9 = Hour(9, 0)
        hour_10 = Hour(11, 0)
        
        state.add_schedule(list_of_subjects[0], 1, hour_1, hour_2, 'Monday')
        state.add_schedule(list_of_subjects[1], 1, hour_3, hour_4, 'Monday')
        state.add_schedule(list_of_subjects[2], 1, hour_5, hour_6, 'Monday')
        state.add_schedule(list_of_subjects[3], 1, hour_7, hour_8, 'Monday')
        state.add_schedule(list_of_subjects[4], 1, hour_9, hour_10, 'Monday')

        state.add_schedule(list_of_subjects[0], 2, hour_1, hour_2, 'Tuesday')
        state.add_schedule(list_of_subjects[1], 2, hour_3, hour_4, 'Tuesday')
        state.add_schedule(list_of_subjects[2], 2, hour_6, hour_6, 'Tuesday')
        state.add_schedule(list_of_subjects[3], 2, hour_7, hour_8, 'Tuesday')
        state.add_schedule(list_of_subjects[4], 2, hour_9, hour_10, 'Tuesday')

        state.add_schedule(list_of_subjects[0], 3, hour_1, hour_2, 'Wednesday')
        state.add_schedule(list_of_subjects[1], 3, hour_3, hour_4, 'Wednesday')
        state.add_schedule(list_of_subjects[2], 3, hour_5, hour_6, 'Wednesday')
        state.add_schedule(list_of_subjects[3], 3, hour_7, hour_8, 'Wednesday')
        state.add_schedule(list_of_subjects[4], 3, hour_9, hour_10, 'Wednesday')

        state.add_schedule(list_of_subjects[0], 4, hour_1, hour_2, 'Thursday')
        state.add_schedule(list_of_subjects[1], 4, hour_3, hour_4, 'Thursday')
        state.add_schedule(list_of_subjects[2], 4, hour_6, hour_6, 'Thursday')
        state.add_schedule(list_of_subjects[3], 4, hour_7, hour_8, 'Thursday')
        state.add_schedule(list_of_subjects[4], 4, hour_9, hour_10, 'Thursday')

        state.add_schedule(list_of_subjects[0], 5, hour_1, hour_2, 'Friday')
        state.add_schedule(list_of_subjects[1], 5, hour_3, hour_4, 'Friday')
        state.add_schedule(list_of_subjects[2], 5, hour_6, hour_6, 'Friday')
        state.add_schedule(list_of_subjects[3], 5, hour_7, hour_8, 'Friday')
        state.add_schedule(list_of_subjects[4], 5, hour_9, hour_10, 'Friday')

        # Gerar estudantes
        subect_and_class_1 = {'MPE': 1, 'SSASC': 2, 'ARSI': 3, 'DSG': 4, 'MRKT': 5}
        target_1 = {'MPE': [1,3], 'ARSI': [1,2]}
        give_ins_1 = {'SSASC':[2,3], 'DSG': [1,2,3,4], 'MRKT': [2,3,5]}

        subect_and_class_2 = {'MPE': 2, 'SSASC': 3, 'ARSI': 4, 'DSG': 5, 'MRKT': 1}
        target_2 = {'SSASC': [1,3], 'DSG': [1,2], 'MRKT': [1,2,3]}
        give_ins_2 = {'MPE':[2,3], 'ARSI': [1,2,3,4]}

        subect_and_class_3 = {'MPE': 3, 'SSASC': 4, 'ARSI': 5, 'DSG': 1, 'MRKT': 2}
        target_3 = {'SSASC': [2,4,5], 'MRKT': [5,1]}
        give_ins_3 = {'DSG': [1,2,4], 'ARSI': [3,4,5]}

        subect_and_class_4 = {'MPE': 4, 'SSASC': 5, 'ARSI': 1, 'DSG': 2, 'MRKT': 3}
        target_4 = {'ARSI': [1,3], 'SSASC': [5,2]}
        give_ins_4 = {'MPE':[2,3,4,5], 'MRKT': [5,3,4], 'DSG': [1,2]}

        subect_and_class_5 = {'MPE': 5, 'SSASC': 1, 'ARSI': 2, 'DSG': 3, 'MRKT': 4}
        target_5 = {}
        give_ins_5 = {'SSASC':[1,2,3], 'DSG': [1,2,3,4], 'MRKT': [2,4,5]}
        buddies_5 = {'MPE': [3], 'ARSI': [2,10]}

        subect_and_class_6 = {'MPE': 1, 'SSASC': 2, 'ARSI': 3, 'DSG': 4, 'MRKT': 5}
        target_6 = {'DSG': [2,5], 'MRKT': [5,1]}
        give_ins_6 = {'MPE':[1,2,3], 'SSASC': [1,3,2], 'ARSI': [3,2]}

        subect_and_class_7 = {'MPE': 2, 'SSASC': 3, 'ARSI': 4, 'DSG': 5, 'MRKT': 1}
        target_7 = {'MPE': [3,2,1], 'ARSI': [5,1], 'SSASC': [5,2]}
        give_ins_7 = {'DSG':[4,5,3], 'MRKT': [1,3,4]}
        
        subect_and_class_8 = {'MPE': 3, 'SSASC': 4, 'ARSI': 5, 'DSG': 1, 'MRKT': 2}
        target_8 = {'DSG': [1,2], 'SSASC': [3,2,4]}
        give_ins_8 = {'MPE':[4,1,3], 'MRKT': [5,2], 'ARSI': [1,5,2]}

        subect_and_class_9 = {'MPE': 4, 'SSASC': 5, 'ARSI': 1, 'DSG': 2, 'MRKT': 3}
        target_9 = {'ARSI': [3,4], 'MRKT': [1,2]}
        give_ins_9 = {'MPE':[1,2,4], 'SSASC': [3,1,5], 'DSG': [3,2]}

        subect_and_class_10 = {'MPE': 5, 'SSASC': 1, 'ARSI': 2, 'DSG': 3, 'MRKT': 4}
        target_10 = {}
        give_ins_10 = {'MRKT':[2,3,4], 'DSG': [5,3,2], 'ARSI': [3,2,1]}
        buddies_10 = {'MPE': [9,20], 'SSASC': [2,17]}

        subect_and_class_11 = {'MPE': 1, 'SSASC': 2, 'ARSI': 3, 'DSG': 4, 'MRKT': 5}
        target_11 = {'MPE': [5]}
        give_ins_11 = {'SSASC': [2,1], 'ARSI': [3,1], 'DSG': [4,1], 'MRKT': [5,1]}

        subect_and_class_12 = {'MPE': 2, 'SSASC': 3, 'ARSI': 4, 'DSG': 5, 'MRKT': 1}
        target_12 = {'ARSI': [1,2,3,4], 'MPE': [5,1,3]}
        give_ins_12 = {'MRKT':[1,2,3], 'SSASC': [1,3,2], 'DSG': [3,5,2]}

        subect_and_class_13 = {'MPE': 3, 'SSASC': 4, 'ARSI': 5, 'DSG': 1, 'MRKT': 2}
        target_13 = {'MRKT': [2,5,3], 'DSG': [1,4], 'SSASC': [1,3,2,5]}
        give_ins_13 = {'ARSI':[1,5,3], 'MPE': [3,2,1]}

        subect_and_class_14 = {'MPE': 4, 'SSASC': 5, 'ARSI': 1, 'DSG': 2, 'MRKT': 3}
        target_14 = {'DSG': [1,2], 'MRKT': [4,5], 'ARSI': [4,3]}
        give_ins_14 = {'MPE':[1,4,3], 'SSASC': [5,3,2]}

        subect_and_class_15 = {'MPE': 5, 'SSASC': 1, 'ARSI': 2, 'DSG': 3, 'MRKT': 4}
        target_15 = {}
        give_ins_15 = {'MPE': [2,3,5], 'SSASC': [1,3,2], 'DSG': [3,5,1]}
        buddies_15 = {'ARSI': [10,11,12], 'MRKT': [1,3]}

        subect_and_class_16 = {'MPE': 1, 'SSASC': 2, 'ARSI': 3, 'DSG': 4, 'MRKT': 5}
        target_16 = {'SSASC': [5,1], 'MRKT': [1], 'MPE':[1,5,3]}
        give_ins_16 = {'DSG': [4,3,2], 'ARSI': [3,2]}

        subect_and_class_17 = {'MPE': 2, 'SSASC': 3, 'ARSI': 4, 'DSG': 5, 'MRKT': 1}
        target_17 = {'DSG': [1,5], 'MRKT': [5,1]}
        give_ins_17 = {'MPE':[5,2,3], 'SSASC': [5,3,1], 'ARSI': [1,2,4]}

        subect_and_class_18 = {'MPE': 3, 'SSASC': 4, 'ARSI': 5, 'DSG': 1, 'MRKT': 2}
        target_18 = {'MPE': [2,3], 'SSASC': [5,3,2]}
        give_ins_18 = {'DSG':[1,2,3,4,5], 'MRKT': [1,2,3,4,5], 'ARSI': [1,2,3,4,5]}

        subect_and_class_19 = {'MPE': 4, 'SSASC': 5, 'ARSI': 1, 'DSG': 2, 'MRKT': 3}
        target_19 = {'DSG': [4,2,5], 'SSASC': [5,1,4]}
        give_ins_19 = {'MPE': [1,2,3,4,5], 'MRKT': [1,2,3,4,5], 'ARSI': [1,2,3,4,5]}

        subect_and_class_20 = {'MPE': 5, 'SSASC': 1, 'ARSI': 2, 'DSG': 3, 'MRKT': 4}
        target_20 = {}
        give_ins_20 = {'DSG': [1,2,3,4,5], 'SSASC': [1,2,3,4,5], 'MRKT': [1,2,3,4,5]}
        buddies_20 = {'ARSI': [7,13], 'MPE': [12,19,9]}


        
        student_1 = Student(1, subect_and_class_1, target_1, give_ins_1, {})
        student_2 = Student(2, subect_and_class_2, target_2, give_ins_2, {})
        student_3 = Student(3, subect_and_class_3, target_3, give_ins_3, {})
        student_4 = Student(4, subect_and_class_4, target_4, give_ins_4, {})
        student_5 = Student(5, subect_and_class_5, target_5, give_ins_5, buddies_5)
        student_6 = Student(6, subect_and_class_6, target_6, give_ins_6, {})
        student_7 = Student(7, subect_and_class_7, target_7, give_ins_7, {})
        student_8 = Student(8, subect_and_class_8, target_8, give_ins_8, {})
        student_9 = Student(9, subect_and_class_9, target_9, give_ins_9, {})
        student_10 = Student(10, subect_and_class_10, target_10, give_ins_10, buddies_10)
        student_11 = Student(11, subect_and_class_11, target_11, give_ins_11, {})
        student_12 = Student(12, subect_and_class_12, target_12, give_ins_12, {})
        student_13 = Student(13, subect_and_class_13, target_13, give_ins_13, {})
        student_14 = Student(14, subect_and_class_14, target_14, give_ins_14, {})
        student_15 = Student(15, subect_and_class_15, target_15, give_ins_15, buddies_15)
        student_16 = Student(16, subect_and_class_16, target_16, give_ins_16, {})
        student_17 = Student(17, subect_and_class_17, target_17, give_ins_17, {})
        student_18 = Student(18, subect_and_class_18, target_18, give_ins_18, {})
        student_19 = Student(19, subect_and_class_19, target_19, give_ins_19, {})
        student_20 = Student(20, subect_and_class_20, target_20, give_ins_20, buddies_20)

        list_of_students = [student_1,
                            student_2,
                            student_3,
                            student_4,
                            student_5,
                            student_6,
                            student_7,
                            student_8,
                            student_9,
                            student_10,
                            student_11,
                            student_12,
                            student_13,
                            student_14,
                            student_15,
                            student_16,
                            student_17,
                            student_18,
                            student_19,
                            student_20]
    
        for student in list_of_students: state.add_student(student)

        return state


    @staticmethod
    def get_states_with_different_number():
        state = State()

        # Gerar horário.
        list_of_subjects = ['MPE', 'SSASC', 'ARSI', 'DSG', "MRKT"]

        hour_1 = Hour(14, 30)
        hour_2 = Hour(16, 30)

        hour_3 = Hour(15, 30)
        hour_4 = Hour(17, 30)

        hour_5 = Hour(11, 30)
        hour_6 = Hour(13, 30)

        hour_7 = Hour(8, 0)
        hour_8 = Hour(10, 0)

        hour_9 = Hour(9, 0)
        hour_10 = Hour(11, 0)
        
        state.add_schedule(list_of_subjects[0], 1, hour_1, hour_2, 'Monday')
        state.add_schedule(list_of_subjects[1], 1, hour_3, hour_4, 'Monday')
        state.add_schedule(list_of_subjects[2], 1, hour_5, hour_6, 'Monday')
        state.add_schedule(list_of_subjects[3], 1, hour_7, hour_8, 'Monday')
        state.add_schedule(list_of_subjects[4], 1, hour_9, hour_10, 'Monday')

        state.add_schedule(list_of_subjects[0], 2, hour_1, hour_2, 'Tuesday')
        state.add_schedule(list_of_subjects[1], 2, hour_3, hour_4, 'Tuesday')
        state.add_schedule(list_of_subjects[2], 2, hour_6, hour_6, 'Tuesday')
        state.add_schedule(list_of_subjects[3], 2, hour_7, hour_8, 'Tuesday')
        state.add_schedule(list_of_subjects[4], 2, hour_9, hour_10, 'Tuesday')

        state.add_schedule(list_of_subjects[0], 3, hour_1, hour_2, 'Wednesday')
        state.add_schedule(list_of_subjects[1], 3, hour_3, hour_4, 'Wednesday')
        state.add_schedule(list_of_subjects[2], 3, hour_5, hour_6, 'Wednesday')
        state.add_schedule(list_of_subjects[3], 3, hour_7, hour_8, 'Wednesday')
        state.add_schedule(list_of_subjects[4], 3, hour_9, hour_10, 'Wednesday')

        state.add_schedule(list_of_subjects[0], 4, hour_1, hour_2, 'Thursday')
        state.add_schedule(list_of_subjects[1], 4, hour_3, hour_4, 'Thursday')
        state.add_schedule(list_of_subjects[2], 4, hour_6, hour_6, 'Thursday')
        state.add_schedule(list_of_subjects[3], 4, hour_7, hour_8, 'Thursday')
        state.add_schedule(list_of_subjects[4], 4, hour_9, hour_10, 'Thursday')

        state.add_schedule(list_of_subjects[0], 5, hour_1, hour_2, 'Friday')
        state.add_schedule(list_of_subjects[1], 5, hour_3, hour_4, 'Friday')
        state.add_schedule(list_of_subjects[2], 5, hour_6, hour_6, 'Friday')
        state.add_schedule(list_of_subjects[3], 5, hour_7, hour_8, 'Friday')
        state.add_schedule(list_of_subjects[4], 5, hour_9, hour_10, 'Friday')

        # Gerar estudantes
        subect_and_class_1 = {'MPE': 1, 'SSASC': 2, 'ARSI': 3, 'DSG': 4, 'MRKT': 5}
        target_1 = {'MPE': [1,3], 'ARSI': [1,2]}
        give_ins_1 = {'SSASC':[2,3], 'DSG': [1,2,3,4], 'MRKT': [2,3,5]}

        subect_and_class_2 = {'MPE': 2, 'SSASC': 3, 'ARSI': 4, 'DSG': 5, 'MRKT': 1}
        target_2 = {'SSASC': [1,3], 'DSG': [1,2], 'MRKT': [1,2,3]}
        give_ins_2 = {'MPE':[2,3], 'ARSI': [1,2,3,4]}

        subect_and_class_3 = {'MPE': 3, 'SSASC': 4, 'ARSI': 5, 'DSG': 1, 'MRKT': 2}
        target_3 = {'SSASC': [2,4,5], 'MRKT': [5,1]}
        give_ins_3 = {'DSG': [1,2,4], 'ARSI': [3,4,5]}

        subect_and_class_4 = {'MPE': 4, 'SSASC': 5, 'ARSI': 1, 'DSG': 2, 'MRKT': 3}
        target_4 = {'ARSI': [1,3], 'SSASC': [5,2]}
        give_ins_4 = {'MPE':[2,3,4,5], 'MRKT': [5,3,4], 'DSG': [1,2]}

        subect_and_class_5 = {'MPE': 5, 'SSASC': 1, 'ARSI': 2, 'DSG': 3, 'MRKT': 4}
        target_5 = {}
        give_ins_5 = {'SSASC':[1,2,3], 'DSG': [1,2,3,4], 'MRKT': [2,4,5]}
        buddies_5 = {'MPE': [3], 'ARSI': [1,4]}

        subect_and_class_6 = {'MPE': 1, 'SSASC': 2, 'ARSI': 3, 'DSG': 4, 'MRKT': 5}
        target_6 = {'DSG': [2,5], 'MRKT': [5,1]}
        give_ins_6 = {'MPE':[1,2,3], 'SSASC': [1,3,2], 'ARSI': [3,2]}

        subect_and_class_7 = {'MPE': 2, 'SSASC': 3, 'ARSI': 4, 'DSG': 5, 'MRKT': 1}
        target_7 = {'MPE': [3,2,1], 'ARSI': [5,1], 'SSASC': [5,2]}
        give_ins_7 = {'DSG':[4,5,3], 'MRKT': [1,3,4]}
        
        subect_and_class_8 = {'MPE': 3, 'SSASC': 4, 'ARSI': 5, 'DSG': 1, 'MRKT': 2}
        target_8 = {'DSG': [1,2], 'SSASC': [3,2,4]}
        give_ins_8 = {'MPE':[4,1,3], 'MRKT': [5,2], 'ARSI': [1,5,2]}

        subect_and_class_9 = {'MPE': 4, 'SSASC': 5, 'ARSI': 1, 'DSG': 2, 'MRKT': 3}
        target_9 = {'ARSI': [3,4], 'MRKT': [1,2]}
        give_ins_9 = {'MPE':[1,2,4], 'SSASC': [3,1,5], 'DSG': [3,2]}

        subect_and_class_10 = {'MPE': 5, 'SSASC': 1, 'ARSI': 2, 'DSG': 3, 'MRKT': 4}
        target_10 = {}
        give_ins_10 = {'MRKT':[2,3,4], 'DSG': [5,3,2], 'ARSI': [3,2,1]}
        buddies_10 = {'MPE': [2,9], 'SSASC': [5,9]}

        subect_and_class_11 = {'MPE': 1, 'SSASC': 2, 'ARSI': 3, 'DSG': 4, 'MRKT': 5}
        target_11 = {'MPE': [5]}
        give_ins_11 = {'SSASC': [2,1], 'ARSI': [3,1], 'DSG': [4,1], 'MRKT': [5,1]}

        subect_and_class_12 = {'MPE': 2, 'SSASC': 3, 'ARSI': 4, 'DSG': 5, 'MRKT': 1}
        target_12 = {'ARSI': [1,2,3,4], 'MPE': [5,1,3]}
        give_ins_12 = {'MRKT':[1,2,3], 'SSASC': [1,3,2], 'DSG': [3,5,2]}

        subect_and_class_13 = {'MPE': 3, 'SSASC': 4, 'ARSI': 5, 'DSG': 1, 'MRKT': 2}
        target_13 = {'MRKT': [2,5,3], 'DSG': [1,4], 'SSASC': [1,3,2,5]}
        give_ins_13 = {'ARSI':[1,5,3], 'MPE': [3,2,1]}

        subect_and_class_14 = {'MPE': 4, 'SSASC': 5, 'ARSI': 1, 'DSG': 2, 'MRKT': 3}
        target_14 = {'DSG': [1,2], 'MRKT': [4,5], 'ARSI': [4,3]}
        give_ins_14 = {'MPE':[1,4,3], 'SSASC': [5,3,2]}

        subect_and_class_15 = {'MPE': 5, 'SSASC': 1, 'ARSI': 2, 'DSG': 3, 'MRKT': 4}
        target_15 = {}
        give_ins_15 = {'MPE': [2,3,5], 'SSASC': [1,3,2], 'DSG': [3,5,1]}
        buddies_15 = {'ARSI': [10,11,12], 'MRKT': [1,3]}

        subect_and_class_16 = {'MPE': 1, 'SSASC': 2, 'ARSI': 3, 'DSG': 4, 'MRKT': 5}
        target_16 = {'SSASC': [5,1], 'MRKT': [1], 'MPE':[1,5,3]}
        give_ins_16 = {'DSG': [4,3,2], 'ARSI': [3,2]}

        subect_and_class_17 = {'MPE': 2, 'SSASC': 3, 'ARSI': 4, 'DSG': 5, 'MRKT': 1}
        target_17 = {'DSG': [1,5], 'MRKT': [5,1]}
        give_ins_17 = {'MPE':[5,2,3], 'SSASC': [5,3,1], 'ARSI': [1,2,4]}

        subect_and_class_18 = {'MPE': 3, 'SSASC': 4, 'ARSI': 5, 'DSG': 1, 'MRKT': 2}
        target_18 = {'MPE': [2,3], 'SSASC': [5,3,2]}
        give_ins_18 = {'DSG':[1,2,3,4,5], 'MRKT': [1,2,3,4,5], 'ARSI': [1,2,3,4,5]}

        subect_and_class_19 = {'MPE': 4, 'SSASC': 5, 'ARSI': 1, 'DSG': 2, 'MRKT': 3}
        target_19 = {'DSG': [4,2,5], 'SSASC': [5,1,4]}
        give_ins_19 = {'MPE': [1,2,3,4,5], 'MRKT': [1,2,3,4,5], 'ARSI': [1,2,3,4,5]}

        subect_and_class_20 = {'MPE': 5, 'SSASC': 1, 'ARSI': 2, 'DSG': 3, 'MRKT': 4}
        target_20 = {}
        give_ins_20 = {'DSG': [1,2,3,4,5], 'SSASC': [1,2,3,4,5], 'MRKT': [1,2,3,4,5]}
        buddies_20 = {'ARSI': [7,13], 'MPE': [12,19,9]}


        
        student_1 = Student(1, subect_and_class_1, target_1, give_ins_1, {})
        student_2 = Student(2, subect_and_class_2, target_2, give_ins_2, {})
        student_3 = Student(3, subect_and_class_3, target_3, give_ins_3, {})
        student_4 = Student(4, subect_and_class_4, target_4, give_ins_4, {})
        student_5 = Student(5, subect_and_class_5, target_5, give_ins_5, buddies_5)
        student_6 = Student(6, subect_and_class_6, target_6, give_ins_6, {})
        student_7 = Student(7, subect_and_class_7, target_7, give_ins_7, {})
        student_8 = Student(8, subect_and_class_8, target_8, give_ins_8, {})
        student_9 = Student(9, subect_and_class_9, target_9, give_ins_9, {})
        student_10 = Student(10, subect_and_class_10, target_10, give_ins_10, buddies_10)
        student_11 = Student(11, subect_and_class_11, target_11, give_ins_11, {})
        student_12 = Student(12, subect_and_class_12, target_12, give_ins_12, {})
        student_13 = Student(13, subect_and_class_13, target_13, give_ins_13, {})
        student_14 = Student(14, subect_and_class_14, target_14, give_ins_14, {})
        student_15 = Student(15, subect_and_class_15, target_15, give_ins_15, buddies_15)
        student_16 = Student(16, subect_and_class_16, target_16, give_ins_16, {})
        student_17 = Student(17, subect_and_class_17, target_17, give_ins_17, {})
        student_18 = Student(18, subect_and_class_18, target_18, give_ins_18, {})
        student_19 = Student(19, subect_and_class_19, target_19, give_ins_19, {})
        student_20 = Student(20, subect_and_class_20, target_20, give_ins_20, buddies_20)

        list_of_students = [student_1,
                            student_2,
                            student_3,
                            student_4,
                            student_5,
                            student_6,
                            student_7,
                            student_8,
                            student_9,
                            student_10,
                            student_11,
                            student_12,
                            student_13,
                            student_14,
                            student_15,
                            student_16,
                            student_17,
                            student_18,
                            student_19,
                            student_20]

        list_of_states = []

        for i in range(1,20, 2):
            copy = deepcopy(state)
            for k in range(i+1): copy.add_student(list_of_students[k])
            list_of_states.append(copy)

        return list_of_states
