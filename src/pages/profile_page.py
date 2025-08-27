from .base_page import BasePage
from src.locators.profile_page_locators import ProfilePageLocators
from src.config import Config


class ProfilePage(BasePage):
    def click_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    def click_logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    def is_order_history_visible(self):
        return self.is_element_visible(ProfilePageLocators.ORDER_HISTORY_LINK)

    def go_to_profile_page(self):
        self.driver.get(Config.PROFILE_URL)

    def is_profile_page(self):
        return self.wait_for_url(Config.PROFILE_URL)