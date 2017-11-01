import unittest

class CreateUser(unittest.TestCase):

    def test_user_adds_user(self):
        use = User()
        result = User.CreateUser('fname','lname',12,'m')
        self.assertIsInstance(result, object)

if __name__ == '__main__':
    unittest.main()