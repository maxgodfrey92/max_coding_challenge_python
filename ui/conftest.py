from selenium.webdriver.remote.webdriver import WebDriver
from ui.utils.driver_utils import start_driver
import pytest


@pytest.fixture
def driver() -> WebDriver:
    driver = start_driver()
    yield driver
    driver.quit()
