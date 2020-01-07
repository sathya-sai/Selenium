"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium basics commands
"""
import time
from selenium import webdriver


class Basic:

    def basic(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        # driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

        driver.get(
            "https://www.youtube.com/watch?v=NYA7AVdD4hA&list=PLUDwpEzHYYLvx6SuogA7Zhb_hZl3sln66&index=3")  # opens the browser with that link
        driver.maximize_window()  # to maximize the window
        print(driver.title)  # title of the page

        print(driver.current_url)  # displays the current url

        driver.find_element_by_xpath('//*[@id="img"]').click()  # xpath of that particular button

        time.sleep(5)  # waits for 5 seconds

        driver.close()  # closes the currently focused browser

        driver.quit()  # closes all the browsers


if __name__ == '__main__':
    b = Basic()
    b.basic()
