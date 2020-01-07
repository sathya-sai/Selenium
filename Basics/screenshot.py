"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium to take screen shot
"""
from selenium import webdriver


class Screenshot:
    def screenshot(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        # driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

        driver.get("https://www.amazon.in/")
        # driver.save_screenshot("/home/admin1/Downloads/screen.png") # captures the screenshot and capture in that path

        driver.get_screenshot_as_file("/home/admin1/Downloads/screen1.png")


if __name__ == '__main__':
    s = Screenshot()
    s.screenshot()
