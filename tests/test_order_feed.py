import allure
from pages.main_page import MainPage
from locators.constructor_locators import ConstructorLocators
from config import USER_EMAIL, USER_PASSWORD
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Открытие всплывающего окна с деталями заказа")
    def test_order_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_feed_button()
        order = main_page.find_order_in_feed()
        order.click()
        assert main_page.find_element_with_wait(ConstructorLocators.COMPOSITION_LOCATOR).is_displayed()

    @allure.title("Заказы из Истории заказов отображаются в Ленте заказов")
    def test_order_in_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.go_to_personal_account()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email(USER_EMAIL)
        personal_account_page.enter_password(USER_PASSWORD)
        personal_account_page.click_login_button()
        constructor_page = ConstructorPage(driver)
        bun = main_page.get_buns_tab()
        basket = main_page.get_basket()
        constructor_page.drag_and_drop_element(bun, basket)
        constructor_page.click_order_button()
        order_number = constructor_page.get_order_id()
        constructor_page.close_order_modal()
        main_page.click_feed_button()
        order = main_page.get_order_element()
        order.click()
        order_feed_element = main_page.get_specific_order_element()
        order_feed_number = order_feed_element.text.strip()
        assert order_feed_number == order_number

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_order_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.go_to_personal_account()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email(USER_EMAIL)
        personal_account_page.enter_password(USER_PASSWORD)
        personal_account_page.click_login_button()
        constructor_page = ConstructorPage(driver)
        bun = main_page.get_buns_tab()
        basket = main_page.get_basket()
        constructor_page.drag_and_drop_element(bun, basket)
        constructor_page.click_order_button()
        order_number = constructor_page.get_order_id()
        constructor_page.close_order_modal()
        main_page.click_feed_button()
        order_feed_element = main_page.get_specific_order_element()
        order_feed_number = order_feed_element.text.strip()
        assert order_feed_number == order_number

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_in_progress(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.go_to_personal_account()
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
        main_page.click_feed_button()
        in_progress_element = main_page.get_in_progress()
        assert in_progress_element.is_displayed()
