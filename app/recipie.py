'''This class deffines the recipie module'''
class Recipie(object):
    '''The classs determining the recipies'''
    def __init__(self, recipiename):
        self.name = recipiename
        self.ingridents = []
        self.procdeure = []

    def add_ingrident(self, ingrid):
        '''Method to add iningredients to a recipie'''
        self.ingridents.append(ingrid)

    def add_procedure(self, proc):
        '''Method to add procedure to recipie'''
        self.procdeure.append(proc)
