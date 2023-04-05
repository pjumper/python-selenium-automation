from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultPage(Page):

        CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')
        PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price-whole')
        SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")

        def get_subnav_locator(self, category):
                return [self.SUBNAV[0], self.SUBNAV[1].replace('{CATEGORY}',)]

        def verify_cart_count(self, expected_amount, *locator):
                actual_text = self.context.driver.find_element(*self.CART_COUNT).text
                assert expected_amount == actual_text, f'Expected {expected_amount} but got {actual_text}'

        def select_product_price(self, *locator):
                # self.context.driver.wait.until(EC.element_to_be_clickable(*self.PRODUCT_PRICE)).click()
                self.wait_for_element_click(*self.PRODUCT_PRICE)

        def verify_selected_dept(self, category):
                locator = self.get_subnav_locator(category)
                self.wait_for_element_appear(*self.SUBNAV)

