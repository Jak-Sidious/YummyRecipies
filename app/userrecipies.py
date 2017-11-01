'''
Module which implements the class UserRecipies
'''

from user import User
from recipie import Recipie

class UserRecipie(User, Recipie):
    def__init__(self, username, password, recipiename, ingridents=None, procdeure=None):
        User.__init__(self, username, password)
        Recipie.__init__(self, recipiename, ingridents, procdeure)