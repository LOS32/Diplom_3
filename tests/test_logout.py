import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from config import USER_EMAIL, USER_PASSWORD

@allure.feature("Выход из аккаунта")
class TestLogout:
    @allure.story("Проверка выхода из аккаунта")
    def test_logout(self, driver):
        # Шаг 1: Открываем главную страницу
        main_page = MainPage(driver)
        main_page.open_main_page()

        # Шаг 2: Кликаем по кнопке "Войти в аккаунт"
        main_page.click_login_button()

        # Шаг 3: Вводим почту и пароль
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email(USER_EMAIL)
        personal_account_page.enter_password(USER_PASSWORD)
        personal_account_page.click_login_button()

        # Шаг 4: Переходим в Личный кабинет
        personal_account_page.go_to_personal_account()

        # Шаг 5: Выходим из аккаунта
        personal_account_page.logout()

        # Шаг 6: Проверяем наличие кнопки "Войти"
        assert main_page.is_login_button_visible(), "Кнопка 'Войти' не отображается после выхода из аккаунта!"
