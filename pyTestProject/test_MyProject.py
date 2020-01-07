"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium
"""
from selenium import webdriver
import pytest
import time


class TestMyProject:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(
            executable_path="/home/admin1/PycharmProjects/Selenium/Drivers/chromedriver.exe")  # opens the chrome driver
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self, setup):
        self.driver.get("http://localhost:8085/login")
        assert self.driver.title == "Login Form"
        time.sleep(5)

    def test_login(self, setup):
        self.driver.get("http://localhost:8085/login")
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("raju")
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("654321")
        self.driver.find_element_by_name("Submit").click()
        assert self.driver.title == "successful"
        time.sleep(5)

    def test_regisration(self,setup):
        self.driver.get("http://localhost:8085/login")
        self.driver.find_element_by_xpath('//*[@id="Registration"]').click()
        self.driver.find_element_by_id("email_id").send_keys("rama@gmail.com")
        self.driver.find_element_by_name("username").send_keys("prem")
        self.driver.find_element_by_name("password").send_keys("12345")
        self.driver.find_element_by_name("Submit").click()
        assert self.driver.title == "SUCESS MESSAGE"
# ToRun:pytest -v -s --html=report.html --self-contained-html pyTestProject/test_MyProject.py
