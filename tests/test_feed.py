import allure
from pages.feed_page import FeedPage

@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Клик по заказу открывает всплывающее окно с деталями")
    def test_order_details_modal(self, driver):
        feed = FeedPage(driver)
        feed.go_to_feed()
        feed.click_first_order()
        
        assert feed.is_modal_visible()

    @allure.title("Счётчик Выполнено за всё время отображается")
    def test_counter_all_time(self, driver):
        feed = FeedPage(driver)
        feed.go_to_feed()
        count = feed.get_done_all_time()
        assert count >= 0
