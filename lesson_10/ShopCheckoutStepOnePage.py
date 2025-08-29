import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ShopCheckoutStepOnePage:
    """Класс ввода данных пользователя для оплаты в магазине"""

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы ввода данных для оплаты в интернет-магазине")
    def open_browser(self):
        """Открывает браузер на заданной в коде странице и разворачивает окно на весь экран"""

        self.driver.implicitly_wait(4)
        self.driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self.driver.maximize_window()

    @allure.step("Ввод данных пользователя fields")
    def input_information(self, fields: dict):
        """Вводит данные пользователя для оплаты, согласно словарю fields"""

        for field, value in fields.items():
            self.driver.find_element(
                By.CSS_SELECTOR, "#" + field
            ).send_keys(value)

    @allure.step("Нажатие на кнопку continue")
    def click_continue(self):
        """Нажимает на кнопку continue"""

        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
