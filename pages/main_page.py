from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    ADD_T0_CART = (By.CSS_SELECTOR, '#add-to-cart-button')
    CLICK_CART = (By.CSS_SELECTOR, '#nav-cart-count')

    def open_main(self, url):
        self.open_url('https://www.amazon.com/')

    def click_cart(self, *locator):
        self.click(*self.CLICK_CART)

