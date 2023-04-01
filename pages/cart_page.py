from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class CartPage(Page):

    CART_COUNT_ZERO = (By.CSS_SELECTOR, 'span.nav-cart-count.nav-cart-0')

    def verify_empty_cart(self, *locator):
        cart = self.context.driver.find_element(*self.CART_COUNT_ZERO)
        assert cart, f"Cart is not zero"