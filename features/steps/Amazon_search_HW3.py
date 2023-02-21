from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when ('Click on cart icon')
def click_cart(context):
    context.driver.get(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()


@then ('Verify Amazon Cart is empty')
def verify_cart(context):
    cart = context.driver.get(By.CSS_SELECTOR, 'span.nav-cart-count.nav-cart-0')
    assert cart, f"Cart is not empty"
    pass
