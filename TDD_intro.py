# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on

def reverseList(_list):
    start = 0
    end =(len(_list))
    while(start<end):
        _list[start],_list[end] = _list[end],_list[start]
    return reverseList
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class IsEvenTests(unittest.TestCase):
    def reverseTest1(self):
        self.assertEqual(reverseList([1,3,5]),[5,3,1])
    def reverseTest2(self):
        self.assertEqual(reverseList([9,6,3,1,2]),[2,3,6,9])
    # # each method in this class is a test to be run

    # def testTwo(self):
    #     self.assertEqual(isEven(2), True)
    #     # another way to write above is
    #     self.assertTrue(isEven(2))
    # def testThree(self):
    #     self.assertEqual(isEven(3), False)
    #     # another way to write above is
    #     self.assertFalse(isEven(3))
    # # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests
