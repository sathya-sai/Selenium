import unittest


class LoginTest(unittest.TestCase):

    def test_loginbyEmail(self):
        print("This is login by Email Test")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("This is login by Facebook Test")
        self.assertTrue(True)

    def test_loginbyTwitter(self):
        print("This is login by Twitter Test")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
