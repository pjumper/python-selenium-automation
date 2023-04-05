from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):



    def open_main(self):
        self.open_url('https://www.amazon.com/')

    def open_amazon_fashion(self):
        self.open_url('https://www.amazon.com/gp/product/B074TBCSC8')


