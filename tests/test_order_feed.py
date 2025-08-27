import allure
from src.pages.order_feed_page import OrderFeedPage



@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Открытие деталей заказа")
    def test_order_details_modal(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_order_feed_page()
        order_feed_page.click_order()
        assert order_feed_page.is_order_modal_visible()

    @allure.title("Проверка отображения ленты заказов")
    def test_order_feed_display(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_order_feed_page()
        assert order_feed_page.is_order_feed_page()