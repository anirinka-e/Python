from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

waiter = WebDriverWait(driver, 40, 0.1)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)

# Решение с тегом img
# search_img = driver.find_elements(By.CSS_SELECTOR, "img")
# print(search_img[3].get_dom_attribute("src"))

# Решение с атрибутом [alt]
search_img = driver.find_elements(By.CSS_SELECTOR, "[alt]")
print(search_img[2].get_dom_attribute("src"))

driver.quit()
