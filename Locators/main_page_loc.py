from selenium.webdriver.common.by import By


class MainPageLoc:

    login_loc = (By.CSS_SELECTOR, ".login")
    basket_empty_loc = (By.XPATH, '//div[@class="shopping_cart"]//span[contains(text(), "(empty)")]')