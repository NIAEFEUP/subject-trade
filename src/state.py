class State:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def trade_classes(self,student1,student2):
        print("ZAs")

    def generate_neighbour(self):
        for student in self.students: # select a student
            for target_subject in student.subject_targets: # select a subject that has target classes (classes that the student wants to go to)

                subject_name = target_subject[0]
                student_class = student.get_class_for_subject(subject_name) # get the current class of the first student for that subject


                for target_class in target_subject[1]: # select, for that subject, a possible target class
        

                    for trader_student in self.students: # find a trader student
                        if trader_student == student:
                            continue
                        
                        trader_class = trader_student.get_class_for_subject(subject_name) # get the class of the trader student, for that subject

                        if trader_class is None or trader_class != target_class: # if target student does not have the desired class for that subject, continue
                            continue


                        trader_targets = trader_student.get_targets_for_subject(subject_name) # get the targets for that suject, for the trader student
                        if trader_targets is not None and student_class in trader_targets:
                            student.set_class_for_subject(subject_name, trader_class)
                            student.remove_subject_target(subject_name)
                            
                            


                        trader_giveins = trader_student.get_giveins_for_subject(subject_name) # get the giveins for that subject, for the trader student
                        #if trader_giveins is not None and student_class in trader_giveins:
                            # TODO: GENERATE NEW STATE, SWITCH CLASSES AND FINISH




class Student:
    # @param: subjects_and_classes looks like [[subject name, class number], ...]
    # Represents the class a student has for each subject.
    #
    # @param: subject_targets looks like [[subject name, [class number, ...]], ...]
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

    def remove_subject_target(self,subject_name):
        for subject_target in self.subject_targets:
            if subject_target[0] == subject_name:
                self.subject_targets.remove(subject_target)

    def add_subject_give_in(self, subject_name, class_number):
        flag = False
        for sgi in self.subject_give_ins:
            if sgi[0] == subject_name:
                sgi[1].append(class_number)
                flag = True
        if not flag: self.subject_give_ins.append([subject_name, [class_number]])


    def get_class_for_subject(self, subject):
        for subject_and_class in self.subjects_and_classes:
            if subject_and_class[0] == subject:
                return subject_and_class[1]
        return None

    def set_class_for_subject(self, subject, subject_class):
        for i, subject_and_class in enumerate(self.subjects_and_classes):
            if subject_and_class[0] == subject:
                self.subjects_and_classes[i][1] = subject_class
                return

    def get_targets_for_subject(self, subject):
        for subject_and_targets in self.subject_targets:
            if subject_and_targets[0] == subject:
                return subject_and_targets[1]
        return None

    def get_giveins_for_subject(self, subject):
        for subject_and_giveins in self.subject_give_ins:
            if subject_and_giveins[0] == subject:
                return subject_and_giveins[1]
        return None


    # equality comparator overload (compares student ids)
    def __eq__(self, x):
        return self.student_id == x.student_id



#TESTING

#First Student
subjects_and_classes1 = [["LPOO",1],["TCOM",1],["MDIS",1],["PLOG",1]]
subject_targets1 = [["LPOO",[2,3]],["TCOM",[4,5]]]
subject_give_ins1 = [["MDIS",[2,3]],["PLOG",[4,5]]] 
a = Student(201603820,subjects_and_classes1,subject_targets1,subject_give_ins1)


#Second student
subjects_and_classes2 = [["LPOO",2],["TCOM",4],["MDIS",2],["PLOG",4]]
subject_targets2 = [["LPOO",[1,4]],["TCOM",[1,5]]]
subject_give_ins2 = [["MDIS",[1,3]],["PLOG",[1,5]]] 
b = Student(201703820,subjects_and_classes2,subject_targets2,subject_give_ins2)

#Creates the state
state = State()

#Add both students
state.add_student(a)
state.add_student(b)

print("\nID: ",a.student_id,"\nClasses: ",a.subjects_and_classes,"\nTarget Classes: ",a.subject_targets)
print("\nID: ",b.student_id,"\nClasses",b.subjects_and_classes,"\nTarget Classes",b.subject_targets)

state.generate_neighbour()


#First Student after trading
print("\nID: ",a.student_id,"\nClasses: ",a.subjects_and_classes,"\nTarget Classes: ",a.subject_targets)

