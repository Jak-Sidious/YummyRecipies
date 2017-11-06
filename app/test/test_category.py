''' this module contains the test case for the category class
'''
import unittest
from models.category import Category

class Categories(unittest.TestCase):
    '''Class destermining the testcase for the category class
    '''

    def test_category_is_instance(self):
        ''' test to ensure that the category constructor returns an
            instance of the class
        '''
        tester = Category('category_name', 'category_description')
        self.assertIsInstance(tester, object)