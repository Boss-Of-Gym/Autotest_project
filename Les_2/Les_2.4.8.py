from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element(By.ID, 'book')
    button.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer_les = browser.find_element(By.ID, 'answer')
    answer_les.send_keys(y)
    button_math = browser.find_element(By.ID, 'solve')
    button_math.click()

    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(answer)
    alert.accept()

    # авторизуемся на Степике
    browser.get('https://stepik.org/catalog?auth=login')
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@id='id_login_email']").send_keys('alienlifeform423@gmail.com')  # здесь вводится e-mail
    browser.find_element(By.XPATH, "//input[@id='id_login_password']").send_keys('1325468790Dimka')  # здесь вводится пароль
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
    time.sleep(3)
    
    url = 'https://stepik.org/lesson/181384/step/8?unit=156009'
    browser.execute_script(f"window.open('{url}', '_blank');")
    WebDriverWait(browser, 10).until(lambda browser: len(browser.window_handles) > 1)
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])

    answer_input = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@class='ember-text-area ember-view textarea string-quiz__textarea']")))
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(answer)

    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']")))
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()