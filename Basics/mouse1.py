"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium Mouse Hover Action
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class Mouse:
    def mouse(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver
        driver.maximize_window()

        driver.get(
            'https://www.goindigo.in/aff.html?cid=Display|Affiliate|Icubes|825_{aff_sub')  # opens the browser with
        book = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[1]/a')
        bookflight = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[1]/div/div/div[1]/a/h6')

        action = ActionChains(driver)
        action.move_to_element(book).move_to_element(bookflight).click().perform()
        time.sleep(5)


if __name__ == '__main__':
    m = Mouse()
    m.mouse()
