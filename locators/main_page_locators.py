from selenium.webdriver.common.by import By

# Локаторы для главной страницы
class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, "//a[@href='/']")
    # Секция "Булки" в конструкторе
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    LOGIN_BUTTON_MAIN_FORM = (By.XPATH, "//button[contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']")
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, "li.ml-2 > a")
    ORDER_FEED_HEADER = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and text()='Лента заказов']")
    INGREDIENT_DETAILS_HEADER = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    BUNS_TAB = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    CLOSE_ORDER_MODAL_BUTTON = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
    COUNTER_ZERO = (By.XPATH, "//div[contains(@class, 'counter_counter__ZNLkj')]//p[text()='0']")
    COUNTER_TWO = (By.XPATH, "//p[@class='counter_counter__num__3nue1' and text()='2']")
    BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")

