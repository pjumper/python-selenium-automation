from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_result_page = SearchResultPage(self.driver)