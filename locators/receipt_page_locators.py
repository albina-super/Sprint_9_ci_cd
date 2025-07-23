from selenium.webdriver.common.by import By


class ReceiptPageLocators:
    CREATE_RECEIPT_LINK = By.XPATH, '//a[contains(@href, "/recipes/create")]'
    TITLE_RECEIPT_INPUT =  By.XPATH, "//label[.//div[text()='Название рецепта']]/input"
    INGREDIENT_INPUT =  By.XPATH, "//label[.//div[text()='Ингредиенты']]/input"
    DIV_INGREDIENT_PARENT = By.CLASS_NAME, 'styles_container__3ukwm'
    DIV_INGREDIENT_CHILD = By.CSS_SELECTOR, '.styles_container__3ukwm > div'
    QTY_INGREDIENTS_INPUT = By.CSS_SELECTOR, "input.styles_ingredientsAmountValue__2matT"
    TIME_INPUT = By.XPATH, "//label[.//div[text()='Время приготовления']]/input"
    DESCRIPTION_INPUT = By.XPATH, "//label[.//div[text()='Описание рецепта']]//textarea"
    PICTURE_FIELD = By.XPATH, '//input[@type="file"]'
    CHOICE_FILE_BUTTON = By.XPATH, '//div[@class="styles_button__xzu5F" and text()="Выбрать файл"]'
    CREATE_RECEIPT_CONFIRM_BUTTON = By.XPATH, '//button[text()="Создать рецепт"]'
    RECEIPT_TITLE_HEADER = By.XPATH, "//h1[contains(@class, 'single-card__title')]"
    RECEIPT_CARD = By.XPATH,'//div[contains(@class, "styles_single-card__1yTTj")]'
    ADD_INGREDIENT = By.XPATH, '//div[text()="Добавить ингредиент"]'



