from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_name1 = browser.find_element(By.XPATH, '//label[text()="First name* "]/following-sibling::input[1]')
    input_name1.send_keys('Autotest')
    input_name2 = browser.find_element(By.XPATH, '//label[text()="First name* "]/following-sibling::input[2]')
    input_name2.send_keys('Autotester')
    input_email = browser.find_element(By.XPATH, '//label[text()="First name* "]/following-sibling::input[3]')
    input_email.send_keys('Autotester@autotest.at')
    dirrectory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dirrectory, 'Les 2.2.8 test_file.txt')
    file_button = browser.find_element(By.NAME, "file")
    file_button.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()