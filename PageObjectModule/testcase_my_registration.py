"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium page object Module
"""
from selenium import webdriver
import unittest
import HtmlTestRunner

class MyAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        cls.driver.maximize_window()

    def test_homepagetitle(self):
        self.driver.get("http://localhost:8085/register")
        self.assertEqual("registration form", self.driver.title, "webpage is not matching")

    def test_register(self):
        self.driver.get("http://localhost:8085/register")
        self.driver.find_element_by_name("email_id").send_keys("rahulo@gmail.com")
        self.driver.find_element_by_name("username").send_keys("rahul")
        self.driver.find_element_by_name("password").send_keys("sa234")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("SUCESS MESSAGE", self.driver.title, "webpage is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='/home/admin1/PycharmProjects/Selenium/PageObjectModule/Reports'))
