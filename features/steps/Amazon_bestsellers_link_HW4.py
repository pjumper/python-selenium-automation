from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_BESTSELLER_LINKS = (By.CSS_SELECTOR, "div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li']")
BESTSELLER_TAB = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")


@given('Open Amazon page_1')
def open_amazon_bestseller_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify bestseller has {expected_amount} links')
def verify_bestseller_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    bestseller_links = context.driver.find_elements(*AMAZON_BESTSELLER_LINKS)
    assert len(bestseller_links) == expected_amount, f'Expected {expected_amount} links but got {len(bestseller_links)}'
