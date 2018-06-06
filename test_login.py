# -*- coding: utf-8 -*-
from model.user import User
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app


def test_valid_login(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()


#def test_invalid_login(app):
#    app.go_to_home_page()
 #   app.login(User.random()) #не понятно как прописать аттрибут рандом#
  #  assert not app.is_logged_in()