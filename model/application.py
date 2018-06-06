# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class Application(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_home_page(self):
        self.driver.get("http://kuki.webtest2.htc-cs.com/"+"users/login")

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Выйти").click()

    def login(self, user):
        driver = self.driver
        driver.find_element_by_id("user_email").click()
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys(user.user_email)
        driver.find_element_by_id("user_password").click()
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys(user.user_password)
        driver.find_element_by_name("commit").click()

    def is_logged_in(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "div.alert-box")))
            return True
        except WebDriverException:
            return False

    def is_not_logged_in(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "div.alert-box")))
            return True
        except WebDriverException:
            return False