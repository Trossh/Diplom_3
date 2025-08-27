from selenium.webdriver.common.by import By

class IngredientModalLocators:
    MODAL = (By.CLASS_NAME, "Modal_modal__P3_V5")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_NAME = (By.CLASS_NAME, "Modal_modal__title__2L34m")
    INGREDIENT_DETAILS = (By.CLASS_NAME, "Modal_modal__details__2LYM1")