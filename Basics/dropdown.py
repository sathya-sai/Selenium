"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium Drop Down by visible text, index, value
    and count and capture all the options from the drop down
"""
from selenium import webdriver

from selenium.webdriver.support.ui import Select


class Dropdown:
    def dropdown(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        driver.get("http://testautomationpractice.blogspot.com/")
        element = driver.find_element_by_xpath('//*[@id="files"]')
        drp = Select(element)

        # select by visible text
        # drp.select_by_visible_text('Faster')

        # select by index (index start with 0)
        # drp.select_by_index(0)

        # select by value
        # drp.select_by_value("Radi0-2")

        # count the number of options
        print(len(drp.options))

        # capture all the options and print them
        all_opt = drp.options
        for option in all_opt:
            print(option.text)


if __name__ == '__main__':
    d = Dropdown()
    d.dropdown()
