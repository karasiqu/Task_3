import allure
from pages.profile_page import ProfilePage
from urls import PROFILE_PATH, HISTORY_PATH, LOGIN_PATH

@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход по клику на Личный кабинет")
    def test_go_to_profile(self, authorized_driver):
        profile = ProfilePage(authorized_driver)
        profile.go_to_profile()

        assert PROFILE_PATH in profile.get_current_url()

    @allure.title("Переход в раздел История заказов")
    def test_go_to_history(self, authorized_driver):
        profile = ProfilePage(authorized_driver)
        profile.go_to_profile()
        profile.click_history()

        assert HISTORY_PATH in profile.get_current_url()

    @allure.title("Выход из аккаунта")
    def test_logout(self, authorized_driver):
        profile = ProfilePage(authorized_driver)
        profile.go_to_profile()
        profile.click_logout()
        profile.wait_for_login_page()

        assert LOGIN_PATH in profile.get_current_url()
