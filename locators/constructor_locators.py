from selenium.webdriver.common.by import By

class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")
    BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    CLOSE_ORDER_MODAL_BUTTON = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
    ORDER_STATUS_LOCATOR = (By.XPATH, "//p[contains(@class, 'text_type_main-small') and text()='Ваш заказ начали готовить']")
    COMPOSITION_LOCATOR = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='Cостав']")
    ORDER_LOCATOR = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")
    ORDER_NUMBER_LOCATOR = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m') and contains(@class, 'text_type_digits-large')]")
    ORDER_HISTORY_LOCATOR = (By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ') and text()='История заказов']")
    HISTORY_ORDER_NUMBER_LOCATOR_TEMPLATE = "//p[contains(@class, 'text_type_digits-default') and text()='#{order_number}']"
    SPECIFIC_ORDER_LOCATOR = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')]")
