from copy import deepcopy
import student
from schedule import Schedule 
import random

penalty = 1000

def translate_subjects_and_classes(subject, class_number):
    return subject + str(class_number)

class State:
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
    # This may seem weird, but the comparison is used in the priority queue, which gives more priority to smaller objects
    # Since we want the bigger objects first in the PQ, I created the operator this way
    def __lt__(self, other):
        return self.heuristic > other.heuristic 

    def __str__(self):
        #return str(self.heuristic)
        st = ""
        for i, student in self.students.items():
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

            #checking buddies 
            score_buddies = 0.5 * MAX_SCORE  # Gives 50% of importance to the buddies
            
            for subject in student.buddies: 
                n = len(student.buddies[subject])
                score_each_buddy = (2 * score_buddies)/(n * (n + 1))
                increment_buddies = n
                for numbers in student.buddies[subject]: 
                    if subject in self.students[numbers].subjects_and_classes:
                        if student.subjects_and_classes[subject] == self.students[numbers].subjects_and_classes[subject]: 
                            score += score_each_buddy * increment_buddies      # Adds points each time the buddie is in the same class
                            increment_buddies -= 1        # Removes some points depending on the priority 
                            alone = False
                        
            #checking if student got a target class
            score_target_class = 0.5 * MAX_SCORE  #Gives 50% of importance to the Target Classes
            score_each_target = (2*score_target_class)//((len(student.subjects_and_classes)+1)*len(student.subjects_and_classes))
            increment_targets = len(student.subjects_and_classes)

            for position, subject_1 in enumerate(student.subjects_and_classes): 
                
                if subject_1 in student.subject_targets.keys(): 
                    if student.subjects_and_classes[subject_1] in student.subject_targets[subject_1]:  
                        score += score_each_target * increment_targets   # Adds points each time it is in a target class
                        increment_targets-=1       # Removes some points depending on the priority
                        got_target = True 

                #checking if a student gave in any classes 
                if subject_1 in student.subject_give_ins.keys():
                    if student.original_sac[subject_1] != student.subjects_and_classes[subject_1]:
                        if student.subjects_and_classes[subject_1] in student.subject_give_ins[subject_1]:
                            gave_in = True

               #checking for schedule conflicts.
                for p in range(position+1, len(list(student.subjects_and_classes.keys()))):
                    key = list(student.subjects_and_classes.keys())[p] 
                    if translate_subjects_and_classes(subject_1,student.subjects_and_classes[subject_1]) in self.class_schedules:
                        if translate_subjects_and_classes(key, student.subjects_and_classes[key]) in self.class_schedules:
                            sched_1 = self.class_schedules[translate_subjects_and_classes(subject_1,student.subjects_and_classes[subject_1])]
                            sched_2 = self.class_schedules[translate_subjects_and_classes(key, student.subjects_and_classes[key])] 
                            if (sched_1.conflicts(sched_2)):
                                score -= penalty
                                self.conflicts += 1

            # If he gives up a class but didn't get the target nor he is with any of his buddies
            if gave_in and not got_target and alone: 
                score -= penalty
                self.didnt_get += 1

        self.heuristic = score
        return score 

    def add_schedule(self, subject, class_number, start_hour, end_hour, day):
        self.class_schedules[translate_subjects_and_classes(subject, class_number)] = Schedule(start_hour, end_hour, day)

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
    
    def new_neighbour(self):
        """
        Goes through every student and checks what is the first student
        it can trade classes with, this meaning, a student 
        that has 1 class in common with the first student and yields
        those changes.
        """
        list_students = []
        for _,elem in self.students.items():
            list_students.append(elem)
        for student_i, student in enumerate(list_students):            #go through every student; chooses 1st student
            
            student_classes = list(student.subjects_and_classes)                # *1 what are the subjects the 1st student attend to - student_classes should be student_subjects per say
            master_students = deepcopy(list_students)[student_i+1:]            #creates a new list with every student that hasn't gone through this process (every student that was 1st student)
            
            for trader_i, trader_student in enumerate(master_students):           #goes through students from the new list
                
                success = False
                
                trader_classes = list(trader_student.subjects_and_classes)          # *1 but with the new student
                
                if trader_student == student:
                    continue
                
                deploy_state = deepcopy(self)
                deploy_students = deepcopy(list_students)
                
                trader_i += student_i+1                             #why? since the new list used for the search of the new student was sliced we need to add the number of indexes that were cut
                
                for trade_class in student_classes:                     #goes through every subject the 1st student has
                    
                    if trade_class in trader_classes:                   #if the new student has that class it trades the class and the new list is yielded
                       
                        success = True
                        
                        deploy_students[student_i].subjects_and_classes[trade_class], deploy_students[trader_i].subjects_and_classes[trade_class] = deploy_students[trader_i].subjects_and_classes[trade_class], deploy_students[student_i].subjects_and_classes[trade_class]
                        
                        #print("------",student_i, trader_i,trade_class) 
                        
                        deploy_dict = {}
                        for elem in deploy_students:
                            deploy_dict[elem.student_id] = elem
                        
                        deploy_state.students = deploy_dict
                        yield deploy_state
                        break
                
                if success == True:
                    break

    def random_neighbour(self):
        list_students = []
        for elem in self.students.values():
            list_students.append(elem)
        master_students = deepcopy(list_students)
        used_master = []
        while (len(used_master) != len(master_students)):
            student_i = random.randrange(0,len(master_students))
            if student_i in used_master:
                continue
            student = master_students[student_i]
            student_classes = list(student.subjects_and_classes)
            temp_students = deepcopy(list_students)
            used_master.append(student_i)
            used_child = [student_i,]
            while (len(used_child)!=len(temp_students)):
                success = False
                trader_i = random.randrange(0,len(temp_students))
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

                        deploy_students[student_i].subjects_and_classes[trade_class], deploy_students[trader_i].subjects_and_classes[trade_class] = deploy_students[trader_i].subjects_and_classes[trade_class], deploy_students[student_i].subjects_and_classes[trade_class]
                
                        deploy_dict = {}
                        for elem in deploy_students:
                            deploy_dict[elem.student_id] = elem

                        deploy_state.students = deploy_dict

                        return deploy_state
                        break
                if success == True:
                    break

    