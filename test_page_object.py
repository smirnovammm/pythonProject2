import pytest

from .Pages.login_page import LoginPage
from .Pages.main_page import MainPage
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome('./chromedriver')
    browser.implicitly_wait(5)


def test_guest_can_open_login_page(open_browser):
    link = "http://automationpractice.com/index.php"
    page = MainPage(browser, link)

    try:
        page.open()
        page.verify_login_link()
        page.open_login_page()
        login_page = LoginPage(browser, url=browser.current_url)
        login_page.verify_login_link()
    finally:
        browser.quit()
