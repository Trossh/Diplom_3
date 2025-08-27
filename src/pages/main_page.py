from .base_page import BasePage
from src.locators.main_page_locators import MainPageLocators
from src.locators.ingredient_modal_locators import IngredientModalLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_ingredient(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        ingredients[index].click()

    def close_ingredient_modal(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON)
        try:
            WebDriverWait(self.driver, 10).until_not(
                EC.visibility_of_element_located(IngredientModalLocators.MODAL)
            )
        except TimeoutException:
            raise AssertionError("Модальное окно не закрылось после клика")

    def is_ingredient_modal_visible(self):
        return self.is_element_visible(IngredientModalLocators.MODAL)

    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    def is_order_modal_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL)

    def is_constructor_visible(self):
        return self.is_element_visible(MainPageLocators.BUNS_SECTION)