from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    def open_browser(self):
        self.driver.implicitly_wait(4)
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()

    def input_login(self, login, password):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
