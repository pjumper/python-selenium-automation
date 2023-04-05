from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Input text {text}')
def input_search_field(context, text):
    context.app.header.input_search_text


@when('Click search button')
def click_search_field(context):
    #context.driver.wait.until(EC.element_to_be_clickable(SEARCH_FIELD_SELECT)).click()
    context.app.header.click_search