import pytest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.dresses_page import DressesPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def open_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


def test_guest_can_open_login_page(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(open_browser, link)
    try:
        main_page.open()
        main_page.verify_login_link()
        main_page.open_login_page()
        login_page = LoginPage(open_browser, url=open_browser.current_url)
        login_page.login()
    finally:
        open_browser.quit()


def test_basket_is_empty(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(open_browser, link)

    main_page.open()
    main_page.verify_basket_is_empty()


def test_dresses_page_working(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(open_browser, link)
    main_page.open()
    main_page.go_to_dresses_page()
    dresses_page = DressesPage(open_browser, open_browser.current_url)
    dresses_page.verify_women_is_present()
