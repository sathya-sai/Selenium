"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium Mouse Double click Action
"""
from selenium import webdriver
import time
from selenium.webdriver import ActionChains


class DoubleClick:
    def doubleClick(self):

        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver
        driver.maximize_window()

        driver.get('http://testautomationpractice.blogspot.com/')  # opens the browser with
        element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')

        actions = ActionChains(driver)

        actions.double_click(element).perform()  # this will perform double click on the button
        time.sleep(5)


if __name__ == '__main__':
    d = DoubleClick()
    d.doubleClick()
