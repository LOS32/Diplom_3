from locators.main_page_locators import MainPageLocators
from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
from config import BASE_URL

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open_page(BASE_URL)

    def click_login_button(self):
        self.click_to_element(MainPageLocators.LOGIN_BUTTON)

    def is_login_button_visible(self):
        return self.find_element_with_wait(MainPageLocators.LOGIN_BUTTON_MAIN_FORM).is_displayed()

    def click_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def get_buns_tab(self):
        return self.find_element_with_wait(MainPageLocators.BUNS_TAB)

    def get_basket(self):
        return self.find_element_with_wait(MainPageLocators.BASKET)

    def find_order_in_feed(self):
        return self.find_element_with_wait(ConstructorLocators.ORDER_LOCATOR)

    def get_order_element(self):
        return self.find_element_with_wait(ConstructorLocators.ORDER_LOCATOR)

    def get_specific_order_element(self):
        return self.find_element_with_wait(ConstructorLocators.SPECIFIC_ORDER_LOCATOR)

    def go_to_personal_account(self):
        self.click_to_element(MainPageLocators.ACCOUNT_BUTTON)

    def click_feed_button(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_buns_tab(self):
        self.click_to_element(MainPageLocators.BUNS_TAB)

    def close_order_modal_button(self):
        self.click_to_element(MainPageLocators.BUNS_TAB)

    def get_in_progress(self):
        return self.find_element_with_wait(ConstructorLocators.IN_PROGRESS)






