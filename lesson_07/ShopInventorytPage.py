from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ShopInventorytPage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    def add_to_cart(self, products):
        for i in products:
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-" + i).click()

    def click_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
