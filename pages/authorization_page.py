from locators.authorization_page_locators import AuthorizationPageLocators
from pages.base_page import BasePage
from allure import step

class AuthorizationPage(BasePage):

    @step('регистрируем юзера')
    def register_user(self, data):
        self.click_to_element(AuthorizationPageLocators.CREATE_ACCOUNT_BUTTON)
        self.add_text_to_element(AuthorizationPageLocators.NAME_INPUT_FIELD, data['first_name'])
        self.add_text_to_element(AuthorizationPageLocators.LAST_NAME_INPUT_FIELD, data['last_name'])
        self.add_text_to_element(AuthorizationPageLocators.USERNAME_INPUT_FIELD, data['username'])
        self.add_text_to_element(AuthorizationPageLocators.EMAIL_INPUT, data['email'])
        self.add_text_to_element(AuthorizationPageLocators.PASSWORD_INPUT, data['password'])
        self.click_to_element(AuthorizationPageLocators.CONFIRM_CREATE_ACCOUNT_BUTTON)

    @step('проверяем прошла регистрация')
    def check_registration(self):
        url = self.get_current_url()
        form = self.find_element_with_wait(AuthorizationPageLocators.AUTHORIZATION_FORM)
        return form, url


    @step('логиним юзера')
    def login(self, data):
        self.click_to_element(AuthorizationPageLocators.SIGNIN_LINK)
        self.add_text_to_element(AuthorizationPageLocators.EMAIL_INPUT, data['email'])
        self.add_text_to_element(AuthorizationPageLocators.PASSWORD_INPUT, data['password'])
        self.click_to_element(AuthorizationPageLocators.SIGNIN_CONFIRM_BUTTON)

    @step('проверяем что логин прошел успешно')
    def check_login(self):
        header = self.find_element_with_wait(AuthorizationPageLocators.MAIN_HEADER_TITLE)
        logout_link = self.find_element_with_wait(AuthorizationPageLocators.LOGOUT_LINK)
        return logout_link, header
