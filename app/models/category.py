'''this Module contains the Category class'''

class Category(object):
    '''Class contains the various food categories that the various
    foods can be broadly classified into'''

    def __init__(self, category_name, description):
        self.category_name = category_name
        self.description = description
        self.recipes = {}
        