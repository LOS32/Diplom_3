from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_button(self):
        self.click_to_element(ConstructorLocators.ORDER_BUTTON)

    def close_order_modal(self):
        if self.get_text_from_element(ConstructorLocators.ORDER_NUMBER_LOCATOR) == '9999':
            self.wait_change_value_in_element_page(ConstructorLocators.ORDER_NUMBER_LOCATOR, '9999')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ConstructorLocators.CLOSE_ORDER_MODAL_BUTTON))
        self.click_to_element(ConstructorLocators.CLOSE_ORDER_MODAL_BUTTON)

