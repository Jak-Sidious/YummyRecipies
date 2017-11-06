'''This class deffines the recipie module'''
class Recipie(object):
    '''The classs determining the recipies'''
    def __init__(self):
        self.recipies = {}

    def create_recipie(self, name, preparation=""" """):
        '''this metthod allows for the creation of recipies'''

        if name not in self.recipies.keys():
            preparation = preparation.split("\r\n")
            self.recipies[name] = preparation
        else:
            return "Recipie already exists"
        return self.recipies

    def browse(self, name):
        '''
        enables a user to view a food recipe
        '''
        if name in self.recipies.keys():
            return self.recipies[name]
        else:
            return 'Not Available'

    def modifyitems(self, name, new_name):
        '''
        changing the recipie items
        '''
        if name in self.recipies.keys():
            self.recipies[new_name] = self.recipies[name]
            del self.recipies[name]
        else:
            return self.recipies
    
    def delete(self, name):
        '''method to delete items'''
        if name in self.recipies.keys():
            del self.recipies[name]
        else:
            return "Invalid Request"
        return self.recipies

