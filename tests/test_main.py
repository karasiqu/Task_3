import allure
from pages.main_page import MainPage

@allure.feature("Основной функционал")
class TestMain:

    @allure.title("Переход по клику на Конструктор")
    def test_go_to_constructor(self, driver):
        main = MainPage(driver)
        main.go_to_feed()
        main.go_to_constructor()
        main.wait_url_contains("qa-stellarburgers.education-services.ru/")

    @allure.title("Переход по клику на Ленту заказов")
    def test_go_to_feed(self, driver):
        main = MainPage(driver)
        main.go_to_feed()
        main.wait_url_contains("/feed")

    @allure.title("Всплывающее окно с деталями ингредиента")
    def test_ingredient_modal(self, driver):
        main = MainPage(driver)
        main.click_ingredient()
        assert main.is_modal_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_modal(self, driver):
        main = MainPage(driver)
        main.click_ingredient()
        main.close_modal()
        assert not main.is_modal_visible()

    @allure.title("При добавлении ингредиента увеличивается каунтер")
    def test_ingredient_counter(self, driver):
        main = MainPage(driver)
        count_before = int(main.get_ingredient_count())
        main.drag_and_drop_ingredient() 
        count_after = int(main.get_ingredient_count())
        assert count_after > count_before

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order(self, authorized_driver):
        main = MainPage(authorized_driver)
        main.drag_and_drop_ingredient()
        main.click_order()
        order_number = main.get_order_number()
        assert order_number != "9999"
