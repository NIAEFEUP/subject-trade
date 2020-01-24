def translate_subject_and_class(subject, class_number):
    return subject + str(class_number)


class Hour:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __lt__(self, other):
        if self.hours == other.hours:
            return self.minutes < other.minutes

        return self.hours < other.hours

    def __le__(self, other):
        if self.hours == other.hours:
            return self.minutes <= other.minutes

        return self.hours <= other.hours


class Schedule:
    def __init__(self, start_hour, end_hour):
        self.start_hour = start_hour
        self.end_hour = end_hour

    def conflicts(self, other):
        flag = False
        if other.start_hour <= self.start_hour and self.start_hour < other.end_hour:
            flag = True

        if other.start_hour < self.end_hour and self.end_hour <= other.end_hour:
            flag = True

        return flag


class State:
    def __init__(self):
        self.students = []
        self.class_schedules = {}

    def add_schedule(self, subject, class_number, start_hour, end_hour):
        self.class_schedules[translate_subject_and_class(subject, class_number)] = Schedule(start_hour, end_hour)

    def add_student(self, student):
        self.students.append(student)


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
