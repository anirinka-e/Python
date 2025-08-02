from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
sleep(1)

search_field = "#username"
username = driver.find_element(By.CSS_SELECTOR, search_field)
username.send_keys("tomsmith")
print("Ввелось значение tomsmith")
sleep(1)

search_field = "#password"
password = driver.find_element(By.CSS_SELECTOR, search_field)
password.send_keys("SuperSecretPassword!")
print("Ввелось значение SuperSecretPassword!")
sleep(1)

search_field = "i"
button_login = driver.find_element(By.CSS_SELECTOR, search_field)
button_login.click()
sleep(1)

driver.quit()
