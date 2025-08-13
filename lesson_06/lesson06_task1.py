from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')

driver.find_element(By.CSS_SELECTOR, "button#ajaxButton").click()

waiter = WebDriverWait(driver, 40)
waiter.until(
    EC.element_located_selection_state_to_be((By.CSS_SELECTOR, ".bg-success"), False)
)

driver.implicitly_wait(15)
print(driver.find_element(By.CSS_SELECTOR, ".bg-success").text)

driver.quit()
