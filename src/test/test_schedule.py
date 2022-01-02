import unittest

from src.state.schedule import Schedule
from src.state.hour import Hour

'''
For two given classes, A and B, there are the following possibilities:

A and B happen in different days -- No conflict

A and B happen in the same day.
    A starts before B.
        B starts before A ends.    -- Conflict
        B starts after A ends.     -- No conflict
        B starts when A ends.      -- No conflict

    B starts before A.
        A starts before B ends.    -- Conflict
        A starts after B ends.     -- No conflict
        A starts when B ends.      -- No conflict

    A and B start at the same hour -- Conflict
'''

class TestSchedule(unittest.TestCase):
    def test_conflict_case(self):
        h1 = Hour(10,20)
        h2 = Hour(12,20)
        h3 = Hour(12,21)
        h4 = Hour(12,50)
        day1 = 'Monday'

        s1 = Schedule(h1, h3, day1)
        s2 = Schedule(h2, h4, day1)

        self.assertTrue(s1.conflicts(s2))
        self.assertTrue(s2.conflicts(s1))
        self.assertTrue(s1.conflicts(s1))

    def test_non_conflict(self):
        h1 = Hour(10,20)
        h2 = Hour(12,20)
        h3 = Hour(12,21)
        h4 = Hour(12,50)
        day1 = 'Monday'
        day2 = 'Tuesday'

        s1 = Schedule(h1, h2, day1)
        s2 = Schedule(h2, h4, day1)
        s3 = Schedule(h3, h4, day1)
        s4 = Schedule(h1, h4, day2)
        
        self.assertFalse(s1.conflicts(s2))
        self.assertFalse(s2.conflicts(s1))
        self.assertFalse(s1.conflicts(s3))
        self.assertFalse(s3.conflicts(s1))
        self.assertFalse(s4.conflicts(s1))
        self.assertFalse(s4.conflicts(s2))
        self.assertFalse(s4.conflicts(s2))

if __name__ == '__main__':
    unittest.main() 
