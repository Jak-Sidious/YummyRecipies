'''This module defines the user class'''
class User(object):
    '''This class determines the user object to be used in the application'''
    def __init__(self, username, password):
        self.username = username
        self.password = password

    #this should be one of the tests
    def signin(self, uname, pword):
        '''Method to determine if the username is correct or not'''
        text1 = "You have succesfully entered your username and password"
        text2 = "please enter the correct username and/or password"
        if uname == self.username and pword == self.password:
            return text1
        else:
            return text2
