from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BESTSELLER_LINKS = (By.CSS_SELECTOR, "div[class*='_p13n-zg-nav-tab-all_style_zg-tabs-li']")
LINK_TITLE = (By.CSS_SELECTOR, '#zg_banner_text')

@then('Verify each top link and correct page opens')
def verify_top_links_open(context):
    all_links = context.driver.find_elements(*BESTSELLER_LINKS)

    for links in all_links:
        print(links)
        



