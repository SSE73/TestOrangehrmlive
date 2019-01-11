from OrangehrmliveProjects.POMProject.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_text_box_id = Locators.username_text_box_id
        self.password_text_box_id = Locators.password_text_box_id
        self.login_button_id      = Locators.login_button_id

    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.username_text_box_id).clear()
        self.driver.find_element_by_id(Locators.username_text_box_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.password_text_box_id).clear()
        self.driver.find_element_by_id(Locators.password_text_box_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(Locators.login_button_id).click()
