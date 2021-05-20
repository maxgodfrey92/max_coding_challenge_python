from selenium.webdriver.common.by import By
from typing import Tuple


def format_xpath_locator(locator: Tuple[By, str], format_str: str) -> Tuple[By, str]:
    formatted_str = locator[1].format(format_str)
    return locator[0], formatted_str
