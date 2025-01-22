import allure
from pages.main_page import MainPage
from locators.constructor_locators import ConstructorLocators
from locators.main_page_locators import MainPageLocators
from config import USER_EMAIL, USER_PASSWORD
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Открытие всплывающего окна с деталями заказа")
    def test_order_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON))
        main_page.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(ConstructorLocators.ORDER_LOCATOR))
        order = main_page.find_element_with_wait(ConstructorLocators.ORDER_LOCATOR)
        order.click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(ConstructorLocators.COMPOSITION_LOCATOR))
        assert main_page.find_element_with_wait(ConstructorLocators.COMPOSITION_LOCATOR).is_displayed()

    @allure.title("Заказы из Истории заказов отображаются в Ленте заказов")
    def test_order_in_feed(self, driver):
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
        order_number = constructor_page.get_order_id()
        constructor_page.close_order_modal()
        main_page.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        order = main_page.find_element_with_wait(ConstructorLocators.ORDER_LOCATOR)
        order.click()
        order_feed_element = main_page.find_element_with_wait(ConstructorLocators.SPECIFIC_ORDER_LOCATOR)
        order_feed_number = order_feed_element.text.strip()
        assert order_feed_number == order_number

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_order_counter(self, driver):
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
        order_number = constructor_page.get_order_id()
        constructor_page.close_order_modal()
        main_page.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        order_feed_element = personal_account_page.find_element_with_wait(ConstructorLocators.SPECIFIC_ORDER_LOCATOR)
        order_feed_number = order_feed_element.text.strip()
        assert order_feed_number == order_number

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_in_progress(self, driver):
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
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(ConstructorLocators.ORDER_BUTTON))
        constructor_page.click_order_button()
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(ConstructorLocators.CLOSE_ORDER_MODAL_BUTTON))
        constructor_page.close_order_modal()
        main_page.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        in_progress_element = main_page.find_element_with_wait(ConstructorLocators.IN_PROGRESS)
        assert in_progress_element.is_displayed(), "Раздел 'В работе' не отображается!"
