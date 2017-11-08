'''This module defines the user class'''

from app.models.category import Category
from app.models.recipie import Recipe


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

    def create_recipe(self, category_name, recipe_name, ingridents):
        '''Creates a recipie that corresponds to a particular category'''
        categori = self.categories[category_name]
        new_recipie = Recipe(recipe_name, ingridents)
        categori.recipes[recipe_name] = new_recipie
        return categori.recipes

    def view_recipies(self, category_name):
        '''creates listing of all recipies'''
        all_recipies = self.categories[category_name].recipes
        the_recipe = list(all_recipies.values())
        return the_recipe

    def view_recipe(self, category_name, recipe_name):
        '''View a particular recipie'''
        the_recipes = self.categories[category_name].recipes
        print (the_recipes)

        if recipe_name in the_recipes:
            return the_recipes[recipe_name].recipe_name
        return 'That recipie name aint here fam'

    def edit_recipe(self, category_name, recipe_name, ingredients=None):
        '''Edits a recipie'''
        the_recipes = self.categories[category_name].recipes
        if recipe_name in the_recipes:
            if ingredients is None:
                ingredients = 'Please enter some Ingredients for the recipe'
            update = Recipe(recipe_name, ingredients)
            the_recipes[recipe_name] = update
            return the_recipes
        return 'The Recipie doesnt exist'

    def delete_recipie(self, category_name, recipe_name):
        '''Deletes a reccipie'''
        del self.categories[category_name].recipes[recipe_name]
        return self.categories[category_name].recipes
