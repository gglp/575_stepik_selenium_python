from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Определяем поля
    firstname_input = browser.find_element(By.NAME, "firstname")
    lastname_input = browser.find_element(By.NAME, "lastname")
    email_input = browser.find_element(By.NAME, "email")
    file_input = browser.find_element(By.NAME, "file")
    
    # Подготовим файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    # Заполняем поля
    firstname_input.send_keys("Александр")
    lastname_input.send_keys("Фёдоров")
    email_input.send_keys("sasha@campanelli.ru")
    file_input.send_keys(file_path)
    
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
