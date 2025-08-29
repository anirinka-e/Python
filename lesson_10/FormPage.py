import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FormPage:
    """Класс формы"""

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы формы")
    def open_browser(self):
        """Открывает браузер на заданной в коде странице и разворачивает окно на весь экран"""

        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
        )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    @allure.step("Введение значений полей fields в форму")
    def input_form(self, fields: dict):
        """Вводит в поля значения, согласно переданному словарю fields"""

        for field, value in fields.items():
            self.waiter.until(
                EC.presence_of_element_located((By.NAME, field))
            ).send_keys(value)

    @allure.step("Нажатие на кнопку Submit")
    def click_button(self, button: str):
        """Нажимает на кнопку Submit"""

        self.waiter.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, button))
        ).click()

    @allure.step("Возвращение количества зеленых полей fields")
    def check_fields_green(self, fields: dict) -> int:
        """Возвращает количество зеленых полей"""

        n = 0
        for field, value in fields.items():
            if self.waiter.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#" + field))
            ).value_of_css_property("background-color") == "rgba(209, 231, 221, 1)":
                n = n + 1
        return n

    @allure.step("Возвращение значения поля zip-code")
    def check_fields_red(self):
        """Возвращает цвет поля zip-code"""

        return self.waiter.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#zip-code'))
        ).value_of_css_property("background-color") == "rgba(248, 215, 218, 1)"

    @allure.step("Проверка соответствия цветов полей fields")
    def check_fields(self, fields: dict):
        """Проверяет, что поля соответствуют правильным цветам (заполненные зеленым, незаполненные красным)"""

        assert self.check_fields_green(fields) == 9
        assert self.check_fields_red()
