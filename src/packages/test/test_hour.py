import unittest

from packages.base.hour import Hour

class Test_Hour(unittest.TestCase): 
    def test_lower(self): 
        # Test by hour
        h1 = Hour(12,10)    
        h2 = Hour(13,10)
        self.assertEqual(True, h1<h2)
        self.assertEqual(False, h2<h1)
        # Test by minutes
        h1 = Hour(12,10)
        h2 = Hour(12, 11)
        self.assertEqual(True,h1<h2)  
        self.assertEqual(False,h2<h1)
        #Test Equals
        h1 = Hour(12,12)
        h2 = Hour(12,12)
        self.assertEqual(False, h1<h2)

    def test_higher(self):
        # Test by hour
        h1 = Hour(12,10)    
        h2 = Hour(13,10)
        self.assertEqual(True, h2>h1)
        self.assertEqual(False, h1>h2)
        # Test by minutes
        h1 = Hour(12,10)
        h2 = Hour(12, 11)
        self.assertEqual(True,h2>h1)  
        self.assertEqual(False,h1>h2)
        #Test Equals
        h1 = Hour(12,12)
        h2 = Hour(12,12)
        self.assertEqual(False, h1>h2)

    def test_equal(self):
        h1 = Hour(12,10)    
        h2 = Hour(13,10)
        h3 = Hour(13,10)
        self.assertFalse(h1 == h2)
        self.assertTrue(h2 == h3)


if __name__ == '__main__': 
    unittest.main() 

