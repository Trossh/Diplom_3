from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon')]")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class,'modal') or contains(@class,'Modal')]")