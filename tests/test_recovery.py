import allure
from pages.auth_page import AuthPage
from urls import BASE_URL, LOGIN_PATH, FORGOT_PASSWORD_PATH, RESET_PASSWORD_PATH

@allure.feature("Восстановление пароля")
class TestRecovery:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_recovery(self, driver):
        driver.get(f"{BASE_URL}{LOGIN_PATH}")
        auth = AuthPage(driver)
        auth.click_recovery_link()

        assert FORGOT_PASSWORD_PATH in auth.get_current_url()

    @allure.title("Ввод почты и клик по кнопке Восстановить")
    def test_recovery_email(self, driver):
        driver.get(f"{BASE_URL}{FORGOT_PASSWORD_PATH}")
        auth = AuthPage(driver)
        auth.fill_email("test@yandex.ru")
        auth.click_recovery_button()

        assert RESET_PASSWORD_PATH in auth.get_current_url()

    @allure.title("Клик по иконке показать/скрыть делает поле активным")
    def test_show_password(self, driver):
        driver.get(f"{BASE_URL}{RESET_PASSWORD_PATH}")
        auth = AuthPage(driver)
        auth.fill_password_recovery("123456")
        auth.toggle_password_visibility()
        assert auth.is_password_active()
