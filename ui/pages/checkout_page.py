from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple
from ui.locators import checkout_locators
from ui.pages.base_page import BasePage


class CheckoutPage(BasePage):

    def get_price(self, price_locator: Tuple[By, str]):
        price_element: WebElement = self.wait_for_element_visible(price_locator)
        return float(price_element.text.strip("$"))

    def get_total_product_price(self):
        return self.get_price(checkout_locators.TOTAL_PRODUCT_PRICE)

    def get_shipping_price(self):
        return self.get_price(checkout_locators.SHIPPING_PRICE)

    def get_total_price(self):
        return self.get_price(checkout_locators.TOTAL_PRICE)
