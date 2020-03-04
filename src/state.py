from copy import deepcopy
from schedule import Schedule 

def translate_subject_and_class(subject, class_number):
    return subject + str(class_number)

class State:
    def __init__(self):
        self.students = {}
        self.class_schedules = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def get_score(self): 
        score = 0

        for student in self.students.values():

            alone = True
            gave_in = False
            got_target = False

            #checking buddies 
            for subject in student.buddies: 
                for numbers in set(student.buddies[subject]): 
                    if student.subjects_and_classes[subject] == self.students[numbers].subjects_and_classes[subject]: 
                        score += 30
                        alone = False
                        
            #checking if student got a target class
            for position, j in enumerate(student.subjects_and_classes): 
                if j in student.subject_targets.keys(): 
                    if student.subjects_and_classes[j] in student.subject_targets[j]:  
                        score += 40    
                        got_target = True 


                #checking if a student gave in any classes 
                if j in student.subject_give_ins.keys():
                    if student.subjects_and_classes[j] in student.subject_give_ins[j]: 
                        score -= 3
                        gave_in = True
                    else: 
                        score += 5
                     

               #checking for schedule conflicts.
                for p in range(position+1, len(list(student.subjects_and_classes.keys()))):
                    key = list(student.subjects_and_classes.keys())[p] 
                    sched_1 = self.class_schedules[translate_subject_and_class(j,student.subjects_and_classes[j])]
                    sched_2 = self.class_schedules[translate_subject_and_class(key, student.subjects_and_classes[key])] 
                    if (sched_1.conflicts(sched_2)):
                        return float('-inf')

            # If he gives up a class but didn't get the target nor he is with any of his buddies
            if gave_in and not got_target and alone: 
                return float('-inf')

        return score 


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



