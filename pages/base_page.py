from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def safe_click(self, locator):
        overlays = self.driver.find_elements(*BaseLocators.MODAL_OVERLAY)
        if overlays:
            self.wait.until(EC.invisibility_of_element_located(BaseLocators.MODAL_OVERLAY))
        self.click(locator)

    def get_text(self, locator):
        return self.find(locator).text

    def get_value(self, locator):
        return self.find(locator).get_attribute("value")

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_url_contains(self, substring):
        self.wait.until(EC.url_contains(substring))

    def go_to_constructor(self):
        self.safe_click(BaseLocators.CONSTRUCTOR_BUTTON)

    def go_to_feed(self):
        self.safe_click(BaseLocators.FEED_BUTTON)

    def go_to_profile(self):
        self.safe_click(BaseLocators.PROFILE_BUTTON)

    def get_current_url(self):
        return self.driver.current_url