from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon_page(context):
    context.app.main_page.open_main()

@given('Open Amazon Fashion page')
def open_amazon_fashion_page(context):
    context.app.main_page.open_amazon_fashion()

@when ('Click Amazon Orders Link')
def click_orders_link(context):
    context.app.header.click_orders_link()


@when ('Click on cart icon')
def select_cart(context):
    context.app.header.click_cart()


@then ('Verify Sign In page is opened')
def verify_Sign_In(context):
    context.app.sign_in_page.verify_page_opened()



@then ('Verify Amazon Cart is empty')
def verify_cart(context):
    cart = context.app.cart_page.verify_empty_cart
    assert cart, f"Cart is not zero"


@then ('Verify {category} department is selected')
def verify_selected_dept(context, category):
    context.app.search_result_page.verify_selected_dept(category)

