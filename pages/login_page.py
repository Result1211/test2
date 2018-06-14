from pages.page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):

    @property
    def user_email_field(self):
        return self.driver.find_element_by_id("user_email")

    @property
    def user_password_field(self):
        return self.driver.find_element_by_id("user_password")

    @property
    def submit_button(self):
        return self.driver.find_element_by_name("commit")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "a[href='/user/login']"))