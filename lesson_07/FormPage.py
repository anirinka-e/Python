from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    def open_browser(self):
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
        )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_form(self, fields):
        for field, value in fields.items():
            self.waiter.until(
                EC.presence_of_element_located((By.NAME, field))
            ).send_keys(value)

    def click_button(self, button):
        self.waiter.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, button))
        ).click()

    def check_fields_green(self, fields):
        n = 0
        for field, value in fields.items():
            if self.waiter.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#" + field))
            ).value_of_css_property("background-color") == "rgba(209, 231, 221, 1)":
                n = n + 1
        return n

    def check_fields_red(self):
        return self.waiter.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#zip-code'))
        ).value_of_css_property("background-color") == "rgba(248, 215, 218, 1)"

    def check_fields(self, fields):
        assert self.check_fields_green(fields) == 9
        assert self.check_fields_red()
