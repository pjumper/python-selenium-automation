
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@when('Click product')
def click_product_price(context):
    #context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_PRICE)).click()
    context.app.search_result_page.select_product_price


@when('Click on cart button')
def click_cart_icon(context):
    context.app.header.add_cart

@when('Open cart')
def open_cart_page(context):
    context.app.header.open_cart


@then('Verify cart have {expected_amount} item(s)')
def verify_cart_amount(context, expected_amount):
    context.app.search_result_page.verify_cart_count


