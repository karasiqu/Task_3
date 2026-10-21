import allure
from pages.profile_page import ProfilePage

@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход по клику на Личный кабинет")
    def test_go_to_profile(self, authorized_driver):
        profile = ProfilePage(authorized_driver)
        profile.go_to_profile()
        profile.wait_url_contains("/account/profile")

    @allure.title("Переход в раздел История заказов")
    def test_go_to_history(self, authorized_driver):
        profile = ProfilePage(authorized_driver)
        profile.go_to_profile()
        profile.click_history()
        profile.wait_url_contains("/account/order-history")

    @allure.title("Выход из аккаунта")
    def test_logout(self, authorized_driver):
        profile = ProfilePage(authorized_driver)
        profile.go_to_profile()
        profile.click_logout()
        profile.wait_for_login_page()
        assert "/login" in authorized_driver.current_url
