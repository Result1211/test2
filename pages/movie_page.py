from pages.page import Page
from selenium.webdriver.common.by import By


class MoviePage(Page):

    @property
    def submit_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[class='button']")