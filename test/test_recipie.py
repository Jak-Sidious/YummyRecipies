'''
This module contains the test cases for the recipie class
'''
import unittest
from app.recipie import Recipie

class Recipes(unittest.TestCase):
    '''class determining all thetest cases for the recipie class'''
    def setUp(self):
        rec = Recipie()
        self.assertIsInstance(rec, object)
