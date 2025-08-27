from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.config import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Config.BASE_URL

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")

    def find_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Elements not found: {locator}")

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ) is not None
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url(self, expected_url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(expected_url)
        )