from .base_page import BasePage
from src.locators.login_page_locators import LoginPageLocators
from src.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def click_forgot_password_link(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )

    def is_login_page(self):
        return Config.LOGIN_URL in self.get_current_url()