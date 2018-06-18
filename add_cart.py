# -*- coding: utf-8 -*-
from model.user import User
from pdb import set_trace as bp
from selenium import webdriver
from selenium.common.exceptions import *
from conftest import app


def test_add_movie(app):
    app.login(User.Admin())
    #assert app.is_logged_in()
    app.add_movie()
    #bp()
    # app.move_cart_page()
    assert app.add_movie_in_cart()
    app.remove_movie()
    # assert app.remove_movie_in_cart()
    app.logout()
    #assert app.is_not_logged_in()