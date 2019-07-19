import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'user_language'})
browser = webdriver.Chrome(options=options)

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome')
    parser.addoption('--language', action='store', default='ru')

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    browser.quit()
