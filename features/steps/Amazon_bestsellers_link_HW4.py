from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_BESTSELLER_LINK = By.CSS_SELECTOR, "div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li']"


@given('Open Amazon page')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then ('Verify bestseller has {expected_amount} links')
def verify_bestseller_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    bestseller_links = context.driver.find_element(AMAZON_BESTSELLER_LINK)
    assert len(bestseller_links) == expected_amount f'Expected {expected_amount} links but got {len(bestseller_links)}'
