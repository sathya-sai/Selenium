"""
    :Summary This is python 3.7 supported usage of skipping of test cases,

    :Since January 2020

    :Author Sathya Sai M

    :keyword Python, Selenium, Unittesting

"""
import unittest


class AppTest(unittest.TestCase):

    @unittest.SkipTest  # by decorator
    def test_firstTest(self):
        print("This is my first unittest")

    @unittest.skip("reason")  # Skip test with reason
    def test_secondTest(self):
        print("This is my second unittest")

    @unittest.skipIf(1 == 1, "reason")  # skip test based on condition
    def test_thirdTest(self):
        print("This is my third unittest")

    def test_forthTest(self):
        print("This is my forth unittest")

    def test_fifthTest(self):
        print("This is my fifth unittest")

    def test_sixthTest(self):
        print("This is my sixth unittest")


if __name__ == '__main__':
    unittest.main()
