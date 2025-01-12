from locators.main_page_locators import MainPageLocators
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

    def is_element_visible(self, locator):
        return self.find_element_with_wait(locator).is_displayed()

