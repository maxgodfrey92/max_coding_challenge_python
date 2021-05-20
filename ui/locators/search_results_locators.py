from typing import Tuple
from selenium.webdriver.common.by import By

PRODUCT_CONTAINER: Tuple[By, str] = (By.XPATH, "//div[@class='product-container' and .//a[@title='{0}']]")
PRODUCT_PRICE: Tuple[By, str] = (By.XPATH, "//span[@itemprop='price']")
PRODUCT_ADD_TO_CART: Tuple[By, str] = (By.XPATH, "//a[@title='Add to cart']")
PROCEED_TO_CHECKOUT: Tuple[By, str] = (By.XPATH, "//a[@title='Proceed to checkout']")
