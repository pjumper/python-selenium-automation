from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultPage(Page):

    CART_COUNT_ZERO = (By.CSS_SELECTOR, 'span.nav-cart-count.nav-cart-0')

    def verify_page_opened(self,):
        context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin?_encoding=UTF8&accountStatusPolicy='))

    def verify_empty_cart(self, *locator):
        cart = context.driver.find_element(*self.CART_COUNT_ZERO)
        assert cart, f"Cart is not zero"
    def verify_search_result(self, expected_text, *locator):
        pass