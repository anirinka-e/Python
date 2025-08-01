from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
sleep(1)
search_field = "button.btn.btn-primary"
button = driver.find_element(By.CSS_SELECTOR, search_field)
button.click()
print("Кнопка нажалась")
sleep(2)
