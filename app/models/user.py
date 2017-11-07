'''This module defines the user class'''

from models.category import Category
from models.recipie import Recipe


class User(object):
    '''This class determines the user object to be used in the application'''
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.categories = {}

    def categorycreate(self, name, description):
        '''Creates the category and provides for the description for said
           created category
        '''
        if description not in self.categories:
            newest = Category(name, description)
            self.categories[name] = newest
            return self.categories
        return "Why like dis!!!! This category exists already"

    def view_categories(self, name):
        '''Method to view categories'''
        return self.categories[name]

    def edit_category(self, category_name, description=None):
        '''Edit a category'''
        if description is None:
            description = 'N/a'
        update = Category(category_name, description)
        self.categories[category_name] = update
        return self.categories

    def delete_category(self, category_name):
        ''' Delete a particular category '''
        del self.categories[category_name]
        return self.categories


