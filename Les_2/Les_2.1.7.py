from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    print(x)
    y = calc(x)
    print(y)
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    click_check = browser.find_element(By.ID, 'robotCheckbox')
    click_check.click()
    clike_radio = browser.find_element(By.ID, 'robotsRule')
    clike_radio.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    print('Тест успешно завершен. Скоро будет закрытие браузера...')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()