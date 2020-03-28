import unittest
import student

class Test_Student(unittest.TestCase): 


    def setUp(self):
        self.student_no_giveIn = student.Student(200000001, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : [2]}, {}, {"LPOO" : [201603820]})
        self.student_no_target = student.Student(200000002, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {}, {}, {"LPOO" : [201603820]})
        self.student_no_buddies = student.Student(200000003, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : [2]}, {}, {})
        self.perfectStudent = student.Student(2000000004, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {}, {})
        self.student1 = student.Student(200000000, {"LPOO" : 1}, {"LPOO" : [2]}, {"LPOO" : [2]}, {"LPOO" : [201603820]})
        self.studentEmpty = student.Student(200000001, {}, {}, {}, {})




    def test_constructor(self): 
        self.student1 = student.Student(200000000, {"LPOO" : 1}, {"LPOO" : [2]}, {"LPOO" : [2]}, {"LPOO" : [201603820]})

        #Should it allow to have the same give in and target?

        self.assertEqual(self.student1.student_id,200000000)
        self.assertNotEqual(self.student1.student_id,201603820)
        self.assertEqual(self.student1.subjects_and_classes,{"LPOO" : 1})
        self.assertNotEqual(self.student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 1})
        self.assertEqual(self.student1.subject_targets, {"LPOO" : [2]})
        self.assertEqual(self.student1.subject_give_ins, {"LPOO" : [2]})
        self.assertEqual(self.student1.buddies, {"LPOO" : [201603820]})

    def test_add_subject_and_class(self):

        #Should test if a class exists?
        #Should not permit more than 7 classes

        student_too_many_classes = student.Student(200000000, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1, "CGRA" : 1, "BDAD" : 1, "PLOG": 1, "IART" : 1}, {}, {}, {})

        # Add normal class
        self.student1.add_subject_and_class("CAL" , 5)
        self.assertEqual(self.student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 5})
        self.assertNotEqual(self.student1.subjects_and_classes,{"LPOO" : 1})

        #Add class to students that does not have any
        self.studentEmpty.add_subject_and_class("CAL" , 5)
        self.assertEqual(self.studentEmpty.subjects_and_classes,{"CAL" : 5})

        #Add repeated class
        self.student1.add_subject_and_class("CAL" , 5)
        self.assertEqual(self.student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 5})

        
        #Try to add more than 7 classes
        student_too_many_classes.add_subject_and_class("PROG" , 1)
        self.assertEqual(student_too_many_classes.subjects_and_classes,{"LPOO" : 1, "CAL" : 1, "SOPE" : 1, "CGRA" : 1, "BDAD" : 1, "PLOG": 1, "IART" : 1})

    def test_add_subject_target(self):

        #Should we verify if is trying to add target class he is already in?
    
        # Add subject
        self.student_no_target.add_subject_target("CAL" , 5)
        self.assertEqual(self.student_no_target.subject_targets,{"CAL" : [5]})

        #Add class to a subject
        self.student_no_target.add_subject_target("CAL" , 4)
        self.assertEqual(self.student_no_target.subject_targets,{"CAL" : [5,4]})

        #Try to add class that he does not belong too
        self.student_no_target.add_subject_target("ZZZ" , 5)
        self.assertNotEqual(self.student_no_target.subject_targets,{"CAL" : [5,4], "ZZZ" : 5})
        self.assertEqual(self.student_no_target.subject_targets,{"CAL" : [5,4]})




if __name__ == '__main__': 
    unittest.main() 

