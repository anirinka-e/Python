import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ShopInventoryPage:
    """Класс добавления товаров в корзину и перехода в нее"""

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Добавление товаров products в корзину")
    def add_to_cart(self, products: list):
        """Добавляет товары в корзину согласно списку products"""

        for i in products:
            self.driver.find_element(
                By.CSS_SELECTOR, "#add-to-cart-" + i
            ).click()

    @allure.step("Нажатие на корзину для перехода в нее")
    def click_to_cart(self):
        """Нажимает на кнопку Корзины"""

        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        ).click()
