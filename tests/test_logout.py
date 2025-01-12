import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from config import USER_EMAIL, USER_PASSWORD

@allure.feature("Выход из аккаунта")
class TestLogout:
    @allure.story("Проверка выхода из аккаунта")
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_login_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.enter_email(USER_EMAIL)
        personal_account_page.enter_password(USER_PASSWORD)
        personal_account_page.click_login_button()
        personal_account_page.go_to_personal_account()
        personal_account_page.logout()
        assert main_page.is_login_button_visible()
