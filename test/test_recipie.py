'''
This module contains the test cases for the recipie class
'''
import unittest
from app.models.recipie import Recipe


class Recipes(unittest.TestCase):
    '''class determining all the test cases for the recipie class'''


    def test_recipie_is_instance(self):
        '''Test case to ensure that the test constructor creates an
        object
        '''
        result = Recipe('Recipie name', 'Your instructions here')
        self.assertIsInstance(result, object)

if __name__ == '__main__':
    unittest.main()
