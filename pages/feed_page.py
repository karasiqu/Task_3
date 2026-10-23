from pages.base_page import BasePage
from locators.feed_locators import FeedLocators
from selenium.webdriver.support import expected_conditions as EC

class FeedPage(BasePage):

    def get_done_all_time(self):
        return int(self.get_text(FeedLocators.DONE_ALL_TIME))

    def get_done_today(self):
        return int(self.get_text(FeedLocators.DONE_TODAY))

    def click_first_order(self):
        self.safe_click(FeedLocators.ORDER_ITEM)

    def is_modal_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(FeedLocators.ORDER_DETAILS_MODAL))
            return True
        except:
            return False
