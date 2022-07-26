from Pages.base_page import BasePage
from Locators.dresses_loc import DressesLoc
import allure


class DressesPage(BasePage):

    @allure.step
    def verify_women_is_present(self):
        assert self.is_element_present(DressesLoc.women_loc), 'Element Women is not present!'
