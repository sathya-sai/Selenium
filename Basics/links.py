"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium basics for links
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class Links:
    def links(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome

        driver.get("https://selenium-python.readthedocs.io/")

        links = driver.find_elements(By.TAG_NAME, "a")  # identifies all rhe tags present in the same page
        print(len(links))  # prints the links present in the page

        for link in links:
            print(link.text)

        # clicking on the link
        driver.find_element(By.LINK_TEXT, "Explicit Waits").click()


if __name__ == '__main__':
    l = Links()
    l.links()
