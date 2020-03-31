import unittest
import student

class Test_Student(unittest.TestCase): 


    def setUp(self):
        self.student_no_giveIn = student.Student(200000001, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : [2]}, {}, {"LPOO" : [201603820]})
        self.student_no_target = student.Student(200000002, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {}, {}, {"LPOO" : [201603820]})
        self.student_no_buddies = student.Student(200000003, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : [2]}, {}, {})
        self.perfectStudent = student.Student(2000000004, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : [1], "CAL" : [1], "SOPE" : [1]}, {}, {})
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

        student_too_many_classes = student.Student(200000000, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1, "CGRA" : 1, "BDAD" : 1, "PLOG": 1, "IART" : 1}, {}, {}, {})

        # Add normal class
        self.assertEqual(self.student1.add_subject_and_class("CAL" , 5),True)
        self.assertEqual(self.student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 5})
        self.assertNotEqual(self.student1.subjects_and_classes,{"LPOO" : 1})

        #Add class to students that does not have any
        self.assertEqual(self.studentEmpty.add_subject_and_class("CAL" , 5),True)
        self.assertEqual(self.studentEmpty.subjects_and_classes,{"CAL" : 5})

        #Add repeated class
        self.assertEqual(self.student1.add_subject_and_class("CAL" , 5),True)
        self.assertEqual(self.student1.subjects_and_classes,{"LPOO" : 1, "CAL" : 5})

        
        #Try to add more than 7 classes
        self.assertEqual(student_too_many_classes.add_subject_and_class("PROG" , 1),False)
        self.assertEqual(student_too_many_classes.subjects_and_classes,{"LPOO" : 1, "CAL" : 1, "SOPE" : 1, "CGRA" : 1, "BDAD" : 1, "PLOG": 1, "IART" : 1})

    def test_add_subject_target(self):

        #Should we verify if is trying to add target class he is already in?
    
        # Add subject
        self.assertEqual(self.student_no_target.add_subject_target("CAL" , 5),True)
        self.assertEqual(self.student_no_target.subject_targets,{"CAL" : [5]})

        #Add class to a subject
        self.assertEqual(self.student_no_target.add_subject_target("CAL" , 4),True)
        self.assertEqual(self.student_no_target.subject_targets,{"CAL" : [5,4]})

        #Try to add class that he does not belong too
        self.assertEqual(self.student_no_target.add_subject_target("ZZZ" , 5),False)
        self.assertNotEqual(self.student_no_target.subject_targets,{"CAL" : [5,4], "ZZZ" : 5})
        self.assertEqual(self.student_no_target.subject_targets,{"CAL" : [5,4]})

    def test_remove_subject_target(self):
    
        # self.perfectStudent = student.Student(2000000004, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {}, {})
        student2 = student.Student(2000000000, {"LPOO" : 1}, {"LPOO" : [1,2,3,4]}, {}, {})
        
        # Remove subject target
        self.assertEqual(self.perfectStudent.remove_subject_target("CAL"),True)
        self.assertEqual(self.perfectStudent.subject_targets,{"LPOO" : [1], "SOPE" : [1]})

        # Remove subject target that does not exist
        self.assertEqual(self.perfectStudent.remove_subject_target("ZZZ"),False)
        self.assertEqual(self.perfectStudent.subject_targets,{"LPOO" : [1], "SOPE" : [1]})

        #Remove subject class 
        self.assertEqual(student2.remove_subject_target_class("LPOO",3),True)
        self.assertEqual(student2.subject_targets,{"LPOO" : [1,2,4]})

        #Remove subject class that does not exist
        self.assertEqual(student2.remove_subject_target_class("LPOO",3),False)
        self.assertEqual(student2.subject_targets,{"LPOO" : [1,2,4]})

        #Remove subject that does not exist
        self.assertEqual(student2.remove_subject_target_class("CAL",3),False)
        self.assertEqual(student2.subject_targets,{"LPOO" : [1,2,4]})


    def test_add_subject_give_ins(self):
    
        #Should we verify if is trying to add target class he is already in?
    
        # Add subject
        self.assertEqual(self.student_no_giveIn.add_subject_give_in("CAL" , 5),True)
        self.assertEqual(self.student_no_giveIn.subject_give_ins,{"CAL" : [5]})

        #Add class to a subject
        self.assertEqual(self.student_no_giveIn.add_subject_give_in("CAL" , 4),True)
        self.assertEqual(self.student_no_giveIn.subject_give_ins,{"CAL" : [5,4]})

        #Try to add class that he does not belong too
        self.assertEqual(self.student_no_giveIn.add_subject_give_in("ZZZ" , 5),False)
        self.assertNotEqual(self.student_no_giveIn.subject_give_ins,{"CAL" : [5,4], "ZZZ" : 5})
        self.assertEqual(self.student_no_giveIn.subject_give_ins,{"CAL" : [5,4]})

    def test_remove_subject_give_in(self):
        
        # self.perfectStudent = student.Student(2000000004, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {"LPOO" : 1, "CAL" : 1, "SOPE" : 1}, {}, {})
        student2 = student.Student(2000000000, {"LPOO" : 1}, {}, {"LPOO" : [1,2,3,4] , "CAL" : [1]}, {})
        
        # Remove subject target
        self.assertEqual(student2.remove_subject_give_in("CAL"),True)
        self.assertEqual(student2.subject_give_ins,{"LPOO" : [1,2,3,4] })

        # Remove subject target that does not exist
        self.assertEqual(student2.remove_subject_give_in("ZZZ"),False)
        self.assertEqual(student2.subject_give_ins,{"LPOO" : [1,2,3,4] })

        #Remove subject class 
        self.assertEqual(student2.remove_subject_give_in_class("LPOO",3),True)
        self.assertEqual(student2.subject_give_ins,{"LPOO" : [1,2,4]})

        #Remove subject class that does not exist
        self.assertEqual(student2.remove_subject_give_in_class("LPOO",3),False)
        self.assertEqual(student2.subject_give_ins,{"LPOO" : [1,2,4]})

        #Remove subject that does not exist
        self.assertEqual(student2.remove_subject_give_in_class("CAL",3),False)
        self.assertEqual(student2.subject_give_ins,{"LPOO" : [1,2,4]})

    def test_add_buddies(self):
       
        # Add buddie
        self.assertEqual(self.student_no_buddies.add_buddie("LPOO" , 200000000),True)
        self.assertEqual(self.student_no_buddies.buddies, {"LPOO": [200000000]})
        

        #Add buddie to a subject
        self.assertEqual(self.student_no_buddies.add_buddie("LPOO" , 200000001),True)
        self.assertEqual(self.student_no_buddies.buddies,{"LPOO" : [200000000,200000001]})

        #Try to add class that he does not belong too
        self.assertEqual(self.student_no_buddies.add_buddie("ZZZ" , 200000005),False)
        self.assertNotEqual(self.student_no_buddies.buddies,{"LPOO" : [200000000,200000001], "ZZZ" : 200000005})
        self.assertEqual(self.student_no_buddies.buddies,{"LPOO" : [200000000,200000001]})

        # Add buddies
        self.student_no_buddies.add_buddies("CAL" , [200000000,20000001])
        self.assertEqual(self.student_no_buddies.buddies,{"LPOO" : [200000000,200000001] , "CAL" : [200000000,20000001]})

        # Add buddies to a subject
        self.student_no_buddies.add_buddies("CAL" , [20000002])
        self.assertEqual(self.student_no_buddies.buddies,{"LPOO" : [200000000,200000001] , "CAL" : [200000000,20000001,20000002]})

        # Add buddies to a subject
        self.student_no_buddies.add_buddies("CAL" , [20000002])
        self.assertEqual(self.student_no_buddies.buddies,{"LPOO" : [200000000,200000001] , "CAL" : [200000000,20000001,20000002]})


    def test_remove_buddie(self):
        
        student2 = student.Student(2000000000, {"LPOO" : 1}, {}, {"LPOO" : [1,2,3,4] , "CAL" : [1]}, {"LPOO": [20000000,20000001,20000002,20000003], "CAL" : 20000000})
        
        # Remove class from buddies
        student2.remove_buddie("CAL")
        self.assertEqual(student2.buddies,{"LPOO": [20000000,20000001,20000002,20000003] })

        # Remove buddies from class that does not exist
        student2.remove_buddie("ZZZ")
        self.assertEqual(student2.buddies,{"LPOO": [20000000,20000001,20000002,20000003]})

        #Remove buddie from class
        student2.remove_buddie_class("LPOO",20000000)
        self.assertEqual(student2.buddies,{"LPOO": [20000001,20000002,20000003]})

        #Remove buddie from subject that does not exist
        student2.remove_buddie_class("LPOO",3)
        self.assertEqual(student2.buddies,{"LPOO" : [20000001,20000002,20000003]})

        #Remove subject that does not exist
        student2.remove_buddie_class("CAL",3)
        self.assertEqual(student2.buddies,{"LPOO" : [20000001,20000002,20000003]})


    def test_equal_buddies(self):
        studentA = student.Student(200000000, {"LPOO" : 1}, {"LPOO" : [2]}, {"LPOO" : [2]}, {"LPOO" : [201603820]})
        studentB = student.Student(200000000, {"CAL" : 1}, {}, {"LPOO" : [2]}, {"CAL" : [201603820]})
        self.assertEqual(True, studentA == studentB)




if __name__ == '__main__': 
    unittest.main() 

