from pages.page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    #@property
    #def _field(self):
    #   return self.driver.find_element_by_CSS_SELECTOR("a[href='/cart']")

    @property
    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/users/login']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "a[href='/users/login']"))

    @property
    def register_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/users/register']")