from selenium.webdriver.common.by import By

def test_add_to_cart_button_exists(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(add_to_cart_button) > 0, "Кнопка 'Добавить в корзину' не найдена на странице"