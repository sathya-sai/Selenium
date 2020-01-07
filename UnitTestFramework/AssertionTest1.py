"""
    :Summary This is python 3.7 supported usage of assertEquals, assertNotEquals,

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
        titleOfPage = driver.title

        # assertEquals

        # self.assertEqual("Google",titleOfPage,"web page tittle is not same")
        self.assertNotEqual("Google", titleOfPage)


if __name__ == '__main__':
    unittest.main()
