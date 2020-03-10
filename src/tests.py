import unittest
import hour

#class Test_StudentGenerator(unittest.TestCase): 


# class Test_State(unittest.TestCase): 


# class Test_MainCycle(unittest.TestCase): 

# class Test_Schedule(unittest.TestCase):
  
class Test_Hour(unittest.TestCase): 
    def test_lower(self): 
        # Test by hour
        h1 = hour.Hour(12,10)    
        h2 = hour.Hour(13,10)
        self.assertEqual(True, h1<h2)
        self.assertEqual(False, h2<h1)
        # Test by minutes
        h1 = hour.Hour(12,10)
        h2 = hour.Hour(12, 11)
        self.assertEqual(True,h1<h2)  
        self.assertEqual(False,h2<h1)
        #Test Equals
        h1 = hour.Hour(12,12)
        h2 = hour.Hour(12,12)
        self.assertEqual(False, h1<h2)
        
    def test_higher(self):
        # Test by hour
        h1 = hour.Hour(12,10)    
        h2 = hour.Hour(13,10)
        self.assertEqual(True, h2>h1)
        self.assertEqual(False, h1>h2)
        # Test by minutes
        h1 = hour.Hour(12,10)
        h2 = hour.Hour(12, 11)
        self.assertEqual(True,h2>h1)  
        self.assertEqual(False,h1>h2)
        #Test Equals
        h1 = hour.Hour(12,12)
        h2 = hour.Hour(12,12)
        self.assertEqual(False, h1>h2)


if __name__ == '__main__': 
    unittest.main() 

