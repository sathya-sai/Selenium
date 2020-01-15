"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium
"""
import HtmlTestRunner
from selenium import webdriver
import time
import unittest
from Sampleproject.POMDemo.Pages.loginPage import LoginPage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/home/admin1/PycharmProjects/Selenium/Drivers/chromedriver.exe")  # opens the chrome driver
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://localhost:8085/login")
        login = LoginPage(driver)
        login.enter_username("raju")
        login.enter_password("654321")
        login.click_login()

        # self.driver.get("http://localhost:8085/login")
        # self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("raju")
        # self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("654321")
        # self.driver.find_element_by_name("Submit").click()
        # assert self.driver.title == "successful"
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/admin1/PycharmProjects/Selenium/Sampleproject/POMDemo/Reports'))
