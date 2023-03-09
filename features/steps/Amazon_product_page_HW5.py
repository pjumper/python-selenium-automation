from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SELECT_COLORS = (By.CSS_SELECTOR, '#variation_color_name li')
PRODUCT_COLORS = (By.CSS_SELECTOR, 'span.selection')

@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/J-Ver-Dress-Shirt-Regular-Stretch/dp/{product_id}/')


@then('Verify user can click on colors')
def verify_user_can_select_product_colors(context):
    context.driver.find_element(*SELECT_COLORS).click()

    all_color_options = context.driver.find_elements(*SELECT_COLORS)
    print('All colors:', all_color_options)
    expected_colors = ['Black', 'White', 'Grey', 'Red Wine', 'Blue']

    actual_colors = []
    for color in all_color_options [:5]:
        color.click()
        current_color = context.driver.find_element(*PRODUCT_COLORS).text
        print('Current colors:', current_color)
        actual_colors += [current_color]


    assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'



