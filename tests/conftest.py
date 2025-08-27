import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user():
    return {
        "email": "111@gmail.ru",
        "password": "1234567890",
    }


@pytest.fixture
def test_email():
    return "test@example.com"