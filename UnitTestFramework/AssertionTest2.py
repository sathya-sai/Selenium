"""
    :Summary This is python 3.7 supported usage of assertTrue, assertFalse,

    :Since January 2020

    :Author Sathya Sai M

    :keyword Python, Selenium, Unittesting

"""
import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        driver.get("https://www.google.com/")
        tittleOFPAge = driver.title
        # self.assertTrue(tittleOFPAge == "Google")  # True
        self.assertFalse(tittleOFPAge == "Google")  # False


if __name__ == '__main__':
    unittest.main()
