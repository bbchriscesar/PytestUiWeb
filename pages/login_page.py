from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'signInBtn')

    def enter_username(self, username):
        self.send_keys(*self.username_input, username)

    def enter_password(self, password):
        self.send_keys(*self.password_input, password)

    def click_login(self):
        self.click(*self.login_button)