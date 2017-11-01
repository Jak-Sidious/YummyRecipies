class User(object):
    '''This class determines the user object to be used in the application'''
    def __init__(self, firstname="", lastname="", age=0, gender=""):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
