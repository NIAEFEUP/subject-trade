class State:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def generate_neighbour(self):
        for student in self.students: # select a student
            for target_subject in student.subject_targets: # select a subject that has target classes (classes that the student wants to go to)
                for target_class in target_subject[1]: # select, for that subject, a possible target class

                    for trader_student in self.students: # find a trader student
                        if trader_student == student
                            continue

                        for trader_student_classes in 





class Student:
    # @param: subjects_and_classes looks like [[subject name, class number], ...]
    # Represents the class a student has for each subject.
    #
    # @param: subject_targets looks like [[subject name, [class number, ...]]], ...]
    # Represents the classes a student would like to trade to for each subject.
    #
    # @param: subject_give_ins looks like [[subject name, [class number,...]], ...]
    # Represents the classes for which the student would give in his place for each subject.
    def __init__(self, student_id, subjects_and_classes, subject_targets, subject_give_ins):
        self.student_id = student_id
        self.subjects_and_classes = subjects_and_classes 
        self.subject_targets = subject_targets
        self.subject_give_ins = subject_give_ins
    
    def add_subject_and_class(self, subject_name, class_name):
        self.subjects_and_classes.append([subject_name, class_name])

    def add_subject_target(self, subject_name, class_number):
        flag = False
        for st in self.subject_targets:
            if st[0] == subject_name:
                st[1].append(class_number)
                flag = True
        if not flag: self.subject_targets.append([subject_name, [class_number]])

    def add_subject_give_in(self, subject_name, class_number):
        flag = False
        for sgi in self.subject_give_ins:
            if sgi[0] == subject_name:
                sgi[1].append(class_number)
                flag = True
        if not flag: self.subject_give_ins.append([subject_name, [class_number]])


    # equality comparator overload (compares student ids)
    def __eq__(self, x):
        return self.student_id == x.student_id
    