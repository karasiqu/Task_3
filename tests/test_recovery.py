import allure
from pages.auth_page import AuthPage
from urls import BASE_URL

@allure.feature("Восстановление пароля")
class TestRecovery:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_recovery(self, driver):
        driver.get(f"{BASE_URL}/login")
        auth = AuthPage(driver)
        auth.click_recovery_link()
        auth.wait_url_contains("/forgot-password")

    @allure.title("Ввод почты и клик по кнопке Восстановить")
    def test_recovery_email(self, driver):
        driver.get(f"{BASE_URL}/forgot-password")
        auth = AuthPage(driver)
        auth.fill_email("test@yandex.ru")
        auth.click_recovery_button()
        auth.wait_url_contains("/reset-password")

    @allure.title("Клик по иконке показать/скрыть делает поле активным")
    def test_show_password(self, driver):
        driver.get(f"{BASE_URL}/reset-password")
        auth = AuthPage(driver)
        auth.fill_password_recovery("123456")
        auth.toggle_password_visibility()
        assert auth.is_password_active()
