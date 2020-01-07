"""
    :Summary This is python 3.7 supported usage of assertIn, assertNotIn,

    :Since January 2020

    :Author Sathya Sai M

    :keyword Python, Selenium, Unittesting

"""
import unittest


class Test(unittest.TestCase):
    def testName(self):
        list = ("python", "selenium", "java")

        # self.assertIn("python", list)  # Pass
        # self.assertIn("rubby", list)  # fail
        #
        # self.assertNotIn("python", list)  # fail
        self.assertNotIn("rubby", list)  # pass


if __name__ == '__main__':
    unittest.main()
