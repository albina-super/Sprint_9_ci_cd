import pytest
from selenium import webdriver

from data import BASE_URL, MY_USER_DATA
from pages.authorization_page import AuthorizationPage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.set_capability("browserName", "chrome")
    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=options
    )
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def login_user(driver):
    user = AuthorizationPage(driver)
    user.login(MY_USER_DATA)