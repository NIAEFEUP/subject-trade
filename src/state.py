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
        #if traded the subject as expected get score
        for i in self.students.values(): 
            #checking buddies 
            for numbers in set(list(i.buddies.values())):
                    for classes in set(list(i.buddies.keys())): 
                        if i.subjects_and_classes[classes] == self.students[numbers].subjects_and_classes[classes]: 
                            score += 30 
                        else: 
                            score -= 20
                        

            for position, j in enumerate(i.subjects_and_classes): 
                if j in i.subject_targets.keys(): 
                    # check if the student got the target class 
                    if i.subjects_and_classes[j] in i.subject_targets[j]:  
                        score += 40
                    else: 
                        score -= 30

                if j in i.subject_give_ins.keys():
                    # check the givin classes but not so much
                    if i.subjects_and_classes[j] in i.subject_give_ins[j]: 
                        score -= 3      #if a class was abdicated
                    else: 
                        score += 5
                     

               #checking schedule conflicts. If two classes are incompatible then score = -100000
                for p in range(position+1, len(list(i.subjects_and_classes.keys()))):
                    key = list(i.subjects_and_classes.keys())[p] 
                    sched_1 = self.class_schedules[translate_subject_and_class(j,i.subjects_and_classes[j])]
                    sched_2 = self.class_schedules[translate_subject_and_class(key, i.subjects_and_classes[key])] 
                    if (sched_1.conflicts(sched_2)):
                        score = -100000
                        # tests to print, please don't delete
                        # print("--Conflict between: {%s,%s}" %(name_1, name_2))
                        # print("----HOURS_1----")
                        # print("START: %i \n END_ %i" %(sched_1.start_hour.hours, sched_1.end_hour.hours))
                        # print("---HOURS_2----")
                        # print("START: %i \n END_ %i" %(sched_2.start_hour.hours, sched_2.end_hour.hours))
                        break 
                               
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



