from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ShopCartPage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    def open_browser(self):
        self.driver.implicitly_wait(4)
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()

    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
