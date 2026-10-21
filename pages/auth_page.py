from pages.base_page import BasePage
from locators.auth_locators import AuthLocators

class AuthPage(BasePage):

    def click_recovery_link(self):
        self.safe_click(AuthLocators.RECOVERY_LINK)

    def fill_email(self, email):
        self.find(AuthLocators.RECOVERY_EMAIL_INPUT).send_keys(email)

    def click_recovery_button(self):
        self.safe_click(AuthLocators.RECOVERY_BUTTON)

    def fill_password_recovery(self, password):
        self.find(AuthLocators.PASSWORD_INPUT_RECOVERY).send_keys(password)

    def toggle_password_visibility(self):
        self.safe_click(AuthLocators.SHOW_PASSWORD_ICON)

    def is_password_active(self):
        container = self.find((By.XPATH, "//div[contains(@class, 'input_type_password')]"))
        return "input_status_active" in container.get_attribute("class")
