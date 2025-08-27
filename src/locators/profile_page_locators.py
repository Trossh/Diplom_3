from selenium.webdriver.common.by import By

class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[contains(@href,'/account/profile')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@href,'/account/order-history')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")