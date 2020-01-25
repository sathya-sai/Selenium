"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium keyboard operations
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Keyboard:
    def keyboard(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver
        driver.maximize_window()

        driver.get(
            'https://www.goibibo.com/flights/flights-from-mumbai/?utm_source=google&utm_medium=cpc&utm_campaign=DF-Generic-Overall-Mumbai-DT&utm_content=Book%20Flight%20Tickets&gclid=CjwKCAiAmNbwBRBOEiwAqcwwpeMi_-u8_amooZ5iWrkS7ErpwzMuPYbYNgf2f4ob1N5d9SJPFy43nRoC80YQAvD_BwE')  # opens the browser with
        driver.find_element_by_id("gi_source_st").clear()
        driver.find_element_by_id("gi_source_st").send_keys("sathya")

        # to perform TAB operation
        act = ActionChains(driver)
        act.send_keys(Keys.TAB).perform()

        # to perform Control operation
        # act = ActionChains(driver)
        # act.send_keys(Keys.CONTROL).send_keys("a").perform()
        time.sleep(5)
        driver.quit()


if __name__ == '__main__':
    k = Keyboard()
    k.keyboard()
