import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ShopCartPage:
    """Класс корзины магазина"""

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы корзины интернет-магазина")
    def open_browser(self):
        """Открывает браузер на заданной в коде странице и разворачивает окно на весь экран"""

        self.driver.implicitly_wait(4)
        self.driver.get('https://www.saucedemo.com/cart.html')
        self.driver.maximize_window()

    @allure.step("Нажатие на кнопку checkout")
    def click_checkout(self):
        """Нажимает на кнопку Checkout"""

        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
