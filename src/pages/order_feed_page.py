from .base_page import BasePage
from src.locators.order_feed_page_locators import OrderFeedPageLocators
from src.config import Config



class OrderFeedPage(BasePage):
    def click_order(self, index=0):
        orders = self.find_elements(OrderFeedPageLocators.ORDER_CARD)
        if orders:
            orders[index].click()

    def is_order_modal_visible(self):
        try:
            modal = self.driver.find_element(*OrderFeedPageLocators.ORDER_MODAL)
            return True
        except:
            return False

    def get_total_orders_count(self):
        element = self.find_element(OrderFeedPageLocators.TOTAL_ORDERS)
        return int(element.text) if element.text.isdigit() else 0

    def get_today_orders_count(self):
        element = self.find_element(OrderFeedPageLocators.TODAY_ORDERS)
        return int(element.text) if element.text.isdigit() else 0

    def go_to_order_feed_page(self):
        self.driver.get(Config.ORDER_FEED_URL)

    def is_order_feed_page(self):
        return Config.ORDER_FEED_URL in self.get_current_url()