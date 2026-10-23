from selenium.webdriver.common.by import By

class MainLocators:
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Оформить заказ']")
    
    INGREDIENT_BUN = (By.XPATH, "//a[@href='/ingredient/6acef97852135b001b21a32b']")
    INGREDIENT_COUNTER = (By.XPATH, "//a[@href='/ingredient/6acef97852135b001b21a32b']//p[contains(@class, 'counter_counter__num')]")
    BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    ORDER_NUMBER_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")
    