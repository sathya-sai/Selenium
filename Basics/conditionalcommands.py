"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium basics conditionalcommands
"""
import time
from selenium import webdriver


class Conditional:

    def conditional(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver
        driver.get("http://localhost:8085/register")  # opens the link
        email = driver.find_element_by_name("email_id")
        print(email.is_displayed())
        print(email.is_enabled())
        user = driver.find_element_by_name("username")
        print(user.is_displayed())
        print(user.is_enabled())
        passw = driver.find_element_by_name("password")
        print(passw.is_displayed())
        print(passw.is_enabled())

        email.send_keys("prem@gmail.com")

        time.sleep(2)
        user.send_keys("prem")
        time.sleep(2)
        passw.send_keys("12345")
        time.sleep(2)
        driver.find_element_by_name("Submit").click()
        time.sleep(2)

        driver.get("http://localhost:8085/login")

        user = driver.find_element_by_name("username")
        user.send_keys("prem")
        time.sleep(2)

        passw = driver.find_element_by_name("password")
        passw.send_keys("12")
        time.sleep(2)

        driver.find_element_by_name("Submit").click()
        time.sleep(2)
        driver.quit()


if __name__ == '__main__':
    c = Conditional()
    c.conditional()
