# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from pages.login_page import LoginPage
from pages.internal_page import InternalPage
from pages.main_page import MainPage
from pdb import set_trace as bp


class Application(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        driver.get(base_url)
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.main_page = MainPage(driver, base_url)
        self.wait = WebDriverWait(driver, 10)

    #def go_to_home_page(self):
     #   self.driver.get(self.base_url)

    def logout(self):
        self.internal_page.logout_button.click()
        #self.driver.find_element_by_CSS_SELECTOR("a[href='/users/logout']").click()

    def login(self, user):
        self.main_page.login_button.click()
        lp = self.login_page
        lp.user_email_field.clear()
        lp.user_email_field.send_keys (user.user_email)
        lp.user_password_field.clear()
        lp.user_password_field.send_keys(user.user_password)
        lp.submit_button.click()

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_not_logged_in(self):
        return self.main_page.is_this_page

    def is_not_logged(self):
        return self.login_page.is_this_page