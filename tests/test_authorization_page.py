from data import SIGNIN_URL, MY_USER_DATA, MAIN_PAGE_URL
from helpers import generate_registration_data
from pages.authorization_page import AuthorizationPage
from allure import title

class TestAuthorizationPage:

    @title('тест на успешную регистрацию')
    def test_register_success(self, driver):
        user = AuthorizationPage(driver)
        data = generate_registration_data()
        user.register_user(data)
        form, url = user.check_registration()
        assert form.is_displayed() and url == SIGNIN_URL

    @title('тест на успешный логин')
    def test_login_success(self, driver):
        user = AuthorizationPage(driver)
        user.login(MY_USER_DATA)
        logout_link, header = user.check_login()
        assert logout_link.is_displayed() and header.text == "Рецепты"