class LoginPage():
    # locators of all the elements
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = '/html/body/form/table/tbody/tr[3]/td[1]/input'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

