from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import search_results_locators
from ui.pages.base_page import BasePage
from ui.utils.test_utils import format_xpath_locator


class SearchResultsPage(BasePage):

    running_price: float

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.running_price = 0

    def add_product_to_cart(self, product_name: str):
        product_locator = format_xpath_locator(search_results_locators.PRODUCT_CONTAINER, product_name)
        product_container: WebElement = self.wait_for_element_visible(product_locator)
        self.scroll_into_view(product_container)

        actions: ActionChains = ActionChains(self.driver)
        actions.move_to_element(product_container).perform()

        product_price_str: str = self.wait_for_element_visible_in_parent(product_container, search_results_locators.PRODUCT_PRICE).text
        product_price: float = float(product_price_str.strip("$"))
        self.running_price += product_price

        self.wait_for_element_visible_in_parent(product_container, search_results_locators.PRODUCT_ADD_TO_CART).click()

    def add_product_to_cart_and_checkout(self, product_name: str):
        self.add_product_to_cart(product_name)
        self.wait_for_element_visible(search_results_locators.PROCEED_TO_CHECKOUT).click()
