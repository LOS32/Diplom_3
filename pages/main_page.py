from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from config import BASE_URL  # Исправили импорт

# Класс для работы с главной страницей
class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open_page(BASE_URL)

    def click_login_button(self):
        self.click_to_element(MainPageLocators.LOGIN_BUTTON)

