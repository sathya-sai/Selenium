"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium
"""
from Sampleproject.POMDemo.Locators.locators import Locators


class LoginPage:
    # create a constructor
    def __init__(self, driver):
        self.driver = driver

        # self.username_text_box_xpath = '//*[@id="username"]'
        # self.password_text_box_xpath = '//*[@id="password"]'
        # self.login_button_name = 'Submit'
        self.username_text_box_xpath = Locators.username_text_box_xpath
        self.password_text_box_xpath = Locators.password_text_box_xpath
        self.login_button_name = Locators.login_button_name

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_text_box_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_text_box_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()
