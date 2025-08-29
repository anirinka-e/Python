import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from ShopPage import ShopPage
from ShopInventoryPage import ShopInventoryPage
from ShopCartPage import ShopCartPage
from ShopCheckoutStepOnePage import ShopCheckoutStepOnePage
from ShopOverviewPage import ShopOverviewPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.close()
    driver.quit()


@allure.title("Тестирование интернет-магазина")
@allure.description(
    "Тест проверяет корректность вывода "
    "суммы стоимости товаров перед оплатой")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver):
    with allure.step("Задание данных для авторизации login и password"):
        login = "standard_user"
        password = "secret_sauce"

    with allure.step("Задание товаров products"):
        products = [
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie"
        ]

    with allure.step("Задание данных пользователя для оплаты fields"):
        fields = {
            'first-name': "Екатерина",
            'last-name': "Твердова",
            'postal-code': "1234567",
        }

    shop_page = ShopPage(driver)
    inventory_page = ShopInventoryPage(driver)
    shop_cart_page = ShopCartPage(driver)
    checkout_step_one_cart_page = ShopCheckoutStepOnePage(driver)
    checkout_overview = ShopOverviewPage(driver)

    with allure.step(f"Авторизация с использованием {login} и {password}"):
        shop_page.open_browser()
        shop_page.input_login(login, password)
        shop_page.click_login()

    with allure.step(f"Добавление товаров {products} в корзину"):
        inventory_page.add_to_cart(products)
        inventory_page.click_to_cart()

    with allure.step("Нажатие на кнопку checkout в корзине"):
        shop_cart_page.click_checkout()

    with allure.step(f"Ввод данных пользователя для оплаты и "
                     f"переход на страницу итоговой суммы стоимости"):
        checkout_step_one_cart_page.input_information(fields)
        checkout_step_one_cart_page.click_continue()

    with allure.step("Сравнение суммы с верным значением"):
        checkout_overview.check_overview()
