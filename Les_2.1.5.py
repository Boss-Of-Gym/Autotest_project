from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = input1.text
    y = calc(x)
    input2 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input2.send_keys(y)
    optional_1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    optional_1.click()
    optional_2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    optional_2.click()
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()