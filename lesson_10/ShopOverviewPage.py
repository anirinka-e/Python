import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ShopOverviewPage:
    """Класс итоговой страницы с суммой стоимости товаров в магазине"""

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы отображения итоговой суммы стоимости")
    def open_browser(self):
        """Открывает браузер на заданной в коде странице и разворачивает окно на весь экран"""

        self.driver.implicitly_wait(4)
        self.driver.get('https://www.saucedemo.com/checkout-step-two.html')
        self.driver.maximize_window()

    @allure.step("Сравнение суммы с верным значением")
    def check_overview(self):
        """Проверяет соответствие полученного значения суммы стоимости товаров"""

        result = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label"
        ).text
        print(result)
        assert result == "Total: $58.29"
