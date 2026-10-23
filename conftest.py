import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from urls import BASE_URL
from helpers import generate_random_email, register_user, delete_user


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        browser = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument("-headless")
        browser = webdriver.Firefox(options=options)
    
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get(BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def new_user():
    email = generate_random_email()
    password = "password123"
    name = "TestUser"
    
    response = register_user(email, password, name)
    token = response.json().get("accessToken")
    
    yield {"email": email, "password": password, "token": token}
    
    delete_user(token)


@pytest.fixture
def authorized_driver(driver, new_user):
    driver.get(BASE_URL)
    driver.execute_script(f"window.localStorage.setItem('accessToken', '{new_user['token']}');")
    driver.refresh()
    yield driver
