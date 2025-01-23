import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage
from config import USER_EMAIL, USER_PASSWORD
from locators.constructor_locators import ConstructorLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title("Переход на страницу конструктора")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_element(MainPageLocators.ACCOUNT_BUTTON)
        main_page.click_constructor_button()
        assert main_page.is_element_visible(MainPageLocators.BUNS_SECTION)

    @allure.title("Переход на страницу Лента заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_FEED_BUTTON))
        main_page.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_FEED_HEADER))
        assert main_page.is_element_visible(MainPageLocators.ORDER_FEED_HEADER)

    @allure.title("Появление всплывающего окна с деталями ингредиента")
    def test_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_element(MainPageLocators.BUNS_TAB)
        assert main_page.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    @allure.title("Закрытие всплывающего окна с деталями ингредиента")
    def test_close_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_element(MainPageLocators.BUNS_TAB)
        main_page.click_to_element(MainPageLocators.CLOSE_ORDER_MODAL_BUTTON)
        assert main_page.is_element_visible(MainPageLocators.BUNS_TAB)

    @allure.title("Увеличение каунтера ингредиента")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        assert main_page.is_element_visible(MainPageLocators.COUNTER_ZERO)
        bun = main_page.find_element_with_wait(MainPageLocators.BUNS_TAB)
        basket = main_page.find_element_with_wait(MainPageLocators.BASKET)
        main_page.drag_and_drop_element(bun, basket)
        assert main_page.is_element_visible(MainPageLocators.COUNTER_TWO)

    @allure.title("Оформление заказа залогиненным пользователем")
    def test_logged_in_user_can_place_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_to_element(MainPageLocators.ACCOUNT_BUTTON)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email(USER_EMAIL)
        personal_account_page.enter_password(USER_PASSWORD)
        personal_account_page.click_login_button()
        constructor_page = ConstructorPage(driver)
        bun = main_page.find_element_with_wait(MainPageLocators.BUNS_TAB)
        basket = main_page.find_element_with_wait(MainPageLocators.BASKET)
        constructor_page.drag_and_drop_element(bun, basket)
        constructor_page.click_order_button()
        assert constructor_page.find_element_with_wait(ConstructorLocators.ORDER_STATUS_LOCATOR).is_displayed()

