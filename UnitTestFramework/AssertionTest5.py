"""
    :Summary This is python 3.7 supported usage of assertGreater, assertGreaterEqual, assertLess, assertLessEqual
 
    :Since January 2020

    :Author Sathya Sai M

    :keyword Python, Selenium, Unittesting

"""
import unittest


class Test(unittest.TestCase):
    def testName(self):
        # self.assertGreater(100, 10)  # assertGreater
        # self.assertGreaterEqual(100, 100)  # assertgreaterEqual

        # self.assertLess(10, 100)  # assert less
        self.assertLessEqual(10, 100)  # assert less equals true


if __name__ == '__main__':
    unittest.main()
