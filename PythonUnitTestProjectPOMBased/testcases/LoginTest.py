import time
import unittest
import HtmlTestRunner

import sys

from selenium import webdriver

from PythonUnitTestProjectPOMBased.pageObject.loginPage import LoginPage

sys.path.append("/home/admin1/Pycharm Projects/Selenium/PythonUnitTestProjectPOMBased")


class LoginTest(unittest.TestCase):
    baseURL = "http://localhost:8085/login"
    username = "Ramu"
    password = "1234"
    driver = webdriver.Chrome(executable_path="/home/admin1/PycharmProjects/Selenium/Drivers/chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("successful", self.driver.title, "webpage tittle is not correct")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='/home/admin1/PycharmProjects/Selenium/PythonUnitTestProjectPOMBased/reports'))
