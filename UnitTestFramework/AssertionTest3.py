"""
    :Summary This is python 3.7 supported usage of assertIsNone, assertIsNotNone,

    :Since January 2020

    :Author Sathya Sai M

    :keyword Python, Selenium, Unittesting

"""
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        self.assertIsNone(driver)  # False
        # self.assertIsNotNone(driver) #True


if __name__ == '__main__':
    unittest.main()
