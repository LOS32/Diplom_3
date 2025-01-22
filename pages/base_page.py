from locators.constructor_locators import ConstructorLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            element = self.driver.find_element(*locator)
            element.click()
        except ElementClickInterceptedException:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def wait_for_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)

    def wait_for_url_contains(self, url_substring, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_substring))

    def drag_and_drop_element(self, source_element, target_element):
        browser_name = self.driver.capabilities['browserName']
        if browser_name == "chrome":
            action = ActionChains(self.driver)
            action.drag_and_drop(source_element, target_element).perform()
        elif browser_name == "firefox":
            self.driver.execute_script(
                """
                const dataTransfer = new DataTransfer();
                arguments[0].dispatchEvent(new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer }));
                arguments[1].dispatchEvent(new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer }));
                """,
                source_element,
                target_element,
            )

    def wait_change_value_in_element_page(self, locator, old_value, timeout=20):
        """Ожидание, пока значение элемента изменится с указанного."""
        WebDriverWait(self.driver, timeout).until(lambda driver: self.get_text_from_element(locator) != old_value)

    def get_order_id(self):
        if self.get_text_from_element(ConstructorLocators.ORDER_NUMBER_LOCATOR) == '9999':
            self.wait_change_value_in_element_page(ConstructorLocators.ORDER_NUMBER_LOCATOR, '9999')
            self.id = self.get_text_from_element(ConstructorLocators.ORDER_NUMBER_LOCATOR)
        else:
            self.id = self.get_text_from_element(ConstructorLocators.ORDER_NUMBER_LOCATOR)
        return self.id








