from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer_les = browser.find_element(By.ID, 'answer')
    answer_les.send_keys(y)

    button_math = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_math.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    time.sleep(20)
    browser.quit()