import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работу "
                    "калькулятора c операцией сложения")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver):
    """Тест проверяет корректность работу калькулятора c операцией сложения"""

    with allure.step("Задание начальных данных"):
        delay = 45
        num1 = 7
        action = "+"
        num2 = 8

    calc_page = CalcPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        calc_page.open_browser()

    with allure.step(f"Установка задержки {delay} секунд"):
        calc_page.input_delay(delay)

    with allure.step(f"Нажатие кнопок: {num1}, {action}, {num2}, '='"):
        calc_page.click_in_calc(num1, action, num2)

    with allure.step("Сверка полученного в калькуляторе результата"):
        calc_page.check_for_addition(driver, delay, num1, num2)
