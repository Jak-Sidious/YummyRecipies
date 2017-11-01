'''This module defines the user class'''
class User(object):
    '''This class determines the user object to be used in the application'''
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # def getuser(self):
    #     '''Method to display the user name'''
    #     return self.username

    # def getpassword(self):
    #     '''method to return the user's password'''
    #     return self.password
