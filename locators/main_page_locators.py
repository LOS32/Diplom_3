from selenium.webdriver.common.by import By

# Локаторы для главной страницы
class MainPageLocators:
    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, "//a[@href='/']")
    # Секция "Булки" в конструкторе
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
