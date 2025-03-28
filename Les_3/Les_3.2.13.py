from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_registration1(self): 
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
        input1.send_keys("Я владею автотестами в совершенстве")
        input2 = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        input2.send_keys("Я владею автотестами в совершенстве")
        input3 = browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        input3.send_keys("I'm_do_autotest_perfect@google.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(10)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self): 
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
        input1.send_keys("Я владею автотестами в совершенстве")
        input2 = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        input2.send_keys("Я владею автотестами в совершенстве")
        input3 = browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        input3.send_keys("I'm_do_autotest_perfect@google.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(10)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
if __name__ == "__main__":
    unittest.main()