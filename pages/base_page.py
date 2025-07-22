from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, timeout=15).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_element(*locator)


    def press_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()


    def click_to_element(self, locator):
        WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()


    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)


    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text


    def get_actual_text(self, locator, title):
        WebDriverWait(self.driver, timeout=30).until(
            EC.text_to_be_present_in_element(locator, title)
        )
        return self.driver.find_element(*locator).text


    def get_class_from_element(self, locator):
        return self.find_element_with_wait(locator).get_attribute("class")


    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)


    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def get_current_url(self):
        initial_url = self.driver.current_url
        WebDriverWait(self.driver, timeout=13).until(
            lambda driver: driver.current_url != initial_url
        )
        return self.driver.current_url


    def select_first_element(self, text, input_locator, div_locator, child_locator):
        wait = WebDriverWait(self.driver, timeout=10)

        input_field = wait.until(EC.presence_of_element_located((
            input_locator
        )))
        input_field.clear()
        input_field.send_keys(text)

        wait.until(EC.presence_of_element_located((
           div_locator
        )))

        first_option = wait.until(EC.element_to_be_clickable((
            child_locator        )))
        first_option.click()


    def upload_file(self, locator, file_path):
        wait = WebDriverWait(self.driver, 10)

        file_input = wait.until(EC.presence_of_element_located(
            locator
        ))

        file_input.send_keys(str(file_path.resolve()))