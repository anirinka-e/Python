import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calc(driver):
    delay = 45
    num1 = 7
    action = "+"
    num2 = 8

    calc_page = CalcPage(driver)
    calc_page.open_browser()
    calc_page.input_delay(delay)
    calc_page.click_in_calc(num1, action, num2)
    calc_page.check_for_addition(driver, delay, num1, num2)
