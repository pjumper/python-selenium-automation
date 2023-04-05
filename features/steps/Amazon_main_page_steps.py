from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('Hover over language options')
def hover_lang_options(context):
    context.app.header.hover_lang_options()

@when('Hover over new arrival')
def hover_new_arrival(context):
    context.app.header.hover_new_arrival()

#@then('Verify Spanish option present')

#def verify_lang_shown(context):
    #context.app.header.verify_lang_shown

@then('Verify user sees new arrival products')
def verify_new_arrival_shown(context):
    context.app.header.verify_new_arrival_shown()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)