from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/feed']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    BUNS_SECTION = (By.XPATH, "//h2[contains(text(),'Булки')]")
    SAUCES_SECTION = (By.XPATH, "//h2[contains(text(),'Соусы')]")
    FILLINGS_SECTION = (By.XPATH, "//h2[contains(text(),'Начинки')]")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class,'Ingredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class,'counter_counter__')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__')]")