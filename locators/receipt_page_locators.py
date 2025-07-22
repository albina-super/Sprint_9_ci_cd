from selenium.webdriver.common.by import By


class ReceiptPageLocators:
    CREATE_RECEIPT_LINK = By.XPATH, '//a[contains(@href, "/recipes/create")]'
