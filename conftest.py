import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="Store", default="Chrome", help="browser type")
    parser.addoption("--base_url", action="store", default="http://kuki.webtest2.htc-cs.com/"+"users/login", help="base_url")


@pytest.fixture(scope="module")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="module")
def base_url(request):
    return request.config.getoption("--base_url")