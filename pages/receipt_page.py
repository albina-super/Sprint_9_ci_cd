from locators.receipt_page_locators import ReceiptPageLocators
from pages.base_page import BasePage
from pathlib import Path
from allure import step


class ReceiptPage(BasePage):

    @step('создаем рецепт')
    def create_receipt(self, data):
        self.click_to_element(ReceiptPageLocators.CREATE_RECEIPT_LINK)
        self.add_text_to_element(ReceiptPageLocators.TITLE_RECEIPT_INPUT, data['title'])
        self.select_first_element(data['ingredient'],ReceiptPageLocators.INGREDIENT_INPUT, ReceiptPageLocators.DIV_INGREDIENT_PARENT, ReceiptPageLocators.DIV_INGREDIENT_CHILD)
        self.add_text_to_element(ReceiptPageLocators.QTY_INGREDIENTS_INPUT, data['qty'])
        self.click_to_element(ReceiptPageLocators.ADD_INGREDIENT)
        self.add_text_to_element(ReceiptPageLocators.TIME_INPUT, data['time'])
        self.add_text_to_element(ReceiptPageLocators.DESCRIPTION_INPUT, data['description'])
        APP_DIR = Path(__file__).parent.parent
        file_path = APP_DIR/"images"/"food.jpg"
        self.upload_file(ReceiptPageLocators.PICTURE_FIELD, file_path)
        self.click_to_element(ReceiptPageLocators.CREATE_RECEIPT_CONFIRM_BUTTON)

    @step('проверяем что рецепт успешно создался')
    def check_create_receipt(self, data):
        title = self.get_actual_text(ReceiptPageLocators.RECEIPT_TITLE_HEADER, data['title'])
        card = self.find_element_with_wait(ReceiptPageLocators.RECEIPT_CARD)
        return title, card

