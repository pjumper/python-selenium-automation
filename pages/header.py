from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class Header(Page):

    AMAZON_SEARCH = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_FIELD_SELECT = (By.CSS_SELECTOR, '#nav-search-submit-button')
    CLICK_ORDER_BUTTON = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")
    ADD_T0_CART = (By.CSS_SELECTOR, '#add-to-cart-button')
    CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')
    OPEN_CART = (By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=sw_gtc']")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH)

    def click_search(self, *locator):
        self.click(*self.SEARCH_FIELD_SELECT)

    def click_button(self, *locator):
        self.click(*self.CLICK_ORDER_BUTTON)

    def click_cart(self, *locator):
        self.click(*self.CART_COUNT)




    def add_cart(self):
        #self.context.driver.wait.until(EC.element_to_be_clickable(*self.ADD_T0_CART)).click()
        self.wait_for_element_click(*self.ADD_T0_CART)


    def open_cart(self):
        #self.context.driver.wait.until(EC.element_to_be_clickable(*self.OPEN_CART)).click()
        self.wait_for_element_click(*self.OPEN_CART)