from selenium.webdriver.common.by import By

class ConstructorLocators():
    # Локатор для вкладки "Булки" в списке ингредиентов конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")
    # Локатор для корзины заказа, куда нужно перетащить булочку
    BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")
    # Кнопка "Оформить заказ"
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Кнопка для закрытия модального окна с номером заказа
    CLOSE_ORDER_MODAL_BUTTON = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
    # Сообщение о статусе заказа "Ваш заказ начали готовить"
    ORDER_STATUS_LOCATOR = (By.XPATH, "//p[contains(@class, 'text_type_main-small') and text()='Ваш заказ начали готовить']")
    # Заголовок раздела "Состав" в модальном окне с деталями заказа
    COMPOSITION_LOCATOR = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='Cостав']")
    # Локатор для номера заказа в Ленте заказов
    ORDER_LOCATOR = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")
    # Локатор для номера заказа в модальном окне после оформления
    ORDER_NUMBER_LOCATOR = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'Modal_modal__title__2L34m')]")
    # Локатор для кнопки "История заказов" в Личном кабинете
    ORDER_HISTORY_LOCATOR = (By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ') and text()='История заказов']")
    # Локатор для поиска конкретного номера заказа в Истории заказов
    HISTORY_ORDER_NUMBER_LOCATOR_TEMPLATE = (By.XPATH, "//p[contains(@class, 'text_type_digits-default') and text()='#{order_number}']")
    # Локатор для номера заказа в Ленте заказов
    SPECIFIC_ORDER_LOCATOR = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')]")
    #
    IN_PROGRESS = (By.XPATH, "//li[contains(@class, 'text_type_main-small') and text()='Все текущие заказы готовы!']")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")
