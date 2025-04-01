import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default= 'en',
                     help="Choose language: en, es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_argument(f"--lang={user_language}")
    print(f"\nStarting browser with language: {user_language}")
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nClosing browser")
    driver.quit()
