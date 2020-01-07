"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium navigational commands
"""
import time
from selenium import webdriver


class Navigational:
    def navigational(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome

        driver.get("https://github.com/ColombiaPython/social-media-automation")

        print(driver.title)

        driver.get("https://www.w3schools.com/sql/sql_union.asp")
        time.sleep(5)

        print(driver.title)

        driver.back()
        time.sleep(5)
        print(driver.title)
        driver.forward()
        time.sleep(5)
        print(driver.title)
        driver.quit()


if __name__ == '__main__':
    n = Navigational()
    n.navigational()
