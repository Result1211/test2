# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, alert_is_present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from pages.login_page import LoginPage
from pages.internal_page import InternalPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.edit_page import EditPage
from pages.movie_page import MoviePage
from pdb import set_trace as bp


class Application(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.main_page = MainPage(driver, base_url)
        self.movie_page = MoviePage(driver, base_url)
        self.register_page = RegisterPage(driver, base_url)
        self.edit_page = EditPage(driver, base_url)
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

    def add_user(self, user):
        self.main_page.register_button.click()
        lp = self.register_page
        #lp.user_email_field.clear()
        lp.user_email_field.send_keys(user.user_email)
        #lp.user_password_field.clear()
        lp.user_password_field.send_keys(user.user_password)
        #lp.user_password_confirmation_field.clear()
        lp.user_password_confirmation_field.send_keys(user.user_password)
        lp.submit_button.click()

    def delete_user(self):
        self.internal_page.edit_button.click()
        lp = self.edit_page
        lp.submit_button.click()
        self.wait.until(alert_is_present()).accept()

    def add_movie(self):
        self.internal_page.movie_poster.click()
        lp = self.movie_page
        lp.submit_button.click()

    def remove_movie(self):
        #self.internal_page.movie_poster.click()
        lp = self.movie_page
        lp.submit_button.click()









