from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_password_recovery_page(self):
        self.click_to_element(PasswordRecoveryLocators.RECOVERY_PASSWORD_BUTTON)

    def enter_email(self, email):
        self.add_text_to_element(PasswordRecoveryLocators.EMAIL_FIELD, email)

    def click_restore_button(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(PasswordRecoveryLocators.RESTORE_BUTTON))
        self.click_to_element(PasswordRecoveryLocators.RESTORE_BUTTON)

    def click_show_password_button(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON))
        self.click_to_element(PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON)

    def is_password_visible(self):
        input_type = self.find_element_with_wait(PasswordRecoveryLocators.PASSWORD_FIELD).get_attribute("type")
        return input_type == "text"

