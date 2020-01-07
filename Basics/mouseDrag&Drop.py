"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium Mouse Drag and Drop Action
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class Drag_Drop:
    def drag_drop(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver
        driver.maximize_window()

        driver.get(
            'http://testautomationpractice.blogspot.com/')  # opens the browser with
        source_element = driver.find_element_by_xpath('//*[@id="draggable"]/p')
        target_element = driver.find_element_by_id('droppable')

        action = ActionChains(driver)

        action.drag_and_drop(source_element, target_element).perform()  # this performs drag and drop operation
        time.sleep(3)


if __name__ == '__main__':
    d = Drag_Drop()
    d.drag_drop()
