from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver, url):
        self.chrome = driver
        self.url = url
        self.chrome.implicity_wait(5)
        pass

    def open(self):
        self.chrome.get(self.url)

    def is_element_present(self, locator):
        try:
            self.chrome.find_element(locator)
        except NoSuchElementException:
            return False
        return True

