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


def test_form(driver):
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
    form_page.open_browser()
    form_page.input_form(fields)
    form_page.click_button("button")
    form_page.check_fields(fields)
