from copy import deepcopy   

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
        if other.start_hour <= self.start_hour and self.start_hour < other.end_hour:
            return True
        elif other.start_hour < self.end_hour and self.end_hour <= other.end_hour:
            return True
        else: return False

class State:
    def __init__(self):
        self.students = {}
        self.class_schedules = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_schedule(self, subject, class_number, start_hour, end_hour):
        self.class_schedules[translate_subject_and_class(subject, class_number)] = Schedule(start_hour, end_hour)

    def trade_classes(self,student1_id,student2_id,subject_name):
        students = self.students
        student1_class = students[student1_id].get_class_for_subject(subject_name)
        student2_class = students[student2_id].get_class_for_subject(subject_name)       
        students[student1_id].set_class_for_subject(subject_name, student2_class)
        students[student2_id].set_class_for_subject(subject_name, student1_class)



    def generate_neighbour(self):
        for student_id,student in self.students.items(): # select a student

            for subject_name,target_classes in student.subject_targets.items(): # select a subject name and its respective  target classes
                student_class = student.get_class_for_subject(subject_name) # get the current class of the first student for that subject
                
                for target_class in target_classes: # select, for that subject, a possible target class
                    
                    for trader_id,trader_student in self.students.items(): # find a trader student
                        if trader_student == student:
                            continue
                        trader_class = trader_student.get_class_for_subject(subject_name) # get the class of the trader student, for that subject
                        
                        if trader_class is None or trader_class != target_class: # if target student does not have the desired class for that subject, continue
                            continue
                  
                        trader_targets = trader_student.get_targets_for_subject(subject_name) # get the targets for that subject, for the trader student

                        if trader_targets is not None and student_class in trader_targets:
                            state_targets = deepcopy(self)
                            state_targets.trade_classes(student_id,trader_id,subject_name) #trades the students classes for that subject
                            yield state_targets

                        trader_give_ins = trader_student.get_giveins_for_subject(subject_name)

                        if trader_give_ins is not None and student_class in trader_give_ins:
                            state_give_ins = deepcopy(self)
                            state_give_ins.trade_classes(student_id,trader_id,subject_name)
                            yield state_give_ins
  




class Student:
    def __init__(self, student_id, subjects_and_classes, subject_targets, subject_give_ins, buddies):
        self.student_id = student_id
        self.subjects_and_classes = subjects_and_classes 
        self.subject_targets = subject_targets
        self.subject_give_ins = subject_give_ins
        self.buddies = buddies
    
    def add_subject_and_class(self, subject_name, class_number):
        self.subjects_and_classes[subject_name] = class_number

    def add_subject_target(self, subject_name, class_number):
        self.subject_targets[subject_name].append(class_number)

    def remove_subject_target(self,subject_name):
        del self.subject_targets[subject_name]

    def add_subject_give_in(self, subject_name, class_number):
        self.subject_give_ins[subject_name].append(class_number)

    def add_buddy(self, subject_name, buddies_up):
        for buddy in buddies_up:
            self.buddies[subject_name] = buddy

    def get_class_for_subject(self, subject):
        if subject in self.subjects_and_classes :
            return self.subjects_and_classes[subject]
        return None

    def set_class_for_subject(self, subject, subject_class):
        if subject in self.subjects_and_classes:
            self.subjects_and_classes[subject] = subject_class

    def get_targets_for_subject(self, subject):
        if subject in self.subject_targets:
            return self.subject_targets[subject]
        return None

    def __str__(self):
        return "\nID: " + str(self.student_id) + "\nClasses: " + str(self.subjects_and_classes) + "\nTarget Classes: " + str(self.subject_targets) + "\nGive ins" + str(self.subject_give_ins)
         
    def get_giveins_for_subject(self, subject):
        if subject in self.subject_give_ins:
            return self.subject_give_ins[subject]
        return None

    def __eq__(self, x):
        return self.student_id == x.student_id




