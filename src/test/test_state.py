import unittest
from src.state.state import State
from src.state.student import Student


class TestState(unittest.TestCase):
    def test_add_student(self):
        state = State()
        student = Student(123, {}, {}, {}, {})
        state.add_student(student)
        self.assertEqual(state.student_num, 1)
        self.assertTrue(123 in state.students)
        stored_student = state.students[123]
        self.assertEqual(stored_student, student)

    def test_get_score(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
