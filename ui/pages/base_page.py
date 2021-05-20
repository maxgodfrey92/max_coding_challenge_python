from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from typing import Optional, Tuple
import time


class BasePage:

    driver: WebDriver

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_element_visible(self, locator: Tuple[By, str], timeout: int = 20):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element_located(locator))

    @staticmethod
    def wait_for_element_visible_in_parent(parent_element: WebElement, locator: Tuple[By, str], timeout: int = 20):
        element: Optional[WebElement] = None
        for i in range(timeout + 1):
            assert i != timeout, f"Waited for {timeout} seconds for element with locator {locator}"
            try:
                element = parent_element.find_element(*locator)
                break
            except (NoSuchElementException, ElementNotVisibleException):
                time.sleep(1)
        return element

    def scroll_into_view(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
