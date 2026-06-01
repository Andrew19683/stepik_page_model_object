import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_configure(config):
    config.addinivalue_line("markers", "positive: positive tests")
    config.addinivalue_line("markers", "negative: negative tests")
    config.addinivalue_line("markers", "parametrized: parametrized tests")
    config.addinivalue_line("markers", "login_guest: login tests for guest users")
    config.addinivalue_line("markers", "need_review: tests that need to be reviewed")

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, etc.")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()