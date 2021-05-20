from selenium.webdriver.remote.webelement import WebElement
from ui.locators import home_page_locators
from ui.pages.base_page import BasePage
import config


class HomePage(BasePage):

    def navigate_to(self):
        self.driver.get(config.UI_URL)

    def perform_search(self, search_term):
        search_bar: WebElement = self.wait_for_element_visible(home_page_locators.SEARCH_BAR)
        search_bar.send_keys(search_term)
        self.wait_for_element_visible(home_page_locators.SEARCH_BUTTON).click()
