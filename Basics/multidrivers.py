"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium drivers
"""
from selenium import webdriver


class Driver:
    def driver(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        # driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

        driver.get("https://www.youtube.com")  # opens the browser with that link

        print(driver.title)  # title of the page

        driver.close()  # it will close the browser


if __name__ == '__main__':
    d = Driver()
    d.driver()
