from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_button(self):
        self.click_to_element(ConstructorLocators.ORDER_BUTTON)

    def close_order_modal(self):
        self.click_to_element(ConstructorLocators.CLOSE_ORDER_MODAL_BUTTON)
