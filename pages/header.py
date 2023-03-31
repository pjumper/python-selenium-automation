from pages.base_page import Page

class Header(Page):

    AMAZON_SEARCH = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_FIELD_SELECT = (By.CSS_SELECTOR, '#nav-search-submit-button')

    def input_search_text(self, text):
        self.input_text('coffee', *self.AMAZON_SEARCH)

    def click_search(self, *locator):
        self.click(*self.SEARCH_FIELD_SELECT)