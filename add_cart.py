# -*- coding: utf-8 -*-
from model.user import User
from selenium import webdriver
from selenium.common.exceptions import *
from conftest import app

def test_add_movie(app):
    app.login(User.Admin())
    #assert app.is_logged_in()
    app.add_movie()
    app.remove_movie()
    app.logout()
    #assert app.is_not_logged_in()