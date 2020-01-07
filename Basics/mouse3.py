"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium Mouse Right click Action
"""
from selenium import webdriver
from selenium.webdriver import ActionChains


class RightClick:
    def rightClick(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver
        driver.maximize_window()

        driver.get(
            'http://testautomationpractice.blogspot.com/')  # opens the browser with
        button = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-9"]')
        action = ActionChains(driver)
        action.context_click(button).perform()  # Mouse Right click action


if __name__ == '__main__':
    r = RightClick()
    r.rightClick()
