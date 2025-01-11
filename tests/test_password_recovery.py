import allure
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage
from config import TEST_EMAIL

@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.story("Проверка восстановления пароля")
    def test_password_recovery(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_login_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.go_to_password_recovery_page()
        password_recovery_page.enter_email(TEST_EMAIL)
        password_recovery_page.click_restore_button()
        password_recovery_page.click_show_password_button()
        assert password_recovery_page.is_password_visible(), "Поле Пароль не изменило тип на 'text'!"


