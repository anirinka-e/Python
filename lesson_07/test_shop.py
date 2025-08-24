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


def test_calc(driver):
    login = "standard_user"
    password = "secret_sauce"

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

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

    shop_page.open_browser()
    shop_page.input_login(login, password)
    shop_page.click_login()

    inventory_page.add_to_cart(products)
    inventory_page.click_to_cart()

    shop_cart_page.click_checkout()

    checkout_step_one_cart_page.input_information(fields)
    checkout_step_one_cart_page.click_continue()

    checkout_overview.check_overview()
