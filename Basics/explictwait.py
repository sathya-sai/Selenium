"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium explicit wait
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Explicitwait:

    def explicit_wait(self):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")

        driver.implicitly_wait(5)
        driver.maximize_window()  # this will maximize the window

        driver.get(
            "https://www.expedia.co.in/?semcid=IN.B.GOOGLE.BT-c-EN.GENERIC&semdtl=a1764777706.b142991159889.r1.g1kwd-7017167707.i1.d1204428726302.e1c.j19062279.k1.f11t1.n1.l1g.h1e.m1&gclid=CjwKCAiAuqHwBRAQEiwAD-zr3UOdwGZsEdS2GpTI-A8Nucrk-Hhu9rOogVFCdJBQ-r7qAUILgLF5tBoC3U8QAvD_BwE")
        print(driver.title)
        driver.find_element_by_xpath(
            '//*[@id="tab-flight-tab-hp"]/span[1]/span').click()  # will clicks on the flight button
        # driver.find_element(By.xpath,'//*[@id="tab-flight-tab-hp"]/span[1]/span').click() # this approach also can be used
        driver.find_element_by_id("flight-origin-hp-flight").clear()
        driver.find_element_by_id("flight-origin-hp-flight").send_keys("Mumbai")  # origin
        time.sleep(2)  # python code
        driver.find_element_by_id("flight-destination-hp-flight").clear()
        driver.find_element_by_id("flight-destination-hp-flight").send_keys(
            "Bengaluru, India (BLR-Kempegowda Intl.)")  # destination

        driver.find_element_by_id("flight-departing-hp-flight").clear()  # it will clear the fields present
        driver.find_element_by_id("flight-departing-hp-flight").send_keys("01/02/2020")  # departing date

        driver.find_element_by_id("flight-returning-hp-flight")  # it will clear the fields present
        driver.find_element_by_id("flight-returning-hp-flight").send_keys("05/02/2020")  # Returning date

        driver.find_element_by_xpath('//*[@id="gcw-flights-form-hp-flight"]/div[8]/label/button').click()

        # Explicit Wait statements
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stopFilter_stops-0"]')))
        element.click()
        time.sleep(5)
        driver.quit()


if __name__ == '__main__':
    e = Explicitwait()
    e.explicit_wait()
