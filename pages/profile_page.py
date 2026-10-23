from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators
from locators.auth_locators import AuthLocators

class ProfilePage(BasePage):

    def click_history(self):
        self.safe_click(ProfileLocators.HISTORY_BUTTON)

    def click_logout(self):
        self.safe_click(ProfileLocators.LOGOUT_BUTTON)

    def wait_for_login_page(self):
        self.wait.until(EC.presence_of_element_located(AuthLocators.LOGIN_BUTTON))

    def get_profile_email(self):
        return self.get_value(ProfileLocators.EMAIL_VALUE)
