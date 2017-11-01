'''This module is used mainly to create test cases for the user class'''
import unittest
from app.user import User

class Users(unittest.TestCase):
    '''Class conserning testcases to do with users'''

    def test_user_constructor(self):
        '''Test case to ensure that the test constructor creates an
        object
        '''
        result = User('fname', 'lname')
        self.assertIsInstance(result, object)

if __name__ == '__main__':
    unittest.main()
