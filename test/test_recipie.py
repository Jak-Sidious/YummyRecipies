'''
This module contains the test cases for the recipie class
'''
import unittest
from app.recipie import Recipie

class Recipes(unittest.TestCase):
    '''class determining all thetest cases for the recipie class'''
    def testconstructor(self):
        '''Test case to ensure that the test constructor creates an
        object
        '''
        result = Recipie()
        self.assertIsInstance(result, object)

