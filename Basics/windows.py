"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium to find main window
"""
from selenium import webdriver


class Window:
    def window(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")  # opens the chrome

        driver.get("https://www.w3schools.com/python/")
        driver.find_element_by_xpath('//*[@id="main"]/div[4]/a').click()

        print(driver.current_window_handle)  # prints the value of the parent window

        handles = driver.window_handles  # returns all the values of the open windows
        for value in handles:
            driver.switch_to.window(value)
            print(driver.title)
            if driver.title == "Python Tutorial":
                driver.close()  # it closes the parent window

        driver.quit()


if __name__ == '__main__':
    w = Window()
    w.window()
