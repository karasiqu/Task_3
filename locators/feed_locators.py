from selenium.webdriver.common.by import By

class FeedLocators:
    DONE_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DONE_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]")
