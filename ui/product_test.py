from ui.pages.checkout_page import CheckoutPage
from ui.pages.home_page import HomePage
from ui.pages.search_results_page import SearchResultsPage


def test_add_product_to_cart(driver):
    product_name: str = "Printed Chiffon Dress"
    home_page: HomePage = HomePage(driver)
    home_page.navigate_to()
    home_page.perform_search(product_name)

    search_results_page: SearchResultsPage = SearchResultsPage(driver)
    search_results_page.add_product_to_cart_and_checkout(product_name)
    exp_product_price: float = search_results_page.running_price

    checkout_page: CheckoutPage = CheckoutPage(driver)
    act_product_price: float = checkout_page.get_total_product_price()
    act_shipping_price: float = checkout_page.get_shipping_price()
    act_total_price: float = checkout_page.get_total_price()

    assert exp_product_price == act_product_price
    assert act_product_price + act_shipping_price == act_total_price
