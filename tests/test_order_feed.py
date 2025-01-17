import allure
import time
from pages.main_page import MainPage
from locators.constructor_locators import ConstructorLocators
from locators.main_page_locators import MainPageLocators
from config import USER_EMAIL, USER_PASSWORD
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.story("Открытие всплывающего окна с деталями заказа")
    def test_order_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        time.sleep(2)
        main_page.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        time.sleep(2)
        order = main_page.find_element_with_wait(ConstructorLocators.ORDER_LOCATOR)
        order.click()
        time.sleep(2)
        assert main_page.find_element_with_wait(ConstructorLocators.COMPOSITION_LOCATOR).is_displayed()

    @allure.story("Заказы из Истории заказов отображаются в Ленте заказов")
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
        time.sleep(2)
        constructor_page.click_order_button()
        time.sleep(2)
        order_number_element = constructor_page.find_element_with_wait(ConstructorLocators.ORDER_NUMBER_LOCATOR)
        time.sleep(2)
        order_number = order_number_element.text.strip()
        time.sleep(2)
        constructor_page.click_to_element(ConstructorLocators.CLOSE_ORDER_MODAL_BUTTON)
        time.sleep(2)
        main_page.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

        # Находим и кликаем на заказ в Ленте заказов
        order = main_page.find_element_with_wait(ConstructorLocators.ORDER_LOCATOR)
        order.click()
        time.sleep(2)

        # Проверяем, что номер заказа совпадает
        order_feed_element = main_page.find_element_with_wait(ConstructorLocators.SPECIFIC_ORDER_LOCATOR)
        order_feed_number = order_feed_element.text.strip()
        assert order_feed_number == order_number

    @allure.story("При создании нового заказа счётчик Выполнено за всё время увеличивается")
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
        time.sleep(2)
        constructor_page.click_order_button()
        time.sleep(2)
        order_number_element = constructor_page.find_element_with_wait(ConstructorLocators.ORDER_NUMBER_LOCATOR)
        time.sleep(2)
        order_number = order_number_element.text.strip()
        time.sleep(2)
        constructor_page.click_to_element(ConstructorLocators.CLOSE_ORDER_MODAL_BUTTON)
        time.sleep(2)
        main_page.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        order_feed_number_locator = (ConstructorLocators.SPECIFIC_ORDER_LOCATOR)
        order_feed_element = personal_account_page.find_element_with_wait(order_feed_number_locator)
        order_feed_number = order_feed_element.text.strip()
        assert order_feed_number == order_number