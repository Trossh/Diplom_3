from .base_page import BasePage
from src.locators.forgot_password_page_locators import ForgotPasswordPageLocators
from src.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ForgotPasswordPage(BasePage):
    def enter_email(self, email):
        self.send_keys(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    def click_restore_button(self, timeout=20):
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON, timeout)
        WebDriverWait(self.driver, timeout).until(
            EC.any_of(
                EC.visibility_of_element_located(ForgotPasswordPageLocators.MODAL_WINDOW),
                EC.url_contains("reset-password")
            )
        )

    def click_show_password_button(self):
        self.click(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_input_active(self):
        password_input = self.find_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
        return password_input.get_attribute("type") == "text"

    def go_to_forgot_password_page(self):
        self.driver.get(Config.FORGOT_PASSWORD_URL)

    def is_forgot_password_page(self):
        return self.wait_for_url(Config.FORGOT_PASSWORD_URL)