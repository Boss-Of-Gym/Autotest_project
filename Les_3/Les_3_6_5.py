from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time, pytest

class Test_with_many_links():
    incorrect_messages = []

    @pytest.mark.parametrize("links", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_with_open_many_links_for_test(self, browser, links):
        url = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(url)
        browser.implicitly_wait(5)
        try:
            button_enter = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]')))
            button_enter.click()
            email_input = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='id_login_email']")))
            email_input.send_keys('')
            password_input = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='id_login_password']")))
            password_input.send_keys('')
            login_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'sign-form__btn')))
            login_button.click()
            browser.implicitly_wait(5)
        except:
            print(f"Не удалось авторизоваться на странице {url}")
            pytest.fail(f"Не удалось авторизоваться на странице {url}")

        again_buttom = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn.white")))
        again_buttom.click()
        answer_input = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@class='ember-text-area ember-view textarea string-quiz__textarea']")))
        answer = str(math.log(int(time.time())))
        answer_input.send_keys(answer)
        browser.implicitly_wait(5)
        button = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']")))
        button.click()

        time.sleep(2)  # ждем появления надписи

        try:
            visibly = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
            visibly_text = visibly.text
            if "Correct!" not in visibly_text:
                Test_with_many_links.incorrect_messages.append(f"Lesson {links}: Expected 'Correct!', but got '{visibly_text}'")
            assert "Correct!" in visibly_text, f"Lesson {links}: Expected 'Correct!', but got '{visibly_text}'"
        except:
            print(f"Не удалось получить фидбек на странице {url}")
            pytest.fail(f"Не удалось получить фидбек на странице {url}")

    @classmethod
    def teardown_class(cls):
        if cls.incorrect_messages:
            print("\nНайденные кусочки послания:")
            for message in cls.incorrect_messages:
                print(message)