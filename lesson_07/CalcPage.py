from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 10)

    def open_browser(self):
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_delay(self, sec):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(sec)

    def click_in_calc(self, num1, action, num2):
        self.driver.find_element(By.XPATH, f"//span[text()='{num1}']").click()
        self.driver.find_element(By.XPATH, f"//span[text()='{action}']").click()
        self.driver.find_element(By.XPATH, f"//span[text()='{num2}']").click()
        self.driver.find_element(By.XPATH, f"//span[text()='=']").click()

    def check_for_addition(self, driver, delay, num1, num2):
        result = num1 + num2
        waiter = WebDriverWait(driver, delay + 1)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), f"{result}")
        )
        assert driver.find_element(By.CSS_SELECTOR, ".screen").text == f"{result}"
