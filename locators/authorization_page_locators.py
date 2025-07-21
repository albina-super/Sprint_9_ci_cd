from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    CREATE_ACCOUNT_BUTTON = By.XPATH, "//button[contains(@class, 'style_link') and text()='Создать аккаунт']"
    NAME_INPUT_FIELD = By.XPATH, "//input[@name='first_name']"
    LAST_NAME_INPUT_FIELD = By.XPATH, "//input[@name='last_name']"
    USERNAME_INPUT_FIELD = By.XPATH, "//input[@name='username']"
    EMAIL_INPUT = By.XPATH, "//input[@name='email']"
    PASSWORD_INPUT = By.XPATH, "//input[@name='password']"
    CONFIRM_LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'
    CONFIRM_CREATE_ACCOUNT_BUTTON = By.XPATH, "//button[text()='Создать аккаунт']"
    AUTHORIZATION_FORM = By.XPATH, "//form[@class='styles_form__2nwxz styles_form__2_42b']"
    SIGNIN_LINK = By.XPATH, '//a[text()="Войти"]'
    SIGNIN_CONFIRM_BUTTON = By.XPATH, '//button[@class="style_button__1FFWl styles_button__1jD3X style_button_style_dark-blue__1cpq7" and text()="Войти"]'
    LOGOUT_LINK = By.XPATH, '//a[contains(@class, "styles_menuLink") and text()="Выход"]'




