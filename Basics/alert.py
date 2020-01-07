"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium with popup handling
"""
from selenium import webdriver
import time


class Alert:
    def alert(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        # driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe") # to open the fire fox driver

        driver.get(
            'http://testautomationpractice.blogspot.com/')  # opens the browser with
        driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

        driver.switch_to_alert().accept()  # closes alert window choosing ok button
        # driver.switch_to_alert().dismiss()  # closes alert window choosing cancel button
        time.sleep(5)


if __name__ == '__main__':
    p = Alert()
    p.alert()
