from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Определяем поля
    firstname_input = browser.find_element(By.CLASS_NAME, "first_block .first")
    lastname_input = browser.find_element(By.CLASS_NAME, "first_block .second")
    email_input = browser.find_element(By.CLASS_NAME, "first_block .third")
    phone_input = browser.find_element(By.CLASS_NAME, "second_block .first")
    address_input = browser.find_element(By.CLASS_NAME, "second_block .second")
    
    # Заполняем поля
    firstname_input.send_keys("Александр")
    lastname_input.send_keys("Фёдоров")
    email_input.send_keys("sasha@campanelli.ru")
    time.sleep(3)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
