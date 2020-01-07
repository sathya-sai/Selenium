"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium Implicit wait
"""
from selenium import webdriver


class ImplicitWait:
    def implicit_wait(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome driver

        # driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

        driver.get("http://localhost:8085/register")  # opens the browser with that link
        driver.implicitly_wait(10)

        assert "registration form" in driver.title
        driver.find_element_by_name("email_id").send_keys("rahulo@gmail.com")
        driver.find_element_by_name("username").send_keys("rahul")
        driver.find_element_by_name("password").send_keys("sathya1234")
        driver.find_element_by_name("Submit").click()
        driver.quit()


if __name__ == '__main__':
    i = ImplicitWait()
    i.implicit_wait()
