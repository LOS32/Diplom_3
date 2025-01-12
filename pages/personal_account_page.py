from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_personal_account(self):
        self.click_to_element(PersonalAccountLocators.ACCOUNT_BUTTON)

    def check_logout_button_visibility(self):
        return self.wait_for_element_visible(PersonalAccountLocators.LOGOUT_BUTTON).is_displayed()

    def logout(self):
        self.click_to_element(PersonalAccountLocators.LOGOUT_BUTTON)

    def enter_email(self, email):
        self.add_text_to_element(PersonalAccountLocators.LOGIN_NAME_FIELD, email)

    def enter_password(self, password):
        self.add_text_to_element(PersonalAccountLocators.PASSWORD_NAME_FIELD, password)

    def click_login_button(self):
        self.click_to_element(PersonalAccountLocators.LOGIN_BUTTON_MAIN_FORM)

    def go_to_order_history(self):
        self.click_to_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    def is_order_present_in_history(self):
        return self.find_element_with_wait(PersonalAccountLocators.ORDER_HISTORY_ITEM).is_displayed()
