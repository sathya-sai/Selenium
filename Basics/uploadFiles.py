"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium  to upload files
"""
from selenium import webdriver
import time


class Upload:
    def upload(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver
        driver.maximize_window()

        driver.get(
            'http://testautomationpractice.blogspot.com/')  # opens the browser with
        driver.switch_to_frame(0)
        driver.find_element_by_id("RESULT_FileUpload-10").send_keys("/home/admin1/Documents/solution1-en.png")
        time.sleep(5)


if __name__ == '__main__':
    u = Upload()
    u.upload()
