"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium scrolling button
"""
from selenium import webdriver
import time


class Scrolling:
    def scrolling(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome

        driver.get("https://www.w3schools.com/python/")
        driver.maximize_window()  # maximize the window size
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,1000)","") # it will scroll down by pixel

        # element = driver.find_element_by_xpath('//*[@id="main"]/p[23]/a')  # it will scroll down till the element is found
        # driver.execute_script("arguments[0].scrollIntoView();", element)

        # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # it will scroll down till the end


if __name__ == '__main__':
    s = Scrolling()
    s.scrolling()
