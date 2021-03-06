from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Firefox()
    browser.get(link)
    
    # Найдём все поля
    firstname_input = browser.find_element(By.NAME, "first_name")
    lastname_input = browser.find_element(By.NAME, "last_name")
    city_input = browser.find_element(By.CLASS_NAME, "city")
    country_input = browser.find_element(By.ID, "country")
    
    # Присвоим значения    
    firstname_input.send_keys("Александр")
    lastname_input.send_keys("Фёдоров")
    city_input.send_keys("Москва")
    country_input.send_keys("Россия")

    # Отправим значения
    button = browser.find_element(By.XPATH, "//form/div[6]/button[3]")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()
