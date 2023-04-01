from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):

    AMAZON_SEARCH = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_FIELD_SELECT = (By.CSS_SELECTOR, '#nav-search-submit-button')
    CLICK_ORDER_BUTTON = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH)

    def click_search(self, *locator):
        self.click(*self.SEARCH_FIELD_SELECT)

    def click_button(self, *locator):
        self.click(*self.CLICK_ORDER_BUTTON)