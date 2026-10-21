from pages.base_page import BasePage
from locators.feed_locators import FeedLocators

class FeedPage(BasePage):

    def get_done_all_time(self):
        return int(self.get_text(FeedLocators.DONE_ALL_TIME))

    def get_done_today(self):
        return int(self.get_text(FeedLocators.DONE_TODAY))

    def click_first_order(self):
        self.safe_click(FeedLocators.ORDER_ITEM)

    def is_modal_visible(self):
        return self.is_visible(FeedLocators.ORDER_DETAILS_MODAL)
