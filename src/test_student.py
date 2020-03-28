import unittest
import student

class Test_Student(unittest.TestCase): 


    def setUp(self):
        student_no_giveIn = student.Student(200000001, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : [2]}, {}, {"LPOO" : [201603820]})
        student_no_target = student.Student(200000002, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {}, {}, {"LPOO" : [201603820]})
        student_no_buddies = student.Student(200000003, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : [2]}, {}, {})
        perfectStudent = student.Student(2000000004, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {}, {})
        student1 = student.Student(200000000, {"LPOO" : 1}, {"LPOO" : [2]}, {"LPOO" : [2]}, {"LPOO" : [201603820]})
        studentEmpty = student.Student(200000001, {}, {}, {}, {})




    def test_constructor(self): 
        student1 = student.Student(200000000, {"LPOO" : 1}, {"LPOO" : [2]}, {"LPOO" : [2]}, {"LPOO" : [201603820]})

        #Should it allow to have the same give in and target?


        self.assertEqual(student1.student_id,200000000)
        self.assertNotEqual(student1.student_id,201603820)
        self.assertEqual(student1.subjects_and_classes,{"LPOO" : 1})
        self.assertNotEqual(student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 1})
        self.assertEqual(student1.subject_targets, {"LPOO" : [2]})
        self.assertEqual(student1.subject_give_ins, {"LPOO" : [2]})
        self.assertEqual(student1.buddies, {"LPOO" : [201603820]})

    def test_add_subject_and_class(self):

        #Should test if a class exists?
        #Should not permit more than 7 classes

        student_too_many_classes = student.Student(200000000, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1, "CGRA" : 1, "BDAD" : 1, "PLOG": 1, "IART" : 1}, {}, {}, {})


        # Add normal class
        student1.add_subject_and_class("CAL" , 5)
        self.assertEqual(student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 5})
        self.assertNotEqual(student1.subjects_and_classes,{"LPOO" : 1})

        #Add class to students that does not have any
        studentEmpty.add_subject_and_class("CAL" , 5)
        self.assertEqual(studentEmpty.subjects_and_classes,{"CAL" : 5})

        #Add repeated class
        student1.add_subject_and_class("CAL" , 5)
        self.assertEqual(student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 5})

        
        #Add repeated class
        student_too_many_classes.add_subject_and_class("PROG" , 1)
        self.assertEqual(student_too_many_classes.subjects_and_classes,{"LPOO" : 1, "CAL" : 1, "SOPE" : 1, "CGRA" : 1, "BDAD" : 1, "PLOG": 1, "IART" : 1})

    def test_add_subject_target(self):
    


        student1 = student.Student(200000000, {"LPOO" : 1}, {"LPOO" : [2]}, {"LPOO" : [2]}, {"LPOO" : [201603820]})
        studentEmpty = student.Student(200000001, {}, {}, {}, {})

        # Add normal class
        student1.add_subject_and_class("CAL" , 5)
        self.assertEqual(student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 5})
        self.assertNotEqual(student1.subjects_and_classes,{"LPOO" : 1})

        #Add class to students that does not have any
        studentEmpty.add_subject_and_class("CAL" , 5)
        self.assertEqual(studentEmpty.subjects_and_classes,{"CAL" : 5})

        #Add repeated class
        student1.add_subject_and_class("CAL" , 5)
        self.assertEqual(student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 5})

        
        #Add repeated class
        student_too_many_classes.add_subject_and_class("PROG" , 1)
        self.assertEqual(student_too_many_classes.subjects_and_classes,{"LPOO" : 1, "CAL" : 1, "SOPE" : 1, "CGRA" : 1, "BDAD" : 1, "PLOG": 1, "IART" : 1})




        



        
    # def test_higher(self):
    #     # Test by hour
    #     h1 = hour.Hour(12,10)    
    #     h2 = hour.Hour(13,10)
    #     self.assertEqual(True, h2>h1)
    #     self.assertEqual(False, h1>h2)
    #     # Test by minutes
    #     h1 = hour.Hour(12,10)
    #     h2 = hour.Hour(12, 11)
    #     self.assertEqual(True,h2>h1)  
    #     self.assertEqual(False,h1>h2)
    #     #Test Equals
    #     h1 = hour.Hour(12,12)
    #     h2 = hour.Hour(12,12)
    #     self.assertEqual(False, h1>h2)

    # def test_equal(self):
    #     h1 = hour.Hour(12,10)    
    #     h2 = hour.Hour(13,10)
    #     h3 = hour.Hour(13,10)
    #     self.assertFalse(h1 == h2)
    #     self.assertTrue(h2 == h3)


if __name__ == '__main__': 
    unittest.main() 

