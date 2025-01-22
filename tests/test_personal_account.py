import allure
import time
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage
from config import USER_EMAIL, USER_PASSWORD
from locators.main_page_locators import MainPageLocators
from locators.constructor_locators import ConstructorLocators

@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.title("Личный кабинет, создание заказа и проверка истории заказов")
    def test_personal_account_order_history(self, driver):
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
        time.sleep(2)
        constructor_page.click_order_button()
        time.sleep(2)
        constructor_page.click_to_element(ConstructorLocators.CLOSE_ORDER_MODAL_BUTTON)
        time.sleep(2)

        personal_account_page.go_to_personal_account()
        personal_account_page.go_to_order_history()
        assert personal_account_page.is_order_present_in_history()


