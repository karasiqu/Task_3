from selenium.webdriver.common.by import By

class AuthLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    RECOVERY_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    RECOVERY_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_INPUT_RECOVERY = (By.XPATH, "//input[@type='password']")
    SHOW_PASSWORD_ICON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
