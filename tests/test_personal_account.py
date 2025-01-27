import allure
from pages.main_page import MainPage
from config import USER_EMAIL, USER_PASSWORD
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage


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
        bun = main_page.get_buns_tab()
        basket = main_page.get_basket()
        constructor_page.drag_and_drop_element(bun, basket)
        constructor_page.click_order_button()
        constructor_page.close_order_modal()
        personal_account_page.go_to_personal_account()
        personal_account_page.go_to_order_history()
        assert personal_account_page.is_order_present_in_history()


