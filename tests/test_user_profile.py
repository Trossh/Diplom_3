import allure
from src.pages.main_page import MainPage
from src.pages.login_page import LoginPage


@allure.feature("Личный кабинет")
class TestUserProfile:
    @allure.title("Переход в личный кабинет")
    def test_navigate_to_personal_account(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        login_page.login(registered_user['email'], registered_user['password'])
        assert "site" in driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        login_page.login(registered_user['email'], registered_user['password'])
        assert "site" in driver.current_url