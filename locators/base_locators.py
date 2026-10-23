from selenium.webdriver.common.by import By

class BaseLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]")
