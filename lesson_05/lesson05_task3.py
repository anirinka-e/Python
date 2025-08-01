from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(1)
search_field = "input"
test_field = driver.find_element(By.CSS_SELECTOR, search_field)

test_field.send_keys("123", Keys.RETURN)
print("Ввелось значение 123")
test_field.clear()
sleep(1)
test_field.send_keys("999", Keys.RETURN)
print("Ввелось значение 999")
driver.quit()
