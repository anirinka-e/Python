from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')

search_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

waiter = WebDriverWait(driver, 40)
waiter.until(
    EC.element_located_selection_state_to_be((By.CSS_SELECTOR, "#updatingButton"), False)
)

search_field.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

driver.implicitly_wait(15)
print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()
