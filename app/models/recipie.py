'''This class deffines the recipie module'''
class Recipe(object):
    '''The classs determining the recipies'''
    def __init__(self, recipie_name, ingridents):
        self.recipie_name = recipie_name
        self.ingridents = ingridents
