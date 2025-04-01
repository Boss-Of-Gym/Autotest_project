import time
from selenium.webdriver.common.by import By

def test_add_to_cart_button_exists(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(30)
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(add_to_cart_button) > 0, "Кнопка 'Добавить в корзину' не найдена на странице"
    button_text = add_to_cart_button[0].text
    print(f"Button text: {button_text}")