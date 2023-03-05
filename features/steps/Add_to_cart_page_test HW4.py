from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_SEARCH = (By.CSS_SELECTOR, '#twotabsearchtextbox')
SEARCH_FIELD_SELECT = (By.CSS_SELECTOR, '#nav-search-submit-button')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price-whole')
CART_ICON = (By.CSS_SELECTOR, '#add-to-cart-button')
OPEN_CART = (By.CSS_SELECTOR,"a[href='/gp/cart/view.html?ref_=sw_gtc']")
CART = (By.CSS_SELECTOR, '#nav-cart-count')


#@given('Open Amazon page_1')
#def open_amazon_page(context):
#    context.driver.get('https://www.amazon.com/')


@when('Input this text {text}')
def input_search_field(context, text):
    context.driver.find_element(*AMAZON_SEARCH).send_keys(text)



@when('Click on search button')
def click_search_field(context):
    context.driver.find_element(*SEARCH_FIELD_SELECT).click()


@when('Click on product')
def click_product_price(context):
    context.driver.find_element(*PRODUCT_PRICE).click()

@when('Click on cart')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()



@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*OPEN_CART).click()


@then('Verify cart has {expected_amount} item(s)')
def verify_cart_amount(context, expected_amount):
    actual_text = context.driver.find_element(*CART).text
    assert expected_amount == actual_text, f'Expected {expected_amount} but got {actual_text}'


