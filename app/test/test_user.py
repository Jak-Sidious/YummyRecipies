'''This module is used mainly to create test cases for the user class'''
import unittest
from models.user import User

class Users(unittest.TestCase):
    '''Class conserning testcases to do with users'''

    def setUp(self):
        self.userr = User('fname', 'lname')
        self.categoriz = self.userr.categories

    def test_user_instance(self):
        '''Test case to ensure that the test constructor creates an
        object
        '''
        self.assertIsInstance(self.userr, User)

    def test_user_category_is_created(self):
        '''Test if the category is created
        '''
        self.userr.categorycreate('name of category', 'description of category')
        self.assertIn('name of category', self.userr.categories)

    def test_category_is_viewable(self):
        '''Test whether or not a category can be viewed'''
        self.userr.categorycreate('name of category', 'description of category')
        view = self.userr.view_categories('name of category')
        self.assertEqual('name of category', view.category_name)

    def test_if_category_is_editable(self):
        '''Test whether or not a category can be edited'''
        self.userr.categorycreate('name of category', 'description of category')
        edit = self.userr.edit_category('name of category', 'descrip')
        self.assertEqual('descrip', self.categoriz['name of category'].description)
    
    def test_if_category_is_deleted(self):
        ''' test whether a category gets deleted'''
        self.userr.categorycreate('name of category', 'description of category')
        delete = self.userr.delete_category('name of category')
        self.assertNotIn('name of category', self.categoriz)
