"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium with cookies
"""
from selenium import webdriver


class Cookies:

    def capturingCookies(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        # driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

        driver.get("https://www.amazon.in/")
        # capturing all the cookies captured by the browser
        cookies = driver.get_cookies()
        print(len(cookies))  # print the number of cookies nave been created
        print(cookies)  # print all the cookie pairs

    def addCookies(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        # driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

        driver.get("https://www.amazon.in/")
        # adding new cookie to the browser
        cookie = {'name': 'Mycookie', 'value': '123454'}
        driver.add_cookie(cookie)
        cookies = driver.get_cookies()
        print(len(cookies))  # print the number of cookies nave been created
        print(cookies)  # print all the cookie pairs

    def deleteCookies(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        # driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

        driver.get("https://www.amazon.in/")
        # deleting the cookie
        driver.delete_cookie("Mycookie")
        cookies = driver.get_cookies()
        print(len(cookies))  # print the number of cookies nave been created
        print(cookies)  # print all the cookie pairs

    def deleteAllCookies(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        # driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

        driver.get("https://www.amazon.in/")
        # deleting all the cookies from the browser
        driver.delete_all_cookies()  # delete all the cookies
        cookies = driver.get_cookies()
        print(len(cookies))  # print the number of cookies nave been created
        print(cookies)  # print all the cookie pairs


if __name__ == '__main__':
    c = Cookies()
    c.capturingCookies()
