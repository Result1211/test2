from pages.page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):

    @property
    def movie_on(self):
        return self.is_element_visible((By.TAG_NAME, "img"))

    @property
    def movie_off(self):
        return self.is_element_visible((By.TAG_NAME, "img").size == 0)


    @property
    def movie_poster(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href='/movies/1']")