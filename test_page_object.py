import pytest

from Pages.login_page import LoginPage
from Pages.main_page import MainPage
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome('/Users/marinasmirnova/PycharmProjects/pytestProject/chromedriver')


def test_guest_can_open_login_page(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(browser, link)

    try:
        login_page = LoginPage(
            browser, url='http://automationpractice.com/index.php?controller=authentication&back=my-account')
        login_page.login()






        main_page.open()
        main_page.verify_login_link()
        main_page.open_login_page()
        login_page = LoginPage(browser, url=browser.current_url)
        login_page.login()
    finally:
        browser.quit()


def test_basket_is_empty(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(browser, link)

    try:
        main_page.open()
        main_page.verify_basket_is_empty()
    finally:
        browser.quit()

