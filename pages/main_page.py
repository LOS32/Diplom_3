from locators.main_page_locators import MainPageLocators
from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
from config import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open_page(BASE_URL)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON))

    def click_login_button(self):
        self.click_to_element(MainPageLocators.LOGIN_BUTTON)

    def is_login_button_visible(self):
        return self.find_element_with_wait(MainPageLocators.LOGIN_BUTTON_MAIN_FORM).is_displayed()

    def click_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def get_buns_tab(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.BUNS_TAB))
        return self.find_element_with_wait(MainPageLocators.BUNS_TAB)

    def get_basket(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.BASKET))
        return self.find_element_with_wait(MainPageLocators.BASKET)

    def find_order_in_feed(self):
        return self.find_element_with_wait(ConstructorLocators.ORDER_LOCATOR)

    def get_bun_tab(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(MainPageLocators.BUNS_TAB))
        return self.driver.find_element(*MainPageLocators.BUNS_TAB)

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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ConstructorLocators.IN_PROGRESS))
        return self.find_element_with_wait(ConstructorLocators.IN_PROGRESS)






