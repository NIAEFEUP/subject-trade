class State:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, student_id, subjects_and_classes):
        self.student_id = student_id
        self.subjects_and_classes = subjects_and_classes
    
    def subject_and_class(self, subject_name, class_name):
        self.subjects_and_classes.append([subject_name, class_name])

    