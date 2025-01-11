from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def drag_and_drop_bun(self):
        bun = self.find_element_with_wait(ConstructorLocators.BUNS_TAB)
        basket = self.find_element_with_wait(ConstructorLocators.BASKET)
        self.drag_and_drop_element(bun, basket)

    def click_order_button(self):
        self.click_to_element(ConstructorLocators.ORDER_BUTTON)

    def close_order_modal(self):
        self.click_to_element(ConstructorLocators.CLOSE_ORDER_MODAL_BUTTON)