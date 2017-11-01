'''This module defines the user class'''
class User(object):
    '''This class determines the user object to be used in the application'''
    def __init__(self, username, password):
        self.username = username
        self.password = password
