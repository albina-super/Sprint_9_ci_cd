import pytest
from selenium import webdriver

from data import BASE_URL, MY_USER_DATA
from pages.authorization_page import AuthorizationPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def login_user(driver):
    user = AuthorizationPage(driver)
    user.login(MY_USER_DATA)