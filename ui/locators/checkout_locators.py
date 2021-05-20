from typing import Tuple
from selenium.webdriver.common.by import By

TOTAL_PRODUCT_PRICE: Tuple[By, str] = (By.ID, "total_product")
SHIPPING_PRICE: Tuple[By, str] = (By.ID, "total_shipping")
TOTAL_PRICE: Tuple[By, str] = (By.ID, "total_price")
