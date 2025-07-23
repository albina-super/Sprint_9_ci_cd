from data import RECEIPT_DATA
from pages.receipt_page import ReceiptPage
from allure import title


class TestReceiptPage:

    @title('тест на успешное создание логина')
    def test_create_receipt(self, driver, login_user):
        receipt_page = ReceiptPage(driver)
        receipt_page.create_receipt(RECEIPT_DATA)
        title, card = receipt_page.check_create_receipt(RECEIPT_DATA)
        assert title == RECEIPT_DATA['title'] and card.is_displayed()