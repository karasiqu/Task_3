from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_locators import MainLocators
from locators.base_locators import BaseLocators


class MainPage(BasePage):
    
    def click_ingredient(self):
        self.safe_click(MainLocators.INGREDIENT_BUN)

    def get_ingredient_count(self):
        return self.get_text(MainLocators.INGREDIENT_COUNTER)

    def is_modal_visible(self):
        return self.is_visible(MainLocators.INGREDIENT_MODAL_TITLE)

    def close_modal(self):
        self.safe_click(BaseLocators.MODAL_CLOSE)
        self.wait.until(EC.invisibility_of_element_located(MainLocators.INGREDIENT_MODAL_TITLE))

    def drag_and_drop_ingredient(self):
        ingredient = self.find(MainLocators.INGREDIENT_BUN)
        basket = self.find(MainLocators.BASKET)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(ingredient, basket).perform()

    def click_order(self):
        self.safe_click(MainLocators.ORDER_BUTTON)

    def get_order_number(self):
        return self.get_text(MainLocators.ORDER_NUMBER_MODAL)
