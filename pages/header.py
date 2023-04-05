from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):

    AMAZON_SEARCH = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_FIELD_SELECT = (By.CSS_SELECTOR, '#nav-search-submit-button')
    CLICK_ORDER_BUTTON = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")
    ADD_T0_CART = (By.CSS_SELECTOR, '#add-to-cart-button')
    CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')
    OPEN_CART = (By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=sw_gtc']")
    LANG_OPTIONS = (By.ID, '#icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_SELECTION = (By.ID, '#searchDropdownBox')
    NEW_ARRIVAL = (By.CSS_SELECTOR, "a[href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")
    NEW_ARRIVAL_DISPLAY =(By.CSS_SELECTOR, )

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

    def hover_lang_options(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_lang_shown(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self, alias):
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value(f'search-alias=[alias]')

    def hover_new_arrival(self):
        new_arrival = self.find_element(*self.NEW_ARRIVAL)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrival)
        actions.perform()

    def verify_new_arrival_shown(self):
        self.wait_for_element_appear(*self.NEW_ARRIVAL_DISPLAY)