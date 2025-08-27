import allure
from src.pages.main_page import MainPage
from src.pages.login_page import LoginPage
import time


@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title("Переход в конструктор")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_constructor()
        assert main_page.is_constructor_visible()

    @allure.title("Переход в ленту заказов")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed()
        assert "feed" in driver.current_url

    @allure.title("Открытие модального окна ингредиента")
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_ingredient()
        assert main_page.is_ingredient_modal_visible()
        main_page.close_ingredient_modal()
        assert not main_page.is_ingredient_modal_visible()

    @allure.title("Оформление заказа авторизованным пользователем")
    def test_make_order_authenticated(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        login_page.login(registered_user['email'], registered_user['password'])
        main_page.go_to_site()
        main_page.click_order_button()
        assert main_page.is_order_modal_visible()