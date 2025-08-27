import allure
from src.pages.main_page import MainPage
from src.pages.login_page import LoginPage
from src.pages.forgot_password_page import ForgotPasswordPage
import time


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_password_recovery(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        login_page.click_forgot_password_link()
        assert "forgot-password" in driver.current_url

    @allure.title("Ввод почты и восстановление пароля")
    def test_password_recovery_process(self, driver, test_email):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.go_to_forgot_password_page()
        forgot_password_page.enter_email(test_email)
        forgot_password_page.click_restore_button()
        assert "reset-password" in driver.current_url