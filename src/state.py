from copy import deepcopy   

class State:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


    #Given two students and a subject, trades their classes for that given subject
    def trade_classes(self,student1,student2,subject_name):

        student1_class = student1.get_class_for_subject(subject_name)
        student2_class = student2.get_class_for_subject(subject_name)
        student1.set_class_for_subject(subject_name, student2_class)
        student2.set_class_for_subject(subject_name, student1_class)


    def generate_neighbour(self):

        for student_index,student in enumerate(self.students,start=1): # select a student


            for subject_name,target_classes in student.subject_targets.items(): # select a subject name and its respective  target classes

                student_class = student.get_class_for_subject(subject_name) # get the current class of the first student for that subject


                for target_class in target_classes: # select, for that subject, a possible target class

                    for trader_student in self.students[student_index:]: # find a trader student
                        if trader_student == student:
                            continue
                        
                        trader_class = trader_student.get_class_for_subject(subject_name) # get the class of the trader student, for that subject

                        if trader_class is None or trader_class != target_class: # if target student does not have the desired class for that subject, continue
                            continue
                  
                        trader_targets = trader_student.get_targets_for_subject(subject_name) # get the targets for that subject, for the trader student
                        
                        if trader_targets is not None and student_class in trader_targets:
                            state = deepcopy(self)
                            state.trade_classes(student,trader_student,subject_name) #trades the students classes for that subject
                            yield state
                                     
                        #Afinal os give in so vao ser feitos depois de já se ter verificado os targets todos
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
    
    def add_subject_and_class(self, subject_name, class_number):
        self.subjects_and_classes[subject_name] = class_number

    def add_subject_target(self, subject_name, class_number):
        self.subject_targets[subject_name].append(class_number)


    def remove_subject_target(self,subject_name):
        del self.subject_targets[subject_name]


    def add_subject_give_in(self, subject_name, class_number):
        self.subject_give_ins[subject_name].append(class_number)



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
        return "\nID: " + str(self.student_id) + "\nClasses: " + str(self.subjects_and_classes) + "\nTarget Classes: " + str(self.subject_targets)
         

    def get_giveins_for_subject(self, subject):
        if subject in self.subject_give_ins:
            return self.subject_give_ins[subject]

        return None

    
    # equality comparator overload (compares student ids)
    def __eq__(self, x):
        return self.student_id == x.student_id



#TESTING

#First Student
subjects_and_classes1 = {"LPOO": 1,"TCOM": 1,"MDIS": 1,"PLOG": 1}
subject_targets1 = {"LPOO": [2,3],"TCOM": [4,5]}
subject_give_ins1 = {"MDIS": [2,3],"PLOG": [4,5]}


a = Student(201603820,subjects_and_classes1,subject_targets1,subject_give_ins1)


#Second student
subjects_and_classes2 = {"LPOO": 2,"TCOM": 4,"MDIS": 2,"PLOG": 4}
subject_targets2 = {"LPOO": [1,4], "TCOM": [1,5]}
subject_give_ins2 = {"MDIS": [1,3],"PLOG": [1,5]}
b = Student(201703820,subjects_and_classes2,subject_targets2,subject_give_ins2)

#Creates the state
state = State()

#Add both students
state.add_student(a)
state.add_student(b)

#print("\nID: ",a.student_id,"\nClasses: ",a.subjects_and_classes,"\nTarget Classes: ",a.subject_targets)
#print("\nID: ",b.student_id,"\nClasses",b.subjects_and_classes,"\nTarget Classes",b.subject_targets)

print("First State")
for student in state.students:
    print(student)


print("\nNew State")
for neighbor in state.generate_neighbour():

    for student in neighbor.students:
        print(student)




