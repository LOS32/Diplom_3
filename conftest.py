import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера: chrome или firefox")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Браузер '{browser}' не поддерживается")
    yield driver
    driver.quit()
