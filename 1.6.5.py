from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(link_text)
time.sleep(5)


try:
    browser = webdriver.Firefox()
    browser.get(link)
    time.sleep(5)
    
    # Найдём ссылку
    scope_link = browser.find_element_by_link_text(link_text)
    scope_link.click()
    
    # Заполним форму получения кода    
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
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(50)
    browser.quit()
