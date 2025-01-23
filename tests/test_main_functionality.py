import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage
from config import USER_EMAIL, USER_PASSWORD
from locators.constructor_locators import ConstructorLocators

@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title("Переход на страницу конструктора")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.go_to_personal_account()
        main_page.click_constructor_button()
        assert main_page.is_element_visible(MainPageLocators.BUNS_SECTION)

    @allure.title("Переход на страницу Лента заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_feed_button()
        assert main_page.is_element_visible(MainPageLocators.ORDER_FEED_HEADER)

    @allure.title("Появление всплывающего окна с деталями ингредиента")
    def test_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_buns_tab()
        assert main_page.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    @allure.title("Закрытие всплывающего окна с деталями ингредиента")
    def test_close_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_buns_tab()
        main_page.close_order_modal_button()
        assert main_page.is_element_visible(MainPageLocators.BUNS_TAB)

    @allure.title("Увеличение каунтера ингредиента")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        assert main_page.is_element_visible(MainPageLocators.COUNTER_ZERO)
        bun = main_page.get_buns_tab()
        basket = main_page.get_basket()
        main_page.drag_and_drop_element(bun, basket)
        assert main_page.is_element_visible(MainPageLocators.COUNTER_TWO)

    @allure.title("Оформление заказа залогиненным пользователем")
    def test_logged_in_user_can_place_order(self, driver):
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
        assert constructor_page.find_element_with_wait(ConstructorLocators.ORDER_STATUS_LOCATOR).is_displayed()

