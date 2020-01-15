"""
    :summary This is python 3.7 supported selenium 3.141.0 and Allure

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium for Allure Report generation, Decorators and Screen-Shots,
"""
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import time
import allure


@allure.severity(allure.severity_level.NORMAL)
class TestMyProject:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(
            executable_path="/home/admin1/PycharmProjects/Selenium/Drivers/chromedriver.exe")  # opens the chrome driver
        self.driver.maximize_window()
        yield
        self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_homePageTitle(self, setup):
        self.driver.get("http://localhost:8085/login")
        assert self.driver.title == "Login Form"
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self, setup):
        self.driver.get("http://localhost:8085/login")
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("raju")
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("654321")
        self.driver.find_element_by_name("Submit").click()
        act_title = self.driver.title
        if act_title == 'successfull':
            assert True
        else:
            # to take the screen shot by giving 3 parameters
            allure.attach(self.driver.get_screenshot_as_png(), name='testLoginScreen',
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_regisration(self, setup):
        self.driver.get("http://localhost:8085/login")
        self.driver.find_element_by_xpath('//*[@id="Registration"]').click()
        self.driver.find_element_by_id("email_id").send_keys("ra@gmail.com")
        self.driver.find_element_by_name("username").send_keys("prem")
        self.driver.find_element_by_name("password").send_keys("12345")
        self.driver.find_element_by_name("Submit").click()
        assert self.driver.title == "SUCESS MESSAGE"
# to execute: pytest -v -s --alluredir="/home/admin1/PycharmProjects/Selenium/AllureReport/report" AllureReport/test_allure.py
#  allure serve /home/admin1/PycharmProjects/Selenium/AllureReport/report
# to share:netlify.com
