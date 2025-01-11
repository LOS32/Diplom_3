from selenium.webdriver.common.by import By

# Локаторы для страницы Личного кабинета
class PersonalAccountLocators:
    LOGIN_NAME_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_NAME_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON_MAIN_FORM = (By.XPATH, "//button[contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']")
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@href='/account/order-history']")
    ORDER_HISTORY_ITEM = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]")

# Локаторы для страницы восстановления пароля
class PasswordRecoveryLocators:
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/forgot-password']")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")

