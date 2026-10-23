from selenium.webdriver.common.by import By

class ProfileLocators:
    HISTORY_BUTTON = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3')]")
    EMAIL_VALUE = (By.XPATH, "//input[@name='name' and @disabled]")
