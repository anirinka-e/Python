import allure
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from FormPage import FormPage


@pytest.fixture
def driver():
    # Открытие драйвера
    # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    # Использую webdriver, установленный на ПК
    edge_driver_path = r"G:\Downloads\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    yield driver
    driver.quit()


@allure.title("Тестирование формы")
@allure.description(
    "Тест проверяет корректность отображения цветов полей в"
    " форме в зависимости от заполнения или отсутствия значений")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_form(driver):
    with allure.step(f"Задание начальных данных fields"):
        fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    form_page = FormPage(driver)
    with allure.step("Открытие страницы формы"):
        form_page.open_browser()

    with allure.step(f"Заполнение формы значениями {fields}"):
        form_page.input_form(fields)

    with allure.step("Нажатие на кнопку Submit"):
        form_page.click_button("button")

    with allure.step("Проверка результата на соответствие цветов"):
        form_page.check_fields(fields)
