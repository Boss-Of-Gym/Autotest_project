from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)
    browser.execute_script('window.scrollBy(0, 150);')
    click_checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    click_checkbox.click()
    click_radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    click_radio.click()

    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()