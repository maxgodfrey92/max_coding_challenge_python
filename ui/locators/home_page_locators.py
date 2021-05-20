from typing import Tuple
from selenium.webdriver.common.by import By

SEARCH_BAR: Tuple[By, str] = (By.ID, "search_query_top")
SEARCH_BUTTON: Tuple[By, str] = (By.XPATH, "//button[@name='submit_search']")
