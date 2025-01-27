from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    # Кнопка "Восстановить пароль"
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/forgot-password']")
    # Поле Email
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    # Кнопка "Восстановить"
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # Кнопка "Показать/Скрыть пароль"
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")

