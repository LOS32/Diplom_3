from selenium.webdriver.common.by import By

class ConstructorLocators:
    # Булка в списке ингредиентов
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")
    # Корзина для заказа
    BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")
    # Кнопка "Оформить заказ"
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    CLOSE_ORDER_MODAL_BUTTON = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
