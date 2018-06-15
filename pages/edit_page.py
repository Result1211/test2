from pages.page import Page
from selenium.webdriver.common.by import By


class EditPage(Page):

    @property
    def submit_button(self):
        return self.driver.find_element(By.XPATH, "//input[@value='Cancel my account']")




