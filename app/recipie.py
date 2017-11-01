'''This class deffines the recipie module'''
class Recipie(object):
    '''The classs determining the recipies'''
    def __init__(self, recipiename, ingridents=None, procdeure=None):
        self.name = recipiename
        if ingridents is None:
            self.ingridents = []
        else:
            self.ingridents = ingridents
        if procdeure is None:
            self.procdeure = []
        else:
            self.procdeure = procdeure