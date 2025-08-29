import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CalcPage:
    """Класс калькулятора"""

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы калькулятора")
    def open_browser(self):
        """Открывает браузер на заданной в коде странице и разворачивает окно на весь экран"""

        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
        )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    @allure.step("Установка задержки {sec} секунд")
    def input_delay(self, sec: int):
        """Очищает и проставляет значение delay на переданное значение"""

        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(sec)

    @allure.step("Нажатие кнопок на калькуляторе {num1}, {action}, {num2}")
    def click_in_calc(self, num1: int, action: str, num2: int):
        """Нажимает на переданные клавиши в калькуляторе. В action передается математический оператор в виде строки"""

        self.driver.find_element(By.XPATH, f"//span[text()='{num1}']").click()
        self.driver.find_element(By.XPATH, f"//span[text()='{action}']").click()
        self.driver.find_element(By.XPATH, f"//span[text()='{num2}']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Получение результата с экрана калькулятора")
    def check_for_addition(self, driver, delay: int, num1: int, num2: int):
        """Совершает операцию сложения и сравнивает результат с полученным в калькуляторе в браузере"""

        result = num1 + num2
        waiter = WebDriverWait(driver, delay + 1)
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), f"{result}"
            )
        )
        assert driver.find_element(By.CSS_SELECTOR, ".screen").text == f"{result}"
