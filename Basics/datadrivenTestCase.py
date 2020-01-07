"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium data driven for login
"""

from Basics import datadrivenutill
from selenium import webdriver


class DataDriven:
    def datadriven(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        driver.get(
            "http://localhost:8085/login")  # opens the browser with that link
        driver.maximize_window()  # maximises the window

        path = "/home/admin1/Downloads/DataDriven.xlsx"  # path of the xlse file

        rows = datadrivenutill.getRowCount(path, "login")  # from datadrivenutill
        for r in range(2, rows + 1):
            username = datadrivenutill.readData(path, "login", r, 1)
            password = datadrivenutill.readData(path, "login", r, 2)

            driver.find_element_by_id("username").send_keys(username)
            driver.find_element_by_id("password").send_keys(password)
            driver.find_element_by_name("Submit").click()

            if driver.title == "successful":
                print("test is passed")
                datadrivenutill.writeData(path, "login", r, 3, "test passed")

            else:
                print("test is failed")
                datadrivenutill.writeData(path, "login", r, 3, "test failed")
            driver.get("http://localhost:8085/login")


if __name__ == '__main__':
    d = DataDriven()
    d.datadriven()
