import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def driver():
    # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    #  Использую webdriver, установленный на ПК
    edge_driver_path = r"G:\Downloads\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    yield driver
    driver.quit()


def test_field(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    driver.implicitly_wait(4)

    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    waiter = WebDriverWait(driver, 10)
    waiter.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button"))
    )

    driver.find_element(By.CSS_SELECTOR, "button").click()
    assert driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property(
        "background-color") == "rgba(248, 215, 218, 1)"

    assert driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property(
        "background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property(
        "background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property(
        "background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property(
        "background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property(
        "background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property(
        "background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property(
        "background-color") == "rgba(209, 231, 221, 1)"
    assert driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property(
        "background-color") == "rgba(209, 231, 221, 1)"
