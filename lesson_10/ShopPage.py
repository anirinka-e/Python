import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ShopPage:
    """Главная страница магазина"""

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы авторизации")
    def open_browser(self):
        """Открывает браузер на заданной в коде странице и разворачивает окно на весь экран"""

        self.driver.implicitly_wait(4)
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()

    @allure.step("Ввод логина и пароля: login и password")
    def input_login(self, login: str, password: str):
        """Вводит в поля значения login и password"""

        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name"
        ).send_keys(login)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

    @allure.step("Нажатие на кнопку Login")
    def click_login(self):
        """Нажимает на кнопку Login"""

        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button"
        ).click()
