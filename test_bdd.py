import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

scenarios('./features/test_bdd.feature')
# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome('/Users/marinasmirnova/PycharmProjects/pytestProject/chromedriver')
    b.implicitly_wait(10)
    yield b
    b.quit()


@given('Open browser')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)


@when(parsers.parse('We input to search "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(phrase + Keys.RETURN)


@then(parsers.parse('Search result should be "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == phrase