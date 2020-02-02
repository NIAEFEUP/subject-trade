from state import State 
from student import Student 
from hour import Hour 
from schedule import Schedule
from random import randint 

subjects_and_classes1 = {"LPOO": 1,"TCOM": 1,"MDIS": 1,"PLOG": 1}
subject_targets1 = {"LPOO": [2,3],"TCOM": [4,5]}
subject_give_ins1 = {"MDIS": [2,3],"PLOG": [4,5]}

s1 = Student(201800175, subjects_and_classes1, subject_targets1, subject_give_ins1, {})

subjects_and_classes2 = {"LPOO": 2, "TCOM": 7, "MDIS": 4, "PLOG": 1, "SINF": 1}
subject_targets2 = {"MDIS": [1]}
subject_give_ins2 = {"LPOO": [3,7], "SINF": [2,4,1,7]}

s2 = Student(201800149, subjects_and_classes2, subject_targets2, subject_give_ins2, {})


#Test with score for target and buddy
subjects_and_classes1 = {"LPOO": 2,"TCOM": 1,"MDIS": 1,"PLOG": 1}
subject_targets1 = {"LPOO": [2,3],"TCOM": [4,5]}
subject_give_ins1 = {"MDIS": [2,3],"PLOG": [4,5]}
s1 = Student(201800175, subjects_and_classes1, subject_targets1, subject_give_ins1, {})

subjects_and_classes2 = {"LPOO": 3, "TCOM": 7, "MDIS": 1, "PLOG": 1, "SINF": 1}
subject_targets2 = {"MDIS": [1]}
subject_give_ins2 = {"LPOO": [3,7], "SINF": [2,4,1,7]}
s2 = Student(201800149, subjects_and_classes2, subject_targets2, subject_give_ins2, {})


s1.add_buddy("MDIS", [201800149])
s2.add_buddy("LPOO",[201800175])
s2.add_buddy("PLOG",[201800175])
print(s1.buddies)

#Random schedule ------------------------------------------------------------------------------------ [STATE 1]
state_1 = State()
state_1.add_student(s1)
state_1.add_student(s2) 
print("STATE_STUDENTS", state_1.students)


for i in ["LPOO", "TCOM", "MDIS", "PLOG", "SINF"]: 
    for j in range(1,8): 
        hour_1 = Hour(randint(1,24), randint(1,60))
        state_1.add_schedule(i, j, hour_1, Hour(randint(hour_1.hours,24),randint(1,60)))

# Correct schedule with no conflict ------------------------------------------------------------------ [STATE 2]

state_2 = State()
state_2.add_student(s1)
state_2.add_student(s2) 
print("STATE_STUDENTS", state_1.students)

for number, subject in enumerate(["LPOO", "TCOM", "MDIS", "PLOG", "SINF"]):
    for j in range(1,8): 
        hour_2 = Hour(number, randint(1,50))
        state_2.add_schedule(subject, j, hour_2, Hour(hour_2.hours, hour_2.hours + 9))

# Wrong state the person got nothing. It's not with his buddy, neither target, neither any givin -------[STATE 3] 

subjects_and_classes1 = {"LPOO": 4,"TCOM": 1,"MDIS": 1,"PLOG": 1}
subject_targets1 = {"LPOO": [2,3],"TCOM": [4,5]}
subject_give_ins1 = {"MDIS": [2,3],"PLOG": [4,5]}

s1 = Student(201800175, subjects_and_classes1, subject_targets1, subject_give_ins1, {})

subjects_and_classes2 = {"LPOO": 2, "TCOM": 7, "MDIS": 4, "PLOG": 1, "SINF": 3}
subject_targets2 = {"MDIS": [1]}
subject_give_ins2 = {"LPOO": [3,7], "SINF": [2,4,1,7]}

s2 = Student(201800149, subjects_and_classes2, subject_targets2, subject_give_ins2, {})

s1.add_buddy("MDIS", [201800149])
s2.add_buddy("LPOO",[201800175])
s2.add_buddy("PLOG",[201800175])

state_3 = State()
state_3.add_student(s1)
state_3.add_student(s2) 
print("STATE_STUDENTS", state_1.students)

for number, subject in enumerate(["LPOO", "TCOM", "MDIS", "PLOG", "SINF"]):
    for j in range(1,8): 
        hour_3 = Hour(number, randint(1,50))
        state_3.add_schedule(subject, j, hour_2, Hour(hour_2.hours, hour_2.hours + 9))


# Test to check schedules 
# for i in state_1.class_schedules.keys():
#     print(i)
#     print(state_1.class_schedules[i].start_hour.hours)
#     print(state_1.class_schedules[i].end_hour.hours)


print(state_1.get_score())
print(state_2.get_score())
print(state_3.get_score())
