from pages.page import Page
from selenium.webdriver.common.by import By


class RegisterPage(Page):

    @property
    def user_email_field(self):
        return self.driver.find_element_by_id("user_email")

    @property
    def user_password_field(self):
        return self.driver.find_element_by_id("user_password")

    @property
    def user_password_confirmation_field(self):
        return self.driver.find_element_by_id("user_password_confirmation")

    @property
    def submit_button(self):
        return self.driver.find_element_by_name("commit")
