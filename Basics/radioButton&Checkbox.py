"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium Radio Button Action and check box action
"""
from selenium import webdriver


class Radio:
    def radio(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver
        driver.maximize_window()

        driver.get(
            'http://testautomationpractice.blogspot.com/')  # opens the browser with
        # working with Radio buttons
        status = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]').is_displayed()

        print(status)
        status.click()
    
    # working with checkboxes


if __name__ == '__main__':
    r = Radio()
    r.radio()
