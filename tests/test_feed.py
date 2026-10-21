import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.feed_page import FeedPage
from locators.feed_locators import FeedLocators

@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Клик по заказу открывает всплывающее окно с деталями")
    def test_order_details_modal(self, driver):
        feed = FeedPage(driver)
        feed.go_to_feed()
        feed.click_first_order()
        
        # Увеличили время ожидания до 15 секунд (сервер лагает)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located(FeedLocators.ORDER_DETAILS_MODAL))
        
        assert feed.is_modal_visible()

    @allure.title("Счётчик Выполнено за всё время отображается")
    def test_counter_all_time(self, driver):
        feed = FeedPage(driver)
        feed.go_to_feed()
        count = feed.get_done_all_time()
        assert count >= 0
