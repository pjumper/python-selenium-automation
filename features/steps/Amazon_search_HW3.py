from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon_bestseller(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when ('Click on cart icon')
def select_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon').click()


@then ('Verify Amazon Cart is empty')
def verify_cart(context):
    cart = context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-count.nav-cart-0')
    assert cart, f"Cart is not zero"
