from selenium import webdriver
import pytest
from model.application import Application


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="browser type")
    parser.addoption("--base_url", action="store", default="", help="base_url")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")

@pytest.fixture(scope="session")
def app(request, browser_type, base_url):

    if browser_type == "Chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "ie":
        driver = webdriver.Ie()
    #driver.implicitly_wait(30)
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)