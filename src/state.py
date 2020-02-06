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
                            score += 30         #the person is at the same class of his friend
                            i.alone = False     #Flag-- 
                        else: 
                            score -= 20
                        
            #checking target class
            for position, j in enumerate(i.subjects_and_classes): 
                if j in i.subject_targets.keys(): 
                    if i.subjects_and_classes[j] in i.subject_targets[j]:  
                        score += 40         #if the person got the target class 
                        i.target = True     #Flag--
                    else: 
                        score -= 30

                #checking givin classes 
                if j in i.subject_give_ins.keys():
                    if i.subjects_and_classes[j] in i.subject_give_ins[j]: 
                        score -= 3          #if a class was abdicated
                        i.givin = True    #Flag--
                    else: 
                        score += 5
                     

               #checking schedule conflicts. If two classes are incompatible then score = -inf 
                for p in range(position+1, len(list(i.subjects_and_classes.keys()))):
                    key = list(i.subjects_and_classes.keys())[p] 
                    sched_1 = self.class_schedules[translate_subject_and_class(j,i.subjects_and_classes[j])]
                    sched_2 = self.class_schedules[translate_subject_and_class(key, i.subjects_and_classes[key])] 
                    if (sched_1.conflicts(sched_2)):
                        score = float('-inf')
                        break 

            # Reading the method of gen states we have that it's just possible to trade classes in the givin list 
            # and target list, but the classes can remain the same. 
            # If there's no change in the classses, then givin = False and target = False 

            # If he gives up a class but didn't get the target nor he is with his buddy, then infinity 
            if i.givin and i.target and i.alone and list(i.buddies): 
                score = float('-inf')
                break 
            # If he gives up a class but didn't get the target and did not choose a buddy 
            if i.givin and not i.target and not list(i.buddies):
                score = float('-inf')
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



