from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_CARD = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem__2x95r')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__container__Wo2l_')]")
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class,'OrderHistory_textBox')]")
    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")