import unittest


class SignupTest(unittest.TestCase):

    def test_signupbyEmail(self):
        print("This is signup by Email Test")
        self.assertTrue(True)

    def test_signupbyFacebook(self):
        print("This is signup by Facebook Test")
        self.assertTrue(True)

    def test_signupbyTwitter(self):
        print("This is signup by Twitter Test")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
