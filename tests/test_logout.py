import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from config import USER_EMAIL, USER_PASSWORD
from locators.main_page_locators import MainPageLocators
from pages.constructor_page import ConstructorPage

@allure.feature("Выход из аккаунта")
class TestLogout:
    @allure.title("Проверка выхода из аккаунта")
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_login_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email(USER_EMAIL)
        personal_account_page.enter_password(USER_PASSWORD)
        personal_account_page.click_login_button()
        constructor_page = ConstructorPage(driver)
        bun = main_page.find_element_with_wait(MainPageLocators.BUNS_TAB)
        basket = main_page.find_element_with_wait(MainPageLocators.BASKET)
        constructor_page.drag_and_drop_element(bun, basket)
        constructor_page.click_order_button()
        constructor_page.close_order_modal()
        personal_account_page.go_to_personal_account()
        personal_account_page.logout()
        assert main_page.is_login_button_visible()
